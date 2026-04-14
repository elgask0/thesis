#!/usr/bin/env python3
"""Rebuild the parsed Gansu panel from saved discovery and raw HTML files."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from fetch_article import compact_text, extract_metrics_from_text, parse_article
from scrape_all import save_panel_csv, slugify_article


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rebuild Gansu panel data from saved raw HTML files.")
    parser.add_argument(
        "--discovery-csv",
        default="03_data/interim/gansu_scrape/gansu_discovery.csv",
        help="Discovery CSV created by scrape_all.py.",
    )
    parser.add_argument(
        "--raw-html-dir",
        default="03_data/raw/electricity_bulletins/gansu",
        help="Directory containing raw Gansu bulletin HTML files.",
    )
    parser.add_argument(
        "--parsed-dir",
        default="03_data/interim/gansu_scrape/articles",
        help="Directory for parsed article JSON outputs.",
    )
    parser.add_argument(
        "--panel-csv",
        default="03_data/interim/gansu_scrape/gansu_monthly_kwh.csv",
        help="Output panel CSV path.",
    )
    parser.add_argument("--engine-label", default="chrome", help="Engine label to store in the panel.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    discovery_rows = list(csv.DictReader(Path(args.discovery_csv).open()))
    raw_html_dir = Path(args.raw_html_dir)
    parsed_dir = Path(args.parsed_dir)
    parsed_dir.mkdir(parents=True, exist_ok=True)

    panel_rows: list[dict[str, object]] = []
    for row in discovery_rows:
        article_url = row["article_url"]
        slug = slugify_article(article_url)
        matching_html_files = sorted(raw_html_dir.glob(f"*__{slug}.html"))
        if not matching_html_files:
            raise FileNotFoundError(f"No raw HTML file found for {article_url}")
        raw_html_path = matching_html_files[0]
        html = raw_html_path.read_text(encoding="utf-8")
        parsed = parse_article(html, article_url)
        summary_text = row.get("summary", "")
        monthly_method = "article_text" if parsed.get("monthly_kwh_100m") is not None else ""
        ytd_method = "article_text" if parsed.get("ytd_kwh_100m") is not None else ""
        if parsed.get("monthly_kwh_100m") is None and summary_text:
            fallback_metrics = extract_metrics_from_text(
                compact_text(summary_text),
                title_month=parsed.get("title_month"),
            )
            if fallback_metrics.get("monthly_kwh_100m") is not None:
                parsed.update(fallback_metrics)
                parsed["summary_fallback_text"] = summary_text
                parsed["used_summary_fallback"] = True
                monthly_method = "search_summary"
                if fallback_metrics.get("ytd_kwh_100m") is not None:
                    ytd_method = "search_summary"

        title_year = parsed.get("title_year")
        title_month = parsed.get("title_month")
        year_month = ""
        if isinstance(title_year, int) and isinstance(title_month, int):
            year_month = f"{title_year:04d}-{title_month:02d}"

        parsed_json_path = parsed_dir / f"{year_month or 'unknown'}__{slug}.json"
        parsed_json_path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2), encoding="utf-8")

        panel_rows.append(
            {
                "province": "Gansu",
                "year_month": year_month,
                "title": parsed.get("title"),
                "article_url": article_url,
                "pub_date": parsed.get("pub_date"),
                "content_source": parsed.get("content_source"),
                "monthly_kwh_100m": parsed.get("monthly_kwh_100m"),
                "monthly_kwh_method": monthly_method,
                "ytd_kwh_100m": parsed.get("ytd_kwh_100m"),
                "ytd_kwh_method": ytd_method,
                "raw_html_file": str(raw_html_path),
                "parsed_json_file": str(parsed_json_path),
                "engine": args.engine_label,
            }
        )

    panel_rows.sort(key=lambda row: str(row["year_month"]))
    for index, row in enumerate(panel_rows):
        if row["monthly_kwh_100m"] is not None:
            continue
        if index == 0 or index == len(panel_rows) - 1:
            continue
        prev_row = panel_rows[index - 1]
        next_row = panel_rows[index + 1]
        prev_ytd = prev_row.get("ytd_kwh_100m")
        next_ytd = next_row.get("ytd_kwh_100m")
        next_monthly = next_row.get("monthly_kwh_100m")
        if prev_ytd is None or next_ytd is None or next_monthly is None:
            continue
        row["monthly_kwh_100m"] = round(float(next_ytd) - float(next_monthly) - float(prev_ytd), 2)
        row["monthly_kwh_method"] = "derived_from_neighbor_ytd"

    save_panel_csv(panel_rows, Path(args.panel_csv))
    print(f"Rebuilt {len(panel_rows)} Gansu panel rows from saved HTML.")


if __name__ == "__main__":
    main()
