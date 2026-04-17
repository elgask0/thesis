# EDWC Thesis Proposal — Literature Review Master File

## Purpose

This is the single operational reference for the proposal's entire literature architecture. It contains every paper in the final corpus, organized by function, with enough detail to write the literature review, background, and empirical-strategy sections using only this file plus the individual papers.

---

## Literature Architecture

Four literature streams, each tied to a specific part of the proposal's logical chain.

| Stream | Short name | Analytical function | Proposal sections served |
|---|---|---|---|
| **Outcome** | DC energy demand, EDWC gap | Why electricity demand from compute infrastructure matters; what EDWC studies already do; where the outcome-side gap is | §1.1.1, §1.1.2, §2.1, §2.4, §3.3 |
| **Design** | Causal identification | Precedent for DiD/event-study on infrastructure shocks; modern staggered-DiD methodology; SCM; electricity-demand dynamics | §2.2, §2.4, §3.4, §3.4.4 |
| **Measurement** | CPC framework | CPC components (CI, PUE, GF/W, accounting logic); standards; China institutional context for green compute | §2.3, §2.4, §3.2, §3.4.3, §4 |
| **China context** | Provincial energy system | Grid mix, renewable curtailment, transmission, dispatch frictions, provincial carbon variation, EDWC policy documents | §1.1.3, §1.1.4, §3.5, interpretation in §3 |

---

## Stream 1 — Outcome: DC Energy Demand and EDWC Gap

### 1.1 Global data center energy demand

**Masanet, E., Shehabi, A., Lei, N., Smith, S. J., & Koomey, J. (2020).** Recalibrating global data center energy-use estimates. *Science, 367*(6481), 984–986. https://doi.org/10.1126/science.aba3758

- Foundational bottom-up estimate: global DC electricity ~205 TWh in 2018, ~1% of world electricity. Showed only ~6% growth 2010–2018 despite ~550% growth in compute instances — historical "efficiency decoupling." This anchors the proposal's baseline claim that compute-infrastructure electricity is material but historically offset by efficiency, so EDWC's geographic relocation can matter even without global volume growth.
- **Use in proposal:** §1.1.1 opening DC-electricity claim; §2.1 baseline reference.
- **Tags:** `DC-energy`; `global-estimates`; `efficiency-decoupling`; `outcome`
- **Filename:** `masanet_2020_recalibrating_dc_energy.md`

**Shehabi, A., Smith, S. J., Hubbard, A., Newkirk, A., Lei, N., Siddik, M. A. B., Holecek, B., Koomey, J., Masanet, E., & Sartor, D. (2024).** *2024 United States Data Center Energy Usage Report* (LBNL-2001637). Lawrence Berkeley National Laboratory. https://doi.org/10.71468/P1WC7Q

- Authoritative bottom-up update for the AI era. US DC electricity reached 176 TWh in 2023 (4.4% of US electricity), with wide 2028 projections (~325–580 TWh). Links recent acceleration to AI-accelerated servers. Provides concrete benchmark for how fast DC electricity can scale when AI hardware diffuses — strengthening plausibility that EDWC could measurably shift provincial electricity demand over a short horizon.
- **Use in proposal:** §1.1.1 AI-era benchmark; §2.1 scaling evidence.
- **Tags:** `DC-energy`; `bottom-up`; `AI-servers`; `LBNL`; `outcome`
- **Filename:** `shehabi_2024_us_dc_energy_report.md`

**International Energy Agency. (2025).** *Energy and AI*. IEA, Paris. https://www.iea.org/reports/energy-and-ai

- Global synthesis projecting DC electricity to ~945 TWh by 2030 (~1.5% → ~3% of world electricity), with AI as primary driver. China and US account for ~80% of growth. Explicitly notes major data gaps for China. This is the highest-level policy anchor for framing compute infrastructure as a fast-growing electricity load and for arguing that provincial causal study of EDWC is policy-relevant.
- **Use in proposal:** §1.1.1 global framing; §1.1.2 policy framing; §2.1 policy-relevance.
- **Tags:** `IEA`; `AI-energy`; `DC-projections`; `policy-report`; `outcome`
- **Filename:** `iea_2025_energy_and_ai.md`

### 1.2 AI-specific carbon accounting

**Patterson, D., Gonzalez, J., Le, Q. V., Liang, C., Munguia, L. M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2021).** Carbon emissions and large neural network training. arXiv:2104.10350. https://doi.org/10.48550/arXiv.2104.10350

- Quantifies energy and CO₂ for training frontier models (T5, GPT-3, etc.) and shows footprint changes substantially with hardware, DC efficiency, and grid-carbon assumptions. Supports the CPC logic that "compute → electricity → emissions" is not a constant mapping — EDWC-induced relocation changes emissions conditional on provincial grid and facility characteristics.
- **Use in proposal:** §1.1.1 background; §2.1 outcome motivation.
- **Tags:** `AI-carbon`; `training`; `CPC-logic`; `outcome`
- **Filename:** `patterson_2021_carbon_nn_training.md`

**Patterson, D., Gonzalez, J., Hölzle, U., Le, Q., Liang, C., Munguia, L.-M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2022).** The carbon footprint of machine learning training will plateau, then shrink. *Computer, 55*(7), 18–28. https://doi.org/10.1109/MC.2022.3148714

- Mitigation-focused complement to Patterson 2021. Highlights that data-center location ("map") is a key mitigation lever and that inference can dominate energy use in production ML at scale. Strengthens the rationale for electricity as primary outcome and for CPC as translation.
- **Use in proposal:** §1.1.1 background; §2.1 outcome motivation.
- **Tags:** `AI-carbon`; `inference`; `location-effects`; `outcome`
- **Filename:** `patterson_2022_ml_carbon_plateau.md`

**Dodge, J., Prewitt, T., Tachet des Combes, R., et al. (2022).** Measuring the carbon intensity of AI in cloud instances. *FAccT '22*, 1877–1894. https://doi.org/10.1145/3531146.3533234

