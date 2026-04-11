# EDWC, Compute, and Energy in China: Causal Evidence from Gansu (2022–2025)

> **Working Paper (ZJU MSc Thesis) — Draft**
> Author: _[Your Name]_
> Last updated: 2025-10-02
>
> **Note:** This file is synced with [[../../04_drafts/working_paper.md]]. Edits should be made in both locations or use one as the working copy.

---

## Abstract

China’s **Eastern Data, Western Computing (EDWC)** program redirects data-processing workloads from coastal demand centers to inland provinces rich in land and lower-cost/cleaner power. We provide causal evidence on how EDWC affects **electricity use** and **CO₂ emissions** at the provincial level, with a **spotlight on Gansu**, and we translate these impacts into **AI-compute-relevant metrics** using an auditable **Carbon‑per‑Compute (CPC)** framework. Our identification combines (i) a **staggered‑adoption event study** (Sun–Abraham) with the go‑live timing of EDWC clusters (Ningxia 2023‑07, Guizhou 2023‑12/2024‑01, Gansu 2024‑06, Inner Mongolia 2024‑04) and (ii) a **single‑treated synthetic control** (SCM) for Gansu (2019–2025) using untreated provinces in the same CAICT compute tier as donors. We estimate dynamic effects on **daily CO₂ emissions** (primary) and **monthly electricity consumption** (secondary), show robust **parallel pre‑trends**, and translate post‑treatment effects into **ΔCPC** using exogenous **compute‑efficiency (GF/W)** and **PUE** paths. We discuss mechanisms (cooling load, task migration, green power availability), heterogeneity by **CAICT quartile** and **EDWC cohort**, and provide **policy/industry products** (risk dashboard, stress‑test inputs, and CPC indices).

---

## 1. Motivation and Contributions

- **Motivation.** AI adoption is increasing **compute demand**, which in turn draws on **electricity** and affects **emissions** via the grid mix. China’s EDWC re‑allocates workloads to western hubs (Ningxia, Gansu, Inner Mongolia, Guizhou), potentially changing **where** and **when** electricity is consumed and emissions are released.
- **Core question.** What is the **causal impact** of EDWC **go‑live** on **provincial electricity use and CO₂ emissions**, and how large is the **AI‑relevant emissions per compute (CPC)** implied by these shifts?
- **Contributions.**
  1) **Causal effects** from a transparent **policy shock** (EDWC go‑live) using **staggered event studies** and **SCM**.  
  2) **AI‑relevant translation**: from ΔCO₂/ΔMWh to **ΔCPC** via **GF/W** and **PUE**, with uncertainty bands.  
  3) **Applied outputs**: a **provincial CPC dashboard**, **risk flags** for utilities/credit, and **scalable metrics** useful to firms and regulators.

---

## 2. Research Questions (RQ)

- **RQ1 (Causal, primary):** *What is the dynamic effect of EDWC **go‑live** on provincial **daily CO₂ emissions** and **monthly electricity consumption**?*  
  - Level and persistence of the treatment effect, **event‑time profile** (anticipation, immediate, and longer‑run effects).
  - **Heterogeneity**: by **CAICT compute quartile**, EDWC vs non‑EDWC, and green resource endowment.
- **RQ2 (Translation to AI):** *Given RQ1’s effects, what is the implied **Carbon‑per‑Compute (CPC)** for each province and month, and how does it vary with **compute efficiency (GF/W)**, **PUE**, and **grid carbon intensity (CI)**?*  
  - Produce **ΔCPC** (post–pre) for treated provinces and **levels** of CPC when combined with a defensible efficiency path.

---

## 3. Policy Background and Timing

- **EDWC design.** In **February 2022**, China approved **8 national hub nodes** and **10 data‑center clusters**, launching EDWC to shift compute westward while ensuring strong network interconnection and greener energy use (cleaner resource bases, land, cooling).  
- **Staggered go‑live dates we use as treatment:**
  - **Ningxia (NX)**: **2023‑07‑21** — **China Telecom Ningxia DC Phase I** accepted and ready for operation (Zhongwei Gov; Zhongwei DRC).
  - **Guizhou (GZ)**: **2023‑12 / 2024‑01** — **NetEase Gui'an DC** trial operation end-2023; ramp in 2024 (Guiyang Daily PDF; Gui'an Admin); **SPIC Guian Data Center** reported online & in operation early 2024.
  - **Gansu (GS)**: **2024‑06‑19** — **Qingyang DC cluster** first **10,000P** batch **online**, **15,000 racks** reported by late June; multiple facilities “投运/上线”.  
  - **Inner Mongolia (IM)**: **2024‑04‑28** — **China Mobile Hohhot Intelligent Computing Center** commissioned/in production (China Mobile; Inner Mongolia News).
