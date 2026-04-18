#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import requests


DEFAULT_USER_ID = os.environ.get("ZOTERO_USER_ID", "18036970")
DEFAULT_API_KEY = os.environ.get("ZOTERO_API_KEY", "")
DEFAULT_TIMEOUT = 60


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json_payload(path: str) -> Any:
    if path == "-":
        return json.loads(sys.stdin.read())
    return json.loads(Path(path).read_text())


def dump_json(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


class ZoteroClient:
    def __init__(self, user_id: str, api_key: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        if not api_key:
            fail("Missing Zotero API key. Set ZOTERO_API_KEY first.")
        self.base = f"https://api.zotero.org/users/{user_id}"
        self.timeout = timeout
        self.headers = {
            "Zotero-API-Key": api_key,
            "Zotero-API-Version": "3",
        }

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = path if path.startswith("http") else f"{self.base}{path}"
        last_response: requests.Response | None = None
        last_error: Exception | None = None

        for attempt in range(1, 6):
            try:
                response = requests.request(method, url, timeout=self.timeout, **kwargs)
                if response.status_code in {409, 429, 500, 502, 503, 504}:
                    last_response = response
                    time.sleep(attempt * 2)
                    continue
                response.raise_for_status()
                return response
            except requests.RequestException as exc:
                last_error = exc
                time.sleep(attempt * 2)

        if last_response is not None:
            fail(f"{method} {url} failed: {last_response.status_code} {last_response.text}")
        if last_error is not None:
            fail(f"{method} {url} failed: {last_error}")
        fail(f"{method} {url} failed for an unknown reason")

    def get_item(self, key: str) -> dict[str, Any]:
        return self.request("GET", f"/items/{key}", headers=self.headers, params={"format": "json"}).json()

    def children(self, key: str) -> list[dict[str, Any]]:
        return self.request("GET", f"/items/{key}/children", headers=self.headers, params={"format": "json"}).json()

    def top(self, start: int = 0, limit: int = 25) -> list[dict[str, Any]]:
        params = {"format": "json", "start": start, "limit": limit}
        return self.request("GET", "/items/top", headers=self.headers, params=params).json()

    def all_top(self, page_size: int = 100) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        start = 0
        while True:
            page = self.top(start=start, limit=page_size)
            if not page:
                break
            items.extend(page)
            if len(page) < page_size:
                break
            start += page_size
        return items

    def search(self, query: str, limit: int = 25, top: bool = False) -> list[dict[str, Any]]:
        endpoint = "/items/top" if top else "/items"
        params = {"format": "json", "q": query, "limit": limit}
        return self.request("GET", endpoint, headers=self.headers, params=params).json()

    def create(self, payload: Any) -> list[dict[str, Any]]:
        items = payload if isinstance(payload, list) else [payload]
        headers = dict(self.headers)
        headers["Content-Type"] = "application/json"
        headers["Zotero-Write-Token"] = uuid.uuid4().hex[:16]
        response = self.request("POST", "/items", headers=headers, data=json.dumps(items, ensure_ascii=False))
        created = response.json().get("successful", {})
        return [self.get_item(meta["key"]) for meta in created.values()]

    def patch(self, key: str, changes: dict[str, Any]) -> dict[str, Any]:
        current = self.get_item(key)
        payload = copy.deepcopy(current["data"])
        payload.update(changes)
        payload.pop("key", None)
        payload.pop("version", None)
        headers = dict(self.headers)
        headers["Content-Type"] = "application/json"
        headers["If-Unmodified-Since-Version"] = str(current["version"])
        self.request("PATCH", f"/items/{key}", headers=headers, data=json.dumps(payload, ensure_ascii=False))
        return self.get_item(key)

    def delete(self, key: str) -> dict[str, str]:
        current = self.get_item(key)
        headers = dict(self.headers)
        headers["If-Unmodified-Since-Version"] = str(current["version"])
        self.request("DELETE", f"/items/{key}", headers=headers)
        return {"deleted": key}

    def register_upload(self, attachment_key: str, file_path: Path) -> dict[str, Any]:
        data = {
            "md5": hashlib.md5(file_path.read_bytes()).hexdigest(),
            "filename": file_path.name,
            "filesize": str(file_path.stat().st_size),
            "mtime": str(int(file_path.stat().st_mtime * 1000)),
        }
        headers = dict(self.headers)
        headers["If-None-Match"] = "*"
        response = self.request("POST", f"/items/{attachment_key}/file", headers=headers, data=data)
        if not response.text.strip():
            return {"exists": True}
        return response.json()

    def upload_file(self, auth: dict[str, Any], file_path: Path) -> None:
        if auth.get("exists"):
            return
        last_error: Exception | None = None
        for attempt in range(1, 6):
            try:
                with file_path.open("rb") as handle:
                    files = {"file": (file_path.name, handle, "application/pdf")}
                    response = requests.post(auth["url"], data=auth["params"], files=files, timeout=180)
                    response.raise_for_status()
                    return
            except requests.RequestException as exc:
                last_error = exc
                time.sleep(attempt * 2)
        if last_error is not None:
            fail(f"Upload failed for {file_path}: {last_error}")
        fail(f"Upload failed for {file_path}")

    def attach_pdf(self, parent_key: str, file_path: Path, title: str = "Full Text PDF") -> dict[str, Any]:
        if not file_path.exists():
            fail(f"PDF not found: {file_path}")
        item = {
            "itemType": "attachment",
            "parentItem": parent_key,
            "linkMode": "imported_file",
            "title": title,
            "contentType": "application/pdf",
            "filename": file_path.name,
        }
        created = self.create(item)[0]
        auth = self.register_upload(created["key"], file_path)
        self.upload_file(auth, file_path)
        return self.get_item(created["key"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Zotero Web API helper for thesis repo workflows")
    parser.add_argument("--user-id", default=DEFAULT_USER_ID)
    parser.add_argument("--api-key", default=DEFAULT_API_KEY)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)

    subparsers = parser.add_subparsers(dest="command", required=True)

    get_cmd = subparsers.add_parser("get", help="Fetch one item")
    get_cmd.add_argument("key")

    children_cmd = subparsers.add_parser("children", help="Fetch child items for a parent item")
    children_cmd.add_argument("key")

    top_cmd = subparsers.add_parser("top", help="Fetch one page of top-level items")
    top_cmd.add_argument("--start", type=int, default=0)
    top_cmd.add_argument("--limit", type=int, default=25)

    all_top_cmd = subparsers.add_parser("all-top", help="Fetch all top-level items")
    all_top_cmd.add_argument("--page-size", type=int, default=100)

    search_cmd = subparsers.add_parser("search", help="Search Zotero items")
    search_cmd.add_argument("query")
    search_cmd.add_argument("--limit", type=int, default=25)
    search_cmd.add_argument("--top", action="store_true")

    create_cmd = subparsers.add_parser("create", help="Create one or more items from a JSON payload")
    create_cmd.add_argument("payload", help="JSON file path or - for stdin")

    patch_cmd = subparsers.add_parser("patch", help="Patch one item with a JSON dict of field changes")
    patch_cmd.add_argument("key")
    patch_cmd.add_argument("changes", help="JSON file path or - for stdin")

    delete_cmd = subparsers.add_parser("delete", help="Delete one item")
    delete_cmd.add_argument("key")
    delete_cmd.add_argument("--yes", action="store_true", help="Required confirmation flag")

    attach_cmd = subparsers.add_parser("attach-pdf", help="Create an imported PDF attachment on a parent item")
    attach_cmd.add_argument("parent_key")
    attach_cmd.add_argument("file_path")
    attach_cmd.add_argument("--title", default="Full Text PDF")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    client = ZoteroClient(user_id=args.user_id, api_key=args.api_key, timeout=args.timeout)

    if args.command == "get":
        dump_json(client.get_item(args.key))
        return

    if args.command == "children":
        dump_json(client.children(args.key))
        return

    if args.command == "top":
        dump_json(client.top(start=args.start, limit=args.limit))
        return

    if args.command == "all-top":
        dump_json(client.all_top(page_size=args.page_size))
        return

    if args.command == "search":
        dump_json(client.search(args.query, limit=args.limit, top=args.top))
        return

    if args.command == "create":
        dump_json(client.create(load_json_payload(args.payload)))
        return

    if args.command == "patch":
        changes = load_json_payload(args.changes)
        if not isinstance(changes, dict):
            fail("Patch payload must be a JSON object of field changes.")
        dump_json(client.patch(args.key, changes))
        return

    if args.command == "delete":
        if not args.yes:
            fail("Refusing to delete without --yes.")
        dump_json(client.delete(args.key))
        return

    if args.command == "attach-pdf":
        dump_json(client.attach_pdf(args.parent_key, Path(args.file_path), title=args.title))
        return

    fail(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
