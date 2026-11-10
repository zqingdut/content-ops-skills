# 内容运营 Skills / MCP 精选集合

> 10 个内容运营方向，每个方向只收录 **一个** 项目：在 GitHub 上 star > 1000 的 Skill / MCP / 工具中，按五维评分调研后留下的最高分。

调研日期：2026-11-11。完整评分过程、落选候选与取舍理由见 [RESEARCH.md](./RESEARCH.md)。10 个入选项目已于同日全部装机实测（通过 3、部分通过 6、未通过 1），结果与两处分数修正见 RESEARCH.md 的"实测结果"一节。

## 评分维度（每维 0–10，总分 50）

**安全性**（许可证、凭据处理、代码可审计性、平台风险）· **评价**（star/fork 与社区采用）· **专业度**（文档、测试、工程规范）· **可用性**（维护活跃度与功能完整度）· **易用性**（上手成本与中文友好度）

## 入选名单

| 方向 | 项目 | ★ | 总分 | 一句话 |
|---|---|---|---|---|
| 小红书 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | 17,063 | 41 | 本地 MCP 驱动已登录账号：搜索、发布、互动、达人数据 |
| 推特 X | [6551Team/opentwitter-mcp](https://github.com/6551Team/opentwitter-mcp) | 1,439 | 34 | X 数据侧 MCP：资料、搜索、粉丝事件、KOL 追踪 |
| 微信公众号运营 | [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) | 3,790 | 40 | Agent CLI：Markdown → 排版 → 配图/封面 → 草稿箱全链路 |
| 排版撰写 | [doocs/md](https://github.com/doocs/md) | 13,521 | 45 | 微信 Markdown 编辑器事实标准，主题与图床生态齐全 |
| 封面 | [all-in-aigc/aicover](https://github.com/all-in-aigc/aicover) | 1,796 | 27 | AI 封面生成器（在线 Demo 已失效，需自部署） |
| 图片 | [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 1,598 | 40 | MiniMax 官方 MCP：图/视频/音频全模态生成 |
| 去 AI 味 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 22,487 | 47 | 中文原生去 AI 味 Skill，保留作者声音，npx 一键装 |
| 视觉设计 | [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | 16,187 | 42 | Figma → Agent 的事实标准 MCP（Framelink） |
| 前端设计 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 8,722 | 42 | Google 官方 Skills 库：自然语言生成 UI 设计 |
| 选题创意 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 63,566 | 45 | 多平台热榜聚合 + AI 筛选，自带 MCP Server |

## 使用前的安全提示

- **小红书 MCP**：扫码登录、cookie 存本地，但自动化操作账号有平台风控风险，建议先用小号。
- **opentwitter-mcp**：依赖 6551 第三方数据 API（付费 Key、请求经第三方），只做数据读取，不做发推；敏感数据慎用。
- **公众号 / 图片类**：凭据与 API Key 均为本地配置或环境变量，使用前先读各仓库的配置说明。
- **去 AI 味类**：纯文本规则 Skill，零凭据零网络，两件同分（47），按中文场景贴合度选了 Humanizer-zh；英文内容可用其上游原典 [blader/humanizer](https://github.com/blader/humanizer)（67,453★）。
- **aicover**：实测发现其在线 Demo 域名已被替换为无关产品，只剩自部署一条路，分数已下调（35→27），入选仅因它是本方向唯一过门槛者。

## 落选但值得知道

- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)（110,860★）：Agent 通用上网套件，单项不专精而未按方向入选，可能是全场最值得装的一个。
- [chubbyguan/chubbyskills](https://github.com/chubbyguan/chubbyskills)（1,323★）：中文全渠道内容采集 14 个 Skill，与国内内容矩阵最贴，单项深度不及各方向冠军。
- [caol64/wenyan-mcp](https://github.com/caol64/wenyan-mcp)（1,357★）：Agent 原生排版+发布到公众号，想全自动时是 doocs/md 的备选。

---

star 数为 2026-11-11 当日数据；评分为基于公开信息（文档、许可证、维护活跃度、凭据模型）的调研判断，非实测跑分；各项目许可证以其仓库 LICENSE 为准。本仓库只做索引与评价，不收录任何第三方代码。
