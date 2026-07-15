# AI 编程工具对比：Claude Code vs Codex vs Antigravity

本文档对比三款主流的 AI 编程工具：Claude Code、Codex，以及 Google 推出的、用于替代已废弃 Gemini CLI 的智能体优先 IDE —— Antigravity。

## 快速对比

| 方面 | Claude Code | Codex CLI | Antigravity |
|------|-------------|-----------|-------------|
| 开发者 | Anthropic | OpenAI | Google |
| 形态 | 终端 CLI + IDE 插件 + 桌面/Web | 终端 CLI + IDE 扩展 + Web/桌面 | 独立 IDE（VS Code 衍生）+ Manager 仪表盘 |
| 开源程度 | 非开源 | 非开源 | 非开源（预览期免费） |
| 默认模型 | Claude 5 (Fable/Mythos) / Claude 4 (Sonnet/Opus) 系列 | OpenAI GPT（Codex 系列） | Gemini 3 Pro / Flash |
| 其他模型 | — | — | Claude 5 (Fable)、Claude Sonnet 4.6、Claude Opus 4.6、GPT-OSS-120B |
| API 需求 | Anthropic API 或 Claude 账户 | OpenAI API 或 ChatGPT 账户 | Google 账户（预览期无需单独 API Key） |
| 多模态 | 文本 + 图片 | 文本 + 图片 | 文本 + 图片 + 内置浏览器 |
| 持久记忆 | ✅ 完整（项目 + 用户记忆） | ⚠️ 会话内有限 | ✅ 跨运行学习 + 项目上下文 |
| 可核验产出 | diff + 工具调用记录 | diff + 沙盒输出 | **Artifacts**：计划、截图、浏览器录屏 |
| 多智能体 | CLI 内支持子智能体与 workflow | 通过 Web/App 并行运行 | Manager 视图跨工作区分发智能体 |
| 安全设计 | 危险操作需确认 | 沙盒优先 | 先出计划、人工确认后再执行；运行可审计 |
| 权限模式 | `--permission-mode`（default / plan / auto） | `--full-auto`、`--ask-for-approval`、`--sandbox`（只读 / 工作区可写 / 完全访问） | Read Only / Auto / Full Access；执行前先确认计划 Artifact |
| 扩展性 | MCP、技能、钩子、插件 | MCP、脚本 | VS Code 扩展、内置浏览器/终端 |

## 详细对比

### 上下文与记忆能力

**Claude Code**
- 长上下文，能跨多文件深度理解
- 跨会话持久记忆（用户级 + 项目级）
- 通过 `CLAUDE.md` / `AGENTS.md` 定义项目规则

**Codex CLI**
- 侧重快速的单文件或函数级编辑
- 轻量级的会话内状态，为低延迟循环而设计
- 没有一等公民的持久记忆，依赖 prompt 与 `AGENTS.md`

**Antigravity**
- 智能体优先：规划 → 编辑 → 运行 → 验证，上下文随步骤传递
- 智能体会从历史运行（包括你的修正）中学习
- 项目上下文以工作区为锚；内置浏览器把运行期信息（DOM、截图）回灌给智能体

### 安全与可控性

**Claude Code**
- 危险操作（删除文件、强制推送等）需用户确认
- 通过记忆和设置维护项目级安全规则
- 完善的工具权限模型（白名单、hooks）便于精细控制

**Codex CLI**
- 沙盒优先的执行环境
- 文件系统与网络隔离默认配置友好
- 简单、快速，面向终端使用的安全模型

**Antigravity**
- 智能体先生成**计划 Artifact**，人工批准后再执行
- 浏览器录屏与截图让事后审计成为可能
- 在 IDE 中运行，访问范围限定在工作区

### 扩展与集成

**Claude Code**
- 支持 MCP（Model Context Protocol）服务器
- 可自定义技能系统、自动化钩子
- 与 Git/GitHub/GitLab 深度集成

**Codex CLI**
- 轻量级、"Unix 原生"的工作流，适合与 shell 管道组合
- 支持 MCP，与终端融合紧密
- 易于与既有脚本搭配

**Antigravity**
- 基于 VS Code，可直接复用其扩展生态
- 内置浏览器，智能体可自行点击、跳转、截图
- 在同一 IDE 内可切换 Gemini / Claude / GPT-OSS 多模型

### 使用门槛

**Claude Code**
- 需要 Anthropic API Key 或 Claude 账户
- 功能强大，掌握 agentic / 记忆 / hooks 后收益更大

**Codex CLI**
- 需要 OpenAI API Key 或 ChatGPT 账户
- 配置极简，反馈循环非常快

**Antigravity**
- 预览期免费，使用 Google 账户登录即可
- 提供 Windows / macOS / Linux 桌面安装包；默认 Gemini 模型无需自己管 API Key

## 选择建议

### 选 Claude Code 如果你需要：
- 深入理解并重构大型、成熟的代码库
- 配合记忆与 hooks 的长链路 agentic 工作流
- 与终端 + IDE + GitHub 的深度集成
- 成熟的权限模型来支持自主执行

### 选 Codex CLI 如果你需要：
- 单文件 / 单函数的极速、低延迟编辑
- 与 shell 管道组合的 "Unix 原生" 体验
- 沙盒优先、配置最简的安全模型
- 一个日常贴身用的终端编程助手

### 选 Antigravity 如果你需要：
- 一个智能体优先的 IDE，而非补全或纯终端工具
- 通过 Artifacts（计划、截图、录屏）让智能体运行**可核验**
- 让智能体自己驱动浏览器去验证它写出的功能
- 通过 Manager 视图做多智能体分发，并在 Gemini / Claude / GPT-OSS 之间灵活切换
- 在公开预览期免费试用、无需 API Key

## 组合使用

这三款工具并不互斥，常见分工：

- **日常编辑 / 终端工作流**：Claude Code 或 Codex
- **由智能体驱动的大变更并需要浏览器验证**：Antigravity
- **快速单文件修改**：Codex
- **强记忆的长链路多文件重构**：Claude Code 或 Antigravity

## 相关链接

- [Claude Code 入门介绍](claude-code/README-CN.md)
- [Codex 入门介绍](codex/README-CN.md)
- [Antigravity 入门介绍](antigravity/README-CN.md)
