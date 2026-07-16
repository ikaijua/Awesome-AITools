# OpenCode Introduction

## What is OpenCode?

OpenCode is an open-source, terminal-native AI coding agent. It runs in your terminal with a polished TUI and a client/server architecture, and it is provider-agnostic — you can point it at Anthropic, OpenAI, Google, or local models rather than being locked to a single vendor. A desktop app (BETA) is also available for macOS, Windows, and Linux.

## Key Features

### 1. Provider-Agnostic
- Works with Anthropic, OpenAI, Google, and local/self-hosted models.
- Not tied to any single provider or subscription.

### 2. Terminal-Native TUI
- Fast, keyboard-driven interface built for the terminal.
- Client/server architecture so the agent can run detached from the UI.

### 3. Built-in Agents
- **build** — default full-access agent for development work.
- **plan** — read-only agent for analysis and exploration; denies edits and asks before running commands.
- **general** — subagent for complex searches and multistep tasks, invoked with `@general`.

### 4. LSP Integration
- Language Server Protocol support for richer, code-aware assistance.

### 5. Extensible
- Custom agents and MCP (Model Context Protocol) server support.
- Configurable via project and global config.

## Quick Start

### Installation

```bash
# Install script
curl -fsSL https://opencode.ai/install | bash

# Package managers
npm i -g opencode-ai@latest          # or bun/pnpm/yarn
brew install anomalyco/tap/opencode  # macOS and Linux (recommended)
scoop install opencode               # Windows
choco install opencode               # Windows
sudo pacman -S opencode              # Arch Linux
mise use -g opencode                 # Any OS
```

### Desktop App (BETA)

Download directly from the [releases page](https://github.com/anomalyco/opencode/releases) or [opencode.ai/download](https://opencode.ai/download).

### Usage

Run `opencode` in a project directory, then switch between the **build** and **plan** agents with the `Tab` key.

## Related Resources

- [Website](https://opencode.ai)
- [Documentation](https://opencode.ai/docs)
- [GitHub Repository](https://github.com/anomalyco/opencode)
- [Discord](https://discord.gg/opencode)
