# AI‑Equivalent Energy Efficiency (GFLOPS/W) 2019–2025: Reproducible Method for Provincial Carbon‑per‑Compute (CPC) in China

## 1. Goal and Why This Matters

We want monthly **Carbon-per-Compute (CPC)** by province in China. Given provincial **carbon intensity** `CI_{p,t}` and **PUE**, we need a defensible monthly series of **AI-equivalent compute efficiency** in **GFLOPS/W (GF/W)** to convert energy into **exaflop-hours** and then into emissions:

$$
e^{IT}_{p,t}=\frac{1000}{\mathrm{GF/W}_{p,t}}
\quad \text{(MWh per EF·h, IT layer)}
$$

$$
e^{Site}_{p,t}=e^{IT}_{p,t}\times \mathrm{PUE}_{p,t}
\quad \text{(MWh per EF·h, site layer)}
$$

$$
\mathrm{CPC}_{p,t}=\mathrm{CI}_{p,t}\times e^{Site}_{p,t}
\quad \text{(tCO_2 per EF·h)}
$$

The challenge is that the long-run, audited efficiency series we can observe consistently is **Green500 / HPL FP64**, not modern AI training or inference. So we construct an **AI-equivalent** proxy that is:

- auditable,
- replicable,
- valid over 2019–2025,
- and explicit about where China-specific frictions enter.

Here, **AI-equivalent** means a transparent proxy for the efficiency of real hardware under modern AI-like mixed-precision workloads, built from public benchmark series and a small number of clearly stated adjustments.

---

## 2. Short History and Core Definitions

- **HPL (High-Performance Linpack):** dense linear-system benchmark in FP64 used by TOP500. Green500 ranks systems by **GF/W measured during HPL**. It is audited, methodologically stable, and available over time.
- **HPL-MxP / HPL-AI:** mixed-precision version of HPL that uses lower precision with iterative refinement, engaging tensor-core style pathways more similar to AI workloads. It reports a **speedup** relative to HPL.
- **Green500 GF/W:** electricity efficiency measured during HPL FP64. It is not an AI benchmark, but it is the cleanest longitudinal audited series.
- **`s_{mxp}(t)`:** the HPL-MxP to HPL speedup used as the bridge from FP64 to AI-like mixed-precision performance.
- **`κ_global`:** a global utilization realism factor that maps theoretical mixed-precision capability into practical large-scale training efficiency.
- **`λ`:** the communication-bound share of workload execution.
- **`β(t)`:** the China-versus-global interconnect ratio by hardware epoch.
- **`χ_CN(t)`:** the China-specific adjustment factor applied to the global AI-equivalent series.

The key intuition is simple: if **HPL** and **HPL-MxP** both operate near similar power envelopes, then a large fraction of the mixed-precision throughput gain should translate approximately one-for-one into higher **GF/W**. We then apply a separate realism factor for practical training efficiency and, after that, a separate China-specific interconnect penalty for the export-control period.

---

## 3. Core Formulas

### 3.1 Global AI-equivalent series

$$
\mathrm{GF/W}_{AI,\;global}(t)=\mathrm{GF/W}_{HPL}(t)\times s_{mxp}(t)\times \kappa_{global}
$$

Where:

- `GF/W_{HPL}(t)` is the monthly HPL efficiency frontier from Green500.
- `s_{mxp}(t)` is the monthly mixed-precision speedup from HPL-MxP.
- `κ_global = 0.50` is the central utilization realism assumption.

### 3.2 China-specific adjustment

For the A800/H800 period, lower interconnect bandwidth matters for the communication-bound part of training. Model that as:

$$
\mathrm{GF/W}_{AI,\;China}(t)=\mathrm{GF/W}_{AI,\;global}(t)\times \chi_{CN}(t)
$$

with

$$
\chi_{CN}(t)=(1-\lambda)+\lambda\cdot\beta(t)
$$

and

$$
\beta(t)=\frac{\mathrm{BW}_{CN}(t)}{\mathrm{BW}_{global}(t)}
$$

Central values:

