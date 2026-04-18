# MinerU Note Upgrade Report

## 1. Corpus summary
- Total canonical papers: 51
- PDFs found: 51
- Notes found: 51
- Notes with stub sections before upgrade: 51
- Notes upgraded: 51

## 2. MinerU setup
- MinerU was not available at the start of the workflow; it was installed into the repo-local `.venv-mineru` environment.
- Environment used: Python 3.12.9 in `/Users/elgask0/REPOS/thesis/.venv-mineru` on macOS Apple Silicon.
- Commands used: `python3 -m venv .venv-mineru`, `.venv-mineru/bin/pip install -U uv`, `.venv-mineru/bin/uv pip install --python .venv-mineru/bin/python -U "mineru[all]"`.
- Parsed output location: `/Users/elgask0/REPOS/thesis/02_literature/parsed`

## 3. Parse results

| paper / citation key | PDF found? | parsed successfully? | fallback to direct PDF needed? | notes |
|---|---|---|---|---|
| `masanet_2020_recalibrating_dc_energy` | yes | full | no | Existing parsed Markdown reused. |
| `shehabi_2024_us_dc_energy_report` | yes | partial | yes | MinerU output was usable for structure, but the executive-summary numbers and quotes were checked against the PDF. |
| `iea_2025_energy_and_ai` | yes | partial | yes | MinerU output was usable for structure, but the global projection and China data-gap claims were checked against the PDF. |
| `patterson_2021_carbon_nn_training` | yes | full | no | Existing parsed Markdown reused. |
| `patterson_2022_ml_carbon_plateau` | yes | full | no | Existing parsed Markdown reused. |
| `dodge_2022_carbon_intensity_ai_cloud` | yes | full | no | Existing parsed Markdown reused. |
| `luccioni_2023_bloom_carbon_footprint` | yes | full | no | Existing parsed Markdown reused. |
| `zheng_2020_load_migration_curtailment` | yes | full | no | Existing parsed Markdown reused. |
| `ni_2024_china_dc_emissions_pathways` | yes | full | no | Existing parsed Markdown reused. |
| `greenpeace_2021_china_5g_dc_outlook` | yes | full | no | Existing parsed Markdown reused. |
| `zhang_duan_2025_edwc_net_zero` | yes | full | no | Existing parsed Markdown reused. |
| `zhang_li_wang_2025_edwc_bits_migration` | yes | full | no | Existing parsed Markdown reused. |
| `xie_2024_ewcrt_co2_reduction` | yes | full | no | Existing parsed Markdown reused. |
| `liu_2020_carbon_monitor_dataset` | yes | full | no | Existing parsed Markdown reused. |
| `kline_moretti_2014_tva_big_push` | yes | partial | no | Existing parsed Markdown reused. |
| `greenstone_2010_plant_openings_spillovers` | yes | partial | yes | Abstract and core findings were checked against the PDF to remove JSTOR boilerplate noise. |
| `busso_2013_place_based_policy` | yes | partial | no | Existing parsed Markdown reused. |
| `lu_wang_zhu_2019_china_economic_zones` | yes | full | no | Existing parsed Markdown reused. |
| `wang_2023_uhv_emissions_staggered_did` | yes | full | no | Existing parsed Markdown reused. |
| `deryugina_2020_electricity_demand_dynamics` | yes | full | no | Existing parsed Markdown reused. |
| `sun_abraham_2021_event_study_het` | yes | full | no | Existing parsed Markdown reused. |
| `callaway_santanna_2021_did_multiple_periods` | yes | full | no | Existing parsed Markdown reused. |
| `goodman_bacon_2021_did_timing` | yes | full | no | Existing parsed Markdown reused. |
| `dechaisemartin_dhaultfoeuille_2020_twfe` | yes | full | no | Existing parsed Markdown reused. |
| `borusyak_2024_event_study_imputation` | yes | full | no | Existing parsed Markdown reused. |
| `abadie_2010_scm_tobacco` | yes | full | no | Existing parsed Markdown reused. |
| `abadie_2015_scm_comparative_politics` | yes | full | no | Existing parsed Markdown reused. |
| `gupta_2022_chasing_carbon` | yes | full | no | Existing parsed Markdown reused. |
| `radovanovic_2023_carbon_aware_computing` | yes | full | no | Existing parsed Markdown reused. |
| `gsf_2024_sci_specification` | yes | parse_poor | yes | Parsed Markdown exists but stayed too thin for note use. |
| `freitag_2021_ict_climate_critique` | yes | full | no | Existing parsed Markdown reused. |
| `green_grid_2012_pue_wp49` | yes | partial | yes | Metric definition and reporting logic were checked against the PDF; MinerU output was incomplete and the note file itself needed cleanup. |
| `yuventi_2013_pue_critique` | yes | full | no | Existing parsed Markdown reused. |
| `eehpc_2015_green500_methodology` | yes | full | no | Existing parsed Markdown reused. |
| `dongarra_luszczek_2026_hpl_mxp` | yes | full | no | Existing parsed Markdown reused. |
| `tschand_2025_mlperf_power` | yes | full | no | Existing parsed Markdown reused. |
| `fernandez_2025_hardware_scaling_llm` | yes | full | no | Existing parsed Markdown reused. |
| `shan_2016_china_provincial_emissions` | yes | full | no | Existing parsed Markdown reused. |
| `caict_2023_computing_power_index` | yes | partial | yes | Front-matter statistics and provincial-index framing were checked against the PDF. |
| `caict_2024_green_computing_report` | yes | partial | yes | Front-matter statistics and the ECCI framework were checked against the PDF. |
| `rmi_2024_china_data_center_low_carbon` | yes | full | yes | Existing parsed Markdown reused. |
| `liao_2019_power_sector_co2_clustering` | yes | full | no | Existing parsed Markdown reused. |
| `liu_2018_curtailment_northwest_china` | yes | full | no | Existing parsed Markdown reused. |
| `song_2019_market_segmentation_wind_curtailment` | yes | full | no | Existing parsed Markdown reused. |
| `zhang_2021_decline_wind_solar_curtailment` | yes | full | no | Existing parsed Markdown reused. |
| `qu_2017_embodied_co2_electricity_transmission` | yes | full | no | Existing parsed Markdown reused. |
| `deng_2022_interregional_transmission_variable_power` | yes | full | no | Existing parsed Markdown reused. |
| `guo_2020_power_market_reform_china` | yes | full | no | Existing parsed Markdown reused. |
| `xiang_2023_market_vs_regulatory_capture` | yes | full | no | Existing parsed Markdown reused. |
| `ndrc_2023_edwc_integrated_computing_network` | yes | full | yes | MinerU text existed, but policy targets and quotes were taken from direct PDF text because the parsed output was noisy. |
| `ndrc_miit_nea_nda_2024_green_datacenter_action_plan` | yes | full | no | Existing parsed Markdown reused. |

