# EDWC Treatment Dates

Working note for source-backed treatment timing evidence used to define province-level EDWC go-live dates.

## Coding Rule

- Prioritize official or high-authority `上线` / `上线运营` / `投运` / `投用` / `投产启用` milestones over construction-complete announcements.
- Distinguish clearly between three timing layers: **policy approval**, **implementation**, and **operational go-live**.
- For monthly panels, code the treatment month as the first day of the event month.
- For daily specifications, keep the exact day only when the source is precise; otherwise use month-level timing and test adjacent robustness windows.
- When operational rollout is phased, use the **first defensible operational milestone** for the baseline `T0`, and keep later public commissioning / full-ramp dates as robustness checks.

## Three-Layer Timing Framework

| Layer | Definition | Empirical use |
|---|---|---|
| Policy approval date | First formal national authorization of the provincial EDWC node. | Policy-event robustness only; too early to be the default operational `T0` in most cases. |
| Implementation date | First provincial implementation / support plan for the node. | Intermediate timing robustness date; still policy/administrative rather than operational. |
| Operational date | First defensible `上线` / `投运` / `投用` / `投产启用` milestone. | Preferred baseline `T0` for operational treatment coding. |

## Province Timing Summary

| Province | Policy approval date | Implementation date | Operational date used for baseline `T0` | Confidence |
|---|---|---|---|---|
| Ningxia | `2021-12-20` | `2022-08-05` | `2023-02-24` | Medium-high |
| Guizhou | `2021-12-20` | `2022-08-09` | `2024-06` | Medium |
| Gansu | `2021-12-20` | `2022-08-28` | `2024-06-20` | High |
| Inner Mongolia | `2021-12-20` | `2023-10-10` | `2024-02-04` | Medium |

> [!note]
> These are working anchors for treatment coding, not claims that an entire provincial hub became fully operational on a single date. In several cases, the evidence is project-level or phased rather than hub-wide.

> [!note]
> This note supersedes earlier placeholder timings. Current baseline month coding is Ningxia `2023-02`, Guizhou `2024-06`, Gansu `2024-06`, and Inner Mongolia `2024-02`.

## Baseline Coding Summary

| Province | Baseline `T0` month | Baseline logic | Robustness / later milestone | Confidence |
|---|---|---|---|---|
| Ningxia | `2023-02` | Use the first clearly documented EDWC network/service-platform launch: the integrated computing-power service platform in Yinchuan was reported as formally launched and operating on `2023-02-24`. | `2023-07` China Telecom Ningxia DC Phase I passed acceptance and was about to enter operation; keep as a later physical-capacity milestone, not baseline `T0`. | Medium-high |
| Guizhou | `2024-06` | Use the cleanest documented operational switch-over: State Power Investment Corporation (SPIC) completed the overall migration of its Beijing data center to Gui'an in June 2024, marking a defensible operational EDWC transition. | `2023-09` can be retained as an early-use / partial-operation candidate because later reports state the SPIC center had been in use since September 2023, but the October 2023 evidence still describes active build-out and upcoming migration. | Medium |
| Gansu | `2024-06` | Use the official cluster-scale milestone: by `2024-06-20` the Qingyang cluster was reported by the Gansu provincial government as already built and operating with 15,000 standard racks and 12,000P. | `2024-12` and `2025-01` are later scale-up updates. | High |
| Inner Mongolia | `2024-02` | Use the first phased operational milestone for China Mobile Hohhot Intelligent Computing Center in Horinger: Phase I was reported as `上线投产` on `2024-02-04`. | `2024-04-28` public formal launch / `已投产使用`; `2024-06-28` full-cluster online; `2024-09` Jiuzhou Intelligent Computing Center put into operation; `2025-05` multi-cloud dispatch platform put into operation. | Medium |

## Evidence Table

### Ningxia