- Proposes a framework to measure operational software carbon intensity using location- and time-specific marginal emissions data. Finds that choosing cloud region delivers the largest operational emissions reductions. Methodological analogue for CPC translation: why relocation matters for emissions conditional on grid.
- **Use in proposal:** §2.1 outcome motivation.
- **Tags:** `AI-carbon`; `marginal-emissions`; `CPC-framework`; `outcome`
- **Filename:** `dodge_2022_carbon_intensity_ai_cloud.md`

**Luccioni, A. S., Viguier, S., & Ligozat, A.-L. (2023).** Estimating the carbon footprint of BLOOM, a 176B parameter language model. *Journal of Machine Learning Research, 24*(253), 1–15. https://www.jmlr.org/papers/v24/23-0069.html

- Lifecycle estimate including inference and deployment emissions under different usage assumptions and energy sources. Supports the argument that AI-related electricity demand is not confined to training and that EDWC relocation can change emissions even holding models constant.
- **Use in proposal:** §1.1.1 background; §2.1 outcome motivation.
- **Tags:** `AI-carbon`; `inference`; `lifecycle`; `outcome`
- **Filename:** `luccioni_2023_bloom_carbon_footprint.md`

### 1.3 Workload migration mechanism

**Zheng, J., Chien, A. A., & Suh, S. (2020).** Mitigating curtailment and carbon emissions through load migration between data centers. *Joule, 4*(10), 2208–2222. https://doi.org/10.1016/j.joule.2020.08.001

- Quantifies how migrating flexible loads between DCs can reduce renewable curtailment and CO₂ (113–239 ktCO₂e/year between PJM and CAISO). The clearest conceptual precursor to EDWC's east-to-west migration logic. Critically, it implies the sign of emissions effects is theoretically ambiguous — reinforcing why provincial electricity and CO₂ outcomes must be empirically estimated rather than assumed.
- **Use in proposal:** §2.1 mechanism; §1.1.2 policy framing; §2.4 research gap.
- **Tags:** `workload-migration`; `grid-interactions`; `curtailment`; `emissions`; `outcome`
- **Filename:** `zheng_2020_load_migration_curtailment.md`

### 1.4 China DC energy and emissions

**Ni, W., Hu, X., Du, H., Kang, Y., Ju, Y., & Wang, Q. (2024).** CO₂ emission-mitigation pathways for China's data centers. *Resources, Conservation & Recycling, 202*, 107383. https://doi.org/10.1016/j.resconrec.2023.107383

- Kaya–LMDI decomposition of China DC CO₂ emissions (2017–2021) showing substantial cross-province heterogeneity; identifies expanding computing scale as primary driver. Key China-specific evidence that DCs are already a nontrivial emissions source with provincial variation, motivating a causal EDWC evaluation.
- **Use in proposal:** §1.1 China framing; §2.1 China-side outcome evidence; §2.4 provincial-heterogeneity motivation.
- **Tags:** `China-DC`; `emissions`; `China-provincial`; `decomposition`; `outcome`
- **Filename:** `ni_2024_china_dc_emissions_pathways.md`

**Greenpeace East Asia. (2021).** *China 5G and Data Center Carbon Emissions Outlook 2035* (English briefing). https://www.greenpeace.org/static/planet4-eastasia-stateless/2021/05/a5886d59-china-5g-and-data-center-carbon-emissions-outlook-2035-english.pdf

- Non-peer-reviewed but provides concrete China projections (~782 billion kWh by 2035) and provincial concentration narrative. Use if §1.1 needs a magnitude citation.
- **Use in proposal:** §1.1 background; §1.1.2 policy framing.
- **Tags:** `China-DC`; `electricity-demand`; `Greenpeace`; `outcome`
- **Filename:** `greenpeace_2021_china_5g_dc_outlook.md`

### 1.5 EDWC-specific evaluations (closest prior work)

**Zhang, N., Duan, H., Guan, Y., Mao, R., Song, G., Yang, J., & Shan, Y. (2025).** The "Eastern Data and Western Computing" initiative in China contributes to its net-zero target. *Engineering, 52*, 256–261. https://doi.org/10.1016/j.eng.2024.08.010

- High-level assessment of EDWC's role in China's net-zero strategy. Frames the policy as relocating DCs westward to leverage renewable energy and climatic advantages. Estimates 16–20% emission reduction by 2030 under scenario analysis. Functions as policy assessment, not provincial causal inference — helping isolate the gap: actual, measured provincial electricity impacts remain unestimated.
- **Use in proposal:** §1.1.2 policy framing; §2.4 research gap (prospective, not causal).
- **Tags:** `EDWC`; `policy-assessment`; `China-netzero`; `scenario-analysis`; `outcome`
- **Filename:** `zhang_duan_2025_edwc_net_zero.md`

**Zhang, Y., Li, H., & Wang, S. (2025).** Decarbonizing data centers through regional bits migration: A comprehensive assessment of China's "eastern data, Western computing" initiative and its global implications. *Applied Energy, 392*, 126020. https://doi.org/10.1016/j.apenergy.2025.126020

- Quantitatively closest prior EDWC work. Route-by-route simulation finding energy-saving potential of ~332–942 GWh/year from cooling reductions and avoided transmission losses; carbon outcomes depend strongly on interregional emissions-factor differences (Shanghai–Sichuan saves 80% carbon; Beijing–Inner Mongolia increases emissions 25%). Remains simulation rather than ex post causal estimation — the paper the proposal most directly improves upon.
- **Use in proposal:** §2.1 closest prior work; §2.4 direct gap reference.
- **Tags:** `EDWC`; `bits-migration`; `grid-mix`; `Applied-Energy`; `outcome`
- **Filename:** `zhang_li_wang_2025_edwc_bits_migration.md`

**Xie, X., Han, Y., & Tan, H. (2024).** Greening China's digital economy: exploring the contribution of the East–West Computing Resources Transmission Project to CO₂ reduction. *Humanities and Social Sciences Communications, 11*, Article 466. https://doi.org/10.1057/s41599-024-02963-0

