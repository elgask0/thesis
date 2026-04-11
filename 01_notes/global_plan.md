# Thesis Plan — EDWC, Energy, and Carbon-per-Compute (CPC)

---

## 0. Central Idea (one-liner)

The thesis studies how China’s **Eastern Data, Western Compute (EDWC)** program affects provincial electricity consumption and CO₂ emissions (an upstream AI-adoption shock) and translates these effects into AI-native units of compute by building a **Carbon-per-Compute (CPC)** index that combines:

- Grid carbon intensity (CI), in $[\text{tCO₂/MWh}]$.  
- Site efficiency (PUE).  
- A reproducible AI-equivalent efficiency series (GFLOPS/W) for China, constructed from Green500 + HPL-MxP + utilization and interconnect adjustments (A800/H800).

The key step is that the DiD/event-study delivers reduced-form EDWC-induced changes in energy and emissions, and you use these deltas to construct **compatible compute scenarios** (in EF·h) under different assumptions about:

- What fraction of the extra MWh truly comes from data centers.  
- How CI would have evolved without EDWC (counterfactual mix).

---

## 0b. Dropped Idea: Curtailment-Welfare RQ

**Original proposal (dropped):** Estimate social welfare from reduced renewable curtailment due to EDWC-driven data center demand. Mechanism: datacenters shift flexible workloads to off-peak hours where curtailment occurs → less curtailed energy.

**Why dropped:** No intraday provincial load/price curves available. Without hourly data, cannot credibly attribute curtailment reduction to datacenter behavior or show price sensitivity. The curtailment-based welfare RQ is not defensible with current data.

**What can still be kept descriptively:** Monthly renewable utilization tables from the National New Energy Consumption Monitoring and Early Warning Center can still be used as mechanism context or an appendix. For example, a June 4, 2024 repost of the April 2024 table shows Gansu at 94.1% wind utilization and 88.7% solar utilization, versus Ningxia at 99.0% and 97.3%, and Guizhou at 99.4% and 98.8%. This is useful for descriptive renewable-integration context, but not for causal welfare claims. Provincial time-of-use tariff reforms can also be stored as institutional background on intraday incentives, but without hourly load data they cannot identify actual within-day reshaping of electricity demand.

---

## 1. Research Questions and Contribution

### RQ1 — Causal (reduced-form EDWC → energy and emissions)

**RQ1.** What is the causal effect of EDWC cluster go-lives on CO₂ emissions and, where data permit, on electricity consumption in destination provinces?

- **Baseline treated provinces:** Ningxia, Guizhou, Gansu, Inner Mongolia.  

- **Outcomes:**  
  - **Primary:** Daily provincial CO₂ (2019–2025), aggregated to monthly for the main model.  
  - **Secondary:** Monthly provincial electricity (kWh/MWh) where coverage is sufficient (Gansu, Henan, etc.).

For each treated province $p$, the design identifies a **reduced-form** effect of the EDWC *package* (data centers + grid reinforcement + associated renewables, etc.):

- $\Delta \text{MWh}^{\text{EDWC}}_{p,t}$: causal change in monthly electricity consumption.  
- $\Delta \text{CO₂}^{\text{EDWC}}_{p,t}$: causal change in monthly CO₂ emissions.

You do **not** assume that changes in CI come solely from data centers: EDWC is bundled with mix and renewables policies.

---

### RQ2 — Compute metric and CPC (scenarios, not a single number)

**RQ2.** Given each province’s energy environment (CI, PUE, compute efficiency GF/W), what are the levels and changes of **Carbon-per-Compute** (CPC) — tCO₂ per exaflop-hour (tCO₂/EF·h) — before and after EDWC, and what range of compute (EF·h) is compatible with the estimated $\Delta \text{MWh}$ and $\Delta \text{CO₂}$?

**CPC definition:**

$$
\text{CPC}_{p,t}
= \text{CI}_{p,t} \times \text{PUE}_{p,t} \times \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)}
\quad [\text{tCO₂/EF·h}]
$$

CPC is an **intensive** metric (tCO₂ per EF·h) that depends on:

- Observed CI (which reflects both load and mix changes).  
- The trajectory of $\text{PUE}_{p,t}$.  
- The national series $\text{GF/W}_{\text{AI,China}}(t)$.

Starting from the causal RQ1 results $(\Delta \text{MWh}, \Delta \text{CO₂})$, you use three complementary views:

1. **Energy-based compute (robust to CI):**  
   - Assume a fraction $\theta$ of EDWC extra MWh is due to data centers, and translate those MWh into EF·h using PUE and GF/W.

