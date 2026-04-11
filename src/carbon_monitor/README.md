# Carbon Monitor Starter

This folder contains the CSV-based scaffold for the thesis CO2 backbone.

## Goal

Turn a raw Carbon Monitor daily file into a province-month panel that can later be joined with treatment and electricity data.

## Current Working Rule

- Start with CO2 first.
- Do not block on final treatment-date fact-checking.
- Do not block on electricity-coverage confidence.
- Build the monthly CO2 backbone, then move back to province-by-province electricity work.

## Expected Input

Use the Carbon Monitor China CSV export stored under `03_data/raw/carbon_monitor/`.

Canonical download URL:

- `https://datas.carbonmonitor.org/API/downloadFullDataset.php?source=carbon_china`

The script expects the website-style layout:

- `state`
- `date`
- `sector`
- `value`

The raw `value` field is treated as daily `MtCO2` and converted to `tonnes` during aggregation.

## Output

The script writes a tidy CSV with:

- `province`
- `date` as the first day of each month
- `year_month`
- `co2_tonnes`
- `source_file`

## Example

```bash
python3 src/carbon_monitor/build_monthly_panel.py \
  --input 03_data/raw/carbon_monitor/carbonmonitor-china_datas_2026-04-11.csv \
  --output 03_data/interim/panel_co2_monthly.csv
```

If you want a sector-specific monthly panel, add one or more `--sector` filters:

```bash
python3 src/carbon_monitor/build_monthly_panel.py \
  --input 03_data/raw/carbon_monitor/carbonmonitor-china_datas_2026-04-11.csv \
  --output 03_data/interim/panel_co2_monthly.csv \
  --sector Power
```
