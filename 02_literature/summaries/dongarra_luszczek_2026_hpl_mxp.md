---
filename_stem: "dongarra_luszczek_2026_hpl_mxp"
citation: "Dongarra, J., & Luszczek, P. (2026).** HPL-MxP benchmark: Mixed-precision algorithms, iterative refinement, and scalable data generation. *The International Journal of High Performance Computing Applications*. https://doi.org/10.1177/10943420251382476"
first_author: "Dongarra"
year: "2026"
title: "HPL-MxP benchmark: Mixed-precision algorithms, iterative refinement, and scalable data generation"
venue: "Dongarra, J., & Luszczek, P. (2026)."
doi: "10.1177/10943420251382476"
url: "https://doi.org/10.1177/10943420251382476"
stream: "Measurement"
subsection: "3.3 Compute efficiency benchmarks (GF/W)"
tags: ["HPL-MxP", "mixed-precision", "GF-W", "AI-benchmark", "measurement"]
proposal_sections: "§3.4.3 HPL-MxP multiplier; §3.2 variable definition; §2.3 benchmarking."
cpc_component: "Compute efficiency (GF/W)"
priority: "strong-include"
caveat: ""
zotero_key: ""
pdf_local: "pdf/dongarra_luszczek_2026_hpl_mxp.pdf"
note_status: "upgraded-mineru-full"
---

# HPL-MxP benchmark: Mixed-precision algorithms, iterative refinement, and scalable data generation

**Authors:** Dongarra et al.
**Year:** 2026
**Venue:** Dongarra, J., & Luszczek, P. (2026).
**DOI:** [10.1177/10943420251382476](https://doi.org/10.1177/10943420251382476)
**Zotero:** not in Zotero
**Stream / subsection:** Measurement / 3.3 Compute efficiency benchmarks (GF/W)

## Role in proposal

The strongest bridge from FP64-oriented HPC efficiency to AI-relevant mixed-precision throughput. Makes the HPL-MxP speedup step in the GF/W construction methodologically citeable rather than purely heuristic.

## Use in proposal

§3.4.3 HPL-MxP multiplier; §3.2 variable definition; §2.3 benchmarking.

## Abstract

We present a mixed-precision benchmark called HPL-MxP that uses both a lower-precision LU factorization with a non-stationary iterative refinement based on GMRES. We evaluate the numerical stability of one of the methods of generating the input matrix in a scalable fashion and show how the diagonal scaling affects the solution quality in terms of the backward-error. Some of the per- formance results at large scale supercomputing installations pro- duced Exascale-level compute throughput numbers thus proving the viability of the proposed benchmark for evaluating such ma- chines. We also present the potential of the benchmark to continue increasing its use with proliferation of hardware accelerators for AI workloads whose reliable evaluation continues to pose a par- ticular challenge for the users.

## Core argument / findings
- The strongest bridge from FP64-oriented HPC efficiency to AI-relevant mixed-precision throughput. Makes the HPL-MxP speedup step in the GF/W construction methodologically citeable rather than purely heuristic.
- We present a mixed-precision benchmark called HPL-MxP that uses both a lower-precision LU factorization with a non-stationary iterative refinement based on GMRES.
- Some of the performance results at large scale supercomputing installations produced Exascale-level compute throughput numbers thus proving the viability of the proposed benchmark for evaluating such machines.
- We also present the potential of the benchmark to continue increasing its use with proliferation of hardware accelerators for AI workloads whose reliable evaluation continues to pose a particular challenge for the users.

## Method & data
- Paper type: standard or benchmark methodology.
- Parsed coverage used here: full document (10 pages).
- We present a mixed-precision benchmark called HPL-MxP that uses both a lower-precision LU factorization with a non-stationary iterative refinement based on GMRES.
- Some of the performance results at large scale supercomputing installations produced Exascale-level compute throughput numbers thus proving the viability of the proposed benchmark for evaluating such machines.
- We also present the potential of the benchmark to continue increasing its use with proliferation of hardware accelerators for AI workloads whose reliable evaluation continues to pose a particular challenge for the users.

## Key quotes
- p. 3: "Then an approximate solution 0 is computed from the ??low-precision factors and ."
- p. 3: "A more extreme case of utilizing mixed-precision schemes is to switch exclusively to integer compute units [40]."
- p. 2: "By that metric alone, HPL-MxP now was ported to and subsequently optimized on the largest supercomputers recorded on TOP500 list."

## Relevance to EDWC thesis
- The strongest bridge from FP64-oriented HPC efficiency to AI-relevant mixed-precision throughput. Makes the HPL-MxP speedup step in the GF/W construction methodologically citeable rather than purely heuristic.
- Proposal placement: §3.4.3 HPL-MxP multiplier; §3.2 variable definition; §2.3 benchmarking.
- Most relevant use within the proposal: literature review, empirical strategy, CPC / measurement logic.

## Caveats / limitations
- This is an institutional or technical source rather than peer-reviewed causal evidence.

## Related papers in corpus
- [eehpc_2015_green500_methodology.md](eehpc_2015_green500_methodology.md): same subsection; same stream; shared tags: GF-W, measurement.
- [fernandez_2025_hardware_scaling_llm.md](fernandez_2025_hardware_scaling_llm.md): same subsection; same stream; shared tags: measurement.
- [tschand_2025_mlperf_power.md](tschand_2025_mlperf_power.md): same subsection; same stream; shared tags: measurement.
- [caict_2023_computing_power_index.md](caict_2023_computing_power_index.md): same stream; shared tags: measurement.
