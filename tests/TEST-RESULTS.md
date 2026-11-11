# 内容运营 Skill/MCP 集合 · 实测报告（第二批 8 项）

测试时间：2026-11-11（Asia/Shanghai）。环境：Linux 容器，无 go / docker / uv，有 node v24、python 3.12。原则：只做安装与启动级验证，不注册账号、不填任何凭据、不付费；每项结论均有实际命令输出或页面内容支撑。测试目录：`~/workspace/skill-tests/`。

> 第一批已完成 2 项（不在本文重复）：Humanizer-zh 实测通过；stitch-skills 结构验证通过（3 个 plugin、16 个 SKILL.md、frontmatter 规范），完整生成需 Stitch MCP 接入。

---

## 1. xpzouying/xiaohongshu-mcp（小红书）

**测试方法**：从 GitHub releases 下载 v2.7.3 的 `xiaohongshu-mcp-linux-amd64` 二进制（17 MB，Go 静态编译），运行 `--help` 后直接启动服务；服务起来后对 `http://localhost:18060/mcp` 做标准 MCP 握手（initialize → tools/list），并调用只读工具 `check_login_status`。未尝试任何登录。

**实测结果**：
- `--help` 正常：参数含 `-headless`（默认 true）、`-port`（默认 `:18060`）、`-token`（鉴权 Token）。
- 启动日志：`xiaohongshu-mcp version: v2.7.3`；首次运行自动下载内置浏览器（Chromium 148.0.7778.215，约 140–190 MB，实测缓存目录长到 207 MB）并解压；约 4 分钟后日志打出 `Registered 18 MCP tools`、`MCP Server initialized with official SDK`、`启动 HTTP 服务器: :18060`。
- MCP 握手成功：initialize 返回 `serverInfo: {"name":"xiaohongshu-mcp","version":"2.0.0"}`，protocolVersion 2024-11-05。
- tools/list 完整返回 18 个工具：check_login_status、delete_cookies、favorite_feed、get_feed_detail、get_login_qrcode、get_my_profile、get_unread_count、like_feed、like_notification、list_feeds、list_notifications、post_comment_to_feed、publish_content、publish_with_video、reply_comment_in_feed、reply_notification、search_feeds、user_profile。
- 调用 `check_login_status` 返回内部错误：`navigation failed: net::ERR_TUNNEL_CONNECTION_FAILED`——本沙箱网络环境下内置浏览器无法直连小红书站点，导航失败（与未登录是两回事，如实记录）。

**结论：部分通过**。二进制、服务、MCP 协议层全部真实可用；业务功能卡点有两个：① 本机沙箱网络下内置浏览器直连小红书失败（ERR_TUNNEL_CONNECTION_FAILED），正常网络环境需复测；② 实际使用需用户本人用小红书 App 扫码登录（get_login_qrcode），本次按要求未登录。

## 2. 6551Team/opentwitter-mcp（推特 / X）

**测试方法**：按 pyproject 说明在 venv 中 `pip install ./opentwitter-mcp`（本地浅克隆），然后直接运行入口命令 `opentwitter-mcp`（config.json 中 api_token 为空、未设环境变量）。

**实测结果**：
- 安装成功（exit 0），依赖为 mcp[cli]、httpx。
- 启动立即崩溃，traceback 最后一行：`ValueError: OPENNEWS_TOKEN not configured. Get your API token at http://app.newsliquid.com/mcp, then set the OPENNEWS_TOKEN environment variable or configure api_token in config.json.`
- 源码核对：`src/opentwitter_mcp/config.py` 在导入期就检查 token，缺失直接抛错；API 基址为 `https://ai.6551.io`（6551 的付费数据 API），tools.py 定义了 get_twitter_user、search_twitter、get_twitter_kol_followers 等 10 个工具，但无 token 根本起不来。

**结论：部分通过**。可正常安装，启动卡在缺少 6551 的付费 API Token（OPENNEWS_TOKEN）——与调研预期一致，需付费购买后才能进一步验证工具调用。

## 3. MiniMax-AI/MiniMax-MCP（图片）

**测试方法**：新建 python venv，`pip install minimax-mcp`（PyPI 官方包，装到 0.0.19），不设任何环境变量直接启动 `minimax-mcp` 并喂入 MCP initialize / tools/list 请求。

**实测结果**：
- 安装成功（exit 0）。
- 启动立即退出，stderr：`File ".../minimax_mcp/server.py", line 42, in <module> raise ValueError("MINIMAX_API_KEY environment variable is required")`。
- 即 server 在导入期强制检查 MINIMAX_API_KEY，无 key 连工具列表都拿不到（比 Figma 那款更严格）。

**结论：部分通过**。官方包可正常安装，启动卡在缺少 MINIMAX_API_KEY（MiniMax 平台付费 API 密钥；README 另注明 key 与区域 host 必须匹配：国内 https://api.minimaxi.com / 全球 https://api.minimax.io）。

