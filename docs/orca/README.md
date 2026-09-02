# Orca Introduction

## What is Orca?

Orca is a cross-platform **Agent Development Environment (ADE)** designed for orchestrating fleets of parallel AI coding agents. It lets you run Claude Code, Codex, OpenCode, Pi, and virtually any CLI agent side-by-side — each in its own isolated git worktree — so you can compare results and merge the best one.

## Core Philosophy

### Parallel Agents, One Workspace
Instead of switching between terminal windows, Orca brings multiple agents into a single desktop IDE. One prompt can be fanned out across several agents, and you pick the winner.

### Bring Your Own Subscriptions
Orca does not replace your agents; it runs the agents you already have. You keep your own API keys and subscriptions for Claude, Codex, OpenAI, etc.

### Desktop-First, Mobile-Aware
Orca is a native desktop app for macOS, Windows, and Linux, with a mobile companion that lets you monitor and steer agents from your phone.

## Core Features

### Parallel Worktrees
- Fan one prompt across up to five agents.
- Each agent runs in its own isolated git worktree.
- Compare outputs side-by-side and merge the winning solution.

### Mobile Companion
- Get notified when an agent finishes or needs attention.
- Send follow-ups from iOS or Android.

### Terminal & Editor
- Ghostty-class terminals with WebGL rendering, infinite splits, and persistent scrollback.
- VS Code-style editor with autosave; drag files or images directly into agent prompts.

### Design Mode
- Click any UI element in a real Chromium window.
- Automatically send the element's HTML, CSS, and a cropped screenshot into the agent context.

### Native Integrations
- Browse GitHub PRs, issues, and Linear project boards in-app.
- Open a worktree directly from a task.
- Review diffs and annotate lines without leaving Orca.

### SSH Worktrees
- Run agents on a remote server with full file editing, git, and terminal access.
- Auto-reconnect and port forwarding included.

### Computer Use
- Let agents operate desktop apps and visible UI when a workflow needs real interaction.

### Supported Agents
Works with any CLI agent, including but not limited to:
Claude Code, Codex, Grok, Cursor, GitHub Copilot, OpenCode, MiMo Code, Amp, OpenClaude, Antigravity, Pi, oh-my-pi, Hermes Agent, Devin, Goose, Auggie, Autohand Code, Charm, Cline, Codebuff, Command Code, Continue, Droid, Kilocode, Kimi, Kiro, Mistral Vibe, Qwen Code, Rovo Dev, and more.

## Quick Start

### Install Desktop App

Download from [onOrca.dev](https://www.onorca.dev) or install via package manager:

```bash
# macOS (Homebrew)
brew install --cask stablyai/orca/orca

# Arch Linux (AUR)
yay -S stably-stably-bin
```

Builds are also available for macOS Apple Silicon, macOS Intel, Windows (.exe), and Linux AppImage.

### Install Mobile Companion

- iOS: App Store or TestFlight
- Android: APK download from the official site

### Basic Usage

1. **Open Orca** and connect one or more agent CLIs installed on your PATH.
2. **Create a worktree** for the task you want to solve.
3. **Fan out a prompt** across multiple agents.
4. **Compare results** side-by-side.
5. **Annotate diffs** and ship the winning solution back to the agent.
6. **Merge** the best worktree into your main branch.

## Common Use Cases

### Compare Agent Outputs
Run the same coding task with Claude Code and Codex in parallel, then pick the more correct or idiomatic implementation.

### Long-Running Tasks
Keep agents running on a remote VPS or powerful workstation while you monitor progress from your phone.

### UI-Centric Development
Use Design Mode to capture real browser UI elements and feed them into an agent for frontend fixes or tests.

## Related Resources

- [GitHub Repository](https://github.com/stablyai/orca)
- [Official Website](https://www.onorca.dev)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Orca is available as a free desktop application. Agents run under your own subscriptions and API keys.
