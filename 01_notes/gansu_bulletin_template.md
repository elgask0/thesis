# Gansu Bulletin Template

Working note for the structure of the Gansu monthly electricity bulletins after the first full scrape and structured extraction pass.

## Coverage

- Current public scrape coverage: `2020-03` to `2026-02`
- Discovered bulletin count: `72`
- Core monthly total electricity consumption is available for all `72` months in the current validated panel
- `2022-06` uses an alternate government repost from Tianshui because the original Gansu article page renders with an empty body in saved HTML

## Current Structured Outputs

- Simple validated panel:
  `03_data/interim/gansu_scrape/gansu_monthly_kwh.csv`
- Wide structured panel:
  `03_data/interim/gansu_scrape/gansu_panel_rich.csv`
- Field coverage summary:
  `03_data/interim/gansu_scrape/gansu_panel_rich_coverage.csv`
- Validation report:
  `03_data/interim/gansu_scrape/gansu_validation_report.md`

## Data Validation Snapshot

- The canonical monthly panel is internally complete from `2020-03` through `2026-02` with no missing months and no duplicate `year_month` rows.
- Title month labels match the panel month labels for all `72` rows.
- From `2020-04` onward, monthly total electricity consumption matches the month-to-month YTD difference exactly within the saved panel.
- Monthly sector sums match the reported monthly total in every month where all four sector values are present.
- The `2022-06` month is now validated from a mirrored government repost rather than a derived neighbor-YTD fill.
- Some `articles/` JSON files still appear twice, once with a short slug and once with a long `https-...` slug. These are legacy filename aliases, not distinct sources.

## Source-Level Omissions In The Rich Panel

- `2023-01` omits the residential monthly detail in the saved source text, so `residential_monthly_kwh_100m` is blank for that month.
- `2023-03` reports total generation in the intro and installed capacity in the power-system section, but omits the usual source-by-source generation breakdown and therefore leaves the source-specific generation components blank.
- January bulletins generally do not restate cumulative sector and generation subcomponents explicitly, so January YTD coverage is thinner for those auxiliary fields than for the headline total series.

## Generation Residual Note

- From `2024-06` onward, `19` bulletins report total generation values that are slightly larger than the sum of the explicitly listed source subtotals.
- Treat these as source-level publication residuals for now rather than parser failures; they likely reflect unreported residual categories or source rounding conventions.

## Template Regimes

### 2020 to early 2023

These bulletins are longer and usually include:

- monthly and cumulative total electricity consumption
- monthly and cumulative external send-out electricity
- monthly and cumulative external purchased electricity
- monthly and cumulative sector split
- cumulative industry split
- monthly and cumulative industrial subsector detail
- installed capacity, generation, and average utilization hours

The wording is usually `当月 / 累计` and the section numbering often uses `1、2、3、`.

### Mid 2023 onward

These bulletins become more standardized and usually open with:

- monthly total generation
- cumulative generation
- monthly total electricity consumption
- cumulative electricity consumption

The wording shifts toward `X月 / 1-X月` and section numbering often uses `1. 2. 3.`.

External send-out and external purchased electricity mostly disappear after early 2023.

### 2024 onward

The modern template is highly standardized, but not literally identical line by line.

It usually includes:

- monthly and cumulative total electricity consumption
- monthly and cumulative sector split
- cumulative industry split
- installed capacity by source
- monthly and cumulative generation by source
- average utilization hours by source in many months

## Field Families Present In The Wide Panel

### Core outcome

- monthly total electricity consumption
- cumulative total electricity consumption

### Electricity composition

- primary sector electricity use
- secondary sector electricity use
- tertiary sector electricity use
- residential electricity use

### Industry detail

- agriculture
- irrigation
- industry total
- construction
- transport / warehousing / postal
- information transmission / software / IT services
- wholesale / retail
- accommodation / catering
- finance
- real estate
- leasing / business services
- public services / public administration

### Industrial subsectors

- nonferrous metals
- aluminum smelting
- ferrous metals
- ferroalloys
- steel
- chemicals
- calcium carbide
- non-metal mineral products
- cement
- petroleum / coal processing

### Power system variables

- total installed capacity
- installed capacity by source
- total generation
- generation by source
- average utilization hours
- utilization hours by source

### Early-period system flows

- external send-out electricity
- external purchased electricity

## Known Source Exception

### 2022-06

- Canonical Gansu article URL:
  `https://gxt.gansu.gov.cn/gxt/c107572/202207/2081569.shtml`
- Saved Gansu page issue:
  the article body block is empty in the saved HTML (`<div class="nr-003"> ... <!--Content Start--> <!--Content End--> ... </div>`)
- Alternate government repost used for validation and extraction:
  `https://www.tianshui.gov.cn/gxj/info/1682/33692.htm`
- Canonical panel method label:
  `mirror_article_text`

This month should be treated as a source-level exception, not as evidence that the extraction logic is broadly unstable.