## 4. Note upgrades performed

| citation key | note filename | sections upgraded | whether parsed Markdown was sufficient | whether PDF fallback was used |
|---|---|---|---|---|
| `masanet_2020_recalibrating_dc_energy` | `masanet_2020_recalibrating_dc_energy.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `shehabi_2024_us_dc_energy_report` | `shehabi_2024_us_dc_energy_report.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `iea_2025_energy_and_ai` | `iea_2025_energy_and_ai.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `patterson_2021_carbon_nn_training` | `patterson_2021_carbon_nn_training.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `patterson_2022_ml_carbon_plateau` | `patterson_2022_ml_carbon_plateau.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `dodge_2022_carbon_intensity_ai_cloud` | `dodge_2022_carbon_intensity_ai_cloud.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `luccioni_2023_bloom_carbon_footprint` | `luccioni_2023_bloom_carbon_footprint.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `zheng_2020_load_migration_curtailment` | `zheng_2020_load_migration_curtailment.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `ni_2024_china_dc_emissions_pathways` | `ni_2024_china_dc_emissions_pathways.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `greenpeace_2021_china_5g_dc_outlook` | `greenpeace_2021_china_5g_dc_outlook.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `zhang_duan_2025_edwc_net_zero` | `zhang_duan_2025_edwc_net_zero.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `zhang_li_wang_2025_edwc_bits_migration` | `zhang_li_wang_2025_edwc_bits_migration.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `xie_2024_ewcrt_co2_reduction` | `xie_2024_ewcrt_co2_reduction.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `liu_2020_carbon_monitor_dataset` | `liu_2020_carbon_monitor_dataset.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `kline_moretti_2014_tva_big_push` | `kline_moretti_2014_tva_big_push.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `greenstone_2010_plant_openings_spillovers` | `greenstone_2010_plant_openings_spillovers.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `busso_2013_place_based_policy` | `busso_2013_place_based_policy.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `lu_wang_zhu_2019_china_economic_zones` | `lu_wang_zhu_2019_china_economic_zones.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `wang_2023_uhv_emissions_staggered_did` | `wang_2023_uhv_emissions_staggered_did.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `deryugina_2020_electricity_demand_dynamics` | `deryugina_2020_electricity_demand_dynamics.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `sun_abraham_2021_event_study_het` | `sun_abraham_2021_event_study_het.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `callaway_santanna_2021_did_multiple_periods` | `callaway_santanna_2021_did_multiple_periods.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `goodman_bacon_2021_did_timing` | `goodman_bacon_2021_did_timing.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `dechaisemartin_dhaultfoeuille_2020_twfe` | `dechaisemartin_dhaultfoeuille_2020_twfe.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `borusyak_2024_event_study_imputation` | `borusyak_2024_event_study_imputation.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `abadie_2010_scm_tobacco` | `abadie_2010_scm_tobacco.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `abadie_2015_scm_comparative_politics` | `abadie_2015_scm_comparative_politics.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `gupta_2022_chasing_carbon` | `gupta_2022_chasing_carbon.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `radovanovic_2023_carbon_aware_computing` | `radovanovic_2023_carbon_aware_computing.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `gsf_2024_sci_specification` | `gsf_2024_sci_specification.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `freitag_2021_ict_climate_critique` | `freitag_2021_ict_climate_critique.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `green_grid_2012_pue_wp49` | `green_grid_2012_pue_wp49.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `yuventi_2013_pue_critique` | `yuventi_2013_pue_critique.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `eehpc_2015_green500_methodology` | `eehpc_2015_green500_methodology.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `dongarra_luszczek_2026_hpl_mxp` | `dongarra_luszczek_2026_hpl_mxp.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `tschand_2025_mlperf_power` | `tschand_2025_mlperf_power.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `fernandez_2025_hardware_scaling_llm` | `fernandez_2025_hardware_scaling_llm.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `shan_2016_china_provincial_emissions` | `shan_2016_china_provincial_emissions.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `caict_2023_computing_power_index` | `caict_2023_computing_power_index.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `caict_2024_green_computing_report` | `caict_2024_green_computing_report.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `rmi_2024_china_data_center_low_carbon` | `rmi_2024_china_data_center_low_carbon.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `liao_2019_power_sector_co2_clustering` | `liao_2019_power_sector_co2_clustering.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `liu_2018_curtailment_northwest_china` | `liu_2018_curtailment_northwest_china.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `song_2019_market_segmentation_wind_curtailment` | `song_2019_market_segmentation_wind_curtailment.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `zhang_2021_decline_wind_solar_curtailment` | `zhang_2021_decline_wind_solar_curtailment.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `qu_2017_embodied_co2_electricity_transmission` | `qu_2017_embodied_co2_electricity_transmission.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `deng_2022_interregional_transmission_variable_power` | `deng_2022_interregional_transmission_variable_power.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `guo_2020_power_market_reform_china` | `guo_2020_power_market_reform_china.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `xiang_2023_market_vs_regulatory_capture` | `xiang_2023_market_vs_regulatory_capture.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |
| `ndrc_2023_edwc_integrated_computing_network` | `ndrc_2023_edwc_integrated_computing_network.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | no | yes |
| `ndrc_miit_nea_nda_2024_green_datacenter_action_plan` | `ndrc_miit_nea_nda_2024_green_datacenter_action_plan.md` | Core argument / findings, Method & data, Key quotes, Relevance to EDWC thesis, Caveats / limitations, Related papers in corpus | yes | no |

## 5. Notes still needing manual review
- `gsf_2024_sci_specification`: the note is usable, but the local PDF extraction is malformed and page numbers are not reliably recoverable, so any future direct quotation should be checked against the source PDF or website.
- `rmi_2024_china_data_center_low_carbon`: the note is usable but still noisier than the rest of the corpus because it leans on mixed extracted text and PDF fallback; if this source becomes central in drafting, its summary and quote selection should be tightened manually.

## 6. Missing inputs
- Missing PDFs: none.
- Missing notes: none.
- Parse failures: `gsf_2024_sci_specification`

## 7. Final readiness
- Literature review drafting: yes
- Background drafting: yes
- Empirical strategy drafting: yes
- CPC / measurement drafting: mostly
