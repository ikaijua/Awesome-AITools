# AI Agent Tools Comparison: Claude Code vs Codex vs Kimi Code

This document compares three mainstream AI agent coding tools: Claude Code, Codex, and Kimi Code.

## Quick Comparison

| Aspect | Claude Code | Codex | Kimi Code |
|--------|-------------|-------|-----------|
| Developer | Anthropic | OpenAI | Moonshot AI |
| Form Factor | Terminal CLI + IDE plugins + desktop/web/app | Terminal CLI + IDE extensions + desktop app + Codex Web | Terminal CLI + ACP editors + local Web UI |
| Open Source | No | Yes (Apache-2.0) | CLI under MIT; core services not open |
| Default Model | Claude family (Opus / Sonnet / Haiku) | GPT-5.x / Codex family | Kimi Code / Moonshot models |
| Other Models | — | — | Configurable compatible providers |
| Account Required | Anthropic API or Claude account | OpenAI API or ChatGPT account | Kimi account or API key |
| Multimodal | Text + images | Text + images | Text + images/video |
| Persistent Memory | ✅ Project + user memory | ⚠️ Per-session + cross-device relay sync | ✅ Session / Goal memory |
| Multi-Agent | ✅ Subagents + workflows | ✅ Subagents | ✅ Subagents |
| Local / Cloud | Local first, `--cloud` optional | Local + Codex Cloud | Local first, `kimi web` local server |
| Cross-Device | ✅ Remote Control + mobile/web | ✅ ChatGPT relay (mobile/desktop/web) | ✅ `kimi web` same-server access |
| Permission Modes | `--permission-mode` default/plan/auto | `--approval-mode` suggest/auto-edit/full-auto + sandbox | Manual / YOLO / Auto / Plan |
| Extensibility | MCP, Skills, Hooks, Plugins | MCP, Skills, Plugins, Hooks | MCP, Skills, Hooks, ACP |

## Detailed Comparison

### Code Understanding & Context Memory

**Claude Code**
- Long context with deep multi-file understanding
- Persistent memory across sessions (user + project)
- Project rules via `CLAUDE.md` / `AGENTS.md`

**Codex**
- Local repository-level understanding and multi-step execution
- Session state syncs across devices via the ChatGPT relay
- Relies on `AGENTS.md` and project prompts for long-term context

**Kimi Code**
- Analyzes project structure, dependencies, and implementation details in the terminal
- Goal mode lets long tasks progress across multiple turns
- Uses `AGENTS.md` and project-local memory for consistency

### Safety and Control

**Claude Code**
- Dangerous operations (deleting files, force pushing, etc.) require confirmation by default
- `--permission-mode` offers default / plan / auto
- `--dangerously-skip-permissions` for trusted scenarios

**Codex**
- Approval modes `suggest` / `auto-edit` / `full-auto` control automation
- Sandbox modes `read-only` / `workspace-write` / `danger-full-access` control access scope
- Kernel-level sandbox + ChatGPT relay; no inbound ports exposed

**Kimi Code**
- Manual / YOLO / Auto / Plan permission modes
- `kimi web` starts a local server; files stay on the machine
- Sensitive operations require confirmation by default

### Extension and Integration

**Claude Code**
- MCP servers connect databases, browsers, external APIs
- Skills / Hooks / Plugins for reusable workflows
- Deep Git / GitHub / GitLab / CI/CD integration

**Codex**
- MCP, Skills, Plugins, Hooks
- `codex exec` fits scripts and CI
- Shared account and sessions with ChatGPT ecosystem

**Kimi Code**
- MCP, Skills, Hooks
- ACP editor integration (Zed, JetBrains, etc.)
- `kimi web` provides a local browser UI

### Cross-Device and Collaboration

**Claude Code**
- `claude remote-control` / `/remote-control` lets you continue local sessions from phone or browser
- `claude --cloud` starts tasks resumable on mobile
- Files and credentials stay on the local machine

**Codex**
- ChatGPT mobile app connects to local/remote Codex sessions
- ChatGPT relay syncs active sessions across phone, desktop, and web
- Remote SSH connects to remote environments

**Kimi Code**
- `kimi web` starts a local server accessible on the local network
- Multiple devices can follow task progress under the same server
- Goal status visible in the Web UI

## Recommendations

### Choose Claude Code if you need:
- Deep understanding and refactoring of large, mature codebases
- Strong project memory plus Skills/Hooks for long-running workflows
- Remote Control to continue local sessions from phone or web
- A mature permission model and broad tool integrations

### Choose Codex if you need:
- An open-source (Apache-2.0) terminal agent you can inspect and customize
- Tight cross-device integration with ChatGPT account/mobile app
- Kernel-level sandbox + approval modes balancing safety and automation
- Cloud tasks (Codex Cloud) and Remote SSH support

### Choose Kimi Code if you need:
- A terminal-native agent plus a local Web UI (`kimi web`)
- Goal mode for autonomous long-horizon tasks
- ACP editor integration and a domestic model/network environment

## Combined Usage

These tools are not mutually exclusive. Common splits:

- **Daily terminal development**: Claude Code, Codex, Kimi Code
- **Quick single-file edits**: Codex, Claude Code
- **Long-horizon multi-file refactors**: Claude Code, Kimi Code
- **Continue tasks across devices**: Claude Code (Remote Control), Codex (ChatGPT relay), Kimi Code (`kimi web`)

## Related Links

- [Claude Code Introduction](claude-code/README.md)
- [Codex Introduction](codex/README.md)
- [Kimi Code Introduction](kimi-code/README.md)
