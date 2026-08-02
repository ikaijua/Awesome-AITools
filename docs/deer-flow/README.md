# DeerFlow Introduction

## What is DeerFlow?

[DeerFlow](https://github.com/bytedance/deer-flow) (Deep Exploration and Efficient Research Flow) is an open-source, long-horizon **SuperAgent harness** from ByteDance. It orchestrates sub-agents, memory, sandboxes, tools, skills, and message gateways to carry out complex tasks that can run from minutes to hours — from deep research and report generation to coding and content creation.

DeerFlow 2.0 is a ground-up rewrite built on [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain). It ships "batteries included" with a web UI, filesystem, persistent memory, skill system, sandbox-aware execution, and multi-provider LLM support.

## Core Positioning

### From Deep Research to Super Agent Harness
DeerFlow started as a deep-research framework, but the community quickly pushed it beyond research into data pipelines, slide decks, dashboards, and automated content workflows. Version 2.0 generalizes that runtime into a harness for long-running agentic work.

### Extensible Skills
Skills are DeerFlow's primary unit of capability. Built-in skills cover research, report generation, slide creation, web pages, image and video generation, and more. You can add your own skills or replace the built-ins. Skills are loaded progressively, keeping the context window lean.

### Sub-Agents and Planning
DeerFlow can spawn sub-agents to tackle sub-tasks, plan multi-step workflows, and iterate based on intermediate results — making it suitable for goals that are too large for a single prompt.

## Core Features

- **Sub-agents & orchestration** — delegate sub-tasks and coordinate long-running workflows.
- **Long-term memory** — retain conversation and project context across sessions.
- **Sandbox-aware execution** — run code and commands in local, Docker, or Kubernetes sandboxes.
- **Skills & tools** — built-in skills plus extensible tools via MCP servers and custom functions.
- **Multi-provider models** — works with OpenAI, Anthropic, DeepSeek, Kimi, Qwen, Doubao, OpenRouter, vLLM, and more.
- **IM channel integration** — receive tasks from Telegram, Slack, Feishu/Lark, WeChat, WeCom, and DingTalk.
- **Observability** — built-in support for LangSmith, Langfuse, and Monocle tracing.
- **Web UI & TUI** — interact through a browser at `http://localhost:2026` or the terminal workbench.

## Quick Start

### Prerequisites
- Python 3.11+ and Node.js 22+
- `uv`, `pnpm`, and optionally Docker

### Install and configure

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
make setup   # interactive wizard; writes config.yaml and .env
```

### Run locally

```bash
make install   # install frontend + backend dependencies
make dev       # start the gateway and UI
```

Then open `http://localhost:2026`.

### Run with Docker (recommended for server use)

```bash
make docker-init
make docker-start
```

## Best Practices

1. **Use a sandbox** — prefer Docker or Kubernetes sandbox modes for untrusted code execution.
2. **Start with a clear goal** — DeerFlow plans and delegates better when the objective is specific.
3. **Configure memory** — enable long-term memory for multi-session projects.
4. **Review skill policies** — when using third-party skills, check their `allowed-tools` policy.
5. **Monitor traces** — enable LangSmith/Langfuse for long-running tasks so you can audit agent steps.

## Security Notice

DeerFlow can execute arbitrary code, browse the web, and access configured integrations. Improper deployment can introduce security risks. Always review the [security recommendations](https://github.com/bytedance/deer-flow) before exposing it to the internet or granting sensitive credentials.

## Related Resources

- [GitHub Repository](https://github.com/bytedance/deer-flow)
- [Official Website](https://deerflow.tech/)
- [Documentation](https://github.com/bytedance/deer-flow/tree/main/docs)
- [Sister Project: LLM Space](https://github.com/bytedance/llm-space)

## License

DeerFlow is open source. Please follow its license when using or distributing it.
