# AI Agent Tools Comparison: Claude Code vs Codex vs Kimi Code vs Grok Build vs Qoder vs Antigravity

This document compares six mainstream AI agent coding tools: Claude Code, Codex, Kimi Code, Grok Build, Qoder, and Google's agent-first IDE Antigravity.

## Quick Comparison

| Aspect | Claude Code | Codex | Kimi Code | Grok Build | Qoder | Antigravity |
|--------|-------------|-------|-----------|------------|-------|-------------|
| Developer | Anthropic | OpenAI | Moonshot AI | xAI | Alibaba Cloud | Google |
| Form Factor | Terminal CLI + IDE plugins + desktop/web/app | Terminal CLI + IDE extensions + desktop app + Codex Web | Terminal CLI + ACP editors + local Web UI | Terminal TUI/CLI + ACP embed + headless mode | Desktop IDE + CLI + Work + Wake + Cloud Agents | Standalone IDE (VS Code fork) + Manager dashboard |
| Open Source | No | Yes (Apache-2.0) | CLI under MIT; core services not open | Yes (Apache-2.0, no external contributions) | No | No (proprietary, free during preview) |
| Default Model | Claude family (Opus / Sonnet / Haiku) | GPT-5.x / Codex family | Kimi Code / Moonshot models | Grok family | Qwen / Bailian models | Gemini 3 Pro / Flash |
| Other Models | — | — | Configurable compatible providers | — | Configurable Bailian models | Claude 5, Claude Sonnet 4.6, Claude Opus 4.6, GPT-OSS-120B |
| Account Required | Anthropic API or Claude account | OpenAI API or ChatGPT account | Kimi account or API key | xAI / X account | Alibaba Cloud account | Google account |
| Multimodal | Text + images | Text + images | Text + images/video | Text + images | Text + images | Text + images + integrated browser |
| Persistent Memory | ✅ Project + user memory | ⚠️ Per-session + cross-device relay sync | ✅ Session / Goal memory | ⚠️ Sessions + checkpoints | ✅ Knowledge engine + adaptive memory | ✅ Cross-run agent learning + project context |
| Multi-Agent | ✅ Subagents + workflows | ✅ Subagents | ✅ Subagents | ✅ Subagents | ✅ Multi-agent collaboration | ✅ Manager view fans out agents |
| Local / Cloud | Local first, `--cloud` optional | Local + Codex Cloud | Local first, `kimi web` local server | Local | Local Desktop/CLI/Work + Cloud Agents | Local IDE |
| Cross-Device | ✅ Remote Control + mobile/web | ✅ ChatGPT relay (mobile/desktop/web) | ✅ `kimi web` same-server access | ❌ | ✅ Remote control + mobile sync | ⚠️ Weak |
| Permission Modes | `--permission-mode` default/plan/auto | `--approval-mode` suggest/auto-edit/full-auto + sandbox | Manual / YOLO / Auto / Plan | Interactive confirm / headless | Confirm / Agent mode | Read Only / Auto / Full Access; plan Artifact approval |
| Extensibility | MCP, Skills, Hooks, Plugins | MCP, Skills, Plugins, Hooks | MCP, Skills, Hooks, ACP | MCP, Skills, Plugins, Hooks, sandbox | MCP, built-in tools, IDE plugins | VS Code extensions, integrated browser/terminal |

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

**Grok Build**
- Full-screen TUI for understanding codebases, searching, editing, and running commands
- Workspace checkpoints preserve session state
- Designed for long-running terminal-based tasks

**Qoder**
- Deep codebase analysis + adaptive memory and knowledge engine
- Multi-agent collaboration with role splitting (planning, coding, testing, review)
- Goal-driven closed loop: plan → execute → verify → iterate

**Antigravity**
- Agent-first workflow: plan → edit → run → verify carries context across steps
- Agents learn from prior runs, including corrections you apply
- Project context anchored inside the workspace; integrated browser feeds runtime context back to the agent

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

**Grok Build**
- Step-by-step confirmation in interactive TUI; headless mode for CI/scripts
- Built-in sandbox and workspace checkpoints
- Files and commands run locally

**Qoder**
- Key actions require user confirmation before Agent mode proceeds
- Local Desktop/CLI/Work separated from Cloud Agents
- Enterprise supports private/cloud-compliant deployment

**Antigravity**
- Agents draft a **plan Artifact** before acting; you approve before execution
- Browser recordings and screenshots make agent behavior auditable after the fact
- Runs inside the IDE with workspace-scoped access

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

**Grok Build**
- MCP, Skills, Plugins, Hooks
- ACP editor embedding and headless mode
- Themes, configuration, and checkpoints are customizable

**Qoder**
- MCP, built-in programming tools, IDE plugins
- Product family: Desktop / CLI / Work / Wake / Cloud Agents
- Remote control and mobile app sync

**Antigravity**
- Built on VS Code, so the existing extension ecosystem applies
- Built-in browser the agent can drive (clicks, navigation, screenshots)
- Multi-model selector (Gemini, Claude, GPT-OSS) inside one IDE

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

**Grok Build**
- Currently focused on single-machine terminal use
- No official cross-device sync or mobile app

**Qoder**
- Qoder web version can remotely control local tasks
- Mobile app syncs with Desktop/CLI in real time
- Cloud Agents keep running after you close your computer

**Antigravity**
- Primarily a local IDE experience
- Cross-device continuity is limited; no mobile session continuation

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

### Choose Grok Build if you need:
- An open-source, Rust-based high-performance terminal TUI agent
- Full-screen mouse interaction, checkpoints, and headless mode
- Deep integration with the xAI / Grok model ecosystem

### Choose Qoder if you need:
- A full product family covering Desktop / CLI / Work / Wake / Cloud Agents
- Multi-agent collaboration + knowledge engine + remote control
- Alibaba Cloud ecosystem and domestic compliance deployment

### Choose Antigravity if you need:
- An agent-first IDE rather than a pure terminal tool
- **Verifiable** agent runs via Artifacts (plans, screenshots, recordings)
- An integrated browser the agent can drive to test what it built
- Flexible model switching between Gemini / Claude / GPT-OSS

## Combined Usage

These tools are not mutually exclusive. Common splits:

- **Daily terminal development**: Claude Code, Codex, Kimi Code, Grok Build
- **Domestic ecosystem / full product family**: Qoder
- **Browser verification / IDE-style experience**: Antigravity
- **Quick single-file edits**: Codex, Grok Build
- **Long-horizon multi-file refactors**: Claude Code, Qoder, Antigravity
- **Continue tasks across devices**: Claude Code (Remote Control), Codex (ChatGPT relay), Kimi Code (`kimi web`), Qoder (remote control)

## Related Links

- [Claude Code Introduction](claude-code/README.md)
- [Codex Introduction](codex/README.md)
- [Kimi Code Introduction](kimi-code/README.md)
- [Grok Build Introduction](grok-build/README.md)
- [Qoder Introduction](qoder/README.md)
- [Antigravity Introduction](antigravity/README.md)
