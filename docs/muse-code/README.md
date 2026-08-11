# Muse Code Introduction

## What is Muse Code?

Muse Code is Meta's beta terminal coding agent, launched on August 5, 2026. It is built around Muse Spark 1.2, a coding-focused model co-trained with the agent harness itself, and is designed to take on complete software engineering tasks across large repositories.

## Core Features

- **Terminal-native workflow**: Install with a single command and work directly in your shell on macOS or Linux.
- **Persistent background agents**: Specialized agents stay alive for the whole session instead of being spawned per task, reducing redundant exploration.
- **Parallel subagents**: Large jobs are fanned out into isolated git worktrees so your working copy is never touched.
- **Append-only event log**: Every model call, tool run, approval, and edit is recorded locally, making sessions replay-exact and restart-safe after crashes.
- **Bundled skills**: Built-in commands such as `/plan`, `/grill`, and `/goal` help structure long-running tasks.
- **Two pricing tiers**:
  - **Standard**: $1.25 / 1M input tokens, $4.25 / 1M output tokens. Prompts and completions are not used to train Meta models.
  - **Contributor**: $0.10 / 1M input tokens, $0.20 / 1M output tokens, in exchange for explicit permission to use your prompts and completions for training.

## Quick Start

Install Muse Code on macOS or Linux:

```bash
curl -fsSL https://dev.meta.ai/install.sh | bash
```

After installation, sign in with a Meta account and add a payment method, then start Muse Code inside your project directory.

## Common Commands

```bash
# Start an interactive session in the current project
muse code

# Create a plan before making changes
/plan

# Stress-test a plan
/grill

# Track completion of a stated objective
/goal <objective>
```

> Note: Muse Code is currently in beta and requires a Meta account with billing details.

## Data and Privacy

The Standard tier keeps prompts and completions out of Meta's training pipeline. The Contributor tier offers significantly lower prices but explicitly allows Meta to train on your data. Choose the tier that matches your project’s privacy requirements.

## Related Resources

- [Official product page](https://www.meta.ai/muse/code)
- [VentureBeat launch coverage](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents)

## License

Muse Code and Muse Spark 1.2 are proprietary Meta services. The terminal agent and model weights are not open source.
