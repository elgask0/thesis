# Time-of-Use Tariff Reforms and Intraday Incentives

Working note on provincial time-of-use electricity tariff reforms that could matter for intraday electricity-shifting incentives.

## Status

- Not part of the current core identification strategy.
- Keep as institutional background and as a future mechanism note.
- Cannot be used to prove intraday reshaping of electricity demand without hourly electricity-use data.

> [!warning]
> This note stores a user-supplied regulatory summary. Before citing any item in the final paper, archive the official PDF or official government text for each norm.

## Why Keep This

- These reforms show that provincial regulation can change the incentive to shift electricity usage across the day.
- They are useful for mechanism discussion if EDWC or data-center operators respond to peak, valley, critical-peak, or deep-valley price signals.
- They are not enough on their own to show that daily electricity usage actually moved across hours.

## Summary Table

| Province | Regulation ID | Publication -> Effective date | What changes |
|---|---|---|---|
| Jiangsu | `苏发改价格发〔2023〕555号` | `2023-05-24 -> 2023-07-01` | Introduces seasonal `尖峰` periods for users `>=315 kVA` and a holiday `深谷` window at `11:00–15:00`, with `尖峰` priced at `峰 +20%`. |
| Gansu | `甘发改价格〔2024〕424号` | `2024-07-05 -> 2024-08-01` | Reallocates hours so `谷 = 10:00–16:00`, requires `峰谷价差 >= 3:1`, and clarifies that spot-market prices are not constrained by these TOU blocks. |
| Henan | `豫发改价管〔2022〕867号` plus 2024 adjustment | `2022-11 -> 2024 adjustment, reportedly effective 2024-06-01` | 2022 rule sets explicit `峰平谷` ratios and restores `尖峰`; 2024 adjustment proposes unified ratios and longer evening critical-peak windows, with more midday accommodation for solar. |
| Hubei | `省发改委关于完善工商业分时电价机制有关事项的通知` | `2024-03-27 -> 2024-05-01` | Keeps `>=100 kVA` scope but redesigns the full `尖峰 / 峰 / 平 / 谷` schedule with explicit four-block ratios and seasonal critical-peak intensification. |

## Province Notes

### Jiangsu

- Regulation: `《省发展改革委关于进一步完善分时电价政策的通知》苏发改价格发〔2023〕555号`
- Publication date: `2023-05-24`
- Effective date: `2023-07-01`
- Scope:
  - mainly industrial users `>=315 kVA`
  - others remain under the broader national transmission-and-distribution regime
- Pre:
  - TOU already existed
  - no explicit holiday midday `深谷`
  - less explicit seasonal `尖峰` design
- Post:
  - summer `尖峰`: `7–8月`, `14:00–15:00` and `20:00–21:00`
  - winter `尖峰`: `12–1月`, `9:00–11:00` and `18:00–20:00`
  - `尖峰` price = `峰 x (1 + 20%)`
  - holiday `深谷` during `春节 / 五一 / 国庆`: `11:00–15:00`
  - holiday `深谷` price is `20%` below the `平`-segment benchmark
- Usefulness:
  - strong regulatory incentive shock
  - useful for mechanism discussion even without intraday load data

### Gansu

- Regulation: `《关于优化调整工商业等用户峰谷分时电价政策有关事项的通知》甘发改价格〔2024〕424号`
- Publication date: `2024-07-05`
- Effective date: `2024-08-01`
- Scope:
  - commercial and industrial users
  - agricultural users except irrigation
  - excludes electric railway traction
- Pre:
  - earlier TOU already existed
  - 2023 transmission-and-distribution reform reorganized user categories
- Post:
  - `峰 = 6:00–8:00, 18:00–23:00`
  - `谷 = 10:00–16:00`
  - remaining hours are `平`
  - minimum `峰谷` ratio `>= 3:1`
  - spot-market prices (`现货`) are not governed by these TOU blocks or ratios
  - medium- and long-term contracts should still respect the minimum ratio
- Usefulness:
  - especially relevant because the valley period moves to midday
  - useful if a later design interacts TOU incentives with spot-market exposure

### Henan

- Base regulation: `《关于进一步完善分时电价机制有关事项的通知》豫发改价管〔2022〕867号`
- Base implementation: `2022-11`
- 2024 adjustment:
  - user summary indicates formal drafting / consultation and later implementation from `2024-06-01`
- 2022 structure:
  - `峰 = 10:00–14:00` and `17:00–21:00`
  - `谷 = 23:00–7:00`
  - `平` for the remaining hours
  - baseline ratio `峰:平:谷 = 1.64:1:0.41`
  - seasonal ratio in `1月, 7–8月, 12月 = 1.71:1:0.47`
  - `尖峰` mechanism restored in `1月, 7–8月, 12月`
- 2024 adjustment:
  - reorganizes blocks by month
  - extends evening high-price periods
  - shifts some midday hours toward `平/谷` to absorb solar generation
  - proposed unified ratio `1.72:1:0.45`
  - `尖峰 = 高峰 x 1.2`
- Usefulness:
  - likely the cleanest pre/post contrast among the four provinces
  - explicit 2022 versus 2024 tariff redesign is useful institutional background for any future mechanism section

### Hubei

- Regulation: `《省发改委关于完善工商业分时电价机制有关事项的通知》`
- Publication date: `2024-03-27`
- Effective date: `2024-05-01`
- Scope:
  - keeps `>=100 kVA` commercial and industrial users within TOU execution
  - excludes electric railway traction, commercial users, government agencies, schools, hospitals, and urban lighting
  - electric storage users such as electric boilers and ice/water storage cooling remain within TOU execution
- 2024 schedule:
  - `尖峰`: `7–8月 20:00–22:00`; other months `18:00–20:00`
  - `峰`: `7–8月 16:00–20:00, 22:00–24:00`; other months `16:00–18:00, 20:00–24:00`
  - `平`: `6:00–12:00, 14:00–16:00`
  - `谷`: `0:00–6:00, 12:00–14:00`
- Ratios:
  - normal months: `尖峰:峰:平:谷 = 1.8 : 1.49 : 1 : 0.48`
  - `7–8月 / 12–1月`: `尖峰 = 2`, `谷 = 0.45`
- Pre:
  - TOU existed for `>=100 kVA`
  - the 2024 reform is the first major redesign in many years
- Usefulness:
  - gives the most complete four-block schedule among the cases
  - useful for a short 2024 mechanism appendix if intraday data ever become available

## Notes for Paper Use

### Suggested coding fields

- `effective_date`
- `province`
- `regulation_id`
- `has_critical_peak`
- `has_deep_valley`
- `peak_to_flat_ratio`
- `valley_to_flat_ratio`
- `hour_mapping_note`
- `market_exemption_note`

### Suggested effective dates

- Jiangsu: `2023-07-01`
- Gansu: `2024-08-01`
- Henan: `2022-11-01` for the base rule, plus `2024-06-01` for the later adjustment
- Hubei: `2024-05-01`

### What is most useful here

- Henan:
  - strongest pre/post contrast in explicit hours and ratios
- Hubei:
  - clean four-block schedule with stable scope
- Gansu:
  - midday valley block plus explicit `>= 3:1` ratio and spot-market carve-out
- Jiangsu:
  - critical-peak and holiday deep-valley incentive shock

## Main Limitation

These regulations can support a mechanism story about **incentives** to shift electricity use within the day, but without hourly electricity consumption, spot-market participation data, or dispatch/load traces, they cannot demonstrate that actual intraday demand shifted.

## Related Notes

- [[global_plan]]
- [[renewable_curtailment_extension]]
- [[electricity_data_pipeline]]