- `λ = 0.40`
- `β = 0.667` for `2022-11` to `2023-10` using A800 `400 GB/s` versus A100 `600 GB/s`
- `β = 0.444` for `2023-11` onward using H800 `400 GB/s` versus H100 `900 GB/s`

This gives:

- pre-`2022-11`: `χ_CN(t) = 1`
- `2022-11` to `2023-10`: `χ_CN(t) = 0.867`
- `2023-11` onward: `χ_CN(t) = 0.678`, which we can summarize as roughly `0.70`

### 3.3 Why `κ` and `λ` do not double count

- `κ_global` captures practical model-FLOPs utilization: kernels, pipeline bubbles, data movement, scheduling overhead, and imperfect scaling in real training.
- `λ` captures an additional **China-specific** slowdown from reduced inter-GPU communication bandwidth during the export-control period.

So the two parameters operate on different margins and should both remain in the model.

### 3.4 CPC mapping

Once `GF/W_{AI,China}(t)` is built, compute:

$$
e^{IT}_{p,t}=\frac{1000}{\mathrm{GF/W}_{AI,\;China}(t)}
$$

$$
e^{Site}_{p,t}=e^{IT}_{p,t}\cdot \mathrm{PUE}_{p,t}
$$

$$
\mathrm{CPC}_{p,t}=\mathrm{CI}_{p,t}\cdot e^{Site}_{p,t}
$$

---

## 4. Data Inputs and Table Shapes

### 4.1 Green500 (HPL FP64)

**Use:** audited longitudinal baseline for energy efficiency under HPL.

Typical table shape:

| date | system | rmax_gflops | power_w | gf_per_w | country |
|---|---|---:|---:|---:|---|
| 2021-11 | XYZ Supercomputer | 5.3e14 | 7.6e6 | 69.7 | JP |
| 2022-06 | ABC Cluster | 3.2e14 | 3.7e6 | 86.5 | US |

Construction choice:

- Default: use the **median** of a top subset or a robust percentile such as **P75**.
- Sensitivity: compare `P50` versus `P75`.

### 4.2 HPL-MxP (HPL-AI)

**Use:** mixed-precision multiplier for AI-like performance.

Typical table shape:

| date | site | computer | hpl_mxp_ef | hpl_ef | speedup |
|---|---|---|---:|---:|---:|
| 2024-11 | ANL | Aurora | 11.643 | 1.012 | 11.5 |
| 2025-06 | LLNL | El Capitan | 16.680 | 1.742 | 9.6 |
| 2025-06 | ORNL | Frontier | 11.390 | 1.353 | 8.4 |

Use the **median speedup by date**.

### 4.3 Interconnect specification table for `β(t)`

| period | cn_sku | bw_cn_gbps | ref_sku | bw_global_gbps | beta |
|---|---|---:|---|---:|---:|
| 2022-11..2023-10 | A800 | 400 | A100 | 600 | 0.667 |
| 2023-11..2025-12 | H800 | 400 | H100 | 900 | 0.444 |

### 4.4 MLPerf Power (validation only)

**Use:** independent trend check, not calibration.

Filter toward:

- `division == "closed"`
- `category == "datacenter"`
- `scenario == "Offline"`
- `result_type == "power"`

Typical table shape:

| submission_date | division | submitter | system | model | scenario | samples_per_j | notes |
|---|---|---|---|---|---|---:|---|
| 2023-04-05 | closed | NVIDIA | DGX H100 | bert-99 | Offline | 0.85 | v3.0 |
| 2023-09-13 | closed | NVIDIA | HGX H100 | resnet50 | Offline | 1.35 | v3.1 |

### 4.5 PUE and provincial CI inputs

For CPC we also need:

- `PUE_{p,t}` by province-month
- `CI_{p,t}` by province-month

These are not derived from the hardware benchmark stack, but they enter directly in the final CPC calculation.

---

## 5. Reproducible Workflow

### Step 1. Build `GF/W_HPL(t)`

1. Download Green500 releases for `2019` to `2025`.
2. For each June/November release, compute a robust frontier statistic:
   - baseline: `P50` of top systems or median of top-N
   - sensitivity: `P75`
3. Convert the biannual series into monthly values.

Default rule:

- use **step-hold** forward until the next release

Optional sensitivity:

