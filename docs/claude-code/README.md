# Claude Code Introduction

## What is Claude Code?

Claude Code is Anthropic's official command-line tool that brings Claude's powerful capabilities directly into your development workflow. It's an interactive AI assistant specifically designed to help developers with various software engineering tasks.

## Core Philosophy

### More Than Just "Code Completion"
Most AI coding assistants just complete a few lines of code. But Claude Code is more like a real partner who understands your project—you tell it "fix the login page bug," and it will read the code, find the issue, fix it, and even commit the change for you.

### Remembers Your Project
Ever had this awkward moment: you explain your project structure to an AI, close the conversation, and next time you have to start all over? Claude Code is different—it remembers:
- Knows your project's modules and how they connect
- Picks up where you left off in the next conversation
- You can use CLAUDE.md to tell it your project's "rules"

### You're in Charge
Claude Code asks you first, never acts on its own:
- Big decisions like deleting files or pushing code need your approval
- It tells you what it's about to do and waits for your confirmation
- If something goes wrong, you can always ask it to fix it

### Safety First
It's more cautious than you are:
- Proactively warns you when it spots potential issues
- Never quietly executes dangerous operations
- You can specify what's absolutely off-limits in CLAUDE.md

## Core Features

### 1. Code Understanding & Navigation
- Automatically explore and understand codebase structure
- Intelligent file and code content search
- Quickly locate function, class, and variable definitions

### 2. Code Editing & Refactoring
- Automatically fix code defects
- Intelligent refactoring and code optimization
- Add new features and functionality

### 3. Development Workflow Integration
- Native Git operations support
- Integration with GitHub/GitLab and other CI/CD platforms
- Automated testing and code review

### 4. Multi-Model Support
- Support for the latest Claude 4.5/4.6 model family
- Switch between models based on task requirements
- Fast mode for quicker responses

## Key Characteristics

### Safe & Reliable
- Built-in safety guards to avoid dangerous operations
- Automatic detection of potential security vulnerabilities
- User confirmation required for sensitive operations

### Intelligent Context
- Automatic conversation history compression for long sessions
- Persistent memory system preserving context across sessions
- Project-level configuration and memory support

### Flexible & Extensible
- Support for MCP (Model Context Protocol) servers
- Customizable skills and tools
- Configurable automation hooks

## Quick Start

### Installation

```bash
npm install -g @anthropic-ai/claude-code
```

### Basic Usage

```bash
# Start Claude Code
claude

# Start in a specific directory
claude /path/to/project

# Use Fast mode
claude --fast
```

### Common Commands

- `claude` - Start interactive session
- `claude "your question"` - Ask a direct question
- `/help` - Get help
- `/clear` - Clear conversation history
- `/commit` - Create a Git commit
- `/review-pr` - Review a Pull Request

## Configuration Files

### settings.json
Main configuration file controlling Claude Code behavior:
- Permission settings
- Environment variables
- Automation hooks

### CLAUDE.md
Project-level instruction file defining project-specific rules and context.

### keybindings.json
Custom keyboard shortcuts configuration.

## Comparison with Other Tools

### Claude Code vs Codex

| Aspect | Claude Code | Codex |
|--------|-------------|-------|
| Developer | Anthropic | OpenAI |
| Context Capability | Ultra-long context, understands entire projects | Focused on single files or functions |
| Memory System | Persistent memory, remembers projects across sessions | No persistent memory |
| Safety Design | Dangerous operations require confirmation, configurable rules | Relatively simple |
| Extensibility | Supports MCP, skills system, hooks | Fewer extension options |

**Recommendation**: Choose Claude Code for deep understanding of large projects, cross-session work, and security focus. Choose Codex for lightweight, single-file assistance.

### Claude Code vs Gemini CLI

| Aspect | Claude Code | Gemini CLI |
|--------|-------------|------------|
| Developer | Anthropic | Google |
| Open Source | Not open source | Fully open source |
| Multimodal | Text only | Supports images and other modalities |
| Memory System | Persistent memory | No persistent memory |
| Integration | Deep Git/GitHub/GitLab integration | Basic integration |

**Recommendation**: Choose Claude Code for project-level memory and deep workflow integration. Choose Gemini CLI if you value open source, need multimodal capabilities, or want Google ecosystem integration.

## Best Practices

1. **Provide Clear Task Descriptions** - More specific questions yield better answers
2. **Leverage CLAUDE.md** - Add context descriptions for your project
3. **Use the Skills System** - Execute common tasks quickly via `/skill-name`
4. **Configure Automation Hooks** - Improve development efficiency

## Related Resources

- [Official Documentation](https://docs.anthropic.com/claude-code)
- [GitHub Repository](https://github.com/anthropics/claude-code)
- [Issue Tracker](https://github.com/anthropics/claude-code/issues)

## License

Claude Code is developed and maintained by Anthropic. Use is subject to Anthropic's terms of service.