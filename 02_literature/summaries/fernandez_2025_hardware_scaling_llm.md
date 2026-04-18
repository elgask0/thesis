---
filename_stem: "fernandez_2025_hardware_scaling_llm"
citation: "Fernandez, J., Wehrstedt, L., Shamis, L., et al. (2025).** Efficient Hardware Scaling and Diminishing Returns in Large-Scale Training of Language Models. *Transactions on Machine Learning Research*. https://openreview.net/forum?id=p7jQEf3wlh"
first_author: "Fernandez"
year: "2025"
title: "Efficient Hardware Scaling and Diminishing Returns in Large-Scale Training of Language Models"
venue: "Fernandez, J., Wehrstedt, L., Shamis, L., et al. (2025)."
doi: ""
url: "https://openreview.net/forum?id=p7jQEf3wlh"
stream: "Measurement"
subsection: "3.3 Compute efficiency benchmarks (GF/W)"
tags: ["MFU", "interconnect", "distributed-training", "realized-efficiency", "measurement"]
proposal_sections: "§3.4.3 MFU / interconnect adjustment; §3.2 variable definition."
cpc_component: "Compute efficiency (GF/W)"
priority: "strong-include"
caveat: ""
zotero_key: "BAH2WYRQ"
pdf_local: "pdf/fernandez_2025_hardware_scaling_llm.pdf"
note_status: "upgraded-mineru-full"
---

# Efficient Hardware Scaling and Diminishing Returns in Large-Scale Training of Language Models

**Authors:** Fernandez
**Year:** 2025
**Venue:** Fernandez, J., Wehrstedt, L., Shamis, L., et al. (2025).
**DOI:** —
**Zotero:** [Open](zotero://select/library/items/BAH2WYRQ)
**Stream / subsection:** Measurement / 3.3 Compute efficiency benchmarks (GF/W)

## Role in proposal

Shows that realized training efficiency declines with scale as communication overhead rises and MFU falls, even when nominal accelerator capability increases. Best justification for the MFU term and the China interconnect adjustment (A800/H800 bandwidth haircut) in the GF/W construction. Cite narrowly.

## Use in proposal

§3.4.3 MFU / interconnect adjustment; §3.2 variable definition.

## Abstract

To train the exceedingly large neural networks required in modern applications, such as large language models (LLMs), model training is distributed across tens of thousands of hardware accelerators (e.g. GPUs), requiring orchestration of computation and communication across large computing clusters. In this work, we demonstrate that careful consideration of hardware configuration and parallelization strategy is critical for effective (i.e. compute- and cost-efficient) scaling of model training. We conduct an extensive empirical study of the performance of large-scale LLM training workloads across model size, hardware configurations, and distributed parallelization strategies with current best practices. In experiments with model sizes up to 70B parameters and utilizing up to 2048 H100 GPUs, we demonstrate that: (1) Naive scale out with Fully Sharded Data Parallelism (FSDP) incurs communication overhead which leads parallelization strategies previously thought to be sub-optimal to in fact become preferable; and (2) scaling the total number of accelerators for training quickly yields diminishing returns even when hardware and parallelization strategies are properly optimized, implying poor marginal performance per additional unit of power or GPU-hour.

## Core argument / findings
- Shows that realized training efficiency declines with scale as communication overhead rises and MFU falls, even when nominal accelerator capability increases. Best justification for the MFU term and the China interconnect adjustment (A800/H800 bandwidth haircut) in the GF/W construction. Cite narrowly.
- In this work, we demonstrate that careful consideration of hardware configuration and parallelization strategy is critical for effective (i.e. compute- and cost-efficient) scaling of model training.
- In experiments with model sizes up to 70B parameters and utilizing up to 2048 H100 GPUs, we demonstrate that: (1) Naive scale out with Fully Sharded Data Parallelism (FSDP) incurs communication overhead which leads parallelization strategies previously thought to be sub-optimal to in fact become preferable; and (2) scaling the total number of accelerators for training quickly yields diminishing returns even when hardware and parallelization strategies are properly optimized, implying poor marginal performance per additional unit of power or GPU-hour.
- GPUs), requiring orchestration of computation and communication across large computing clusters.

## Method & data
- Paper type: measurement or accounting paper.
- Parsed coverage used here: full document (20 pages).
- In experiments with model sizes up to 70B parameters and utilizing up to 2048 H100 GPUs, we demonstrate that: (1) Naive scale out with Fully Sharded Data Parallelism (FSDP) incurs communication overhead which leads parallelization strategies previously thought to be sub-optimal to in fact become preferable; and (2) scaling the total number of accelerators for training quickly yields diminishing returns even when hardware and parallelization strategies are properly optimized, implying poor marginal performance per additional unit of power or GPU-hour.
- GPUs), requiring orchestration of computation and communication across large computing clusters.
- In this work, we demonstrate that careful consideration of hardware configuration and parallelization strategy is critical for effective (i.e. compute- and cost-efficient) scaling of model training.

## Key quotes
- p. 4: "In Figure 2, we empirically benchmark the AllReduce and AllGather operations performance with the NCCL library."
- p. 5: "We compute the estimated per-device words per second (WPS) and the global words per second across all devices."
- p. 16: "In our investigation across computing platforms, we primarily consider variations in the speed of compute (i.e."

## Relevance to EDWC thesis
- Shows that realized training efficiency declines with scale as communication overhead rises and MFU falls, even when nominal accelerator capability increases. Best justification for the MFU term and the China interconnect adjustment (A800/H800 bandwidth haircut) in the GF/W construction. Cite narrowly.
- Proposal placement: §3.4.3 MFU / interconnect adjustment; §3.2 variable definition.
- Most relevant use within the proposal: empirical strategy, CPC / measurement logic.

## Caveats / limitations
- No major citation-use caveat beyond the paper's own scope is obvious from the current parse.

## Related papers in corpus
- [dongarra_luszczek_2026_hpl_mxp.md](dongarra_luszczek_2026_hpl_mxp.md): same subsection; same stream; shared tags: measurement.
- [eehpc_2015_green500_methodology.md](eehpc_2015_green500_methodology.md): same subsection; same stream; shared tags: measurement.
- [tschand_2025_mlperf_power.md](tschand_2025_mlperf_power.md): same subsection; same stream; shared tags: measurement.
- [caict_2023_computing_power_index.md](caict_2023_computing_power_index.md): same stream; shared tags: measurement.
