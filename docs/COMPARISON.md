# AI Coding Tools Comparison: Claude Code vs Codex vs Antigravity

This document compares three mainstream AI coding tools: Claude Code, Codex, and Google's Antigravity (the agent-first IDE that replaces the now-deprecated Gemini CLI).

## Quick Comparison

| Aspect | Claude Code | Codex CLI | Antigravity |
|--------|-------------|-----------|-------------|
| Developer | Anthropic | OpenAI | Google |
| Form Factor | Terminal CLI + IDE plugins + desktop/web | Terminal CLI + IDE extensions + web/desktop | Standalone IDE (VS Code fork) + Manager dashboard |
| Open Source | No | No | No (proprietary, free during preview) |
| Default Model | Claude 5 (Fable/Mythos) / Claude 4 (Sonnet/Opus) | OpenAI GPT (Codex family) | Gemini 3 Pro / Flash |
| Other Models | — | — | Claude 5 (Fable), Claude Sonnet 4.6, Claude Opus 4.6, GPT-OSS-120B |
| API Required | Anthropic API or Claude account | OpenAI API or ChatGPT account | Google account (no separate API key during preview) |
| Multimodal | Text + images | Text + images | Text + images + integrated browser |
| Persistent Memory | ✅ Full (per-project + user memory) | ⚠️ Limited per-session | ✅ Cross-run agent learning + project context |
| Verifiable Output | Diff + tool transcripts | Diff + sandbox output | **Artifacts**: plans, screenshots, browser recordings |
| Multi-Agent | Subagents and workflows in CLI | Parallel runs via web/app | Manager view fans out agents across workspaces |
| Safety Design | Confirmation for dangerous operations | Sandbox-first | Plan-then-act with reviewable Artifacts |
| Permission Modes | `--permission-mode` (default / plan / auto) | `--full-auto`, `--ask-for-approval`, `--sandbox` (read-only / workspace-write / full-access) | Read Only / Auto / Full Access; approve plan Artifact before execution |
| Extensibility | MCP, skills, hooks, plugins | MCP, scripts | VS Code extensions, integrated browser/terminal |

## Detailed Comparison

### Context and Memory Capabilities

**Claude Code**
- Long context with deep multi-file understanding
- Persistent memory across sessions (user + project memory)
- Project rules via `CLAUDE.md` / `AGENTS.md`

**Codex CLI**
- Focuses on fast single-file or function-level edits
- Lightweight per-session state, designed for low-latency loops
- No first-class persistent memory; rely on prompts and `AGENTS.md`

**Antigravity**
- Agent-first workflow: plan → edit → run → verify carries context across steps
- Agents learn from prior runs, including the corrections you apply
- Project context is anchored inside the workspace; the integrated browser feeds runtime context (DOM, screenshots) back to the agent

### Safety and Control

**Claude Code**
- Dangerous operations (deleting files, force pushing, etc.) require user confirmation
- Per-project safety rules via memory and settings
- Tool permission model (allowlists, hooks) for tight control

**Codex CLI**
- Sandbox-first execution environment
- Strong defaults for filesystem and network isolation
- Simple, fast safety model focused on terminal use

**Antigravity**
- Agents draft a **plan Artifact** before acting; you approve before execution
- Browser recordings and screenshots make agent behavior auditable after the fact
- Runs inside the IDE with workspace-scoped access

### Extension and Integration

**Claude Code**
- MCP (Model Context Protocol) servers
- Customizable skills system, hooks for automation
- Deep Git/GitHub/GitLab integration

**Codex CLI**
- Lightweight, "Unix-native" workflow optimized for shell pipelines
- MCP support and tight terminal integration
- Easy to compose with existing scripts

**Antigravity**
- Built on VS Code, so the existing extension ecosystem applies
- Built-in browser the agent can drive (clicks, navigation, screenshot capture)
- Multi-model selector (Gemini, Claude, GPT-OSS) inside one IDE

### Entry Barrier

**Claude Code**
- Requires an Anthropic API key or Claude account
- Powerful but rewards learning the agentic / memory / hooks model

**Codex CLI**
- Requires an OpenAI API key or ChatGPT account
- Minimal configuration, very fast feedback loop

**Antigravity**
- Free during the public preview; sign in with a Google account
- IDE download for Windows / macOS / Linux; no API key juggling for the default Gemini models

## Recommendations

### Choose Claude Code if you need:
- Deep understanding and refactoring of large, established codebases
- Long-running agentic workflows with strong memory and hooks
- Tight terminal + IDE + GitHub integration
- A mature permission model for autonomous execution

### Choose Codex CLI if you need:
- Ultra-fast, low-latency single-file or single-function edits
- A "Unix-native" experience that composes with shell scripts
- Sandbox-first safety with minimal configuration
- A lightweight day-to-day terminal companion

### Choose Antigravity if you need:
- An agent-first IDE rather than an autocomplete or terminal tool
- **Verifiable** agent runs via Artifacts (plans, screenshots, recordings)
- An integrated browser the agent can drive to test what it built
- Multi-agent fan-out via Manager view, with multi-model choice (Gemini / Claude / GPT-OSS)
- Free access during the public preview, no API key required

## Combined Usage

These tools are not mutually exclusive. A common split:

- **Daily code editing / terminal flows**: Claude Code or Codex
- **Big agent-driven changes with browser verification**: Antigravity
- **Quick single-file edits**: Codex
- **Long-horizon multi-file refactors with strong memory**: Claude Code or Antigravity

## Related Links

- [Claude Code Introduction](claude-code/README.md)
- [Codex Introduction](codex/README.md)
- [Antigravity Introduction](antigravity/README.md)