- linear interpolation between releases
- 3-month smoothing after interpolation

### Step 2. Build `s_mxp(t)`

1. Download the HPL-MxP results table.
2. Keep the release date and `speedup`.
3. Compute the **median speedup** by date.
4. Convert to monthly values using step-hold or lightly smoothed interpolation.

### Step 3. Apply `κ_global`

Take:

$$
\kappa_{global}=0.50
$$

as the central case, motivated by reported large-scale training MFU in the `40%` to `60%` range, with higher values only under strong optimization.

Then compute:

$$
\mathrm{GF/W}_{AI,\;global}(t)=\mathrm{GF/W}_{HPL}(t)\cdot s_{mxp}(t)\cdot 0.50
$$

### Step 4. Apply `χ_CN(t)`

1. Set the central communication-bound share `λ = 0.40`.
2. Build the epoch-specific `β(t)` table from public NVLink bandwidth.
3. Compute:

$$
\chi_{CN}(t)=(1-\lambda)+\lambda\beta(t)
$$

4. Compute:

$$
\mathrm{GF/W}_{AI,\;China}(t)=\mathrm{GF/W}_{AI,\;global}(t)\cdot \chi_{CN}(t)
$$

### Step 5. Move from efficiency to CPC

1. Build `PUE_{p,t}` by province-month.
2. Build `CI_{p,t}` by province-month.
3. Compute `e^{IT}`, `e^{Site}`, and `CPC`.

---

## 6. Why the HPL-MxP Speedup Can Proxy AI Efficiency

This is the key identifying assumption in the method.

### Assumption A1: throughput speedup approximately transfers to GF/W

The argument is:

- HPL and HPL-MxP both tend to run near high power envelopes.
- Mixed precision engages tensor-core-style pathways closer to real AI math.
- If power is roughly similar but performance is much higher, **GF/W** should rise proportionally.

This is still an approximation, so we do **not** claim exact calibration. Instead we:

- keep the assumption explicit,
- propagate uncertainty with Monte Carlo,
- and validate trend co-movement using MLPerf Power from `2023` onward.

---

## 7. Ex-Post Validation with MLPerf Power

The objective is not to calibrate the series to MLPerf, only to show that they move together over time.

### Validation procedure

1. Pull MLPerf Inference Power results for `Datacenter / Closed / Power / Offline`.
2. Use stable recurring models first:
   - `bert-99`
   - `resnet50`
   - optionally later LLM entries where coverage is sufficient
3. Aggregate to a monthly MLPerf efficiency index using the median `samples_per_joule`.
4. Rebase both:
   - MLPerf index
   - `GF/W_{AI,global}(t)` or `GF/W_{AI,China}(t)`

to `100` at `2023-06`.

5. Compute:
   - Spearman correlation
   - Pearson correlation
   - slope coefficient between rebased indices

Suggested acceptance rule:

- Spearman `ρ >= 0.7`
- slope roughly within `0.7` to `1.3`

Interpretation:

- strong co-movement supports the temporal shape of the series
- divergence does not automatically falsify the method, because MLPerf is inference-focused and hardware/model mix changes over time

---

## 8. PUE by Province-Month

Public province-month PUE is limited, so the construction must be rule-based and well documented.

### Baseline anchor

- China-wide reference level around `1.48` in `2023`
- policy target below `1.5` by `2025`

### Defensible province-month construction

1. Start from the national anchor.
2. Add a climate adjustment by province using cooling-degree or weather-based seasonality.
3. Allow EDWC western hubs to have structurally better PUE where justified by climate and newer campuses.

Practical rule:

- seasonal adjustment: approximately `±0.05` to `±0.10`
- EDWC hubs such as Inner Mongolia, Ningxia, Guizhou, and Gansu can receive a modest downward adjustment, for example `-0.05`
- warm coastal provinces can receive a modest upward adjustment, for example `+0.05`

If operator-specific PUE becomes available for places such as Hohhot, Zhongwei, Gui'an, or Zhangjiakou, use it in priority over the generic climate-rule construction.

---

## 9. Carbon Intensity by Province-Month

Two defensible routes exist, but the preferred one for CPC is province-month generation mix.

