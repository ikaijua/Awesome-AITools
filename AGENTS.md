# AGENTS.md for Awesome-AITools

This file provides context and instructions for AI coding agents (e.g., Cursor, Aider, Claude Code, Windsurf) to help them understand this repository more effectively. It follows the [AGENTS.md](https://agents.md/) standard.

## Repository Purpose

A curated, bilingual (EN/CN) "awesome list" of AI tools — chatbots, agents, skills, CLI tools, and more. There is no application code; the repository's product is the two README files and their supporting `docs/` deep-dives.

## Key Files & Directories

- `README.md` — Main tool list (English).
- `README-CN.md` — Main tool list (Chinese).
- `docs/<tool-slug>/` — Longer-form intros for individual tools.
- `CHANGELOG.md` — Monthly log (e.g. `## June 2026`) of additions/removals/renames.
- `scripts/format_readmes.py` — Maintenance/normalization script.

## Architecture

The repo is structured as two parallel, mirrored documents that must stay in sync:

- `README.md` and `README-CN.md` share the same category structure, the same set of tools, and the same 4-column table schema:
  - English: `| Name | Description | Links | Fees |`
  - Chinese: `| 名称 | 说明 | 链接 | 费用 |`
- README entries with a deep-dive link to `docs/<slug>/` via `[Intro](docs/<slug>/...)` (EN) and `[入门介绍](docs/<slug>/...)` (CN).

When adding/removing/editing a tool, the change almost always touches **both** READMEs (and often `CHANGELOG.md` and a `docs/` page). A change in only one language is a bug.

## Commands

- Format/normalize both READMEs: `python3 scripts/format_readmes.py` (run from anywhere — the script resolves the project root itself). This rewrites tables to the canonical 4-column form, strips ` `, converts `</br>` → `<br>`, dedents tabs, and fixes a couple of known broken TOC anchors. Run it after any table edit.
- Local link check (requires [lychee](https://github.com/lycheeverse/lychee) installed): `lychee .` — mirrors the CI workflow at `.github/workflows/link-check.yml`. `.lycheeignore` holds the exclusion list.

There is no build, test, or lint suite beyond the above — CI only runs link checking on `**/*.md`.

## Editing Conventions

- When adding a new tool, follow the existing table format in both READMEs.
- Table format is strict: exactly 4 columns, with the separator row `| --- | --- | --- | --- |`. `format_readmes.py` will rewrite divergent separators, so don't hand-craft 3- or 5-column variants.
- The TOC at the top of each README lists category anchors. The formatter knows about two specific anchor-typo fixes (`#news-information` in EN, `#gpt-llms应用` in CN) — preserve those exact slugs.
- When linking to a deep-dive doc, use the EN/CN phrasing pair `[Intro](...)` / `[入门介绍](...)` so both READMEs stay parallel.
- Keep tool descriptions concise and factual; ensure links are valid.
- Maintain bilingual consistency between English and Chinese READMEs.
