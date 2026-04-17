---
filename_stem: "radovanovic_2023_carbon_aware_computing"
citation: "Radovanović, A., Koningstein, R., Schneider, I., et al. (2023).** Carbon-aware computing for datacenters. *IEEE Transactions on Power Systems, 38*(2), 1270–1280. https://doi.org/10.1109/TPWRS.2022.3173250"
first_author: "Radovanović"
year: 2023
title: "Carbon-aware computing for datacenters"
venue: "Radovanović, A., Koningstein, R., Schneider, I., et al. (2023)."
doi: "10.1109/TPWRS.2022.3173250"
url: "https://doi.org/10.1109/TPWRS.2022.3173250"
stream: "Measurement"
subsection: "3.1 Carbon-accounting frameworks for compute"
tags: ["carbon-aware-computing", "grid-CI", "scheduling", "CPC", "measurement"]
proposal_sections: "§2.3 carbon-aware computing; §3.4.3 CI justification."
cpc_component: "Accounting framework (grounds CI logic)"
priority: "must-cite"
caveat: ""
zotero_key: "NQFUKE2Q"
pdf_local: "pdf/radovanovic_2023_carbon_aware_computing.pdf"
note_status: "stub-pdf-read"
---

# Carbon-aware computing for datacenters

**Authors:** Radovanović
**Year:** 2023
**Venue:** Radovanović, A., Koningstein, R., Schneider, I., et al. (2023).
**DOI:** [10.1109/TPWRS.2022.3173250](https://doi.org/10.1109/TPWRS.2022.3173250)
**Zotero:** [Open](zotero://select/library/items/NQFUKE2Q)
**Stream / subsection:** Measurement / 3.1 Carbon-accounting frameworks for compute

## Role in proposal

Canonical system-method paper on time- and location-specific grid carbon signals as inputs to compute scheduling and carbon accounting. Grounds the CI term conceptually: carbon per unit of compute depends on where and when workloads run, even when electricity use is unchanged.

## Use in proposal

§2.3 carbon-aware computing; §3.4.3 CI justification.

## Abstract

1270 IEEE TRANSACTIONS ON POWER SYSTEMS, VOL. 38, NO. 2, MARCH 2023 Carbon-Aware Computing for Datacenters Ana Radovanovi´c, Ross Koningstein , Ian Schneider, Bokan Chen , Alexandre Duarte , Binz Roy, Diyue Xiao, Maya Haridasan, Patrick Hung, Nick Care, Saurav Talukdar, Eric Mullen, Kendal Smith, MariEllen Cottman , and Walfredo Cirne Abstract—The amount of CO2 emitted per kilowatt-hour on an electricity grid varies by time of day and substantially varies by location due to the types of generation. Networked collections of warehouse scale computers, sometimes called Hyperscale Comput- ing, emit more carbon than needed if operated without regard to these variations in carbon intensity. This paper introduces Google’s systemforglobalCarbon-IntelligentComputeManagement,which actively minimizes electricity-based carbon footprint and power infrastructure costs by delaying temporally ﬂexible workloads. The core component of the system is a suite of analytical pipelines used to gather the next day’s carbon intensity forecasts, train day-ahead demand prediction models, and use risk-aware optimization to generate the next day’s carbon-aware Virtual Capacity Curves (VCCs) for all datacenter clusters across Google’s ﬂeet. VCCs impose hourly limits on resources available to temporally ﬂexible workloads while preserving overall daily capacity, enabling all such workloads to complete within a day with high probability. Data from Google’s in-production operation shows that VCCs effectively limit hourly capacity when the grid’s energy supply mix is carbon intensive and delay the execution of temporally ﬂexible workloads to “greener” times. Index Terms—Carbon- and efﬁciency-aware compute manage- ment, datacenter computing, power management. I. INTRODUCTION D EMAND for computing resources

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
