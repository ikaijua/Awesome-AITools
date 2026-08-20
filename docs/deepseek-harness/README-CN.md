# DeepSeek Harness 介绍

## 什么是 DeepSeek Harness？

DeepSeek Harness（命令行工具名 `dsh`）是 DeepSeek AI 开源的 **agent harness（智能体运行时）**，采用基于 [Cordis](https://github.com/trycua/cordis) 的「**一切皆插件**」架构。它同时提供 CLI 与本地 Web UI，覆盖 LLM、MCP、LSP、ACP、沙箱、Skills、子代理、会话、工具、计划、调度、Shell、Web 等完整子系统——不是只套了一个模型的薄壳，而是一个真正可扩展的运行时框架。

> ⚠️ **开发者预览版。** DeepSeek Harness 于 2026 年 8 月 13 日开源，仍在快速迭代，预计会有不兼容更新。请将 CLI/API 视为不稳定。

## 核心亮点

- **一切皆插件。** 整个运行时基于 Cordis（一个成熟的 IoC 风格插件框架）构建。LLM、MCP、LSP、会话、工具、计划、沙箱、调度、Web 等所有子系统都是一个 Cordis 插件，使用统一的 `event` / `service` / `effect` 模型协作。
- **开箱即用的 CLI + Web UI。** 运行 `npx @deepseek-ai/dsh web` 即可在 `http://127.0.0.1:3080` 启动 Web UI；不需要单独的「headless」或「GUI」构建。
- **中英双语架构文档。** `docs/` 目录下提供完整的中英双语文档：架构、agent 生命周期、工具执行管线、能力接缝、Cordis 入门、防守式编程模式等。
- **40+ 一方子包。** `core` / `llm` / `mcp` / `lsp` / `acp` / `sandbox` / `skill` / `subagent` / `session` / `tools` / `plan` / `goal` / `schedule` / `web` / `shell` / `terminal` / `workflow` / `jobs` / `hooks` / `guard` / `feedback` / `compaction` / `context` / `attachment` / `identity` / `credentials` / `e2b` / `runtime-diagnostics` / `typert` / `client` / `host` / `sdk` / `extensions` / `bundle` / `boot` / `storage` / `preset` 等。
- **一等公民的扩展点。** 所有功能都可以通过 Cordis 插件替换或扩展；官方邀请插件作者给自己的仓库打 `dsh-plugin` 主题以便被发现。
- **MIT 协议。** 源代码、文档、工具全部 MIT。

## 安装与运行

### 启动 Web UI（推荐第一次尝试）

```bash
# 需要 Node.js
npx @deepseek-ai/dsh web
```

该命令会在 `http://127.0.0.1:3080` 启动 Web UI。`--host` / `--port` 等参数参见上游 Web UI 指南。

### 从源码运行

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

## 核心概念

- **Plugin（Cordis）** — 最基本的单元。一个插件声明 `events`、`services`、`effects`，并可以 `await` 其它插件的 services。
- **Service** — 可注入的能力。插件通过 `this.someService` 获取并 await。
- **Event** — 类型化的生命周期钩子，用于插件间消息传递以及运行时诊断。
- **Effect** — 长时间运行的副作用（如工具调用、沙箱子进程），注册到生命周期系统中。
- **Capability seams（能力接缝）** — 新能力接入的明确位置（LLM provider、tool、transport、storage 等）。详见上游 `docs/capability-seams.md`。

正是这些原语组合起来，使整个架构是「**一切皆插件**」，而不是把功能硬编码成流水线。

## 子系统一览

| 子系统 | 包 | 作用 |
| --- | --- | --- |
| 核心运行时 | `core`、`runtime-diagnostics`、`compaction` | 插件生命周期、错误与追踪、上下文压缩 |
| LLM 与工具 | `llm`、`tool-catalog`、`tool-execution-pipeline` | 抽象 Provider、工具注册、沙箱化工具执行 |
| 智能体编排 | `agent`、`subagent`、`plan`、`goal` | Agent 生命周期、子代理、计划、目标追踪 |
| 技能与记忆 | `skill`、`feedback`、`context` | 可复用技能、反馈循环、工作上下文 |
| 会话与任务 | `session`、`session-query`、`jobs` | 长会话、查询接口、调度任务 |
| 外部集成 | `mcp`、`lsp`、`acp`、`client` | MCP server、语言服务、ACP、客户端集成 |
| 沙箱与执行 | `sandbox`、`e2b`、`subprocess`、`shell`、`terminal` | 沙箱化代码/工具执行、子进程、Shell/终端 |
| UI 与 Web | `web`、`host`、`interaction` | Web UI、宿主运行时、用户交互 |
| 存储与身份 | `storage`、`credentials`、`identity`、`attachment` | 持久化、密钥、身份、附件 |
| 扩展面 | `extensions`、`sdk`、`hooks`、`guard` | 自定义插件、SDK、钩子、护栏 |
| 工作流 | `workflow`、`schedule`、`boot`、`bundle` | 工作流定义、定时任务、启动、打包 |
| 诊断 | `runtime-diagnostics`、`compaction`、`typert` | 追踪、压缩策略、类型 |

完整子系统图参见上游 `docs/architecture.md`。

## 典型用法

- **独立的 agent 运行时。** 在终端运行 `dsh` 或打开 Web UI，把它当 Claude Code / Codex 一样使用——区别在于**每个能力都是插件**。
- **嵌入到你自己的产品里。** 因为整个运行时就是一组 Cordis 插件，你可以只引入需要的子包，跳过其它部分（例如去掉 Web UI、headless 跑）。
- **扩展自己的 LLM / 工具。** 新增一个 provider 或 tool，只需写一个 Cordis 插件，注册一个 `service` 和一个 `effect`；运行时负责生命周期、事件总线、连接。
- **规约驱动 / 工作流驱动的执行。** 用 `workflow`、`plan`、`goal`、`schedule` 等包，跑多步骤、定时或目标驱动的任务，并能跨重启存活。

## 什么时候选 DeepSeek Harness？

| 适合 | 不一定适合 |
| --- | --- |
| 想要一个由 DeepSeek 维护、MIT 协议、真正基于插件的 agent 运行时（而非硬编码的流水线）。 | 想要一个今天就能直接拿来用的 CLI 编程智能体——Claude Code / Codex / Kimi Code / Antigravity 目前更成熟。 |
| 需要把 agent 运行时嵌入或扩展，并且希望接口面是 Cordis 插件。 | 依赖稳定、文档齐备的 CLI API——上游 `dsh` CLI 当前仍标「开发者预览」。 |
| 需要原生支持 MCP、LSP、ACP 的运行时。 | 只需要一个聊天 UI，不需要定制运行时。 |

## 注意事项

- **非常新。** 首发是 2026 年 8 月 13 日，文档、CLI、API 都可能变化。
- **文档略落后于代码。** 多数文档都是中英双语且质量不错，但部分新包可能还没完整覆盖。
- **npm 分发尚早。** `@deepseek-ai/dsh` 已发布，但 `dsh` CLI 仍在稳定化。
- **没有官方云服务。** 这是一个自托管、本地优先的运行时（截至本文写作时 DeepSeek 暂未提供 harness 本身的托管服务）。

## 相关资源

- [GitHub 仓库](https://github.com/deepseek-ai/deepseek-harness)
- [DSH Plugin Store](https://github.com/sandbaseai/dsh-plugin-store) — 原生集成到 Settings 的社区插件市场，支持搜索、筛选、安装与已加载插件查看，并提供可复现的预览版和 Agent 目录工具。
- [架构文档（上游）](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
- [Cordis 入门（上游）](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/cordis-primer.md)
- [Agent 生命周期（上游）](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/agent-lifecycle.md)
- [工具执行管线（上游）](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/tool-execution-pipeline.md)
- [社区 Discord](https://github.com/deepseek-ai/deepseek-harness#community-and-support)

## 许可证

MIT —— 详见 [`LICENSE`](https://github.com/deepseek-ai/deepseek-harness/blob/master/LICENSE)。
