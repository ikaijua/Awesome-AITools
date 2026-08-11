# TencentDB Agent Memory Introduction

## What is TencentDB Agent Memory?

[TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) is an open-source memory infrastructure for AI agent teams from Tencent Cloud. It addresses a practical problem: reducing repetitive work when using agents by letting experience accumulate, flow, and pass on to the next agent.

Instead of treating memory as simple conversation history, it converts useful information into reusable memory assets—chat memories, skills, wikis, and code graphs—so new sessions and new agents can start from existing experience rather than from scratch.

## Core Concepts

### Memory Hub for Agent Teams
Memory Hub closes the loop across the agent experience lifecycle:

- **Automatic asset extraction** — extracts Chat Memory and Skills from conversations and tasks; converts documents and code into Wiki and CodeGraph.
- **Portable & multi-agent compatible** — memory assets are decoupled from any single agent framework, so they can move across frameworks and be shared among agents and team members.
- **Cold-start friendly** — import existing documents, codebases, and past agent sessions so new teams start from accumulated experience.

### A Brain That Remembers People and Context
- **Chat Memory** retains preferences, facts, decisions, and interaction history.
- Each agent automatically gets its own memory when created.
- Raw conversations are distilled through four layers: L0 Conversation → L1 Atom → L2 Scenario → L3 Persona.

### A Skill Library That Accumulates Expertise
- After complex work, agents can extract reusable Skills from conversations and tool calls.
- A Skill is more than a prompt snippet: it has versions, resource files, trigger boundaries, execution steps, and validation rules.
- Personal Skills are private by default; after review they can be shared with the team.

### A Knowledge Map That Reads Docs and Code
- **Wiki** turns product docs, design specs, and ops runbooks into structured pages with a link graph.
- **CodeGraph** indexes codebases so agents can navigate and reason about projects without re-reading every file.

## Core Features

- **Cross-session memory** — retain context across separate agent sessions.
- **Cross-agent sharing** — memory assets can be reused by different agents and frameworks.
- **Skill extraction & versioning** — turn repeated workflows into versioned, reusable skills.
- **Document & code indexing** — build Wiki and CodeGraph from existing knowledge.
- **Local-first deployment** — self-host memory-core, memory-hub, and proxy services.
- **IDE/Agent integration** — works with Claude Code, CodeBuddy, and other agents via the proxy.

## Quick Start

### Prerequisites
- Docker and Docker Compose (recommended)
- Two sets of LLM API credentials: one for the memory group and one for the proxy group

### Run locally with one command

```bash
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images
cp .env.example .env
# Edit .env to fill in your LLM parameters
./start-all.sh
```

When finished, the script prints a one-liner you can paste into Claude Code or CodeBuddy.

Open the web panel at http://localhost:8125.

For standalone deployment, proxy-only setup, or migration from older versions, see `INSTALL.md` (English) or `INSTALL_CN.md` (Chinese) in the upstream repository.
