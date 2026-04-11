---
title: "EDWC Thesis — Next Steps & Action Plan"
description: "Detailed roadmap for completing the EDWC thesis with specific tasks and timelines"
status: active
tags: [project, thesis, tasks, roadmap, edwc]
created: 2026-02-19
---

# EDWC Thesis — Next Steps & Action Plan

**Last Updated:** 2026-02-19
**Status:** Phase 1 — Data Collection

---

## Overview

This document breaks down the thesis work into concrete steps. Start from the top and work down.

---

## Phase 1: Data Collection (Weeks 1-3)

### Step 1.1: Build CO₂ Panel ✊ Start Here
**Time Estimate:** 2-4 hours | **Priority:** HIGH

**Tasks:**
- [ ] Download Carbon Monitor China daily data
  - URL: https://carbonmonitor.org
  - Years: 2019-2025
  - Provinces: All 31 provinces
- [ ] Aggregate daily → monthly by province
  - Sum daily CO₂ to monthly totals
  - Create `province`, `year_month`, `co2_tonnes` columns
- [ ] Save to `03_data/processed/panel_co2_monthly.csv`
- [ ] QA check: Plot monthly CO₂ for a few provinces to verify

**Output:** `panel_co2_monthly.csv` (31 provinces × ~84 months)

---

### Step 1.2: Build kWh Panel 🕷️ Hardest Step
**Time Estimate:** 1-2 days | **Priority:** HIGH

**Tasks:**
- [ ] Identify bulletin URLs for each treated province
  - Gansu: https://gxt.gansu.gov.cn
  - Ningxia: Find site
  - Inner Mongolia: Find site
  - Guizhou: Find site
- [ ] Inspect bulletin structure for each province
  - Note format (HTML/PDF)
  - Identify recurring title pattern
  - Check monthly coverage (2019-2025)
- [ ] Build scraper for Gansu (highest coverage)
  - Paginate through bulletin list
  - Extract article text
  - Parse monthly kWh values
- [ ] Extend scraper to other provinces
- [ ] Save to `03_data/processed/panel_kwh_monthly.csv`
- [ ] QA check: Coverage % by province; flag if <80%

**Output:** `panel_kwh_monthly.csv`

**Coverage Status:**
| Province | 2024 | 2025 | Status |
|----------|------|------|--------|
| Gansu | 100% | 100% | ✓ Confirmed |
| Ningxia | ? | ? | ? Verify |
| Inner Mongolia | ? | ? | ? Verify |
| Guizhou | ? | ? | ? Verify |

---

### Step 1.3: Collect Control Variables
**Time Estimate:** 4-6 hours | **Priority:** MEDIUM

**Tasks:**
- [ ] Download weather data
  - CDD (Cooling Degree Days) by province-month
  - HDD (Heating Degree Days) by province-month
  - Precipitation by province-month
  - Source: China Meteorological Administration or global dataset
- [ ] Create holiday indicator
  - List statutory holidays (2019-2025)
  - Add `holiday_days` count per province-month
- [ ] Save to `03_data/processed/panel_controls.csv`

**Output:** `panel_controls.csv`

---

### Step 1.4: Create Treatment Variables
**Time Estimate:** 1-2 hours | **Priority:** HIGH

**Tasks:**
- [ ] Create treatment dates file
  - Ningxia: 2023-07-21
  - Guizhou: 2023-12 (use 2023-12-01)
  - Inner Mongolia: 2024-04-28
  - Gansu: 2024-06 (use 2024-06-01)
- [ ] For each province-month, calculate:
  - `is_treated`: 1 if province ∈ {Gansu, Ningxia, IM, Guizhou}
  - `event_month`: ℓ = t - T₀ (relative to commissioning)
  - `cohort`: Province name
- [ ] Save to `03_data/processed/treatment_dates.csv`

**Output:** `treatment_dates.csv`

---

### Step 1.5: Assemble Analysis Panel
**Time Estimate:** 1-2 hours | **Priority:** HIGH

**Tasks:**
- [ ] Merge all datasets
  - Left join: CO₂ panel + kWh panel + controls + treatment
  - On: `province` + `year_month`
- [ ] Create final columns for estimation
  - `co2_tonnes`, `kwh_total` (outcomes)
  - `cdd`, `hdd`, `precipitation_mm`, `holiday_days` (controls)
  - `is_treated`, `event_month`, `cohort` (treatment)
- [ ] Add event-window indicator
  - Keep only obs where `event_month ∈ [-12, +18]` for treated
  - Keep all time periods for controls
