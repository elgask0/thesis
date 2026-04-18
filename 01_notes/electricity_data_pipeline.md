# Electricity Data Pipeline

Working note for the electricity bulletin collection and extraction process used in the EDWC thesis project.

## Purpose

- Track provincial bulletin sources
- Record extraction steps for monthly electricity data
- Document cleaning issues and coverage gaps

## Current Context

- Raw bulletin files are stored in `../03_data/raw/electricity_bulletins/`
- Intermediate monthly panels will be created in `../03_data/interim/`
- The target is province-month coverage for treated provinces with clear provenance
- Python collection and parsing scripts should run from the `edwc-thesis` conda environment
- Gansu now has a verified first scrape and panel rebuild; other provinces still need province-by-province discovery
- Availability should be discovered by trying province by province, not by estimating confidence in advance
- For Gansu specifically, direct HTTP scraping is currently blocked by the site's anti-bot layer; the working technical path is browser-assisted fetching through a real Chrome session driven from Python over DevTools Protocol

## Source Leads

### Gansu

- Institution: 甘肃省工业和信息化厅 / Gansu Provincial Department of Industry and Information Technology
- Search endpoint: [Gansu electricity search results](https://gxt.gansu.gov.cn/guestweb4/s?siteCode=6200000082&checkHandle=1&pageSize=10&left_right_index=0&searchWord=%E5%85%A8%E7%9C%81%E7%94%B5%E5%8A%9B%E7%94%9F%E4%BA%A7%E8%BF%90%E8%A1%8C%E6%83%85%E5%86%B5)
- Search phrase: `全省电力生产运行情况`
- Current status: starting lead only
- Use: candidate bulletin index for monthly Gansu electricity production and consumption updates
- Extraction note: preserve the search term, publication date, bulletin title, and final article URL for each hit so the monthly panel has source-level provenance

## Extraction Notes

- For search-based bulletin sources, save both the search results page and the resolved article URL.
- Track recurring title patterns separately from numeric extraction logic.
- Prefer bulletins that explicitly report province-wide electricity consumption totals (`全社会用电量`) or monthly power operation summaries.
- Do not claim coverage until specific monthly bulletins have been collected and logged.
- Do not spend time assigning ex ante confidence scores to province coverage; attempt the EDWC provinces one by one and record what is actually available.
- For Gansu, the current practical script stack is: Python -> Chrome DevTools Protocol -> rendered page HTML -> Beautiful Soup parser.
- Selenium and plain headless Chrome both failed on the live site, while a persistent real Chrome session worked for both discovery and article extraction.
- The current Gansu discovery scrape found `72` bulletin pages covering `2020-03` through `2026-02`.
- The current rebuilt Gansu panel has `72` months with monthly total electricity consumption populated.
- `71` months come from the original Gansu article text and `1` month (`2022-06`) comes from a mirrored Tianshui government repost because the saved original Gansu HTML has an empty article body block.
- The current rich-panel and source-validation summary live at `03_data/interim/gansu_scrape/gansu_panel_rich.csv`, `03_data/interim/gansu_scrape/gansu_panel_rich_coverage.csv`, and `03_data/interim/gansu_scrape/gansu_validation_report.md`.

## Related Notes

- [[global_plan]]
- [[thesis_structure]]
- [[EDWC_Gansu_EventStudy]]
