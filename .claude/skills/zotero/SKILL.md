---
name: zotero
description: Use Zotero safely for this thesis repo: audit the canonical thesis corpus, repair metadata, inspect attachments, resolve duplicates, and write exact status reports via the Zotero Web API first.
---

# Zotero Skill

Use this skill for any Zotero work in this repo.

This repo's Zotero work is not generic library cleanup. The default job is a strict thesis-corpus pass against the canonical literature list in `02_literature/literature_master.md`.

## Defaults

- Primary interface: Zotero Web API.
- Never touch the Zotero SQLite database directly.
- Prefer the bundled helper script at `scripts/zotero_api.py` for API work.
- Use raw `requests` or `curl` only for one-off checks or when the helper script lacks a needed feature.
- For anything beyond a trivial single fetch, use Python rather than `jq`.
- If a required Zotero request fails because the environment blocks network access, rerun it with escalated permissions immediately instead of switching to brittle workarounds.

## Repo Paths

When the task is thesis-corpus normalization or audit, treat these as canonical:

- Master literature file: `/Users/elgask0/REPOS/thesis/02_literature/literature_master.md`
- Local PDF folder: `/Users/elgask0/REPOS/thesis/02_literature/pdf/`
- Final report path: `/Users/elgask0/REPOS/thesis/02_literature/zotero_perfection_report.md`

Keep scratch artifacts in `/tmp/thesis_zotero_*` so they do not pollute the repo.

## Credentials

Export the key before running the helper script:

```bash
export ZOTERO_API_KEY="xn89yDS2E8alvVIip2vVH8pc"
export ZOTERO_USER_ID="18036970"
```

The helper script reads these environment variables automatically.

## Quick Start

```bash
cd /Users/elgask0/REPOS/thesis
export ZOTERO_API_KEY="xn89yDS2E8alvVIip2vVH8pc"

# Inspect one item
python .claude/skills/zotero/scripts/zotero_api.py get ZURREEWR

# Inspect child attachments
python .claude/skills/zotero/scripts/zotero_api.py children ZURREEWR

# Search top-level items only
python .claude/skills/zotero/scripts/zotero_api.py search "10.1257/aer.103.2.897" --top --limit 10

# Fetch the full top-level library in pages
python .claude/skills/zotero/scripts/zotero_api.py all-top > /tmp/thesis_zotero_top_items.json
```

## Thesis-Corpus Workflow

When the user asks for a thesis pass, execute in this order.

### 1. Parse the canonical corpus

Read `02_literature/literature_master.md` and build the source list with:

- citation key
- title
- authors
- year or date
- DOI or URL
- item type
- tags
- stream or bucket
- proposal sections
- priority
- suggested filename or local PDF hint when present

This file is the source of truth for thesis scope. Do not expand the corpus on your own.

### 2. Audit Zotero against the canonical corpus

Audit only top-level Zotero items first.

- Use `/items/top` or the helper's `top` and `all-top` commands.
- Do not use `/items` for library-wide counts without filtering; child attachments and notes will pollute the audit.
- For each canonical source, determine:
  - exact match
  - possible duplicate set
  - metadata completeness
  - tag completeness
  - PDF attachment status
  - whether the current Zotero record is actually the right source

Use the status buckets:

- `clean`
- `missing`
- `duplicate`
- `metadata repair needed`
- `attachment repair needed`
- `manual review needed`

### 3. Add missing items

Before creating an item:

1. Search by DOI.
2. Search by normalized title.
3. Search by author-year when the title is noisy or translated.
4. Check whether a hit is only a placeholder webpage or orphan attachment.

Create the missing item only when you are satisfied that no clean survivor already exists.

### 4. Repair metadata strictly

For thesis-corpus work, do not accept "good enough" metadata if the exact fields can be repaired.

Use authoritative sources in this order when possible:

1. DOI resolver or publisher page
2. Journal page
3. Crossref or official conference proceedings
4. Official institutional source
5. Reputable archive page only if nothing better exists

Repair:

- title
- creators
- date
- publication venue or institution
- DOI
- URL
- item type
- publication fields such as volume, issue, pages, proceedings title, report number, standard number, organization, version number

### 5. Repair tags

For thesis items:

- add every tag specified by `literature_master.md`
- add `thesis`
- do not add generic housekeeping tags such as `added-by-claude-code` unless the user explicitly asks for them
- remove obviously wrong thesis tags only when you are sure they came from a bad duplicate or wrong cross-match

### 6. Repair PDF attachments

Inspect child items with `/items/<key>/children` or the helper's `children` command.

