# 商品数据

## 开发样本

`products.sample.json` 保留全量文件顶层的 `batchSource` 和 `items`，按原始顺序截取 `items` 的前 500 条。未排序、去重、筛选或改写字段值。前 500 条均来自苏宁（`platform: suning`），不代表全量数据的平台分布。

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
| `rawPayload` | 来源记录及采集上下文，包含关键词、页码、属性等 |

## 全量数据（仅本地）

全量文件存放在项目目录下的 `data/local/collected_all_20260606-full.json`。`data/local/` 已加入根目录 `.gitignore`，不会随普通 Git 提交上传，队友克隆仓库时也不会获得该目录。需要完整数据时另行传递原文件，并放入相同目录。

## 文件校验

SHA-256：

- 全量原文件与本地副本：`cb7b21da1cb548268e81ebf23aab4a05c97a7b1f4458d12b0cc178f92fa82cac`
- 开发样本（仓库原始文件，UTF-8、LF）：`c45874888022586a422aeee70b152c1d31471f29c9b4936ede8f0a477114410e`
- 开发样本（Windows 工作副本，UTF-8、CRLF）：`10180c9ec9bad0df8edcd0fcb13e1cae11ef6f1c5a584cfe17722b6864d105aa`

SHA-256 按文件原始字节计算。从 GitHub 下载原始 JSON 时使用 LF 版本的校验值；若工作副本被 Git 转为 CRLF，则使用 CRLF 版本的值。
