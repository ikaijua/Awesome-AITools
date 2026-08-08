# Conductor Introduction

## What is Conductor?

[Conductor](https://github.com/conductor-oss/conductor) is an open-source, event-driven **agentic workflow engine** originally built at Netflix and now actively maintained by Orkes and the open-source community. It provides a durable, highly resilient execution engine for orchestrating microservices, AI agents, and long-running workflows at internet scale.

Conductor separates orchestration from business logic: the workflow graph is declarative and deterministic by construction, while workers are plain code in any language. This makes it well suited for AI agent loops that need to survive crashes, retries, and human-in-the-loop approvals without losing state.

## Core Positioning

### From Microservices Orchestration to AI Agent Engine

Conductor started as Netflix's workflow engine for microservices orchestration. With the rise of agentic AI, it has evolved into a durable execution platform for AI agents, adding native LLM task types, MCP tool calling, function calling, vector database support for RAG, and human approval gates.

### Durable by Design

Every workflow step is persisted. Executions can survive server restarts, network failures, and long pauses (days, weeks, or months) waiting for external signals or human approvals. Failed steps can be retried individually without replaying the entire workflow.

### Polyglot, Decoupled Workers

Workers poll the Conductor server, execute tasks, and report results. They can be written in Java, Python, Go, JavaScript, C#, Ruby, or Rust, with no framework constraints on business logic.

## Core Features

- **Durable execution** — persisted state with configurable retries, timeouts, and compensation.
- **AI agent orchestration** — native task types for 14+ LLM providers, MCP tool calling, function calling, and vector DB integration for RAG.
- **Declarative workflows** — JSON/YAML workflow definitions that are versioned, observable, and debuggable in the built-in UI.
- **Dynamic runtime behavior** — dynamic forks, sub-workflows, and tasks resolved at runtime; LLMs can generate workflows that Conductor executes immediately.
- **Full replayability** — restart from the beginning, rerun from any task, or retry only the failed step.
- **Human-in-the-loop** — built-in approval tasks and wait-for-signal support.
- **Self-hosted, no lock-in** — Apache 2.0, with 5 persistence backends and 6 message brokers.

## Quick Start

### Run locally with the official CLI

Prerequisites: Node.js v16+ and Java 21+.

```bash
npm install -g @conductor-oss/conductor-cli
conductor server start
```

Open http://localhost:8080 for the built-in UI.

### Run with Docker

```bash
docker run -p 5000:5000 -p 8080:8080 conductoross/conductor:next
```

UI at http://localhost:5000, API at http://localhost:8080.

### Define and run your first workflow

```bash
curl -s https://raw.githubusercontent.com/conductor-oss/conductor/main/docs/quickstart/workflow.json -o workflow.json
conductor workflow create workflow.json
conductor workflow start -w hello_workflow --sync
```

## Best Practices

1. **Keep workers stateless** — let Conductor own state and orchestration; workers should be idempotent.
2. **Use versioned workflow definitions** — deploy new versions without breaking in-flight executions.
3. **Set meaningful retries and timeouts** — Conductor can retry failed tasks, but configure policies that match your downstream behavior.
4. **Enable observability** — use the built-in UI to inspect inputs, outputs, timing, and retry history.
5. **Scope worker permissions** — grant workers only the credentials they need; keep sensitive operations behind approval tasks.

## Security Notice

Conductor can execute arbitrary worker code, call external APIs via MCP, and read/write vector databases. Run workers in isolated environments, restrict network access, and require human approval for destructive or high-risk operations.

## Related Resources

- [GitHub Repository](https://github.com/conductor-oss/conductor)
- [Documentation](https://conductor-oss.github.io/conductor/)
- [Conductor Skills for AI Coding Assistants](https://github.com/conductor-oss/conductor-skills)

## License

Conductor is licensed under the Apache 2.0 License.
