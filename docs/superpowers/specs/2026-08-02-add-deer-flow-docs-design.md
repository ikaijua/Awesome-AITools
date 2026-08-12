# Design: Add DeerFlow Deep-Dive Docs

## Goal
Improve the existing `deer-flow` entry in Awesome-AITools by adding bilingual deep-dive docs under `docs/deer-flow/` and linking them from both READMEs, while also refreshing the table description to match the project's official positioning.

## Background
- `deer-flow` is already listed in the **AI Agent** section of `README.md` and `README-CN.md`.
- The current description is generic: "A framework for building high-performance AI agents, developed by ByteDance..."
- The official GitHub tagline is: "An open-source long-horizon SuperAgent harness that researches, codes, and creates."
- No `docs/deer-flow/` directory exists yet.

## Changes

### New files
1. `docs/deer-flow/README.md`
   - What is DeerFlow?
   - Core positioning (SuperAgent harness, sub-agents, memory, sandbox, skills, MCP, IM channels)
   - Key features summary
   - Quick Start (clone + `make setup` / Docker)
   - Best practices / security note
   - Related resources
2. `docs/deer-flow/README-CN.md`
   - Chinese mirror of the above.

### Modified files
1. `README.md` AI Agent table row for `deer-flow`:
   - Replace short description with a concise SuperAgent-harness summary.
   - Append `[Intro](docs/deer-flow/README.md)`.
2. `README-CN.md` AI Agent table row for `deer-flow`:
   - Replace short description with Chinese SuperAgent-harness summary.
   - Append `[入门介绍](docs/deer-flow/README-CN.md)`.

### Not changed
- `CHANGELOG.md`: this is a description/docs enhancement for an already-listed tool, not an addition/removal/rename, so no changelog entry is required per `AGENTS.md`.

## Verification
- Run `python3 scripts/format_readmes.py` to normalize table formatting.
- Run `lychee .` (if available) to confirm new `docs/deer-flow/` links are valid.