- Scenario-based CO₂ reduction estimates for EDWC over 2020–2050; analyzes heterogeneous strategy bundles across hub configurations using fuzzy-set QCA. Third EDWC-focused peer-reviewed study. Clarifies that much EDWC research is prospective rather than a province-year causal evaluation.
- **Note:** Earlier notes may reference this as "Guo et al. (2024)" — the correct authorship is Xie, Han & Tan (2024).
- **Use in proposal:** §1.1.2 policy framing; §2.4 research gap.
- **Tags:** `EDWC`; `China-digital-economy`; `CO2-scenarios`; `outcome`
- **Filename:** `xie_2024_ewcrt_co2_reduction.md`

### 1.6 Carbon Monitor data methodology

**Liu, Z., Ciais, P., Deng, Z., et al. (2020).** Carbon Monitor, a near-real-time daily dataset of global CO₂ emission from fossil fuel and cement production. *Scientific Data, 7*, 392. https://doi.org/10.1038/s41597-020-00708-7

- Foundational dataset-methodology paper for Carbon Monitor. Documents the activity-data methodology for daily, sector-resolved CO₂ estimates. Required citation whenever the proposal's complementary CO₂ outcome data are used.
- **Use in proposal:** §3.3 data source; §2.1 background.
- **Tags:** `Carbon-Monitor`; `CO2-daily`; `methodology`; `data-source`; `outcome`
- **Filename:** `liu_2020_carbon_monitor_dataset.md`

---

## Stream 2 — Design: Causal Identification

### 2.1 Classic place-based infrastructure evaluations

**Kline, P., & Moretti, E. (2014).** Local economic development, agglomeration economies, and the big push: 100 years of evidence from the Tennessee Valley Authority. *Quarterly Journal of Economics, 129*(1), 275–331. https://doi.org/10.1093/qje/qjt034

- Canonical evaluation of a large, historically important place-based infrastructure program using panel quasi-experimental methods. Template for treating a geographically targeted infrastructure rollout as a quasi-experimental "shock" suitable for event-study style causal evaluation — analogous to EDWC's province go-live dates.
- **Use in proposal:** §2.2 lead example; §2.4 design-side gap.
- **Tags:** `place-based-policy`; `infrastructure-shock`; `event-study`; `DiD-precedent`; `design`
- **Filename:** `kline_moretti_2014_tva_big_push.md`

**Greenstone, M., Hornbeck, R., & Moretti, E. (2010).** Identifying agglomeration spillovers: Evidence from winners and losers of large plant openings. *Journal of Political Economy, 118*(3), 536–598. https://doi.org/10.1086/653714

- Estimates causal spillovers by comparing "winner" and "loser" locations around discrete, high-stakes place-based shocks (large plant openings). Widely cited template for framing localized, timed interventions as quasi-experiments — the same logic underlying EDWC's staggered activation.
- **Use in proposal:** §2.2 design template; §2.4 design-side gap.
- **Tags:** `place-based-policy`; `infrastructure-shock`; `quasi-experiment`; `event-time`; `design`
- **Filename:** `greenstone_2010_plant_openings_spillovers.md`

**Busso, M., Gregory, J., & Kline, P. (2013).** Assessing the incidence and efficiency of a prominent place based policy. *American Economic Review, 103*(2), 897–947. https://doi.org/10.1257/aer.103.2.897

- Evaluates a place-based designation using rejected and future applicants as controls. Demonstrates how careful comparison-group construction supports credible causal inference — the same logic (treated vs not-yet/never-treated) underlying EDWC's staggered event-study.
- **Use in proposal:** §2.2 control-group design example.
- **Tags:** `place-based-policy`; `DiD-precedent`; `control-group`; `policy-evaluation`; `design`
- **Filename:** `busso_2013_place_based_policy.md`

### 2.2 China infrastructure evaluations using DiD

**Lu, Y., Wang, J., & Zhu, L. (2019).** Place-based policies, creation, and agglomeration economies: Evidence from China's economic zone program. *American Economic Journal: Economic Policy, 11*(3), 325–360. https://doi.org/10.1257/pol.20160272

- Uses rich administrative and firm data to estimate effects of China's economic zone program. Directly supports the proposal's claim that modern causal evaluation of place-based policy using panel quasi-experiments has strong precedent in China-focused economics — making an EDWC staggered event-study methodologically "native" to the field.
- **Use in proposal:** §2.2 China-specific applied precedent; §2.4 design-side gap.
- **Tags:** `China-policy`; `economic-zones`; `place-based-policy`; `DiD`; `design`
- **Filename:** `lu_wang_zhu_2019_china_economic_zones.md`

### 2.3 Applied DiD in energy and environment

**Wang, H., Zhang, Y., Lin, W., & Wei, W. (2023).** Transregional electricity transmission and carbon emissions: Evidence from ultra-high voltage transmission projects in China. *Energy Economics, 123*, 106751. https://doi.org/10.1016/j.eneco.2023.106751

- Treats UHV transmission projects as a quasi-natural experiment with staggered timing DiD to estimate impacts on total carbon emissions and carbon intensity. The closest published methodological parallel to the proposal: same method (staggered DiD), same country (China), same type of outcome (energy/emissions), infrastructure go-live timing.
- **Use in proposal:** §2.2 direct methodological analogue; §3.4 design precedent; §3.4.4 robustness framing.
- **Tags:** `energy-DiD`; `China-infrastructure`; `emissions`; `staggered-DiD`; `UHV`; `design`
- **Filename:** `wang_2023_uhv_emissions_staggered_did.md`

**Deryugina, T., MacKay, A., & Reif, J. (2020).** The long-run dynamics of electricity demand: Evidence from municipal aggregation. *American Economic Journal: Applied Economics, 12*(1), 86–114. https://doi.org/10.1257/app.20180256

- Uses municipal aggregation in Illinois as a natural experiment producing large, long-lasting electricity price changes across 250+ communities. Combines DiD with matching to estimate dynamic price elasticities of residential electricity demand using monthly data. Shows elasticity grows from −0.09 at 6 months to −0.27 at 2 years, demonstrating that electricity consumption responds dynamically to shocks over multi-year horizons. Methodologically valuable as a high-quality precedent for applying DiD/event-study methods to monthly electricity consumption data at the sub-national level, with careful parallel-trends validation, placebo tests, and anticipation checks. The paper's event-study figures, table structure, and robustness design provide a useful template for presenting the EDWC results.
- **Use in proposal:** §2.2 as a precedent for causal evaluation of sub-national electricity-consumption effects using monthly panel data and event-study logic; §3.4 as a methodological guide for table/figure structure and robustness design. The setting differs from the proposal (price shock vs infrastructure shock), but the outcome variable (monthly electricity consumption) and the empirical toolkit (DiD with event-time plots, pre-trend validation, placebo exercises) are directly parallel.
- **Tags:** `electricity-demand`; `DiD`; `event-study`; `monthly-panel`; `design`
- **Filename:** `deryugina_2020_electricity_demand_dynamics.md`

