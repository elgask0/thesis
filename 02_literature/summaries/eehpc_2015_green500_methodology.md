---
filename_stem: "eehpc_2015_green500_methodology"
citation: "Energy Efficient High Performance Computing Working Group. (2015).** *Energy Efficient High Performance Computing Power Measurement Methodology* (Version 2.0 RC 1.0). TOP500/Green500. https://www.top500.org/static/media/uploads/methodology-2.0rc1.pdf"
first_author: "Energy Efficient High Performance Computing Working Group"
year: "2015"
title: "*Energy Efficient High Performance Computing Power Measurement Methodology* (Version 2"
venue: "Energy Efficient High Performance Computing Working Group. (2015)."
doi: ""
url: "https://www.top500.org/static/media/uploads/methodology-2.0rc1.pdf"
stream: "Measurement"
subsection: "3.3 Compute efficiency benchmarks (GF/W)"
tags: ["Green500", "GF-W", "benchmark-methodology", "power-measurement", "measurement"]
proposal_sections: "§3.4.3 GF/W construction; §3.2 variable definition; §2.3 benchmarking."
cpc_component: "Compute efficiency (GF/W)"
priority: "strong-include"
caveat: ""
zotero_key: ""
pdf_local: "pdf/eehpc_2015_green500_methodology.pdf"
note_status: "upgraded-mineru-full"
---

# *Energy Efficient High Performance Computing Power Measurement Methodology* (Version 2

**Authors:** Energy Efficient High Performance Computing Working Group
**Year:** 2015
**Venue:** Energy Efficient High Performance Computing Working Group. (2015).
**DOI:** —
**Zotero:** not in Zotero
**Stream / subsection:** Measurement / 3.3 Compute efficiency benchmarks (GF/W)

## Role in proposal

Formalizes how system power under benchmark load is measured for Green500, including quality levels, instrumentation boundaries, and full-run reporting. Essential to justify using Green500-style audited performance-per-watt data as the GF/W base in CPC.

## Use in proposal

§3.4.3 GF/W construction; §3.2 variable definition; §2.3 benchmarking.

## Abstract

Contents 1 Introduction 6 2 Checklist 7 Quality Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 Power Measurement Locations . . . . . . . . . . . . . . . . . . . . . . . . 7 Measuring Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 Workload Requirement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 Level 1 Power Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . 8 Level 2 Power Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . 8 Level 3 Power Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . 9 Idle Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 Included Subsystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 Tunable Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 Environmental Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 3 Reporting Power Values (Detailed Information) 12 3.1 Measuring Device Terminology and Speciﬁcations . . . . . . . . . . . . . . 12 3.1.1 Accuracy Requirements . . . . . . . . . . . . . . . . . . . . . . . . 12 3.1.2 Sampling and Power Readings . . . . . . . . . . . . . . . . . . . . 13 3.1.3 Power-Averaged and Total Energy Measurements . . . . . . . . . . 14 3.2 Aspect and Quality Levels . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 3.3 Aspect 1: Granularity, Timespan and Reported Measurements . . . . . . 16 3.3.1 Core Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 3.3.2 The Whole Run . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 3.3.3 Level 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 3.3.4 Level 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 3.3.5 L

## Core argument / findings
- Formalizes how system power under benchmark load is measured for Green500, including quality levels, instrumentation boundaries, and full-run reporting. Essential to justify using Green500-style audited performance-per-watt data as the GF/W base in CPC.
- 16 3.3 Aspect 1: Granularity, Timespan and Reported Measurements 16 3.3.1 Core Phase . .
- 24 3.6 Example of a Power Measurement Schematic 29 1 Introduction This document recommends a methodological approach for measuring, recording, and reporting the power used by a high performance computer (HPC) system while running a workload.
- 10 Included Subsystems 10 Tunable Parameters 11 Environmental Factors 11 3 Reporting Power Values (Detailed Information) 12 3.1 Measuring Device Terminology and Specifications 12 3.1.1 Accuracy Requirements 12 3.1.2 Sampling and Power Readings 13 3.1.3 Power-Averaged and Total Energy Measurements .

## Method & data
- Paper type: standard or benchmark methodology.
- Parsed coverage used here: full document (33 pages).
- 7 Power Measurement Locations 7 Measuring Devices 7 Workload Requirement .
- 8 Level 1 Power Measurement 8 Level 2 Power Measurement 8 Level 3 Power Measurement 9 Idle Power .
- Energy Efficient High Performance Computing Power Measurement Methodology (version 2.0 RC 1.0) Contents 1 Introduction 6 2 Checklist 7 Quality Level .

## Key quotes
- p. 14: "Level 3 specifies an energy measurement, but reports a power value."
- p. 26: "For Level 1, both the compute-node subsystem and the interconnect must be reported."
- p. 10: "– For Level 1, both the compute-node subsystem and the interconnect must be reported."

## Relevance to EDWC thesis
- Formalizes how system power under benchmark load is measured for Green500, including quality levels, instrumentation boundaries, and full-run reporting. Essential to justify using Green500-style audited performance-per-watt data as the GF/W base in CPC.
- Proposal placement: §3.4.3 GF/W construction; §3.2 variable definition; §2.3 benchmarking.
- Most relevant use within the proposal: literature review, empirical strategy, CPC / measurement logic.

## Caveats / limitations
- This is an institutional or technical source rather than peer-reviewed causal evidence.

## Related papers in corpus
- [dongarra_luszczek_2026_hpl_mxp.md](dongarra_luszczek_2026_hpl_mxp.md): same subsection; same stream; shared tags: GF-W, measurement.
- [fernandez_2025_hardware_scaling_llm.md](fernandez_2025_hardware_scaling_llm.md): same subsection; same stream; shared tags: measurement.
- [tschand_2025_mlperf_power.md](tschand_2025_mlperf_power.md): same subsection; same stream; shared tags: measurement.
- [caict_2023_computing_power_index.md](caict_2023_computing_power_index.md): same stream; shared tags: measurement.
