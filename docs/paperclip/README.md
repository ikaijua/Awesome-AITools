# Paperclip Introduction

## What is Paperclip?

Paperclip is an open-source AI agent orchestration platform that models your AI operations as a company. Instead of managing a pile of disconnected scripts and terminal tabs, you define an org chart with roles, reporting lines, budgets, and governance policies, then let your agents work autonomously within that structure.

Created by @dotta and launched in March 2026, Paperclip crossed 30,000 GitHub stars within three weeks, making it one of the fastest-growing open-source agent projects of the year.

## Core Philosophy

### Agents as a Company
Most multi-agent frameworks ask you to think about agents as pipelines: nodes in a graph, workers in a queue. Paperclip takes a different angle. Your agents are a company. There is a CEO agent that receives goals and delegates, Engineers that execute tasks, and QA agents that review outputs. The coordination happens through projects and issues, just like a real development team.

### Governance by Default
Every agent has a role, a budget, and a manager. Actions are bounded by governance policies. You get audit trails, cost tracking, and state recovery out of the box.

### Heartbeat Execution
Agents are not always-on processes. They wake up on a schedule, check for work, execute actions, and report back. Delegation flows up and down the org chart. This makes costs predictable and behavior observable.

## Core Features

### Organizational Structure
- **Org Charts:** Define reporting structures and authority levels.
- **Role-Based Agents:** CEO, CTO, Engineer, QA, Researcher — each with clear responsibilities.
- **Goal Alignment:** Every task traces back to a company mission. Agents know not just what to do, but why.

### Budget & Cost Control
- **Per-Agent Budgets:** Set monthly spending limits per agent or team.
- **Automatic Throttling:** Agents stop when they hit budget caps. No runaway token consumption.
- **Cost Analytics:** Track API costs across the entire organization.

### Multi-Agent Coordination
- **Inter-Agent Communication:** Structured messaging between agents.
- **Manager Agents:** Supervisory agents that review and approve sub-agent work.
- **Shared Context:** Agents understand what others are doing to avoid duplicate work.

### Broad Agent Backend Support
- **Supported Runtimes:** OpenClaw, Claude Code, Codex, and custom agents.
- **Extensible Architecture:** Bring your own agent implementation.

## Quick Start

### Self-Hosted Installation

```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
docker compose up -d
```

### Basic Usage

1. **Access Dashboard:** Open the web UI in your browser.
2. **Define Company:** Create an org chart with roles and reporting lines.
3. **Set Budgets:** Assign monthly budgets to each agent or team.
4. **Create Goal:** Define a high-level company goal.
5. **Let Agents Work:** The CEO agent decomposes the goal and delegates to sub-agents.

## Common Use Cases

### Automated Software Development
Set up an AI company with a CTO agent, multiple Engineer agents, and a QA agent. Assign a product goal and let them design, implement, test, and review code autonomously.

### Research & Analysis Teams
Deploy a Research Director agent with specialized researcher agents. They divide topics, gather information, cross-check findings, and compile reports.

### Content Production Pipelines
Create a content team with Writer agents, Editor agents, and SEO agents. They collaborate on drafts, revisions, and publication-ready content.

## Comparison with Similar Tools

| Tool | Focus | Key Difference |
|------|-------|----------------|
| **Paperclip** | AI agents as a company | Org charts, budgets, governance, heartbeat execution |
| **Multica** | AI agents as teammates | Task assignment, progress tracking, skill reuse |
| **OpenClaw** | Single autonomous agent | Depth: memory, planning, messaging platforms |
| **LangGraph** | Agent workflow graphs | Code-level DAG orchestration |

## Related Resources

- [GitHub Repository](https://github.com/paperclipai/paperclip)
- [Official Website](https://paperclip.ing)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Paperclip is open-source under the MIT License.