### 2.4 Modern staggered-DiD methodology

**Sun, L., & Abraham, S. (2021).** Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics, 225*(2), 175–199. https://doi.org/10.1016/j.jeconom.2020.09.006

- Shows that TWFE event-study coefficients with leads/lags can be contaminated under staggered adoption with heterogeneous treatment effects, producing misleading dynamics and spurious "pre-trends." Directly justifies implementing a Sun–Abraham style cohort-interacted event study as the main estimator for EDWC. The proposal's main estimator is named after this paper.
- **Use in proposal:** §3.4 main estimator justification; §3.4.2 event-study specification; §2.4 design-side gap.
- **Tags:** `Sun-Abraham`; `staggered-DiD`; `event-study`; `TWFE-bias`; `design`
- **Filename:** `sun_abraham_2021_event_study_het.md`

**Callaway, B., & Sant'Anna, P. H. C. (2021).** Difference-in-differences with multiple time periods. *Journal of Econometrics, 225*(2), 200–230. https://doi.org/10.1016/j.jeconom.2020.12.001

- Provides identification, estimation, and inference for ATT in multi-period panels with staggered timing, emphasizing "clean" comparisons (treated vs not-yet-treated) under parallel trends. Standard complementary reference for EDWC's staggered rollout; can be cited as an alternative estimator family for robustness alongside Sun–Abraham.
- **Use in proposal:** §3.4 alternative estimator; §3.4.4 robustness reference.
- **Tags:** `Callaway-SantAnna`; `staggered-DiD`; `ATT`; `robustness`; `design`
- **Filename:** `callaway_santanna_2021_did_multiple_periods.md`

**Goodman-Bacon, A. (2021).** Difference-in-differences with variation in treatment timing. *Journal of Econometrics, 225*(2), 254–277. https://doi.org/10.1016/j.jeconom.2021.03.014

- Decomposes the TWFE DiD estimator into weighted averages of all possible two-group/two-period comparisons, clarifying when problematic weighting arises under staggered timing. Supports the "why not TWFE" argument in the proposal. Note: correctly published in *Journal of Econometrics*, not *Econometrica* as sometimes misattributed.
- **Use in proposal:** §3.4 "why not TWFE" explanation; §2.4 design-side gap.
- **Tags:** `Goodman-Bacon`; `TWFE-weights`; `staggered-DiD`; `identification`; `design`
- **Filename:** `goodman_bacon_2021_did_timing.md`

**de Chaisemartin, C., & D'Haultfœuille, X. (2020).** Two-way fixed effects estimators with heterogeneous treatment effects. *American Economic Review, 110*(9), 2964–2996. https://doi.org/10.1257/aer.20181169

- Shows that TWFE regressions can place negative weights on some group-time treatment effects under heterogeneity, so the pooled coefficient can be misleading even in sign. High-profile AER anchor for replacing TWFE with staggered-robust estimators.
- **Use in proposal:** §3.4 methodological justification; §2.4 design-side gap.
- **Tags:** `TWFE-bias`; `negative-weights`; `heterogeneous-effects`; `staggered-DiD`; `design`
- **Filename:** `dechaisemartin_dhaultfoeuille_2020_twfe.md`

**Borusyak, K., Jaravel, X., & Spiess, J. (2024).** Revisiting event-study designs: Robust and efficient estimation. *Review of Economic Studies, 91*(6), 3253–3285. https://doi.org/10.1093/restud/rdae007

- Reframes staggered event studies as DiD designs and derives a robust, efficient "imputation" estimator with tools for inference and pre-trend testing. Cutting-edge justification that modern event-study practice should match estimands and assumptions to estimators.
- **Use in proposal:** §3.4 methodology; §3.4.4 robustness reference.
- **Tags:** `event-study`; `imputation`; `staggered-DiD`; `inference`; `design`
- **Filename:** `borusyak_2024_event_study_imputation.md`

### 2.5 Synthetic control methodology

**Abadie, A., Diamond, A., & Hainmueller, J. (2010).** Synthetic control methods for comparative case studies: Estimating the effect of California's tobacco control program. *Journal of the American Statistical Association, 105*(490), 493–505. https://doi.org/10.1198/jasa.2009.ap08746

- Introduces synthetic control as a transparent way to build a weighted comparison unit for a single treated unit. Canonical methodological citation for the supplementary synthetic-Gansu exercise alongside the main staggered DiD.
- **Use in proposal:** §3.4.4 robustness (supplementary SCM for Gansu).
- **Tags:** `SCM`; `synthetic-control`; `robustness`; `comparative-case`; `design`
- **Filename:** `abadie_2010_scm_tobacco.md`

**Abadie, A., Diamond, A., & Hainmueller, J. (2015).** Comparative politics and the synthetic control method. *American Journal of Political Science, 59*(2), 495–510. https://doi.org/10.1111/ajps.12116

- Clarifies SCM logic for comparative case studies; emphasizes transparency in counterfactual construction. Supports a concise write-up of supplementary SCM.
- **Use in proposal:** §3.4.4 robustness reference.
- **Tags:** `SCM`; `comparative-case`; `robustness`; `counterfactual`; `design`
- **Filename:** `abadie_2015_scm_comparative_politics.md`

---

## Stream 3 — Measurement: CPC Framework

### 3.1 Carbon-accounting frameworks for compute

**Gupta, U., Kim, Y. G., Lee, S., Tse, J., Lee, H.-H. S., Wei, G. Y., Brooks, D., & Wu, C.-J. (2022).** Chasing Carbon: The Elusive Environmental Footprint of Computing. *IEEE Micro, 42*(4), 37–47. https://doi.org/10.1109/MM.2022.3163226

