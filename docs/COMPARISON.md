# Terminal AI Coding Tools Comparison

This document compares three mainstream terminal AI coding tools: Claude Code, Codex, and Gemini CLI.

## Quick Comparison

| Aspect | Claude Code | Codex CLI | Gemini CLI |
|--------|-------------|-----------|------------|
| Developer | Anthropic | OpenAI | Google |
| Open Source | No | No | Yes (fully) |
| Architecture | TypeScript/Node | Rust-based | TypeScript/Node |
| API Required | Anthropic API | OpenAI API | Google AI API |
| Multimodal | Text only | Text only | Supports images & design assets |
| Persistent Memory | ✅ Yes (Full) | ❌ No | ⚠️ Project Context (`GEMINI.md`) |
| Context Window | 1M Tokens | 128K Tokens | 1M+ Tokens |
| Project Understanding | Deep understanding of entire projects | Single file/function focus | Massive-scale repository mapping |
| Safety Design | Confirmation for dangerous operations | Sandbox-first | Confirmation for dangerous operations |
| Extensibility | MCP, skills, hooks | Security-focused scripts | Customizable (open source) |

## Detailed Comparison

### Context and Memory Capabilities

**Claude Code**
- Ultra-long context, understands entire project structure
- Persistent memory, remembers project info across sessions
- Supports `claude.md` for project rules and style guides

**Codex CLI**
- Focuses on high-speed single file or function level understanding
- Rust-based architecture for ultra-low latency
- No persistent session memory, each conversation is independent

**Gemini CLI**
- 1M+ token context window, can ingest entire large-scale repositories
- Project-level context via `GEMINI.md` files for architectural mandates
- Multimodal support for design-to-code workflows (images, PDFs)

### Safety and Control

**Claude Code**
- Dangerous operations (deleting files, force pushing, etc.) require user confirmation
- Configurable project-level safety rules via `claude.md`
- Automatic detection of potential security vulnerabilities

**Codex CLI**
- Sandbox-first execution environment
- Real-time vulnerability patching in "Security Mode"
- Relatively simple but fast safety design

**Gemini CLI**
- Open source code is auditable
- Project-specific mandates in `GEMINI.md` ensure architectural compliance
- Basic safety protections with confirmation for sensitive actions

### Extension and Integration

**Claude Code**
- Supports MCP (Model Context Protocol) servers
- Customizable skills system
- Configurable automation hooks
- Deep Git/GitHub/GitLab integration

**Codex CLI**
- Optimized for shell script integration
- Lightweight and "Unix-native" workflow
- Focused on security and performance

**Gemini CLI**
- Fully open source, self-modifiable and extensible
- Deep integration with Google Search for up-to-date documentation
- Supports shell scripts and pipe operations
- Google ecosystem integration

### Entry Barrier

**Claude Code**
- Requires Anthropic API access
- Powerful but requires learning the agentic workflow

**Codex CLI**
- Requires OpenAI API key (GPT-5.4 ecosystem)
- Simple configuration, minimal latency

**Gemini CLI**
- Requires Google AI API key
- Flexible and customizable for developers who want full control

## Recommendations

### Choose Claude Code if you need:
- Deep understanding of large projects
- Complex autonomous refactoring
- High security and controllability
- Parallel agent collaboration
- Deep integration with Git platforms

### Choose Codex CLI if you need:
- Ultra-fast, low-latency performance
- "Unix-native" experience for scripts
- Security-focused vulnerability patching
- Minimal configuration

### Choose Gemini CLI if you need:
- Processing of massive-scale codebases (1M+ context)
- Multimodal capabilities (design assets, screenshots)
- Customization and extensibility of the tool itself
- Real-time web grounding via Google Search
- Transparent and controllable open-source code

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