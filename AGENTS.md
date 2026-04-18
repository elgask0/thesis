# AGENTS.md — Canonical Instruction File

This file is the canonical source of truth for any agent (Codex, Claude Code, or
otherwise) working in this repository. Read it fully before taking any action.
If any other file in the repo appears to contradict it — including
`CLAUDE.md`, `README.md`, older notes, or draft prose — this file wins.

`CLAUDE.md` is a thin wrapper that routes Claude Code here. Do not treat it as
a second instruction layer. Do not create a third one.

---

## 1. Project Objective

The immediate deliverable is a **master's thesis proposal in English** for the
Master in Chinese Economy at Zhejiang University. The thesis studies the
causal effect of China's Eastern Data, Western Compute (EDWC) program on
provincial electricity consumption, with a complementary translation into
carbon-per-compute (CPC).

The task for agents right now is to **draft the LaTeX proposal, section by
section**, using the existing skeleton, the approved literature corpus, and
the repo's working notes. This is not a research-redesign task, not a
literature-search task, and not an empirical-estimation task.

---

## 2. Thesis Scope (Frozen for the Proposal)

The current thesis logic is fixed. Do not silently change it.

- Two core research questions only.
  - **RQ1.** Causal effect of EDWC go-lives on **provincial electricity
    consumption**. CO₂ is a complementary, secondary outcome — not the
    primary empirical target.
  - **RQ2.** Compute translation through **CPC**, downstream from RQ1.
- Electricity is the main empirical outcome.
- **Sun–Abraham** event-study is the main identification design.
- **Synthetic Gansu (SCM)** is supplementary only.
- Economic outcomes (investment, employment) are **not** a core question.
  Keep them in discussion or appendix framing only if explicitly needed.
- Realism dominates ambition. The proposal is evaluated as a credible plan,
  not as finished research.

Hard limits on claims:

- Do not overclaim electricity-panel readiness. Only Gansu has a verified
  scraped panel; the rest is still province-by-province discovery.
- Do not overclaim treatment-date certainty. The `T0` values in
  `01_notes/edwc_treatment_dates.md` are **working anchors**, to be locked
  with source-backed provenance later.
- Do not claim results. No RQ1 or RQ2 estimates exist yet. Write the
  proposal as a plan, not as a findings report.
- EDWC is a bundled intervention. Interpretation is reduced-form, not
  "pure data center" causality.

---

## 3. Source-of-Truth Hierarchy

When sources disagree, use this priority (highest first):

1. Verified repo state (files actually present, panels actually built,
   scripts that actually run).
2. `thesis-proposal.tex` — the LaTeX skeleton is the **writing target**.
   Its section structure and inline `% PURPOSE` / `% CONTENT` /
   `% REPO SUPPORT` / `% DO NOT OVERCLAIM` comments are binding drafting
   instructions.
3. `literature_master.md` — canonical literature architecture. Defines the
   approved corpus, per-paper analytical function, section mapping, and
   tags. This is the **only** approved source for which papers are used
   where.
4. `01_notes/global_plan.md` — overall research design. Use for conceptual
   framing consistent with the frozen scope in §2.
5. `01_notes/thesis_structure.md` — outline-level guidance where the LaTeX
   skeleton is silent.
6. `01_notes/EDWC_Gansu_EventStudy.md` — technical design reference for the
   empirical-strategy section.
7. `01_notes/edwc_treatment_dates.md` — working `T0` anchors and evidence.
8. `01_notes/electricity_data_pipeline.md`,
   `01_notes/gansu_bulletin_template.md` — electricity feasibility and
   coverage status.
9. `01_notes/AI_equivalent_GFLOPS_per_W.md`,
   `01_notes/caict_series_map.md`,
   `01_notes/renewable_curtailment_extension.md`,
   `01_notes/time_of_use_tariff_reforms.md` — technical inputs for CPC and
   for mechanism/appendix framing.
10. `README.md` — project summary; use for high-level framing only.

Older prose, slide decks, or draft paragraphs **never** override the files
above. If you find stale claims in the prose, correct them against this
hierarchy.

---

## 4. Current Empirical Status (What You May and May Not Assume)

You may assume:

- A monthly CO₂ panel has been built from the local Carbon Monitor export
  and lives at `03_data/interim/panel_co2_monthly.csv`, spanning roughly
  `2019-01` to `2025-11`, 31 provinces.
- Gansu has a verified first scrape: 72 discovered bulletin pages from
  `2020-03` to `2026-02`, with 71 parsed months of monthly total
  electricity consumption and one remaining gap at `2022-06`.
- Working `T0` anchors: Ningxia `2023-02`, Guizhou `2023-09`,
  Gansu `2024-06`, Inner Mongolia `2024-09`.

You may **not** assume:

- That electricity panels exist for any province other than Gansu.
- That treatment dates are final.
- That any DiD, SCM, or CPC estimate has been produced.
- That CI constructed from CO₂/MWh is available outside the current
  Gansu × CO₂ overlap.
