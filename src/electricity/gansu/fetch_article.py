#!/usr/bin/env python3
"""Fetch and parse one Gansu electricity bulletin article."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from chrome_cdp_fetch import fetch_source


TITLE_MONTH_PATTERN = re.compile(r"(\d{4})年(\d{1,2})月")
MONTHLY_PATTERNS = [
    re.compile(r"(?P<month>\d{1,2})月(?:当月|[，,])?(?:全省)?全社会用电量(?P<value>[0-9]+(?:\.[0-9]+)?)亿千瓦时"),
    re.compile(r"当月(?:[，,])?(?:全省)?全社会用电量(?P<value>[0-9]+(?:\.[0-9]+)?)亿千瓦时"),
    re.compile(r"(?:全省)?全社会用电量(?P<value>[0-9]+(?:\.[0-9]+)?)亿千瓦时"),
]
YTD_PATTERNS = [
    re.compile(r"1-(?P<month>\d{1,2})月[，,]?(?:全省)?全社会用电量累计(?:为)?(?P<value>[0-9]+(?:\.[0-9]+)?)亿千瓦时"),
    re.compile(r"1-(?P<month>\d{1,2})月[，,]?(?:全省)?全社会累计用电量(?P<value>[0-9]+(?:\.[0-9]+)?)亿千瓦时"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and parse a Gansu electricity bulletin article.")
    parser.add_argument("--url", required=True, help="Article URL.")
    parser.add_argument("--delay", type=int, default=8, help="Seconds to wait for Chrome to render the article page.")
    parser.add_argument("--output", help="Optional output JSON path.")
    parser.add_argument("--save-html", help="Optional path to save raw rendered HTML.")
    return parser.parse_args()


def text_or_empty(node) -> str:
    return "" if node is None else node.get_text(" ", strip=True)


def compact_text(value: str) -> str:
    return re.sub(r"\s+", "", value)


def first_match(
    patterns: list[re.Pattern[str]],
    text: str,
    title_month: int | None,
    allow_month_fallback: bool = False,
) -> tuple[int | None, float | None]:
    for index, pattern in enumerate(patterns):
        match = pattern.search(text)
        if not match:
            continue
        month_value = match.groupdict().get("month")
        if month_value is None and not allow_month_fallback:
            continue
        month = int(month_value) if month_value is not None else title_month
        value = float(match.group("value"))
        return month, value
    return None, None


def extract_metrics_from_text(text: str, title_month: int | None) -> dict[str, int | float | None]:
    monthly_sentence_month, monthly_kwh = first_match(
        MONTHLY_PATTERNS,
        text,
        title_month=title_month,
        allow_month_fallback=True,
    )
    ytd_sentence_month, ytd_kwh = first_match(
        YTD_PATTERNS,
        text,
        title_month=title_month,
    )
    if ytd_kwh is None and title_month == 1 and monthly_kwh is not None:
        ytd_sentence_month = 1
        ytd_kwh = monthly_kwh
    return {
        "monthly_kwh_100m": monthly_kwh,
        "monthly_kwh_sentence_month": monthly_sentence_month,
        "ytd_kwh_100m": ytd_kwh,
        "ytd_kwh_sentence_month": ytd_sentence_month,
    }


def parse_article(html: str, url: str) -> dict[str, object]:
    soup = BeautifulSoup(html, "html.parser")
    content_text = ""
    for selector in [".nr-003", ".v_news_content", "#vsb_content", ".arc-con", 'meta[name="Description"]']:
        node = soup.select_one(selector)
        if node is None:
            continue
        if selector.startswith("meta"):
            candidate = (node.get("content") or "").strip()
        else:
            candidate = text_or_empty(node)
        if candidate and len(compact_text(candidate)) > len(compact_text(content_text)):
            content_text = candidate

    title = ""
    title_meta = soup.select_one('meta[name="ArticleTitle"]')
    if title_meta is not None:
        title = (title_meta.get("content") or "").strip()
    if not title:
        title = text_or_empty(soup.select_one(".nr-001 h1"))

    pub_date = ""
    pub_meta = soup.select_one('meta[name="PubDate"]')
    if pub_meta is not None:
        pub_date = (pub_meta.get("content") or "").strip()

    content_source = ""
    source_meta = soup.select_one('meta[name="ContentSource"]')
    if source_meta is not None:
        content_source = (source_meta.get("content") or "").strip()

    normalized_text = compact_text(content_text)
    title_month_match = TITLE_MONTH_PATTERN.search(title)
    title_month = int(title_month_match.group(2)) if title_month_match else None
    lead_text = normalized_text[:800]
    metrics = extract_metrics_from_text(lead_text, title_month=title_month)

    parsed = {
        "url": url,
        "title": title,
        "pub_date": pub_date,
        "content_source": content_source,
        "content_text": content_text,
        "content_text_compact": normalized_text,
        "title_year": int(title_month_match.group(1)) if title_month_match else None,
        "title_month": title_month,
        "monthly_kwh_100m": metrics["monthly_kwh_100m"],
        "monthly_kwh_sentence_month": metrics["monthly_kwh_sentence_month"],
        "ytd_kwh_100m": metrics["ytd_kwh_100m"],
        "ytd_kwh_sentence_month": metrics["ytd_kwh_sentence_month"],
    }
    return parsed


def main() -> None:
    args = parse_args()
    html = fetch_source(args.url, delay_seconds=args.delay)

    if args.save_html:
        save_html_path = Path(args.save_html)
        save_html_path.parent.mkdir(parents=True, exist_ok=True)
        save_html_path.write_text(html, encoding="utf-8")

    parsed = parse_article(html, args.url)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(parsed, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