- **Why these dates?** They mark **operational milestones** at scale (transaction platform online; DC clusters entering service; official communications indicating commissioning). We use ±1–2‑month windows in robustness.

> **Note.** Sichuan/Chongqing are an EDWC pair; however **Sichuan’s 2022 hydro drought power rationing** complicates identification. We keep SC/Chongqing **out of the initial treated set** and use them in **robustness** or as excluded donors in SCM.

---

## 4. Data

### 4.1 Outcomes (dependent variables)

1) **Daily provincial CO₂ emissions** (2019–2025): tonnes/day by province.  
2) **Monthly electricity consumption** (kWh) at province and national levels (2022–2025, subset broader for treated provinces and matched controls).

### 4.2 Treatment and covariates

- **EDWC treatment**: province‑specific **T₀** (go‑live date) and **post** indicator.  
- **CAICT compute quartiles** (Q1–Q4, “Elite”): used for **heterogeneity** and **donor selection**.  
- **Grid mix & CI (tCO₂/MWh)**: monthly shares (coal, gas, hydro, wind, solar, nuclear) and computed CI.  
- **PUE**: monthly provincial PUE paths, converging to policy target **<1.5 by 2025**, with uncertainty ±0.1.  
- **Weather controls**: daily max/min temperature and **cooling degree days** (CDD), precipitation; lag structure to absorb heat‑driven cooling effects.  
- **Other controls**: provincial industrial production proxy (if available), outage/curtailment flags (e.g., Sichuan 2022 heat‑drought episode).

### 4.3 AI‑compute parameters for CPC translation

- **GF/W (AI‑equivalent compute efficiency)**: monthly series (2019–2025), constructed from **Green500 FP64** frontier × **HPL‑MxP** speedup × **MFU realism** × **China interconnect haircut (A800/H800)**.  
- **PUE**: as above.  
- **CI**: as above.

---

## 5. Identification Strategy and Models

### 5.1 Staggered‑adoption event study (Sun–Abraham) — RQ1

Let $Y_{p,t}$ be either daily CO₂ (primary) or monthly kWh (secondary) for province $p$ at date $t$. Let $E_p$ be the **first EDWC go‑live** month for province $p$ (absorbing treatment). Define **event time** $\ell = t - E_p$. We estimate:

$$
Y_{p,t} \;=\; \alpha_p + \tau_t \;+\; \sum_{\ell\in \mathcal{L},\,\ell\neq \ell_0}
\beta_\ell\, 1\{t-E_p=\ell\} \;+\; \gamma'X_{p,t} \;+\; \varepsilon_{p,t},
$$

where $\alpha_p$ are **province fixed effects**, $\tau_t$ **time fixed effects** (day or month), $X_{p,t}$ includes weather and CI controls, and $\ell_0$ is the **omitted bin** (e.g., $\ell=-1$). We implement **Sun–Abraham (2021)** cohort‑specific estimators to avoid TWFE contamination under staggered adoption and treatment heterogeneity.

- **Cohorts** $g$ are defined by $E_p=g$. We estimate **cohort‑relative ATTs** $\text{ATT}_{g,\ell}$ and then **aggregate** to overall event‑time effects $\beta_\ell$ using the Sun–Abraham aggregation rules.  
- **Pre‑trend checks**: $\widehat{\beta}_\ell \approx 0$ for $\ell\ll 0$; joint F‑tests on leads.  
- **Dynamic patterns**: plot $\widehat{\beta}_\ell$ for $\ell\in[-12,+18]$ months.  
- **Heterogeneity**: interact treatment with **CAICT quartile** and **treated cohort** dummies.

**Interpretation (simple):** if $\widehat{\beta}_{+6} = 1{,}500$ tCO₂/day for Gansu, six months after go‑live, then all else equal EDWC is associated with **+1.5 kt/day** emissions relative to the no‑EDWC counterfactual for that date (after removing province/time effects and controls).

### 5.2 Synthetic Control for Gansu (optional / supplementary) — RQ1

