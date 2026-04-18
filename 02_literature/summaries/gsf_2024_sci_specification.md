---
filename_stem: "gsf_2024_sci_specification"
citation: "Green Software Foundation. (2024).** *Software Carbon Intensity (SCI) specification* (ISO/IEC 21031:2024). https://sci.greensoftware.foundation/"
first_author: "Green Software Foundation"
year: "2024"
title: "*Software Carbon Intensity (SCI) specification* (ISO/IEC 21031:2024)"
venue: "Green Software Foundation. (2024)."
doi: ""
url: "https://sci.greensoftware.foundation/"
stream: "Measurement"
subsection: "3.1 Carbon-accounting frameworks for compute"
tags: ["SCI", "carbon-accounting", "functional-unit", "standards", "measurement"]
proposal_sections: "§2.3 standards reference; §3.4.3 CPC structure; §4 contribution framing."
cpc_component: "Accounting framework"
priority: "must-cite"
caveat: ""
zotero_key: "M7MWJU6L"
pdf_local: "pdf/gsf_2024_sci_specification.pdf"
note_status: "upgraded-pdf-fallback-parse_poor"
---

# *Software Carbon Intensity (SCI) specification* (ISO/IEC 21031:2024)

**Authors:** Green Software Foundation
**Year:** 2024
**Venue:** Green Software Foundation. (2024).
**DOI:** —
**Zotero:** [Open](zotero://select/library/items/M7MWJU6L)
**Stream / subsection:** Measurement / 3.1 Carbon-accounting frameworks for compute

## Role in proposal

Formal rate-based accounting standard: operational + embodied emissions normalized by a functional unit. Directly parallel to CPC's structure (CO₂ per exaflop-hour replacing SCI's software service unit).

## Use in proposal

§2.3 standards reference; §3.4.3 CPC structure; §4 contribution framing.

## Abstract

Version 1.1.0 technical specification defining Software Carbon Intensity as a rate that combines operational and embodied emissions per functional unit of software service. The standard is designed for measurement and design comparison, not for claiming net-zero through offsets.

## Core argument / findings
- The specification asks how software emissions should be expressed as a comparable rate rather than as a raw total.
- Its central move is to define `SCI = (O + M) per R`, where operational emissions `O` come from energy use times grid carbon intensity and embodied emissions `M` allocate hardware manufacturing emissions over time and resource share.
- The standard treats energy efficiency, hardware efficiency, and carbon awareness as the three main ways to reduce the score. It explicitly rejects offsetting as a way to lower SCI.
- For the thesis, the important contribution is structural: SCI is a formal template for a rate-based metric that normalizes emissions by a functional unit. CPC follows the same logic but swaps the software service unit for compute output.

## Method & data
- Paper type: standard / accounting methodology.
- This is not an empirical study. It defines a reporting framework, the required variables, and the decomposition of emissions into operational and embodied components.
- Operational emissions are calculated as `O = E * I`. Embodied emissions are allocated as `M = TE * TS * RS`, then normalized by the functional unit `R`.
- The document allows modeled inputs when direct measurement is unavailable, but the preferred approach is granular real-world data.

## Key quotes
- Page numbers were not reliably recoverable from the local PDF extraction, so any direct quotation should be checked against the source PDF or website before citation.
- "SCI is a rate; carbon emissions per one unit of `R`."
- "Reducing an SCI score is only possible through the elimination of emissions."
- "Carbon Awareness: Actions taken to time- or region-shift software computation to take advantage of cleaner ... electricity."

## Relevance to EDWC thesis
- Formal accounting analogue for CPC. It shows how to turn emissions into a rate by dividing by a functional unit and by keeping operational and embodied components explicit.
- Proposal placement: §2.3 standards reference; §3.4.3 CPC structure; §4 contribution framing.
- Most relevant use within the proposal: literature review, empirical strategy, CPC / measurement logic.

## Caveats / limitations
- This is a standards document rather than peer-reviewed causal evidence.
- SCI is written for software services, not for province-level compute infrastructure. The thesis can borrow its accounting logic, but not its functional unit directly.
- The local PDF extraction was poor and page numbering was unreliable, so any future direct quotation needs source checking.

## Related papers in corpus
- [gupta_2022_chasing_carbon.md](gupta_2022_chasing_carbon.md): closest conceptual neighbor on emissions accounting choices for compute workloads.
- [radovanovic_2023_carbon_aware_computing.md](radovanovic_2023_carbon_aware_computing.md): direct complement on time- and location-shifting to lower operational emissions.
- [freitag_2021_ict_climate_critique.md](freitag_2021_ict_climate_critique.md): broad systems-level critique that cautions against narrow or incomplete carbon metrics.
- [caict_2023_computing_power_index.md](caict_2023_computing_power_index.md): institutional bridge from general carbon-accounting logic to the Chinese compute-capacity setting.
