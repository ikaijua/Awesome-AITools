# Add Codex Security to Awesome-AITools

## Goal

Add OpenAI's open-source `codex-security` project to the Awesome-AITools list, keeping the English and Chinese READMEs in sync.

## Background

- Repository: https://github.com/openai/codex-security
- License: Apache 2.0
- Description: CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in code.
- Key features: repo scanning, finding tracking, fix verification, CI/CD integration, containerized bulk scans, TypeScript SDK.

The project is a good fit for this curated bilingual list of AI tools.

## Placement

Add Codex Security to the `### AI Coding` section in both `README.md` and `README-CN.md`, because it is a code-focused security scanning tool.

## Changes

1. **README.md**
   - Add one row to the `### AI Coding` table.
   - Link to the GitHub repo.
   - Mark fee as `Free` (the CLI/SDK is open source).

2. **README-CN.md**
   - Add the corresponding Chinese row to the `### AI Coding` table.
   - Use the standard Chinese column headers and phrasing.

3. **docs/codex-security/**
   - Create `README.md` and `README-CN.md` with a brief introduction, quick-start commands, and key features.
   - Link the README entries to these docs using `[Intro](docs/codex-security/README.md)` / `[入门介绍](docs/codex-security/README-CN.md)`.

4. **CHANGELOG.md**
   - Add an entry under the latest month: "Added Codex Security to AI Coding section (EN/CN)".

5. **Formatting**
   - Run `python3 scripts/format_readmes.py` to normalize table formatting.

## Verification

- Both READMEs contain the new row in the AI Coding section.
- Both docs pages exist and are linked.
- CHANGELOG has a new entry.
- `python3 scripts/format_readmes.py` completes without errors.