| Approx. `T0` | Layer | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|---|
| `2021-12-20` | Policy approval | 宁夏枢纽 / Ningxia national hub node | 国家发展改革委等部门复函同意在宁夏启动建设全国一体化算力网络国家枢纽节点 | Use as policy-event robustness only. | [NDRC approval reply for Ningxia](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202112/t20211229_1310526.html) |
| `2022-08-05` | Implementation | 宁夏枢纽建设 2022 年推进方案 / Ningxia hub 2022 promotion plan | 成文时间 `2022-08-05`; 宁政办发〔2022〕52号 | First province-level implementation plan. | [Ningxia Government Office notice](https://www.nx.gov.cn/zwgk/qzfwj/202208/t20220815_3672063.html) |
| `2023-02-24` | Operational | 东数西算一体化算力服务平台 / Integrated EDWC computing-power service platform | `正式上线运营` | Best current source-backed candidate for network/service-platform go-live in Ningxia; preferred baseline `T0`. | [CCTV-sourced report via People’s Political Consultative News](https://www.rmzxw.com.cn/c/2023-02-24/3297764.shtml), [China Securities Journal summary](https://www.cs.com.cn/xwzx/hg/202302/t20230225_6325702.html) |
| `2023-07-21` | Later physical-capacity milestone | 中国电信宁夏数据中心项目一期 / China Telecom Ningxia Data Center Phase I | `建成通过验收，即将投入运营` | Readiness / acceptance, but not confirmed operation. Keep only as later robustness milestone. | [Zhongwei Municipal Government](https://www.nxzw.gov.cn/zwgk/zfxxgkml/zdxmjs/zdxm/202307/t20230721_4189462.html) |

### Guizhou

| Approx. `T0` | Layer | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|---|
| `2021-12-20` | Policy approval | 贵州枢纽 / Guizhou national hub node | 国家发展改革委等部门复函同意在贵州启动建设全国一体化算力网络国家枢纽节点 | Use as policy-event robustness only. | [NDRC approval reply for Guizhou](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202112/t20211229_1310520.html) |
| `2022-08-09` | Implementation | 贵州枢纽节点实施意见 / Guizhou implementation opinion | 黔府办函〔2022〕68号 | First province-level implementation/support document. | [Guizhou Government Office implementation opinion](https://drc.guizhou.gov.cn/xxgk/xxgkml/zcwj/gfxwj/202208/t20220812_76073936.html) |
| `2023-09` | Early-use candidate | 国家电投集团贵安数据中心 / SPIC Gui'an Data Center | `去年9月投用以来` | Supports September 2023 as an early-use / partial-operation candidate, but not the cleanest switch-over date. | [Xinhua Guizhou](https://gz.news.cn/20240103/230fc867d4ff46e58407ad8c19543572/c.html) |
| `2023-09` | Planned trial run only | 网易贵安数据中心项目 / NetEase Gui'an Data Center | `计划今年9月底试运行` | Planned trial-run date only; not realized operation. Do not use as primary `T0`. | [Guizhou DRC project progress note](https://fgw.guizhou.gov.cn/zwgk/xxgkml/zdlyxx/zdxmjs/zdxmjsjz/202308/t20230831_82144464.html), [Guizhou DRC news note](https://fgw.guizhou.gov.cn/fggz/ywdt/202302/t20230201_78061509.html) |
| `2023-10` | Counter-evidence against clean Sep-2023 full go-live | 国家电投集团贵安数据中心 / SPIC Gui'an Data Center | `为了该公司北京的数据中心在今年11月全部迁至贵安而日夜奋战` | Shows that as of October 2023 migration / construction activity was still ongoing; weakens September 2023 as a clean full-operational date. | [Guizhou Science and Technology Department reprint](https://kjt.guizhou.gov.cn/wzzt/qmgcgf2022/gcls/202310/t20231018_82785621.html), [Guizhou DRC reprint](https://drc.guizhou.gov.cn/xwzx/zwyw/202310/t20231010_82715838.html) |
| `2024-06` | Operational | 国家电投集团贵安数据中心 / SPIC Gui'an Data Center | `6月，跨越距离超2000公里的国家电投集团数据中心整体搬迁至贵安新区……标志着国家电投集团数字化底座已经建好` | Cleanest documented operational switch-over; preferred baseline `T0`. | [Guizhou DRC thematic page](https://fgw.guizhou.gov.cn/ztzl/dsjzlxd/202408/t20240823_85446871.html), [Guiyang Evening News](https://wb.gywb.cn/ipaper/gywb/html/2024-08/13/content_14127.htm) |

### Gansu

| Approx. `T0` | Layer | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|---|
| `2021-12-20` | Policy approval | 甘肃枢纽 / Gansu national hub node | 国家发展改革委等部门复函同意在甘肃启动建设全国一体化算力网络国家枢纽节点 | Use as policy-event robustness only. | [NDRC approval reply for Gansu](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202112/t20211229_1310522.html) |
| `2022-08-28` | Implementation | 甘肃建设运营若干措施 / Gansu support measures | 甘政办发〔2022〕103号，`2022年8月28日` | First province-level support / implementation document. | [Gansu Government notice](https://www.gansu.gov.cn/gsszf/c100055/202209/2114730.shtml), [Gansu Government Gazette PDF](https://swt.gansu.gov.cn/swt/c110405/202211/2152485/files/9a1e6fc442c14f8d9efe148772af0a60.pdf) |
| `2024-06-20` | Operational | 全国算力枢纽（甘肃·庆阳）节点与庆阳数据中心集群 / National Computing Power Hub (Gansu-Qingyang) and Qingyang cluster | `已建成投运标准机架1.5万个，算力规模达到1.2万P` | Strongest cluster-scale operational milestone; preferred baseline `T0`. | [Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202406/173935221.shtml), [Xinhua / Guangming follow-up](https://www.news.cn/tech/20240625/7f79aa96a7054f199b2e5ea407b268b6/c.html) |
| `2024-05` | Supporting operational evidence | 中国电信 / 中国移动庆阳项目等 / telecom projects in Qingyang cluster | `建成投用` | Supports the June 2024 cluster-scale coding. | [Guangming Daily reprint](https://news.gmw.cn/2024-05/13/content_37319020.htm) |
| `2024-12` | Post-`T0` expansion update | “中国算谷·智慧庆阳” / China Compute Valley – Smart Qingyang | `已建成投运`规模更新 | Later scale-up update only. | [Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202412/174043995.shtml) |
| `2025-01` | Post-`T0` expansion update | 庆阳数据中心集群 / Qingyang Data Center Cluster | 规模综述 | Further post-`T0` scale-up evidence only. | [Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202501/174059902.shtml) |

### Inner Mongolia

| Approx. `T0` | Layer | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|---|
| `2021-12-20` | Policy approval | 内蒙古枢纽 / Inner Mongolia national hub node | 国家发展改革委等部门复函同意在内蒙古启动建设全国一体化算力网络国家枢纽节点 | Use as policy-event robustness only. | [NDRC approval reply for Inner Mongolia](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202112/t20211229_1310524.html) |
| `2023-10-10` | Implementation | 内蒙古数字经济高质量发展工作方案（2023—2025年） / digital economy work plan | 成文日期 `2023-10-10`，公开发布 `2024-04-08` | First clear province-level implementation / support plan used here. | [Inner Mongolia Government Office notice](https://ylbzj.nmg.gov.cn/ztzl/ztzl_whz/yhyshj/yshjzcwj/zzqzce/202404/t20240408_2490553.html?zbb=true) |
| `2024-02-04` | Operational | 中国移动呼和浩特智算中心 / China Mobile Hohhot Intelligent Computing Center | `一阶段于2月4日上线投产` | Earliest defensible phased operational milestone; preferred baseline `T0` under the first-go-live rule. | [Inner Mongolia News](https://inews.nmgnews.com.cn/system/2024/04/28/013579403.shtml), [Wuhai municipal government reprint](https://www.nmgwx.gov.cn/relevantDepartmentsReleased/12820.jhtml) |
| `2024-03-21` | Phased expansion | 中国移动呼和浩特智算中心 / China Mobile Hohhot Intelligent Computing Center | `二阶段于3月21日上线投产` | Keep as phased expansion milestone. | [Inner Mongolia News](https://inews.nmgnews.com.cn/system/2024/04/28/013579403.shtml) |
| `2024-04-28` | Public formal commissioning | 中国移动呼和浩特智算中心 / China Mobile Hohhot Intelligent Computing Center | `目前已投产使用` / `正式对外发布` | Strong later robustness milestone if the preferred coding rule requires public formal commissioning rather than first phased operation. | [China Mobile official](https://www.10086.cn/aboutus/news/groupnews/index_detail_49656.html), [Xinhua](https://www.news.cn/info/20240428/71614bc2f5404c74b46d09538d6f13f3/c.html) |
| `2024-06-28` | Full-cluster online | 中国移动呼和浩特智算中心 / China Mobile Hohhot Intelligent Computing Center | `全部集群正式上线` | Later robustness milestone for full-ramp operation. | [Shenzhen asset-management information reprint](https://www.szzg.gov.cn/2024/szzg/xyzx/202407/t20240704_4854433.htm) |
| `2024-09` | Later physical-node milestone | 九州智算中心 / Jiuzhou Intelligent Computing Center | `今年9月底建成投运` | Keep as later physical-node milestone; no longer the preferred baseline `T0`. | [Xinhua Tech](https://www.xinhuanet.com/tech/20241127/64301a76191045489b80436d5cfea77f/c.html), [Sina Finance reprint](https://finance.sina.com.cn/jjxw/2024-11-28/doc-incxrfqr2879759.shtml) |
| `2025-05` | Later network/platform milestone | 和林格尔数据中心集群多云算力资源监测与调度平台 / Horinger multi-cloud monitoring and dispatch platform | `平台投运` | Network/platform milestone, not first compute go-live. | [Xinhua Politics](https://www.news.cn/politics/20250530/e5da7c9099b04454a53b00502b5c6fca/c.html) |

## Related Notes

- [[global_plan]]
- [[EDWC_Gansu_EventStudy]]
- [[thesis_structure]]