### Mix-based formula

$$
\mathrm{CI}_{p,t}=\sum_{k\in\{\mathrm{coal,gas,hydro,wind,solar,nuclear}\}}\omega_{p,t,k}\cdot \mathrm{EF}_k
$$

Where:

- `ω_{p,t,k}` is the generation share of technology `k`
- `EF_k` is the emissions factor for technology `k`

Baseline emissions factors:

- coal: about `0.95 tCO2/MWh`
- gas: about `0.40 tCO2/MWh`
- wind / solar / hydro / nuclear: operationally near zero in the direct-combustion sense

### Data route

- NBS
- CEC
- CREA
- Ember
- optionally CEADs for annual cross-checks or interpolation support

---

## 10. Execution Recipe

1. Download Green500 for `2019–2025` and build monthly `GF/W_HPL(t)`.
2. Download HPL-MxP and build monthly `s_mxp(t)`.
3. Apply `κ_global = 0.50` to get `GF/W_AI,global(t)`.
4. Construct `χ_CN(t)` using `λ = 0.40` and the A800/H800 bandwidth table.
5. Build `GF/W_AI,China(t)`.
6. Validate trend co-movement against MLPerf Power over `2023–2025`.
7. Build `PUE_{p,t}` from a national anchor plus climate / hub adjustments.
8. Build `CI_{p,t}` from province-month electricity mix.
9. Compute `e^{IT}_{p,t}`, `e^{Site}_{p,t}`, and `CPC_{p,t}`.

---

## 11. Uncertainty and Monte Carlo

Use a lightweight Monte Carlo so the method remains transparent and reproducible.

### Suggested draws

- `s_mxp(t)`: empirical release dispersion, for example based on the release distribution or a fitted log-normal around the median
- `κ_global ~ N(0.50, 0.05)`, truncated to `[0.35, 0.70]`
- `λ ~ U[0.30, 0.50]`
- `β(t)`: deterministic by epoch; optional `±0.05` sensitivity if topology uncertainty matters
- `PUE_{p,t} ~ N(\bar{PUE}_{p,t}, 0.05)`, truncated to `[1.2, 1.8]`
- `CI_{p,t} ~ N(\bar{CI}_{p,t}, 0.10\cdot \bar{CI}_{p,t})`

### Reporting

- `10,000` simulations
- report median and `p5–p95` for:
  - `GF/W_{AI,China}(t)`
  - `e^{IT}_{p,t}`
  - `e^{Site}_{p,t}`
  - `CPC_{p,t}`

---

## 12. BIS / Export-Control Note

The `2023-10` BIS update shifts the regulatory framework away from the earlier focus on interconnect bandwidth alone and toward **performance density** and related thresholds.

For this note, the China adjustment is deliberately kept simple:

- use public NVLink bandwidth to define `β(t)`
- do not yet add a separate performance-density term

If the thesis later needs a richer China hardware-mix model, add a term such as `ψ(t)` for mix shifts across H800, H20, or other China-market SKUs. For now, keeping only the NVLink-based `χ_CN(t)` maximizes transparency and reproducibility.

---

## 13. Limitations

- HPL is not an AI benchmark.
- HPL-MxP is closer to AI-style math but still not the same as real frontier training.
- MLPerf Power validates trend co-movement, not level calibration.
- The China haircut is intentionally parsimonious and captures only one margin of hardware restriction.
- Province-month PUE remains partly modeled unless operator data are obtained.
- Province-month CI depends on the quality and frequency of generation-mix data.

---

## 14. Why This Is Defensible

- **Simple:** it starts from a long-run audited benchmark series.
- **Transparent:** every transformation is explicit and small in number.
- **China-specific:** the export-control adjustment is visible rather than hidden.
- **Auditable:** all inputs can be recomputed from public sources.
- **Falsifiable enough for practice:** the series can be checked against MLPerf Power trend behavior.

---

## 15. Practical Notes

- Monthly interpolation:
  - default to **step-hold**
  - optionally show smoothed variants as sensitivity
- Green500 frontier choice:
  - `P75` emphasizes best practice
  - `P50` captures a broader market-like benchmark
