#!/usr/bin/env python3
"""Validate the saved Gansu electricity bulletin data artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Gansu electricity data artifacts.")
    parser.add_argument(
        "--base-panel",
        default="03_data/interim/gansu_scrape/gansu_monthly_kwh.csv",
        help="Canonical monthly Gansu panel CSV.",
    )
    parser.add_argument(
        "--rich-panel",
        default="03_data/interim/gansu_scrape/gansu_panel_rich.csv",
        help="Wide structured Gansu panel CSV.",
    )
    parser.add_argument(
        "--output",
        default="03_data/interim/gansu_scrape/gansu_validation_report.md",
        help="Markdown validation report path.",
    )
    return parser.parse_args()


def load_csv(path: Path) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding="utf-8")))


def month_range(start_ym: str, end_ym: str) -> list[str]:
    start_year, start_month = map(int, start_ym.split("-"))
    end_year, end_month = map(int, end_ym.split("-"))
    current = date(start_year, start_month, 1)
    end = date(end_year, end_month, 1)
    months: list[str] = []
    while current <= end:
        months.append(f"{current.year:04d}-{current.month:02d}")
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)
    return months


def compact_text(value: str) -> str:
    return re.sub(r"\s+", "", value or "")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def summarize_range(values: list[str]) -> str:
    if not values:
        return "none"
    if len(values) <= 8:
        return ", ".join(values)
    return ", ".join(values[:5]) + f", ... ({len(values)} total)"


def generation_residuals(rich_rows: list[dict[str, str]]) -> list[tuple[str, float]]:
    residuals: list[tuple[str, float]] = []
    component_columns = [
        "generation_hydro_monthly_100m_kwh",
        "generation_thermal_monthly_100m_kwh",
        "generation_wind_monthly_100m_kwh",
        "generation_solar_monthly_100m_kwh",
        "generation_other_monthly_100m_kwh",
    ]
    for row in rich_rows:
        if row["generation_total_monthly_100m_kwh"] in ("", None):
            continue
        component_values = [float(row[col]) for col in component_columns if row[col] not in ("", None)]
        if not component_values:
            continue
        total = float(row["generation_total_monthly_100m_kwh"])
        residual = round(total - sum(component_values), 2)
        if abs(residual) > 0.1:
            residuals.append((row["year_month"], residual))
    return residuals


def main() -> None:
    args = parse_args()
    base_panel_path = Path(args.base_panel)
    rich_panel_path = Path(args.rich_panel)
    output_path = Path(args.output)

    base_rows = load_csv(base_panel_path)
    rich_rows = load_csv(rich_panel_path)
    rich_by_ym = {row["year_month"]: row for row in rich_rows}

    year_months = [row["year_month"] for row in base_rows]
    expected_months = month_range(year_months[0], year_months[-1]) if year_months else []
    missing_months = [ym for ym in expected_months if ym not in set(year_months)]
    duplicate_months = sorted([ym for ym, count in Counter(year_months).items() if count > 1])

    title_mismatches: list[str] = []
    for row in base_rows:
        match = re.search(r"(\d{4})年(\d{1,2})月", row["title"])
        if not match:
            title_mismatches.append(f"{row['year_month']} -> {row['title']}")
            continue
        title_ym = f"{int(match.group(1)):04d}-{int(match.group(2)):02d}"
        if title_ym != row["year_month"]:
            title_mismatches.append(f"{row['year_month']} -> {row['title']}")

    ytd_mismatches: list[str] = []
    for index, row in enumerate(base_rows):
        month = int(row["year_month"].split("-")[1])
        monthly = float(row["monthly_kwh_100m"])
        ytd = float(row["ytd_kwh_100m"])
        if index == 0:
            continue
        if month == 1:
            if abs(monthly - ytd) > 0.02:
                ytd_mismatches.append(f"{row['year_month']} January monthly {monthly} != YTD {ytd}")
            continue
        prev_ytd = float(base_rows[index - 1]["ytd_kwh_100m"])
        if abs(monthly - (ytd - prev_ytd)) > 0.02:
            ytd_mismatches.append(
                f"{row['year_month']} monthly {monthly} != YTD delta {round(ytd - prev_ytd, 2)}"
            )

    sector_sum_mismatches: list[str] = []
    sector_columns = [
        "primary_monthly_kwh_100m",
        "secondary_monthly_kwh_100m",
        "tertiary_monthly_kwh_100m",
        "residential_monthly_kwh_100m",
    ]
    for row in rich_rows:
        if any(row[col] in ("", None) for col in sector_columns):
            continue
        sector_sum = sum(float(row[col]) for col in sector_columns)
        total = float(row["monthly_total_kwh_100m"])
        diff = round(sector_sum - total, 2)
        if abs(diff) > 0.05:
            sector_sum_mismatches.append(f"{row['year_month']} sector sum diff {diff:+.2f}")

    generation_residual_months = generation_residuals(rich_rows)

    article_dir = base_panel_path.parent / "articles"
    duplicate_json_urls: dict[str, list[str]] = defaultdict(list)
    duplicate_json_hashes: dict[str, list[str]] = defaultdict(list)
    template_counter: Counter[str] = Counter()
    section_pattern_counter: Counter[tuple[str, ...]] = Counter()
    text_lengths: list[tuple[str, int]] = []

    markers = ["分产业用电", "分行业用电", "工业用电", "装机规模", "发电量", "平均发电利用小时", "外送", "外购"]
    for path in sorted(article_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        duplicate_json_urls[data["url"]].append(path.name)
        normalized_json = json.dumps(data, ensure_ascii=False, sort_keys=True)
        duplicate_json_hashes[sha256_text(normalized_json)].append(path.name)

    for row in base_rows:
        parsed = json.loads(Path(row["parsed_json_file"]).read_text(encoding="utf-8"))
        text = parsed.get("content_text_compact") or parsed.get("content_text") or ""
        masked = re.sub(r"[0-9]+(?:\.[0-9]+)?", "<N>", text)
        masked = re.sub(r"同比(?:增长|下降)<N>%?", "同比<Y>", masked)
        masked = re.sub(r"环比(?:增长|下降)<N>%?", "环比<M>", masked)
        template_counter[masked] += 1
        section_pattern_counter[tuple(marker for marker in markers if marker in text)] += 1
        text_lengths.append((row["year_month"], len(text)))

    duplicate_json_urls = {
        url: names for url, names in duplicate_json_urls.items() if len(names) > 1
    }
    duplicate_json_hashes = {
        digest: names for digest, names in duplicate_json_hashes.items() if len(names) > 1
    }

    methods = Counter(row["monthly_kwh_method"] for row in base_rows)

    coverage_columns = [
        "monthly_total_kwh_100m",
        "ytd_total_kwh_100m",
        "primary_monthly_kwh_100m",
        "primary_ytd_kwh_100m",
        "industry_total_monthly_kwh_100m",
        "industry_total_ytd_kwh_100m",
        "capacity_total_wan_kw",
        "generation_total_monthly_100m_kwh",
        "generation_total_ytd_100m_kwh",
        "utilization_total_hours",
        "generation_other_monthly_100m_kwh",
        "capacity_biomass_wan_kw",
    ]
    coverage_summary = {
        column: sum(1 for row in rich_rows if row.get(column) not in ("", None))
        for column in coverage_columns
    }

    original_2022_06 = Path("03_data/raw/electricity_bulletins/gansu/2022-06__2081569.html")
    mirror_2022_06 = Path("03_data/raw/electricity_bulletins/gansu/2022-06__33692_tianshui_mirror.html")
    original_text = original_2022_06.read_text(encoding="utf-8")
    mirror_text = mirror_2022_06.read_text(encoding="utf-8")
    original_empty_body = '<div class="nr-003">' in original_text and "<!--Content Start-->" in original_text and "<!--Content End-->" in original_text
    mirror_has_body = 'id="vsb_content"' in mirror_text and "6月当月，全省全社会用电量126.20亿千瓦时" in mirror_text

    lines = [
        "# Gansu Data Validation Report",
        "",
        f"- Base panel: `{base_panel_path}`",
        f"- Rich panel: `{rich_panel_path}`",
        f"- Generated from saved repo artifacts: `{date.today().isoformat()}`",
        "",
        "## Core Checks",
        "",
        f"- Rows in canonical monthly panel: `{len(base_rows)}`",
        f"- Coverage: `{year_months[0]}` to `{year_months[-1]}`",
        f"- Missing months inside the covered span: `{summarize_range(missing_months)}`",
        f"- Duplicate `year_month` rows: `{summarize_range(duplicate_months)}`",
        f"- Title-to-month mismatches: `{summarize_range(title_mismatches)}`",
        f"- Monthly extraction methods: `{dict(methods)}`",
        f"- YTD arithmetic mismatches after the initial `2020-03` entry: `{summarize_range(ytd_mismatches)}`",
        f"- Monthly sector-sum mismatches against total consumption: `{summarize_range(sector_sum_mismatches)}`",
        "",
        "## 2022-06 Source Exception",
        "",
        "- Original Gansu article URL: `https://gxt.gansu.gov.cn/gxt/c107572/202207/2081569.shtml`",
        "- Mirror article URL used in the canonical panel: `https://www.tianshui.gov.cn/gxj/info/1682/33692.htm`",
        f"- Saved original HTML has an empty article body block: `{original_empty_body}`",
        f"- Saved mirror HTML contains the bulletin text and the `126.20` monthly total sentence: `{mirror_has_body}`",
        "",
        "## Filename Audit",
        "",
        f"- Duplicate parsed JSON URL groups: `{len(duplicate_json_urls)}`",
        f"- Duplicate parsed JSON content-hash groups: `{len(duplicate_json_hashes)}`",
    ]

    for url, names in sorted(duplicate_json_urls.items()):
        lines.append(f"- Legacy alias group: `{url}` -> `{names}`")

    lines.extend(
        [
            "",
            "These long `https-...` filenames are legacy alias artifacts from an older URL-sanitized naming scheme. The canonical panel now points to the shorter slug-based files.",
            "",
            "## Template Audit",
            "",
            f"- Unique masked text templates across 72 months: `{len(template_counter)}`",
            f"- Shortest parsed bulletin text: `{min(text_lengths, key=lambda item: item[1])}`",
            f"- Longest parsed bulletin text: `{max(text_lengths, key=lambda item: item[1])}`",
            "",
            "### Section-pattern counts",
        ]
    )
    for combo, count in section_pattern_counter.most_common():
        label = " + ".join(combo) if combo else "(no standard markers)"
        lines.append(f"- `{count}` months: `{label}`")

    lines.extend(
        [
            "",
            "## Rich-Panel Coverage",
            "",
        ]
    )
    for column in coverage_columns:
        lines.append(f"- `{column}`: `{coverage_summary[column]}` non-null months")

    residual_summary = ", ".join(
        f"{year_month} ({residual:+.2f})" for year_month, residual in generation_residual_months[:10]
    )
    max_residual = max(generation_residual_months, key=lambda item: abs(item[1])) if generation_residual_months else None
    lines.extend(
        [
            "",
            "## Generation Residual Audit",
            "",
            f"- Months where published generation source subtotals do not sum to published total generation: `{len(generation_residual_months)}`",
            f"- First residual months: `{residual_summary or 'none'}`",
            f"- Largest residual month: `{max_residual}`",
            "",
            "These residuals are treated as source-level publication behavior unless later process validation shows a parser error. The extractor records only source-explicit category values.",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote validation report to {output_path}")


if __name__ == "__main__":
    main()
