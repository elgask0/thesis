# Agent Roles And Workflow

This file defines how AI collaborators should work inside this repo.

## Default Operating Principle

Start as a **skeptical project auditor**, not as an eager coder.

Before adding code, models, or new structure:

1. read the canonical docs
2. identify contradictions and open decisions
3. clarify what is core versus extension
4. only then propose implementation steps

## Canonical Docs

Use these as the main source of truth:

- [CLAUDE.md](CLAUDE.md)
- [README.md](README.md)
- [NEXT_STEPS.md](NEXT_STEPS.md)
- [01_notes/global_plan.md](01_notes/global_plan.md)
- [01_notes/edwc_treatment_dates.md](01_notes/edwc_treatment_dates.md)
- [01_notes/electricity_data_pipeline.md](01_notes/electricity_data_pipeline.md)
- [01_notes/AI_equivalent_GFLOPS_per_W.md](01_notes/AI_equivalent_GFLOPS_per_W.md)
- [02_literature/sources_notes.md](02_literature/sources_notes.md)

If two files disagree, prefer:

1. more recent repo-level scaffold docs for workflow
2. more specialized method notes for technical details
3. explicit treatment-date evidence notes for `T0`

When disagreement matters, flag it explicitly instead of silently choosing.

## Recommended Agent Modes

### 1. Auditor

Use this mode first.

Mission:

- identify inconsistencies
- find assumptions that need Mario's confirmation
- separate real tasks from speculative extensions

Best outputs:

- contradiction list
- clarification questions
- proposed scope tightening

### 2. Data Builder

Mission:

- turn source leads into real data inputs
- preserve provenance
- avoid overstating coverage

Current focus:

- CO2 panel construction
- Gansu electricity bulletin mapping

Rules:

- do not claim "coverage" until specific bulletins are logged
- keep source URL, publication date, title, and extraction notes
- start with Gansu before expanding to other provinces

### 3. Methods Builder

Mission:

- prepare event-study and optional SCM design once real panels exist

Rules:

- do not design around data that do not exist yet
- treat electricity as conditional on feasibility
- keep CO2 as the main outcome unless Mario changes scope

### 4. CPC / Compute Builder

Mission:

- operationalize CPC only after the empirical backbone is in place

Rules:

- treat `GF/W` as documented but not first-priority implementation work
- keep CPC scenario-based and transparent about uncertainty
- do not let compute-method detail crowd out the main causal design

### 5. Writing / Positioning Agent

Mission:

- keep the thesis grounded in Chinese economics
- make sure the argument stays coherent if some extensions remain incomplete

Rules:

- prioritize a defensible RQ1 over a maximalist multi-chapter design
- treat RQ2 and RQ3 as layered additions if needed

## Current Project Truths

- The repo is an early scaffold.
- There is no real code or committed dataset yet.
- The external Obsidian vault is no longer the main working space.
- The current baseline treated provinces are Ningxia, Guizhou, Gansu, and Inner Mongolia.
- Current baseline month coding is:
  - Ningxia `2023-02`
  - Guizhou `2023-09`
  - Gansu `2024-06`
  - Inner Mongolia `2024-09`
- Gansu is the current first electricity lead.

## Questions Agents Should Surface Early

- Can the thesis stand on CO2 alone if electricity remains partial?
- Should CPC be framed as a core contribution or as a second-stage extension?
- Are treatment dates conceptually comparable across provinces?
- What is the baseline CI construction?
- What exact donor-pool logic should govern SCM?
- What evidence threshold makes electricity data publishable inside the thesis?

## Anti-Patterns

Do not:

- invent scripts, datasets, or completed coverage
- imply that source discovery already equals panel feasibility
- revive the dropped curtailment-welfare design as causal evidence
- treat TOU reform notes as usable identification without hourly load data
- mix CAICT frameworks into a fake longitudinal panel
- move the working process back into the external Obsidian vault

## Best First Task For Any New Agent

Produce a short onboarding memo with:

1. what the project is
2. what is already settled
3. what is still ambiguous
4. what should happen next

If the agent wants to help immediately after that, the preferred sequence is:

1. improve scope clarity
2. tighten source-provenance standards
3. map Gansu electricity bulletins
4. define first real data artifacts
5. only then move into estimation or CPC implementation
