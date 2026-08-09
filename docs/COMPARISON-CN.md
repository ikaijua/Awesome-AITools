# AI Agent Tools 对比：Claude Code vs Codex vs Kimi Code vs Grok Build vs Qoder vs Antigravity

本文档对比六款主流的 AI Agent 编程工具：Claude Code、Codex、Kimi Code、Grok Build、Qoder，以及 Google 推出的智能体优先开发平台 —— Antigravity。

## 快速对比

| 方面 | Claude Code | Codex | Kimi Code | Grok Build | Qoder | Antigravity |
|------|-------------|-------|-----------|------------|-------|-------------|
| 开发者 | Anthropic | OpenAI | Moonshot AI | xAI | 阿里云 | Google |
| 形态 | 终端 CLI + IDE 插件 + 桌面/Web/App | 终端 CLI + IDE 扩展 + 桌面 App + Codex Web | 终端 CLI + ACP 编辑器 + 本地 Web UI | 终端 TUI/CLI + ACP 嵌入 + 无头模式 | 桌面 IDE + CLI + Work + Wake + Cloud Agents | 桌面 App + IDE + CLI (`agy`) + SDK |
| 开源 | ❌ | ✅ Apache-2.0 | ⚠️ CLI 使用 MIT，核心服务不开源 | ✅ Apache-2.0（不接受外部贡献） | ❌ | ❌（预览期免费） |
| 默认模型 | Claude 系列（Opus / Sonnet / Haiku） | GPT-5.x / Codex 系列 | Kimi Code / Moonshot 模型 | Grok 系列 | 通义 / 百炼模型 | Gemini 3.5 / 3.6 Flash |
| 其他模型 | — | — | 可配置兼容供应商 | — | 可配置阿里云百炼等 | Gemini 3 Pro、Claude、GPT-OSS 等 |
| 账号要求 | Anthropic API 或 Claude 账户 | OpenAI API 或 ChatGPT 账户 | Kimi 账户或 API Key | xAI / X 账户 | 阿里云账号 | Google 账户 |
| 多模态 | 文本 + 图片 | 文本 + 图片 | 文本 + 图片/视频 | 文本 + 图片 | 文本 + 图片 | 文本 + 图片 + 内置浏览器 |
| 持久记忆 | ✅ 项目级 + 用户级记忆 | ⚠️ 会话内 + 跨端 relay 同步 | ✅ 会话/Goal 记忆 | ⚠️ 会话 + checkpoints | ✅ 知识引擎 + 自适应记忆 | ✅ 跨运行学习 + 项目上下文 |
| 多智能体 | ✅ 子代理 + workflows | ✅ 子代理 | ✅ 子代理 | ✅ 子代理 | ✅ 多智能体协同 | ✅ Manager 视图跨工作区分发 |
| 本地/云端 | 本地优先，`--cloud` 可选 | 本地 + Codex Cloud | 本地优先，`kimi web` 本地 server | 本地 | 本地 Desktop/CLI/Work + Cloud Agents | 本地桌面 App/IDE/CLI + 托管 Agent 服务 |
| 跨端继续 | ✅ Remote Control + 手机/Web | ✅ ChatGPT relay（手机/桌面/Web） | ✅ `kimi web` 同 server 多端访问 | ❌ | ✅ 远程控制 + Mobile 同步 | ⚠️ 弱 |
| 权限模式 | `--permission-mode` default/plan/auto | `--approval-mode` suggest/auto-edit/full-auto + sandbox | Manual / YOLO / Auto / Plan | 交互确认 / 无头模式 | 确认 / Agent 模式 | Read Only / Auto / Full Access；先审计划 Artifact |
| 扩展性 | MCP、Skills、Hooks、Plugins | MCP、Skills、Plugins、Hooks | MCP、Skills、Hooks、ACP | MCP、Skills、Plugins、Hooks、沙箱 | MCP、内置工具、IDE 插件 | VS Code 扩展、SDK、内置浏览器/终端 |

## 详细对比