## 4. GLips/Figma-Context-MCP（视觉设计）

**测试方法**：`npx -y figma-developer-mcp --help` 确认包可拉取运行；再以 `--stdio` 模式无 token 启动并喂入 MCP initialize / tools/list 请求。

**实测结果**：
- npx 成功下载并运行，版本 `figma-developer-mcp v0.13.2`；`--help` 输出完整，含 `--figma-api-key`、`--figma-oauth-token`、`--stdio`、`--port` 等参数。
- 无 token 以 stdio 启动时立即报错退出，stderr 只有一行：`Either FIGMA_API_KEY or FIGMA_OAUTH_TOKEN is required (via CLI argument or .env file)`。

**结论：部分通过**。npx 一键可跑、版本与参数齐全，启动卡在缺少 Figma Personal Access Token（或 OAuth Token）——与调研预期一致；有 token 后才能验证取稿数据。

## 5. geekjourneyx/md2wechat-skill（微信公众号运营）

**测试方法**：GitHub releases 有预编译二进制（v3.8.0，含 linux-amd64，约 20 MB），无需装 Go。下载后跑 `--help`、`doctor`、`themes list --json`、`layout list/show/render`，并用自备示例 Markdown 分别跑 `convert`（api 模式）、`convert --mode ai`、`preview`。未填任何公众号凭据，未测推草稿箱。

**实测结果**：
- 二进制开箱即用，子命令很全：convert / preview / create_draft / generate_cover / generate_image / humanize / layout / themes / doctor 等；`--help` 注明推草稿/上传需 WECHAT_APPID、WECHAT_SECRET。
- `doctor` 输出：config 与 59 个 layout 模块目录加载 PASS；`FAIL api.config - missing API conversion configuration: MD2WECHAT_API_KEY`；`WARN wechat.config - draft creation is not ready; missing WECHAT_APPID, WECHAT_SECRET`，并明确提示「Skip draft commands if you only need local convert or preview」。
- `themes list --json` 本地可用：返回完整主题目录（api 主题 50+ 个，如 apple、sspai-red、github-readme、wechat-native 等；ai 主题 4 个：autumn-warm、ocean-calm、spring-fresh、custom）。
- `convert`（默认 api 模式）与 `preview` 均被挡：`{"success":false,"code":"CONVERT_INVALID","message":"MD2WECHAT_API_KEY is required for API mode"}`——成稿 HTML 转换走项目方云 API，需要它自己的 MD2WECHAT_API_KEY（不是公众号凭据）。
- `convert --mode ai --theme autumn-warm sample.md` 无 key 成功：返回 `CONVERT_AI_REQUEST_READY`（status: action_required），生成一份 4721 字的完整排版设计提示词（主题「秋日暖光」），按其 Agent-Skill 设计由宿主 Agent 拿这份 prompt 去生成最终 HTML——工具本身不直接产 HTML。
- `layout render author-card --var name=测试作者 --var bio=...` 本地成功（LAYOUT_RENDERED），59 个高级排版模块的目录、规格（layout show）与渲染在本地均可用。

**结论：部分通过**。CLI 本体、主题/模块目录、AI 模式提示词生成全部本地真实可用，无需 Go 环境（有官方预编译二进制）；但两条成稿路径都有前置条件：api 模式需 MD2WECHAT_API_KEY（项目方 key，本次未填），ai 模式只产出提示词、需宿主 Agent 接力生成 HTML；推送草稿箱还需 WECHAT_APPID / WECHAT_SECRET（按要求未测）。

## 6. sansan0/TrendRadar（选题创意）

**测试方法**：git clone 后建 venv 用 pip 按 pyproject 安装依赖（不用 docker、不用 uv），默认 config/config.yaml（AI 分析 key 留空），运行 `python -m trendradar` 做一次核心抓取，超时上限约 9 分钟。

**实测结果**：
- 安装有个坑，先后踩了两次：① 第一次运行时报 `ModuleNotFoundError: No module named 'litellm'`；② 排查发现 pip 自行解析出 pydantic 2.14.3，与 litellm 1.82.6 不兼容（`ImportError: cannot import name 'eval_type_backport'`）。项目主推 uv 按 uv.lock 锁定版本（pydantic 2.12.2）；手动 `pip install pydantic==2.12.2` 对齐后，`import litellm, fastmcp, trendradar` 全部通过（trendradar 6.11.0）。
- 对齐后正式运行 `python -m trendradar`，完整跑通并正常退出（exit 0）。日志关键行：
  - `读取到 255 个标题`，来源 11 个平台：baidu、bilibili-hot-search、cls-hot、douyin、ifeng、thepaper、tieba、toutiao、wallstreetcn-hot、weibo、zhihu。
  - `255 条当前榜单新闻中有 44 条频率词匹配`（默认频率词过滤生效）。
  - AI 分析按预期跳过：`[AI] 配置警告: 未配置 AI API Key` → `分析失败: 未配置 AI API Key`，仅警告不崩溃，主流程继续（默认模型配置为 deepseek/deepseek-v4-flash）；翻译步骤同样因无 key 跳过。
  - `HTML报告已生成: output/html/2026-11-11/01-27.html`，`最新报告已更新: output/html/latest/current.html`；通知因未配渠道跳过（仅警告）。
