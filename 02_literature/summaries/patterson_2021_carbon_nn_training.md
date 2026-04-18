---
filename_stem: "patterson_2021_carbon_nn_training"
citation: "Patterson, D., Gonzalez, J., Le, Q. V., Liang, C., Munguia, L. M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2021).** Carbon emissions and large neural network training. arXiv:2104.10350. https://doi.org/10.48550/arXiv.2104.10350"
first_author: "Patterson"
year: "2021"
title: "Carbon emissions and large neural network training"
venue: "Patterson, D., Gonzalez, J., Le, Q. V., Liang, C., Munguia, L. M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2021)."
doi: "10.48550/arXiv.2104.10350"
url: "https://doi.org/10.48550/arXiv.2104.10350"
stream: "Outcome"
subsection: "1.2 AI-specific carbon accounting"
tags: ["AI-carbon", "training", "CPC-logic", "outcome"]
proposal_sections: "§1.1.1 background; §2.1 outcome motivation."
cpc_component: ""
priority: "conditional"
caveat: ""
zotero_key: "QVN2FX3N"
pdf_local: "pdf/patterson_2021_carbon_nn_training.pdf"
note_status: "upgraded-mineru-full"
---

# Carbon emissions and large neural network training

**Authors:** Patterson et al.
**Year:** 2021
**Venue:** Patterson, D., Gonzalez, J., Le, Q. V., Liang, C., Munguia, L. M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2021).
**DOI:** [10.48550/arXiv.2104.10350](https://doi.org/10.48550/arXiv.2104.10350)
**Zotero:** [Open](zotero://select/library/items/QVN2FX3N)
**Stream / subsection:** Outcome / 1.2 AI-specific carbon accounting

## Role in proposal

Quantifies energy and CO₂ for training frontier models (T5, GPT-3, etc.) and shows footprint changes substantially with hardware, DC efficiency, and grid-carbon assumptions. Supports the CPC logic that "compute → electricity → emissions" is not a constant mapping — EDWC-induced relocation changes emissions conditional on provincial grid and facility characteristics.

## Use in proposal

§1.1.1 background; §2.1 outcome motivation.

## Abstract

Abstract: The computation demand for machine learning (ML) has grown rapidly recently, which comes with a number of costs. Estimating the energy cost helps measure its environmental impact and finding greener strategies, yet it is challenging without detailed information .

## Core argument / findings
- Quantifies energy and CO₂ for training frontier models (T5, GPT-3, etc.) and shows footprint changes substantially with hardware, DC efficiency, and grid-carbon assumptions. Supports the CPC logic that "compute → electricity → emissions" is not a constant mapping — EDWC-induced relocation changes emissions conditional on provincial grid and facility characteristics.
- We calculate the energy use and carbon footprint of several recent large models—T5, Meena, GShard, Switch Transformer, and GPT-3—and refine earlier estimates for the neural architecture search that found Evolved Transformer.
- Estimating the energy cost helps measure its environmental impact and finding greener strategies, yet it is challenging without detailed information.
- Geographic location matters for ML workload scheduling since the fraction of carbon-free energy and resulting CO2e vary \~5X-10X, even within the same country and the same organization.

## Method & data
- Paper type: empirical paper.
- Parsed coverage used here: full document (22 pages).
- Remarkably, the choice of DNN, datacenter, and processor can reduce the carbon footprint up to \~100-1000X.
- Specific datacenter infrastructure matters, as Cloud datacenters can be \~1.4-2X more energy efficient than typical datacenters, and the ML-oriented accelerators inside them can be \~2-5X more effective than off-the-shelf systems.
- We highlight the following opportunities to improve energy efficiency and CO2 equivalent emissions (CO2e): ● Large but sparsely activated DNNs can consume <1/10th the energy of large, dense DNNs without sacrificing accuracy despite using as many or even more parameters.

## Key quotes
- p. 5: "Energy Usage and CO2e Emissions of Five Recent Large NLP Models"
- p. 11: "4.4 Standard ML algorithmic techniques can improve energy efficiency"
- p. 5: "If cloud providers don’t share PUE, use the US average PUE as in [Str19]."

## Relevance to EDWC thesis
- Quantifies energy and CO₂ for training frontier models (T5, GPT-3, etc.) and shows footprint changes substantially with hardware, DC efficiency, and grid-carbon assumptions. Supports the CPC logic that "compute → electricity → emissions" is not a constant mapping — EDWC-induced relocation changes emissions conditional on provincial grid and facility characteristics.
- Proposal placement: §1.1.1 background; §2.1 outcome motivation.
- Most relevant use within the proposal: background, literature review.

## Caveats / limitations
- No major citation-use caveat beyond the paper's own scope is obvious from the current parse.

## Related papers in corpus
- [dodge_2022_carbon_intensity_ai_cloud.md](dodge_2022_carbon_intensity_ai_cloud.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [luccioni_2023_bloom_carbon_footprint.md](luccioni_2023_bloom_carbon_footprint.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [patterson_2022_ml_carbon_plateau.md](patterson_2022_ml_carbon_plateau.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [greenpeace_2021_china_5g_dc_outlook.md](greenpeace_2021_china_5g_dc_outlook.md): same stream; shared tags: outcome.
