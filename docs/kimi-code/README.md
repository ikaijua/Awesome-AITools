# Kimi Code CLI Introduction

## What is Kimi Code CLI?

Kimi Code CLI is Moonshot AI's AI coding agent that runs in your terminal. It can read and edit code, run shell commands, search files, fetch web pages, and decide the next step based on feedback from tools and the user. It works out of the box with Kimi Code / Moonshot AI models and can also be configured for other compatible providers.

## Core Philosophy

### Terminal-first agent workflow
Kimi Code is designed for developers who want to stay in the terminal:
- Start an interactive TUI directly in a project directory
- Ask natural-language questions about a repository
- Let the agent plan, edit, run tests, and iterate in the same session

### Controlled autonomy
Kimi Code can do more than answer questions, but keeps permission modes explicit:
- Read-only exploration runs smoothly by default
- File edits and shell commands can require approval
- YOLO and Auto modes are available when you deliberately want less friction

### Extensible agent platform
Kimi Code includes capabilities commonly needed for agentic development:
- MCP configuration through natural-language commands
- Skills and subagents for focused tasks
- Lifecycle hooks for local automation
- ACP editor integration for Zed, JetBrains, and other Agent Client Protocol clients

## Core Features

### Code understanding and editing
- Analyze project structure and dependencies
- Read, search, and modify files
- Implement features, fix bugs, refactor code, and generate tests

### Shell and workflow automation
- Run build, test, lint, and project scripts
- Chain multiple steps while observing tool feedback
- Support non-interactive prompt mode for scripts and CI-style tasks

### Multimodal and editor integration
- Paste screenshots or videos into the TUI when the selected model supports multimodal input
- Use `kimi acp` from ACP-compatible editors and IDEs
- Open the browser-based UI via the local Kimi server

## Quick Start

### Installation

Recommended install script:

```bash
# macOS / Linux
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash

# Windows PowerShell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

Homebrew:

```bash
brew install kimi-code
```

npm / pnpm installation:

```bash
npm install -g @moonshot-ai/kimi-code
# or
pnpm add -g @moonshot-ai/kimi-code
```

Verify the installation:

```bash
kimi --version
```

### First launch

```bash
cd your-project
kimi
```

On first launch, run `/login` in the TUI and choose either Kimi Code OAuth or a Moonshot AI platform API key. You can also log in from the shell without entering the TUI:

```bash
kimi login
```

## Common CLI Commands

```bash
# Start an interactive session in the current directory
kimi

# Continue the most recent session in the current directory
kimi --continue
kimi -C

# Choose a previous session, or resume a known session ID
kimi --session
kimi --session <session-id>

# Run one prompt non-interactively
kimi --prompt "Summarize the current repository status"
kimi -p "Explain the latest diff"

# Emit JSONL-style streaming output for automation
kimi -p "List changed files" --output-format stream-json

# Use a specific model for this launch
kimi --model kimi-code/kimi-for-coding
kimi -m kimi-code/kimi-for-coding -p "Explain this project"

# Start in Plan mode, focusing on read-only exploration before edits
kimi --plan

# Add an extra workspace directory for the session
kimi --add-dir ../shared-lib

# Load skills from custom directories for this launch
kimi --skills-dir /path/to/team-skills --skills-dir ./local-skills
```

## Permission Modes: Manual, YOLO, Auto, and Plan

Kimi Code's normal interactive flow asks before side-effecting operations such as file writes and shell commands. You can switch modes when you need a different balance between safety and speed.

### YOLO mode

YOLO mode skips approval prompts for regular tool calls, including file writes and shell command execution. Use it only in trusted repositories and for tasks where you are comfortable reviewing the result afterward.

```bash
# Start a session with YOLO mode enabled
kimi --yolo
kimi -y

