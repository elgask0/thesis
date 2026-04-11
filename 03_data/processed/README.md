# Processed Data

Final analysis-ready panels for DiD/SCM estimation. This folder currently contains only placeholders and target file definitions; no processing code or notebooks exist in the repo yet.

---

## Contents

### CO₂ Panel (Event-Study Ready)
- **File:** `panel_co2_monthly.csv` (to be created)
- **Description:** Province-month CO₂ emissions for Sun-Abraham estimator
- **Columns:**
  - `province` (string, standardized name)
  - `date` (YYYY-MM-DD, first of month)
  - `year_month` (YYYY-MM)
  - `co2_tonnes` (float, outcome variable $y_{p,t}$)
  - `ln_co2` (float, log CO₂ for specification)
  - `is_treated` (binary, 1 if province ∈ treated set)
  - `event_month` (integer, event time $\ell = t - E_p$)
  - `cohort` (string, EDWC cohort: Ningxia, Gansu, etc.)

### Electricity Panel (Event-Study Ready)
- **File:** `panel_kwh_monthly.csv` (to be created)
- **Description:** Province-month electricity consumption (baseline outcome, harder to collect than CO₂)
- **Columns:**
  - `province`
  - `date` (YYYY-MM-DD, first of month)
  - `year_month` (YYYY-MM)
  - `kwh_total` (float, outcome variable)
  - `ln_kwh` (float, log kWh)
  - `coverage_flag` (binary, 1 if ≥80% months covered)
  - `is_treated`, `event_month`, `cohort` (same structure as CO₂ panel)

### Full Analysis Panel
- **File:** `panel_analysis.csv` (to be created)
- **Description:** Merged panel with outcomes + controls + treatment indicators
- **Columns:** All outcomes + controls from `../interim/`
  - Outcomes: `co2_tonnes`, `kwh_total`
  - Controls: `cdd`, `hdd`, `precipitation_mm`, `holiday_days`
  - Treatment: `is_treated`, `event_month`, `cohort`
  - FE variables: `province_fe`, `month_fe` (for estimation)

### Treatment Dates
- **File:** `treatment_dates.csv` (to be created)
- **Description:** T₀ anchors for event-study construction
- **Usage:** Create event time variable $\ell = t - E_p$

---

## Usage

Target use once the repo has real code:

- event-study estimation
- synthetic control estimation
- CPC and scenario construction

At the moment, `src/` and `notebooks/` are placeholders only.

---

## Regeneration

These files are intended to be generated from `../interim/`, but no finalization script exists yet in the repo.

---

## Version Control

- **Commit processed data to git** (these are analysis-ready, small files)
- Include hash of intermediate files used for reproducibility
- Document any cleaning decisions in code comments

---

## Last Updated

2026-04-11
