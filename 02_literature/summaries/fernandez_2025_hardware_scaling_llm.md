---
filename_stem: "fernandez_2025_hardware_scaling_llm"
citation: "Fernandez, J., Wehrstedt, L., Shamis, L., et al. (2025).** Efficient Hardware Scaling and Diminishing Returns in Large-Scale Training of Language Models. *Transactions on Machine Learning Research*. https://openreview.net/forum?id=p7jQEf3wlh"
first_author: "Fernandez"
year: 2025
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
note_status: "stub-pdf-read"
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

- _to fill during close read_

## Method & data

- _to fill during close read_

## Key quotes

- _page / quote_

## Relevance to EDWC thesis

- _how this paper supports specific claims / sections_

## Caveats / limitations

- _none noted in master file_

## Related papers in corpus

- _link sibling notes_
