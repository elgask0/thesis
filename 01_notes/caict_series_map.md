# CAICT Series Map

Working note mapping the CAICT series that could be useful for the EDWC thesis.

## Purpose

- Track which CAICT series are actually available.
- Separate province/city benchmarking series from national-only macro context.
- Clarify which series are suitable for cross-sectional rankings versus short time comparisons.

## Series Map (2018-2025 materials)

| Series ID | Theme | Frequency | Reference years | Geographic scope | Granularity | What it measures |
|---|---|---|---|---|---|---|
| `caict_compower_index_wp_2023` | Compute development index (`算力发展指数`) | Annual | 2022 | China | Province, city | Composite index covering basic compute, AI compute, supercomputing, infrastructure, ecosystem, connectivity, IT spending, open data, mobile traffic, and industrial digitalization; methodology described as AHP + FP32 normalization, version 2.0. |
| `caict_comprehensive_calc_eval_wp_2023` | Comprehensive compute evaluation (`综合算力`) | One-off first edition | 2022 | China | Province, city | Four dimensions: compute, storage, transport/network, and environment. |
| `caict_comprehensive_calc_eval_rep_2024` | Comprehensive compute evaluation (`综合算力`) | Annual | 2023 | China | Province, city | Same 4D framework in a 3.0 version with 53 indicators: total and smart compute (FP32), storage (EB), network quality, and environment (PUE / green energy). |
| `caict_industrial_internet_eval_rep_2024` | Industrial Internet | Annual | 2023 | China (31 provinces) | Province | Provincial indices for basic capability, innovation, industrial development, adoption, and enabling environment. |
| `caict_5g_impact_wp_2023` | 5G socioeconomic impact | Annual | 2023 | China | National | 5G base stations, 5G users, industrial use cases, and macroeconomic impact. |
| `caict_cloud_wp_2024` | Cloud | Annual | 2023 | Global / China | National | Global cloud market size, China cloud market size, and a cloud-development evaluation framework. |
| `caict_data_center_wp_2022` | Data centers | One-off | 2021 | Global / China | National | Rack stock and market revenue. |
| `caict_global_digecon_wp_2023` | Global digital economy | Annual | 2022 | Global (51 countries) | Country | Digital-economy value added and cross-country comparisons. |

## Quick Picks

- Best for province/city benchmarking:
  - `caict_compower_index_wp_2023`
  - `caict_comprehensive_calc_eval_wp_2023`
  - `caict_comprehensive_calc_eval_rep_2024`
- Best for a short comparable series:
  - Focus on the 4D `综合算力` framework from 2022 to 2023.
- Best for national macro context only:
  - `caict_5g_impact_wp_2023`
  - `caict_cloud_wp_2024`
  - `caict_data_center_wp_2022`
  - `caict_global_digecon_wp_2023`

## Measurement Families and Units

### Compute / Comprehensive Compute

- `算力`: total, basic, smart, and supercomputing capacity, typically in `EFlops` with `FP32` references.
- `存力`: storage capacity in `EB`.
- `运力`: network quality / capacity indicators, including backbone and dual-100G style metrics.
- `环境`: PUE, green energy share, and related conditions.

### Ecosystem Indicators (mainly in the 2023 development index)

- Equipment production
- Integrated-circuit production
- Software / IT revenues
- R&D spending
- Patent counts
- 5G coverage
- Open-data indicators
- Mobile traffic
- Industrial digitalization

## Thesis Use

### Main use in this thesis

- Define province tiers for heterogeneity.
- Select donor pools for SCM among provinces with similar compute environments.
- Add program-fit context for the exploratory economic extension.

### Recommended series choices

- For donor selection and heterogeneity:
  - Start from `caict_comprehensive_calc_eval_rep_2024` for the 2023 cross section.
- For 2022 to 2023 comparisons:
  - Use the two `综合算力` editions rather than mixing the broader development-index framework directly over time.
- For broader context on the digital economy:
  - Use the national-only 5G, cloud, and data-center reports as background, not as merge-ready province panel inputs.
- For exploratory economic extension:
  - Consider `caict_industrial_internet_eval_rep_2024` as a province-level companion series.

## Caveats

- Do not assume levels are directly comparable across different CAICT frameworks without checking methodology changes.
- The broad 2023 `算力发展指数` is rich cross-sectionally but not the cleanest basis for year-to-year changes.
- National-only series cannot be merged directly into a province-year panel except as common national context.
- Some reports rank both provinces and cities; city results should not be mixed into province analysis without an explicit rule.

## Related Notes

- [[global_plan]]
- [[thesis_structure]]
- [[EDWC_Gansu_EventStudy]]
