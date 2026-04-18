#!/usr/bin/env python3
"""Fetch rendered HTML from Chrome via DevTools Protocol."""

from __future__ import annotations

import json
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path
from typing import Any

import websocket


DEFAULT_CHROME_BINARY = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def _pick_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as handle:
        handle.bind(("127.0.0.1", 0))
        return int(handle.getsockname()[1])


def _wait_for_json(url: str, timeout_seconds: float = 20.0) -> Any:
    deadline = time.time() + timeout_seconds
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # pragma: no cover - network timing dependent
            last_error = exc
            time.sleep(0.5)
    raise RuntimeError(f"Timed out waiting for Chrome DevTools endpoint: {last_error}")


def _wait_for_page_target(port: int, timeout_seconds: float = 20.0) -> dict[str, Any]:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        targets = _wait_for_json(f"http://127.0.0.1:{port}/json/list", timeout_seconds=5.0)
        for target in targets:
            if target.get("type") == "page" and target.get("webSocketDebuggerUrl"):
                return target
        time.sleep(0.5)
    raise RuntimeError("Timed out waiting for a Chrome page target.")


class _CDPSession:
    def __init__(self, websocket_url: str) -> None:
        self._socket = websocket.create_connection(websocket_url, timeout=20)
        self._next_id = 1

    def close(self) -> None:
        self._socket.close()

    def send(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        message_id = self._next_id
        self._next_id += 1
        self._socket.send(
            json.dumps(
                {
                    "id": message_id,
                    "method": method,
                    "params": params or {},
                }
            )
        )
        while True:
            payload = json.loads(self._socket.recv())
            if payload.get("id") == message_id:
                if "error" in payload:
                    raise RuntimeError(f"CDP error for {method}: {payload['error']}")
                return payload.get("result", {})


def _extract_html(session: _CDPSession, url: str, delay_seconds: int) -> str:
    session.send("Page.navigate", {"url": url})
    time.sleep(delay_seconds)
    html = (
        session.send(
            "Runtime.evaluate",
            {
                "expression": "document.documentElement.outerHTML",
                "returnByValue": True,
            },
        )
        .get("result", {})
        .get("value", "")
    )
    if html and "<html" in html.lower() and html.strip() != "<html><head></head><body></body></html>":
        return html
    raise RuntimeError("Chrome returned an empty or invalid HTML document.")


def _find_chrome_binary(chrome_binary: str | None = None) -> str:
    if chrome_binary:
        return chrome_binary
    if Path(DEFAULT_CHROME_BINARY).exists():
        return DEFAULT_CHROME_BINARY
    resolved = shutil.which("google-chrome") or shutil.which("chrome")
    if resolved:
        return resolved
    raise FileNotFoundError("Google Chrome binary not found.")


class ChromeFetcher:
    """Reusable Chrome DevTools fetch session."""

    def __init__(self, chrome_binary: str | None = None) -> None:
        self.chrome_binary = chrome_binary
        self.port: int | None = None
        self.profile_dir: tempfile.TemporaryDirectory[str] | None = None
        self.process: subprocess.Popen[str] | None = None
        self.session: _CDPSession | None = None

    def __enter__(self) -> "ChromeFetcher":
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def start(self) -> None:
        if self.session is not None:
            return
        self.port = _pick_free_port()
        self.profile_dir = tempfile.TemporaryDirectory(prefix="gansu-chrome-profile-")
        launch_args = [
            _find_chrome_binary(self.chrome_binary),
            f"--remote-debugging-port={self.port}",
            f"--user-data-dir={self.profile_dir.name}",
            "--no-first-run",
            "--no-default-browser-check",
            "--remote-allow-origins=*",
            "about:blank",
        ]

        self.process = subprocess.Popen(
            launch_args,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        _wait_for_json(f"http://127.0.0.1:{self.port}/json/version")
        target = _wait_for_page_target(self.port)
        websocket_url = target["webSocketDebuggerUrl"]
        self.session = _CDPSession(websocket_url)
        self.session.send("Page.enable")
        self.session.send("Runtime.enable")

    def fetch(self, url: str, delay_seconds: int = 15) -> str:
        if self.session is None:
            self.start()
        if self.session is None:
            raise RuntimeError("Chrome session did not start.")
        return _extract_html(self.session, url, delay_seconds=delay_seconds)

    def close(self) -> None:
        if self.session is not None:
            try:
                self.session.close()
            except Exception:
                pass
            self.session = None
        if self.process is not None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
        if self.profile_dir is not None:
            self.profile_dir.cleanup()
            self.profile_dir = None


def fetch_source(
    url: str,
    delay_seconds: int = 8,
    retries: int = 1,
    chrome_binary: str | None = None,
) -> str:
    """Open a URL in Chrome and return rendered HTML via DevTools Protocol."""

    last_error: RuntimeError | None = None
    for _ in range(retries + 1):
        chrome_fetcher: ChromeFetcher | None = None
        try:
            chrome_fetcher = ChromeFetcher(chrome_binary=chrome_binary)
            chrome_fetcher.start()
            return chrome_fetcher.fetch(url, delay_seconds=delay_seconds)
        except Exception as exc:  # pragma: no cover - browser timing dependent
            last_error = RuntimeError(str(exc))
        finally:
            if chrome_fetcher is not None:
                chrome_fetcher.close()
            time.sleep(1)

    raise last_error or RuntimeError("Chrome fetch failed.")