# Hidden aliases documented by Kimi Code
kimi --yes
kimi --auto-approve
```

Inside the TUI:

```text
/yolo
/yolo on
/yolo off
/yes
```

Plan-mode exit approval is not bypassed by YOLO mode.

### Auto mode

Auto mode lets the agent handle approvals automatically and avoids asking the user clarifying questions. It is useful for unattended work where you want more autonomy without using the full YOLO toggle.

```bash
kimi --auto
kimi --continue --auto
```

Inside the TUI:

```text
/auto
/auto on
/auto off
```

### Plan mode

Plan mode asks the agent to explore and produce a plan before making file changes. It is useful for larger or higher-risk tasks.

```bash
kimi --plan
```

Inside the TUI:

```text
/plan
/plan clear
```

Keyboard shortcut: `Shift-Tab` toggles Plan mode.

## Useful Slash Commands

| Command | Purpose |
| --- | --- |
| `/help` | Show built-in help, shortcuts, and available commands |
| `/login` / `/logout` | Sign in or clear credentials |
| `/provider` | Manage configured model providers |
| `/model` | Switch the model used in the current session |
| `/permission` | Select a permission mode |
| `/settings` or `/config` | Open settings inside the TUI |
| `/new` or `/clear` | Start a fresh session |
| `/sessions` or `/resume` | Browse and restore session history |
| `/compact` | Compress the current context to free tokens |
| `/undo` | Remove recent prompts from active context |
| `/reload` | Reload configuration without restarting the CLI |
| `/init` | Analyze the codebase and generate `AGENTS.md` |
| `/add-dir` | Add an extra workspace directory |
| `/mcp` | List MCP server status |
| `/mcp-config` | Configure MCP servers and MCP OAuth login |
| `/plugins` | Open the plugin manager |
| `/editor` | Configure the external editor opened by `Ctrl-G` |
| `/theme` | Change the terminal UI theme |
| `/exit`, `/quit`, `/q` | Exit Kimi Code CLI |

## Keyboard Shortcuts

| Shortcut | Function |
| --- | --- |
| `Enter` | Submit the current input |
| `Shift-Enter` / `Ctrl-J` | Insert a newline |
| `↑` / `↓` | Browse input history |
| `Esc` / `Ctrl-C` | Interrupt streaming output or close a popup |
| `Ctrl-D` | Exit when the input box is empty |
| `Shift-Tab` | Toggle Plan mode |
| `Ctrl-S` | Inject a message into a running turn |
| `Ctrl-O` | Collapse or expand tool output |
| `Ctrl-G` | Edit the current input in an external editor |

## Configuration Files

Kimi Code stores local data under `~/.kimi-code/` by default. Set `KIMI_CODE_HOME` to move this directory.

Main files:
- `~/.kimi-code/config.toml` - providers, models, default model, permission mode, hooks, and agent/runtime settings
- `~/.kimi-code/tui.toml` - terminal UI preferences such as theme, editor, notifications, and update behavior
- `~/.kimi-code/mcp.json` - MCP server declarations
- `.kimi-code/local.toml` - project-local remembered settings such as extra workspace directories

Useful maintenance commands:

```bash
kimi doctor
kimi doctor config
kimi doctor tui
kimi upgrade
```

## Goal Mode

Use `/goal` when a task has a clear finish line and the next useful step depends on what the agent learns while working:

```text
/goal Fix every bug labeled checkout-regression, add or update tests for each fix, and run the checkout test suite
```

Common commands:

| Command | Action |
| --- | --- |
| `/goal` or `/goal status` | Show the current goal and its progress |
| `/goal pause` | Pause the active goal |
| `/goal resume` | Resume a paused or blocked goal |
| `/goal cancel` | Cancel the current goal |
| `/goal replace <objective>` | Replace the current goal with a new one |
| `/goal next <objective>` | Queue a goal to run after the current one |

A goal can end in three states:
- **complete**: the objective is done
- **paused**: you paused it, interrupted the turn, resumed a session with an active goal, or hit a runtime error
- **blocked**: Kimi Code needs input, cannot complete the goal as stated, or reached a budget limit

The Web UI also shows the current goal in a status strip where you can expand details, pause, resume, or cancel.

## Session Resume and Export

Kimi Code persists every conversation as a session. You can close the terminal and pick up where you left off:

```bash
# Resume the most recent session in the current directory
kimi --continue
kimi -C

# Browse history or resume a specific session ID
kimi --session
kimi --session <session-id>
```

Export sessions:

```bash
# Package a session as a ZIP (includes diagnostic logs)
kimi export <session-id>

# Export as a Markdown file
kimi -p "/export" --session <session-id>
```

## Server, Web UI, and ACP

```bash
# Start or reuse the local background server
kimi server run

# Open the browser UI
kimi web

# Run the server in the foreground
kimi server run --foreground

# Entry point used by ACP-compatible editors
kimi acp
```

### Web UI Login

The Web UI uses the same Kimi account authentication as the CLI. There are two login methods:

1. **OAuth device-code flow (recommended)**
   - Run `kimi login` in the CLI and choose **Kimi Code OAuth**
   - The terminal prints an authorization URL and an 8-digit device code
   - Open the URL on your phone or computer browser, sign in to your Kimi account, and enter the device code
   - Once authorized, the Web UI on the same machine is automatically logged in

2. **Moonshot AI API Key**
   - Create an API Key at `platform.kimi.com` or `platform.kimi.ai`
   - Choose API Key login when the CLI or Web UI first starts and paste the key

> Note: If you run `kimi server run --foreground` on a remote server, access the Web UI through a local browser on the server or via an SSH tunnel, and complete OAuth/API Key login once.

### Checking Goal Status in the Web UI

After logging in, open the Web UI:

- The current goal appears in a strip below the conversation
- Select the strip to expand or collapse its details
- Goals with a token budget show a progress bar in the header; goals without a budget do not
- The strip provides **Pause / Resume / Cancel** actions
- Selecting **Resume** starts the next goal turn

For Zed or JetBrains ACP integration, configure the editor to run `kimi acp` over stdio after logging in once from the CLI.

## Best Practices

1. **Start in Plan mode for large changes** - Review the plan before letting the agent edit files.
2. **Use YOLO only in trusted directories** - It skips approval for edits and shell commands.
3. **Keep prompts concrete** - Mention files, expected behavior, tests to run, and constraints.
4. **Review diffs and run tests** - Treat agent output like a teammate's patch.
5. **Use `/mcp-config` for integrations** - Prefer the built-in MCP flow over hand-editing JSON when possible.
6. **Use `-p` for automation** - Non-interactive prompt mode is better for scripts than driving the TUI.

## Related Resources

- [GitHub Repository](https://github.com/MoonshotAI/kimi-code)
- [Official Documentation](https://moonshotai.github.io/kimi-code/en/)
- [Command Reference](https://moonshotai.github.io/kimi-code/en/reference/kimi-command)
- [Interaction and Approvals](https://moonshotai.github.io/kimi-code/en/guides/interaction)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Kimi Code CLI is released under the MIT License. Usage of Kimi Code, Moonshot AI, or third-party model providers is subject to the corresponding provider terms.
