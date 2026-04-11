---
title: "EDWC Thesis — Eastern Data, Western Compute in China"
description: "Master's thesis examining causal effects of China's EDWC program on provincial CO₂ emissions, electricity consumption, and AI-relevant Carbon-per-Compute metrics"
status: active
tags: [project, thesis, economics, china, energy, AI, EDWC]
---

# Eastern Data, Western Compute (EDWC) Thesis

Master's thesis in Chinese Economy at Zhejiang University.

**Author:** Mario D.M.
**Last Updated:** 2026-02-19

---

## Quick Overview

**Research Question:** What is the causal effect of China's EDWC program on provincial CO₂ emissions, electricity consumption, and AI compute?

**Methods:** Sun-Abraham event-study + Synthetic Control (Gansu)

**Key Contribution:** Translating energy effects into AI-native Carbon-per-Compute (CPC) metrics

---

## Where to Start

| What to Read | Why | Length |
|--------------|-----|--------|
| **[[NEXT_STEPS.md|Next Steps →]]** | Action roadmap, start here for work! | - |
| **[[01_notes/global_plan.md|Global Plan]]** | Complete research design (RQ1-RQ3, data, methods) | 722 lines |
| **[[01_notes/EDWC_Gansu_EventStudy.md|Working Paper]]** | Current draft of the thesis | 352 lines |
| **[[01_notes/AI_equivalent_GFLOPS_per_W.md|GF/W Methodology]]** | How we build the CPC metric | 213 lines |
| **[[01_notes/thesis_structure.md|Structure]]** | Chapter-by-chapter outline | 257 lines |

---

## Research Questions

### RQ1 — Causal Effects
What is the effect of EDWC go-live on provincial CO₂ and electricity?
- **Method:** Event-study (Sun-Abraham) + Synthetic Control (Gansu)
- **Outcomes:** Daily CO₂ (primary), monthly kWh (secondary)

### RQ2 — Compute Translation
What is the implied Carbon-per-Compute (CPC) before and after EDWC?
- **Method:** CPC = CI × PUE × (1000/GF/W)
- **Output:** tCO₂ per EF·h by province-month

### RQ3 — Economic Outcomes
How do energy/compute changes relate to provincial economics?
- **Outcomes:** Investment, employment, digital specialization (CAICT tiers)

---

## Progress

### Done ✓
- [x] Research design (RQ1-RQ3 finalized)
- [x] Data sources identified (CO₂, electricity, PUE, GF/W)
- [x] Empirical strategy (Sun-Abraham + SCM)
- [x] Treatment dates documented (T₀ for each province)

### In Progress 🔄
- [ ] Build CO₂ panel (daily → monthly)
- [ ] Build kWh panel (scraping + API)
- [ ] Estimate event-study
- [ ] Build synthetic Gansu

### To Do ⏳
- [ ] Construct CPC series
- [ ] Estimate RQ3
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
├── 01_notes/              # Research documentation
│   ├── global_plan.md              # START HERE - Complete plan
│   ├── EDWC_Gansu_EventStudy.md    # Working paper draft
│   ├── AI_equivalent_GFLOPS_per_W.md  # CPC methodology
│   └── thesis_structure.md         # Chapter outline
├── 02_literature/         # Papers and sources
├── 03_data/               # Raw, interim, processed datasets
├── 04_drafts/             # Working drafts
├── 05_misc/               # Slides, miscellaneous
├── notebooks/             # Jupyter analysis notebooks
└── src/                   # Data collection code
```

---

## Quick Reference

**Treated Provinces:** Gansu, Ningxia, Inner Mongolia, Guizhou

**T₀ Dates:**
- Ningxia: 2023-07-21
- Guizhou: 2023-12 / 2024-01
- Inner Mongolia: 2024-04-28
- Gansu: 2024-06

**Event Window:** [-12, +18] months around T₀

**CPC Formula:**
$$
\text{CPC}_{p,t} = \text{CI}_{p,t} \times \text{PUE}_{p,t} \times \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)}
$$

---

*Last updated: 2026-02-19*
