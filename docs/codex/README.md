# Codex Introduction

## What is Codex?

Codex is OpenAI's AI coding agent. Its core is an open-source (Apache-2.0) terminal CLI written in Rust. It can understand, edit, and run code directly in your local repository, and is also available through VS Code / Cursor / Windsurf / JetBrains IDE extensions, the Codex App (desktop), and Codex Web (cloud tasks). Active sessions can sync across phone, desktop, and web through the same ChatGPT account.

## Core Philosophy

### Terminal-Native
Codex CLI is built around the terminal workflow, letting you complete the full development loop—explore, edit, run, and review—inside your familiar shell environment.

### Local-First with Optional Cloud
By default Codex runs on your local machine, keeping code and credentials local. You can also hand work off to Codex Cloud and let it finish asynchronously in a cloud sandbox.

### Controllable Automation
Approval modes and sandbox settings let you control when Codex can read or write files, run commands, and access the network.

### Extensible
Codex supports Skills (reusable instructions), Plugins (team tool integrations), MCP servers, subagents, and Hooks.

## Available Surfaces

| Surface | Description |
| --- | --- |
| Terminal CLI | Open-source Rust client with the full feature set |
| IDE Extensions | VS Code / Cursor / Windsurf / JetBrains |
| Desktop App | `codex app` for visual management and multiple sessions |
| Codex Web | chatgpt.com/codex for cloud tasks and collaboration |
| Mobile App | ChatGPT app can connect to and continue active sessions |

## Core Capabilities

### Code Understanding & Modification
- Analyze project structure, dependencies, and call relationships
- Automatically fix bugs, refactor, and add features
- Execute and iterate on multi-step tasks

### Command-Line & CI Integration
- Interactive TUI and one-shot prompt mode
- `codex exec` for scripts and pipelines
- Pipe and shell-script integration

### Code Review
- `codex review` examines uncommitted changes, commits, or branches
- Does not modify the working tree; only reports risks and suggestions

### Extensibility
- **Skills / Plugins**: reusable instructions and team tool integrations
- **MCP servers**: connect to external tools and data sources
- **Subagents**: delegate complex investigations to specialized agents
- **Hooks**: customize lifecycle behavior

### Cross-Device & Remote
- **ChatGPT relay**: active sessions sync across phone, desktop, and web
- **Remote SSH**: connect directly to remote development environments
- **Codex Cloud**: submit tasks to a cloud environment that keeps running after you close your laptop

## Quick Start

### Installation

Official install script:

```bash
# macOS / Linux
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Homebrew:

```bash
brew install --cask codex
```

npm (alternative):

```bash
npm install -g @openai/codex
```

Verify installation:

```bash
codex --version
```

### Log In

```bash
codex
```

Choose **Sign in with ChatGPT** (recommended) or use an OpenAI API key.

### Common Commands

```bash
codex                                      # Start an interactive session
codex "analyze the structure of this project"  # One-shot prompt
codex exec "run the test suite"            # Non-interactive / CI mode
codex review                               # Review uncommitted changes
codex resume                               # Resume the most recent session
codex cloud                                # Manage cloud tasks
codex mcp list                             # List configured MCP servers
codex --image error.png "how do I fix this error"  # Pass image context
```

## Approval Modes & Sandbox

Codex uses an **approval mode** to decide when to pause for confirmation and a **sandbox** to define file and network access.

### Approval Modes

| Mode | Description |
| --- | --- |
| `suggest` (default) | Ask before every change |
| `auto-edit` | Auto-edit files, ask before running commands |
| `full-auto` | Auto-edit and run commands (use with caution) |

```bash
codex --approval-mode auto-edit
codex --approval-mode full-auto
```

### Sandbox Modes

| Mode | Description |
| --- | --- |
| `read-only` | Read-only, no file modifications (similar to plan mode) |
| `workspace-write` | Read/write within the current working directory |
| `danger-full-access` | No sandbox restrictions |

```bash
codex -s read-only
codex --sandbox workspace-write
```

> Use `/permissions` in the interactive UI to switch quickly. On unfamiliar projects, start with `suggest` plus `read-only` or `workspace-write`.

## Best Practices

1. **Start with `suggest` mode**: increase automation only after you know the project.
2. **Scope tasks clearly**: mention target files, expected behavior, and tests to run.
3. **Review diffs and run tests**: AI-generated changes still need human review.
4. **Use Skills for repetitive workflows**: reduce repeated prompting.
5. **Use a strict sandbox for sensitive code**: avoid accidental file or network access.

## Related Resources

- [GitHub Repository](https://github.com/openai/codex)
- [Codex CLI Documentation](https://developers.openai.com/codex/cli)
- [OpenAI: Work with Codex from Anywhere](https://openai.com/index/work-with-codex-from-anywhere/)

## License

Codex CLI is released under the Apache-2.0 license. Use of OpenAI model services is subject to the corresponding terms of service.
