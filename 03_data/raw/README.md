# Raw Data

Original, unmodified data sources. This folder is currently just a scaffold; no raw datasets are committed yet.

---

## Contents

### CO₂ Emissions
- **Folder:** `carbon_monitor/`
- **Source:** Carbon Monitor China (https://carbonmonitor.org)
- **Description:** Daily provincial CO₂ emissions (2019–2025)
- **Format:** CSV/JSON (original format from source)
- **Status:** Local CSV now stored in `carbon_monitor/carbonmonitor-china_datas_2026-04-11.csv`
- **Canonical download URL:** `https://datas.carbonmonitor.org/API/downloadFullDataset.php?source=carbon_china`
- **Observed coverage in the current best local CSV:** `2019-01-01` to `2025-11-30`, `31` provinces, `5` sectors (`Industry`, `Ground Transport`, `Aviation`, `Residential`, `Power`)
- **Canonical repo workflow:** use the CSV export, not the narrower XLSX export
- **Notes:** Primary outcome variable for RQ1

### Electricity Consumption
- **Folder:** `electricity_bulletins/`
- **Source:** Scraped from provincial government bulletins
- **Description:** Monthly electricity consumption by province
- **Format:** HTML, PDF, or extracted text
- **Status:** Source discovery only; see [[electricity_data_pipeline]]
- **Coverage:** Target ≥80% of months for each treated province

### Weather & Controls
- **Status:** Not yet downloaded
- **Planned sources:**
  - CDD/HDD (Cooling/Heating Degree Days)
  - Precipitation
  - Statutory holidays
- **Purpose:** Control variables $X_{p,t}$ in event-study specification

### Grid Mix & Generation
- **Status:** Not yet downloaded
- **Planned sources:** Provincial generation shares by fuel type
- **Purpose:** CI computation (supplementary to CO₂/kWh)

---

## Important Notes

### Git Policy
- **Usually do not commit raw data files** to git unless they are tiny and clearly reusable
- Store intermediate data in `../interim/`
- Store final analysis panels in `../processed/`
- Use `.gitignore` to exclude raw data files

### Data Collection Workflow
1. Download data from original sources
2. Store in appropriate subfolder (carbon_monitor, electricity_bulletins, etc.)
3. Do **not modify** raw files — create cleaned copies in `interim/`
4. Document source URL, download date, and any access notes

---

## Regeneration

All files in this folder can be re-downloaded from original sources:

| Data Type | Source | URL | Notes |
|-----------|--------|-----|-------|
| CO₂ | Carbon Monitor China | https://datas.carbonmonitor.org/API/downloadFullDataset.php?source=carbon_china | Daily export used by the repo |
| Electricity | Provincial bulletins | Varies by province | See [[electricity_data_pipeline]] |
| Weather | Meteorological datasets | TBD | To be determined |

See [[global_plan]] for detailed data source documentation.

---

## Last Updated

2026-04-11
