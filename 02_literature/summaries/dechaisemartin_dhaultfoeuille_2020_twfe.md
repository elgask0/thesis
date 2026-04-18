---
filename_stem: "dechaisemartin_dhaultfoeuille_2020_twfe"
citation: "de Chaisemartin, C., & D'Haultfœuille, X. (2020).** Two-way fixed effects estimators with heterogeneous treatment effects. *American Economic Review, 110*(9), 2964–2996. https://doi.org/10.1257/aer.20181169"
first_author: "de Chaisemartin"
year: "2020"
title: "Two-way fixed effects estimators with heterogeneous treatment effects"
venue: "de Chaisemartin, C., & D'Haultfœuille, X. (2020)."
doi: "10.1257/aer.20181169"
url: "https://doi.org/10.1257/aer.20181169"
stream: "Design"
subsection: "2.4 Modern staggered-DiD methodology"
tags: ["TWFE-bias", "negative-weights", "heterogeneous-effects", "staggered-DiD", "design"]
proposal_sections: "§3.4 methodological justification; §2.4 design-side gap."
cpc_component: ""
priority: "must-cite"
caveat: ""
zotero_key: "5FVPGK28"
pdf_local: "pdf/dechaisemartin_dhaultfoeuille_2020_twfe.pdf"
note_status: "upgraded-mineru-full"
---

# Two-way fixed effects estimators with heterogeneous treatment effects

**Authors:** de Chaisemartin et al.
**Year:** 2020
**Venue:** de Chaisemartin, C., & D'Haultfœuille, X. (2020).
**DOI:** [10.1257/aer.20181169](https://doi.org/10.1257/aer.20181169)
**Zotero:** [Open](zotero://select/library/items/5FVPGK28)
**Stream / subsection:** Design / 2.4 Modern staggered-DiD methodology

## Role in proposal

Shows that TWFE regressions can place negative weights on some group-time treatment effects under heterogeneity, so the pooled coefficient can be misleading even in sign. High-profile AER anchor for replacing TWFE with staggered-robust estimators.

## Use in proposal

§3.4 methodological justification; §2.4 design-side gap.

## Abstract

American Economic Review 2020, 110(9): 2964–2996 https://doi.org/10.1257/aer.20181169 2964 Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects† By Clément de Chaisemartin and Xavier D’Haultfœuille* Linear regressions with period and group fixed effects are widely used to estimate treatment effects. We show that they estimate weighted sums of the average treatment effects (ATE ) in each group and period, with weights that may be negative. Due to the negative weights, the linear regression coefficient may for instance be nega- tive while all the ATEs are positive. We propose another estimator that solves this issue. In the two applications we revisit, it is signifi- cantly different from the linear regression estimator. (JEL C21, C23, D72, J31, J51, L82) A popular method to estimate the effect of a treatment on an outcome is to com- pare over time groups experiencing different evolutions of their exposure to treat- ment. In practice, this idea is implemented by estimating regressions that control for group and time fixed effects. Hereafter, we refer to those as ­two-way fixed effects (FE) regressions. We conducted a survey, and found that 19 percent of all empiri- cal articles published by the American Economic Review (AER) between 2010 and 2012 have used a ­two-way FE regression to estimate the effect of a treatment on an outcome. When the treatment effect is constant across groups and over time, such regressions estimate that effect under the standard “common trends” assumption. However, it is often implausible that the treatment effect is constant. For instance, the minimum wage’s effect on employment may vary across US counties, and may change over time. This paper examines the properties of ­two-way FE regressions when the constant effect assumption

## Core argument / findings
- Shows that TWFE regressions can place negative weights on some group-time treatment effects under heterogeneity, so the pooled coefficient can be misleading even in sign. High-profile AER anchor for replacing TWFE with staggered-robust estimators.
- Due to the negative weights, the linear regression coefficient may for instance be negative while all the ATEs are positive.
- We show that they estimate weighted sums of the average treatment effects (ATE) in each group and period, with weights that may be negative.
- Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects† By Clément de Chaisemartin and Xavier D’Haultfœuille\* Linear regressions with period and group fixed effects are widely used to estimate treatment effects.

## Method & data
- Paper type: methods paper.
- Parsed coverage used here: full document (33 pages).
- The contribution is formal identification and estimation logic rather than a new sector-specific dataset.
- Due to the negative weights, the linear regression coefficient may for instance be negative while all the ATEs are positive.
- We show that they estimate weighted sums of the average treatment effects (ATE) in each group and period, with weights that may be negative.

## Key quotes
- p. 22: "We use the data in Vella and Verbeek (1998) to compute various estimators of the union wage premium."
- p. 23: "We also compute DIDMpl,2 and DIDMpl,3, two pl,3 other placebo estimators performing the same comparison two and three periods before the change."
- p. 23: "It is computed by the fuzzydid and did_multiplegt Stata packages."

## Relevance to EDWC thesis
- Shows that TWFE regressions can place negative weights on some group-time treatment effects under heterogeneity, so the pooled coefficient can be misleading even in sign. High-profile AER anchor for replacing TWFE with staggered-robust estimators.
- Proposal placement: §3.4 methodological justification; §2.4 design-side gap.
- Most relevant use within the proposal: literature review, research gap, empirical strategy.

## Caveats / limitations
- Use it to justify identification strategy or estimator choice, not as direct evidence on EDWC or China data centers.

## Related papers in corpus
- [sun_abraham_2021_event_study_het.md](sun_abraham_2021_event_study_het.md): same subsection; same stream; shared tags: TWFE-bias, design, staggered-DiD.
- [borusyak_2024_event_study_imputation.md](borusyak_2024_event_study_imputation.md): same subsection; same stream; shared tags: design, staggered-DiD.
- [callaway_santanna_2021_did_multiple_periods.md](callaway_santanna_2021_did_multiple_periods.md): same subsection; same stream; shared tags: design, staggered-DiD.
- [goodman_bacon_2021_did_timing.md](goodman_bacon_2021_did_timing.md): same subsection; same stream; shared tags: design, staggered-DiD.
