# 商品数据

## 开发样本

`products.sample.json` 保留全量文件顶层的 `batchSource` 和 `items`，覆盖苏宁、淘宝、天猫、唯品会、闲鱼，每个平台 100 条，共 500 条。按原文件顺序遍历 `items`，平台配额未满且 `externalId` 未在已选样本中出现时保留记录，达到总量后停止；不随机抽样、不改写记录字段。本次跳过了 4 条 ID 重复的候选记录。

这是用于字段对接和开发测试的均衡样本，不反映全量数据的平台比例。跨平台记录的 `externalId` 可能重复；本样本为便于测试采用全样本 ID 去重，业务中的商品标识仍应同时考虑 `platform`。所选记录没有验证为跨平台同款，也未重新核实当前价格、库存、规格及优惠条件。

| 平台 | `platform` | 全量记录数 | 样本记录数 |
| --- | --- | --- | --- |
| 苏宁 | `suning` | 40,197 | 100 |
| 淘宝 | `taobao` | 2,675 | 100 |
| 天猫 | `tmall` | 2,842 | 100 |
| 唯品会 | `vipshop` | 44,501 | 100 |
| 闲鱼 | `xianyu` | 48,447 | 100 |
| 合计 | | 138,662 | 500 |

本次样本更新关联 [任务 #37](https://github.com/MXH814/DressWell/issues/37)，替换 [PR #12](https://github.com/MXH814/DressWell/pull/12) 的 500 条苏宁样本。

- 来源文件：`collected_all_20260606-full.json`
- 来源批次：`collected_all_20260606`（沿用原文件标识，不额外推定实际采集时间）
- 全量记录数：138,662
- 样本记录数：500
- 价格字段 `price` 在原数据中是字符串，样本保留该类型。
- 样本用于字段对接、开发和演示；库存与价格是来源快照中的值。

## 字段说明

| 字段 | 含义 |
| --- | --- |
| `externalId` | 来源商品标识 |
| `platform` | 来源平台 |
| `title` | 商品标题 |
| `price` / `currency` | 来源报价与币种 |
| `stockStatus` | 来源库存状态 |
| `shopName` / `shopType` | 店铺名称与类型标记 |
| `productUrl` / `imageUrl` | 商品页与图片链接 |
| `brandHint` | 部分平台记录提供的品牌提示，保留原字段 |
| `rawPayload` | 来源记录及采集上下文，包含关键词、页码、属性等 |

不同平台提供的字段不完全相同，例如部分记录没有 `shopName` 或 `shopType`，样本保留原始缺项，不补写空值。

## 全量数据（仅本地）

全量文件存放在项目目录下的 `data/local/collected_all_20260606-full.json`。`data/local/` 已加入根目录 `.gitignore`，不会随普通 Git 提交上传，队友克隆仓库时也不会获得该目录。需要完整数据时另行传递原文件，并放入相同目录。

## 文件校验

SHA-256：

- 全量原文件与本地副本：`cb7b21da1cb548268e81ebf23aab4a05c97a7b1f4458d12b0cc178f92fa82cac`
- 开发样本（仓库原始文件，UTF-8、LF）：`f550d55504f92b2d13b8b0357c42354074551776544e01c613e9462c1f88ecec`
- 开发样本（Windows 工作副本，UTF-8、CRLF）：`f7af446611eac7a8a82dee5b084da62fd7f22a996720ca6aab0a8cb414a8a3e8`

SHA-256 按文件原始字节计算。从 GitHub 下载原始 JSON 时使用 LF 版本的校验值；若工作副本被 Git 转为 CRLF，则使用 CRLF 版本的值。
