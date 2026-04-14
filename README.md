---
title: "EDWC Thesis — Eastern Data, Western Compute in China"
description: "Master's thesis examining causal effects of China's EDWC program on provincial CO₂ emissions, electricity consumption, and AI-relevant Carbon-per-Compute metrics"
status: active
tags: [project, thesis, economics, china, energy, AI, EDWC]
---

# Eastern Data, Western Compute (EDWC) Thesis

Master's thesis in Chinese Economy at Zhejiang University.

**Author:** Mario D.M.
**Last Updated:** 2026-04-11

**Current State:** This repo is still an early scaffold. It contains the project structure, working notes, source archives, and the research plan, but no real analysis code or committed datasets yet.

**Current Working Posture:** Use the supervisor slide deck as the narrative anchor for the thesis, but start implementation with the Carbon Monitor CO2 backbone. Exact treatment-date fact-checking and province-level electricity coverage decisions can wait until the baseline data backbone exists.

**AI onboarding:** [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) define the current repo rules and work sequence.

---

## Quick Overview

**Research Question:** What is the causal effect of China's EDWC program on provincial CO₂ emissions and electricity consumption, and how should those results later be translated into AI-relevant compute metrics?

**Methods:** Sun-Abraham event-study, province-by-province electricity scraping starting with Gansu, and optional Synthetic Control for Gansu

**Key Contribution:** Translating energy effects into AI-native Carbon-per-Compute (CPC) metrics

---

## Where to Start

| What to Read | Why |
|--------------|-----|
| **`05_misc/pdfs/supervisor_meeting_slides.pdf`** | Current supervisor-facing framing of the thesis |
| **[[NEXT_STEPS|Next Steps →]]** | Current orientative work order for the repo |
| **[[global_plan|Global Plan]]** | Full research design, scope, and empirical logic |
| **[[electricity_data_pipeline|Electricity Data Pipeline]]** | Current state of the provincial electricity collection plan |
| **[[edwc_treatment_dates|Treatment Dates]]** | T₀ evidence archive by province |
| **[[thesis_structure|Structure]]** | Chapter-level thesis outline |

---

## Research Questions

### RQ1 — Causal Effects
What is the effect of EDWC go-live on provincial CO₂ and electricity?
- **Method:** Event-study (Sun-Abraham) + Synthetic Control (Gansu, optional)
- **Outcomes:** Daily CO₂ and monthly kWh are both baseline outcomes
- **Sequencing:** CO₂ is easier to assemble first; electricity is harder but required and starts with Gansu

### RQ2 — Compute Translation
What is the implied Carbon-per-Compute (CPC) before and after EDWC?
- **Method:** CPC = CI × PUE × (1000/GF/W)
- **Output:** tCO₂ per EF·h by province-month
- **Sequencing:** This is a later phase after the baseline DiD and the CO₂/electricity backbone are in place

### RQ3 — Economic Outcomes (exploratory extension)
How do energy/compute changes relate to provincial economics?
- **Status:** Exploratory extension for program-fit (Chinese economics positioning)
- **Outcomes:** Investment, employment, digital specialization (CAICT tiers)

---

## Progress

### Done ✓
- [x] Repo structure initialized
- [x] Core research notes and plan drafted
- [x] Treatment-date archive started
- [x] Source tracking notes started
- [x] First monthly CO₂ panel built from the local Carbon Monitor CSV export

### In Progress 🔄
- [ ] Build the first verified Gansu electricity extraction workflow
- [ ] Turn source notes into actual collected data
- [ ] Refine the implementation roadmap as real work begins

### To Do ⏳
- [ ] Expand the electricity scraper province by province after Gansu
- [ ] Estimate the baseline models
- [ ] Operationalize CPC after the core panel exists
- [ ] Write thesis chapters

---

## Data Sources

| Data | Source | Frequency | Status |
|------|--------|-----------|--------|
| CO₂ | Carbon Monitor China | Daily | ✓ Identified |
| Electricity | Provincial bulletins | Monthly | Pipeline specified |
| CI | Computed from CO₂/kWh | Monthly | To compute |
| PUE | Policy targets | Trajectory | <1.5 by 2025 |
| GF/W | Green500 + HPL-MxP | Monthly | Method specified |

---

## Folder Structure

```
edwc-thesis/
├── 01_notes/              # Main research notes, source archives, and method notes
├── 02_literature/         # Papers and sources
├── 03_data/               # Empty scaffold for raw, interim, and processed datasets
├── 05_misc/               # Slides, miscellaneous
├── notebooks/             # Placeholder for future analysis notebooks
└── src/                   # Placeholder for future code
```

---

## Quick Reference

**Treated Provinces:** Gansu, Ningxia, Inner Mongolia, Guizhou

**Current local CO₂ file coverage:** the best local Carbon Monitor CSV now spans `2019-01` to `2025-11`, covers `31` provinces, and has been aggregated into `03_data/interim/panel_co2_monthly.csv`.

**T₀ Dates:** Keep these as working anchors only for now. Final province-by-province fact-checking happens later, once the baseline CO₂ and electricity panels are usable.

**Event Window:** [-12, +18] months around T₀

**CPC Formula:**
$$
\text{CPC}_{p,t} = \text{CI}_{p,t} \times \text{PUE}_{p,t} \times \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)}
$$

---

*Last updated: 2026-04-11*