We build a **synthetic Gansu** from a convex combination of **untreated donor provinces** (same **CAICT quartile Q1**; exclude EDWC destinations and provinces with major power shocks). Pre‑period: 2019–**2024‑05**. Post: **2024‑06** onward.

- **Outcome to match:** **daily CO₂** (primary); secondary SCM on **monthly kWh** (if data coverage suffices).  
- **Predictors:** lags of the outcome (seasonal means), **weather (CDD)**, **grid mix shares**, **CI**, and **industrial proxy** where available.  
- **Placebos:** leave‑one‑out and **in‑space** placebo distribution to compute **post/pre RMSPE ratios** and **p‑values**.  
- **Robustness:** ridge‑augmented SCM, restricted donor pools, alternative start date (**±1 month**).

**Interpretation:** post‑2024‑06 divergence between actual Gansu and its synthetic is the **causal effect** under standard SCM assumptions.

### 5.3 Translating impacts into AI‑relevant CPC — RQ2

We map energy/emissions impacts into **CPC** using an **exogenous efficiency (GF/W)** & **PUE** path (no calibration to outcomes). For province $p$ and month $t$:

1. **IT‑layer energy per EF·h:**
   $$e^{IT}_{t} \;=\; \frac{1000}{\mathrm{GF/W}_{AI,China}(t)} \;\; \text{[MWh per EF·h].}$$
2. **Site energy per EF·h:** $e^{Site}_{p,t} = e^{IT}_{t}\times \mathrm{PUE}_{p,t}$.
3. **CPC level:** $\mathrm{CPC}_{p,t} = \mathrm{CI}_{p,t}\times e^{Site}_{p,t}$ $[\mathrm{tCO_2/EF\cdot h}]$.
4. **ΔCPC:** compare **post** minus **pre** within province and against controls to attribute **policy‑relevant change**.

> **Key point.** We **do not need** to observe total MWh **used by AI**. CPC is an **intensive margin**: “tonnes of CO₂ per unit of compute”, constructed from **exogenous** efficiency and local PUE/CI. RQ1’s **ΔCO₂** quantifies the **scale** impact of EDWC (how much more/less emissions), while **CPC** translates the environment in which any compute would operate.

---

## 6. Estimation Steps (High‑School First, Then University)

### 6.1 High‑school explanation

1) **Pick dates** when EDWC truly started in each province (e.g., Gansu June 2024).  
2) **Look at CO₂ every day** in those provinces and in similar provinces that didn’t start yet.  
3) **Compare before/after** the start date, while also comparing to provinces that didn’t start (so we don’t confuse the effect with national trends).  
4) **If you see a jump** in CO₂ in the treated province right after the start, bigger than in the control provinces, it suggests EDWC made emissions go up. If you see a drop, the opposite.  
5) **To be extra sure**, we create a **synthetic twin** of the treated province using a weighted average of control provinces that mirrors its past behavior. After the start date, we check whether the real province behaves differently than its twin.  
6) **Finally**, we translate the environment into **CPC**: knowing how efficient computers are (GF/W), how much extra energy the site uses (PUE), and how dirty/clean the grid is (CI), we compute **tonnes of CO₂ per EF·h**. Lower CPC means **cleaner compute**.

### 6.2 University/graduate detail

- **Event study (Sun–Abraham).** Construct cohort‑relative dummies $1\{t-E_p=\ell\}$, drop $\ell=-1$; run cohort‑specific regressions and **aggregate** to event‑time ATTs. Cluster SEs by province; weight by population or unweighted (report both). Add **controls** $X_{p,t}$: CDD, precipitation, CI levels, month×year FE (for daily spec include day‑of‑week). Test **placebo leads** jointly; include **anticipation window** (e.g., set $\ell<-2$ to a lead bin).  
- **SCM (Abadie et al.).** Outcome: daily CO₂. Donor pool: Q1 provinces **not** in EDWC destinations (e.g., Guangxi, Hainan, Yunnan, Qinghai). Fit on 2019–2024‑05. Plot gap and compute **RMSPE ratios**. Conduct **leave‑one‑out** checks.  
- **From Δ to CPC.** CPC is **level** built from parameters; **ΔCPC** uses contemporaneous **PUE/CI** shifts and efficiency month $t$. To **attribute** emissions changes to **AI compute growth**, we multiply **ΔCPC** by **estimated ΔEF·h** only if we also build an EF·h proxy (optional; see §8).

