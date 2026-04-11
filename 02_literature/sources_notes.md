# Literature and Sources

Master's thesis literature and reference materials for EDWC research.

---

## Core Papers

### EDWC and Data Centers

#### Zhang et al. (2025) — Decarbonizing data centers through regional bits migration
- **Journal:** Applied Energy
- **File:** `pdf/The 'Eastern Data and Western Computing" Initiative in China Contributes to Its Net-Zero Target.pdf`
- **Key findings:**
  - EDWC reduces data center emissions by **16-20%** through regional workload migration
  - Quantifies carbon savings from shifting compute to western provinces
  - Provides baseline estimates for our counterfactual analysis
- **Relevance:** Validates EDWC emissions impact; supports RQ1 identification

#### Additional EDWC Literature
- [ ] NDRC (2022-02-17) — 东数西算工程正式全面启动
- [ ] Policy analysis papers on EDWC implementation and regional effects
- [ ] Data center energy demand studies in Chinese context

---

### Carbon Monitor China

#### Liu et al. (2020) — Carbon Monitor: Real-time global CO₂ emissions
- **Journal:** Scientific Data
- **Paper:** https://www.nature.com/articles/s41597-020-00708-7
- **Method PDF:** https://carbonmonitor.org.cn/uploads/2006/CarbonMonitor_method.pdf
- **Data portal:** https://cn.carbonmonitor.org/
- **China-specific:**
  - Cui et al. — Daily CO₂ for China's provinces (2019–2020)
    - Preprint: https://essd.copernicus.org/preprints/essd-2021-153/
    - Zenodo: https://zenodo.org/records/4730168
  - Provincial disaggregation methodology
- **Consolidated 2019–2025 dataset (31 provinces):**
  - Figshare: https://figshare.com/articles/dataset/CarbonMonitor-China_a_near-real-time_CO_sub_2_sub_emission_dataset_for_31_provinces_in_China_2019-2025/29444291
- **Usage:** Primary outcome variable for RQ1

---

### Empirical Methods

#### Sun & Abraham (2021) — Dynamic treatment effects in event studies
- **Journal:** Journal of Econometrics
- **Contribution:** Cohort-based estimator for staggered adoption with heterogeneous effects
- **Key insight:** Avoids TWFE negative-weight bias
- **Usage:** Main identification strategy for RQ1

#### Abadie et al. (2010, 2015) — Synthetic Control Methods
- **2010:** *Synthetic Control Method for Comparative Case Studies* (JASA)
- **2015:** *Comparative Case Studies: Synthetic Control Method* (in *High-Dimensional Econometrics*)
- **Contribution:** Data-driven counterfactual construction for single-treated units
- **Usage:** Complementary method for Gansu (primary SCM case)

#### Additional Methodology Papers
- [ ] Callaway & Sant'Anna (2021) — Difference-in-differences with multiple time periods
- [ ] Goodman-Bacon (2021) — Difference-in-differences with variation in treatment timing
- [ ] Event-study robustness and placebo tests

---

## Policy Sources

### EDWC Policy Documents

#### NDRC (2022-02-17) — 东数西算工程正式全面启动
- **Publisher:** National Development and Reform Commission
- **Description:** Official launch of EDWC national program
- **Key content:** 8 node clusters, implementation timeline, policy goals
- **URL:** https://www.ndrc.gov.cn (search 东数西算)

#### NDRC (2022-02-17) — 东数西算三问
- **Publisher:** National Development and Reform Commission
- **Description:** Q&A on EDWC rationale, design, and expected outcomes
- **Key content:** Why EDWC, how it works, what it achieves

#### Additional Policy Sources
- [ ] Implementation plans for each EDWC node (Gansu, Ningxia, etc.)
- [ ] Provincial government EDWC integration plans
- [ ] Data center industry policy documents

---

### PUE and Green Data Centers

#### CAICT (2024) — China Green Computing Power Development Research Report
- **Publisher:** 中国信息通信研究院 (CAICT)
- **Key data:** National DC PUE 1.54 (2022), 1.48 (2023)
- **PDF:** https://www.caict.ac.cn/kxyj/qwfb/ztbg/202407/P020240711551514828756.pdf

#### Xinhua (2024-06) — China's Computing Power Industry Shows New Trend of Green Transition
- **Publisher:** 新华社 (Xinhua News)
- **Key data:** Confirms PUE 2023 = 1.48, 2022 = 1.54
- **URL:** https://www.news.cn/20240629/3e439c6edbe241178335732da8d0e87d/c.html

#### MIIT + 6 ministries (2022) — Action Plan for Green and Low-Carbon Development of ICT Industry (2022–2025)
- **Policy:** New large DCs PUE < 1.3; renovated core rooms PUE < 1.5
- **PDF:** https://www.mee.gov.cn/xxgk2018/xxgk/xxgk10/202208/W020220831368118636346.pdf
- **Gov.cn:** https://www.gov.cn/zhengce/2022-08/26/content_5706915.htm

#### NDRC / MIIT / NEA / NDA — Special Action Plan for Green DC Development
- **Policy:** National avg PUE < 1.5 by 2025; rack rate ≥ 60%; renewables ≥ 10% annual growth
- **PDF:** https://www.ndrc.gov.cn/xwdt/tzgg/202407/P020240723625616053849.pdf
- **Interpretation:** https://home.wuhan.gov.cn/zcfg/202408/t20240808_2439562.shtml