- 产出文件实查：HTML 报告 144 KB（标题「热点新闻分析」）；`output/news/2026-11-11.db`（282 KB）中 news_items 表实有 255 条，样本标题为当下真实热榜（如「2026年布克奖揭晓，81岁英国科幻作家成为史上最年长获奖者」）；另生成 `output/rss/2026-11-11.db`、`output/index.html`。

**结论：通过**。核心抓取—过滤—出报告全链路真实跑通，255 条热榜数据落盘可查；AI 分析/翻译在无 key 时优雅跳过（用 AI 功能需另配 AI_API_KEY）。唯一摩擦：脱离 uv 用 pip 安装时有依赖版本坑，需按 uv.lock 对齐 pydantic==2.12.2。

## 7. doocs/md（排版撰写）

**测试方法**：用 browser.open 打开官方在线版 https://doocs.github.io/md/ ，核对页面可达性、标题与界面内容。

**实测结果**：
- 页面可达，标题为 "WeChat Markdown Editor"，抓取时间为测试当下（2026-11-10 17:25 UTC）。
- 应用完整加载：页面呈现编辑器自带的整篇示例文档《Explore the Wonderful World of Markdown》，且不只是源码文本——抓取到的内容包含渲染后的结构（标题层级、加粗/斜体/删除线/高亮、列表、表格、引用、代码块，以及 LaTeX 公式、Mermaid/PlantUML、Callouts 等高级语法的渲染占位与说明），即编辑+实时预览的成品界面。
- 文档内可见编辑器功能线索（如「Edit → Insert table」「Format → Convert external WeChat links to footnotes」菜单说明），与仓库定位（微信 Markdown 编辑器）一致。

**结论：通过**。在线版真实可达且应用完整加载渲染，零安装即可用；说明一点：本次为页面内容抓取验证，未做交互输入实测（抓取工具不能打字），但编辑器本体与预览渲染均已确认工作。

## 8. all-in-aigc/aicover（封面）

**测试方法**：用 browser.open 打开仓库 README 标注的 Live Demo：https://aicover.design ，核对在线版可达性与功能界面。

**实测结果**：
- 域名可达，但内容已完全不是 AI Cover：页面标题是 "WorkAny Bot"（WorkAny - Desktop Agent for Any Task），通篇是 "WorkAny Bot / OpenClaw Hosting" 云端 Agent 的介绍与定价（Cloud Bot、Personal Assistant 套餐、$60/$180 credits 等），图片资源也指向 workany.ai。
- 也就是说 aicover.design 这个域名现在承载的是另一个无关产品，README 里链接的封面生成在线 Demo 已经不存在/被替换，无法进入任何封面生成界面，更谈不上走到填 API Key 生成那一步。

**结论：未通过（在线版）**。卡点不在 API Key，而是更靠前：官方在线 Demo 已失效（域名内容被替换为无关产品 WorkAny）。GitHub 仓库代码仍在（本次未实测自部署），理论上可自行 clone 部署并自备图片生成 API Key 使用，但「开箱即用的在线版」这一条已经没了——这也意味着调研报告里它「可用性 8 分（有在线 demo）」的依据不复存在，实际应下调。

---

## 汇总（第二批 8 项）

| 项目 | 结论 | 卡点 |
|---|---|---|
| xiaohongshu-mcp | 部分通过 | 本机网络下浏览器直连小红书失败；需用户本人扫码登录 |
| opentwitter-mcp | 部分通过 | 缺 6551 付费 API Token（OPENNEWS_TOKEN） |
| MiniMax-MCP | 部分通过 | 缺 MINIMAX_API_KEY |
| Figma-Context-MCP | 部分通过 | 缺 Figma API Token |
| md2wechat-skill | 部分通过 | api 模式需 MD2WECHAT_API_KEY；草稿需公众号 AppID/Secret |
| TrendRadar | 通过 | —（核心抓取全链路跑通；AI 分析需另配 AI_API_KEY，pip 安装需对齐 pydantic==2.12.2） |
| doocs/md | 通过 | —（在线版零安装可用） |
| aicover | 未通过 | 在线 Demo 已失效：aicover.design 已变成无关产品 |

第二批 8 项总计：通过 2（TrendRadar、doocs/md）、部分通过 5（xiaohongshu-mcp、opentwitter-mcp、MiniMax-MCP、Figma-Context-MCP、md2wechat-skill，全部卡在各自的密钥/登录，安装与启动本身均无问题）、未通过 1（aicover，在线 Demo 已失效）。
