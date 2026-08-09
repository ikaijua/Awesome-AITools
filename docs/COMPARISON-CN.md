# AI Agent Tools 对比：Claude Code vs Codex vs Kimi Code vs Qoder vs Trae

本文档对比五款主流的 AI Agent 编程工具：Claude Code、Codex、Kimi Code、Qoder 和 Trae。

## 快速对比

| 方面 | Claude Code | Codex | Kimi Code | Qoder | Trae |
|------|-------------|-------|-----------|-------|------|
| 开发者 | Anthropic | OpenAI | Moonshot AI | 阿里云 | 字节跳动 |
| 形态 | 终端 CLI + IDE 插件 + 桌面/Web/App | 终端 CLI + IDE 扩展 + 桌面 App + Codex Web | 终端 CLI + ACP 编辑器 + 本地 Web UI | 桌面 IDE + CLI + Work + Wake + Cloud Agents | 终端 CLI + IDE + Web/桌面/移动工作空间 |
| 开源 | ❌ | ✅ Apache-2.0 | ⚠️ CLI 使用 MIT，核心服务不开源 | ❌ | ⚠️ Trae Code（trae-agent）MIT；IDE/Work 不开源 |
| 默认模型 | Claude 系列（Opus / Sonnet / Haiku） | GPT-5.x / Codex 系列 | Kimi Code / Moonshot 模型 | 通义 / 百炼模型 | Doubao-Seed-2.1 Pro / 可配置多供应商 |
| 其他模型 | — | — | 可配置兼容供应商 | 可配置阿里云百炼等 | OpenAI / Anthropic / Gemini / OpenRouter / Ollama 等 |
| 账号要求 | Anthropic API 或 Claude 账户 | OpenAI API 或 ChatGPT 账户 | Kimi 账户或 API Key | 阿里云账号 | Trae 账号 |
| 多模态 | 文本 + 图片 | 文本 + 图片 | 文本 + 图片/视频 | 文本 + 图片 | 文本 + 图片 |
| 持久记忆 | ✅ 项目级 + 用户级记忆 | ⚠️ 会话内 + 跨端 relay 同步 | ✅ 会话/Goal 记忆 | ✅ 知识引擎 + 自适应记忆 | ✅ 项目上下文 + 云端账号同步 |
| 多智能体 | ✅ 子代理 + workflows | ✅ 子代理 | ✅ 子代理 | ✅ 多智能体协同 | ✅ 自定义 Agent / SOLO Mode 子代理 / 并发 Cloud tasks |
| 本地/云端 | 本地优先，`--cloud` 可选 | 本地 + Codex Cloud | 本地优先，`kimi web` 本地 server | 本地 Desktop/CLI/Work + Cloud Agents | 本地 IDE/CLI + Trae Work 云端任务 |
| 跨端继续 | ✅ Remote Control + 手机/Web | ✅ ChatGPT relay（手机/桌面/Web） | ✅ `kimi web` 同 server 多端访问 | ✅ 远程控制 + Mobile 同步 | ✅ Trae Work Web/桌面/移动同步 |
| 权限模式 | `--permission-mode` default/plan/auto | `--approval-mode` suggest/auto-edit/full-auto + sandbox | Manual / YOLO / Auto / Plan | 确认 / Agent 模式 | 终端命令默认手动批准，可配置允许/拒绝列表 |
| 扩展性 | MCP、Skills、Hooks、Plugins | MCP、Skills、Plugins、Hooks | MCP、Skills、Hooks、ACP | MCP、内置工具、IDE 插件 | MCP、自定义 Agent、规则、Skills |

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

**Qoder**
- 深度代码库分析 + 自适应记忆与知识引擎
- 多智能体协同，角色分工（规划、编码、测试、审查）
- 目标导向的“规划 → 执行 → 验证 → 迭代”闭环

**Trae**
- Trae IDE 索引仓库上下文，规则与自定义 Agent 保持一致
- SOLO Mode 在 IDE 内自主完成多文件任务
- Trae Work 云端任务支持异步委派和跨设备继续
- 项目上下文在 Trae Code / IDE / Work 之间通过账号同步

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

**Qoder**
- Agent 模式前需要用户确认关键操作
- 本地 Desktop/CLI/Work 与云端 Cloud Agents 分离
- 企业版支持私有化/云端合规部署

**Trae**
- 终端命令默认需要手动批准，可配置命令允许/拒绝列表
- Privacy Mode 可限制聊天数据用于训练/分析
- 本地 IDE/CLI 与 Trae Work 云端任务分离，便于控制数据边界

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

**Qoder**
- MCP、内置编程工具、IDE 插件
- Desktop / CLI / Work / Wake / Cloud Agents 产品族
- 远程控制与 Mobile App 同步

**Trae**
- MCP 支持 stdio / SSE / Streamable HTTP
- 自定义 Agent、规则、Skills 复用工作流
- Trae Code / IDE / Work 共享代码库索引、规则与 MCP 扩展

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

**Qoder**
- Qoder 网页版可远程控制本地任务
- Mobile App 与 Desktop/CLI 实时同步
- Cloud Agents 支持关闭电脑后继续运行

**Trae**
- Trae Work 提供 Web、桌面和移动端工作空间
- 并发 Cloud tasks 可在后台运行，跨设备查看结果
- 同一 Trae 账号下，IDE、CLI 与 Work 的任务状态同步

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

### 选 Qoder 如果你需要：
- 覆盖 Desktop / CLI / Work / Wake / Cloud Agents 的全产品族
- 多智能体协同 + 知识引擎 + 远程控制
- 阿里云生态和国内合规部署

### 选 Trae 如果你需要：
- 同一产品族覆盖终端 CLI、IDE 和 Web/桌面/移动工作空间
- 低成本入门 + 云端异步任务（Trae Work）
- 自定义 Agent、规则、MCP 扩展与多模型支持
- 在 IDE  supervision 和 SOLO autonomy 之间灵活切换

## 组合使用

这些工具并不互斥，常见分工：

- **日常终端开发**：Claude Code、Codex、Kimi Code、Trae Code
- **国内环境与全产品族**：Qoder、Trae
- **快速单文件修改**：Codex、Claude Code、Trae SOLO Mode
- **长链路多文件重构**：Claude Code、Kimi Code、Qoder、Trae SOLO Mode
- **跨端继续任务**：Claude Code（Remote Control）、Codex（ChatGPT relay）、Kimi Code（`kimi web`）、Qoder（远程控制）、Trae（Trae Work）

## 相关链接

- [Claude Code 入门介绍](claude-code/README-CN.md)
- [Codex 入门介绍](codex/README-CN.md)
- [Kimi Code 入门介绍](kimi-code/README-CN.md)
- [Qoder 入门介绍](qoder/README-CN.md)
- [Trae 入门介绍](trae/README-CN.md)
