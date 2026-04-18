#!/usr/bin/env python3
"""End-to-end Gansu bulletin scraping pipeline."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from chrome_cdp_fetch import ChromeFetcher
from discover_bulletins import DEFAULT_SEARCH_URL, TITLE_PATTERN, build_search_url, parse_results
from fetch_article import parse_article


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape all available Gansu electricity bulletins.")
    parser.add_argument("--search-delay", type=int, default=15, help="Seconds to wait for Chrome to render search pages.")
    parser.add_argument("--article-delay", type=int, default=8, help="Seconds to wait for Chrome to render article pages.")
    parser.add_argument("--search-url", default=DEFAULT_SEARCH_URL, help="Base search URL.")
    parser.add_argument("--page-size", type=int, default=10, help="Search-results page size.")
    parser.add_argument("--max-pages", type=int, default=50, help="Maximum pages to probe.")
    parser.add_argument(
        "--output-dir",
        default="03_data/interim/gansu_scrape",
        help="Directory for discovery and parsed outputs.",
    )
    parser.add_argument(
        "--raw-html-dir",
        default="03_data/raw/electricity_bulletins/gansu",
        help="Directory for raw article HTML snapshots.",
    )
    return parser.parse_args()


def discover_all(
    fetch_html,
    search_url: str,
    page_size: int,
    max_pages: int,
) -> list[dict[str, object]]:
    seen_urls: set[str] = set()
    discovered: list[dict[str, object]] = []
    duplicate_streak = 0

    for page_num in range(max_pages):
        page_url = build_search_url(search_url, page_num=page_num, page_size=page_size)
        html = fetch_html(page_url)
        results = [row for row in parse_results(html) if TITLE_PATTERN.match(row["title"])]
        if not results:
            break

        new_rows = []
        for row in results:
            article_url = row["article_url"]
            if article_url in seen_urls:
                continue
            seen_urls.add(article_url)
            row_with_page = dict(row)
            row_with_page["page_num"] = page_num
            new_rows.append(row_with_page)

        if not new_rows:
            duplicate_streak += 1
            if duplicate_streak >= 2:
                break
            continue

        duplicate_streak = 0
        discovered.extend(new_rows)

    return discovered


def slugify_article(url: str) -> str:
    path = urlsplit(url).path.rstrip("/")
    stem = Path(path).stem
    if stem:
        return stem
    return re.sub(r"[^a-zA-Z0-9]+", "-", url).strip("-")


def save_discovery_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["page_num", "title", "article_url", "pub_date", "source_name", "column_name", "summary"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_panel_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "province",
        "year_month",
        "title",
        "article_url",
        "source_url_used",
        "source_note",
        "pub_date",
        "content_source",
        "monthly_kwh_100m",
        "monthly_kwh_method",
        "ytd_kwh_100m",
        "ytd_kwh_method",
        "raw_html_file",
        "parsed_json_file",
        "engine",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    raw_html_dir = Path(args.raw_html_dir)
    parsed_dir = output_dir / "articles"
    discovery_csv = output_dir / "gansu_discovery.csv"
    panel_csv = output_dir / "gansu_monthly_kwh.csv"

    with ChromeFetcher() as chrome_fetcher:
        def fetch_search_html(url: str) -> str:
            return chrome_fetcher.fetch(url, delay_seconds=args.search_delay)

        def fetch_article_html(url: str) -> str:
            return chrome_fetcher.fetch(url, delay_seconds=args.article_delay)

        discovered = discover_all(
            fetch_html=fetch_search_html,
            search_url=args.search_url,
            page_size=args.page_size,
            max_pages=args.max_pages,
        )
        save_discovery_csv(discovered, discovery_csv)

        panel_rows: list[dict[str, object]] = []
        for row in discovered:
            article_url = str(row["article_url"])
            html = fetch_article_html(article_url)
            parsed = parse_article(html, article_url)

            title_year = parsed.get("title_year")
            title_month = parsed.get("title_month")
            year_month = ""
            if isinstance(title_year, int) and isinstance(title_month, int):
                year_month = f"{title_year:04d}-{title_month:02d}"

            slug = slugify_article(article_url)
            raw_html_path = raw_html_dir / f"{year_month or 'unknown'}__{slug}.html"
            parsed_json_path = parsed_dir / f"{year_month or 'unknown'}__{slug}.json"
            raw_html_path.parent.mkdir(parents=True, exist_ok=True)
            parsed_json_path.parent.mkdir(parents=True, exist_ok=True)
            raw_html_path.write_text(html, encoding="utf-8")
            parsed_json_path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")

            panel_rows.append(
                {
                    "province": "Gansu",
                    "year_month": year_month,
                    "title": parsed.get("title"),
                    "article_url": article_url,
                    "source_url_used": article_url,
                    "source_note": "",
                    "pub_date": parsed.get("pub_date"),
                    "content_source": parsed.get("content_source"),
                    "monthly_kwh_100m": parsed.get("monthly_kwh_100m"),
                    "monthly_kwh_method": "article_text" if parsed.get("monthly_kwh_100m") is not None else "",
                    "ytd_kwh_100m": parsed.get("ytd_kwh_100m"),
                    "ytd_kwh_method": "article_text" if parsed.get("ytd_kwh_100m") is not None else "",
                    "raw_html_file": str(raw_html_path),
                    "parsed_json_file": str(parsed_json_path),
                    "engine": "chrome",
                }
            )

    panel_rows.sort(key=lambda row: str(row["year_month"]))
    save_panel_csv(panel_rows, panel_csv)
    print(
        "Scraped "
        f"{len(panel_rows)} Gansu bulletins. "
        f"Discovery: {discovery_csv}. Panel: {panel_csv}."
    )


if __name__ == "__main__":
    main()
