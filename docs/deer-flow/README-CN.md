# DeerFlow 简介

## 什么是 DeerFlow？

[DeerFlow](https://github.com/bytedance/deer-flow)（Deep Exploration and Efficient Research Flow）是字节跳动开源的**长时程超级智能体 harness（SuperAgent harness）**。它通过编排子代理、记忆、沙箱、工具、技能和消息网关，完成从几分钟到数小时的复杂任务——涵盖深度研究、报告生成、编程开发以及内容创作等场景。

DeerFlow 2.0 基于 [LangGraph](https://github.com/langchain-ai/langgraph) 和 [LangChain](https://github.com/langchain-ai/langchain) 彻底重写，采用"开箱即用"的设计，内置 Web UI、文件系统、持久记忆、技能系统、沙箱执行能力，并支持多种大语言模型。

## 核心定位

### 从深度研究到超级智能体 Harness
DeerFlow 最初是一个深度研究框架，但社区很快将其扩展到数据流水线、幻灯片、仪表盘和自动化内容工作流等场景。2.0 版本将这一运行时泛化为面向长时程智能体任务的 harness。

### 可扩展的技能体系
技能（Skill）是 DeerFlow 的核心能力单元。内置技能覆盖研究、报告生成、幻灯片制作、网页、图像与视频生成等。你也可以添加或替换自己的技能。技能按需渐进加载，有助于控制上下文窗口大小。

### 子代理与规划
DeerFlow 可以派生子代理处理子任务、规划多步工作流，并根据中间结果迭代优化，适合单次提示无法完成的复杂目标。

## 核心功能

- **子代理与编排** — 委派子任务，协调长时间运行的工作流。
- **长期记忆** — 跨会话保留对话与项目上下文。
- **沙箱执行** — 在本地、Docker 或 Kubernetes 沙箱中运行代码与命令。
- **技能与工具** — 内置技能，并可通过 MCP 服务器和自定义函数扩展工具。
- **多模型支持** — 兼容 OpenAI、Anthropic、DeepSeek、Kimi、Qwen、豆包、OpenRouter、vLLM 等。
- **IM 消息通道** — 支持从 Telegram、Slack、飞书/Lark、微信、企业微信、钉钉接收任务。
- **可观测性** — 内置 LangSmith、Langfuse 和 Monocle 链路追踪。
- **Web UI 与 TUI** — 通过浏览器访问 `http://localhost:2026`，或使用终端工作台交互。

## 快速开始

### 环境要求
- Python 3.11+ 与 Node.js 22+
- `uv`、`pnpm`，可选 Docker

### 安装与配置

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup   # 交互式向导，生成 config.yaml 和 .env
```

### 本地运行

```bash
make install   # 安装前后端依赖
make dev       # 启动 Gateway 与 UI
```

然后打开 `http://localhost:2026`。

### Docker 运行（推荐用于服务器部署）

```bash
make docker-init
make docker-start
```

## 最佳实践

1. **使用沙箱** — 对于不可信代码，优先使用 Docker 或 Kubernetes 沙箱模式。
2. **目标要明确** — 目标越具体，DeerFlow 的规划与委派效果越好。
3. **配置记忆** — 多会话项目建议开启长期记忆。
4. **审查技能权限** — 使用第三方技能时，检查其 `allowed-tools` 策略。
5. **开启链路追踪** — 长时程任务建议启用 LangSmith/Langfuse，以便审计代理执行步骤。

## 安全提示

DeerFlow 可以执行任意代码、浏览网页并访问已配置的集成。不当部署可能带来安全风险。在将其暴露到公网或授予敏感凭据之前，请务必阅读官方安全建议。

## 相关资源

- [GitHub 仓库](https://github.com/bytedance/deer-flow)
- [官方网站](https://deerflow.tech/)
- [文档](https://github.com/bytedance/deer-flow/tree/main/docs)
- [姊妹项目：LLM Space](https://github.com/bytedance/llm-space)

## 许可证

DeerFlow 是开源项目，使用和分发时请遵循其许可证。
