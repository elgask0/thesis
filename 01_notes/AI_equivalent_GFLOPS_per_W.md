# AI‑Equivalent Energy Efficiency (GFLOPS/W) 2019–2025: Reproducible Method for Provincial Carbon‑per‑Compute (CPC) in China

**Purpose.** We want monthly **Carbon‑per‑Compute (CPC)** by province in China. Given provincial **carbon intensity** (CI, in tCO₂/MWh) and **PUE**, we need a defensible monthly series of **AI‑equivalent compute efficiency** in **GFLOPS/W (GF/W)** to convert electricity into **EF·h** and then into emissions:

$$
e^{IT}_{p,t} = \frac{1000}{\mathrm{GF/W}_{p,t}} \quad \text{(MWh per EF·h, IT layer)} \\
e^{Site}_{p,t} = e^{IT}_{p,t} \times \mathrm{PUE}_{p,t} \\
\mathrm{CPC}_{p,t} = \mathrm{CI}_{p,t} \times e^{Site}_{p,t} \quad (\mathrm{tCO_2/EF\cdot h})
$$

**What “AI‑equivalent” means.** Historic, audited efficiency is reported under **HPL FP64** (Green500), not modern AI workloads. We **bridge** from FP64 to mixed‑precision AI‑like math using the public **HPL‑MxP (HPL‑AI) speedup** and then apply a global **utilization realism** factor (MFU) and a **China interconnect haircut** (for A800/H800 epochs). The goal is an **auditable, replicable proxy** for AI‑class efficiency pre‑2023 that we can validate (trend‑wise) against **MLPerf Power** from 2023 onward.

---

## 1) Data (shape & where to get it)

### 1.1 Green500 (HPL FP64 efficiency)
- **What:** energy efficiency during HPL FP64, in **GF/W** (audited).
- **Where:** Green500 list (June/November editions). Keep top‑N rows to compute a robust frontier (options: median top‑10, or Q4 / P75 of all systems; sensitivity test both).

**Columns (example):**

| date       | system_id | vendor | cpu_gpu | HPL_GFlops_per_W | notes |
|------------|-----------|--------|---------|------------------|-------|
| 2019-06-01 | 1001      | ABC    | V100    | 18.2             | top10 |
| 2019-11-01 | 1203      | ABC    | V100    | 20.1             | top10 |
| 2020-06-01 | 1502      | DEF    | A100    | 29.8             | #1    |

### 1.2 HPL‑MxP (HPL‑AI) speedups
- **What:** per edition, **speedup** = $R_\mathrm{max}^{MxP}/R_\mathrm{max}^{FP64}$ per system; use the **median** speedup across leaders.
- **Why:** MxP engages tensor cores / lower precision typical of AI math.

**Columns (example):**

| date       | system_id | HPL_MxP_EF | HPL_FP64_EF | speedup_mxp | notes    |
|------------|-----------|------------|-------------|-------------|----------|
| 2020-06-01 | 1502      | 0.252      | 0.063       | 4.0         | Selene   |
| 2021-11-01 | 2001      | 1.411      | 0.149       | 9.5         | Summit   |
| 2024-11-01 | 3005      | 16.680     | 1.735       | 9.6         | ElCap    |

### 1.3 Interconnect & China‑specific SKUs
- **What:** NVLink per‑GPU bandwidth for global SKUs (A100/H100) vs China SKUs (A800/H800). Use to build a **China haircut** on AI efficiency for communication‑bound portions.

**Columns (example):**

| period              | cn_sku | bw_cn_gbps | ref_sku | bw_global_gbps | ratio_beta |
|---------------------|--------|------------|---------|----------------|------------|
| 2022-11..2023-10    | A800   | 400        | A100    | 600            | 0.667      |
| 2023-11..2025-12    | H800   | 400        | H100    | 900            | 0.444      |

### 1.4 MLPerf Power (validation only, 2023+)
- **What:** **samples_per_joule** (or tokens/J) per release for fixed datacenter inference benchmarks (Closed division), used to **validate trend**.
- **Columns (example):**

| release_date | system | division   | benchmark | scenario | samples_per_j | notes |
|--------------|--------|------------|-----------|----------|---------------|-------|
| 2023-04-05   | HGX    | datacenter | BERT-99   | offline  | 0.85          | v3.x  |
| 2024-03-27   | HGX    | datacenter | LLaMA2-70B| offline  | 0.92          | v4.x  |

### 1.5 PUE and provincial grid CI (for CPC)
- **PUE:** China policy targets **<1.5 by 2025**; sector reports show **~1.48 in 2023**. If operator data absent, build a monthly provincial path converging to target (add uncertainty ±0.1).  
- **CI:** Compute monthly provincial **tCO₂/MWh** from generation mix (NBS/CEC + Ember/CREA) and standard emission factors.

**Columns (example):**

