# Contributing to Awesome-AITools

Thanks for your interest in improving this list! Awesome-AITools is a curated, bilingual (EN/CN) collection of AI tools — the product is the two README files, with long-form tool intros hosted as GitHub Discussions.

There is no application code. The value is in keeping entries accurate, links alive, and the two READMEs in sync.

## Ways to contribute

- **Recommend a tool** — open an issue using the [recommendation template](https://github.com/ikaijua/Awesome-AITools/issues/233), or submit a PR that adds the entry directly.
- **Write a long-form intro (optional)** — not required. If you want to go deeper, create a GitHub Discussion (one EN + one CN) for a tool and link it from the README entry (see below).
- **Fix links, typos, or stale entries** — the most common and always welcome type of PR.
- **Report a problem** — broken link, outdated description, dead discussion link.

## Inclusion criteria

- **Unique and practical first** — there are many similar tools, so prioritize tools with unique, practical functionality: something others don't offer, or clearly better at a specific job.
- **Broad applicability** — the wider the scope, the better: a tool that serves most people and most scenarios is more likely to be included than one solving a narrow niche problem.
- **Actually usable** — ships with an entry point, docs, or examples — not a concept demo; key capabilities and pricing should be verifiable.
- **Still alive** — recently updated or showing activity, with working links; stale or abandoned tools are not added.
- **Not included** — near-identical clones (without a clear increment), thin wrappers with no own value, or tools with obvious security or compliance risks.

## Editing conventions

The two READMEs serve different audiences and are allowed to differ — each is written for its own readers' familiarity and habits (e.g. international readers need no explanation of Western services, while Chinese readers may need more background on foreign tools, and vice versa). Keep the tool set consistent so nothing appears in only one list, but wording, detail level, and phrasing may differ.

- **Table schema**: both files use the same 4-column table:
  - English: `| Name | Description | Links | Fees |`
  - Chinese: `| 名称 | 说明 | 链接 | 费用 |`
- **Strict table format**: exactly 4 columns, separator row `| --- | --- | --- | --- |`. Don't hand-craft 3- or 5-column variants — the formatter rewrites them.
- **Keep descriptions concise and factual**; make sure every link is valid.
- **Markers**:
  - 🌟 — genuinely great, the first-choice pick in its category; use sparingly.
  - 🌱 — high short-term buzz, but still early-stage.
- **Deep dives (optional)**: not every entry needs a long-form intro — the README entry itself is enough. When you do write one, it lives in GitHub Discussions — never add per-tool pages under a `docs/` directory. Each deep dive has one CN + one EN post (e.g. `[Intro](...)` / `[入门介绍](...)`), and the README entry links to it. Content that changes frequently (features, pricing) belongs in the Discussion, not the README.
- **Preserve known TOC slugs** at the top of each README (the formatter relies on `#news-information` in EN and `#gpt-llms应用` in CN).

## CHANGELOG

- Record additions, removals, renames, and notable model updates (e.g. a chatbot entry refreshed to a new flagship version).
- One line per change: tool/section name + what changed + `(both EN/CN)`.
- Minor description edits, section reordering, and link/reference fixes do **not** need a changelog entry.

## Before submitting

1. After any table edit, run the normalizer from anywhere:
   ```bash
   python3 scripts/format_readmes.py
   ```
   It rewrites tables to the canonical 4-column form and fixes known TOC anchor typos.
2. Optional local link check (requires [lychee](https://github.com/lycheeverse/lychee)):
   ```bash
   lychee .
   ```
   CI runs the same check on `**/*.md`; `.lycheeignore` holds the exclusion list.

## License

This repository is licensed under [CC BY 4.0](LICENSE). By contributing, you agree that your contributions are licensed under the same terms.
