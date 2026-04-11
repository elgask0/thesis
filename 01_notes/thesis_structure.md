# Thesis Structure — EDWC, Carbon, Energy and Compute

This is a working outline for the Master's thesis.  
It should evolve as the empirical work and positioning become clearer.

---

## Front matter

- Title page
- Acknowledgments (optional)
- Abstract (≈ 200–300 words)
  - One paragraph on motivation (EDWC, AI, energy–climate tension).
  - One paragraph summarizing RQ1–RQ3 and methods (event-study, SCM, CPC).
  - One paragraph on main quantitative findings and policy relevance.
- Keywords (5–8)

---

## 1. Introduction

1.1. Motivation  
- Why AI and large-scale compute are relevant for energy and climate.  
- China's dual goals: digital development and carbon peaking / neutrality.  
- Eastern Data, Western Compute (EDWC) as an “upstream” AI shock to the power system.

1.2. Research questions  
- RQ1: causal impact of EDWC on provincial CO₂ emissions and electricity consumption.  
- RQ2: construction of Carbon-per-Compute (CPC, tCO₂/EF·h) and compute-compatible scenarios.  
- RQ3: link between EDWC-induced compute/energy changes and provincial economic variables.

1.3. Contribution  
- Empirical: reduced-form causal estimates of EDWC → CO₂ / electricity using event-study + SCM.  
- Measurement: reproducible CPC index combining CI, PUE, and AI-equivalent GF/W.  
- Applied: EDWC “scorecards” and implications for China’s regional development and energy policy.

1.4. Roadmap  
- Short paragraph describing the structure of the remaining sections.

---

## 2. Institutional background: EDWC, compute and green data centers

2.1. The EDWC program  
- Policy launch (February 2022), national hubs and clusters.  
- East–west data and compute reallocation logic (land, climate, renewables).  
- Role of Ningxia, Guizhou, Gansu, Inner Mongolia.

2.2. Data centers, AI compute and electricity demand  
- Nature of AI / GPU workloads (quasi-baseload with some flexibility).  
- Interactions with renewable integration and grid constraints.  
- PUE as a key metric for site efficiency.

2.3. Policy objectives for green compute in China  
- PUE targets for large / ultra-large data centers (MIIT, NDRC, NEA).  
- Targets for renewable electricity use and rack utilization.  
- Role of EDWC hubs in national compute and green transition strategies.

2.4. CAICT computing power indices  
- Description of 综合算力 indices and tiers (Q1–Q4, Elite).  
- How these indices will be used in the thesis (heterogeneity, donor selection for SCM).

---

## 3. Data

3.1. CO₂ emissions (Carbon Monitor–China)  
- Description of daily provincial CO₂ dataset and sectoral breakdown.  
- Aggregation from daily to monthly CO₂ for each province.  
- Discussion of coverage, strengths and limitations.

3.2. Provincial electricity data  
- Sources (NEA, provincial statistical bulletins).  
- Construction of monthly MWh series; treatment of YTD-only reports.  
- Coverage criteria (e.g. ≥ 80% of months for inclusion).

3.3. Carbon intensity (CI)  
- CI from CO₂/MWh (baseline, CM-based).  
- Optional CI from generation mix + emission factors (for checks and counterfactuals).  
- Interpretation: CI reflects both load changes and mix changes.

3.4. PUE trajectories  
- National average PUE levels in 2022–2023.  
- Policy targets for 2025 (national and EDWC hubs).  
- Construction of province-specific PUE paths, with stricter paths for EDWC hubs.

3.5. AI-equivalent efficiency GF/W\_{AI,China}(t)  
- Use of Green500 FP64 efficiency as a starting point.  
- HPL-MxP speedup and MFU adjustment.  
- China-specific interconnect haircut (A800/H800 vs A100/H100).  
- Resulting monthly GF/W time series.

3.6. EDWC go-live dates (treatment definition)  
- Criteria: operational go-live (“投运”, “上线”, “put into use”) with significant capacity.  
- Baseline T₀ for Ningxia, Guizhou, Gansu, Inner Mongolia.  
- Alternative T₀ definitions for robustness (e.g. migration completion, platform go-live).

3.7. Economic controls and outcomes for RQ3  
- Provincial investment (fixed asset investment, infrastructure, ICT).  
- Employment in ICT / software / data center related sectors.  
- CAICT compute tiers and related indicators.

---

## 4. Empirical strategy for RQ1: EDWC → CO₂ and electricity

4.1. Conceptual framework  
- EDWC as a bundled intervention: data centers + grid + renewables + digital policy.  
- What the reduced-form estimates capture (package effect, not pure data center impact).  
- Interpretation in terms of ΔMWh and ΔCO₂.

4.2. Event-study design (Sun–Abraham)  
- Panel structure (province–month, with CO₂ and MWh as baseline outcomes; CO₂ likely assembled first because electricity requires province-by-province scraping).  
- Staggered adoption and group–time ATTs.  
- Model specification: province FE, time FE, weather and other controls.  
- Definition of event-time leads and lags, binning strategy.

