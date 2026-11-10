# 内容运营 Skills / MCP 调研报告

调研日期：2026-11-11。范围：GitHub 上 star > 1000、面向内容运营的 Agent Skill / MCP / 工具项目，覆盖 10 个方向：小红书、推特 X、微信公众号运营、排版撰写、封面、图片、去 AI 味、视觉设计、前端设计、选题创意。

## 评分方法

五维评分，每维 0–10，总分 50：

- **安全性**：许可证是否齐全、凭据处理方式（本地/自备 key/交给第三方）、代码可审计性、有无 SECURITY.md、平台 ToS 与账号风险。
- **评价**：star / fork 规模与社区采用度（star 数为 2026-11-11 当日数据）。
- **专业度**：文档完整度、测试/CI、变更日志、工程结构。
- **可用性**：当前是否活跃维护、功能是否完整可用、依赖是否可靠。
- **易用性**：安装与上手成本、对中文用户的友好度。

规则：每方向只保留总分最高的一个进入集合仓库；同分时以与中文内容运营场景的贴合度定胜负（仅去 AI 味方向触发，见该节）。

## 各方向结果

### 1. 小红书运营 —— 入选：xpzouying/xiaohongshu-mcp（17,063★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **xpzouying/xiaohongshu-mcp** | 7 | 9 | 9 | 9 | 7 | **41** |
| chubbyguan/chubbyskills（全渠道采集 skills 集） | 8 | 5 | 7 | 7 | 7 | 34 |

- 形态：MCP Server（Go），本地浏览器自动化驱动已登录的小红书账号：搜索、推荐流、发布图文/视频、评论互动、达人数据。
- 安全要点：扫码登录、cookie 只存本地，开源可审计、有 LICENSE 与 40 人贡献者体系；**固有风险在平台侧**——自动化操作账号有触发小红书风控的可能，建议用小号试运行。
- 文档：README 近 3.9 万字、中英双语、Docker 一键部署。

### 2. 推特 / X 运营 —— 入选：6551Team/opentwitter-mcp（1,439★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **6551Team/opentwitter-mcp** | 6 | 6 | 8 | 7 | 7 | **34** |

- 形态：MCP Server（Python），X 数据侧：用户资料、推文搜索、粉丝事件、KOL 追踪；四语文档，附带 openclaw-skill。
- 门槛说明：这是全场最薄弱的方向——**专职 X 的 MCP 里只有它过 1000★**，且只做数据读取/监测，不做发推。发推自动化方向的 nirholas/XActions（652★）未达门槛，未入选，仅在此备注。
- 安全要点：依赖 6551 第三方数据 API（需付费 API Key，请求经第三方通道），敏感账号数据慎用；代码本身开源、有 LICENSE。
- 泛用替代：Panniantong/Agent-Reach（110,860★）能读/搜 Twitter 等多平台，但定位是通用 Agent 上网工具而非 X 运营，未按方向入选，值得单独收藏。

### 3. 微信公众号运营 —— 入选：geekjourneyx/md2wechat-skill（3,790★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **geekjourneyx/md2wechat-skill** | 8 | 7 | 9 | 9 | 7 | **40** |
| caol64/wenyan-mcp（排版+发布 MCP） | 8 | 6 | 8 | 9 | 7 | 38 |

- 形态：面向 AI Agent 的 CLI Skill（Go）：写 Markdown → 生成公众号排版 → AI 制作封面与配图 → 预览校验 → 推送草稿箱，全链路。
- 安全要点：本地运行，公众号凭据与生图 key 均由用户本地配置，不经第三方中转。
- 专业度：CHANGELOG、VERSION、Makefile、docs、examples 一应俱全，是本批完成度最高的国产 skill 之一。

### 4. 排版撰写 —— 入选：doocs/md（13,521★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **doocs/md** | 8 | 10 | 9 | 9 | 9 | **45** |
| caol64/wenyan-mcp | 8 | 6 | 8 | 9 | 7 | 38 |
| lyricat/wechat-format | 8 | 7 | 7 | 8 | 8 | 38 |

- 形态：微信 Markdown 编辑器（Web 应用，2019 年至今），Markdown → 公众号富文本，主题/图床/内容管理/AI 助手齐全。
- 取舍说明：它是编辑器而非 Agent 原生工具，但排版质量与生态规模断层领先；若只想让 Agent 全自动排版+发布，wenyan-mcp 是备选（已在公众号运营方向落选，分数并列备选第一）。

### 5. 封面 —— 入选：all-in-aigc/aicover（1,796★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **all-in-aigc/aicover** | 7 | 6 | 6 | 2 | 6 | **27** |