2. **Emissions-compatible compute (via CPC):**  
   - “How much additional compute would be consistent with the net observed $\Delta \text{CO₂}$, given CPC?”  
   - Plus a “gross” variant using $\text{CI}_{\text{pre}}$ (as if the mix had not changed).

3. **Emissions offset index (volume vs mix):**  
   - Compare the “volume” CO₂ that would arise if CI did not change with the net observed CO₂.  
   - This measures how much of the potential emissions from higher load is offset by renewables/mix.

---

### Extension — Economic outcomes (program-fit mitigation)

Relate scenario-based $\Delta \text{EF·h}$ to provincial economic variables as a **mitigation for program-fit concerns** (ensuring the thesis is grounded in Chinese economics, not only energy/technology):

- Provincial fixed investment (infrastructure, power sector, ICT).
- Employment in ICT/software/data center sectors.
- Positions in CAICT compute indices.

> **Status:** This is an exploratory extension, not a core research question. It supports the thesis positioning as a Chinese economics study and may become a discussion section or appendix.

---

### Contributions

1. **Upstream AI → energy causality**  
   - Estimate EDWC → CO₂/kWh effects via:
     - Staggered adoption event-study (Sun–Abraham).  
     - Synthetic Control (SCM) for Gansu as an optional/supplementary check.
   - Clearly interpreted as **reduced-form effects** on energy and emissions, not on “pure CI”.

2. **AI-native physical accounting (CPC)**  
   - Build a reproducible energy ↔ compute bridge using:
     - Observed provincial CI,  
     - $\text{PUE}_{p,t}$ consistent with MIIT/NDRC/NEA targets,  
     - $\text{GF/W}_{\text{AI,China}}(t)$ constructed from Green500 + HPL-MxP + MFU + a China haircut (A800/H800).

3. **Applied product**  
   - Monthly CPC series by province–month + $\Delta \text{CPC}$ post-EDWC.  
   - EDWC scorecards by province: $\Delta \text{CO₂}$, $\Delta \text{GWh}$, $\Delta \text{CPC}$, $\Delta \text{EF·h}$ (scenarios).  
   - Stress-test modules (e.g., “impact of +X EF·h in Gansu” under different CPC assumptions).

---

## 2. Key Institutional Background

### 2.1. EDWC

- Officially launched in February 2022 (NDRC): 8 national hubs, 10 clusters.  
- Objective: redirect data workloads from the east toward compute capacity in the west, leveraging:
  - Cheaper land,  
  - Data center–friendly climate,  
  - Higher availability of renewables (wind, solar, hydro).  
- Key western provinces: Ningxia, Gansu, Inner Mongolia, Guizhou, plus the Sichuan–Chongqing pair.

### 2.2. Compute and energy

- AI adoption implies GPU farms that create **intensive compute demand**:
  - Near-baseload load,  
  - Some temporal flexibility (shiftable workloads).  
- EDWC overlaps with:
  - Massive expansion of solar/wind capacity,  
  - Targets for decreasing PUE and increasing renewable use in data centers,  
  - Political pressure around “computing power” as a competitiveness factor.

### 2.3. CAICT compute indices

- CAICT’s 综合算力 / computing power reports classify provinces/cities into tiers (Q1–Q4, Elite).  
- The thesis uses these indices to:
  - Define compute tiers and heterogeneity (Q1–Q4).  
  - Select donors for SCM (provinces with similar infrastructure but without EDWC).
- For clean 2022→2023 comparison, the most usable pair is the 4D 综合算力 evaluation across its 2022 and 2023 reference editions.
- The broader 2023 算力发展指数 is still useful cross-sectionally because it adds ecosystem signals such as software revenue, R&D, connectivity, and industrial digitalization, but it should not be treated as a naive year-to-year continuation of the 4D framework.

---

## 3. EDWC Treatment: $T_0$ Dates and Official Evidence

Treatment is defined by **operational go-live dates** from official portals, prioritizing milestones such as “投运/上线/试运行/put into use” tied to:

- Compute trading/dispatch platforms (算力 platforms that enable load flows).  
- Data center clusters built and put into operation with significant capacity (P).

### 3.1. Operational $T_0$ Dates (Baseline + Robustness)

**Ningxia (NX)**