### 代码理解与上下文记忆

**Claude Code**
- 长上下文，能跨多文件深度理解
- 跨会话持久记忆（用户级 + 项目级）
- 通过 `CLAUDE.md` / `AGENTS.md` 定义项目规则

**Codex**
- 本地仓库级代码理解，可执行多步骤任务
- 会话状态跨设备通过 ChatGPT relay 同步
- 依赖 `AGENTS.md` 和项目 prompt 提供长期上下文

**Kimi Code**
- 终端内分析项目结构、依赖和实现细节
- 支持 Goal 模式，长任务可跨多轮推进
- 通过 `AGENTS.md` 与项目本地记忆保持一致

**Grok Build**
- 全屏 TUI 中理解代码库、搜索、编辑、运行命令
- 工作区 checkpoints 保存会话状态
- 适合长时间运行的终端内任务

**Qoder**
- 深度代码库分析 + 自适应记忆与知识引擎
- 多智能体协同，角色分工（规划、编码、测试、审查）
- 目标导向的“规划 → 执行 → 验证 → 迭代”闭环

**Antigravity**
- 智能体优先：规划 → 编辑 → 运行 → 验证，上下文随步骤传递
- 桌面 App、IDE、CLI（`agy`）、SDK 四种形态共享同一套智能体引擎
- 支持 Projects、多工作区、子代理、Hooks 与定时任务
- 项目上下文以工作区为锚；内置浏览器把运行期信息回灌给智能体

### 安全与可控性

**Claude Code**
- 危险操作（删除文件、强制推送等）默认需确认
- `--permission-mode` 提供 default / plan / auto 三档
- 支持 `--dangerously-skip-permissions` 用于可信场景

**Codex**
- 审批模式 `suggest` / `auto-edit` / `full-auto` 控制自动程度
- 沙箱 `read-only` / `workspace-write` / `danger-full-access` 控制访问范围
- 内核级沙箱 + ChatGPT relay，不暴露本地端口

**Kimi Code**
- Manual / YOLO / Auto / Plan 四种权限模式
- `kimi web` 在本地启动 server，文件不离开本机
- 敏感操作默认需要确认

**Grok Build**
- 交互式 TUI 中逐步确认；无头模式用于 CI/脚本
- 内置沙箱与工作区 checkpoints
- 本地运行时文件和命令都在本机执行

**Qoder**
- Agent 模式前需要用户确认关键操作
- 本地 Desktop/CLI/Work 与云端 Cloud Agents 分离
- 企业版支持私有化/云端合规部署

**Antigravity**
- 智能体先生成**计划 Artifact**，人工批准后再执行
- 浏览器录屏与截图让事后审计成为可能
- Read Only / Auto / Full Access 模式，Full Access 下仍先审计划 Artifact
- 访问范围限定在工作区，桌面 App / IDE / CLI 均可使用

### 扩展与集成

**Claude Code**
- MCP 服务器连接数据库、浏览器、外部 API
- Skills / Hooks / Plugins 实现可复用工作流
- 深度 Git / GitHub / GitLab / CI/CD 集成

**Codex**
- MCP、Skills、Plugins、Hooks
- `codex exec` 适合脚本和 CI
- 与 ChatGPT 生态共享账号和会话

**Kimi Code**
- MCP、Skills、Hooks
- ACP 编辑器集成（Zed、JetBrains 等）
- `kimi web` 提供本地浏览器 UI

**Grok Build**
- MCP、Skills、Plugins、Hooks
- ACP 编辑器嵌入与无头模式
- 主题、配置、checkpoints 可定制

**Qoder**
- MCP、内置编程工具、IDE 插件
- Desktop / CLI / Work / Wake / Cloud Agents 产品族
- 远程控制与 Mobile App 同步

**Antigravity**
- 桌面 App / IDE 基于 VS Code，可直接复用其扩展生态
- 内置浏览器，智能体可自行点击、跳转、截图
- CLI（`agy`）支持 Skills、Plugins、Hooks、MCP
- SDK 可用 Python 脚本自定义智能体
- 在模型选择器中可切换 Gemini / Claude / GPT-OSS 多模型

