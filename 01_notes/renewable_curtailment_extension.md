# Renewable Utilization / Curtailment Extension

Working note for a possible descriptive extension on renewable integration conditions around EDWC go-live.

## Status

- Not a restored core research question.
- Use only as a descriptive appendix or mechanism note unless a better identification strategy appears.

## Why Keep This

- Monthly renewable utilization rates can help describe whether EDWC provinces were operating in tighter or looser renewable-integration conditions.
- These tables can support a non-causal appendix on renewable absorption conditions.
- They do **not** solve the main problem that caused the original curtailment-welfare idea to be dropped: no intraday load, price, or dispatch data.

## Source Example

- Title: `2024年4月全国新能源并网消纳情况统计表` / `National New Energy Grid Integration and Consumption Statistics for April 2024`
- Publication date: `2024-06-04`
- Repost URL: [International Energy Network](https://mnewenergy.in-en.com/html/newenergy-2434843.shtml?utm_source=chatgpt.com)
- Official origin cited in the repost: `全国新能源消纳监测预警中心` / National New Energy Consumption Monitoring and Early Warning Center

## Variables Available

- Wind power utilization rate
- Photovoltaic utilization rate
- Current month value
- Year-to-date cumulative value

Useful transformation:

$$
\text{utilization shortfall}_{p,t} = 1 - \text{utilization rate}_{p,t}
$$

This is a descriptive proxy for renewable integration stress, not a direct measure of curtailed MWh.

## April 2024 Example Values

| Region | Wind Apr | Wind Jan-Apr | Solar Apr | Solar Jan-Apr | Notes |
|---|---:|---:|---:|---:|---|
| Gansu | 94.10% | 92.20% | 88.70% | 91.10% | Lower solar utilization than the other core treated provinces in this snapshot. |
| Ningxia | 99.00% | 98.00% | 97.30% | 96.40% | High utilization in both wind and solar. |
| Guizhou | 99.40% | 99.30% | 98.80% | 95.80% | High utilization; useful comparison with Gansu. |
| Western Inner Mongolia | 93.60% | 94.00% | 93.00% | 92.60% | Reported as grid-region rather than province. |
| Eastern Inner Mongolia | 91.90% | 92.80% | 96.60% | 97.40% | Also grid-region rather than province. |
| Qinghai | 92.30% | 92.70% | 92.20% | 91.50% | Potential donor / comparison region. |
| Xinjiang | 93.10% | 94.70% | 93.60% | 95.30% | Another western comparison case. |

## How This Could Be Used

- Descriptive appendix: plot monthly wind and solar utilization around `T0` for treated provinces where coverage is available.
- Mechanism context: compare provinces where EDWC increases electricity load but renewable absorption conditions differ.
- Robustness narrative: discuss whether cleaner-compute interpretations are more plausible in provinces with stronger renewable utilization.

## Limitations

- Utilization rates are not curtailed energy volumes.
- The link provided is a repost; the preferred long-run workflow is to locate the official monitoring-center publication or archive.
- Inner Mongolia is split into `蒙西` and `蒙东`, so province-level matching requires a documented aggregation choice.
- Monthly utilization rates still do not identify whether flexible data-center load reduced curtailment.
- No welfare calculation should be built from this alone.

## Related Notes

- [[global_plan]]
- [[EDWC_Gansu_EventStudy]]
- [[thesis_structure]]
- [[electricity_data_pipeline]]