- The clearest operational-vs-embodied decomposition for computing carbon. Establishes that electricity and CO₂ should be translated into a rate-based compute metric rather than treated as raw energy totals alone. The accounting-logic foundation for CPC.
- **CPC component:** Accounting framework
- **Use in proposal:** §2.3 opening framework; §3.4.3 CPC justification; §2.4 measurement gap; §4 contribution.
- **Tags:** `CPC`; `accounting-framework`; `embodied-carbon`; `operational-carbon`; `measurement`
- **Filename:** `gupta_2022_chasing_carbon.md`

**Radovanović, A., Koningstein, R., Schneider, I., et al. (2023).** Carbon-aware computing for datacenters. *IEEE Transactions on Power Systems, 38*(2), 1270–1280. https://doi.org/10.1109/TPWRS.2022.3173250

- Canonical system-method paper on time- and location-specific grid carbon signals as inputs to compute scheduling and carbon accounting. Grounds the CI term conceptually: carbon per unit of compute depends on where and when workloads run, even when electricity use is unchanged.
- **CPC component:** Accounting framework (grounds CI logic)
- **Use in proposal:** §2.3 carbon-aware computing; §3.4.3 CI justification.
- **Tags:** `carbon-aware-computing`; `grid-CI`; `scheduling`; `CPC`; `measurement`
- **Filename:** `radovanovic_2023_carbon_aware_computing.md`

**Green Software Foundation. (2024).** *Software Carbon Intensity (SCI) specification* (ISO/IEC 21031:2024). https://sci.greensoftware.foundation/

- Formal rate-based accounting standard: operational + embodied emissions normalized by a functional unit. Directly parallel to CPC's structure (CO₂ per exaflop-hour replacing SCI's software service unit).
- **CPC component:** Accounting framework
- **Use in proposal:** §2.3 standards reference; §3.4.3 CPC structure; §4 contribution framing.
- **Tags:** `SCI`; `carbon-accounting`; `functional-unit`; `standards`; `measurement`
- **Filename:** `gsf_2024_sci_specification.md`

**Freitag, C., Berners-Lee, M., Widdicks, K., Knowles, B., Blair, G. S., & Friday, A. (2021).** The real climate and transformative impact of ICT: A critique of estimates, trends and regulations. *Patterns, 2*(9), Article 100340. https://doi.org/10.1016/j.patter.2021.100340

- Meta-methodology critique establishing that ICT carbon measurement is itself contested; lifecycle scope choices and truncation materially change results. Supports the claim that measurement-side innovation is a recognized problem.
- **CPC component:** Accounting framework (meta level)
- **Use in proposal:** §2.3 ICT measurement challenge; §2.4 measurement gap; §4 contribution.
- **Tags:** `ICT-footprint`; `lifecycle`; `measurement-critique`; `CPC`; `measurement`
- **Filename:** `freitag_2021_ict_climate_critique.md`

### 3.2 PUE and facility efficiency

**The Green Grid. (2012).** *PUE: A comprehensive examination of the metric* (White Paper 49). https://www.thegreengrid.org/en/resources/library-and-tools/237-WP%2349---PUE%3A-A-Comprehensive-Examination-of-the-Metric

- Canonical PUE practitioner document covering definition, measurement, reporting, interpretation, and globally harmonized guidelines. Use for accessible explanations of PUE in the proposal text.
- **CPC component:** PUE / facility efficiency
- **Use in proposal:** §3.4.3 PUE construction; §3.2 variable definition; §2.3 standards.
- **Tags:** `PUE`; `data-center-efficiency`; `standards`; `facility-efficiency`; `measurement`
- **Filename:** `green_grid_2012_pue_wp49.md`

**Yuventi, J., & Mehdizadeh, R. (2013).** A critical analysis of Power Usage Effectiveness and its use in communicating data center energy consumption. *Energy and Buildings, 64*, 90–94. https://doi.org/10.1016/j.enbuild.2013.04.015

- Best critique of PUE as a communication metric: explains why instantaneous or cherry-picked PUE values can mislead, why time-averaged energy-based interpretation matters. Strengthens the argument that CPC embeds PUE in a broader carbon-per-compute framework that corrects what PUE alone misses.
- **CPC component:** PUE / facility efficiency (critique)
- **Use in proposal:** §2.3 PUE critique; §3.4.3 CPC design rationale.
- **Tags:** `PUE`; `metric-critique`; `facility-efficiency`; `data-centers`; `measurement`
- **Filename:** `yuventi_2013_pue_critique.md`

### 3.3 Compute efficiency benchmarks (GF/W)

**Energy Efficient High Performance Computing Working Group. (2015).** *Energy Efficient High Performance Computing Power Measurement Methodology* (Version 2.0 RC 1.0). TOP500/Green500. https://www.top500.org/static/media/uploads/methodology-2.0rc1.pdf

- Formalizes how system power under benchmark load is measured for Green500, including quality levels, instrumentation boundaries, and full-run reporting. Essential to justify using Green500-style audited performance-per-watt data as the GF/W base in CPC.
- **CPC component:** Compute efficiency (GF/W)
- **Use in proposal:** §3.4.3 GF/W construction; §3.2 variable definition; §2.3 benchmarking.
- **Tags:** `Green500`; `GF-W`; `benchmark-methodology`; `power-measurement`; `measurement`
- **Filename:** `eehpc_2015_green500_methodology.md`

**Dongarra, J., & Luszczek, P. (2026).** HPL-MxP benchmark: Mixed-precision algorithms, iterative refinement, and scalable data generation. *The International Journal of High Performance Computing Applications*. https://doi.org/10.1177/10943420251382476

- The strongest bridge from FP64-oriented HPC efficiency to AI-relevant mixed-precision throughput. Makes the HPL-MxP speedup step in the GF/W construction methodologically citeable rather than purely heuristic.
- **CPC component:** Compute efficiency (GF/W)
- **Use in proposal:** §3.4.3 HPL-MxP multiplier; §3.2 variable definition; §2.3 benchmarking.
- **Tags:** `HPL-MxP`; `mixed-precision`; `GF-W`; `AI-benchmark`; `measurement`
- **Filename:** `dongarra_luszczek_2026_hpl_mxp.md`