#### NDA + NEA (2025) — Computing Power and Electricity Synergy
- **Key data:** EDWC hub clusters avg PUE ≈ 1.3, best practice 1.04
- **NDA:** https://www.nda.gov.cn/sjj/swdt/sjdt/0318/20250318212051776584737_pc.html
- **People's Daily:** https://finance.people.com.cn/n1/2025/0319/c1004-40442025.html

#### ODCC — Data Center Green Design White Paper
- **Key data:** Design PUE ~1.32 (construction), ~1.28–1.29 (hyperscale), target ≤ 1.25
- **Download:** https://www.odcc.org.cn/download/p-1673994360961089537.html

#### RMI China (2024) — Decoupling Computing Power Growth and Carbon Emissions
- **Key data:** Confirms PUE 2023 = 1.48; tightened targets PUE ≤ 1.25 (new DCs), ≤ 1.2 (EDWC hubs)
- **PDF:** https://rmi.org.cn/wp-content/uploads/2024/11/241119-%E8%A7%A3%E8%80%A6%E7%AE%97%E5%8A%9B%E5%8F%91%E5%B1%95%E4%B8%8E%E7%A2%B3%E6%8E%92%E6%94%BE-%E2%80%93-%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E7%94%A8%E8%83%BD%E5%A2%9E%E9%95%BF%E7%9A%84%E6%8C%91%E6%88%98%E4%B8%8E%E8%A7%A3%E5%86%B3%E8%B7%AF%E5%BE%84.pdf

#### Greenpeace East Asia (2024) — Clean Cloud 2024
- **Key content:** Cloud/DC operator rankings, renewables use, PUE target recap
- **PDF:** https://www.greenpeace.org.cn/wp-content/uploads/2024/07/Clean-Cloud-2024.pdf

---

## Technical References

### Compute Efficiency

#### Green500 — Top500 Supercomputing Energy Efficiency
- **Description:** Ranking of supercomputers by FP64 efficiency (GFLOPS/W)
- **URL:** https://www.top500.org/green500/
- **Usage:** FP64 frontier for GF/W construction
- **Frequency:** Biannual rankings (June, November)

#### HPL-MxP — Mixed-Precision AI Benchmark
- **Description:** HPL (High-Performance LINPACK) adapted for mixed-precision AI workloads
- **Contribution:** Speedup factors for FP16/FP32 vs. FP64
- **Usage:** Bridge from FP64 to AI-equivalent efficiency
- **Assumption:** Throughput speedup ⇒ efficiency improvement (NVIDIA tensor-core note)

#### MLPerf Power — Inference Energy Metrics
- **Description:** Standardized benchmarks for AI inference energy consumption
- **URL:** https://mlcommons.org/en/benchmarks/power/
- **Usage:** Alternative validation for GF/W assumptions

---

### Hardware Specifications

#### NVIDIA A800 vs A100 Interconnect
- **A100:** NVLink bandwidth = 600 GB/s
- **A800:** NVLink bandwidth = 400 GB/s (China export variant)
- **Ratio:** β = 400/600 = 0.667
- **Usage:** China interconnect haircut in GF/W construction

#### Additional Hardware
- [ ] H800/A800 cluster specifications in Chinese data centers
- [ ] Utilization benchmarks from Chinese cloud providers (Alibaba, Tencent)

---

## CAICT (China Academy of Information and Communications Technology)

### China Green Computing Power Development Research Report (2024)
- **Publisher:** CAICT
- **Description:** Annual report on computing power and green development
- **Key content:**
  - Provincial compute index (综合算力指数)
  - Green computing metrics
  - Data center efficiency trends
- **Usage:** Province tiers (Elite/Q4/Q3/Q2/Q1) for donor pool construction

### 综合算力指数 (Provincial Compute Index)
- **Description:** Cross-sectional ranking of provinces by computing capacity
- **Tiers:**
  - **Elite:** Beijing, Shanghai, Guangdong, Zhejiang, Jiangsu
  - **Q4:** Shandong, Sichuan, etc.
  - **Q1:** Gansu, Ningxia, etc. (potential EDWC destinations)
- **Usage:** Heterogeneity analysis; SCM donor pool selection

---

## To Add

### Event-Study Methodology Papers
- [ ] Additional recent DiD/event-study papers (2020–2025)
- [ ] Placebo test and robustness methods

### Data Center Energy Demand Literature
- [ ] Global data center energy consumption forecasts
- [ ] China-specific data center energy studies
- [ ] Renewable energy integration in data centers

### China Power System and Renewable Integration
- [ ] Curtailment studies (provincial and national)
- [ ] Renewable capacity expansion and utilization
- [ ] Grid flexibility and demand response

### AI Energy Consumption Studies
- [ ] Large language model training energy costs
- [ ] Data center AI workload characterization
- [ ] Trends in AI compute efficiency

---

## File Organization

```
02_literature/
├── sources_notes.md          # This file — literature catalog
├── pdf/                      # PDF files of papers and reports
│   ├── The_Eastern_Data_and_Western_Computing_Initiative_in_China_Contributes_to_Its_Net-Zero_Target.pdf
│   └── ... (additional PDFs)
└── zotero/                   # Auto-synced from Zotero (if using)
```

---

## Last Updated

2026-02-19
