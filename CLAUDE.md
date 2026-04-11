# Claude Guide

This repo is the canonical workspace for an early-stage master's thesis on China's Eastern Data, Western Compute (EDWC) program.

Right now the defensible baseline is narrower than some draft materials make it sound:

- Core thesis backbone: EDWC go-live timing plus matched provincial CO2 and electricity outcomes.
- CO2 is easier to assemble first; electricity is equally important baseline work and must be built province by province starting with Gansu.
- CPC / `GF/W` / PUE / CI translation is a key later module, but it is not the first implementation task.

There is still no real analysis code and no committed datasets in this repo.

## Current Reality

- The repo contains useful notes, but not all notes are equally current.
- Some documents are aspirational research designs rather than binding execution plans.
- The slide deck in `05_misc/slides/` contains older treatment timings and premature coverage claims; treat it as historical context, not current truth.
- Source discovery is not the same thing as data feasibility.

## Read Order

When orienting to the project, read in this order:

1. `README.md`
2. `NEXT_STEPS.md`
3. `01_notes/edwc_treatment_dates.md`
4. `01_notes/electricity_data_pipeline.md`
5. `01_notes/global_plan.md`
6. `01_notes/thesis_structure.md`
7. The relevant `03_data/*/README.md` files and `02_literature/sources_notes.md`

## Truth Hierarchy

When documents disagree, use this priority:

1. Verified repo state and source evidence
2. `01_notes/edwc_treatment_dates.md` for treatment timing
3. `01_notes/electricity_data_pipeline.md` for electricity feasibility
4. `README.md` and `NEXT_STEPS.md` for current work order
5. `01_notes/global_plan.md` for broader design ideas
6. `05_misc/slides/` as historical material

## Canonical Notes

The repo now keeps the main conceptual and drafting notes in `01_notes/`.

Do not recreate mirrored draft copies of the same document in multiple folders.

## Core vs Extension

### Core now

- Lock EDWC treatment dates with source-backed provenance.
- Build the CO2 backbone from Carbon Monitor.
- Build the electricity backbone province by province, starting with Gansu.
- Define minimal schemas and provenance rules for treatment, CO2, and electricity data.
- Run the baseline RQ1 work once the first usable CO2 and kWh panels exist.

### Later core

- The baseline DiD on CO2 and kWh
- CI constructed on real overlap between CO2 and electricity data
- A simple CPC translation layer built on documented observed inputs after the baseline DiD backbone exists

### Extension

- Bespoke `GF/W` series construction and Monte Carlo bands
- Synthetic Control for Gansu
- CAICT-driven heterogeneity beyond basic donor logic
- Economic outcomes for "program fit"
- Renewable curtailment / utilization appendices
- Time-of-use tariff mechanism work
- Dashboards, procurement guidance, credit-risk products, or other applied products

## Working Rules

- Audit first, build second.
- Do not invent coverage, pipelines, or empirical results.
- Do not assume electricity data are feasible because a search URL exists.
- Do not make `GF/W`, CPC, or dashboards the first coding task.
- Do not revive the dropped curtailment-welfare design without hourly data.
- Do not use time-of-use tariff notes as evidence of actual intraday reshaping.
- Preserve provenance for every empirical source: URL, publication date, title, and raw file or text location.
- For electricity extraction, build a manual seed set before automating anything.
- Do not claim province coverage until month-level evidence is logged.

## Methodological Guardrails

- Treat EDWC as a bundled intervention. Baseline claims are reduced-form, not "pure data center" effects.
- Do not control for CI in the baseline RQ1 specification unless there is explicit methodological justification; it is plausibly post-treatment and in some notes is constructed from the same outcome family.
- Do not force a CPC module with modeled CI just to preserve the original vision if the electricity backbone is weak.
- Do not promise a uniform `[-12, +18]` event window without checking the actual post-treatment support for late-treated provinces.
- Keep Sichuan/Chongqing outside the baseline treated set unless there is a deliberate redesign.

## Good First Actions

If a task is underspecified, prefer one of these:

1. Build or QA the monthly CO2 backbone.
2. Expand the treatment-date evidence log.
3. Map Gansu electricity bulletins and prove one extraction template by hand.
4. Turn the verified Gansu workflow into the first reusable province scraper path.
5. Tighten schemas, provenance logs, or minimal analysis inputs.

Everything else should usually wait on those steps.
