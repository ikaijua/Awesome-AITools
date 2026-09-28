# AX

[AX](https://github.com/google/ax) is Google's open-source agentic orchestration runtime — positioned as "the Kubernetes for agents". Created on 2026-03-30, it has grown to 12.2k+ stars and is under active development; the README warns that breaking changes are expected before a stable release.

## What it does

- Lets you define agent workloads with declarative YAML manifests instead of imperative code.
- Runs each agent task inside a sandbox with resource isolation and CPU/memory limits.
- Provides lifecycle controls such as `ax suspend/resume` to pause and resume long-running tasks, and `ax ssh` to drop into a sandbox for debugging.

## Core abstractions

- **Workspace**: a pre-packaged environment (Git repos, MCP servers, skill packs) that tasks run against.
- **Task**: an agent task executed inside a sandbox, with configurable CPU/memory limits.
- **Model**: the LLM configuration used by the platform itself.

## Architecture

AX runs on top of Google's **Agent Substrate** and is designed around a single cluster that targets billions of autonomous agent workloads.

## Quick start

Install the `ax` CLI and follow the getting-started guide in the official repository README: <https://github.com/google/ax>.

## Links

- [GitHub repository](https://github.com/google/ax)
