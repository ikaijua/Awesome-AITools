# Claude Code Introduction

## What is Claude Code?

Claude Code is Anthropic's official AI coding agent. In addition to the terminal CLI, it is available as a VS Code / Cursor / JetBrains IDE plugin, a standalone desktop app, a web interface at claude.ai/code, and—via Remote Control—the Claude iOS / Android mobile app. All surfaces share the same underlying engine, so CLAUDE.md files, MCP servers, Skills, Hooks, and memory stay consistent across devices.

## Core Philosophy

### Agent-First, Not Just Completion
Claude Code understands your entire codebase. It can plan across multiple files, edit code, run commands, check test results, and iterate based on feedback until the task you described is done.

### Project-Level Memory
Through the `CLAUDE.md` project instruction file and automatic memory, Claude Code remembers project structure, conventions, and common commands so you don't have to restate the context every time.

### Controllable Autonomy
From strict plan mode to automatic mode to a fully permission-skipping YOLO mode, you can choose how autonomous Claude should be based on task risk and trust.

### Unified Surfaces
Whether you work in the terminal, IDE, desktop app, web, or phone, you connect to the same Claude Code engine, and sessions and settings can carry across devices.

## Available Surfaces

| Surface | Description |
| --- | --- |
| Terminal CLI | Full feature set, best for deep development |
| VS Code / Cursor | Plugin with inline diffs and chat panel |
| JetBrains | Plugin for IDEA, PyCharm, WebStorm, etc. |
| Desktop App | Visual diffs, side-by-side sessions, scheduled tasks |
| Web | claude.ai/code, no local setup required |
| Mobile App | Claude iOS / Android app connects to local sessions via Remote Control |

## Core Capabilities

### Code Understanding & Editing
- Automatically explores codebase structure, dependencies, and call relationships
- Refactors across files, adds features, and fixes bugs
- Inline diffs and visual review

### Terminal & Toolchain Integration
- Runs shell commands, tests, and build scripts
- Native Git operations and GitHub / GitLab integration
- Extensible to CI/CD, Slack, Chrome, and more

### Extensibility
- **MCP servers**: connect to databases, browsers, external APIs
- **Skills**: reusable project-level workflows (invoke with `/skill`)
- **Hooks**: scripts triggered at lifecycle points such as file writes or command execution
- **Subagents**: split complex work among specialized agents that run in parallel

### Cross-Device Collaboration
- **Remote Control**: continue a local Claude Code session from your phone or browser
- **Cloud sessions**: `claude --cloud` starts a task you can continue from mobile
- Files, credentials, and the local environment stay on the machine running Claude Code

## Quick Start

### Installation

Official install script (macOS / Linux):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Homebrew:

```bash
brew install claude-code
```

npm (alternative):

```bash
npm install -g @anthropic-ai/claude-code
```

On Windows, use WinGet or the PowerShell install script. See the [official docs](https://docs.anthropic.com/en/docs/claude-code/overview) for details.

First run:

```bash
claude
```

Log in with your Anthropic account, or set `ANTHROPIC_API_KEY` beforehand.

### Common Commands

```bash
claude                          # Start an interactive session
claude /path/to/project         # Start in a specific directory
claude "fix the login bug"      # Ask directly
claude --permission-mode plan   # Plan before making changes
claude --permission-mode auto   # Auto-approve routine actions
claude --cloud                  # Start a cloud session resumable on mobile
```

### Permission Modes

| Mode | Description |
| --- | --- |
| `default` | Asks before sensitive actions (recommended for daily use) |
| `plan` | Explores and plans only, waits for confirmation before changes |
| `auto` | Auto-approves low-risk routine actions, still asks for sensitive ones |
| `--dangerously-skip-permissions` | Skips all confirmations (use only in trusted repos / CI) |

> Start with `default` or `plan` on unfamiliar projects, then move to `auto` once you trust the workflow.

## Common Slash Commands

- `/help` - Show help
- `/clear` - Clear the current session
- `/commit` - Create a Git commit
- `/review-pr` - Review a Pull Request
- `/remote-control` - Enable cross-device Remote Control
- `/mcp` - View MCP server status
- `/settings` or `/config` - Open settings

## Configuration Files

- `~/.claude/settings.json`: user-level settings (permissions, model, hooks, environment variables)
- `CLAUDE.md`: project-level instructions and rules
- `.claude/`: project-local memory and configuration

## Best Practices

1. **Write clear task goals**: describe expected behavior, relevant files, and tests to run.
2. **Use CLAUDE.md**: document conventions, safety guardrails, and common commands.
3. **Start with plan/default**: increase automation only after you know the project.
4. **Review diffs and run tests**: treat Claude's output like a colleague's PR.
5. **Use Skills and Hooks**: encapsulate repetitive workflows into reusable capabilities.

## Related Resources

- [Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
- [GitHub Repository](https://github.com/anthropics/claude-code)
- [Claude Code Remote Control](https://docs.anthropic.com/en/docs/claude-code/remote-control)

## License

Claude Code is developed and maintained by Anthropic. Use is subject to Anthropic's terms of service.
