---
filename_stem: "green_grid_2012_pue_wp49"
citation: "The Green Grid. (2012).** *PUE: A comprehensive examination of the metric* (White Paper 49). https://www.thegreengrid.org/en/resources/library-and-tools/237-WP%2349---PUE%3A-A-Comprehensive-Examination-of-the-Metric"
first_author: "The Green Grid"
year: "2012"
title: "*PUE: A comprehensive examination of the metric* (White Paper 49)"
venue: "The Green Grid. (2012)."
doi: ""
url: "https://www.thegreengrid.org/en/resources/library-and-tools/237-WP%2349---PUE%3A-A-Comprehensive-Examination-of-the-Metric"
stream: "Measurement"
subsection: "3.2 PUE and facility efficiency"
tags: ["PUE", "data-center-efficiency", "standards", "facility-efficiency", "measurement"]
proposal_sections: "§3.4.3 PUE construction; §3.2 variable definition; §2.3 standards."
cpc_component: "PUE / facility efficiency"
priority: "must-cite"
caveat: ""
zotero_key: "BL3UU85C"
pdf_local: "pdf/green_grid_2012_pue_wp49.pdf"
note_status: "upgraded-pdf-fallback-partial"
---

# *PUE: A comprehensive examination of the metric* (White Paper 49)

**Authors:** The Green Grid
**Year:** 2012
**Venue:** The Green Grid. (2012).
**DOI:** —
**Zotero:** [Open](zotero://select/library/items/BL3UU85C)
**Stream / subsection:** Measurement / 3.2 PUE and facility efficiency

## Role in proposal

Canonical practitioner reference for what PUE does and does not measure. Use it to define the metric cleanly, explain boundary discipline, and avoid overstating PUE as a full carbon metric.

## Use in proposal

§3.4.3 PUE construction; §3.2 variable definition; §2.3 standards.

## Abstract

Consolidated Green Grid white paper that standardizes PUE definition, measurement boundaries, reporting rules, and interpretation. It supersedes earlier Green Grid PUE guidance and is written as the main practitioner reference for implementation and reporting.

## Core argument / findings
- The paper asks how PUE should be defined, measured, and reported so that facilities can be compared without mixing inconsistent boundaries or estimation shortcuts.
- Its central conclusion is that PUE is useful only when the numerator and denominator are measured consistently at the facility level and accompanied by clear reporting conventions.
- The core metric is straightforward: `PUE = Total Facility Energy / IT Equipment Energy`. The white paper then shows why apparently simple comparisons can mislead when cooling, shared services, or mixed-use buildings are handled differently.
- A major conceptual move is to separate full-facility PUE from `partial PUE (pPUE)` when operators cannot measure all facility energy inputs. That matters for the thesis because PUE is a facility-efficiency input to CPC, not a stand-alone emissions measure.

## Method & data
- Paper type: standards / practitioner white paper.
- It is not an empirical causal paper. It consolidates prior Green Grid guidance into a single reference covering definition, measurement levels, component classification, reporting rules, and pPUE.
- The document is organized around implementation logic rather than a sample or dataset: what counts as total facility energy, what counts as IT equipment energy, how mixed-use buildings should be handled, and what must be disclosed when reporting results.

## Key quotes
- p. 3: "Power usage effectiveness (PUETM) has become the industry-preferred metric for measuring infrastructure energy efficiency for data centers."
- p. 3: "The PUE metric is an end-user tool that helps boost energy efficiency in data center operations."
- Page number not reliably recovered from the local extraction for the formula figure; verify in the PDF before direct citation: "PUE = Total Facility Energy / IT Equipment Energy."

## Relevance to EDWC thesis
- Supports the proposal's definition of facility efficiency in the CPC build. PUE belongs in the denominator-side translation from electricity use to useful compute, not as a proxy for carbon intensity by itself.
- Proposal placement: §3.4.3 PUE construction; §3.2 variable definition; §2.3 standards.
- Most relevant use within the proposal: literature review, empirical strategy, CPC / measurement logic.

## Caveats / limitations
- This is a standards document rather than peer-reviewed causal evidence.
- PUE captures facility overhead relative to IT load; it does not identify grid carbon intensity, hardware embodied emissions, or useful compute output.
- The local MinerU parse covered only the first 40 pages, but the sections needed for metric definition and reporting logic were recoverable from the PDF.

## Related papers in corpus
- [yuventi_2013_pue_critique.md](yuventi_2013_pue_critique.md): direct critique of how PUE can be misused or overinterpreted.
- [eehpc_2015_green500_methodology.md](eehpc_2015_green500_methodology.md): benchmark methodology for energy efficiency at the compute-system level rather than the facility level.
- [dongarra_luszczek_2026_hpl_mxp.md](dongarra_luszczek_2026_hpl_mxp.md): benchmark-side complement for turning electricity into compute-oriented efficiency metrics.
- [caict_2024_green_computing_report.md](caict_2024_green_computing_report.md): Chinese institutional source using PUE within a broader green-computing framework.