**Tschand, A., Rajan, A. T. R., Idgunji, S., et al. (2025).** MLPerf Power: Benchmarking the energy efficiency of machine learning systems from microwatts to megawatts for sustainable AI. *2025 IEEE HPCA*, 1201–1216. https://arxiv.org/abs/2410.12032

- ML-specific energy-efficiency benchmarking at system level; emphasizes reproducible wall-power measurement and comparability across hardware classes. Validates the broader move from peak specs to benchmarked, workload-relevant efficiency measures. Cite narrowly for ML-specific benchmarking.
- **CPC component:** Compute efficiency (GF/W)
- **Use in proposal:** §2.3 ML-specific benchmarking; §3.4.3 GF/W construction.
- **Tags:** `MLPerf-Power`; `AI-efficiency`; `system-power`; `benchmark`; `measurement`
- **Filename:** `tschand_2025_mlperf_power.md`

**Fernandez, J., Wehrstedt, L., Shamis, L., et al. (2025).** Efficient Hardware Scaling and Diminishing Returns in Large-Scale Training of Language Models. *Transactions on Machine Learning Research*. https://openreview.net/forum?id=p7jQEf3wlh

- Shows that realized training efficiency declines with scale as communication overhead rises and MFU falls, even when nominal accelerator capability increases. Best justification for the MFU term and the China interconnect adjustment (A800/H800 bandwidth haircut) in the GF/W construction. Cite narrowly.
- **CPC component:** Compute efficiency (GF/W)
- **Use in proposal:** §3.4.3 MFU / interconnect adjustment; §3.2 variable definition.
- **Tags:** `MFU`; `interconnect`; `distributed-training`; `realized-efficiency`; `measurement`
- **Filename:** `fernandez_2025_hardware_scaling_llm.md`

### 3.4 Carbon intensity and emission factor methodology

**Shan, Y., Liu, J., Liu, Z., Xu, X., Shao, S., Wang, P., & Guan, D. (2016).** New provincial CO₂ emission inventories in China based on apparent energy consumption data and updated emission factors. *Applied Energy, 184*, 742–750. https://doi.org/10.1016/j.apenergy.2016.03.073

- Core China-provincial emissions-method paper linking apparent energy consumption to updated local emission factors, explicitly referenced by CEADs as a method source. Grounds the provincial CI side of CPC in China-specific subnational accounting rather than generic national default factors.
- **CPC component:** Carbon intensity (CI)
- **Use in proposal:** §3.4.3 CI construction; §3.2 variable definition; §2.3 methodology. Also supporting context in Stream 4 for provincial carbon-intensity variation.
- **Tags:** `CEADs`; `emission-factors`; `provincial-CO2`; `carbon-intensity`; `measurement`
- **Filename:** `shan_2016_china_provincial_emissions.md`

### 3.5 China institutional context for CPC

**China Academy of Information and Communications Technology. (2023).** *中国算力发展指数白皮书（2023年）* [China Computing Power Development Index White Paper (2023)]. CAICT, No. 202306, September 2023.

- Primary Chinese institutional document publishing a provincial-level computing-power development index together with national compute-capacity totals (2022: 180 EFlops basic-infrastructure scale, 302 EFlops total, 33% global share; 25 intelligent-compute centres in operation). Provides the quantified provincial compute-capacity context that complements CAICT 2024's green-compute framing — the 2023 report is the compute-scale/index anchor, the 2024 report the carbon/efficiency anchor. Supports the proposal's EDWC framing by giving quantified provincial compute concentration and growth rates prior to and during the go-live window.
- **CPC component:** China institutional context (compute-scale / index)
- **Use in proposal:** §1.1.2 compute-scale quantification; §2.3 institutional framing; §3 interpretation of provincial compute concentration.
- **Tags:** `CAICT`; `computing-power-index`; `China-provincial`; `institutional-context`; `measurement`
- **Filename:** `caict_2023_computing_power_index.md`

**China Academy of Information and Communications Technology & Horinger New Area. (2024).** *中国绿色算力发展研究报告（2024年）* [China Green Computing Power Development Research Report (2024)]. https://www.caict.ac.cn/kxyj/qwfb/ztbg/202407/P020240711551514828756.pdf

- Primary Chinese institutional document organizing green computing around devices, facilities, compute-energy coordination, and regional hub development. Establishes that China already treats green compute as a multi-component measurement and governance problem — but has not built an integrated provincial CPC metric. Directly supports the measurement-side gap.
- **CPC component:** China institutional context
- **Use in proposal:** §2.3 institutional framing; §2.4 measurement gap; §4 contribution claim.
- **Tags:** `CAICT`; `green-computing`; `China`; `institutional-context`; `measurement`
- **Filename:** `caict_2024_green_computing_report.md`

**RMI. (2024, November).** *Powering the data-center boom with low-carbon solutions: China's perspective and global insights*. https://rmi.org/wp-content/uploads/dlm_uploads/2024/11/powering_the_data_center_boom.pdf

- Connects China's computing-power boom to low-carbon electricity, infrastructure planning, green power trading, and national computing-network policy. Explicitly cites CAICT 2024. Justifies why a province-level CPC measure is policy-relevant in the EDWC setting.
- **CPC component:** China institutional context
- **Use in proposal:** §2.3 institutional bridge; §2.4 measurement gap; §4 contribution claim.
- **Tags:** `RMI`; `China`; `low-carbon-data-centers`; `EDWC-context`; `measurement`
- **Filename:** `rmi_2024_china_data_center_low_carbon.md`

---

## Stream 4 — China Context: Provincial Energy System

### 4.1 Provincial emissions and carbon-intensity context

**Shan et al. (2016)** — see Stream 3 §3.4. In this stream, use as supporting context for provincial carbon-intensity variation. Do not lead with it here; primary citation home is Stream 3.

**Liao, C. Y., Wang, S. G., Zhang, Y. Y., Song, D., & Zhang, C. H. (2019).** Driving forces and clustering analysis of provincial-level CO₂ emissions from the power sector in China from 2005 to 2015. *Journal of Cleaner Production, 240*, 118026.

