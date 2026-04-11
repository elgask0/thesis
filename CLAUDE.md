# Claude Onboarding

This file is the fastest way for Claude to gain working context on this repo.

## Project Snapshot

- **Project:** Master's thesis on China's **Eastern Data, Western Compute (EDWC)** program
- **Author:** Mario D.M.
- **Program:** Chinese Economy at Zhejiang University
- **Repo status:** early scaffold only
- **Canonical workspace:** this repo, not the external Obsidian vault

The repo currently contains:

- research notes
- source archives
- treatment-date evidence
- a thesis plan
- a roadmap

The repo does **not** yet contain:

- real analysis code
- downloaded raw datasets
- cleaned panels
- finished estimation outputs

## What The Thesis Is Trying To Do

### Baseline question

Estimate the reduced-form effect of EDWC go-live on provincial:

- CO2 emissions
- electricity consumption, if the data prove workable

### Secondary / extension question

Translate the energy and emissions environment into **Carbon-per-Compute (CPC)** using:

- carbon intensity
- PUE
- AI-equivalent compute efficiency (`GF/W`)

### Exploratory extension

Relate EDWC-linked energy / compute changes to provincial economic positioning.

## Read Order

Read these files in this order before proposing changes:

1. [README.md](README.md)
2. [NEXT_STEPS.md](NEXT_STEPS.md)
3. [01_notes/global_plan.md](01_notes/global_plan.md)
4. [01_notes/edwc_treatment_dates.md](01_notes/edwc_treatment_dates.md)
5. [01_notes/electricity_data_pipeline.md](01_notes/electricity_data_pipeline.md)
6. [01_notes/AI_equivalent_GFLOPS_per_W.md](01_notes/AI_equivalent_GFLOPS_per_W.md)
7. [02_literature/sources_notes.md](02_literature/sources_notes.md)
8. [01_notes/caict_series_map.md](01_notes/caict_series_map.md)
9. [01_notes/time_of_use_tariff_reforms.md](01_notes/time_of_use_tariff_reforms.md)
10. [01_notes/renewable_curtailment_extension.md](01_notes/renewable_curtailment_extension.md)

Optional after that:

- [01_notes/EDWC_Gansu_EventStudy.md](01_notes/EDWC_Gansu_EventStudy.md)
- [04_drafts/working_paper.md](04_drafts/working_paper.md)
- [01_notes/thesis_structure.md](01_notes/thesis_structure.md)

## Current Ground Truth

- The repo is intentionally **notes-first** right now.
- `NEXT_STEPS.md` is **orientative**, not a rigid execution plan.
- The first operational data task is **Gansu electricity source mapping**, not a full cross-province electricity panel.
- The first empirical backbone is **CO2**, because that data path is much clearer.
- `GF/W` / CPC methodology is documented, but it is **not** the first implementation priority.
- The current treated provinces are:
  - Ningxia
  - Guizhou
  - Gansu
  - Inner Mongolia
- Current baseline `T0` coding is:
  - Ningxia: `2023-02`
  - Guizhou: `2023-09`
  - Gansu: `2024-06`
  - Inner Mongolia: `2024-09`

## How To Think About The Repo

Treat the project as having three layers:

1. **Core empirical layer**
   - CO2 panel
   - treatment timing
   - event-study / optional SCM

2. **Data feasibility layer**
   - electricity bulletins
   - source provenance
   - coverage and extraction realism

3. **Translation / extension layer**
   - CPC
   - compute scenarios
   - CAICT benchmarking
   - economic extension

If there is tension between layers, prioritize the **core empirical layer** first.

## What Needs Pressure-Testing

When reading the repo, focus on inconsistencies, hidden assumptions, and questions that should be clarified with Mario before implementation hardens.

Priority questions:

1. Is electricity a true secondary outcome, or should the thesis be framed so it can still succeed if electricity coverage stays weak?
2. Is CPC a core contribution from day one, or a staged extension after the CO2/event-study backbone exists?
3. Is treatment timing being defined consistently across provinces:
   - platform / dispatch go-live
   - physical data center operation
   - migration completion
4. What should be the baseline carbon-intensity construction:
   - Carbon Monitor CO2 divided by monthly electricity
   - generation-mix-based CI
5. Will the main estimation be monthly from the start, or will daily CO2 ever be used directly?
6. What donor-pool rules should govern the optional Gansu SCM?
7. What is the minimum evidence standard before claiming electricity coverage is "usable"?

## Things You Should Not Assume

- Do **not** assume the repo already contains real data.
- Do **not** assume `src/` or `notebooks/` are implemented.
- Do **not** assume the external Obsidian vault is still the working source of truth.
- Do **not** assume hourly electricity data exist.
- Do **not** revive the curtailment-welfare design as a causal chapter without new intraday data.
- Do **not** treat all CAICT frameworks as one clean panel without checking methodological comparability.

## First Useful Output From Claude

After reading the repo, the most useful first response is a short memo with:

1. the top inconsistencies or ambiguities
2. the top questions Claude needs Mario to answer
3. a proposed tightening of scope
4. the best immediate next actions for the repo

The ideal outcome is not more theory. It is a cleaner path to:

- build the first panel
- document provenance
- decide what is core versus extension

## Immediate Working Priorities

If Claude is asked to help move the repo forward, the recommended order is:

1. sanity-check scope and open questions
2. sharpen `CLAUDE.md` and `AGENTS.md` if needed
3. improve the Gansu electricity source-mapping plan
4. define the first real data artifacts to create
5. only then move into code, estimation, or CPC construction
