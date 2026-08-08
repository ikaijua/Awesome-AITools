# Agency Agents Introduction

## What is Agency Agents?

[Agency Agents](https://github.com/msitarzewski/agency-agents) is an open-source collection of **230+ specialized AI agent personas** organized as a complete digital agency. Each agent is a domain specialist with a distinct personality, workflow, deliverables, and success metrics — covering engineering, design, marketing, sales, finance, game development, healthcare, and more.

The project also ships a **native desktop app** ([agencyagents.app](https://agencyagents.app/)) for macOS, Linux, and Windows that lets you browse the full roster and install agents into Claude Code, Cursor, Codex, Gemini, Kimi Code, Aider, Windsurf, and other AI coding tools with one click.

## Core Positioning

### A Specialist for Every Task
Instead of generic "act as a developer" prompts, Agency Agents provides deep, role-specific personas — from Frontend Developer and Backend Architect to Reddit Community Builder, FinOps Engineer, and Clinical Evidence Agent. Each persona includes identity, memory, mission, rules, deliverables, and workflow.

### Native Desktop App
The desktop app removes the need to clone repositories or run install scripts manually. It auto-detects supported tools, installs the selected agents, and keeps them up to date.

### Multi-Tool Support
Agents are provided in formats compatible with the major agentic coding platforms, including Claude Code, GitHub Copilot, Cursor, Aider, Windsurf, Codex, Gemini CLI, Kimi Code, OpenCode, Antigravity, Osaurus, and more.

## Core Features

- **230+ specialized agents** across 15+ divisions (Engineering, Design, Marketing, Sales, Product, Testing, Security, Finance, Game Development, GIS, Healthcare, etc.).
- **Personality-driven** — each agent has a unique voice, communication style, and approach.
- **Deliverable-focused** — concrete outputs such as code, documents, audits, plans, and reports.
- **Workflow templates** — step-by-step processes with success metrics and quality gates.
- **Native desktop app** — browse, install, and update agents across multiple tools.
- **Open and forkable** — transparent Markdown-based agent files you can adapt for your own workflows.

## Quick Start

### Option 1: Desktop App (Recommended)

Download the native app from [agencyagents.app](https://agencyagents.app/) or install via Homebrew on macOS:

```bash
brew install --cask msitarzewski/agency-agents/agency-agents
```

Then select your tools and divisions, and the app installs the agents for you.

### Option 2: Manual Install for Claude Code

```bash
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
./scripts/install.sh --tool claude-code
```

Or copy a specific division:

```bash
cp engineering/*.md ~/.claude/agents/
```

### Option 3: Convert for Multiple Tools

```bash
./scripts/convert.sh
./scripts/install.sh
```

The installer auto-detects supported tools and installs the matching formats.

## Best Practices

1. **Start with a clear role** — activate the most specific agent for your task rather than a general one.
2. **Pick a division, not the whole roster** — installing every agent can overwhelm tool menus; choose the teams you actually need.
3. **Review deliverables up front** — each agent lists expected outputs; use them to frame your request.
4. **Combine agents for projects** — use multiple personas in sequence or in parallel for cross-functional work.
5. **Keep the desktop app updated** — it auto-syncs new agents and format changes for supported tools.

## Related Resources

- [GitHub Repository](https://github.com/msitarzewski/agency-agents)
- [Desktop App](https://agencyagents.app/)
- [Agent Roster](https://github.com/msitarzewski/agency-agents#-the-agency-roster)

## License

See the [LICENSE](https://github.com/msitarzewski/agency-agents/blob/main/LICENSE) file in the repository for details.