---

## 7. Variables, Construction, and Joins

- **Unit/date:** province‑day for CO₂; province‑month for kWh, CI, PUE.  
- **Joins:** aggregate daily to monthly when needed; interpolate CI monthly; align PUE monthly paths; align **GF/W** monthly (linear between Green500/ HPL‑MxP editions).  
- **Key series summaries:**
  - **CO₂\_{p,t} (day):** tonnes/day.  
  - **kWh\_{p,m}:** electricity consumption (MWh).  
  - **CI\_{p,m}:** computed from generation mix and standard emission factors.  
  - **PUE\_{p,m}:** converging to **<1.5** by 2025 with province‑specific priors (e.g., cooler climates ↘ PUE).  
  - **GF/W\_{AI,China}(t):** from FP64 frontier × MxP speedup × MFU (0.5) × China interconnect haircut (A800/H800 epochs).

---

## 8. Optional: Backing‑out ΔEF·h (Scale) from ΔCO₂ (If Desired)

If we want **AI compute scale** (EF·h) induced by EDWC, under strong assumptions we can **back‑out**:

1) Use **event‑study effect** on emissions $\Delta \mathrm{CO₂}_{p,t}$.  
2) Divide by **CPC\_{p,t}** to get a **lower‑bound** of **ΔEF·h**:
   $$
   \Delta \widehat{\mathrm{EF\cdot h}}_{p,t} \;=\; \frac{\Delta \mathrm{CO₂}_{p,t}}{\mathrm{CPC}_{p,t}}.
   $$
   This is a **lower‑bound** because not all $\Delta \mathrm{CO₂}$ is necessarily AI‑compute (other industries may co‑move).  
3) Sum across months to obtain **cumulative EF·h** increment attributable to EDWC.

**Caveat.** This step is **not needed** to compute CPC; it is an **optional scale translation** subject to identification risk. We keep it in an **appendix**.

---

## 9. Estimation Details and Pseudocode

### 9.1 Event study (Sun–Abraham) in Stata

```stata
* Panel: province-day (primary) or province-month (secondary)
xtset prov_id date

* Create event-time variables around T0 (EDWC go-live) for each province
gen relm = month(date) - month(T0_prov) + 12*(year(date)-year(T0_prov))

* Collapse leads/tails to bins, drop -1 as reference
gen L2plus = relm<=-2
gen F12plus = relm>=12
forvalues l=-12/12 {
    gen ev`l' = (relm==`l')
}

* Sun–Abraham via suest/stacked (use csdid-like or dedicated packages)
* Suggested: use community implementation "eventstudyinteract" in Stata or "sunab()" in fixest (R).

* Stata (reghdfe) + sunab() equivalent in R:
* reghdfe Y i.rel#i.cohort X, absorb(prov_id date) vce(cluster prov_id)