- Shows that provincial power-sector emissions follow different structural patterns (clustering analysis), strengthening heterogeneity language.
- **Use in proposal:** §3 carbon-intensity context; §3 heterogeneity / interpretation.
- **Tags:** `power-sector-co2`; `provincial-heterogeneity`; `generation-side`; `china-context`
- **Filename:** `liao_2019_power_sector_co2_clustering.md`

### 4.2 Renewable curtailment and utilization

**Liu, S., Bie, Z., Lin, J., & Wang, X. (2018).** Curtailment of renewable energy in Northwest China and market-based solutions. *Energy Policy, 123*, 494–502. https://doi.org/10.1016/j.enpol.2018.09.007

- Most directly relevant northwest-China curtailment paper. Ties western renewable abundance to under-utilization and institutional barriers rather than automatic clean absorption.
- **Use in proposal:** §1.1.3 background; §3 heterogeneity / interpretation.
- **Tags:** `curtailment`; `northwest-china`; `renewable-utilization`; `china-context`
- **Filename:** `liu_2018_curtailment_northwest_china.md`

**Song, F., Bi, D., & Wei, C. (2019).** Market segmentation and wind curtailment: An empirical analysis. *Energy Policy, 132*, 831–838.

- Shows that curtailment is not only a resource issue — interprovincial market segmentation itself matters.
- **Use in proposal:** §3 heterogeneity / interpretation; §3 transmission / grid context.
- **Tags:** `wind-curtailment`; `market-segmentation`; `dispatch-frictions`; `china-context`
- **Filename:** `song_2019_market_segmentation_wind_curtailment.md`

**Zhang, X., Wang, J.-X., Cao, Z., Shen, S., Meng, S., & Fan, J.-L. (2021).** What is driving the remarkable decline of wind and solar power curtailment in China? Evidence from China and four typical provinces. *Renewable Energy, 174*, 31–42. https://doi.org/10.1016/j.renene.2021.04.043

- Decomposes local absorption vs UHV and conventional transmission contributions to curtailment decline. Maps onto interpretation logic: transmission structure and local demand absorption differ across western provinces.
- **Use in proposal:** §1.1.3 background; §3 heterogeneity / interpretation.
- **Tags:** `wind-curtailment`; `solar-curtailment`; `UHV`; `provincial-cases`; `china-context`
- **Filename:** `zhang_2021_decline_wind_solar_curtailment.md`

### 4.3 Transmission and interprovincial electricity flows

**Qu, S., Liang, S., & Xu, M. (2017).** CO₂ emissions embodied in interprovincial electricity transmissions in China. *Environmental Science & Technology, 51*(18), 10893–10902. https://doi.org/10.1021/acs.est.7b01814

- Core paper for carbon embodied in interprovincial electricity trade. Prevents an overly local interpretation of provincial emissions effects.
- **Use in proposal:** §3 carbon-intensity context; §3 transmission / grid context.
- **Tags:** `embodied-carbon`; `interprovincial-electricity`; `purchased-electricity`; `china-context`
- **Filename:** `qu_2017_embodied_co2_electricity_transmission.md`

**Deng, X., Lv, T., Xu, J., Hou, X., & Liu, F. (2022).** Assessing the integration effect of inter-regional transmission on variable power generation under renewable energy consumption policy in China. *Energy Policy, 170*, 113219. https://doi.org/10.1016/j.enpol.2022.113219

- Links transmission capacity to renewable accommodation under China's policy setting.
- **Use in proposal:** §1.1.3 background; §3 transmission / grid context; §3 heterogeneity / interpretation.
- **Tags:** `transmission`; `renewable-consumption`; `interregional-flows`; `flexibility`; `china-context`
- **Filename:** `deng_2022_interregional_transmission_variable_power.md`

### 4.4 Provincial grid and electricity-market context

**Guo, H., Davidson, M. R., Chen, Q., Zhang, D., Jiang, N., Xia, Q., Kang, C., & Zhang, X. (2020).** Power market reform in China: Motivations, progress, and recommendations. *Energy Policy, 145*, 111717. https://doi.org/10.1016/j.enpol.2020.111717

- Best compact review of post-2015 power-market reform, dispatch change, and interprovincial coordination problems. Justifies why dispatch and pricing institutions may cause the same EDWC demand shock to map differently into generation, imports, and carbon across provinces.
- **Use in proposal:** §3 grid / dispatch context; §3 heterogeneity / interpretation.
- **Tags:** `power-market-reform`; `dispatch`; `provincial-markets`; `institutional-context`; `china-context`
- **Filename:** `guo_2020_power_market_reform_china.md`

**Xiang, C., Zheng, X., Song, F., Lin, J., & Jiang, Z. (2023).** Assessing the roles of efficient market versus regulatory capture in China's power market reform. *Nature Energy, 8*(7), 747–757. https://doi.org/10.1038/s41560-023-01278-9

- Strongest evidence that local protection and regulatory capture shape power-market outcomes, limiting efficient dispatch and emissions gains.
- **Use in proposal:** §3 heterogeneity / interpretation; §3 transmission / grid context.
- **Tags:** `regulatory-capture`; `dispatch-frictions`; `local-protection`; `power-market-reform`; `china-context`
- **Filename:** `xiang_2023_market_vs_regulatory_capture.md`

### 4.5 EDWC policy and institutional documents

**National Development and Reform Commission. (2023, December 29).** *关于深入实施"东数西算"工程加快构建全国一体化算力网的实施意见（发改数据〔2023〕1779号）* [Implementation opinions on deeply advancing the Eastern Data, Western Compute project and accelerating the building of an integrated national computing network].

- Core official EDWC policy text linking westward siting, compute-power coordination, and clean-energy advantages.
- **Use in proposal:** §1.1.2 EDWC policy; §1.1.4 policy context; §3 interpretation.
- **Tags:** `edwc-policy`; `hub-nodes`; `compute-network`; `policy-context`; `china-context`
- **Filename:** `ndrc_2023_edwc_integrated_computing_network.md`

**National Development and Reform Commission, Ministry of Industry and Information Technology, National Energy Administration, & National Data Administration. (2024, July 23).** *数据中心绿色低碳发展专项行动计划* [Special action plan for green and low-carbon development of data centers].

