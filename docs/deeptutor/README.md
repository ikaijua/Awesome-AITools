# DeepTutor Introduction

## What is DeepTutor?

DeepTutor is an **agent-native learning workspace** open-sourced by HKUDS (The University of Hong Kong Data Science Institute). It connects AI tutoring, problem solving, quiz generation, research, visualization, and mastery practice in one extensible system, running every mode on the same agent loop so context follows the learner across workflows.

## Key Capabilities

- **Chat, Quiz, Solve, and Research** — switch the objective instead of the engine; the same agent loop handles tutoring conversations, quiz generation, step-by-step problem solving, and deep research.
- **Visualize and Mastery Path** — turn concepts into interactive visualizations and follow structured learning paths with mastery gates.
- **Partners and My Agents** — consult live coding CLIs (Claude Code, Codex, Gemini CLI, Kimi Code, opencode, MiMo) or custom Partner agents from any turn.
- **Connected learning context** — knowledge bases, books, Co-Writer drafts, notebooks, question banks, personas, and Memory are shared across every workflow instead of living in isolated tools.

## Knowledge Bases and RAG

DeepTutor supports multiple retrieval engines and document parsers:

- **Multi-engine RAG** — choose from LlamaIndex, PageIndex, GraphRAG, LightRAG, or a linked Obsidian vault.
- **Pluggable document parsing** — ingest PDF, DOCX, XLSX, PPTX, and other formats with parsing backends like MinerU, Docling, or PyMuPDF4LLM.
- **Versioned indexes** — knowledge-base indexes are versioned and can be re-built without losing prior snapshots.

## Installation

Four deployment shapes are supported:

1. **PyPI** — `pip install deeptutor && deeptutor init && deeptutor start`
2. **Source** — clone the repo, install Python deps and Next.js frontend, then `deeptutor start`
3. **Docker** — run the pre-built image from `ghcr.io/hkuds/deeptutor:latest`
4. **CLI-only** — install `packaging/deeptutor-cli` for terminal use without the web UI

See the [GitHub repository](https://github.com/HKUDS/DeepTutor) for detailed instructions, provider setup, and Docker compose examples.

## Typical Use Cases

- **Self-paced learning** — upload a textbook or paper, ask questions, generate quizzes, and track mastery.
- **Research assistant** — build a knowledge base from arXiv papers and run agentic deep research with traceable citations.
- **Programming tutor** — connect a coding CLI Partner to walk through code, debug, and explain algorithms interactively.
- **Course authoring** — use the Book engine and Co-Writer to compile living course materials with embedded quizzes and visualizations.