* In R (fixest):
# fes <- feols(Y ~ sunab(cohort, date) + X | prov_id + date, data=panel, cluster="prov_id")
# etable(fes, coefstat="se")
```

### 9.2 SCM for Gansu in R

```r
library(Synth)
# Treated unit: Gansu (GS)
# Donors: Guangxi, Hainan, Yunnan, Qinghai (Q1, non-EDWC)
dataprep.out <- dataprep(
  foo = panel_month,
  predictors = c("ci","cdd","precip","co2_month_mean"),
  predictors.op = "mean",
  time.predictors.prior = 2019:2024.416,   # up to May 2024
  dependent = "co2_month",
  unit.variable = "prov_id",
  time.variable = "t",
  treatment.identifier = "GS",
  controls.identifier = c("GX","HI","YN","QH"),
  time.optimize.ssr = 2019:2024.416,
  time.plot = 2019:2025.75
)
synth.out <- synth(dataprep.out)
# Plot gaps and compute post/pre RMSPE
```

### 9.3 CPC computation

```python
# CPC_{p,t} = CI_{p,t} * PUE_{p,t} * (1000 / GF_W_{AI,China}(t))
# All arrays are monthly; CI in tCO2/MWh; GF_W in GF/W
CPC = CI * PUE * (1000.0 / GF_W)
```

---

## 10. Robustness, Falsification, and Sensitivity

- **Parallel trends:** joint tests on **pre‑treatment leads**; show flat pre‑profiles.  
- **Placebo provinces:** assign placebo T₀ to never‑treated provinces; expect null.  
- **Placebo years:** randomly re‑date T₀; expect null.  
- **Alternative outcomes:** monthly kWh as secondary with consistent signs.  
- **Climate shocks:** control for **CDD** and interactions; exclude **Sichuan 2022** window as a robustness.  
- **Alternative T₀ windows:** shift go‑live ±1–2 months; results stable.  
- **Aggregation choice:** daily vs monthly; report both where possible.  
- **Donor pool restrictions:** same **CAICT quartile**; exclude provinces with EDWC projects or major confounders.  
- **Inference:** cluster‑robust SEs (event study), RMSPE ratio p‑values (SCM).

---

## 11. Mechanisms and Heterogeneity

- **Cooling & PUE:** Hot‑day cooling raises **site energy**; western hubs may have cooler nights/elevation, lowering PUE.  
- **Green resources:** Higher **wind/solar shares** (IM, Gansu) can depress **CPC** even if total compute grows.  
- **Network & utilization:** China‑SKU interconnect haircuts (A800/H800) reduce realized **GF/W**, raising CPC; expect improvements as ecosystems optimize.  
- **Heterogeneity by CAICT tier:** Higher‑tier provinces may show **greater load re‑allocation** (more data to send west) but not necessarily worse CPC if grids are cleaner.

---

## 12. Applied Products (for private sector & policy)

1) **EDWC Impact Dashboard**: panel of event‑study estimates by province; flagged **pre‑trend**, **post‑level**, **CI/PUE** paths; export to PDF.  
2) **CPC Indices**: province‑month CPC levels and ΔCPC; uncertainty bands via simple Monte Carlo.  
3) **Stress‑tests**:  
   - **Grid stress**: simulate 10% extra EF·h routed to Gansu; compute ΔMWh and ΔCO₂ using CPC.  
   - **Credit risk**: translate persistent ΔCO₂ to implied **load growth** and CapEx needs.  
4) **Procurement guide**: prioritize **low‑CPC provinces** for flexible training jobs; quantify **CO₂ saved per EF·h migrated**.

---

## 13. Limitations and How We Address Them

- **Intraday data absent:** we cannot measure within‑day shifting. We focus on **daily CO₂** and **monthly kWh**; interpretation is **aggregate**.  
- **Attribution risk:** ΔCO₂ may reflect non‑compute industry growth. We use **donor‑matched controls**, **placebos**, and **weather/industry controls** to mitigate.  
- **Baseline AI MWh unknown:** we avoid claiming levels of AI MWh. We provide **CPC levels** and **ΔCPC** from exogenous parameters; **ΔEF·h** back‑out is **optional** and labeled conservative.  
- **Treatment timing noise:** we adopt **T₀ windows** and multiple sources; results must be robust to ±1–2 months.  
- **Sichuan 2022**: excluded from main treated set; used only in robustness.

---

## 14. Implementation Checklist

- [ ] Build panel (daily CO₂; monthly kWh, CI, PUE; weather).  
- [ ] Tag **T₀** for NX (2023‑07‑21), GZ (2023‑12/2024‑01), GS (2024‑06‑19), IM (2024‑04‑28).
- [ ] Estimate **Sun–Abraham** event study (primary: CO₂/day).  
- [ ] SCM for **Gansu** (2019–2025) — optional.
- [ ] Construct **GF/W\_{AI,China}(t)**, **PUE\_{p,t}**, **CI\_{p,t}**; compute **CPC** and **ΔCPC**.  
- [ ] Translate into **products** (dashboard, tables, write‑up).

---

## 15. Notation Summary

- $Y_{p,t}$: outcome (CO₂/day, kWh/month).  
- $E_p$: first go‑live month (absorbing treatment).  
- $\ell=t-E_p$: event time; $\ell_0=-1$ omitted.  
- $\alpha_p, \tau_t$: province and time fixed effects.  
- $X_{p,t}$: controls (weather, CI, etc.).  
- $\mathrm{GF/W}_{AI,China}(t)$: monthly compute efficiency.  
- $\mathrm{PUE}_{p,t}$: power usage effectiveness.  
- $\mathrm{CI}_{p,t}$: grid carbon intensity (tCO₂/MWh).  
- $\mathrm{CPC}_{p,t}$: $=\mathrm{CI}_{p,t}\cdot \mathrm{PUE}_{p,t}\cdot\frac{1000}{\mathrm{GF/W}_{AI,China}(t)}$.

---

## 16. Figures to Produce (once data are merged)

- **Figure 1.** Event‑study coefficients $\widehat{\beta}_\ell$ for CO₂/day (overall and by province).  
- **Figure 2.** SCM for Gansu: actual vs synthetic CO₂ (2019–2025) and gap.  
- **Figure 3.** Monthly **CPC\_{p,t}** for Gansu and peer provinces (with P10–P90 bands).  
- **Figure 4.** Heterogeneity: post‑12‑month ATTs vs **CAICT quartile** and **CI/PUE** levels.

---

## 17. Ethical and Reproducibility Notes

- All sources are **public**; code will be released under an **open license**.  
- We avoid **proprietary secrets**; no facility‑level confidential data used.  
- Pre‑register hypotheses: *sign and persistence of ATTs; CPC declines where CI/PUE improve; stronger effects in EDWC destinations.*

---

## Bibliography (APA 7th)

Abadie, A., Diamond, A., & Hainmueller, J. (2010). **Synthetic Control Methods for Comparative Case Studies**. *Journal of the American Statistical Association, 105*(490), 493–505. https://www.tandfonline.com/doi/abs/10.1198/jasa.2009.ap08746

Abadie, A., Diamond, A., & Hainmueller, J. (2015). **Comparative Politics and the Synthetic Control Method**. *American Journal of Political Science, 59*(2), 495–510. https://onlinelibrary.wiley.com/doi/abs/10.1111/ajps.12116

China State Council (2024, July 24). **China sets green targets for data centers (PUE < 1.5 by 2025).** https://english.www.gov.cn/news/202407/24/content_WS66a0b167c6d0868f4e8e96ba.html

MLCommons. (n.d.). **Inference Power Measurement Methodology.** https://docs.mlcommons.org/inference/power/

National Development and Reform Commission (NDRC). (2022, Feb 17). **“东数西算”工程正式全面启动**. https://www.gov.cn/xinwen/2022-02/17/content_5674322.htm

National Development and Reform Commission (NDRC). (2022, Feb 17). **“东数西算”三问**. https://www.gov.cn/zhengce/2022-02/17/content_5674406.htm

Zhongwei Government / Zhongwei DRC. (2023, Jul 21). **China Telecom Ningxia DC Phase I accepted and ready for operation** (中卫市).

People’s Daily / Guangming Daily. (2024, Jun 19–25). **庆阳数据中心集群首批万P算力上线 / 算力规模新突破**. https://gansu.gansudaily.com.cn/system/2024/06/19/031018769.shtml ; https://kpzg.people.com.cn/n1/2024/0625/c404214-40263395.html

Qingyang, Gansu — Media reports. (2024–2025). **庆阳市“东数西算”重大项目建设全面提速 / 产业园投运**. https://gansu.gscn.com.cn/system/2024/06/19/013158221.shtml ; https://finance.sina.com.cn/roll/2024-09-23/doc-incqeerh9859198.shtml

Reuters. (2022, Aug 22). **China’s Sichuan extends power curbs as heatwave drags on**. https://www.reuters.com/world/china/chinas-sichuan-extends-power-curbs-until-aug25-heatwave-drags-caixin-2022-08-22/

RMI. (2024, Nov). **Powering the Data‑Center Boom with Low‑Carbon Solutions**. https://rmi.org/insight/powering-the-data-center-boom-with-low-carbon-solutions/

Sun, L., & Abraham, S. (2021). **Estimating dynamic treatment effects in event studies with heterogeneous treatment effects**. *Journal of Econometrics, 225*(2), 175–199. https://www.sciencedirect.com/science/article/abs/pii/S030440762030378X

China Mobile / Inner Mongolia News. (2024, Apr 28). **China Mobile Hohhot Intelligent Computing Center commissioned/in production** (中国移动呼和浩特智算中心).

Guiyang Daily PDF / Gui'an Admin. (2023–2024). **NetEase Gui'an DC trial operation / SPIC Guian DC online** (贵阳日报; 贵安新区).

TOP500/Green500 (various years). **Green500 Lists and Methodology.** https://top500.org/lists/green500/

Xinhua/NCSTI (2025). **东数西算 — 专题** (overview hub/cluster list). https://www.ncsti.gov.cn/kjdt/ztbd/dsxs/

---

*End of report.*
