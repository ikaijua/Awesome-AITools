# Contributing to Awesome-AITools

Thanks for your interest in improving this list! Awesome-AITools is a curated, bilingual (EN/CN) collection of AI tools — the product is the two README files, with long-form tool intros hosted as GitHub Discussions.

There is no application code. The value is in keeping entries accurate, links alive, and the two READMEs in sync.

## Ways to contribute

- **Recommend a tool** — submit a PR that adds the entry directly to both READMEs. Focus your PR on the three [submission requirements](#before-you-submit) below.
- **Write a long-form intro (optional)** — not required. If you want to go deeper, create a GitHub Discussion (one EN + one CN) for a tool and link it from the README entry (see below).
- **Fix links, typos, or stale entries** — the most common and always welcome type of PR.
- **Report a problem** — broken link, outdated description, dead discussion link.

## Inclusion criteria

- **Unique and practical first** — there are many similar tools, so prioritize tools with unique, practical functionality: something others don't offer, or clearly better at a specific job.
- **Broad applicability** — the wider the scope, the better: a tool that serves most people and most scenarios is more likely to be included than one solving a narrow niche problem.
- **Actually usable** — ships with an entry point, docs, or examples — not a concept demo; key capabilities and pricing should be verifiable.
- **Still alive** — recently updated or showing activity, with working links; stale or abandoned tools are not added.
- **Not included** — near-identical clones (without a clear increment), thin wrappers with no own value, or tools with obvious security or compliance risks.

## What to demonstrate before contributing

The inclusion criteria above are principles. In practice, reviewers weigh three things most heavily — prepare these and your PR merges faster:

- **Disclose any affiliation (required)** — if you're the author, team member, investor, or promoter of the tool, say so in the PR. Transparent recommendations are welcome.
- **Uniqueness (required)** — explain why it deserves a spot: the concrete capability others lack, or where it's clearly better than comparable tools. Don't just paste a feature list. Stating what it *can't* do is a strong signal of a genuine product. If it wraps a mainstream LLM, make clear the value is in the in-house orchestration / integration, not the base model — otherwise it looks like a thin wrapper. Back it up with:
  - Third-party reviews / head-to-head evaluations
  - Standout user cases (named customers or shipped production case studies)
- **Popularity & traction (required)** — back "it's worth including" with verifiable evidence of reach and activity; this also shows the tool is "still alive":
  - Monthly active users / total user count, download numbers

> If affiliation isn't disclosed, or uniqueness / popularity can't be shown, reviewers will ask for more material or decline the submission.

## Editing conventions

The two READMEs serve different audiences and are allowed to differ — each is written for its own readers' familiarity and habits (e.g. international readers need no explanation of Western services, while Chinese readers may need more background on foreign tools, and vice versa). Keep the tool set consistent so nothing appears in only one list, but wording, detail level, and phrasing may differ.

- **Table schema**: both files use the same 4-column table:
  - English: `| Name | Description | Links | Fees |`
  - Chinese: `| 名称 | 说明 | 链接 | 费用 |`
- **Strict table format**: exactly 4 columns, separator row `| --- | --- | --- | --- |`. Don't hand-craft 3- or 5-column variants — the formatter rewrites them.
- **Keep descriptions concise and factual**; make sure every link is valid.
- **Disclose affiliation**: if you are the author, team member, or maintainer of the tool, say so in the PR (e.g. "I built it" / "I maintain it").
- **Markers**:
  - 🌟 — genuinely great, the first-choice pick in its category; use sparingly.
  - 🌱 — high short-term buzz, but still early-stage.
- **Deep dives (optional)**: not every entry needs a long-form intro — the README entry itself is enough. When you do write one, it lives in GitHub Discussions — never add per-tool pages under a `docs/` directory. Each deep dive has one CN + one EN post (e.g. `[Intro](...)` / `[入门介绍](...)`), and the README entry links to it. Content that changes frequently (features, pricing) belongs in the Discussion, not the README.
- **Preserve known TOC slugs** at the top of each README (the formatter relies on `#news-information` in EN and `#gpt-llms应用` in CN).

## CHANGELOG

- Record additions, removals, renames, and notable model updates (e.g. a chatbot entry refreshed to a new flagship version).
- One line per change: tool/section name + what changed + `(both EN/CN)`.
- Minor description edits, section reordering, and link/reference fixes do **not** need a changelog entry.

## Before you submit

Focus your effort on the three things that decide whether a tool gets included:

- **Disclose any affiliation** — author / team / investor / promoter? Say so in the PR. (See [What to demonstrate](#what-to-demonstrate-before-contributing).)
- **Show uniqueness** — why this tool, and what it does better than comparable ones.
- **Show popularity & traction** — verifiable reach/activity: user count (MAU / total users).

## Before submitting (commands)

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