- Implementation-level source on hub-first siting, renewable links, and PUE/green data-center requirements.
- **Use in proposal:** §1.1.3 background; §1.1.4 policy context.
- **Tags:** `green-data-centers`; `renewable-power`; `PUE`; `policy-context`; `china-context`
- **Filename:** `ndrc_miit_nea_nda_2024_green_datacenter_action_plan.md`

---

## Paper-to-Section Mapping

### §1.1 Research Background

| Sub-section | Papers |
|---|---|
| §1.1.1 AI compute demand and electricity | Masanet (2020); Shehabi (2024); IEA (2025); Patterson (2022) |
| §1.1.2 Eastern Data, Western Compute | Zhang/Duan (2025); Zhang/Li/Wang (2025); Xie (2024); NDRC 2023 |
| §1.1.3 Renewable energy and DC siting | Liu S. (2018); Zhang X. (2021); Deng (2022); NDRC/MIIT/NEA/NDA 2024 |
| §1.1.4 Policy targets | CAICT (2024); NDRC 2024 green DC plan |

### §2 Literature Review

| Sub-section | Papers |
|---|---|
| §2.1 Energy/emissions effects of compute infrastructure | Masanet (2020); Shehabi (2024); IEA (2025); Patterson (2021, 2022); Zheng (2020); Ni (2024); Zhang/Duan (2025); Zhang/Li/Wang (2025) |
| §2.2 Place-based infrastructure policies and causal evaluation | Kline–Moretti (2014); Greenstone et al. (2010); Busso et al. (2013); Lu–Wang–Zhu (2019); Wang et al. (2023); Deryugina et al. (2020); Sun–Abraham (2021); Callaway–Sant'Anna (2021); Goodman-Bacon (2021); de Chaisemartin–D'Haultfœuille (2020) |
| §2.3 Energy–compute accounting and carbon metrics | Gupta (2022); Radovanović (2023); Freitag (2021); SCI/GSF (2024); Green Grid (2012); Dongarra–Luszczek (2026); Shan (2016); CAICT (2023); CAICT (2024) |
| §2.4 Literature summary and research gap | Outcome gap: Zhang/Li/Wang (2025), Zhang/Duan (2025), Zheng (2020), Ni (2024). Design gap: Sun–Abraham (2021), Goodman-Bacon (2021). Measurement gap: Gupta (2022), CAICT (2024) |

### §3 Research Content and Design

| Sub-section | Papers |
|---|---|
| §3.2 Variables | Shan (2016) for CI; Green Grid (2012) for PUE; EEHPC (2015) + Dongarra–Luszczek (2026) for GF/W |
| §3.3 Data sources | Liu Z. (2020) Carbon Monitor (provincial daily CO₂ panel for China) |
| §3.4.1 Identification | Sun–Abraham (2021); Callaway–Sant'Anna (2021); Goodman-Bacon (2021); de Chaisemartin–D'Haultfœuille (2020) |
| §3.4.2 Event-study model | Sun–Abraham (2021); Borusyak et al. (2024); Deryugina et al. (2020) for table/figure structure |
| §3.4.3 CPC construction | Gupta (2022); Radovanović (2023); Green Grid (2012); EEHPC (2015); Dongarra–Luszczek (2026); Shan (2016); CAICT (2024); Fernandez (2025) for MFU |
| §3.4.4 Robustness | Abadie et al. (2010, 2015) for SCM; Borusyak et al. (2024) for imputation |
| §3.5 Feasibility / interpretation | Qu (2017); Guo (2020); Xiang (2023) |

### §4 Contributions and Innovations

- Academic: Sun–Abraham (2021) + Zhang/Li/Wang (2025) frame "first causal EDWC evaluation"
- Measurement: Gupta (2022) + CAICT (2024) frame "no integrated provincial CPC"

---

## Note-Making Priority

Create individual paper-summary notes in this order before starting section drafting.

**Before drafting §2 (literature review):**
1. Zhang, Li & Wang (2025) — closest prior EDWC work; defines the gap
2. Zhang, Duan et al. (2025) — second EDWC anchor
3. Sun & Abraham (2021) — main estimator
4. Gupta et al. (2022) — CPC accounting-logic anchor
5. Masanet et al. (2020) — baseline DC energy anchor
6. Zheng, Chien & Suh (2020) — migration mechanism anchor
7. Goodman-Bacon (2021) — TWFE decomposition
8. CAICT (2024) — China institutional context for CPC

**Before drafting §3 (empirical strategy / CPC):**
9. Shan et al. (2016) — CI methodology
10. Dongarra & Luszczek (2026) — HPL-MxP bridge
11. Deryugina et al. (2020) — table/figure structure precedent for electricity DiD
12. Guo et al. (2020) — power market reform context

**Remaining papers:** create notes as needed during section drafting.

---

## Deferred Items

| Item | Why deferred | When to revisit |
|---|---|---|
| NDRC 2021 computing-hub implementation plan (发改高技〔2021〕709号) | Treatment-timing document; wait until electricity data complete and DiD implementation begins | Model implementation stage |
| 2021–2022 official hub-node approval letters | Same: treatment-timing documents | Model implementation stage |
| Empirical PUE variation paper (China/climate focus) | Not blocking; query: `"power usage effectiveness" PUE empirical seasonal climate data center 2018..2025` | Only if §3.4.3 PUE assumptions feel thin |
| Second China-infrastructure DiD paper | Not blocking; query: `("high-speed rail" OR "broadband" OR "pilot free trade zone") China "difference-in-differences" 2018..2025` | Only if §2.2 feels thin |
| Province-year operational data (2022–2025) | Conceptual coverage sufficient; operational statistics for estimation stage | Model implementation |
| Roth (2022) on pre-trend test interpretation | Useful only if §3.4 discussion goes deep on diagnostics | Only if methods write-up warrants it |

---

## Next Step

Download all papers. Set up Zotero collections by stream (`outcome`, `design`, `measurement`, `china-context`). Create the first 12 summary notes in the priority order above. Then begin drafting §2.4 (gap statement) to test whether the architecture holds before writing the full literature review.