- [ ] Save to `03_data/processed/panel_analysis.csv`

**Output:** `panel_analysis.csv`

---

## Phase 2: Estimation (Weeks 4-6)

### Step 2.1: Event-Study (Sun-Abraham) — CO₂
**Time Estimate:** 4-6 hours | **Priority:** HIGH

**Tasks:**
- [ ] Install/familiarize with Sun-Abraham implementation
  - Python: `csdid` or `eventstudy` packages
  - Or R: `fixest` package
- [ ] Run event-study on CO₂ outcome
  - Dependent variable: `co2_tonnes`
  - Treatment: `is_treated`
  - Event time: `event_month`
  - Cohort: `cohort`
  - Controls: CDD, HDD, precipitation, holidays
  - FE: Province, month-year
- [ ] Extract event-time coefficients βℓ
- [ ] Plot dynamic effects (ℓ = -12 to +18)
- [ ] Pre-trend test: Leads should be insignificant

**Output:** Event-study plots and coefficient table

---

### Step 2.2: Event-Study (Sun-Abraham) — kWh
**Time Estimate:** 2-4 hours | **Priority:** MEDIUM

**Tasks:**
- [ ] Run same event-study on `kwh_total` outcome
- [ ] Only if coverage ≥80% for treated provinces
- [ ] Plot dynamic effects

**Output:** kWh event-study results (conditional on coverage)

---

### Step 2.3: Synthetic Control (Gansu)
**Time Estimate:** 4-6 hours | **Priority:** HIGH

**Tasks:**
- [ ] Select donor pool
  - Non-EDWC provinces in CAICT Q1 tier
  - Candidates: Qinghai, Yunnan, Guangxi, etc. (verify from CAICT report)
- [ ] Fit SCM on pre-period
  - Pre-period: Up to 2024-05 (month before Gansu T₀)
  - Predictor variables: CO₂ levels, trends
- [ ] Evaluate post-period gap
  - Compare Gansu vs Synthetic Gansu (2024-06 onward)
- [ ] Robustness checks
  - Placebo tests: Run SCM on non-treated provinces
  - Leave-one-out: Exclude each donor iteratively
  - Alternative pre-period windows

**Output:** SCM plots and results

---

### Step 2.4: Interpret Results
**Time Estimate:** 2-3 hours | **Priority:** HIGH

**Tasks:**
- [ ] Summarize event-study findings
  - Average treatment effect (post-period)
  - Dynamic pattern: Immediate vs. lagged effects
  - Statistical significance (clustered SEs)
- [ ] Compare with SCM results
  - Do methods agree on magnitude/direction?
- [ ] Document any anomalies
  - Anticipation effects (leads ≠ 0)?
  - Heterogeneity across cohorts?

**Output:** Results summary (1-2 pages)

---

## Phase 3: CPC Construction (Weeks 7-8)

### Step 3.1: Compute Carbon Intensity (CI)
**Time Estimate:** 1-2 hours | **Priority:** HIGH

**Tasks:**
- [ ] Calculate CI by province-month
  - CI = CO₂ / kWh (both in consistent units)
  - If kWh missing, skip CI for that obs
- [ ] Save CI series to `03_data/processed/panel_ci.csv`

**Output:** `panel_ci.csv`

---

### Step 3.2: Build GF/W Series
**Time Estimate:** 4-6 hours | **Priority:** HIGH

**Tasks:**
- [ ] Download Green500 data (2019-2025)
  - URL: https://www.top500.org/green500/
  - Extract top-10 systems per edition
  - Compute median GF/W as frontier
- [ ] Download HPL-MxP speedup factors
  - Find HPL-MxP benchmark results
  - Extract speedup = MxP_EF / FP64_EF
- [ ] Interpolate to monthly frequency
  - Linear interpolation between Green500 editions
- [ ] Apply adjustments
  - MFU (utilization): κ ∈ [0.4, 0.6], center 0.5
  - China interconnect: λ ∈ [0.3, 0.5], center 0.4
  - GF/W_China = GF/W_FP64 × speedup × κ × (1 - λ × (1 - β))
  - where β = A800_bandwidth / A100_bandwidth = 400/600 = 0.667
- [ ] Generate uncertainty bands via Monte Carlo
- [ ] Save to `03_data/processed/series_gfw.csv`

**Output:** `series_gfw.csv` (monthly 2019-2025)

---

### Step 3.3: Apply PUE Trajectories
**Time Estimate:** 1-2 hours | **Priority:** MEDIUM