| month   | province | coal | gas | hydro | wind | solar | nuclear | CI_tCO2_per_MWh |
|---------|----------|------|-----|-------|------|-------|---------|-----------------|
| 2024-01 | Jiangsu  | 0.65 | 0.06| 0.10  | 0.06 | 0.07  | 0.06    | 0.700           |
| 2024-01 | InnerMG  | 0.80 | 0.02| 0.05  | 0.07 | 0.04  | 0.02    | 0.800           |

---

## 2) Method (formulas)

### 2.1 FP64 baseline (monthly)
Compute a robust **frontier** per edition (median top‑10 or P75) and **linearly interpolate** to monthly:

$$
\overline{\mathrm{GF/W}}_{FP64}(t) = \operatorname{median}_{i \in \text{top10}} \ \mathrm{GF/W}_{i}(t)
$$

### 2.2 Mixed‑precision bridge
From HPL‑MxP:

$$
s_{mxp}(t) = \operatorname{median}_i \frac{R_{\mathrm{max},i}^{MxP}(t)}{R_{\mathrm{max},i}^{FP64}(t)}
$$

**Assumption A1 (proportionality):** MxP speedup approximately transfers **1:1** to **GF/W** at system level because HPL and HPL‑MxP both operate near constant power envelopes; tensor‑core acceleration raises throughput and reduces energy/op (supported by kernel/solver studies).

### 2.3 Global utilization realism
Take

$$
\kappa_{\mathrm{global}} = 0.50
$$

as central MFU‑style realism (literature: ~35–60% on large clusters after optimization). This **does not** double‑count China’s networking haircut below.

### 2.4 China interconnect haircut
Let $\lambda$ be the **communication‑bound share** (central 0.40; test 0.30–0.50). Let $\beta(t)$ be the **NVLink ratio** (China/global).

- A800 vs A100: $\beta = 400/600 = 0.667$ (2022‑11..2023‑10).  
- H800 vs H100: $\beta = 400/900 = 0.444$ (2023‑11..2025‑12).

Apply a linear slowdown on the comm‑bound slice:

$$
\kappa_{\mathrm{China}}(t) = 1 - \lambda \,(1 - \beta(t))
$$

### 2.5 Final series

$$
\mathrm{GF/W}_{AI,\mathrm{global}}(t) = \overline{\mathrm{GF/W}}_{FP64}(t) \cdot s_{mxp}(t) \cdot \kappa_{\mathrm{global}}
$$

$$
\mathrm{GF/W}_{AI,\mathrm{China}}(t) = \mathrm{GF/W}_{AI,\mathrm{global}}(t) \cdot \kappa_{\mathrm{China}}(t)
$$

Then compute CPC variables:

$$
e^{IT}_{p,t} = \frac{1000}{\mathrm{GF/W}_{AI,\mathrm{China}}(t)} \\
e^{Site}_{p,t} = e^{IT}_{p,t} \cdot \mathrm{PUE}_{p,t} \\
\mathrm{CPC}_{p,t} = \mathrm{CI}_{p,t} \cdot e^{Site}_{p,t}
$$

---

## 3) Validation (trend only) with MLPerf Power, 2023+

1. Filter **Inference/Datacenter/Closed** results with **power**. Use `samples_per_joule` or `tokens_per_joule`.  
2. Build a **top‑quartile** or median frontier per release and **interpolate** to monthly.  
3. Normalize both the MLPerf series and our $\mathrm{GF/W}_{AI}$ to **base‑100 at 2023‑06**.  
4. Compute Pearson/Spearman correlations (expect strong positive). No parameter calibration to MLPerf.

---

## 4) Uncertainty (simple Monte Carlo)

For each edition/month draw:

- $s_{mxp}(t) \sim$ Log‑Normal(median = speedup, GSD = 1.10).  
- $\kappa_{\mathrm{global}} \sim \text{Triangular}(0.40,0.50,0.60)$.  
- $\lambda \sim \text{Triangular}(0.30,0.40,0.50)$.  
- $\beta(t)$: deterministic by epoch; optionally add ±0.05.  
- $\mathrm{PUE}_{p,t} \sim \mathcal{N}(\bar{PUE},0.07)$ clipped [1.2,1.8].  
- $\mathrm{CI}_{p,t} \sim \mathcal{N}(\bar{CI},0.05\,\bar{CI})$.

Aggregate to monthlies; report median and P10–P90 for $\mathrm{GF/W}_{AI,\mathrm{China}}$, $e^{IT}$, $e^{Site}$, CPC.

---

## 5) Where to get PUE and CI

- **PUE:** China policy news and sector reports (target **<1.5 by 2025**, observed **~1.48 in 2023**). If provincial PUE is not published, construct a monthly path per province converging to target, with climate/hub adjustments and uncertainty.  
- **CI:** Provincial monthly generation mix from **NBS/CEC/Ember/CREA**; multiply by standard emission factors (coal ~0.95 tCO₂/MWh, gas ~0.40, others ~0).

