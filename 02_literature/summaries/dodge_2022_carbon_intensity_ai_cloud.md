---
filename_stem: "dodge_2022_carbon_intensity_ai_cloud"
citation: "Dodge, J., Prewitt, T., Tachet des Combes, R., et al. (2022).** Measuring the carbon intensity of AI in cloud instances. *FAccT '22*, 1877–1894. https://doi.org/10.1145/3531146.3533234"
first_author: "Dodge"
year: "2022"
title: "Measuring the carbon intensity of AI in cloud instances"
venue: "Dodge, J., Prewitt, T., Tachet des Combes, R., et al. (2022)."
doi: "10.1145/3531146.3533234"
url: "https://doi.org/10.1145/3531146.3533234"
stream: "Outcome"
subsection: "1.2 AI-specific carbon accounting"
tags: ["AI-carbon", "marginal-emissions", "CPC-framework", "outcome"]
proposal_sections: "§2.1 outcome motivation."
cpc_component: ""
priority: "conditional"
caveat: ""
zotero_key: "9AIKZ29M"
pdf_local: "pdf/dodge_2022_carbon_intensity_ai_cloud.pdf"
note_status: "upgraded-mineru-full"
---

# Measuring the carbon intensity of AI in cloud instances

**Authors:** Dodge
**Year:** 2022
**Venue:** Dodge, J., Prewitt, T., Tachet des Combes, R., et al. (2022).
**DOI:** [10.1145/3531146.3533234](https://doi.org/10.1145/3531146.3533234)
**Zotero:** [Open](zotero://select/library/items/9AIKZ29M)
**Stream / subsection:** Outcome / 1.2 AI-specific carbon accounting

## Role in proposal

Proposes a framework to measure operational software carbon intensity using location- and time-specific marginal emissions data. Finds that choosing cloud region delivers the largest operational emissions reductions. Methodological analogue for CPC translation: why relocation matters for emissions conditional on grid.

## Use in proposal

§2.1 outcome motivation.

## Abstract

The advent of cloud computing has provided people around the world with unprecedented access to computational power and en- abled rapid growth in technologies such as machine learning, the computational demands of which incur a high energy cost and a commensurate carbon footprint. As a result, recent scholarship has called for better estimates of the greenhouse gas impact of AI: data scientists today do not have easy or reliable access to measurements of this information, which precludes development of actionable tac- tics. We argue that cloud providers presenting information about software carbon intensity to users is a fundamental stepping stone towards minimizing emissions. In this paper, we provide a framework for measuring software carbon intensity, and propose to measure operational carbon emis- sions by using location-based and time-specific marginal emissions data per energy unit. We provide measurements of operational soft- ware carbon intensity for a set of modern models covering natural language processing and computer vision applications, and a wide range of model sizes, including pretraining of a 6.1 billion param- eter language model. We then evaluate a suite of approaches for reducing emissions on the Microsoft Azure cloud compute platform: using cloud instances in different geographic regions, using cloud instances at different times of day, and dynamically pausing cloud instances when the marginal carbon intensity is above a certain This work is licensed under a Creative Commons Attribution International 4.0 License. FAccT ’22, June 21–24, 2022, Seoul, Republic of Korea © 2022 Copyright held by the owner/author(s). ACM ISBN 978-1-4503-9352-2/22/06. https://doi.org/10.1145/3531146.3533234 threshold. We confirm previous results that the geographic region 

## Core argument / findings
- Proposes a framework to measure operational software carbon intensity using location- and time-specific marginal emissions data. Finds that choosing cloud region delivers the largest operational emissions reductions. Methodological analogue for CPC translation: why relocation matters for emissions conditional on grid.
- We argue that cloud providers presenting information about software carbon intensity to users is a fundamental stepping stone towards minimizing emissions.
- As a result, recent scholarship has called for better estimates of the greenhouse gas impact of AI: data scientists today do not have easy or reliable access to measurements of this information, which precludes development of actionable tactics.
- We provide measurements of operational software carbon intensity for a set of modern models covering natural language processing and computer vision applications, and a wide range of model sizes, including pretraining of a 6.1 billion parameter language model.

## Method & data
- Paper type: empirical paper.
- Parsed coverage used here: full document (18 pages).
- As a result, recent scholarship has called for better estimates of the greenhouse gas impact of AI: data scientists today do not have easy or reliable access to measurements of this information, which precludes development of actionable tactics.
- In this paper, we provide a framework for measuring software carbon intensity, and propose to measure operational carbon emissions by using location-based and time-specific marginal emissions data per energy unit.
- We confirm previous results that the geographic region of the data center plays a significant role in the carbon intensity for a given cloud instance, and find that choosing an appropriate region can have the largest operational emissions reduction impact.

## Key quotes
- p. 1: "CO2, emissions, cloud, carbon intensity, carbon awareness, grid"
- p. 3: "As expected the GPU accounts for almost 3/4 of electricity consumption."
- p. 6: "During the day, a region may have a higher mix of renewable energy or fossil-fuel based source [6]."

## Relevance to EDWC thesis
- Proposes a framework to measure operational software carbon intensity using location- and time-specific marginal emissions data. Finds that choosing cloud region delivers the largest operational emissions reductions. Methodological analogue for CPC translation: why relocation matters for emissions conditional on grid.
- Proposal placement: §2.1 outcome motivation.
- Most relevant use within the proposal: literature review.

## Caveats / limitations
- No major citation-use caveat beyond the paper's own scope is obvious from the current parse.

## Related papers in corpus
- [luccioni_2023_bloom_carbon_footprint.md](luccioni_2023_bloom_carbon_footprint.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [patterson_2021_carbon_nn_training.md](patterson_2021_carbon_nn_training.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [patterson_2022_ml_carbon_plateau.md](patterson_2022_ml_carbon_plateau.md): same subsection; same stream; shared tags: AI-carbon, outcome.
- [greenpeace_2021_china_5g_dc_outlook.md](greenpeace_2021_china_5g_dc_outlook.md): same stream; shared tags: outcome.
