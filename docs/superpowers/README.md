# Superpowers Introduction

## What is Superpowers?

Superpowers is a complete software development methodology for coding agents, built on top of a set of composable skills and session-start instructions. Created by Jesse Vincent and the team at Prime Radiant, it turns agents such as Claude Code, Codex, Cursor, Kimi Code, OpenCode, Antigravity, GitHub Copilot CLI, and Pi into systematic engineering partners.

Instead of jumping straight into code, a Superpowers-enabled agent first refines a spec with you, gets your approval, writes a detailed implementation plan, and then executes through test-driven, review-driven workflows. The skills trigger automatically, so the agent "just has Superpowers" without manual prompting.

## Core Philosophy

### Spec Before Code
Every task starts by understanding what you are really trying to build. The agent asks clarifying questions, explores alternatives, and presents the design in short, reviewable chunks.

### Test-Driven Development (TDD)
Superpowers enforces a strict RED-GREEN-REFACTOR cycle: write a failing test first, watch it fail, write the minimal code to make it pass, then refactor. Code written before tests is deleted.

### Systematic Over Ad Hoc
Processes such as debugging, planning, and code review are handled through structured skills rather than improvisation. The goal is evidence over claims.

### Subagent-Driven Development
Once a plan is approved, the agent dispatches subagents to work through tasks, inspects their output, runs two-stage reviews (spec compliance, then code quality), and continues autonomously for extended periods.

## Core Skills

| Skill | Purpose |
| --- | --- |
| `brainstorming` | Refine rough ideas through Socratic questioning and present designs in sections for validation. |
| `writing-plans` | Break approved designs into small, actionable tasks with exact file paths and verification steps. |
| `using-git-worktrees` | Create isolated branches, run project setup, and verify a clean test baseline. |
| `subagent-driven-development` / `executing-plans` | Execute tasks via subagents or batch execution with human checkpoints. |
| `test-driven-development` | Enforce RED-GREEN-REFACTOR and testing anti-pattern awareness. |
| `systematic-debugging` | 4-phase root-cause analysis with tracing and verification-before-completion. |
| `requesting-code-review` | Review work against the plan and report issues by severity. |
| `finishing-a-development-branch` | Verify tests, present merge/PR/keep/discard options, and clean up worktrees. |
| `writing-skills` | Create new skills following the project's best practices. |

## Supported Harnesses

Superpowers installs as a plugin or package for:

- Claude Code
- Antigravity
- Codex App / Codex CLI
- Cursor
- Factory Droid
- GitHub Copilot CLI
- Kimi Code
- OpenCode
- Pi

## Quick Start

### Kimi Code

```bash
/plugins install https://github.com/obra/superpowers
```

Or install from Kimi Code's plugin marketplace.

### Claude Code

```bash
/plugin install superpowers@claude-plugins-official
```

For other harnesses, see the [installation section](https://github.com/obra/superpowers#installation) in the repository.

## Basic Workflow

1. **Brainstorm** — refine the goal and produce a design document.
2. **Approve design** — review short sections and sign off.
3. **Plan** — generate a task-level implementation plan.
4. **Execute** — run tasks via subagents or checkpoints.
5. **Review** — check spec compliance and code quality between tasks.
6. **Finish** — verify tests and decide whether to merge, PR, keep, or discard.

## Best Practices

1. **Start with a clear goal** — the better the initial problem statement, the better the spec.
2. **Review design chunks** — do not skip the approval checkpoints; they keep the agent aligned.
3. **Let the tests lead** — resist the urge to write implementation before a failing test.
4. **Use worktrees** — they keep experimental work isolated from your main branch.
5. **Inspect subagent output** — critical review issues block progress for a reason.

## Related Resources

- [GitHub Repository](https://github.com/obra/superpowers)
- [Release Announcement](https://primeradiant.com/superpowers/)
- [Issues](https://github.com/obra/superpowers/issues)
- [Community Discord](https://discord.gg/superpowers)

## License

Superpowers is open-source under the MIT License.
