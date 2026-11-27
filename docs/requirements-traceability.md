# 穿好需求追溯矩阵 v0

本期共 21 个用例，其中 18 个功能用例、3 个非功能需求用例（性能、安全、可用性）。业务描述和 Given / When / Then 见[需求规格说明书](requirements-srs.md)，便于组内阅读的版本见[需求评审清单](第三周需求评审清单.md)。

表中的负责人在 GitHub 上负责需求确认及跟踪。此表记录需求预计交付的增量，开发、测试分工及迭代排期由组长依据团队分工协调。

| 用户故事 | 需求 | 用例 | 业务主题 | Issue | 需求负责人 | 交付增量 |
| --- | --- | --- | --- | --- | --- | --- |
| US-01 | FR-01 | UC-01 | 指定规格跨平台比价与降级 | [#14](https://github.com/MXH814/DressWell/issues/14) | 胡知鱼（@Chloeee-fish） | v0.2 必做 |
| US-02 | FR-02 | UC-02 | 用旧衣对照尺码 | [#15](https://github.com/MXH814/DressWell/issues/15) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-03 | FR-03 | UC-03 | 识别无法比较的尺寸 | [#16](https://github.com/MXH814/DressWell/issues/16) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-04 | FR-04 | UC-04 | 登记衣物 | [#17](https://github.com/MXH814/DressWell/issues/17) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-05 | FR-05 | UC-05 | 排除不可穿衣物 | [#18](https://github.com/MXH814/DressWell/issues/18) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-06 | FR-06 | UC-06 | 保存待购候选 | [#19](https://github.com/MXH814/DressWell/issues/19) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-07 | FR-07 | UC-07 | 用已有衣物试搭 | [#20](https://github.com/MXH814/DressWell/issues/20) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-08 | FR-08 | UC-08 | 只换指定单品 | [#21](https://github.com/MXH814/DressWell/issues/21) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-09 | FR-09 | UC-09 | 按款号找同款 | [#22](https://github.com/MXH814/DressWell/issues/22) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-10 | FR-10 | UC-10 | 识别过期与待核实报价 | [#23](https://github.com/MXH814/DressWell/issues/23) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-11 | FR-11 | UC-11 | 提示实际试穿核对 | [#24](https://github.com/MXH814/DressWell/issues/24) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-12 | FR-12 | UC-12 | 登记已买待收 | [#25](https://github.com/MXH814/DressWell/issues/25) | 胡知鱼（@Chloeee-fish） | v0.3 |
| US-13 | FR-13 | UC-13 | 留用后复用原搭配 | [#26](https://github.com/MXH814/DressWell/issues/26) | 胡知鱼（@Chloeee-fish） | v0.3 |
| US-14 | FR-14 | UC-14 | 记录退货并排除推荐 | [#27](https://github.com/MXH814/DressWell/issues/27) | 胡知鱼（@Chloeee-fish） | v0.3 |
| US-15 | FR-15 | UC-15 | 按场合及手填条件搭配 | [#28](https://github.com/MXH814/DressWell/issues/28) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-16 | FR-16 | UC-16 | 保存试穿反馈 | [#29](https://github.com/MXH814/DressWell/issues/29) | 胡知鱼（@Chloeee-fish） | v0.3 |
| US-17 | FR-17 | UC-17 | 维护失效报价 | [#30](https://github.com/MXH814/DressWell/issues/30) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-19 | NFR-01 | UC-19 | 核对查价响应时间 | [#31](https://github.com/MXH814/DressWell/issues/31) | 胡知鱼（@Chloeee-fish） | v0.2 |
| US-20 | NFR-02 | UC-20 | 保护私人衣物照片 | [#32](https://github.com/MXH814/DressWell/issues/32) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-21 | FR-19 | UC-21 | 访客查看公开示例 | [#33](https://github.com/MXH814/DressWell/issues/33) | 胡知鱼（@Chloeee-fish） | v0.1 |
| US-22 | NFR-03 | UC-22 | 中断后恢复已保存搭配 | [#35](https://github.com/MXH814/DressWell/issues/35) | 胡知鱼（@Chloeee-fish） | v0.2 |

US-03 补充 US-02 缺少可比尺寸时的处理。US-18／FR-18／UC-18 为定时报价复核提醒，保留编号供后续验证，不计入本期基线。