- Baseline $T_0$: 2023-02-24.
- Asset: 东数西算一体化算力服务平台 (Eastern Data Western Compute Integrated Computing Power Service Platform).
- Evidence:
  - Ningxia News Network reports the platform was “正式发布上线”.
  - CCTV reports the platform “上线运营”.
  - Zhongwei Government later reports China Telecom Ningxia DC Phase I fully built and accepted in July 2023.
- Interpretation:
  - Main $T_0$: 2023-02-24 (network/platform go-live).
  - Alternative $T_0$ (robustness): 2023-07 (physical capacity milestone for China Telecom Ningxia DC Phase I).

**Guizhou (GZ)**

- Baseline $T_0$: 2023-09.
- Relevant assets:
  - 国家电投贵安数据中心 (SPIC Gui’an DC): reported in use from September 2023.
  - 网易贵安数据中心 (NetEase Gui’an DC): planned trial operation by end-September 2023.
- Interpretation:
  - Main $T_0$: 2023-09 (first official put-into-use / trial-operation window in Gui’an).
  - Alternative $T_0$ (robustness): 2024-06 (completed migration from Beijing).

**Gansu (GS)**  

- Baseline $T_0$: 2024-06.  
- Asset: National computing hub (Gansu·Qingyang node) and Qingyang data center cluster (全国算力枢纽（甘肃·庆阳）节点, 庆阳数据中心集群).  
- Evidence:
  - Gansu portal: hub and cluster “建成投运标准机架1.5万个，算力规模达到1.2万P” and surpass 10,000 P in June 2024.  
  - Updates:
    - 2024-12: >21,000 racks built and operating.  
    - 2025-01: ≈31,000 racks and ≈50,000 P of compute.  
- Interpretation:
  - $T_0 =$ June 2024, when the cluster reaches significant operational scale (≥10k P).  
  - The post period includes further expansion (Dec 2024, Jan 2025).

**Inner Mongolia (IM)**

- Baseline $T_0$: 2024-09.
- Asset: 九州智算中心 (Jiuzhou Intelligent Computing Center) in the Horinger New Area.
- Evidence:
  - Xinhua reports the center “今年9月底建成投运” with deployable capacity of about 20,000 P.
  - A later Xinhua report states Inner Mongolia put the Horinger multi-cloud monitoring and dispatch platform into operation in May 2025.
- Interpretation:
  - Main $T_0$: 2024-09 (large physical computing node goes into operation).
  - Alternative $T_0$ (robustness): 2025-05 (cluster-level platform and cross-hub dispatch capability).

**Note on Sichuan**

- Sichuan experiences a severe hydro-thermal shock in 2022 with electricity rationing.  
- It is excluded from the **baseline treated set** and used carefully as donor/robustness province in SCM and DiD (specific dummies and exclusions).

---

## 4. Data

### 4.1. CO₂ Emissions: Carbon Monitor–China

**Primary source:** Carbon Monitor–China, which provides daily CO₂ emissions by province and sector (2019–2025).

- General methodology:
  - Z. Liu et al. (2020), *Carbon Monitor: a near-real-time daily dataset of global CO₂ emissions*, Scientific Data.
    - Paper: https://www.nature.com/articles/s41597-020-00708-7
    - Method PDF: https://carbonmonitor.org.cn/uploads/2006/CarbonMonitor_method.pdf
- Extension to Chinese provinces:
  - C. Cui et al., *Daily CO₂ emissions for China’s provinces in 2019–2020*, ESSD (preprint) + Zenodo dataset.
    - Preprint: https://essd.copernicus.org/preprints/essd-2021-153/
    - Zenodo 2019–2020: https://zenodo.org/records/4730168
- Consolidated dataset:
  - *CarbonMonitor–China: a near-real-time CO₂ emission dataset for 31 provinces in China 2019–2025* (Figshare).
    - Dataset: https://figshare.com/articles/dataset/CarbonMonitor-China_a_near-real-time_CO_sub_2_sub_emission_dataset_for_31_provinces_in_China_2019-2025/29444291
- Data portal: https://cn.carbonmonitor.org/

**Construction of the monthly series in the thesis:**

1. Download daily provincial series from Carbon Monitor–China.  
2. For each province $p$ and calendar month $t$, define:

   $$
   \text{CO₂}_{p,t}
   = \sum_{d \in t} \text{CO₂}_{p,d}
   $$

   (simple sum over days in the month, no additional rescaling).

3. For electric CI (when using CO₂/MWh directly), the “minimal” option is:

   $$
   \text{CI}^{(\text{CM})}_{p,t} = \frac{\text{CO₂}_{p,t}}{\text{MWh}_{p,t}}
   $$

   using monthly total CO₂ and monthly total MWh (see 4.2).

