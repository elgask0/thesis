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

**AI onboarding:** Any assistant connected to this repo should read [CLAUDE.md](CLAUDE.md) first, then [AGENTS.md](AGENTS.md).

---

## Quick Overview

**Research Question:** What is the causal effect of China's EDWC program on provincial CO₂ emissions, electricity consumption, and AI compute?

**Methods:** Sun-Abraham event-study + Synthetic Control (Gansu, optional)

**Key Contribution:** Translating energy effects into AI-native Carbon-per-Compute (CPC) metrics

---

## Where to Start

| What to Read | Why |
|--------------|-----|
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
- **Outcomes:** Daily CO₂ (primary), monthly kWh (secondary)

### RQ2 — Compute Translation
What is the implied Carbon-per-Compute (CPC) before and after EDWC?
- **Method:** CPC = CI × PUE × (1000/GF/W)
- **Output:** tCO₂ per EF·h by province-month

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

### In Progress 🔄
- [ ] Build CO₂ panel (daily → monthly)
- [ ] Map Gansu electricity bulletin structure
- [ ] Turn source notes into actual collected data
- [ ] Refine the implementation roadmap as real work begins

### To Do ⏳
- [ ] Build the electricity panel
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
├── 04_drafts/             # Working drafts
├── 05_misc/               # Slides, miscellaneous
├── notebooks/             # Placeholder for future analysis notebooks
└── src/                   # Placeholder for future code
```

---

## Quick Reference

**Treated Provinces:** Gansu, Ningxia, Inner Mongolia, Guizhou

**T₀ Dates:**
- Ningxia: 2023-02 (platform go-live)
- Guizhou: 2023-09 (DC put into use; 2024-06 migration robustness)
- Inner Mongolia: 2024-09 (Jiuzhou center go-live)
- Gansu: 2024-06

**Event Window:** [-12, +18] months around T₀

**CPC Formula:**
$$
\text{CPC}_{p,t} = \text{CI}_{p,t} \times \text{PUE}_{p,t} \times \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)}
$$

---

*Last updated: 2026-04-11*
