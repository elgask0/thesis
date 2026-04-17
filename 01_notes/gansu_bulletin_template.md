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
  the article body block is empty in the saved HTML
- Alternate government repost used for validation and extraction:
  `https://www.tianshui.gov.cn/gxj/info/1682/33692.htm`

This month should be treated as a source-level exception, not as evidence that the extraction logic is broadly unstable.