4.3. Synthetic Control for Gansu (optional / supplementary)
- Motivation for SCM as a complementary design.
- Donor pool selection (CAICT tiers, exclusion of EDWC and extreme-shock provinces).
- Predictor set (pre-trends in CO₂ / MWh, weather, economic indicators).
- Placebo tests, pre-treatment fit, and robustness checks.

4.4. Identification and limitations  
- Discussion of potential confounders and policy co-movements.  
- Why estimates are interpreted as reduced-form EDWC effects.  
- Role of robustness exercises (alternative T₀, exclusion of specific provinces, etc.).

---

## 5. Results for RQ1: EDWC and provincial CO₂ / electricity

5.1. Event-study results  
- Main β\_\ell dynamics for CO₂: pre-trends, post-treatment patterns.  
- Heterogeneity by province and by CAICT tier.  
- Interpretation in terms of average ΔCO₂ per month post-EDWC.

5.2. Electricity outcomes  
- Event-study for MWh where data coverage allows.  
- Comparison between ΔCO₂ and ΔMWh patterns.  
- Discussion of cases with ΔMWh > 0 but weak or negative ΔCO₂.

5.3. SCM results for Gansu (and others if applicable)  
- Actual vs synthetic CO₂ paths.  
- Placebo distribution and inference.  
- Relation between SCM findings and event-study estimates.

5.4. Summary of reduced-form effects  
- Consolidated estimates of ΔMWh^{EDWC} and ΔCO₂^{EDWC}.  
- Discussion of magnitudes relative to provincial baselines.

---

## 6. CPC and translation to compute (RQ2)

6.1. Definition of Carbon-per-Compute (CPC)  
- Formal definition: CPC\_{p,t} = CI\_{p,t} × PUE\_{p,t} × 1000 / GF/W\_{AI,China}(t).  
- Unit interpretation: tCO₂ per EF·h of compute.  
- Discussion of dependence on CI (mix), PUE (site) and hardware efficiency.

6.2. CPC levels and dynamics  
- CPC\_{p,t} across provinces and over time.  
- Comparison between EDWC and non-EDWC provinces.  
- ΔCPC around EDWC go-live dates.

6.3. Translating ΔMWh and ΔCO₂ into compute (scenarios)  
- Energy-based compute bounds using θ fraction of ΔMWh.  
- Emissions-consistent compute using ΔCO₂ and CPC\_{post}.  
- “Brute” scenarios using pre-EDWC CI as if the mix had not changed.

6.4. Offset index and mix vs volume decomposition  
- Decomposition of ΔCO₂ into volume and mix components.  
- Definition and interpretation of the offset index.  
- Cases where load increases but net CO₂ falls (high offset).

6.5. Uncertainty analysis  
- Monte Carlo treatment of key parameters (GF/W, PUE, CI).  
- Reporting of P10–P90 bands for CPC and EF·h scenarios.

---

## 7. Robustness and sensitivity analyses

7.1. Alternative treatment timings
- Guizhou: later migration-based T₀.
- Inner Mongolia: multi-cloud dispatch platform T₀.
- Effects of shifting T₀ windows on estimated impacts.

7.2. Alternative samples and donor pools
- Excluding Sichuan or other provinces with extreme shocks.
- Alternative donor sets for SCM.

7.3. Alternative parameter choices for PUE and GF/W
- Different PUE convergence paths (more/less aggressive).
- Alternative assumptions about MFU and interconnect haircut.
- Sensitivity of CPC and EF·h scenarios.

7.4. Alternative CI constructions
- Using mix-based CI instead of CM-based CI.
- Effects on CPC and offset indexes.

---

## 8. Discussion

8.1. What do the results imply for China's EDWC strategy?
- Trade-offs between regional development, compute capacity and emissions.
- Role of renewables and grid integration.

8.2. Comparison with international debates on AI and energy
- How China's EDWC experience fits into global concerns about AI energy use.
- Lessons for other countries considering “compute hubs”.

8.3. Exploratory: economic outcomes (program-fit extension)
- Descriptive patterns linking compute/energy shifts to provincial investment and employment.
- Discussion of causality vs association; limitations.
- How EDWC effects map to broader digital-industrial strategy.

8.4. Limitations and open questions
- Data gaps, especially for electricity and data center-specific loads.
- Identification limits for mix vs volume effects.

---

## 9. Conclusions

9.1. Summary of main findings
- Concise recap of RQ1–RQ2 answers.

9.2. Policy implications
- For EDWC and future compute-oriented industrial policy.
- For green data center regulation and grid planning.

9.3. Future research
- Data center-level load and hourly data.
- Integration of prices, curtailment, and demand response.
- Extensions to other countries or global models.

---

## Appendices

- A. Additional data description and cleaning procedures.
- B. Full formulas for GF/W, PUE trajectories and CPC.
- C. Detailed event-study and SCM specifications.
- D. Full robustness tables and additional figures.
