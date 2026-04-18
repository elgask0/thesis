# Gansu Electricity Scraper

This folder contains the first province-specific scraper scaffold for monthly electricity bulletins from the Gansu Provincial Department of Industry and Information Technology.

## Why This Approach

Direct HTTP fetches do not work reliably for this site:

- `curl` returns an anti-bot shell
- Python `requests` / `urllib` only see the challenge page
- Selenium with Chrome launched successfully but still received an empty DOM for both the homepage and article pages
- Plain headless Chrome `--dump-dom` also returned an empty DOM during testing

The first approach that worked was:

- Python
- Chrome DevTools Protocol
- a real Chrome browser session
- rendered page HTML pulled through CDP

## Current Scope

Only Gansu for now.

The scripts are intentionally split into:

1. search-result discovery
2. article fetch and parse

Do not treat this as the final all-province architecture yet.

## Scripts

### `discover_bulletins.py`

Loads the Gansu search-results page in Chrome, parses result cards, and writes a CSV or JSON file of candidate bulletins.

Example:

```bash
conda run -n edwc-thesis python src/electricity/gansu/discover_bulletins.py \
  --output 03_data/interim/gansu_bulletins.csv
```

### `fetch_article.py`

Loads one article URL in Chrome, extracts metadata and the article body, and optionally writes parsed JSON plus raw HTML.

Example:

```bash
conda run -n edwc-thesis python src/electricity/gansu/fetch_article.py \
  --url https://gxt.gansu.gov.cn/gxt/jjyx/202603/174299309.shtml \
  --output 03_data/interim/gansu_article_2026-02.json \
  --save-html 03_data/raw/electricity_bulletins/gansu/2026-02.html
```

### `scrape_all.py`

Discovers bulletin pages, fetches every article, saves raw HTML and parsed JSON, and writes a first monthly panel.

Example:

```bash
conda run -n edwc-thesis python src/electricity/gansu/scrape_all.py \
  --output-dir 03_data/interim/gansu_scrape \
  --raw-html-dir 03_data/raw/electricity_bulletins/gansu
```

### `rebuild_panel.py`

Rebuilds the parsed article JSON files and the monthly panel from already saved raw HTML, which is useful after parser improvements.

Example:

```bash
conda run -n edwc-thesis python src/electricity/gansu/rebuild_panel.py
```

### `build_structured_panel.py`

Builds the wide structured Gansu panel from the canonical monthly panel and parsed article JSON files.

Example:

```bash
conda run -n edwc-thesis python src/electricity/gansu/build_structured_panel.py
```

## Current Saved Snapshot

The repo's saved Gansu scrape snapshot currently contains:

- `72` discovered bulletin pages
- coverage from `2020-03` through `2026-02`
- `72` months with parsed monthly total electricity consumption
- `71` months parsed directly from the original Gansu article text
- `1` source-level exception at `2022-06`, where the original Gansu page renders an empty article body and the canonical panel uses a mirrored Tianshui government repost instead

A fresh live run may return newer months beyond this stored snapshot.

## Notes

- This is a browser-assisted Python scraper, not a pure HTTP scraper.
- Selenium with Chrome and plain headless Chrome `--dump-dom` both failed on the live site.
- Chrome only worked in a real browser session through DevTools Protocol.
- The maintained pipeline is Chrome-only and uses the non-headless path because that is the one that worked reliably on the live site.
- Run these scripts from the `edwc-thesis` conda environment.
