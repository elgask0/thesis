# Agent Guide

This repo is still a scaffold, so agents should optimize for clarity, provenance, and scope control before speed.

## Default Posture

Any agent entering this repo starts as an auditor.

Before building code, workflows, or timelines:

1. read the relevant notes
2. decide whether the task belongs to the core thesis or an extension
3. surface hidden assumptions or contradictions
4. only then implement the smallest useful next step

## Canonical Docs

Use these as the current project anchors:

- `README.md` for the project summary
- `NEXT_STEPS.md` for current sequencing
- `01_notes/edwc_treatment_dates.md` for baseline treatment timing
- `01_notes/electricity_data_pipeline.md` for electricity feasibility and provenance expectations
- `01_notes/global_plan.md` for the broad research design
- `01_notes/thesis_structure.md` for the canonical outline

Treat this as historical context:

- `05_misc/slides/supervisor_meeting_slides.pdf`

## Single-Source Rule

Keep one canonical copy of each major note.

Do not recreate mirrored draft files of the same content in multiple folders.

## Agent Roles

One person can wear multiple hats, but the responsibilities should stay distinct.

### 1. Auditor / Orienter

- Reads the repo state and relevant notes
- Checks whether the task is core, conditional, or extension
- Flags contradictions before work starts

### 2. Source and Provenance Lead

- Owns treatment-date evidence
- Owns electricity bulletin discovery and source logs
- Preserves URL, date, title, and raw-source provenance

### 3. Panel Builder

- Builds schemas, download scripts, cleaning steps, and QA checks
- Does not claim coverage until source logging proves it
- Starts with CO2 and only then expands to electricity

### 4. Baseline Analyst

- Owns the first defensible RQ1 backbone
- Works on treatment coding, CO2 panels, and baseline event-study inputs
- Treats CO2 and electricity as co-equal baseline outcomes while sequencing the work pragmatically

### 5. Extension Analyst

- Handles SCM, CPC, `GF/W`, PUE, CI variants, CAICT heterogeneity, and economic outcomes
- Starts only after the baseline DiD backbone exists

### 6. Drafting Agent

- Updates prose, tables, and figures from verified empirical work
- Does not write speculative findings as if they already exist

## Core vs Extension

### Core baseline

- Treatment timing with source-backed evidence
- CO2 panel construction
- Gansu-first electricity scraping and expansion province by province
- Minimal treatment and analysis schemas
- Baseline RQ1 estimation plan and later implementation

### Later core

- The baseline DiD on both CO2 and electricity
- Simple CI and CPC translation built on observed overlap after the baseline DiD exists

### Extension

- Full bespoke `GF/W` module
- Monte Carlo CPC uncertainty
- Synthetic Control for Gansu
- CAICT tier heterogeneity beyond basic donor matching
- Economic outcomes
- Renewable-utilization and time-of-use appendices
- Private-sector dashboards, procurement tools, credit-risk outputs

## Handoff Rules

Every meaningful handoff should state:

- what is verified
- what is still an assumption
- which files are canonical for this task
- which source URLs or raw files back the claim
- what the next blocker is

Use explicit labels where helpful:

- `verified`
- `working assumption`
- `extension`

## Method Guardrails

- EDWC is a bundled intervention; do not oversell "pure data center" causality.
- Do not use CI as a baseline control in RQ1 unless that choice is explicitly defended; it is plausibly post-treatment and may be outcome-derived.
- Do not promise electricity coverage from search leads alone.
- Do not automate extraction before a manual template has been proven.
- Do not design around hourly demand-shifting, curtailment welfare, or TOU response without hourly data.
- Do not turn speculative products or dashboards into baseline thesis tasks.

## Open Decisions For Mario

These are the main unresolved choices the repo should keep visible:

- After Gansu, which province should be the second electricity scraper target?
- What exact coverage rule should trigger inclusion in the first kWh estimation sample if treated-province coverage ramps unevenly?

## Anti-Patterns

Do not:

- invent completed pipelines
- overstate data coverage
- treat historical slides as current ground truth
- conflate platform go-live and physical-capacity go-live without saying which is used
- recreate mirrored draft files that can drift
- turn ambitious extensions into the default next step