- MLPerf model coverage:
  - BERT and ResNet are the most stable early anchors
  - LLM entries become more useful only once coverage is thick enough

---

## 16. References (APA 7th; clickable links)

**BIS / export controls**  
Bureau of Industry and Security. (2023, October 25). *Implementation of Additional Export Controls: Certain Advanced Computing Items; Supercomputer and Semiconductor End Use* (Final Rule). https://www.federalregister.gov/documents/2023/10/25/2023-23055/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and  
Bureau of Industry and Security. (2024, December 5). *Updated public information on advanced computing export controls to the PRC.* https://www.bis.doc.gov/press-release/bis-updated-public-information-page-export-controls-imposed-advanced-computing-semiconductor  

**Green500 / HPL**  
TOP500. (2025, June). *The Green500 list*. https://top500.org/lists/green500/2025/06/  
Ge, R. (2007). *Power Measurement Tutorial for the Green500 List*. https://top500.org/files/green500/tutorial.pdf  

**HPL-MxP**  
HPL-MxP Team. (2023). *HPL-MxP Mixed-Precision Benchmark*. https://hpl-mxp.org/  
HPL-MxP Team. (2025). *Results (Speedups)*. https://hpl-mxp.org/results.md  
Tomov, S., et al. (2023). *HPL-MxP: Mixed-Precision Benchmark (SC'23 poster).* https://icl.utk.edu/files/print/2023/hpl-mxp-sc23.pdf  

**Tensor cores / mixed-precision efficiency**  
NVIDIA. (2019). *Using Tensor Cores for Mixed-Precision Scientific Computing*. https://developer.nvidia.com/blog/tensor-cores-mixed-precision-scientific-computing/  
Haidar, A., et al. (2020). *Mixed-precision iterative refinement using tensor cores on GPUs*. *Royal Society Open Science, 7*(12). https://pmc.ncbi.nlm.nih.gov/articles/PMC7735315/  
NVIDIA. (2020). *A100 Tensor Core GPU Architecture Whitepaper*. https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf  

**Interconnect bandwidth (global vs China SKUs)**  
NVIDIA. (2021). *A100 datasheet* (NVLink 600 GB/s). https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf  
Megware. (2023). *H100 datasheet* (NVLink 900 GB/s). https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf  
LenovoPress. (2023). *ThinkSystem NVIDIA H800 PCIe Gen5 GPUs* (NVLink 400 GB/s). https://lenovopress.lenovo.com/lp1814-thinksystem-nvidia-h800-pcie-gen5-gpu  
Reuters. (2022, November 8). *Nvidia offers A800 chip for China to meet export rules*. https://www.reuters.com/technology/exclusive-nvidia-offers-new-advanced-chip-china-that-meets-us-export-controls-2022-11-08/  

**MFU / utilization**  
NVIDIA Megatron-LM. (2025). *Repository* (MFU context). https://github.com/NVIDIA/Megatron-LM  
Dao, T., et al. (2023). *FlashAttention-2*. https://arxiv.org/abs/2307.08691  

**MLPerf Power**  
MLCommons. (n.d.). *Power measurement methodology*. https://docs.mlcommons.org/inference/power/  
Tschand, A., et al. (2024). *MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems* (arXiv:2410.12032). https://arxiv.org/abs/2410.12032  

**PUE / China policy**  
Gov.cn (State Council). (2024, July 24). *China sets green targets for data centres (PUE < 1.5 by 2025).* https://english.www.gov.cn/news/202407/24/content_WS66a0b167c6d0868f4e8e96ba.html  
RMI. (2024, November). *Powering the Data-Center Boom with Low-Carbon Solutions* (PUE about 1.48 in 2023). https://rmi.org/wp-content/uploads/dlm_uploads/2024/11/Powering_the_Data_Center_Boom_with_Low_Carbon_Solutions_report.pdf  

**Provincial mix / CI**  
NBS. *Energy and electricity tables (provincial).* https://data.stats.gov.cn/english/  
Ember. *Monthly Electricity Data*. https://ember-energy.org/data/monthly-electricity-data/  
CREA. *Regional analysis and reports (China).* https://energyandcleanair.org/  