**Tasks:**
- [ ] Define PUE paths by province
  - Start: Current PUE (if known) or assume 1.8 (2022)
  - End: 1.5 by 2025 (policy target)
  - Linear interpolation between start and end
- [ ] Add uncertainty band: ±0.1
- [ ] Save to `03_data/processed/series_pue.csv`

**Output:** `series_pue.csv`

---

### Step 3.4: Calculate CPC
**Time Estimate:** 1-2 hours | **Priority:** HIGH

**Tasks:**
- [ ] Compute CPC by province-month
  - CPC = CI × PUE × (1000 / GF/W)
  - Units: tCO₂ per EF·h
- [ ] Compare pre- vs. post-EDWC CPC
  - Pre-period: Average CPC before T₀
  - Post-period: Average CPC after T₀
  - Calculate ΔCPC
- [ ] Save to `03_data/processed/panel_cpc.csv`

**Output:** `panel_cpc.csv`

---

### Step 3.5: Translate to Compute Scenarios
**Time Estimate:** 2-3 hours | **Priority:** HIGH

**Tasks:**
- [ ] For each treated province and post-treatment month:
  - Energy-based: ΔEF·h = ΔMWh × θ / (PUE × GF/W)
    - Where θ ∈ [0.5, 1.0] = fraction of MWh from datacenters
  - Emissions-based: ΔEF·h = ΔCO₂ / CPC
- [ ] Generate scenario bands (low, medium, high)
- [ ] Plot implied compute over time

**Output:** Compute scenarios by province-month

---

## Phase 4: RQ3 & Writing (Weeks 9-12)

### Step 4.1: Economic Outcomes (RQ3)
**Time Estimate:** 2-3 days | **Priority:** MEDIUM

**Tasks:**
- [ ] Collect provincial economic data
  - Fixed asset investment (monthly/quarterly)
  - Employment (ICT sector, if available)
  - CAICT compute index updates (if new editions)
- [ ] Merge with main panel
- [ ] Estimate event-study with economic outcomes
- [ ] Document correlations between energy/compute and economics

**Output:** RQ3 results section

---

### Step 4.2: Write Thesis Chapters
**Time Estimate:** 2-3 weeks | **Priority:** HIGH

**Chapter Outline:**
1. **Introduction** (2 weeks)
   - [ ] Motivation and context
   - [ ] Research questions
   - [ ] Contributions
2. **Background** (1 week)
   - [ ] EDWC policy overview
   - [ ] China's energy system and data centers
   - [ ] Literature review
3. **Data** (1 week)
   - [ ] CO₂ sources
   - [ ] Electricity data collection
   - [ ] CPC inputs
4. **Methods** (1 week)
   - [ ] Event-study design
   - [ ] SCM design
   - [ ] CPC construction
5. **Results** (2 weeks)
   - [ ] RQ1: Event-study and SCM findings
   - [ ] RQ2: CPC and compute scenarios
   - [ ] RQ3: Economic outcomes
6. **Conclusion** (1 week)
   - [ ] Summary of findings
   - [ ] Policy implications
   - [ ] Limitations and future work

**Output:** Complete thesis draft

---

## Progress Checklist

### Phase 1: Data Collection
- [ ] Step 1.1: CO₂ panel
- [ ] Step 1.2: kWh panel
- [ ] Step 1.3: Control variables
- [ ] Step 1.4: Treatment variables
- [ ] Step 1.5: Analysis panel

### Phase 2: Estimation
- [ ] Step 2.1: Event-study (CO₂)
- [ ] Step 2.2: Event-study (kWh)
- [ ] Step 2.3: Synthetic Control
- [ ] Step 2.4: Interpret results

### Phase 3: CPC
- [ ] Step 3.1: Carbon intensity
- [ ] Step 3.2: GF/W series
- [ ] Step 3.3: PUE trajectories
- [ ] Step 3.4: CPC calculation
- [ ] Step 3.5: Compute scenarios

### Phase 4: Writing
- [ ] Step 4.1: RQ3 economic outcomes
- [ ] Step 4.2: Thesis chapters

---

## Quick Start for Today

**Recommended first task:** Step 1.1 — Build CO₂ Panel

1. Go to https://carbonmonitor.org
2. Download China daily CO₂ data (2019-2025)
3. Aggregate to monthly by province
4. Save to `03_data/processed/panel_co2_monthly.csv`

This is the easiest win and gets you started immediately!

---

*Last updated: 2026-02-19*