### 跨端与协作

**Claude Code**
- `claude remote-control` / `/remote-control` 让手机/浏览器继续本地会话
- `claude --cloud` 可在移动端继续
- 文件、凭证保留在本地机器

**Codex**
- ChatGPT mobile app 可连接本地/远程 Codex 会话
- ChatGPT relay 在手机、桌面、Web 之间同步活跃会话
- Remote SSH 连接远程环境

**Kimi Code**
- `kimi web` 启动本地 server，局域网内多端访问
- 同一 server 下手机/浏览器可查看任务进展
- 支持 Goal 状态在 Web UI 中查看

**Grok Build**
- 当前主要面向单机终端使用
- 无官方跨端同步或手机 App

**Qoder**
- Qoder 网页版可远程控制本地任务
- Mobile App 与 Desktop/CLI 实时同步
- Cloud Agents 支持关闭电脑后继续运行

**Antigravity**
- 桌面 App / IDE / CLI 主要本地运行
- 提供托管 Agent 服务（Gemini Enterprise Agent Platform）
- 跨端继续会话能力较弱，暂不支持手机直接继续本地会话

## 选择建议

### 选 Claude Code 如果你需要：
- 深入理解并重构大型、成熟代码库
- 强大的项目记忆 + Skills/Hooks 长链路工作流
- 从手机或 Web 继续本地会话的 Remote Control
- 成熟的权限模型和广泛的工具集成

### 选 Codex 如果你需要：
- 开源（Apache-2.0）终端智能体，可自由审查和定制
- 与 ChatGPT 账号/移动端紧密集成的跨端体验
- 内核级沙箱 + 审批模式，兼顾安全与自动化
- 云端任务（Codex Cloud）和 Remote SSH 支持

### 选 Kimi Code 如果你需要：
- 终端原生 + 本地 Web UI（`kimi web`）的轻量组合
- Goal 模式自主推进长任务
- ACP 编辑器集成和国内模型/网络环境

### 选 Grok Build 如果你需要：
- 开源、基于 Rust 的高性能终端 TUI 智能体
- 全屏鼠标交互、checkpoints、无头模式
- 与 xAI / Grok 模型生态深度集成

### 选 Qoder 如果你需要：
- 覆盖 Desktop / CLI / Work / Wake / Cloud Agents 的全产品族
- 多智能体协同 + 知识引擎 + 远程控制
- 阿里云生态和国内合规部署

### 选 Antigravity 如果你需要：
- 一个智能体优先的开发平台，横跨桌面 App、IDE、CLI（`agy`）和 SDK
- 用 **Manager 视图**并行展开、监控多个智能体
- 通过 Artifacts（计划、截图、录屏）让智能体运行**可核验**
- 让智能体自己驱动浏览器去验证它写出的功能
- 灵活切换模型，默认使用 Gemini 3.5 / 3.6 Flash
- 项目上下文、多工作区编排、子智能体、Hooks 与定时任务

## 组合使用

这些工具并不互斥，常见分工：

- **日常终端开发**：Claude Code、Codex、Kimi Code、Grok Build
- **国内环境与全产品族**：Qoder
- **浏览器验证 / IDE 化体验**：Antigravity
- **快速单文件修改**：Codex、Grok Build
- **长链路多文件重构**：Claude Code、Qoder、Antigravity
- **跨端继续任务**：Claude Code（Remote Control）、Codex（ChatGPT relay）、Kimi Code（`kimi web`）、Qoder（远程控制）

## 相关链接

- [Claude Code 入门介绍](claude-code/README-CN.md)
- [Codex 入门介绍](codex/README-CN.md)
- [Kimi Code 入门介绍](kimi-code/README-CN.md)
- [Grok Build 入门介绍](grok-build/README-CN.md)
- [Qoder 入门介绍](qoder/README-CN.md)
- [Antigravity 入门介绍](antigravity/README-CN.md)
