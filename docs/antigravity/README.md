# Antigravity Introduction

## What is Antigravity?

Antigravity (currently Antigravity 2.0) is Google's agent-first AI coding platform and the successor to the deprecated Gemini CLI. It is no longer just an IDE plugin, but a product family with four surfaces:

- **Antigravity Desktop App**: a standalone agentic development workbench
- **Antigravity IDE**: an agent-first IDE with Agent Manager, Artifacts, and deep codebase understanding
- **Antigravity CLI (`agy`)**: a lightweight, fast, terminal-native agent
- **Antigravity SDK**: a Python toolkit for prototyping custom agents and evaluations

Antigravity defaults to Gemini 3.5 / 3.6 Flash models and also supports switching to Claude, GPT-OSS, and other models via a model picker.

## Core Philosophy

### Agent-First, Not Autocomplete-First
Antigravity treats the human as a manager of agents:
- The unit of work is a task or a plan, not a keystroke
- Agents have direct access to the editor, terminal, and an integrated browser
- Every run produces **Artifacts** — task lists, plans, screenshots, browser recordings — so the human can verify what was done before accepting it

### Multiple Surfaces, Same Agent Engine
Whether you use the desktop app, IDE, terminal CLI, or SDK, the same Antigravity agent engine powers Projects, multi-workspace orchestration, subagents, and scheduled tasks.

### Multi-Model, Gemini-Centered
- Default models: Gemini 3.5 Flash / 3.6 Flash
- Optional models: Gemini 3 Pro, Claude family, GPT-OSS-120B
- Switch quickly with `/model` or configuration

### Verifiable Agent Output
- Artifacts make agent runs auditable
- Agents accumulate learnings across sessions instead of starting cold every time

## Product Surfaces

| Surface | Positioning | Best For |
| --- | --- | --- |
| **Desktop App** | Standalone agentic workbench | Daily development, multi-project management |
| **IDE** | Agent-first IDE with Agent Manager | Deep code editing and parallel agents |
| **CLI (`agy`)** | Terminal-native agent | Command-line users, scripting / CI |
| **SDK** | Python programmable interface | Custom agents and evaluations |

## Core Capabilities

### Autonomous Coding Agents
- Multi-step task execution: plan → edit → run → verify
- Parallel agents working across files and even repositories
- Long-horizon refactors and migrations rather than single-snippet edits

### Multi-Agent Management
- **Agent Manager**: fan out and orchestrate tasks across multiple agents and workspaces
- **Projects**: group related conversations and tasks
- **Subagents**: delegate focused work to specialized agents

### Integrated Browser Control
- Agents can drive a real browser to test the changes they wrote
- Captures screenshots and recordings as evidence of behavior

### Project Memory and Learning
- Carries project context across agent runs
- Learns from prior interactions, including corrections you apply
- Supports Hooks and scheduled tasks

## Quick Start

### Download

Antigravity is currently in public preview and free for individual users. Download the desktop app or IDE for your system from:

- <https://antigravity.google/>

System requirements:
- Windows 10 (64-bit) or later
- macOS Monterey (12) or later
- 64-bit Linux (modern glibc / glibcxx)

### Sign In and Pick a Model

1. Launch Antigravity and sign in with your Google account
2. Pick a default model — Gemini 3.5 Flash is a good baseline
3. Open a folder/workspace and start in **Editor/IDE** view, or jump to **Manager** view to plan a multi-agent run

### Typical Workflow

1. Describe the task in natural language ("add unit tests for `auth/`", "migrate this service from REST to gRPC")
2. The agent produces a plan as an Artifact for you to approve
3. The agent edits files, runs commands in the terminal, and optionally drives the browser to verify
4. Review the diff and the Artifacts (screenshots, recordings, logs), then accept or iterate

## CLI Usage

Antigravity 2.0's terminal entry point is `agy` (Antigravity CLI), the successor to Gemini CLI.

### Installation

- **Via IDE / Desktop App**: open the Command Palette (F1 / Ctrl+Shift+P) and run `Shell Command: Install 'agy' command in PATH`
- **Standalone install** (see official docs):
  ```bash
  # Follow the official Antigravity documentation for the latest command
  ```

### Basic Commands

```bash
# Launch interactive terminal session
agy

# Ask a prompt directly
agy "Analyze current project structure"

# Non-interactive (headless / script) mode
agy -p "Write unit tests for src/auth.js"

# Migrate plugins from Gemini CLI
agy plugin import gemini
```

### Common Options

- `-m, --model <model>`: specify model, e.g. `gemini-3.5-flash`
- `-p, --prompt <prompt>`: run in non-interactive mode
- `--approval-mode <mode>`: approval mode (`default`, `auto_edit`, `yolo`, `plan`)
- `-s, --sandbox`: run inside a sandbox
- `agy mcp list` / `agy skills list` / `agy hooks list`: manage MCP, Skills, Hooks

> Note: the `gemini` command stopped serving individual users on June 18, 2026. Migrate scripts to `agy`.

## Common Use Cases

### Long-Horizon Refactoring
Hand the agent a multi-file refactor and review the produced plan and diff instead of writing every edit yourself.

### End-to-End Feature Work
Spec → implementation → tests → browser-verified UI changes, all driven by one or more agents in the same workspace.

### Parallel Workstreams
Use Manager view to run several agents on different tasks/branches at once and inspect their Artifacts as they finish.

### Custom Agents (SDK)
Use the Antigravity SDK to quickly prototype custom agents in Python and run evaluations.

## Best Practices

1. **Start from a clear task statement** — the better the prompt, the better the plan
2. **Review the Artifact, not just the diff** — screenshots and recordings catch behavior the diff hides
3. **Let the agent verify** — give it permission to run tests and drive the browser; the goal is verifiable output
4. **Bring corrections back as context** — Antigravity learns across runs, so explicit feedback compounds
5. **Start with the desktop app or IDE** — move to the `agy` CLI for scripting once you're comfortable

## Related Resources

- [Official Site](https://antigravity.google/)
- [Google Antigravity 2.0 Announcement](https://blog.google/products/antigravity/)

## License

Antigravity is a proprietary Google product. It is free for individual users during the public preview; some advanced features or higher quotas may require a Google AI subscription. Subject to Google's terms of service.
