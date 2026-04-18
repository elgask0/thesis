#!/usr/bin/env python3
"""Discover Gansu electricity bulletins from the search-results page."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from bs4 import BeautifulSoup

from chrome_cdp_fetch import fetch_source


DEFAULT_SEARCH_URL = (
    "https://gxt.gansu.gov.cn/guestweb4/s?"
    "searchWord=%25E5%2585%25A8%25E7%259C%2581%25E7%2594%25B5%25E5%258A%259B%25E7%2594%259F"
    "%25E4%25BA%25A7%25E8%25BF%2590%25E8%25A1%258C%25E6%2583%2585%25E5%2586%25B5&"
    "column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=0&orderBy=1&startTime=&endTime=&"
    "pageSize=10&pageNum=0&timeStamp=0&siteCode=6200000082&sonSiteCode=&checkHandle=1&"
    "strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&"
    "topical=&pubName=&countKey=0&uc=0&isSonSite=false&left_right_index=0"
)
TITLE_PATTERN = re.compile(r"^\d{4}年\d{1,2}月全省电力生产运行情况$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover Gansu electricity bulletin candidates.")
    parser.add_argument("--search-url", default=DEFAULT_SEARCH_URL, help="Gansu search-results URL.")
    parser.add_argument("--delay", type=int, default=15, help="Seconds to wait for Chrome to render the search page.")
    parser.add_argument("--output", required=True, help="Output CSV or JSON path.")
    parser.add_argument("--save-html", help="Optional path to save raw rendered HTML.")
    parser.add_argument("--page-num", type=int, default=0, help="Search-results page number.")
    parser.add_argument("--page-size", type=int, default=10, help="Search-results page size.")
    parser.add_argument(
        "--strict-title",
        action="store_true",
        help="Keep only titles matching YYYY年M月全省电力生产运行情况.",
    )
    return parser.parse_args()


def parse_results(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    results: list[dict[str, str]] = []
    for block in soup.select("div.wordGuide"):
        anchor = block.select_one("a.titleSelf")
        if anchor is None:
            continue
        title = anchor.get("title", "").strip() or anchor.get_text(" ", strip=True)
        title = re.sub(r"\s+", "", title)
        summary = ""
        summary_node = block.select_one("p.summaryFont")
        if summary_node is not None:
            summary = summary_node.get_text(" ", strip=True)
        source_name = ""
        source_anchor = block.select_one("p.time a.sourceDateFont")
        if source_anchor is not None:
            source_name = source_anchor.get_text(" ", strip=True)
        pub_date = ""
        date_nodes = block.select("p.time .sourceDateFont")
        if date_nodes:
            pub_date = date_nodes[-1].get_text(" ", strip=True)
        column_name = ""
        column_node = block.select_one(".columnLabel")
        if column_node is not None:
            column_name = column_node.get_text(" ", strip=True)
        results.append(
            {
                "title": title,
                "article_url": anchor.get("href", "").strip().replace("http://", "https://"),
                "pub_date": pub_date,
                "source_name": source_name,
                "column_name": column_name,
                "summary": summary,
            }
        )
    return results


def build_search_url(search_url: str, page_num: int, page_size: int) -> str:
    parts = urlsplit(search_url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query["pageNum"] = str(page_num)
    query["pageSize"] = str(page_size)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def write_output(results: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() == ".json":
        output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    fieldnames = ["title", "article_url", "pub_date", "source_name", "column_name", "summary"]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main() -> None:
    args = parse_args()
    page_url = build_search_url(args.search_url, page_num=args.page_num, page_size=args.page_size)
    html = fetch_source(page_url, delay_seconds=args.delay)
    if args.save_html:
        Path(args.save_html).write_text(html, encoding="utf-8")

    results = parse_results(html)
    if args.strict_title:
        results = [item for item in results if TITLE_PATTERN.match(item["title"])]

    write_output(results, Path(args.output))
    print(f"Discovered {len(results)} Gansu bulletin candidates on page {args.page_num}.")


if __name__ == "__main__":
    main()
