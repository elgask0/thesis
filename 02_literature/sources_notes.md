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
- **Description:** Daily CO₂ emissions by country, sector, and province
- **URL:** https://carbonmonitor.org
- **China-specific:**
  - Cui et al. — Daily CO₂ for China's provinces (2019–2020)
  - Provincial disaggregation methodology
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

#### State Council (2024-07-24) — China sets green targets for data centers
- **Policy:** PUE < 1.5 by 2025 for new data centers
- **Description:** National energy efficiency targets for data center infrastructure
- **Usage:** PUE trajectory assumptions for CPC construction

#### MIIT / NDRC / NEA — Action plans for green data centers
- **Documents:**
  - Action Plan for Carbon Peaking in Data Center Sector (2021–2025)
  - Green Data Center Assessment Guidelines
- **Key content:** PUE targets, renewable energy requirements, efficiency standards

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
