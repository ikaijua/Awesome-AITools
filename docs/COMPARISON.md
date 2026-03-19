# Terminal AI Coding Tools Comparison

This document compares three mainstream terminal AI coding tools: Claude Code, Codex, and Gemini CLI.

## Quick Comparison

| Aspect | Claude Code | Codex | Gemini CLI |
|--------|-------------|-------|------------|
| Developer | Anthropic | OpenAI | Google |
| Open Source | No | No | Yes (fully) |
| API Required | Anthropic API | OpenAI API | Google AI API |
| Multimodal | Text only | Text only | Supports images |
| Persistent Memory | ✅ Yes | ❌ No | ❌ No |
| Project Understanding | Deep understanding of entire projects | Single file/function focus | Moderate |
| Safety Design | Confirmation for dangerous operations | Relatively simple | Relatively simple |
| Extensibility | MCP, skills, hooks | Limited | Customizable (open source) |

## Detailed Comparison

### Context and Memory Capabilities

**Claude Code**
- Ultra-long context, understands entire project structure
- Persistent memory, remembers project info across sessions
- Supports CLAUDE.md for project rules

**Codex**
- Focuses on single file or function level understanding
- No persistent memory, each conversation is independent

**Gemini CLI**
- Long context processing capability
- No persistent memory
- Can pipe in file contents

### Safety and Control

**Claude Code**
- Dangerous operations (deleting files, force pushing, etc.) require user confirmation
- Configurable project-level safety rules via CLAUDE.md
- Automatic detection of potential security vulnerabilities

**Codex**
- Relatively simple safety design
- Code modifications require user initiation

**Gemini CLI**
- Open source code is auditable
- Basic safety protections

### Extension and Integration

**Claude Code**
- Supports MCP (Model Context Protocol) servers
- Customizable skills system
- Configurable automation hooks
- Deep Git/GitHub/GitLab integration

**Codex**
- Fewer extension options
- Basic command-line integration

**Gemini CLI**
- Fully open source, self-modifiable and extensible
- Supports shell scripts and pipe operations
- Google ecosystem integration

### Entry Barrier

**Claude Code**
- Requires Anthropic API access
- Relatively complex configuration, but powerful

**Codex**
- Requires OpenAI API key
- Simple configuration, works out of the box

**Gemini CLI**
- Requires Google AI API key
- Can install from source, suitable for developers

## Recommendations

### Choose Claude Code if you need:
- Deep understanding of large projects
- Cross-session project memory
- High security and controllability
- Complex workflow integration
- Deep integration with Git platforms

### Choose Codex if you need:
- Quick single-file assistance
- Simple and direct experience
- Minimal configuration
- Already familiar with OpenAI ecosystem

### Choose Gemini CLI if you need:
- Fully open source solution
- Multimodal capabilities (image processing)
- Customization and extensibility
- Integration with Google services
- Transparent and controllable code

## Combined Usage

These three tools are not mutually exclusive. You can choose flexibly based on scenarios:

- **Daily Development**: Claude Code for complex tasks
- **Quick Q&A**: Codex or Gemini CLI for lightweight queries
- **Multimodal Needs**: Gemini CLI for image-related tasks
- **Server Environment**: Gemini CLI for auditable open source

## Related Links

- [Claude Code Introduction](claude-code/README.md)
- [Codex Introduction](codex/README.md)
- [Gemini CLI Introduction](gemini-cli/README.md)