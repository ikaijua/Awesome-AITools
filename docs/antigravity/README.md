# Antigravity Introduction

## What is Antigravity?

Antigravity is Google's agent-first AI coding platform built around the Gemini 3 family of models. Announced alongside Gemini 3, it is delivered as a heavily modified VS Code–based IDE (often regarded as a successor to / derivative of Windsurf) that lets developers delegate end-to-end software tasks to autonomous agents instead of just accepting inline code completions.

> ℹ️ Antigravity replaces Gemini CLI as Google's primary recommendation for agentic coding workflows. Gemini CLI is being deprecated in favor of the agent-oriented experience offered by Antigravity.

## Core Philosophy

### Agent-First, Not Autocomplete-First
Antigravity treats the human as a manager of agents:
- The unit of work is a task or a plan, not a keystroke
- Agents have direct access to the editor, terminal, and an integrated browser
- Every agent run produces **Artifacts** — task lists, plans, screenshots, browser recordings — so the human can verify what was done before accepting it

### Two Built-in Surfaces
- **Editor view**: a VS Code–like IDE with an agent sidebar for in-context collaboration
- **Manager view**: a dashboard for fanning out work across multiple agents and workspaces in parallel

### Multi-Model, Gemini-Centered
Out of the box you can choose between:
- Gemini 3 Pro (default, with generous preview rate limits)
- Gemini 3 Flash
- Anthropic Claude Sonnet 4.6 / Claude Opus 4.6
- GPT-OSS-120B

### Verifiable Agent Output
- Artifacts (plans, screenshots, browser recordings) make agent runs auditable
- Agents accumulate learnings across sessions instead of starting cold every time

## Core Features

### Autonomous Coding Agents
- Multi-step task execution: plan → edit → run → verify
- Parallel agents working across files and even repositories
- Long-horizon refactors and migrations rather than single-snippet edits

### Integrated Browser Control
- Agents can drive a real browser to test the changes they wrote
- Captures screenshots and recordings as evidence of behavior

### Project Memory and Learning
- Carries project context across agent runs
- Learns from prior interactions, including corrections you apply

### IDE Integration
- VS Code–style editor experience that most developers already know
- Terminal, source control, and extensions work as expected

## Quick Start

### Download

Antigravity is distributed as a desktop IDE (public preview, free during the preview period). Get it from the official site:

- <https://antigravity.google/>

System requirements:
- Windows 10 (64-bit) or later
- macOS Monterey (12) or later
- 64-bit Linux (modern glibc / glibcxx)

### Sign In and Pick a Model

1. Launch Antigravity and sign in with your Google account
2. Pick a default model — Gemini 3 Pro is a good baseline
3. Open a folder/workspace and start in **Editor view**, or jump to **Manager view** to plan a multi-agent run

### Typical Workflow

1. Describe the task in natural language ("add unit tests for `auth/`", "migrate this service from REST to gRPC")
2. The agent produces a plan as an Artifact for you to approve
3. The agent edits files, runs commands in the terminal, and optionally drives the browser to verify
4. Review the diff and the Artifacts (screenshots, recordings, logs), then accept or iterate

## CLI Usage

While Antigravity is primarily delivered as a desktop IDE with Editor and Manager views, it also inherits and expands on the command-line capabilities of the former `Gemini CLI`. You can interact with the Antigravity agent directly from your terminal using the `gemini` command.

### Installation / Setup
- **IDE Built-in**: Inside the Antigravity desktop IDE, open the Command Palette (F1 or Cmd/Ctrl+Shift+P) and search for `Shell Command: Install 'gemini' command in PATH`.
- **Standalone Client** (if you need a standalone command-line client):
  ```bash
  npm install -g @google/gemini-cli
  ```

### Basic Commands

```bash
# Launch interactive terminal session
gemini

# Ask a prompt directly and start interactive mode
gemini "Analyze current project structure"

# Run in non-interactive (headless) mode with a given prompt
gemini --prompt "Write unit tests for src/auth.js"

# Safely run inside a new Git worktree to avoid contaminating the current branch
gemini --worktree my-refactor "Refactor login logic"
```

### Common Options

- `-m, --model <model_name>`: Specify the model to use (e.g. `gemini-3-pro`, `gemini-3-flash`, `claude-3-5-sonnet`)
- `-y, --yolo`: YOLO mode; automatically approve all agent actions (edits, shell commands) without asking
- `--approval-mode <mode>`: Set the tool approval mode (`default`, `auto_edit` for auto-approving file changes, `yolo`, or `plan` for read-only plan mode)
- `-r, --resume <session_id>`: Resume a previous session (e.g. `latest` or a specific index/ID)
- `-s, --sandbox`: Run the agent within a sandbox environment for command execution security

### Helper Commands

```bash
# Manage Model Context Protocol (MCP) servers
gemini mcp list
gemini mcp add <name> <command>

# Manage agent skills
gemini skills list

# Manage automation hooks
gemini hooks list
```

## Common Use Cases

### Long-Horizon Refactoring
Hand the agent a multi-file refactor and review the produced plan and diff instead of writing every edit yourself.

### End-to-End Feature Work
Spec → implementation → tests → browser-verified UI changes, all driven by one or more agents in the same workspace.

### Parallel Workstreams
Use Manager view to run several agents on different tasks/branches at once and inspect their Artifacts as they finish.

## Best Practices

1. **Start from a clear task statement** — the better the prompt, the better the plan
2. **Review the Artifact, not just the diff** — screenshots and recordings catch behavior the diff hides
3. **Let the agent verify** — give it permission to run tests and drive the browser; the goal is verifiable output
4. **Bring corrections back as context** — Antigravity learns across runs, so explicit feedback compounds

## Related Resources

- [Official Site](https://antigravity.google/)
- [Wikipedia: Google Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Antigravity is a proprietary Google product. It is free of charge during the public preview, with generous rate limits for the included Gemini 3 Pro usage. Subject to Google's terms of service.
