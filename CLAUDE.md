# Claude Bootstrap

This file is intentionally temporary.

It is **not** the final onboarding document for this repo.

Your first job is to read the repository yourself, build your own understanding, identify inconsistencies or hidden assumptions, ask Mario the questions that matter, and then rewrite this file and `AGENTS.md` from your own repo audit.

## First Task

Before proposing code, workflow, or structure:

1. Read the repo carefully.
2. Treat all Markdown docs as candidate context, not unquestioned truth.
3. Produce a short memo for Mario with:
   - inconsistencies or contradictions you found
   - assumptions that need confirmation
   - scope risks or places where the project is too ambitious
   - what should be treated as core versus extension
   - the best immediate next actions
4. Ask Mario only the clarifying questions that are genuinely important.
5. After that, rewrite `CLAUDE.md` and `AGENTS.md` so they reflect your own understanding of the repo.

## Read Everything

This repo is still small enough that you should inspect **all important Markdown docs**, especially:

- `README.md`
- `NEXT_STEPS.md`
- `01_notes/`
- `02_literature/`
- `03_data/*/README.md`
- `04_drafts/`

## Current Working Reality

Do not lose sight of these facts while auditing:

- The repo is still an early scaffold.
- There is no real analysis code yet.
- There are no committed datasets yet.
- This repo folder is now the canonical workspace.
- The external Obsidian vault is no longer the main working location.

## Behavioral Rules

- Audit first, build later.
- Do not invent scripts, datasets, or completed coverage.
- Do not assume electricity data are already feasible just because source leads exist.
- Do not assume CPC / `GF/W` implementation should be the first coding task.
- Do not revive the dropped curtailment-welfare design as causal evidence unless new intraday data appear.
- Do not treat time-of-use tariff notes as proof of hourly demand reshaping without hourly load data.

## What A Good First Response Looks Like

The first useful output is a memo with:

1. what the thesis appears to be doing
2. what seems settled
3. what seems inconsistent or under-specified
4. what Mario should clarify
5. what the repo should do next

## Then Replace This File

Once you have read the repo and spoken with Mario, replace this bootstrap file with a proper project-level `CLAUDE.md`.