4. For sectoral analyses, you can repeat the aggregation using only the “power” sector.

---

### 4.2. Monthly Electricity (kWh/MWh)

- **Sources:** official bulletins (NEA, development commissions, provincial statistics).  
- **Examples:** Jiangsu, Gansu, Shanxi, Henan, Hubei, Qinghai…

**Issues:**

- Some bulletins report only cumulative YTD (累计) and year-on-year % growth.  
- Others explicitly report “当月” (this month).  
- Heterogeneous formats and missing months.

**Use in the thesis:**

- Secondary outcome for RQ1 wherever 2022–2025 coverage is dense enough.  
- Input for physical consistency checks:

  $$
  \Delta \text{MWh}^{(\text{from CO₂})}_{p,t}
  = \frac{\Delta \text{CO₂}_{p,t}}{\text{CI}_{p,t}}
  \quad\text{vs.}\quad
  \Delta \text{kWh}^{\text{observed}}_{p,t}
  $$

**Construction pipeline:**

1. For each province, locate the index page for electricity/energy operation bulletins  
   (e.g. “电力运行情况”, “能源生产运行情况”, etc.).  
2. Web-scrape monthly bulletin links (title, URL, date).  
3. Download HTML/PDF and clean the text (remove HTML, menus, etc.).  
4. Send the clean text to a generative model (e.g. DeepSeek) with a strict prompt that returns **only JSON**:

   ```json
   {
     "province": "...",
     "year": 2024,
     "month": 8,
     "total_kwh_this_month": ...,
     "industrial_kwh_this_month": ...,
     "units": "10^8 kWh"
   }
   ```

5. Assemble all rows into a national province–month panel and standardize units to MWh.

**Acceptance rule:** a province enters the kWh sample if it has ≥ 80% monthly coverage in the key period (e.g. 2022–2025).

---

### 4.3. Carbon Intensity $\text{CI}_{p,t}$

You have two complementary ways to construct CI:

1. **“Minimal” CI** from total CO₂ and total MWh:

   $$
   \text{CI}^{(\text{CM})}_{p,t} = \frac{\text{CO₂}_{p,t}}{\text{MWh}_{p,t}}
   $$

   - Total CO₂ from Carbon Monitor + total MWh from the electricity panel.  
   - This CI enters directly into CPC to preserve DiD ↔ CPC consistency.

2. **CI from power mix + emission factors (for checks/scenarios):**

   - Use monthly electricity mix (shares of coal, gas, hydro, wind, solar, nuclear, etc.).  
   - Standard emission factors:
     - Coal $\approx 0.95 \text{ t/MWh}$, gas $\approx 0.40 \text{ t/MWh}$, renewables $\approx 0$.  
   - Sources: NBS/CEC, Ember, CREA, your compiled tables.

Uses of the second construction:

- Build counterfactual CI (e.g., “CI if the mix had followed the historical trajectory”).  
- Analyze volume vs mix decomposition (see section 5.3).

---

### 4.4. PUE: Observed Levels and 2022–2025 Targets

**National average PUE data:**

- CAICT – *China Green Computing Power Development Research Report (2024)*:
  - National data center PUE: 1.54 (2022), 1.48 (2023).
  - PDF: https://www.caict.ac.cn/kxyj/qwfb/ztbg/202407/P020240711551514828756.pdf
- Xinhua recap (*China’s Computing Power Industry Shows New Trend of Green Transition*):
  - Confirms PUE 2023 = 1.48, 2022 = 1.54.
  - Article: https://www.news.cn/20240629/3e439c6edbe241178335732da8d0e87d/c.html

**Official PUE policies (MIIT, NDRC, NEA, National Data Administration):**

- *Action Plan for Green and Low-Carbon Development of the Information and Communications Industry (2022–2025)* (MIIT + 6 ministries):
  - New large and ultra-large DCs: PUE < 1.3.
  - Renovated core rooms: PUE < 1.5.
  - PDF: https://www.mee.gov.cn/xxgk2018/xxgk/xxgk10/202208/W020220831368118636346.pdf
  - Gov.cn interpretation: https://www.gov.cn/zhengce/2022-08/26/content_5706915.htm