For each thesis item:

- confirm whether a PDF child exists
- verify the PDF belongs to the correct parent item
- check filename, `contentType`, and `linkMode`
- remove or replace wrong attachments only after a survivor item has been chosen

Important attachment rule:

- An attached preprint can satisfy "PDF attached" if the user accepts it, but if the cited version is a journal or conference publication, note clearly in the report when the linked PDF is a preprint rather than the final version.

The helper script supports `imported_file` uploads. If the task specifically requires a linked-file attachment to a local path and the Web API route is awkward, use a safe fallback such as the Zotero local API or the Zotero client.

### 7. Resolve duplicates

Duplicate handling for thesis items should be conservative:

1. Choose the survivor first.
2. Preserve the best metadata on the survivor.
3. Preserve the correct PDF and useful child items.
4. Preserve the correct thesis tags.
5. Delete only the clearly redundant top-level duplicates after the survivor is confirmed.

Common duplicate shapes in this repo:

- full bibliographic item plus placeholder webpage
- full item plus standalone attachment placeholder
- working paper or preprint plus published version
- wrong cross-match that shares one author or keyword but is not the thesis source

### 8. Final verification pass

Do not stop after individual fixes. Re-audit the whole canonical corpus and confirm for every source:

- present in Zotero
- exactly one surviving thesis item
- metadata complete
- tags complete
- `thesis` tag present
- PDF linked if available locally

## Matching Heuristics

Use these tiers in order:

1. DOI exact match
2. Normalized title exact or near-exact match
3. Author-year-title combination
4. Venue and pages for published articles
5. Institution plus title for reports and policy documents

Near-duplicate warning signs:

- same title, different item type
- one record has DOI and one does not
- one record is a webpage shell pointing at the same source
- one record has the correct PDF attached but worse metadata

## Metadata Normalization Rules

Use corporate creators in single-field `name` form when the author is an institution.

Typical mappings:

- journal article: `publicationTitle`, `volume`, `issue`, `pages`, `DOI`
- conference paper: `proceedingsTitle`, `conferenceName`, `publisher`, `pages`, `DOI`
- report: `institution`, `reportType`, `reportNumber`, `place`
- standard: `organization`, `number`, `versionNumber`

For official Chinese policy or institutional documents:

- prefer the issuing body as creator
- keep the original Chinese title when that is the official title
- use the exact issue date when available

## Write Safety

For updates and deletes:

- re-fetch the current item first
- use `If-Unmodified-Since-Version`
- on `412`, re-fetch and retry once
- re-fetch the item after a successful write to confirm the new state

Patch pattern:

1. fetch current item
2. start from `item["data"]`
3. apply field changes
4. remove `key` and `version` from the payload
5. `PATCH` the item

## Helper Script

Bundled helper: `/Users/elgask0/REPOS/thesis/.claude/skills/zotero/scripts/zotero_api.py`

Supported commands:

- `get KEY`
- `children KEY`
- `top`
- `all-top`
- `search QUERY`
- `create PAYLOAD.json`
- `patch KEY CHANGES.json`
- `delete KEY --yes`
- `attach-pdf PARENT_KEY /absolute/path/file.pdf`

Examples:

```bash
python .claude/skills/zotero/scripts/zotero_api.py top --limit 25
python .claude/skills/zotero/scripts/zotero_api.py search "HPL-MxP benchmark" --top
python .claude/skills/zotero/scripts/zotero_api.py patch MU6UDK3X /tmp/greenstone_patch.json
python .claude/skills/zotero/scripts/zotero_api.py attach-pdf ZURREEWR /Users/elgask0/REPOS/thesis/02_literature/pdf/dongarra_luszczek_2026_hpl_mxp.pdf
```

Use the helper by default. Drop to ad hoc Python only when the task is more specialized than the helper supports.

## Reporting Standard for Thesis Passes

If the user requests a full thesis-corpus repair pass, write the final report to:

- `/Users/elgask0/REPOS/thesis/02_literature/zotero_perfection_report.md`

Track at least:

- items added
- metadata repairs
- tag repairs
- attachment repairs
- duplicate resolutions
- missing PDFs
- remaining manual-review items
- one-line final checklist for every canonical source

## Error Handling

Common cases:

- `403`: wrong API key or missing key
- `404`: item key not found
- `409`: write conflict, retry with backoff
- `412`: stale item version, re-fetch and retry
- `429`: rate limit, back off and retry

If Zotero returns JSON that makes shell tooling unhappy, switch to Python immediately.
