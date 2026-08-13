# DeepSeek Harness Introduction

## What is DeepSeek Harness?

DeepSeek Harness (dsh) is an open-source agent harness developed by DeepSeek AI. It uses an "everything is a plugin" architecture powered by Cordis, and ships as both a CLI and a local Web UI. It is a full agent runtime — not just a thin wrapper around a model — covering LLM, MCP, LSP, ACP, sandbox, skills, subagents, sessions, tools, plans, scheduling, shell, and the web layer.

> ⚠️ **Developer preview.** DeepSeek Harness was released on August 13, 2026 and is iterating rapidly. Breaking changes are expected. Treat the API as unstable for now.

## Highlights

- **Everything is a plugin.** The runtime is built on [Cordis](https://github.com/trycua/cordis), a well-known IoC-style plugin framework. Every subsystem — LLM, MCP, LSP, sessions, tools, plans, sandbox, scheduling, web, etc. — is a Cordis plugin, so the same `event` / `service` / `effect` model is used across all of them.
- **CLI + Web UI out of the box.** Run `npx @deepseek-ai/dsh web` and the Web UI is served at `http://127.0.0.1:3080` by default. No separate "headless" vs "GUI" build.
- **Bilingual architecture docs.** The `docs/` tree ships in English *and* Chinese, covering architecture, agent lifecycle, tool execution pipeline, capability seams, the Cordis primer, defensive patterns, and more.
- **40+ first-party packages.** `core`, `llm`, `mcp`, `lsp`, `acp`, `sandbox`, `skill`, `subagent`, `session`, `session-query`, `tools` (via `tool-catalog` + `tool-execution-pipeline`), `plan`, `goal`, `schedule`, `web`, `shell`, `terminal`, `workflow`, `jobs`, `hooks`, `guard`, `feedback`, `compaction`, `context`, `attachment`, `identity`, `credentials`, `e2b`, `runtime-diagnostics`, `typert`, `client`, `host`, `sdk`, `extensions`, etc.
- **First-class extension points.** Any package can be extended or replaced via a Cordis plugin. The repo asks plugin authors to tag their repos with `dsh-plugin` for discoverability.
- **MIT licensed.** The full source, including docs and tooling, is MIT.

## Install & Run

### Web UI (recommended for first try)

```bash
# Requires Node.js
npx @deepseek-ai/dsh web
```

The command starts the Web UI, served at `http://127.0.0.1:3080` by default. See the Web UI guide in the upstream docs for the `--host` / `--port` flags.

### Run from source

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

## Core Concepts

- **Plugin (Cordis)** — the fundamental unit. A plugin declares `events`, `services`, and `effects`, and can `await` services from other plugins.
- **Service** — an injectable capability. Plugins obtain services via `this.someService` and await them.
- **Event** — a typed lifecycle hook, used for inter-plugin messaging and for the harness's own diagnostic surfaces.
- **Effect** — long-running side effect (e.g. a tool call, a sandboxed subprocess) registered with the lifecycle system.
- **Capability seams** — the explicit places where new capabilities (LLM provider, tool, transport, storage) plug in. See `docs/capability-seams.md` upstream.

The combination of these primitives is what makes the architecture "everything is a plugin" rather than a hard-coded pipeline of features.

## Subsystems at a Glance

| Subsystem | Package(s) | What it does |
| --- | --- | --- |
| Core runtime | `core`, `runtime-diagnostics`, `compaction` | Plugin lifecycle, error/trace, context window compaction |
| LLM & tools | `llm`, `tool-catalog`, `tool-execution-pipeline` | Provider abstraction, tool registry, sandboxed tool execution |
| Agent orchestration | `agent`, `subagent`, `plan`, `goal` | Agent lifecycle, sub-agents, planning, goal tracking |
| Skills & memory | `skill`, `feedback`, `context` | Reusable skills, feedback loop, working context |
| Sessions & jobs | `session`, `session-query`, `jobs` | Long-running sessions, queries, scheduled jobs |
| External integrations | `mcp`, `lsp`, `acp`, `client` | MCP servers, language servers, ACP, client-side integrations |
| Sandbox & execution | `sandbox`, `e2b`, `subprocess`, `shell`, `terminal` | Sandboxed code/tool execution, subprocess management, shell/terminal |
| UI & web | `web`, `host`, `interaction` | Web UI, host runtime, user interaction |
| Storage & identity | `storage`, `credentials`, `identity`, `attachment` | Persistence, secrets, identity, file attachments |
| Extension surface | `extensions`, `sdk`, `hooks`, `guard` | Custom plugins, SDK, hook points, guardrails |
| Workflow | `workflow`, `schedule`, `boot`, `bundle` | Workflow definitions, scheduled runs, bootstrap, packaging |
| Diagnostics | `runtime-diagnostics`, `compaction`, `typert` | Tracing, compaction policies, schema types |

See `docs/architecture.md` in the upstream repo for the canonical subsystem diagram.

## Typical Use Cases

- **Standalone agent runner.** Run `dsh` from the terminal or open the Web UI and use it as a coding/research agent — similar to Claude Code or Codex, with the difference that *every* capability is a plugin.
- **Embed in your own product.** Because the runtime is a set of Cordis plugins, you can import only the packages you need and skip the rest (e.g. drop the Web UI and run headless).
- **Extend with your own LLM / tools.** Add a new provider or tool by writing a small Cordis plugin that registers a `service` and an `effect`. The harness handles the lifecycle, the event bus, and the rest of the wiring.
- **Spec-driven or workflow-driven runs.** Use the `workflow`, `plan`, `goal`, and `schedule` packages to run multi-step, time-based, or goal-oriented jobs that survive restarts.

## When to Pick DeepSeek Harness

| Pick it if… | Maybe skip if… |
| --- | --- |
| You want a DeepSeek-maintained, MIT-licensed agent runtime that is genuinely plugin-based (not a hard-coded pipeline). | You just want a polished CLI coding agent today — Claude Code / Codex / Kimi Code / Antigravity are more battle-tested right now. |
| You need to embed or extend an agent runtime and prefer its surface area to be Cordis plugins. | You depend on a stable, documented CLI API — the upstream `dsh` CLI is still labelled "developer preview". |
| You want a runtime that natively speaks MCP, LSP, and ACP. | You only need a chat UI with no runtime customization. |

## Caveats

- **Brand new.** Initial release was August 13, 2026. Treat docs, packages, and the CLI as subject to change.
- **Documentation lags code in places.** Most of the docs are bilingual and high quality, but some newer packages may not yet be fully covered.
- **npm distribution is early.** `@deepseek-ai/dsh` is published but the `dsh` CLI API is still being stabilized.
- **No public cloud tier.** This is a self-hosted, local-first runtime. There is no hosted offering from DeepSeek for the harness itself (as of this writing).

## Related Resources

- [GitHub Repository](https://github.com/deepseek-ai/deepseek-harness)
- [Architecture documentation (upstream)](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
- [Cordis primer (upstream)](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/cordis-primer.md)
- [Agent lifecycle (upstream)](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/agent-lifecycle.md)
- [Tool execution pipeline (upstream)](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/tool-execution-pipeline.md)
- [Community Discord](https://github.com/deepseek-ai/deepseek-harness#community-and-support)

## License

MIT — see [`LICENSE`](https://github.com/deepseek-ai/deepseek-harness/blob/master/LICENSE).
