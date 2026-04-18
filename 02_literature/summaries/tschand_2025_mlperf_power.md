---
filename_stem: "tschand_2025_mlperf_power"
citation: "Tschand, A., Rajan, A. T. R., Idgunji, S., et al. (2025).** MLPerf Power: Benchmarking the energy efficiency of machine learning systems from microwatts to megawatts for sustainable AI. *2025 IEEE HPCA*, 1201–1216. https://arxiv.org/abs/2410.12032"
first_author: "Tschand"
year: "2025"
title: "MLPerf Power: Benchmarking the energy efficiency of machine learning systems from microwatts to megawatts for sustainable AI"
venue: "Tschand, A., Rajan, A. T. R., Idgunji, S., et al. (2025)."
doi: ""
url: "https://arxiv.org/abs/2410.12032"
stream: "Measurement"
subsection: "3.3 Compute efficiency benchmarks (GF/W)"
tags: ["MLPerf-Power", "AI-efficiency", "system-power", "benchmark", "measurement"]
proposal_sections: "§2.3 ML-specific benchmarking; §3.4.3 GF/W construction."
cpc_component: "Compute efficiency (GF/W)"
priority: "strong-include"
caveat: ""
zotero_key: "YVE7KXKH"
pdf_local: "pdf/tschand_2025_mlperf_power.pdf"
note_status: "upgraded-mineru-full"
---

# MLPerf Power: Benchmarking the energy efficiency of machine learning systems from microwatts to megawatts for sustainable AI

**Authors:** Tschand
**Year:** 2025
**Venue:** Tschand, A., Rajan, A. T. R., Idgunji, S., et al. (2025).
**DOI:** —
**Zotero:** [Open](zotero://select/library/items/YVE7KXKH)
**Stream / subsection:** Measurement / 3.3 Compute efficiency benchmarks (GF/W)

## Role in proposal

ML-specific energy-efficiency benchmarking at system level; emphasizes reproducible wall-power measurement and comparability across hardware classes. Validates the broader move from peak specs to benchmarked, workload-relevant efficiency measures. Cite narrowly for ML-specific benchmarking.

## Use in proposal

§2.3 ML-specific benchmarking; §3.4.3 GF/W construction.

## Abstract

2025 IEEE International Symposium on High-Performance Computer Architecture (HPCA) MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems from µWatts to MWatts for Sustainable AI Arya Tschand1∗Arun Tejusve Raghunath Rajan2∗Sachin Idgunji3∗Anirban Ghosh3 Jeremy Holleman4 Csaba Kiraly5 Pawan Ambalkar6 Ritika Borkar3 Ramesh Chukka7 Trevor Cockrell6 Oliver Curtis8 Grigori Fursin9 Miro Hodak10 Hiwot Kassa2 Anton Lokhmotov11 Dejan Miskovic3 Yuechao Pan12 Manu Prasad Manmathan7 Liz Raymond6 Tom St. John13 Arjun Suresh14 Rowan Taubitz8 Sean Zhan8 Scott Wasson15 David Kanter15 Vijay Janapa Reddi1 ∗Equal contribution 1Harvard University 2Meta 3NVIDIA 4UNC Charlotte / Syntiant 5Codex 6Dell 7Intel 8SMC 9FlexAI / cTuning 10AMD 11KRAI 12Google 13Decompute 14GATE Overflow 15MLCommons Abstract—Rapid adoption of machine learning (ML) technolo- gies has led to a surge in power consumption across diverse systems, from tiny IoT devices to massive datacenter clusters. Benchmarking the energy efficiency of these systems is crucial for optimization, but presents novel challenges due to the variety of hardware platforms, workload characteristics, and system-level interactions. This paper introduces MLPerf® Power, a compre- hensive benchmarking methodology with capabilities to evaluate the energy efficiency of ML systems at power levels ranging from microwatts to megawatts. Developed by a consortium of industry professionals from more than 20 organizations, coupled with insights from academia, MLPerf Power establishes rules and best practices to ensure comparability across diverse architectures. We use representative workloads from the MLPerf benchmark suite to collect 1,841 reproducible measurements from 60 systems across the entire range of ML deployment scales. Our anal

## Core argument / findings
- ML-specific energy-efficiency benchmarking at system level; emphasizes reproducible wall-power measurement and comparability across hardware classes. Validates the broader move from peak specs to benchmarked, workload-relevant efficiency measures. Cite narrowly for ML-specific benchmarking.
- We use representative workloads from the MLPerf benchmark suite to collect 1,841 reproducible measurements from 60 systems across the entire range of ML deployment scales.
- This paper introduces MLPerf® Power, a comprehensive benchmarking methodology with capabilities to evaluate the energy efficiency of ML systems at power levels ranging from microwatts to megawatts.
- Benchmarking the energy efficiency of these systems is crucial for optimization, but presents novel challenges due to the variety of hardware platforms, workload characteristics, and system-level interactions.

## Method & data
- Paper type: standard or benchmark methodology.
- Parsed coverage used here: full document (16 pages).
- —Rapid adoption of machine learning (ML) technologies has led to a surge in power consumption across diverse systems, from tiny IoT devices to massive datacenter clusters.
- We use representative workloads from the MLPerf benchmark suite to collect 1,841 reproducible measurements from 60 systems across the entire range of ML deployment scales.
- This paper introduces MLPerf® Power, a comprehensive benchmarking methodology with capabilities to evaluate the energy efficiency of ML systems at power levels ranging from microwatts to megawatts.

## Key quotes
- p. 4: "Mobile MLPerf Mobile benchmarks the performance of mobile ML systems [32]."
- p. 11: "Several MLPerf workloads have separate benchmarks set at 99% and 99.9% accuracy."
- p. 10: "In MLPerf Inference v4.0, each of the two LLM benchmarks uses a different metric."

## Relevance to EDWC thesis
- ML-specific energy-efficiency benchmarking at system level; emphasizes reproducible wall-power measurement and comparability across hardware classes. Validates the broader move from peak specs to benchmarked, workload-relevant efficiency measures. Cite narrowly for ML-specific benchmarking.
- Proposal placement: §2.3 ML-specific benchmarking; §3.4.3 GF/W construction.
- Most relevant use within the proposal: literature review, empirical strategy, CPC / measurement logic.

## Caveats / limitations
- This is an institutional or technical source rather than peer-reviewed causal evidence.

## Related papers in corpus
- [dongarra_luszczek_2026_hpl_mxp.md](dongarra_luszczek_2026_hpl_mxp.md): same subsection; same stream; shared tags: measurement.
- [eehpc_2015_green500_methodology.md](eehpc_2015_green500_methodology.md): same subsection; same stream; shared tags: measurement.
- [fernandez_2025_hardware_scaling_llm.md](fernandez_2025_hardware_scaling_llm.md): same subsection; same stream; shared tags: measurement.
- [caict_2023_computing_power_index.md](caict_2023_computing_power_index.md): same stream; shared tags: measurement.