- That PUE, `GF/W`, or CPC series have been built.

Write the proposal in a way that is consistent with this state. Describe the
empirical work as a plan, qualify feasibility honestly, and flag remaining
work where the skeleton requests it.

---

## 5. Literature Workflow (Binding)

- `literature_master.md` is the **only** approved source for literature
  architecture. Use its four-stream structure (Outcome, Design, Measurement,
  China Context) and its section mapping (`§1.1`, `§2`, `§3`, `§4`) to
  decide which papers go where.
- Before drafting any subsection, locate the relevant entries in
  `literature_master.md`, read the per-paper `Use in proposal` field, and
  rely on the summary notes for each paper when available at
  `/Users/elgask0/REPOS/thesis/02_literature/` (check
  `02_literature/sources_notes.md` and per-paper `.md` files named in the
  `Filename:` field of each entry).
- Do not cite a paper that is not in `literature_master.md`. If a paper
  seems needed and is not in the master file, stop and flag it to the user
  rather than inventing a citation or reopening literature search.
- Do not reopen literature search. The corpus is frozen for the proposal.
- Do not invent references, DOIs, or quotes.
- The `.bib` file is available at `02_literature/Exported Items.bib` with
  Zotero auto-generated keys (51 entries). These keys are canonical.
- Each entry in `literature_master.md` has a `bib_key` field mapping the
  human-readable `Filename:` stem to the actual Zotero `.bib` key.
  Use the `bib_key` value directly in `\citep{}` commands.
- Do not invent or modify `.bib` keys. If a key seems wrong, flag it to
  the user rather than changing it unilaterally.

---

## 6. Writing Workflow (Binding)

- **Language:** English only.
- **Target file:** `thesis-proposal.tex`. Do not create parallel draft files
  for the same content.
- **Granularity:** draft **one subsection at a time**, then stop. Do not
  draft multiple sections in a single pass. Do not draft the entire
  proposal at once.
- **Skeleton discipline:** replace `[TO BE DRAFTED]` markers only. Leave
  the structural `%` comments in place above each block as drafting
  instructions for future passes. Do not delete `% PURPOSE`,
  `% CONTENT`, `% REPO SUPPORT`, `% STILL NEEDED`, or
  `% DO NOT OVERCLAIM` comments.
- **Style skill:** every prose task — drafting, revising, polishing,
  expanding — must follow the `writing-style` skill. This is the default
  editorial standard for the thesis. See §8.
- **Grounding rule:** every substantive claim must be traceable to either
  (a) an approved paper in `literature_master.md`, or (b) a working note in
  `01_notes/`, or (c) a verified repo artifact. If you cannot trace a
  claim, do not write it.
- **Realism over ambition:** prefer plain, defensible phrasing to
  grandstanding. Match the skeleton's `% DO NOT OVERCLAIM` instructions.
- **No filler:** no AI-academic sludge, no generic scene-setting, no empty
  intensifiers. The `writing-style` skill's blacklist is binding.

---

## 7. Section Drafting Order

Follow this order unless the user explicitly overrides it. The order is
chosen so each section builds on material the previous ones have already
pinned down, and so literature use stays coherent with
`literature_master.md`.

1. `\section{Literature Review}` (§2) — drafted first because it freezes
   how the literature is used elsewhere. Work subsection by subsection in
   the order they appear in the skeleton. Use the stream architecture in
   `literature_master.md` §§1–4 and the explicit mapping table at the end
   of that file.
2. `\section{Research Background and Significance}` (§1) — drafted after
   §2 so that background prose cites the same sources consistently. Work
   subsection by subsection.
3. `\subsection{Research Problem}` and `\subsection{Research Significance}`
   (inside §1) — draft after the background subsections and the literature
   review, so the gap framing matches the rest.
4. `\section{Research Content and Design}` (§3) — RQs, variables, data
   sources, empirical strategy, feasibility, structure. Use
   `01_notes/EDWC_Gansu_EventStudy.md` and `01_notes/global_plan.md` as
   technical anchors. Respect the frozen scope in §2 of this file.
5. `\section{Contributions and Innovations}` (§4) — written after §3 so
   that contributions are stated against the design actually proposed.
6. `\section{Work Already Completed and Current Progress}` (§5) — reflect
   the real repo state in §4 of this file. Do not inflate.
7. `\section{Research Plan and Timeline}` (§6) — conservative, consistent
   with realistic data feasibility.
8. References and front matter last; the `.bib` consolidation pass happens
   at the very end.

Within each section, follow the skeleton's subsubsection order exactly.

---

## 8. Skill Usage Rules

Two skills are relevant to this repo.

### 8.1 `writing-style` skill (binding for prose)

- Invoke implicitly on every drafting, revising, polishing, or expansion
  task. Do not announce it in the output.
- Treat it as the default editorial standard, not as a paraphrase-only
  tool.
