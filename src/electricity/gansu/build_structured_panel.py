#!/usr/bin/env python3
"""Build a wide structured Gansu panel from parsed bulletin JSON files."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


NUMBER = r"([0-9]+(?:\.[0-9]+)?)"
NAMED_NUMBER = r"(?P<value>[0-9]+(?:\.[0-9]+)?)"


EXPORT_MONTHLY_PATTERNS = [
    re.compile(rf"(?:当月|(?P<month>\d{{1,2}})月(?:当月)?)[，,:：]?(?:预计)?全省外送(?:电量)?{NAMED_NUMBER}亿千瓦时"),
]
EXPORT_YTD_PATTERNS = [
    re.compile(rf"1-(?P<month>\d{{1,2}})月[，,:：]?(?:预计)?全省累计外送(?:电量)?{NAMED_NUMBER}亿千瓦时"),
]
IMPORT_MONTHLY_PATTERNS = [
    re.compile(rf"(?:当月|(?P<month>\d{{1,2}})月(?:当月)?)[，,:：]?(?:预计)?全省(?:外购电量|购入电量){NAMED_NUMBER}亿千瓦时"),
]
IMPORT_YTD_PATTERNS = [
    re.compile(rf"1-(?P<month>\d{{1,2}})月[，,:：]?(?:预计)?全省累计(?:外购电量|购入电量){NAMED_NUMBER}亿千瓦时"),
]


SECTOR_LABELS = {
    "primary": ["第一产业用电量"],
    "secondary": ["第二产业用电量"],
    "tertiary": ["第三产业用电量"],
    "residential": ["城乡居民生活用电量", "居民生活用电量"],
}

INDUSTRY_YTD_LABELS = {
    "agriculture": ["农林牧渔业用电"],
    "irrigation": ["排灌用电"],
    "industry_total": ["工业用电"],
    "construction": ["建筑业用电"],
    "transport_post": ["交通运输、仓储和邮政业用电"],
    "it_services": ["信息传输、软件和信息技术服务业用电"],
    "wholesale_retail": ["批发和零售业用电"],
    "accommodation_catering": ["住宿和餐饮业用电"],
    "finance": ["金融业用电"],
    "real_estate": ["房地产业用电"],
    "leasing_business": ["租赁和商业服务业用电"],
    "public_services": ["公共服务及管理组织用电"],
}

INDUSTRIAL_SUBSECTOR_LABELS = {
    "industry_total": ["工业用电", "工业用电量"],
    "nonferrous": ["有色金属冶炼和压延加工业用电"],
    "aluminum": ["铝冶炼用电"],
    "ferrous": ["黑色金属冶炼和压延加工业用电"],
    "ferroalloy": ["铁合金冶炼用电"],
    "steel": ["钢铁用电"],
    "chemical": ["化学原料和化学制品制造业用电"],
    "calcium_carbide": ["电石"],
    "nonmetal_mineral": ["非金属矿物制品业用电"],
    "cement": ["水泥制造业用电", "水泥用电"],
    "petroleum_coal": ["石油、煤炭及其他燃料加工业用电"],
}

CAPACITY_LABELS = {
    "total": ["发电装机容量", "装机容量"],
    "hydro": ["水电"],
    "thermal": ["火电"],
    "wind": ["风电"],
    "solar": ["太阳能", "光伏发电"],
    "storage": ["储能"],
    "biomass": ["生物质"],
}

GENERATION_LABELS = {
    "total": ["全省完成发电量"],
    "hydro": ["水电"],
    "thermal": ["火电"],
    "wind": ["风电"],
    "solar": ["光电"],
    "other": ["其他（储能、生物质）", "其他(储能、生物质)"],
}

UTILIZATION_LABELS = {
    "total": ["平均利用小时数累计为", "平均利用小时数为"],
    "hydro": ["水电"],
    "thermal": ["火电"],
    "wind": ["风电"],
    "solar": ["光电"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a wide structured Gansu monthly panel.")
    parser.add_argument(
        "--base-panel",
        default="03_data/interim/gansu_scrape/gansu_monthly_kwh.csv",
        help="Base panel CSV with parsed JSON file paths.",
    )
    parser.add_argument(
        "--output",
        default="03_data/interim/gansu_scrape/gansu_panel_rich.csv",
        help="Output CSV path for the wide structured panel.",
    )
    parser.add_argument(
        "--coverage-output",
        default="03_data/interim/gansu_scrape/gansu_panel_rich_coverage.csv",
        help="Output CSV path for coverage summary.",
    )
    return parser.parse_args()


def compact_text(value: str) -> str:
    return re.sub(r"\s+", "", value or "")


def first_index(text: str, markers: list[str], start: int = 0) -> int:
    positions = [text.find(marker, start) for marker in markers if text.find(marker, start) != -1]
    return min(positions) if positions else -1


def extract_section(text: str, start_markers: list[str], end_markers: list[str]) -> str:
    start = first_index(text, start_markers)
    if start == -1:
        return ""
    matched_start = next(marker for marker in start_markers if text.find(marker) == start)
    start += len(matched_start)
    end = first_index(text, end_markers, start)
    if end == -1:
        end = len(text)
    return text[start:end]


def extract_intro(text: str) -> str:
    split_at = first_index(text, ["一、全省全社会用电情况"])
    return text[:split_at] if split_at != -1 else text


def extract_metric(patterns: list[re.Pattern[str]], text: str) -> float | None:
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return float(match.group(1 if pattern.groups == 1 else "value"))
    return None


def extract_repeated_values(section: str, labels: list[str], unit: str) -> list[float]:
    values: list[float] = []
    for label in labels:
        pattern = re.compile(re.escape(label) + NUMBER + re.escape(unit))
        matches = [float(match.group(1)) for match in pattern.finditer(section)]
        if matches:
            values = matches
            break
    return values


def extract_first_value(section: str, labels: list[str], unit: str) -> float | None:
    matches = extract_repeated_values(section, labels, unit)
    return matches[0] if matches else None


def extract_sector_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    for key, labels in SECTOR_LABELS.items():
        matches = extract_repeated_values(section, labels, "亿千瓦时")
        output[f"{key}_monthly_kwh_100m"] = matches[0] if len(matches) >= 1 else None
        output[f"{key}_ytd_kwh_100m"] = matches[1] if len(matches) >= 2 else None
    return output


def extract_industry_ytd_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    for key, labels in INDUSTRY_YTD_LABELS.items():
        output[f"{key}_ytd_kwh_100m"] = extract_first_value(section, labels, "亿千瓦时")
    return output


def extract_industrial_subsector_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    for key, labels in INDUSTRIAL_SUBSECTOR_LABELS.items():
        matches = extract_repeated_values(section, labels, "亿千瓦时")
        output[f"{key}_monthly_kwh_100m"] = matches[0] if len(matches) >= 1 else None
        output[f"{key}_ytd_kwh_100m"] = matches[1] if len(matches) >= 2 else None
    return output


def extract_capacity_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    for key, labels in CAPACITY_LABELS.items():
        output[f"capacity_{key}_wan_kw"] = extract_first_value(section, labels, "万千瓦")
    return output


def extract_generation_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    for key, labels in GENERATION_LABELS.items():
        matches = extract_repeated_values(section, labels, "亿千瓦时")
        output[f"generation_{key}_monthly_100m_kwh"] = matches[0] if len(matches) >= 1 else None
        output[f"generation_{key}_ytd_100m_kwh"] = matches[1] if len(matches) >= 2 else None
    return output


def extract_utilization_values(section: str) -> dict[str, float | None]:
    output: dict[str, float | None] = {}
    total = None
    for label in UTILIZATION_LABELS["total"]:
        match = re.search(re.escape(label) + NUMBER + r"小时", section)
        if match:
            total = float(match.group(1))
            break
    output["utilization_total_hours"] = total
    for key in ["hydro", "thermal", "wind", "solar"]:
        output[f"utilization_{key}_hours"] = extract_first_value(section, UTILIZATION_LABELS[key], "小时")
    return output


def derive_sections(text: str) -> dict[str, str]:
    sector = extract_section(text, ["分产业用电"], ["分行业用电"])
    industry = extract_section(text, ["分行业用电"], ["3.工业用电", "3、工业用电", "二、全省发电情况"])
    industrial = extract_section(text, ["3.工业用电", "3、工业用电"], ["二、全省发电情况"])
    generation_block = extract_section(text, ["二、全省发电情况"], [])
    capacity = extract_section(generation_block, ["1.发电装机规模", "1、发电装机规模", "1.装机规模", "1、装机规模"], ["2.发电量", "2、发电量"])
    generation = extract_section(generation_block, ["2.发电量", "2、发电量"], ["3.平均发电利用小时", "3、平均发电利用小时"])
    utilization = extract_section(generation_block, ["3.平均发电利用小时", "3、平均发电利用小时"], [])
    return {
        "intro": extract_intro(text),
        "sector": sector,
        "industry": industry,
        "industrial": industrial,
        "capacity": capacity,
        "generation": generation,
        "utilization": utilization,
    }


def build_row(base_row: dict[str, str], parsed: dict[str, object]) -> dict[str, object]:
    text = compact_text(parsed.get("content_text_compact", "") or parsed.get("content_text", ""))
    sections = derive_sections(text)

    row: dict[str, object] = dict(base_row)
    row.update(
        {
            "monthly_total_kwh_100m": base_row.get("monthly_kwh_100m") or None,
            "monthly_total_kwh_method": base_row.get("monthly_kwh_method") or None,
            "ytd_total_kwh_100m": base_row.get("ytd_kwh_100m") or None,
            "ytd_total_kwh_method": base_row.get("ytd_kwh_method") or None,
            "source_text_length": len(text),
        }
    )

    row["export_monthly_kwh_100m"] = extract_metric(EXPORT_MONTHLY_PATTERNS, sections["intro"])
    row["export_ytd_kwh_100m"] = extract_metric(EXPORT_YTD_PATTERNS, sections["intro"])
    row["import_monthly_kwh_100m"] = extract_metric(IMPORT_MONTHLY_PATTERNS, sections["intro"])
    row["import_ytd_kwh_100m"] = extract_metric(IMPORT_YTD_PATTERNS, sections["intro"])

    row.update(extract_sector_values(sections["sector"]))
    row.update(extract_industry_ytd_values(sections["industry"]))
    row.update(extract_industrial_subsector_values(sections["industrial"]))
    row.update(extract_capacity_values(sections["capacity"]))
    row.update(extract_generation_values(sections["generation"]))
    row.update(extract_utilization_values(sections["utilization"]))

    return row


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_coverage(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    metadata_columns = {
        "province",
        "year_month",
        "title",
        "article_url",
        "source_url_used",
        "source_note",
        "pub_date",
        "content_source",
        "raw_html_file",
        "parsed_json_file",
        "engine",
    }
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["column_name", "non_null_count", "first_year_month", "last_year_month"])
        writer.writeheader()
        for column in rows[0].keys():
            if column in metadata_columns:
                continue
            non_null_rows = [row for row in rows if row.get(column) not in ("", None)]
            first_ym = non_null_rows[0]["year_month"] if non_null_rows else ""
            last_ym = non_null_rows[-1]["year_month"] if non_null_rows else ""
            writer.writerow(
                {
                    "column_name": column,
                    "non_null_count": len(non_null_rows),
                    "first_year_month": first_ym,
                    "last_year_month": last_ym,
                }
            )


def main() -> None:
    args = parse_args()
    base_rows = list(csv.DictReader(Path(args.base_panel).open()))
    structured_rows: list[dict[str, object]] = []
    for base_row in base_rows:
        parsed = json.loads(Path(base_row["parsed_json_file"]).read_text(encoding="utf-8"))
        structured_rows.append(build_row(base_row, parsed))

    structured_rows.sort(key=lambda row: str(row["year_month"]))
    write_csv(structured_rows, Path(args.output))
    write_coverage(structured_rows, Path(args.coverage_output))
    print(f"Built {len(structured_rows)} structured Gansu rows.")


if __name__ == "__main__":
    main()
