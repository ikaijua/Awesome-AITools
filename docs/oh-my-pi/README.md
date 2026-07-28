# oh-my-pi Introduction

## What is oh-my-pi?

[oh-my-pi](https://github.com/can1357/oh-my-pi) (also known as `omp`) is a fork of [Pi](https://github.com/mariozechner/pi) by [@can1357](https://github.com/can1357). It is a terminal-native AI coding agent with the IDE wired in — designed to edit, search, debug, and execute code from a single TUI surface while leveraging everything your IDE already knows.

The project ships with 40+ model providers, 32 built-in tools, 14 LSP operations, and 28 DAP operations, all built on top of a ~55k-line Rust core.

## Key Features

### 1. IDE Integration Wired In
- Full LSP support so the agent can rename symbols, follow references, and reason about your codebase like an IDE.
- Real debugger integration via DAP: attach `lldb`, `dlv`, or `debugpy` and let the agent inspect stack frames and variables.

### 2. Code Execution with Tool-Calling
- Persistent Python and Bun workers run inside the agent session.
- Either kernel can call back into the agent's own tools (read, search, task) over a loopback bridge.
- Load a CSV with `tool.read` from Python and chart it from JavaScript without leaving the session.

### 3. Provider-Agnostic
- Works with 40+ providers, so you can bring your own API keys or local models.

### 4. Time-Traveling Stream Rules
- User-defined rules stay dormant until the model output matches a regex, then inject a reminder mid-stream and retry from the same point.
- Provides course-correction without paying a context tax on every turn.

### 5. Batteries Included
- 32 built-in tools and optimized prompts tuned per model for first-attempt edits, summarized file reads, and fast search.

## Quick Start

### Installation

```bash
# Install script (macOS / Linux)
curl -fsSL https://omp.sh/install | sh

# Windows PowerShell
irm https://omp.sh/install.ps1 | iex

# Homebrew
brew install can1357/tap/omp

# Bun (recommended)
bun install -g @oh-my-pi/pi-coding-agent

# mise
mise use -g github:can1357/oh-my-pi
```

### Usage

Run `omp` in a project directory to start an agent session. Use shell completions generated from live CLI metadata:

```bash
# zsh — add to ~/.zshrc
eval "$(omp completions zsh)"

# bash — add to ~/.bashrc
eval "$(omp completions bash)"

# fish
omp completions fish > ~/.config/fish/completions/omp.fish
```

## Related Resources

- [Website](https://omp.sh)
- [GitHub Repository](https://github.com/can1357/oh-my-pi)
