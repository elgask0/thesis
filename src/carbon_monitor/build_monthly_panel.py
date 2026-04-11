#!/usr/bin/env python3
"""Build a province-month CO2 panel from the Carbon Monitor China CSV export."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


RAW_DATE_FORMAT = "%d/%m/%Y"
RAW_VALUE_TO_TONNES = 1_000_000.0
REQUIRED_COLUMNS = ("state", "date", "sector", "value")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate Carbon Monitor China daily CSV data to province-month totals."
    )
    parser.add_argument("--input", required=True, help="Path to the raw Carbon Monitor CSV.")
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the monthly province output CSV.",
    )
    parser.add_argument(
        "--sector",
        action="append",
        default=[],
        help="Optional sector filter. Repeat to keep multiple sectors.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    sector_filter = set(args.sector)

    monthly_totals: dict[tuple[str, str], float] = defaultdict(float)
    matched_rows = 0
    skipped_rows = 0

    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing_columns = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
        if missing_columns:
            raise ValueError(
                f"Missing required columns {missing_columns} in {input_path}. "
                f"Found columns: {fieldnames}"
            )

        for row in reader:
            province = (row.get("state") or "").strip()
            raw_date = (row.get("date") or "").strip()
            sector = (row.get("sector") or "").strip()
            raw_value = (row.get("value") or "").strip()

            if sector_filter and sector not in sector_filter:
                continue

            if not province or not raw_date or not raw_value:
                skipped_rows += 1
                continue

            try:
                parsed_date = datetime.strptime(raw_date, RAW_DATE_FORMAT)
                value_tonnes = float(raw_value.replace(",", "")) * RAW_VALUE_TO_TONNES
            except ValueError:
                skipped_rows += 1
                continue

            year_month = parsed_date.strftime("%Y-%m")
            monthly_totals[(province, year_month)] += value_tonnes
            matched_rows += 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["province", "date", "year_month", "co2_tonnes", "source_file"],
        )
        writer.writeheader()
        for province, year_month in sorted(monthly_totals):
            writer.writerow(
                {
                    "province": province,
                    "date": f"{year_month}-01",
                    "year_month": year_month,
                    "co2_tonnes": f"{monthly_totals[(province, year_month)]:.6f}",
                    "source_file": input_path.name,
                }
            )

    sector_label = ",".join(sorted(sector_filter)) if sector_filter else "all sectors"
    print(
        f"Wrote {len(monthly_totals)} province-month rows from {matched_rows} matched rows "
        f"and skipped {skipped_rows} non-data rows using {sector_label} to {output_path}"
    )


if __name__ == "__main__":
    main()
