# Muse Glimmer & Muse Code Addition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Meta's newly open-sourced Muse Glimmer model and the Muse Code terminal coding agent to the bilingual READMEs and CHANGELOG.

**Architecture:** Insert two new rows into existing tables in both READMEs (Open Source LLMs and AI Agent sections), add two bullets to the August 2026 CHANGELOG, run the README formatter, and optionally verify links.

**Tech Stack:** Markdown, Python 3, `scripts/format_readmes.py`, optional `lychee`.

## Global Constraints

- Keep English and Chinese READMEs structurally mirrored.
- Use the existing 4-column table schema.
- Run `python3 scripts/format_readmes.py` after any table edit.
- Do not modify existing tool entries or unrelated sections.
- If the `meta.ai` product link fails link checking, add `meta.ai` to `.lycheeignore`.

---

### Task 1: Add Muse Glimmer to README.md Open Source LLMs

**Files:**
- Modify: `README.md:115-116` (between Gemma 4 and Llama 3)

**Interfaces:**
- Consumes: Existing `### Open Source LLMs` table.
- Produces: New `Muse Glimmer` row in the English table.

- [ ] **Step 1: Insert Muse Glimmer row**

Insert the following row immediately after the `| Gemma 4 |...` row and before the `| Llama 3 |...` row:

```markdown
| Muse Glimmer | Meta's 30B-parameter open-weight multimodal model for local agents, released under Apache 2.0. Features ~131K context, text/image input, tool use, 4-bit quantized variants for 24–32 GB VRAM, and DFlash speculative decoding. Distilled from Muse Spark. | [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B) [Ars Technica coverage](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/) | Free |
```

- [ ] **Step 2: Verify insertion**

Run:

```bash
grep -n "Muse Glimmer" README.md
```

Expected output contains the new row and line number is between the Gemma 4 and Llama 3 rows.

---

### Task 2: Add Muse Code to README.md AI Agent

**Files:**
- Modify: `README.md:137-138` (between Kimi Code and Grok Build)

**Interfaces:**
- Consumes: Existing `### AI Agent` table.
- Produces: New `Muse Code` row in the English table.

- [ ] **Step 1: Insert Muse Code row**

Insert the following row immediately after the `| Kimi Code |...` row and before the `| Grok build |...` row:

```markdown
| Muse Code | Meta's beta terminal coding agent powered by Muse Spark 1.2. Plans changes, writes code, and validates results across large repos using persistent async background agents and an append-only event log. macOS/Linux; pay-as-you-go with an optional Contributor tier that exchanges lower pricing for training-data permission. | [URL](https://www.meta.ai/muse/code) [VentureBeat coverage](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents) | Free/Paid |
```

- [ ] **Step 2: Verify insertion**

Run:

```bash
grep -n "Muse Code" README.md
```

Expected output contains the new row and line number is between the Kimi Code and Grok build rows.

---

### Task 3: Add Muse Glimmer to README-CN.md 开源大语言模型

**Files:**
- Modify: `README-CN.md:124-125` (between Gemma 4 and Llama 3)

**Interfaces:**
- Consumes: Existing `### 开源大语言模型` table.
- Produces: New `Muse Glimmer` row in the Chinese table.

- [ ] **Step 1: Insert Muse Glimmer row**

Insert the following row immediately after the `| Gemma 4 |...` row and before the `| Llama 3 |...` row:

```markdown
| Muse Glimmer | Meta 开源的 300 亿参数多模态本地智能体模型，采用 Apache 2.0 许可。支持约 13.1 万 token 上下文、文本/图像输入、工具调用，4-bit 量化后可在 24–32 GB 显存的消费级显卡上运行，并配备 DFlash 投机解码。由 Muse Spark 蒸馏而来。 | [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B) [Ars Technica 报道](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/) | 免费 |
```

- [ ] **Step 2: Verify insertion**

Run:

```bash
grep -n "Muse Glimmer" README-CN.md
```

Expected output contains the new row and line number is between the Gemma 4 and Llama 3 rows.

---

### Task 4: Add Muse Code to README-CN.md AI Agent

**Files:**
- Modify: `README-CN.md:146-147` (between Kimi Code and Trae)

**Interfaces:**
- Consumes: Existing `### AI Agent` table.
- Produces: New `Muse Code` row in the Chinese table.

- [ ] **Step 1: Insert Muse Code row**

Insert the following row immediately after the `| Kimi Code |...` row and before the `| Trae |...` row:

```markdown
| Muse Code | Meta 推出的基于终端的 AI 编程智能体（Beta），由 Muse Spark 1.2 驱动。支持跨大型代码库的规划、编写代码与验证结果，具备持久异步后台代理和追加式本地事件日志，可在崩溃后恢复。支持 macOS/Linux；按量付费，另有 Contributor 档位以允许使用提示/补全训练来换取更低价格。 | [URL](https://www.meta.ai/muse/code) [VentureBeat 报道](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents) | 免费/付费 |
```

- [ ] **Step 2: Verify insertion**

Run:

```bash
grep -n "Muse Code" README-CN.md
```

Expected output contains the new row and line number is between the Kimi Code and Trae rows.

---

### Task 5: Update CHANGELOG.md

**Files:**
- Modify: `CHANGELOG.md:5-8`

**Interfaces:**
- Consumes: Existing `## August 2026` block.
- Produces: Two new bullets documenting the additions.

- [ ] **Step 1: Append changelog bullets**

Add the following bullets to the `## August 2026` list, at the top of the existing entries:

```markdown
- Added Muse Glimmer (meta-models/Muse-Glimmer-30B) to Open Source LLMs section (both EN/CN)
- Added Muse Code to AI Agent section (both EN/CN)
```

- [ ] **Step 2: Verify CHANGELOG entries**

Run:

```bash
grep "Muse Glimmer" CHANGELOG.md
grep "Muse Code" CHANGELOG.md
```

Expected output contains both new bullets under `## August 2026`.

---

### Task 6: Format READMEs and Check Links

**Files:**
- Modify: `README.md`, `README-CN.md` (formatter may normalize whitespace/separators)

**Interfaces:**
- Consumes: Updated READMEs with new tables.
- Produces: Normalized READMEs.

- [ ] **Step 1: Run README formatter**

Run:

```bash
python3 scripts/format_readmes.py
```

Expected: script exits with code 0 and no error output.

- [ ] **Step 2: Verify formatter preserved the new rows**

Run:

```bash
grep -c "Muse Glimmer" README.md
grep -c "Muse Glimmer" README-CN.md
grep -c "Muse Code" README.md
grep -c "Muse Code" README-CN.md
```

Expected: each command outputs at least `1`.

- [ ] **Step 3: Optional link check**

If `lychee` is installed, run:

```bash
lychee .
```

Expected: no new 404 errors for the added links.

If `https://www.meta.ai/muse/code` fails due to bot challenges, add `meta.ai` to `.lycheeignore` and re-run.

---

## Self-Review Checklist

- [ ] Spec coverage: Muse Glimmer and Muse Code rows in both READMEs, CHANGELOG entries, formatter run, and optional link check are all covered.
- [ ] No placeholders: all markdown content and commands are exact.
- [ ] Type consistency: table columns and section structure match the existing 4-column schema in both languages.
