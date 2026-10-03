# AGENTS.md for Awesome-AITools

This file provides context and instructions for AI coding agents (e.g., Cursor, Aider, Claude Code, Windsurf) to help them understand this repository more effectively. It follows the [AGENTS.md](https://agents.md/) standard.

## Repository Purpose

A curated, bilingual (EN/CN) "awesome list" of AI tools — chatbots, agents, skills, CLI tools, and more. There is no application code; the repository's product is the two README files, with long-form tool intros hosted as GitHub Discussions.

## Key Files & Directories

- `README.md` — Main tool list (English).
- `README-CN.md` — Main tool list (Chinese).
- `CHANGELOG.md` — Monthly log (e.g. `## June 2026`) of additions/removals/renames.
- `scripts/format_readmes.py` — Maintenance/normalization script.

Note: there is **no `docs/` directory**. It was retired — every per-tool page was either migrated to a GitHub Discussion or dropped. Do not recreate it.

## Architecture

The repo has two READMEs serving different audiences — they are not parallel mirrors:

- `README.md` (EN) and `README-CN.md` (CN) cover the same tool set but are written for different readers' familiarity and habits; wording, detail level, and phrasing may differ per language. Both use the same 4-column table schema:
  - English: `| Name | Description | Links | Fees |`
  - Chinese: `| 名称 | 说明 | 链接 | 费用 |`
- README entries with a deep-dive link point to a GitHub Discussion, e.g. `[Intro](https://github.com/ikaijua/Awesome-AITools/discussions/<n>)` (EN) and `[入门介绍](https://github.com/ikaijua/Awesome-AITools/discussions/<n>)` (CN). One discussion per language — the EN entry links the English post, the CN entry links the Chinese post.

When adding/removing/editing a tool, the change touches **both** READMEs — keep the tool set consistent across languages, though the wording may differ per audience (and the change often also touches `CHANGELOG.md` and a GitHub Discussion). A tool missing from one language is a bug.

## Commands

- Format/normalize both READMEs: `python3 scripts/format_readmes.py` (run from anywhere — the script resolves the project root itself). This rewrites tables to the canonical 4-column form, strips ` `, converts `</br>` → `<br>`, dedents tabs, and fixes a couple of known broken TOC anchors. Run it after any table edit.
- Local link check (requires [lychee](https://github.com/lycheeverse/lychee) installed): `lychee .` — mirrors the CI workflow at `.github/workflows/link-check.yml`. `.lycheeignore` holds the exclusion list.

There is no build, test, or lint suite beyond the above — CI only runs link checking on `**/*.md`.

## Editing Conventions

- When adding a new tool, follow the existing table format in both READMEs.
- Inclusion criteria: prioritize tools with unique, practical functionality and broad applicability; require usable, verifiable, still-active tools; exclude clones, thin wrappers, and tools with security or compliance risks.
- Table format is strict: exactly 4 columns, with the separator row `| --- | --- | --- | --- |`. `format_readmes.py` will rewrite divergent separators, so don't hand-craft 3- or 5-column variants.
- The TOC at the top of each README lists category anchors. The formatter knows about two specific anchor-typo fixes (`#news-information` in EN, `#gpt-llms应用` in CN) — preserve those exact slugs.
- When linking to a deep-dive discussion, use the EN/CN phrasing pair `[Intro](...)` / `[入门介绍](...)` so the link convention stays consistent across both READMEs.
- **Deep-dive placement convention**: All long-form tool intros live in GitHub Discussions (one CN + one EN, e.g. Codex, Kimi Code, 豆包工作, Google AX, ARTEMIS), and the README entry links to the corresponding discussion — never add per-tool pages under a `docs/` directory. Content that changes frequently (product features, pricing details) belongs in Discussions.
- **Discussion body format**: Start with an `# H1` matching the discussion title, then a table of contents whose entries are **absolute** anchor links back to the discussion URL. EN posts use `## Table of Contents`; CN posts use `## 目录` preceded by a maintenance note, e.g. `> 本帖随产品更新持续维护。仓库 README 的 <名称> 条目已链接到本帖，详细介绍直接在这里更新，避免频繁改动仓库。` Titles follow `<Tool>: Detailed Introduction` (EN) / `<名称> 详细介绍` (CN).
- Keep tool descriptions concise and factual; ensure links are valid.
  - **Description depth guideline**: aim for roughly 400–600 characters in English and 300–450 characters in Chinese. Focus on what the tool is, its current flagship model/version, its key differentiation, and availability/pricing. Avoid dumping exhaustive architecture details, benchmark scores, or long release history into the README table — if a dedicated discussion exists, link to it (`[Intro](...)` / `[入门介绍](...)`) and keep the table entry brief.
  - **What to emphasize**: lead with the tool's positioning and key advantage — answer "why choose it" (open license / self-hosting, cost-performance, unique capability, ecosystem fit), not just "what are its specs". Prioritize features, effects/quality, and uniqueness — the things that help a reader decide whether to try the tool. Move low-attention details (parameter counts, architecture acronyms, minor feature release dates, cost-saving modes, version retirement/reversal plans) to the linked discussion.
  - **Line breaks inside descriptions**: `<br>` is fine for separating distinct pieces of information (e.g., a second link list or a short note), but don't use it to stack many paragraphs; if a cell needs that much structure, move the detail to a discussion.
  - Maintain a similar information density across both languages: trimming one language usually means trimming the other as well.
- Keep the tool set consistent across the two READMEs; wording may differ per audience.
- **Marker conventions**: 🌟 marks tools that are genuinely good to use — the first-choice pick in their category; apply it sparingly. 🌱 marks tools with high short-term buzz but still early-stage.
- **CHANGELOG.md**: Document additions, removals, renames, and notable model updates (e.g., when a chatbot or model entry is refreshed to a new flagship version). Keep entries concise — one line per change: tool/section name, the essence of what changed, and `(both EN/CN)`; spec details and background belong in the README or discussion pages, not the changelog. Minor description updates (e.g., fixing typos, small feature list tweaks), section reordering, and moving tools within a section do NOT require a changelog entry. Neither do link/reference fixes — e.g., repairing dead links, repointing a README link to a different Discussion, or other changes that alter no tool information.