- *Special Action Plan for Green and Low-Carbon Development of Data Centers* (NDRC, MIIT, NEA, National Data Administration):
  - 2025 targets:
    - National average PUE for all DCs: < 1.5.
    - Rack rate ≥ 60%.
    - Renewable utilization: ≥ 10% average annual growth.
  - PDF: https://www.ndrc.gov.cn/xwdt/tzgg/202407/P020240723625616053849.pdf
  - Interpretation: https://home.wuhan.gov.cn/zcfg/202408/t20240808_2439562.shtml

- Joint note (National Data Administration + NEA, 2025) — *Systematically Promoting Synergy between Computing Power and Electricity*:
  - In the eight EDWC hubs, clusters have average PUE ≈ 1.3, with best-practice cases at 1.04.
  - NDA: https://www.nda.gov.cn/sjj/swdt/sjdt/0318/20250318212051776584737_pc.html
  - People’s Daily reprint: https://finance.people.com.cn/n1/2025/0319/c1004-40442025.html

**Other sources:**

- ODCC – *Data Center Green Design White Paper*:
  - Design PUE for projects under construction ~1.32; hyperscale ~1.28–1.29; target PUE ≤ 1.25.
  - Download: https://www.odcc.org.cn/download/p-1673994360961089537.html

- RMI – *Decoupling Computing Power Growth and Carbon Emissions – Data Center Energy Use*:
  - Confirms PUE 2023 = 1.48 (CAICT).
  - Tightened targets: new/expanded large DCs PUE ≤ 1.25, EDWC hubs PUE ≤ 1.2.
  - PDF: https://rmi.org.cn/wp-content/uploads/2024/11/241119-%E8%A7%A3%E8%80%A6%E7%AE%97%E5%8A%9B%E5%8F%91%E5%B1%95%E4%B8%8E%E7%A2%B3%E6%8E%92%E6%94%BE-%E2%80%93-%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E7%94%A8%E8%83%BD%E5%A2%9E%E9%95%BF%E7%9A%84%E6%8C%91%E6%88%98%E4%B8%8E%E8%A7%A3%E5%86%B3%E8%B7%AF%E5%BE%84.pdf

- Greenpeace East Asia – *Clean Cloud 2024*:
  - Rankings of cloud/DC operators; renewables use; recap of PUE targets.
  - PDF: https://www.greenpeace.org.cn/wp-content/uploads/2024/07/Clean-Cloud-2024.pdf

**Interpretation in the thesis (trajectories $\text{PUE}_{p,t}$):**

- Model $\text{PUE}_{p,t}$ as a monthly trajectory that:
  - Starts around 1.54 (2022) and 1.48 (2023) at the national level.  
  - Converges toward ~1.5 national average by 2025.  
- For EDWC hubs/treated provinces, trajectories converge toward ~1.3 (or even 1.2 in optimistic scenarios).  
- Adjustments:
  - EDWC provinces (Ningxia, Gansu, IM, Guizhou) have more aggressive paths (PUE → 1.3).  
  - Cluster PUE in hubs can approach 1.2–1.3 by 2025; use ±0.1–0.2 bands for uncertainty.

---

### 4.5. $\text{GF/W}_{\text{AI,China}}(t)$ Series (AI-equivalent Efficiency)

Built from:

1. **Green500 FP64:**
   - Take the frontier GF/W per edition (options: median of top-10 systems, or Q4 / P75 of all systems; sensitivity test both).
   - Use step-hold between June/November releases to obtain the baseline monthly series; keep linear interpolation only as a sensitivity check.

2. **HPL-MxP speedup (MxP/FP64):**
   - Speedup factor from FP64 to mixed-precision AI-like workloads.  
   - Based on HPL-MxP / HPL-AI; assumed to translate into higher effective GF/W for AI workloads.

3. **MFU realism (effective utilization):**
   - Global factor $\kappa_{\text{global}} \in [0.4, 0.6]$ (center 0.5) to reflect that clusters do not operate at 100% peak efficiency.

4. **China interconnect haircut:**
   - NVLink A800/H800 (400 GB/s) vs A100/H100 (600–900 GB/s).  
   - Define $\beta(t) \approx 0.667$ (A800 era) and $\beta(t) \approx 0.444$ (H800 era).  
   - China efficiency:

     $$
     \kappa_{\text{China}}(t)
     = 1 - \lambda \,[1 - \beta(t)]
     $$

     with $\lambda \approx 0.4$ (share of comm-bound workloads).

5. **Qualitative validation:**
   - Compare normalized trend with MLPerf Inference Power metrics (tokens/s per watt) from 2023 onward.

From here you obtain:

$$
\text{GF/W}_{\text{AI,global}}(t)
= \overline{\text{GF/W}}_{\text{FP64}}(t)\cdot s_{\text{mxp}}(t)\cdot \kappa_{\text{global}},
$$

