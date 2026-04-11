# EDWC Treatment Dates

Working note for official-source treatment timing evidence used to define province-level EDWC go-live dates.

## Coding Rule

- Prioritize official `上线` / `上线运营` / `投运` / `put into use` milestones over construction-complete announcements.
- For monthly panels, code the treatment month as the first day of the event month.
- For daily specifications, keep the exact day only when the source is precise; otherwise use month-level timing and test adjacent robustness windows.

> [!note]
> This note supersedes earlier placeholder timings in the repo. Current baseline month coding is Ningxia `2023-02`, Guizhou `2023-09`, Gansu `2024-06`, and Inner Mongolia `2024-09`.

## Baseline Coding Summary

| Province | Baseline `T0` month | Baseline logic | Robustness / later milestone |
|---|---|---|---|
| Ningxia | `2023-02` | Integrated EDWC computing-power service platform officially launched and operating on 2023-02-24. | `2023-07` China Telecom Ningxia DC Phase I fully built, accepted, and about to enter operation. |
| Guizhou | `2023-09` | SPIC Gui'an Data Center reported in use from September 2023; NetEase Gui'an DC also targeted trial operation by end-September 2023. | `2024-06` completion of Beijing data-center migration to Gui'an. |
| Gansu | `2024-06` | Qingyang cluster reported built and operating at 15,000 standard racks and 12,000 P, surpassing 10,000 P. | `2024-12` and `2025-01` scale-up updates. |
| Inner Mongolia | `2024-09` | Jiuzhou Intelligent Computing Center in Horinger reported completed and put into operation at end-September 2024. | `2025-05` Horinger multi-cloud monitoring and dispatch platform put into operation. |

## Evidence Table

### Ningxia

| Approx. `T0` | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|
| `2023-02-24` | 东数西算一体化算力服务平台 / Eastern Data Western Compute Integrated Computing Power Service Platform | 平台正式发布上线 / 上线运营 | Best current official-source candidate for network-level go-live in Ningxia. | [宁夏新闻网 / Ningxia News Network](https://www.nxnews.net/yc/jrww/202302/t20230224_7868269.html), [央视网 / CCTV](https://tv.cctv.com/2023/02/24/VIDE4NE8wtpRwqAzmF2lQAki230224.shtml) |
| `2023-07` | 中国电信宁夏数据中心项目一期 / China Telecom Ningxia Data Center Phase I | 建成通过验收，即将投入运营 | Keep as a physical-capacity milestone, but not the current baseline `T0`. | [中卫市人民政府 / Zhongwei Municipal Government](https://www.nxzw.gov.cn/zwgk/zfxxgkml/zdxmjs/zdxm/202307/t20230721_4189462.html) |

### Guizhou

| Approx. `T0` | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|
| `2023-09` | 国家电投集团贵安数据中心 / SPIC Gui'an Data Center | 投用 | Strongest current operational milestone in the pasted table. | [国际在线贵州频道 / CRI Guizhou, Xinhua-syndicated](https://gz.cri.cn/n/20240103/25e22ceb-655b-4f21-45ce-3116bf4d7b66.html) |
| `2023-09` | 网易贵安数据中心项目 / NetEase Gui'an Data Center | 计划试运行时间 | Supportive evidence for the same month, but note that this row is a planned trial-run date rather than realized operation. | [贵州省发展和改革委员会 / Guizhou DRC](https://fgw.guizhou.gov.cn/zwgk2025/zdlyxx/zdjsxm/zdxmjsjz/202308/t20230831_88414224.html), [多彩贵州网 / Guizhou Government special topic](https://www.guizhou.gov.cn/ztzl/2023nsbh/mtjj/202305/t20230521_79827773.html) |
| `2024-06` | 国家电投集团贵安数据中心 / SPIC Gui'an Data Center | 完成北京机房整体搬迁 | Best robustness date for full business migration and switch-over. | [贵州省大数据发展管理局 / Guizhou Big Data Development Administration](https://dsj.guizhou.gov.cn/zwgk/zdlyxx/jscs/202511/t20251112_88938026.html) |

### Gansu

| Approx. `T0` | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|
| `2024-06` | 全国算力枢纽（甘肃·庆阳）节点与庆阳数据中心集群 / National Computing Power Hub (Gansu-Qingyang) and Qingyang Data Center Cluster | 集群建成投运，算力规模破万P | Baseline `T0` remains June 2024. This is the clearest cluster-scale operational milestone in the repo so far. | [甘肃省人民政府门户网站 / Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202406/173935221.shtml) |
| `2024-12` | “中国算谷·智慧庆阳”城市品牌 / "China Compute Valley - Smart Qingyang" | 已建成投运规模更新 | Post-`T0` expansion update. | [甘肃省人民政府门户网站 / Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202412/174043995.shtml) |
| `2025-01` | 庆阳数据中心集群 / Qingyang Data Center Cluster | 规模综述 | Further post-`T0` scale-up evidence. | [甘肃省人民政府门户网站 / Gansu Provincial Government](https://www.gansu.gov.cn/gsszf/c100002/c100006/c100008/202501/174059902.shtml) |

### Inner Mongolia

| Approx. `T0` | Project / Asset | Go-live evidence | Notes | Source |
|---|---|---|---|---|
| `2024-09` | 九州智算中心 / Jiuzhou Intelligent Computing Center | 今年9月底建成投运 | Best current baseline candidate from the official-source table for a large physical computing node in Horinger. | [新华网科技频道 / Xinhua Tech](https://www.xinhuanet.com/tech/20241127/64301a76191045489b80436d5cfea77f/c.html), [新浪财经转载 / Sina Finance](https://finance.sina.com.cn/jjxw/2024-11-28/doc-incxrfqr2879759.shtml) |
| `2025-05` | 和林格尔数据中心集群多云算力资源监测与调度平台 / Horinger Multi-Cloud Computing Power Monitoring and Dispatch Platform | 平台投运与跨枢纽调度 | Stronger network-level operations milestone; use as a later robustness date rather than the baseline. | [新华网政治频道 / Xinhua Politics](https://www.news.cn/politics/20250530/e5da7c9099b04454a53b00502b5c6fca/c.html) |

## Related Notes

- [[global_plan]]
- [[EDWC_Gansu_EventStudy]]
- [[thesis_structure]]
