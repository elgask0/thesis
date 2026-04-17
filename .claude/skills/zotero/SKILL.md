---
name: zotero
description: Manage Zotero library via Web API. Full read/write access. Search, create, tag, and sync items with the project's literature system.
---

# Zotero Library Management

Full read/write access to gask0's Zotero library via the Web API. Search, create, tag, and sync items.

---

# PRINCIPLES

## 1. API Key Handling

**Always store in variable first. Never inline.**

```bash
ZOTERO_KEY="xn89yDS2E8alvVIip2vVH8pc"
curl -s "URL" -H "Zotero-API-Key: ${ZOTERO_KEY}"
```

**Why**: Shell interprets special characters in the key incorrectly when pasted inline.

## 2. Tool Selection

| Operation | Tool | When to Use |
|-----------|------|-------------|
| Single Zotero requests | `curl` | Fetching one item, creating one item |
| Batch Zotero requests | Python `requests` | Fetching all items, bulk operations |
| JSON parsing | Python `json` module | Zotero API responses (contain control characters) |

**Critical**: Zotero API returns JSON with control characters (U+0000-U+001F). `jq` fails parsing these. Use Python for Zotero batch operations.

## 3. Duplicate Prevention

Before adding to Zotero:
1. Search by DOI (most reliable)
2. Search by title if DOI unavailable
3. Check project literature files for existing entry

## 4. Tagging Convention

- `added-by-claude-code` — all Zotero items you create
- `metadata:incomplete` — papers needing manual review

## 5. Incomplete Data Handling

**Time limit rule**: Spend maximum 2-3 minutes per paper trying to find metadata.

If unable to locate paper:
- Tag as `metadata:incomplete` if partial metadata exists
- Move on — better to have 100 complete entries than 0 due to perfectionism

---

# OPERATIONS

## Fetch Zotero Item

```bash
ZOTERO_KEY="xn89yDS2E8alvVIip2vVH8pc"
curl -s "https://api.zotero.org/users/18036970/items/KEY?format=json" \
  -H "Zotero-API-Key: ${ZOTERO_KEY}" \
  -H "Zotero-API-Version: 3"
```

## Search Zotero

```bash
# By keyword
curl -s "https://api.zotero.org/users/18036970/items?q=QUERY&format=json&limit=25" \
  -H "Zotero-API-Key: ${ZOTERO_KEY}" \
  -H "Zotero-API-Version: 3"

# By tag
curl -s "https://api.zotero.org/users/18036970/items?tag=TAGNAME&format=json" \
  -H "Zotero-API-Key: ${ZOTERO_KEY}" \
  -H "Zotero-API-Version: 3"
```

## Create Zotero Item

```bash
curl -X POST "https://api.zotero.org/users/18036970/items" \
  -H "Zotero-API-Key: ${ZOTERO_KEY}" \
  -H "Content-Type: application/json" \
  -H "Zotero-API-Version: 3" \
  -d '[{...item_data...}]'
```

Response contains new key: `{"success": {"0": "NEWKEY"}, ...}`

---

# BATCH OPERATIONS

## Fetch All Zotero Keys

Use Python for batch Zotero operations:

```python
import requests

ZOTERO_KEY = "xn89yDS2E8alvVIip2vVH8pc"
BASE_URL = "https://api.zotero.org/users/18036970/items/top"

headers = {"Zotero-API-Key": ZOTERO_KEY, "Zotero-API-Version": "3"}

all_keys = []
start = 0

while True:
    params = {"format": "json", "limit": 100, "start": start}
    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()

    if not data:
        break

    all_keys.extend([item["key"] for item in data if item.get("key")])

    if len(data) < 100:
        break

    start += 100

# Save to file
with open("/tmp/zotero_keys.txt", "w") as f:
    f.write("\n".join(sorted(set(all_keys))))
```

---

# PATTERNS

## Pattern: Add Single Paper

```
1. Resolve metadata via CrossRef or other academic search
2. Search Zotero for duplicate (by DOI, then title)
3. If found → stop
4. Create Zotero item with metadata + tags
5. Check project literature files for existing entry
6. If exists → update, don't duplicate
7. Create literature entry with template below
```

## Pattern: Sync Zotero with Local Literature

```
1. Fetch all Zotero keys (use Python)
2. Extract cited papers from local literature files
3. Find: papers in local files but not in Zotero
4. For each missing paper:
   a. Try to find via academic search
   b. If found: add to Zotero, update local reference
   c. If not found: tag incomplete
5. Verify all non-empty keys exist in Zotero
6. Report final status
```

---

# LITERATURE NOTE TEMPLATE

**Filename**: `@AuthorLastName_Year.md`

**Citekey**: `author_year` (lowercase, underscore). Multiple: `smith_doe_2024`. Disambiguate: `smith_2024a`.

```markdown
---
title: "{{title}}"
authors: [{{authors}}]
year: {{year}}
DOI: "{{doi}}"
citekey: "{{citekey}}"
zotero_key: "{{zotero_key}}"
tags: [source-note, {{topic}}]
created_by: claude-code
date_added: {{YYYY-MM-DD}}
---

# {{title}}

**Authors**: {{authors}} | **Year**: {{year}} | **Journal**: {{venue}}
**DOI**: [{{doi}}](https://doi.org/{{doi}}) | **Zotero**: [Open](zotero://select/library/items/{{zotero_key}})

## Abstract

{{abstract}}

## Key Findings

-

## Notes

-
```

---

# ERROR HANDLING

## API Errors

| Code | Meaning | Action |
|------|---------|--------|
| 403 | Invalid key | Use `${ZOTERO_KEY}` variable |
| 404 | Not found | Key doesn't exist, search by title |
| 409 | Conflict | Library locked, retry in 2s |
| 412 | Precondition failed | Version conflict, re-fetch version |
| 429 | Rate limited | Wait 10-15s |

## jq Parse Error

**Symptom**: `jq: parse error: Invalid string: control characters...`

**Cause**: Zotero API responses contain control characters

**Solution**: Use Python instead of bash/jq for Zotero operations

## Empty zotero_key in Literature Entry

**Causes**:
- Incomplete metadata → tag `metadata:incomplete`
- Missing Zotero entry → find paper via academic search, add to Zotero, update entry

---

# CREDENTIALS

- **API Key**: `xn89yDS2E8alvVIip2vH8pc`
- **User ID**: `18036970`
- **Base URL**: `https://api.zotero.org/users/18036970`