$$
\text{GF/W}_{\text{AI,China}}(t)
= \text{GF/W}_{\text{AI,global}}(t)\cdot \kappa_{\text{China}}(t).
$$

---

## 5. Empirical Strategy (RQ1)

### 5.1. Sun–Abraham Event-Study (Staggered Adoption)

**Panel:**

- Province–day (CO₂) for fine-grained shock exploration.  
- Province–month (aggregated CO₂ and kWh) for the main model.

**Conceptual monthly model:**

$$
Y_{p,t}
= \alpha_p + \delta_t
+ \sum_{\ell\in \mathcal{L},\,\ell\neq -1} \beta_{\ell}\,\mathbf{1}\{t - E_p = \ell\}
+ X_{p,t}'\gamma + \varepsilon_{p,t}
$$

- $Y_{p,t}$: monthly CO₂ (primary) or monthly kWh (secondary).  
- $E_p$: month of $T_0$ (see treatment table).  
- $\ell = t - E_p$: event time (in months; tails are binned).  
- $\alpha_p$: province fixed effects; $\delta_t$: month fixed effects (national shocks).  
- $X_{p,t}$: CDD/HDD, precipitation, holidays, and optionally dummies for Sichuan-type shocks in 2022.  
- Estimator: **Sun–Abraham** (group-time ATT with staggered adoption, avoiding negative weights from TWFE).

**Checks:**

- Pre-trends: $\beta_\ell \approx 0$ for $\ell < 0$ (joint test).  
- Tails: $\ell \le -12$ and $\ell \ge +18$ grouped.  
- Standard errors clustered by province; wild bootstrap as robustness.

---

### 5.2. SCM for Gansu (optional / supplementary)

> **Status:** SCM is a supplementary robustness exercise. The main identification comes from the Sun–Abraham event-study (5.1). SCM is run if time and data permit.

- Treated unit: **Gansu**.
- Pre period: 2019-01 to 2024-05.
- Post period: from 2024-06 (Gansu $T_0$).

**Donors:**

- Q1–Q2 provinces without EDWC (Guangxi, Hainan, Yunnan, Qinghai, etc.),  
- Excluding provinces with extreme shocks (Sichuan 2022) or overlapping EDWC $T_0$.

**Predictors:**

- Pre-treatment means and trends of CO₂.  
- Pre-treatment means/trends of kWh (where available).  
- CDD/HDD, pre-EDWC CI, proxies for economic activity.

**Inference:**

- In-space placebos (each donor treated as if in 2024-06).  
- Compare pre/post RMSPE; Abadie-style p-values.  
- Robustness: leave-one-out; ridge-SCM variant if donor weights are unstable.

---

### 5.3. What DiD Identifies (and What It Does Not): Volume vs Mix

From the RQ1 model you obtain:

- $\Delta \text{MWh}^{\text{EDWC}}_{p,t}$ and  
- $\Delta \text{CO₂}^{\text{EDWC}}_{p,t}$  

(the ATT at each event time $\ell$).

CI is defined as:

$$
\text{CI}_{p,t}
= \frac{\text{CO₂}_{p,t}}{\text{MWh}_{p,t}}
$$

and can change due to:

- Increases/decreases in load (MWh).  
- Changes in generation mix (more renewables, less coal).  
- Other energy policies (electricity market, dispatch rules, etc.).

DiD does **not** identify a “pure” EDWC effect on CI. But you can implement an approximate **accounting decomposition**:

$$
\Delta \text{CO₂}^{\text{EDWC}}_{p,t}
\approx
\underbrace{\text{CI}^{\text{pre}}_{p} \cdot \Delta \text{MWh}^{\text{EDWC}}_{p,t}}_{\text{volume with pre-mix}}
+
\underbrace{\text{MWh}^{\text{pre}}_{p} \cdot \Delta \text{CI}^{\text{EDWC}}_{p,t}}_{\text{mix change with pre-load}}
+ \text{residual}.
$$

This lets you say, for each province:

- “If the mix had not changed (CI$_\text{pre}$ fixed), the extra EDWC MWh would have implied $\Delta \text{CO₂}_\text{volume}$.”  
- Compare that to the net observed $\Delta \text{CO₂}$: if net $\ll$ volume → strong mix/renewables compensation.  
- Extreme case: $\Delta \text{MWh} > 0$ but $\Delta \text{CO₂} < 0$ (CI falls a lot).