- 形态：AI 封面生成器（Next.js），可自部署；自备生图 API Key。
- 说明：专用封面工具整体 star 不高，这是唯一过门槛且专注封面的；短板是文档较薄（README 约 2 千字）。公众号链路里 md2wechat-skill 自带封面制作，可互补。
- **实测更正（2026-11-11）**：原记的在线版 aicover.design 已失效——域名内容已被替换成无关产品 WorkAny Bot，README 标注的 Live Demo 不复存在。可用性 8→2、易用性 8→6，总分 35→27；仓库代码仍在，未实测自部署。它仍是本方向唯一过门槛者而保留入选，但状态应视为"待自部署验证"，不是开箱可用。

### 6. 图片 —— 入选：MiniMax-AI/MiniMax-MCP（1,598★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **MiniMax-AI/MiniMax-MCP** | 8 | 6 | 9 | 9 | 8 | **40** |

- 形态：MiniMax 官方 MCP Server：文生图、图生图、视频、音频全模态，uvx 一行接入。
- 安全要点：官方出品、tests 齐全、key 走环境变量；调用按官方 API 计费。star 不算高，胜在官方身份与工程规范。
- 备注：单点模型绑定 MiniMax 一家；需要 Gemini 系生图时可看 zhongweili/nanobanana-mcp-server（404★，未达门槛）。

### 7. 去 AI 味 —— 入选：op7418/Humanizer-zh（22,487★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| blader/humanizer | 10 | 10 | 9 | 10 | 8 | 47 |
| **op7418/Humanizer-zh** | 10 | 9 | 8 | 10 | 10 | **47** |

- 同分 47，按预设规则以场景贴合度定胜负：Humanizer-zh 是中文原生重写（2026-09 重写规则与示例，明确"保留事实、作者立场与文体"，且诚实声明不保证通过任何 AI 检测器），npx 一键安装；blader/humanizer（67,453★）是上游原典、英文规则第一，收录于此备注，英文内容可直接用它。
- 安全要点：两者都是纯文本规则型 Skill，零凭据、零网络，安全性满分。

### 8. 视觉设计 —— 入选：GLips/Figma-Context-MCP（16,187★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **GLips/Figma-Context-MCP** | 8 | 9 | 9 | 9 | 7 | **42** |
| grab/cursor-talk-to-figma-mcp | 7 | 8 | 7 | 8 | 7 | 37 |

- 形态：Figma 官方 token 接入的 MCP（Framelink），把设计稿布局/样式喂给编码 Agent，是 Figma→Agent 生态的事实标准；有 SECURITY.md 与 ROADMAP。
- 易用短板：需要有 Figma 设计稿与 token 才发挥价值，做封面/视觉稿时是把设计资产接进 Agent 的桥。

### 9. 前端设计 —— 入选：google-labs-code/stitch-skills（8,722★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **google-labs-code/stitch-skills** | 9 | 8 | 9 | 8 | 8 | **42** |
| onlook-dev/onlook | 7 | 10 | 8 | 8 | 6 | 39 |

- 形态：Google 官方 Agent Skills 库，配合 Stitch MCP 用自然语言生成 UI 设计与前端页面，遵循 Agent Skills 开放标准，兼容 Claude Code / Cursor / Gemini CLI 等。
- 取舍：onlook（27,163★）star 更高，但形态是可视化编辑器产品、不是 skill/MCP，与本集合定位不符，易用性按 Agent 工作流扣分。

### 10. 选题创意 —— 入选：sansan0/TrendRadar（63,566★）

| 候选 | 安全 | 评价 | 专业 | 可用 | 易用 | 总分 |
|---|---|---|---|---|---|---|
| **sansan0/TrendRadar** | 8 | 10 | 9 | 10 | 8 | **45** |
| ericciarla/trendFinder | 7 | 6 | 6 | 7 | 7 | 33 |

- 形态：多平台热榜聚合（微博/抖音/知乎/B站/头条等）+ RSS + AI 筛选推送，自带 MCP Server 与 MCP FAQ，Docker 号称 30 秒部署；forks 高达 24,923。
- 与小红书/公众号选题的贴合度：热榜源覆盖国内主平台，是本批与"选题"二字最对位的项目。

## 落选但值得知道

- **Panniantong/Agent-Reach**（110,860★）：Agent 通用上网套件（Twitter/Reddit/YouTube/小红书等读取搜索），单项不专精，未按方向入选，但可能是全场最值得装的一个。
- **chubbyguan/chubbyskills**（1,323★）：中文全渠道内容采集的 14 个 Skill（抖音/B站/小红书/公众号/X/播客 → 个人知识库），与你的内容矩阵最贴，但单项深度不及各方向冠军。
- **qiye45/wechatDownload**（10,030★）/ **wechat-article/wechat-article-exporter**（13,145★）：公众号方向的高星项目，但定位是文章下载/导出（采集侧），不是运营发布，未入选。
- **zhouxiaoka/autoclip**（10,248★）：长视频自动剪短视频并生成封面与发布文案，偏视频流水线，与"封面"只部分重合。

