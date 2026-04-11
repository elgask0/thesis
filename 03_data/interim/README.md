# Intermediate Data

Cleaned and merged datasets, ready for final processing. This folder is still a scaffold: the target files are defined here, but no regeneration scripts exist in the repo yet.

---

## Contents

### CO₂ Panels
- **File:** `panel_co2_monthly.csv`
- **Description:** Monthly provincial CO₂ emissions from the current best local Carbon Monitor export
- **Source:** Aggregated from daily Carbon Monitor data in `../raw/`
- **Current local build:** `panel_co2_monthly.csv` now exists and was aggregated from `carbonmonitor-china_datas_2026-04-11.csv`
- **Observed coverage in the current local build:** `2573` rows = `31` provinces × `83` months (`2019-01` to `2025-11`)
- **Canonical build path:** `python3 src/carbon_monitor/build_monthly_panel.py --input 03_data/raw/carbon_monitor/carbonmonitor-china_datas_2026-04-11.csv --output 03_data/interim/panel_co2_monthly.csv`
- **Columns:**
  - `province` (string)
  - `year_month` (YYYY-MM)
  - `co2_tonnes` (float, tonnes CO₂)
  - `source_file` (string, for provenance)

### Electricity Panels
- **File:** `panel_kwh_monthly.csv` (to be created)
- **Description:** Monthly provincial electricity consumption (2019–2025)
- **Source:** Scraped and API-extracted from provincial bulletins
- **Columns:**
  - `province` (string)
  - `year_month` (YYYY-MM)
  - `kwh_total` (float, kWh)
  - `kwh_industrial` (float, optional)
  - `yoy_percent` (float, optional)
  - `source_url` (string, for provenance)

### Merged Controls
- **File:** `panel_controls.csv` (to be created)
- **Description:** Weather, holidays, and other control variables
- **Columns:**
  - `province`
  - `year_month`
  - `cdd` (cooling degree days)
  - `hdd` (heating degree days)
  - `precipitation_mm` (float)
  - `holiday_days` (integer, statutory holidays in month)

### Treatment & Cohort Data
- **File:** `treatment_dates.csv` (to be created)
- **Description:** T₀ commissioning dates by province
- **Columns:**
  - `province` (string)
  - `t0_date` (YYYY-MM-DD)
  - `cohort` (string, e.g., "Ningxia", "Gansu")
  - `evidence_url` (string)
- **Source:** [[edwc_treatment_dates]]

---

## Regeneration

Planned regeneration workflow:

- aggregate raw CO₂ data into monthly province panels
- extract electricity values from provincial bulletins
- merge weather, holidays, and other controls

No regeneration scripts have been implemented in `src/` yet.

---

## Quality Checks

Before using intermediate files, verify:

1. **Completeness:** No gaps in time series (except expected missing data)
2. **Consistency:** Province names standardized across files
3. **Ranges:** Values within plausible bounds (e.g., CO₂ > 0, kWh > 0)
4. **Metadata:** Source files and dates documented

---

## Last Updated

2026-04-11