Important: always present this as **accounting** (which combination of volume and mix makes the observed $\Delta \text{CO₂}$ consistent), not as causal identification of mix effects.

---

## 6. CPC and Translation to Compute (RQ2)

### 6.1. CPC Definition (Intensive)

For each province $p$ and month $t$:

$$
e^{\text{IT}}_{t}
= \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)} \quad [\text{MWh/EF·h}]
$$

$$
e^{\text{Site}}_{p,t}
= e^{\text{IT}}_{t} \cdot \text{PUE}_{p,t}
$$

$$
\text{CPC}_{p,t}
= \text{CI}_{p,t} \cdot e^{\text{Site}}_{p,t}
= \text{CI}_{p,t} \cdot \text{PUE}_{p,t} \cdot \frac{1000}{\text{GF/W}_{\text{AI,China}}(t)}
\quad [\text{tCO₂/EF·h}]
$$

RQ2 focuses on:

- Levels of $\text{CPC}_{p,t}$.  
- Changes $\Delta \text{CPC}$ pre/post EDWC.  
- Comparisons across provinces (EDWC vs non-EDWC, CAICT tiers).

---

### 6.2. Translating $\Delta \text{MWh}$/$\Delta \text{CO₂}$ into Compute (Scenarios)

#### 6.2.1. View A – Energy-Based Compute (Robust to CI)

Define a parameter $\theta \in [0,1]$:

- Share of additional EDWC MWh that corresponds to data center consumption.

Let $\overline{\Delta \text{MWh}}^{\text{EDWC}}_{p}$ be the average post effect (e.g., months 0–6 after $T_0$):

$$
\Delta \text{EF·h}^{(E)}_{p}(\theta)
= \frac{\theta \cdot \overline{\Delta \text{MWh}}^{\text{EDWC}}_{p}}{e^{\text{Site}}_{p,\text{post}}}.
$$

Interpretation:

- $\theta = 1$ → upper bound: all extra MWh are data center load.  
- $\theta = 0.3–0.5$ → more conservative scenarios.

This approach does **not** depend on how CI changes; it works even if CI drops sharply due to renewables.

---

#### 6.2.2. View B – Emissions-Compatible Compute (via CPC)

(i) **Based on net $\Delta \text{CO₂}$ (with observed CI):**

$$
\Delta \text{EF·h}^{(\text{CO₂,net})}_{p}
= \frac{\overline{\Delta \text{CO₂}}^{\text{EDWC}}_{p}}{\text{CPC}_{p,\text{post}}}.
$$

Interpretation:

- Minimum EF·h of additional compute whose carbon footprint, given $\text{CPC}_{p,\text{post}}$, is consistent with the net $\Delta \text{CO₂}$ identified by DiD.

(ii) **“Gross of mix” (as if CI had not changed):**

First, CO₂ associated with extra MWh if the pre-mix CI had persisted:

$$
\Delta \text{CO₂}^{\text{volume}}_{p}
= \text{CI}^{\text{pre}}_{p} \cdot \overline{\Delta \text{MWh}}^{\text{EDWC}}_{p}.
$$

Then, “gross” compute:

$$
\Delta \text{EF·h}^{(\text{CO₂,gross})}_{p}
= \frac{\Delta \text{CO₂}^{\text{volume}}_{p}}{\text{CPC}_{p,\text{post}}}.
$$

Comparison:

- If $\Delta \text{EF·h}^{(\text{CO₂,gross})} \gg \Delta \text{EF·h}^{(\text{CO₂,net})}$, a large share of the potential emissions from extra load is offset by lower CI (renewables, cleaner mix).

---

#### 6.2.3. View C – Emissions Offset Index

Define:

$$
\text{Offset}_{p}
= 1 - \frac{\overline{\Delta \text{CO₂}}^{\text{EDWC}}_{p}}{\Delta \text{CO₂}^{\text{volume}}_{p}}.
$$

- $\text{Offset} \approx 0$ → almost no compensation via mix.  
- $\text{Offset} \approx 1$ → almost all potential emissions from extra load are offset by lower CI.  
- $\text{Offset} > 1$ → extreme case: load rises but net emissions fall.

This index links energy, mix, and compute and allows statements such as:

> “In Gansu, EDWC increases electricity load but, thanks to renewables, the net CO₂ footprint is much smaller than what the pre-EDWC mix would imply.”

---

### 6.3. Uncertainty (Simple Monte Carlo)

Parameters with uncertainty:

- $s_{\text{mxp}}$, MFU $\kappa_{\text{global}}$,  
- $\lambda$ (share of comm-bound workloads),  
- $\text{PUE}_{p,t}$, $\text{CI}_{p,t}$.

Procedure:

1. Define simple distributions (uniform or triangular) for each parameter.  
2. Simulate many realizations of:
   - $\text{GF/W}_{\text{AI,China}}(t)$, $e^{\text{IT}}$, $e^{\text{Site}}$, $\text{CPC}_{p,t}$.  
3. Report P10–P90 bands for CPC and, if you use $\Delta \text{EF·h}$, for the compute translations too.

Figures and tables show medians + bands instead of single-point estimates.

---

## 7. Manuscript Structure

1. **Introduction**  
   - Motivation (upstream AI → energy).  
   - What EDWC does.  
   - RQ1–RQ2, contributions, and economic extension.

2. **Context and institutions**  
   - EDWC, hubs, clusters.  
   - PUE and renewable policies in data centers.  
   - CAICT compute indices.

3. **Data**  
   - CO₂ (Carbon Monitor–China).  
   - Electricity (provincial bulletins).  
   - CI, PUE, $\text{GF/W}_{\text{AI,China}}(t)$.  
   - $T_0$ dates; CAICT tiers.

4. **Empirical strategy for RQ1**
   - Sun–Abraham event-study.
   - SCM for Gansu (optional / supplementary).
   - Identification discussion (reduced-form nature).

5. **RQ1 results**
   - Plots of $\beta_\ell$ (CO₂, kWh).
   - Gansu SCM — actual vs synthetic paths, placebos (optional, if run).
   - Heterogeneity (by CAICT tier, by province, by offset index).

6. **CPC and compute translation (RQ2)**
   - Construction of GF/W and $\text{PUE}_{p,t}$.
   - $\text{CPC}_{p,t}$ and $\Delta \text{CPC}$.
   - $\Delta \text{EF·h}$ scenarios and emissions offsets.

7. **Robustness and sensitivity**
   - Alternative event windows.
   - Alternative $T_0$ (Guizhou, IM).
   - PUE/GF/W parameters.
   - Exclusion of Sichuan, etc.

8. **Discussion and applications**
   - Implications for energy and digital policy in China.
   - Compute–climate trade-offs; lessons for other countries.
   - Exploratory: relationship to provincial investment and employment (program-fit extension).

9. **Conclusions**
   - Summary of findings.
   - Limitations (especially CI/mix).
   - Future agenda (hourly data, prices, curtailment, if available).

**Appendices:** full formulas, detailed $T_0$ source tables, alternative specifications, Monte Carlo details.

---

## 8. Implementation Pipeline (High Level)

1. Build CO₂ panel (day → month) by province.  
2. Build kWh panel (scraping + generative extraction) and select provinces with good coverage.  
3. Construct $\text{CI}^{(\text{CM})}_{p,t} = \text{CO₂}/\text{MWh}$; optionally CI-from-mix for checks.  
4. Build $\text{PUE}_{p,t}$ trajectories using CAICT/RMI/ODCC targets and levels.  
5. Build $\text{GF/W}_{\text{AI,China}}(t)$ series.  
6. Estimate Sun–Abraham event-study (CO₂ and, where relevant, kWh).  
7. Estimate SCM for Gansu (and optionally for another province).  
8. Compute $\text{CPC}_{p,t}$ and $\Delta \text{CPC}$; decompose volume vs mix; build offset indices.  
9. Translate $\Delta \text{MWh}$/$\Delta \text{CO₂}$ into $\Delta \text{EF·h}$ under multiple scenarios ($\theta$, net, gross).
10. Generate final figures/tables and write results sections.
11. *(Optional extension)* Cross with economic variables (investment, employment, CAICT) for program-fit discussion.

---

## 9. Main Risks (Reminder)

- **Incomplete kWh coverage**  
  → Primary outcome = CO₂; kWh as secondary outcome/check.

- **Non-EDWC shocks (Sichuan 2022)**  
  → Dummies, donor exclusion, sensitivity analysis.

- **Modeling PUE and GF/W**  
  → Address via Monte Carlo, CPC bands, and clear references (CAICT, MIIT/NDRC/NEA, RMI, ODCC, Green500, HPL-MxP).

- **Endogeneity of EDWC hubs**  
  → Combine Sun–Abraham with SCM; ensure good pre-fits; use placebos; be transparent that these are reduced-form effects of the EDWC package, not of a “data center in a vacuum”.