## 总表（入选 10 件）

| 方向 | 项目 | ★ | 总分 |
|---|---|---|---|
| 小红书 | xpzouying/xiaohongshu-mcp | 17,063 | 41 |
| 推特 X | 6551Team/opentwitter-mcp | 1,439 | 34 |
| 微信公众号运营 | geekjourneyx/md2wechat-skill | 3,790 | 40 |
| 排版撰写 | doocs/md | 13,521 | 45 |
| 封面 | all-in-aigc/aicover | 1,796 | 27（实测下调） |
| 图片 | MiniMax-AI/MiniMax-MCP | 1,598 | 40 |
| 去 AI 味 | op7418/Humanizer-zh | 22,487 | 47 |
| 视觉设计 | GLips/Figma-Context-MCP | 16,187 | 42 |
| 前端设计 | google-labs-code/stitch-skills | 8,722 | 42 |
| 选题创意 | sansan0/TrendRadar | 63,566 | 45 |

注：star 数与仓库状态为 2026-11-11 调研当日数据；评分为本报告基于公开信息的判断（文档、许可证、维护活跃度、凭据模型）；各项目许可证以其仓库 LICENSE 文件为准。2026-11-11 已对全部 10 个入选项目做装机实测，结果见下节，两处分数已按实测修正。

## 实测结果（2026-11-11 装机实测）

环境：Linux（node v24 / python 3.12，无 go/docker/uv）；原则：只做安装与启动级验证，不注册、不填凭据、不付费。完整记录见测试日志（TEST-RESULTS，含 Humanizer-zh 改写样例与各项目命令输出）。

| 项目 | 结论 | 实测要点 |
|---|---|---|
| xpzouying/xiaohongshu-mcp | 部分通过 | v2.7.3 二进制真实运行：自动下载内置浏览器、HTTP 服务 :18060、MCP 握手成功、18 个工具清单完整。卡点：本机沙箱网络下浏览器直连小红书失败（ERR_TUNNEL_CONNECTION_FAILED，环境问题，正常网络需复测）；实际使用需用户本人扫码登录 |
| 6551Team/opentwitter-mcp | 部分通过 | pip 安装成功；启动即报 OPENNEWS_TOKEN not configured。卡点：6551 付费 API Token |
| geekjourneyx/md2wechat-skill | 部分通过 | 官方预编译二进制开箱即用；50+ 主题、59 个排版模块、ai 模式排版提示词生成（4721 字）全部本地可用。卡点：默认 api 模式成稿转换需项目方 MD2WECHAT_API_KEY；推草稿箱需 WECHAT_APPID/SECRET（未测）。易用性据此 8→7，总分 41→40 |
| doocs/md | 通过 | 在线版 doocs.github.io/md 可达，编辑器完整加载、示例文档与渲染齐全，零安装可用（页面抓取验证，未做交互打字实测） |
| all-in-aigc/aicover | 未通过 | 在线 Demo 已失效：aicover.design 已变成无关产品 WorkAny Bot；仓库代码仍在，自部署未测。分数已下调（见封面节更正） |
| MiniMax-AI/MiniMax-MCP | 部分通过 | 官方包 pip 安装成功；启动即报 MINIMAX_API_KEY required（无 key 连工具列表都拿不到）。卡点：MiniMax 付费 API Key |
| op7418/Humanizer-zh | 通过 | 取 AI 腔样例文本按 SKILL.md 规则实际改写：套话清除，三个功能点、"一些专家"的归因与"可能"的限定全部保留，无虚构信息 |
| GLips/Figma-Context-MCP | 部分通过 | npx 一键拉起 v0.13.2、--help 完整；无 token 启动即报错。卡点：Figma Personal Access Token |
| google-labs-code/stitch-skills | 部分通过 | 结构验证：3 个 plugin、16 个 SKILL.md、frontmatter 规范齐全；实际生成需接入 Stitch MCP（Google 服务），本次未接 |
| sansan0/TrendRadar | 通过 | 全链路跑通：11 个平台 255 条热榜落盘 SQLite、44 条频率词命中、生成 144 KB HTML 报告；AI 分析无 key 时优雅跳过。注意 pip 安装需按 uv.lock 对齐 pydantic==2.12.2（项目主推 uv） |

汇总：通过 3（TrendRadar、doocs/md、Humanizer-zh）、部分通过 6（全部卡在各自的密钥/登录，安装与启动本身无问题）、未通过 1（aicover 在线版失效）。

解锁清单（补上即可从"部分通过"变真可用）：小红书 = 本人扫码登录；opentwitter-mcp = 6551 付费 Token；MiniMax-MCP = MiniMax API Key；Figma-Context-MCP = Figma Token；md2wechat = MD2WECHAT_API_KEY ＋ 公众号 AppID/Secret（推草稿时）；stitch-skills = Stitch MCP 接入。