---

## 6) Assumptions & limitations

- **A1 proportionality (MxP→GF/W)** is a first‑order approximation justified by tensor‑core literature and similar power envelopes; residuals are covered by uncertainty and trend validation.  
- **China haircut** models interconnect as the binding differentiator; if future SKUs change clocks/HBM, update $\beta(t)$ or add a compute ratio term.  
- **Validation** checks **co‑movement** only (no calibration).

---

## References (APA 7th; clickable links)

**BIS / export controls**  
Bureau of Industry and Security. (2023, October 25). *Implementation of Additional Export Controls: Certain Advanced Computing Items; Supercomputer and Semiconductor End Use* (Final Rule). Federal Register. https://www.federalregister.gov/documents/2023/10/25/2023-23055/implementation-of-additional-export-controls-certain-advanced-computing-items-supercomputer-and  
Bureau of Industry and Security. (2024, December 5). *Updated public information on advanced computing export controls to the PRC.* https://www.bis.doc.gov/press-release/bis-updated-public-information-page-export-controls-imposed-advanced-computing-semiconductor  

**Green500 / HPL**  
TOP500. (2025, June). *The Green500 list*. https://top500.org/lists/green500/2025/06/  
Ge, R. (2007). *Power Measurement Tutorial for the Green500 List*. https://top500.org/files/green500/tutorial.pdf  

**HPL‑MxP**  
HPL‑MxP Team. (2023). *HPL‑MxP Mixed‑Precision Benchmark*. https://hpl-mxp.org/  
HPL‑MxP Team. (2025). *Results (Speedups)*. https://hpl-mxp.org/results.md  
Tomov, S., et al. (2023). *HPL‑MxP: Mixed‑Precision Benchmark (SC’23 poster).* https://icl.utk.edu/files/print/2023/hpl-mxp-sc23.pdf  

**Tensor cores / mixed‑precision efficiency**  
NVIDIA. (2019). *Using Tensor Cores for Mixed‑Precision Scientific Computing*. https://developer.nvidia.com/blog/tensor-cores-mixed-precision-scientific-computing/  
Haidar, A., et al. (2020). *Mixed‑precision iterative refinement using tensor cores on GPUs*. Royal Society Open Science, 7(12). https://pmc.ncbi.nlm.nih.gov/articles/PMC7735315/  
NVIDIA. (2020). *A100 Tensor Core GPU Architecture Whitepaper*. https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf  

**Interconnect bandwidth (global vs China SKUs)**  
NVIDIA. (2021). *A100 datasheet* (NVLink 600 GB/s). https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf  
Megware (repack of NVIDIA). (2023). *H100 datasheet* (NVLink 900 GB/s). https://www.megware.com/fileadmin/user_upload/LandingPage%20NVIDIA/nvidia-h100-datasheet.pdf  
LenovoPress. (2023). *ThinkSystem NVIDIA H800 PCIe Gen5 GPUs* (NVLink 400 GB/s). https://lenovopress.lenovo.com/lp1814-thinksystem-nvidia-h800-pcie-gen5-gpu  
Reuters. (2022, Nov 8). *Nvidia offers A800 chip for China to meet export rules*. https://www.reuters.com/technology/exclusive-nvidia-offers-new-advanced-chip-china-that-meets-us-export-controls-2022-11-08/  

**MFU / utilization**  
NVIDIA Megatron‑LM. (2025). *Repository* (MFU context). https://github.com/NVIDIA/Megatron-LM  
Dao, T., et al. (2023). *FlashAttention‑2*. https://arxiv.org/abs/2307.08691  

**MLPerf Power**  
MLCommons. (n.d.). *Power measurement methodology*. https://docs.mlcommons.org/inference/power/  
Tschand, A., et al. (2024). *MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems* (arXiv:2410.12032). https://arxiv.org/abs/2410.12032  

**PUE / China policy**  
Gov.cn (State Council). (2024, Jul 24). *China sets green targets for data centres (PUE < 1.5 by 2025).* https://english.www.gov.cn/news/202407/24/content_WS66a0b167c6d0868f4e8e96ba.html  
RMI. (2024, Nov). *Powering the Data‑Center Boom with Low‑Carbon Solutions* (PUE ≈ 1.48 in 2023). https://rmi.org/wp-content/uploads/dlm_uploads/2024/11/Powering_the_Data_Center_Boom_with_Low_Carbon_Solutions_report.pdf  

**Provincial mix / CI**  
NBS. *Energy & electricity tables (provincial).* https://data.stats.gov.cn/english/  
Ember. *Monthly Electricity Data*. https://ember-energy.org/data/monthly-electricity-data/  
CREA. *Regional analysis & reports (China)*. https://energyandcleanair.org/

