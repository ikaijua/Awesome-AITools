# Dify Introduction

## What is Dify?

[Dify](https://github.com/langgenius/dify) is an open-source LLM application development platform. It combines a visual app builder, RAG pipeline, agentic workflow engine, model orchestration, and observability in one place, so teams can go from prototype to production AI applications faster.

## Core Positioning

### Visual LLM App Builder
Dify provides a drag-and-drop interface for designing chatbots, agents, and complex workflows without writing boilerplate code. Prompt versioning, structured outputs, and multi-turn conversation management are built in.

### RAG and Knowledge Base
Upload documents, websites, or structured data to build retrieval-augmented generation apps. Dify handles chunking, embedding, vector storage, and reranking, with configurable retrieval strategies.

### Agent and Workflow Orchestration
Create multi-step workflows and autonomous agents that can use tools, call APIs, make decisions, and loop until a task is complete. Dify supports conditional branching, loops, and human-in-the-loop approvals.

### Model Orchestration
Connect to OpenAI, Anthropic, Gemini, DeepSeek, local models via Ollama, and many other providers through a unified interface. Switch models or route by task without rewriting application logic.

### Observability and Operations
Built-in logs, tracing, annotation, and evaluation tools help teams monitor production usage, debug failures, and continuously improve prompts and retrieval quality.

## Quick Start

### Self-host with Docker

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
```

Open `http://localhost` for the default web UI.

### Managed cloud

Sign up at [dify.ai](https://dify.ai/) for the hosted version.

## Related Resources

- [GitHub Repository](https://github.com/langgenius/dify)
- [Official Documentation](https://docs.dify.ai/)
- [Website](https://dify.ai/)

## License

Dify is licensed under the Apache 2.0 License.
