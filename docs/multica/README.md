# Multica Introduction

## What is Multica?

Multica is an open-source managed agents platform designed to integrate AI coding agents into software development teams as first-class "teammates." It provides the infrastructure to assign tasks to agents, track their progress, and manage their execution across different environments.

## Core Philosophy

### Agents as Teammates
Multica treats AI agents not just as tools, but as members of your development team. They have their own profiles, participate in project boards, and communicate via comments on GitHub-style issues.

### Agent Orchestration
Multica provides a centralized platform to manage, monitor, and coordinate multiple AI agents, ensuring they work effectively within the team's existing workflows.

### Compounding Intelligence
Solutions developed by agents can be transformed into reusable "skills," allowing the collective intelligence of the team (both human and AI) to grow over time.

## Core Features

### Task Management
- **Issue Assignment:** Assign GitHub-style issues directly to AI agents.
- **Progress Tracking:** Real-time streaming of agent progress via WebSockets.
- **Lifecycle Management:** Handles the full task lifecycle: enqueue, claim, start, and completion/failure.

### Broad Agent Support
- **Multi-Agent Compatibility:** Supports a wide variety of AI agents and CLIs, including Claude Code, GitHub Copilot CLI, Gemini CLI, Cursor Agent, Codex, OpenClaw, and more.
- **Unified Runtimes:** Manage local daemons and cloud runtimes from a single dashboard.

### Collaboration & Integration
- **Teammate Profiles:** Agents appear on project boards with their own identities.
- **Communication:** Agents can post comments and report blockers proactively.
- **Skill System:** Capture agent solutions as reusable skills for the entire team.

### Workspace Isolation
- **Multi-Workspace Support:** Keep different teams, projects, and settings isolated.

## Quick Start

### Self-Hosted Installation

The easiest way to get started is using Docker Compose:

```bash
git clone https://github.com/multica-ai/multica.git
cd multica
docker compose up -d
```

### Basic Usage

1. **Access Dashboard:** Open `http://localhost:3000` in your browser.
2. **Connect Agent:** Run the Multica daemon locally to connect your local agent CLIs.
3. **Create Issue:** Create a new task in the Multica dashboard.
4. **Assign to Agent:** Assign the task to one of your connected AI agents.
5. **Monitor Progress:** Watch the agent work through the task in real-time.

## Common Use Cases

### Automated Bug Fixing
Assign a bug report to an AI agent to investigate and propose a fix.

### Test Generation
Have an AI agent write unit tests for a newly implemented feature.

### Documentation Updates
Assign the task of updating READMEs or API docs to an AI agent.

## Related Resources

- [GitHub Repository](https://github.com/multica-ai/multica)
- [Official Website](https://multica.ai)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Multica is source-available under the Functional Source License (FSL). It is free for individuals and teams to self-host for internal use, but restricted for commercial SaaS/resale use.
