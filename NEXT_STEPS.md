---
title: "EDWC Thesis — Next Steps & Action Plan"
description: "Detailed roadmap for completing the EDWC thesis with specific tasks and timelines"
status: active
tags: [project, thesis, tasks, roadmap, edwc]
created: 2026-02-19
---

# EDWC Thesis — Next Steps & Action Plan

**Last Updated:** 2026-04-11
**Status:** Phase 1 — Data Collection

---

## Overview

This document is orientative, not binding. Right now the real priority is to build the empirical backbone for both baseline outcomes: CO₂ and electricity. CO₂ is easier to assemble first, but electricity is equally important and must begin immediately with a Gansu-first province-by-province workflow.

---

## Phase 1: Data Collection (Weeks 1-3)

### Step 1.1: Build CO₂ Panel ✊ Start Here
**Time Estimate:** 2-4 hours | **Priority:** HIGH

This is the easier of the two baseline outcome builds, not the more important one.

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
- [ ] Start with Gansu first
  - Base search URL: `https://gxt.gansu.gov.cn/guestweb4/s?siteCode=6200000082&checkHandle=1&pageSize=10&left_right_index=0&searchWord=全省电力生产运行情况`
  - Query phrase: `全省电力生产运行情况`
- [ ] Inspect the Gansu bulletin structure
  - Note format (HTML/PDF)
  - Identify recurring title pattern
  - Check whether bulletins report province-wide electricity consumption, production, or only YTD aggregates
- [ ] Collect a small verified seed set for Gansu
  - Save title, publication date, search URL, and final article URL
  - Extract the units used in the bulletin
  - Record one parsing template that could later be automated
- [ ] Only after Gansu works, identify starting URLs for Ningxia, Inner Mongolia, and Guizhou
- [ ] Log findings in `01_notes/electricity_data_pipeline.md`
- [ ] Only create `03_data/processed/panel_kwh_monthly.csv` after extraction is proven workable
- [ ] QA check: confirm what can actually be extracted before claiming coverage

**Output:** Verified Gansu source log + extraction template + first province-ready path toward the baseline electricity panel

**Current Source Status:**
| Province | Current status |
|----------|----------------|
| Gansu | Base search URL identified |
| Ningxia | Not mapped yet |
| Inner Mongolia | Not mapped yet |
| Guizhou | Not mapped yet |

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
  - Ningxia: 2023-02-24 (use 2023-02-01 for month coding)
  - Guizhou: 2023-09 (use 2023-09-01; keep 2024-06 as robustness)
  - Inner Mongolia: 2024-09 (use 2024-09-01 for month coding; refine exact daily date later if needed)
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
**Time Estimate:** 2-4 hours | **Priority:** HIGH

**Tasks:**
- [ ] Run same event-study on `kwh_total` outcome
- [ ] Use the verified kWh sample that meets the documented coverage rule
- [ ] Keep expanding province coverage even if the first estimation sample is incomplete
- [ ] Plot dynamic effects

**Output:** First kWh event-study results on the verified sample, plus a documented coverage gap list

---

### Step 2.3: Synthetic Control (Gansu) — Optional
**Time Estimate:** 4-6 hours | **Priority:** MEDIUM (optional / supplementary)

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

## Phase 3: Extension & Writing (Weeks 7-12)

### Step 3.1: Economic Outcomes (Exploratory Extension)
**Time Estimate:** 2-3 days | **Priority:** LOW (program-fit extension)

**Tasks:**
- [ ] Collect provincial economic data
  - Fixed asset investment (monthly/quarterly)
  - Employment (ICT sector, if available)
  - Extract CAICT province tiers / indicators
  - Prioritize 2022 and 2023 `综合算力` editions for comparable province-level benchmarking
  - Use broader CAICT `算力发展指数` variables only as cross-sectional enrichment, not as a direct year-to-year continuation
- [ ] Merge with main panel
- [ ] Estimate event-study with economic outcomes
- [ ] Document correlations between energy/compute and economics

**Output:** Economic extension section (discussion)

---

### Step 3.2: Write Thesis Chapters
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
   - [ ] Source logging and provenance
4. **Methods** (1 week)
   - [ ] Event-study design
   - [ ] SCM design
   - [ ] Identification assumptions and robustness
5. **Results** (2 weeks)
   - [ ] RQ1: Event-study and SCM findings
   - [ ] Electricity evidence, if data quality permits
   - [ ] Economic extension (program-fit)
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

### Phase 3: Extension & Writing
- [ ] Step 3.1: RQ3 economic outcomes
- [ ] Step 3.2: Thesis chapters

---

## Quick Start for Today

**Recommended electricity task for now:** Step 1.2 — map the Gansu bulletin structure from the base URL

1. Open the Gansu search endpoint
2. Save a few candidate bulletin titles and URLs
3. Check what each article actually reports
4. Write down one reusable parsing template

This is the current best way to turn the electricity note into real work.

---

*Last updated: 2026-04-11*