- Lexical blacklist, structural rules, and priority rules in the skill
  file are binding. Do not introduce blacklisted vocabulary.
- Preserve user-provided citations, numbers, equations, labels, and
  technical terms exactly.
- Do not invent claims, citations, examples, or data.
- Do not add meta-commentary about the style or the skill in the output.

### 8.2 Zotero skill (if present)

- If a Zotero skill exists anywhere in this repo (search under `skills/`,
  `.claude/skills/`, `05_misc/`, or similar), use it for interactions with
  the Zotero library — fetching metadata, resolving citation keys,
  exporting a `.bib`.
- Treat Zotero as **tooling only**, not as a source of truth for argument
  structure. Argument structure comes from `literature_master.md`.
- If the Zotero skill is not present, do not invent its behavior. Flag it
  to the user and continue drafting with placeholder citation keys per §5.

---

## 9. Citation and Bibliography Rules

- Cite only papers present in `literature_master.md`.
- Use `natbib` commands (`\citep`, `\citet`) consistent with the preamble
  of `thesis-proposal.tex`.
- Use the Zotero auto-generated `.bib` keys listed in the `bib_key`
  field of each `literature_master.md` entry. These keys are canonical.
- Do not hand-insert fabricated DOIs, URLs, or bibliographic entries in
  the `.tex`.
- Do not over-cite. Follow the per-paper `Use in proposal` guidance in
  `literature_master.md`. If a paper says it belongs in §2.1 outcome
  motivation, use it there — not as a drive-by citation elsewhere.

---

## 10. LaTeX Editing Rules

- Edit `thesis-proposal.tex` in place. Do not fork parallel drafts.
- Preserve the preamble, document class, packages, and the titlepage
  block.
- Preserve all structural `%` comments above each section block. They are
  drafting instructions, not leftover scaffolding.
- Replace `[TO BE DRAFTED]` with finished prose when a subsection is
  completed in a given pass.
- Keep math in the existing style (`amsmath` already loaded). Do not
  restructure equations from `EDWC_Gansu_EventStudy.md` or `global_plan.md`
  beyond what the skeleton already contains.
- Use `\subsection`, `\subsubsection`, `\paragraph` as already used in the
  skeleton. Do not introduce new sectioning levels.
- Avoid TikZ or heavy figure packages unless the user explicitly requests
  them.
- Compile-safety: after edits, the file must still compile with `pdflatex`
  plus `bibtex` (or `biber` if switched later). If a change could break
  compilation, stop and flag it.

---

## 11. Prohibited Behaviors and Common Failure Modes

Do not:

- Draft multiple sections at once in a single pass.
- Silently change the two core RQs, elevate economic outcomes into a core
  question, or promote SCM to primary design.
- Treat `T0` dates as final.
- Claim any DiD, SCM, or CPC result.
- Control for CI in the baseline RQ1 specification without an explicit
  justification in text; CI is plausibly post-treatment.
- Cite papers outside `literature_master.md`.
- Invent DOIs, URLs, author lists, or bibliographic metadata.
- Reopen literature search or expand the corpus.
- Introduce blacklisted vocabulary from the `writing-style` skill.
- Produce paper-by-paper narration ("A finds X. B finds Y. C finds Z.")
  in the literature review; synthesize by stream.
- Write persuasive or promotional prose. The target voice is disciplined
  academic exposition.
- Use curtailment-welfare or time-of-use claims as evidence of intraday
  reshaping. Those live in appendix/mechanism framing only.
- Elevate Sichuan/Chongqing into the baseline treated set.
- Create mirrored draft files (`thesis-proposal-v2.tex`, etc.).
- Create a third canonical instruction file beside this one.

---

## 12. Execution Guidance for Agents

When given a drafting task:

1. Read this file in full.
2. Read the specific target subsection in `thesis-proposal.tex`, including
   its `%` comments.
3. Read the relevant entries in `literature_master.md` using its
   paper-to-section mapping.
4. Read the relevant repo note(s) from §3 of this file.
5. If a citation or claim cannot be grounded, stop and ask the user
   rather than fabricating.
6. Draft **one subsection**, following the `writing-style` skill.
7. Replace only the `[TO BE DRAFTED]` marker; leave the `%` comments
   intact.
8. Report briefly: which subsection you drafted, which papers you cited,
   and any unresolved blockers.

When given an ambiguous task, pick the smallest useful next step that is
consistent with §7 and stop. Do not expand scope on your own.

---

## 13. Open Decisions Visible to Agents

These are unresolved and should be surfaced if they become blockers during
drafting. Do not resolve them unilaterally.

- Second province target for electricity scraping after Gansu.
- Exact coverage rule for inclusion in the first kWh estimation sample.
- Final citation-key convention (now resolved: Zotero auto-generated keys in `bib_key` field of `literature_master.md`).
- Final locked `T0` values (currently working anchors).

---

End of `AGENTS.md`.