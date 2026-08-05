# Symphony Introduction

## What is Symphony?

[Symphony](https://github.com/openai/symphony) is an open-source **project-to-delivery harness** from OpenAI. It turns project work into isolated, autonomous implementation runs so that teams can manage *work* instead of supervising coding agents.

Rather than prompting an agent to write code, Symphony monitors a work board (such as Linear), spawns agents to handle tasks, and produces proof-of-work — CI status, PR review feedback, complexity analysis, demo videos — before safely merging the pull request. Engineers stay at the level of goal and review, while the system handles execution.

## Core Positioning

### From Coding Agents to Work Management
Symphony represents a shift from "managing coding agents" to "managing work." The harness is responsible for task lifecycle, context, verification, and delivery, letting human engineers focus on higher-level direction.

### Isolated, Autonomous Runs
Each task runs in an isolated implementation environment. Agents plan, code, test, and report on their own, with checkpoints and verification gates before any change lands.

### Compatibility with Existing Tools
Symphony is designed to work alongside existing coding-agent tools. It does not replace Claude Code, Codex, or Cursor; it orchestrates them around real project workflows.

## Core Features

- **Work-board integration** — monitor task trackers like Linear and automatically start implementation runs.
- **Autonomous PR lifecycle** — generate branches, commits, pull requests, and merge after verification.
- **Proof-of-work** — collect CI status, review feedback, complexity analysis, and demo videos for each change.
- **Human-in-the-loop approval** — engineers review outcomes and decide when to merge.
- **Two implementation paths** — build your own harness from the open specification, or use the experimental Elixir reference implementation.
- **Agent-agnostic** — compatible with existing coding agents and toolchains.

## Quick Start

> **Note:** Symphony is currently in a quiet engineering preview. OpenAI recommends testing only in trusted environments.

### Option A: Use the experimental Elixir reference implementation

```bash
git clone https://github.com/openai/symphony.git
cd symphony
# Follow the Elixir reference implementation setup in the repository
```

### Option B: Build from the open specification

Read the [Symphony specification](https://github.com/openai/symphony) in the repository to implement the harness in your own stack.

## Best Practices

1. **Start with trusted codebases** — preview software should be run on repositories where mistakes are recoverable.
2. **Define clear task boundaries** — well-scoped issues and tickets produce more reliable autonomous runs.
3. **Require CI and review gates** — keep human approval and automated checks enabled before merge.
4. **Monitor agent output** — review proof-of-work artifacts regularly to catch subtle errors early.
5. **Use isolated environments** — run agents in sandboxes or restricted CI environments when possible.

## Security Notice

Symphony can read codebase context, execute tests, open pull requests, and merge code. Grant it only the permissions it needs, use branch-protection rules, and review every merged change.

## Related Resources

- [GitHub Repository](https://github.com/openai/symphony)
- [OpenAI Codex](https://github.com/openai/codex) — a coding agent Symphony can orchestrate
- [Linear](https://linear.app/) — example work board supported by the reference implementation

## License

Symphony is released under the license specified in its [GitHub repository](https://github.com/openai/symphony).
