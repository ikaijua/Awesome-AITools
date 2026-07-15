# Codex Introduction

## What is Codex?

Codex CLI is a high-performance, Rust-based coding agent from OpenAI that runs in your terminal. It's an AI-powered coding assistant that can understand and modify code directly from the command line. Powered by the GPT-5.4 ecosystem, Codex CLI provides developers with a ultra-low latency, workflow-integrated way to interact with code.

## Core Philosophy

### Terminal First & High Performance
Codex CLI is built in Rust for the fastest possible terminal interaction:
- Ultra-low latency responses powered by GPT-5.4 mini
- Use AI assistance without leaving your terminal
- Seamlessly integrates with existing shell scripts and pipes

### Understand and Modify
Not just generating code snippets, Codex CLI can:
- Understand your project structure
- Directly modify code in files
- Execute multi-step programming tasks with high speed

### Simple and Efficient
- Minimal configuration, works out of the box
- Focused on core programming tasks
- Doesn't disrupt your workflow

## Core Features

### Code Understanding
- Analyze project structure and dependencies
- Understand function and class purposes
- Trace code call relationships

### Code Modification
- Automatically fix bugs
- Refactor code
- Add new features

### Command Line Integration
- Ask questions directly in terminal
- Support pipes and redirections
- Works with shell scripts

## Quick Start

### Installation

```bash
npm install -g @openai/codex
```

### Configuration

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

### Basic Usage

```bash
# Ask a question
codex "What does this function do?"

# Ask it to modify code
codex "Help me refactor this function to be more readable"

# Specify a file
codex "Fix the bug in src/utils.js"
```

## Approval Modes & Sandbox

Codex CLI controls autonomy along two dimensions: an **approval policy** (when it pauses to ask you) and a **sandbox** (what it's allowed to touch). This is Codex's counterpart to Claude Code's `--permission-mode`.

### `--full-auto` — the low-friction "auto" mode

The closest equivalent to an "auto" mode: Codex runs routine actions on its own and only interrupts you when it really needs to.

```bash
codex --full-auto
```

### Approval policy — `--ask-for-approval` (`-a`)

- `untrusted` - Only trusted commands run automatically; everything else needs confirmation
- `on-failure` - Runs in the sandbox first, asks only when a command fails and needs to escalate
- `on-request` - The model decides when to ask for approval (default)
- `never` - Never asks (fully autonomous)

### Sandbox — `--sandbox` (`-s`)

- `read-only` - Can read files but not modify them (good for safe exploration, similar to a plan mode)
- `workspace-write` - Can read and write within the current workspace
- `danger-full-access` - No sandbox restrictions

### Handy combinations

```bash
# Low-friction auto mode
codex --full-auto

# Read-only exploration (plan-like)
codex -s read-only

# Fully unrestricted (use with caution)
codex --dangerously-bypass-approvals-and-sandbox
```

> Inside the interactive UI these are surfaced as **Read Only / Auto / Full Access** modes, switchable via `/approvals`. Start with a restrictive mode on unfamiliar projects and switch to `--full-auto` once you're comfortable letting Codex move faster.

## Common Commands

```bash
# Start interactive mode
codex

# Analyze current directory's code
codex "Analyze this project's structure"

# Generate tests
codex "Generate unit tests for src/api.js"
```

## Best Practices

1. **Provide Context** - Tell it what you're doing, and it will give better suggestions
2. **Iterate Gradually** - Start with the big picture, then dive into details
3. **Verify Results** - Always check and test AI-generated code yourself
4. **Use Interactively** - Ask follow-up questions and have it refine solutions

## Related Resources

- [GitHub Repository](https://github.com/openai/codex)
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Get API Key](https://platform.openai.com/api-keys)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Codex is developed by OpenAI and requires an OpenAI API key to use. Please follow OpenAI's terms of service.