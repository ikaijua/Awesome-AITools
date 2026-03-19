# Claude Code Introduction

## What is Claude Code?

Claude Code is Anthropic's official command-line tool that brings Claude's powerful capabilities directly into your development workflow. It's an interactive AI assistant specifically designed to help developers with various software engineering tasks.

## Core Philosophy

### AI-Native Development
Claude Code is not just a code completion tool—it deeply integrates AI into the entire development workflow. It understands project context, executes complex task chains, and goes beyond generating mere code snippets.

### Context Awareness
Traditional code assistants can only see the current file, while Claude Code can:
- Explore and understand the entire codebase structure
- Track function calls and dependency relationships
- Maintain long-term memory, understanding project evolution history
- Preserve project knowledge across sessions

### Human-AI Collaboration
Claude Code adopts a "human-in-the-loop" design philosophy:
- AI proposes solutions, humans make final decisions
- Sensitive operations require user confirmation
- Transparent execution process, users always maintain control
- Supports iterative dialogue to progressively refine solutions

### Safety and Control
Safety is a core design principle of Claude Code:
- Dangerous operations (e.g., deleting files, force pushing) require explicit confirmation
- Automatic detection and alerts for potential security vulnerabilities
- Support for project-level security rules via CLAUDE.md
- Operations are traceable and easy to rollback

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