# Qwen README Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the Qwen / 通义千问 chatbot entry in both README files to reflect the latest Qwen3.8-Max model.

**Architecture:** Direct in-place edits of the bilingual README markdown tables, followed by the repository's standard formatter to normalize table structure and a quick diff/link verification.

**Tech Stack:** Markdown, `python3 scripts/format_readmes.py`, optional `lychee`.

## Global Constraints

- Maintain bilingual consistency between `README.md` and `README-CN.md`.
- Preserve the existing 4-column table schema (`| Name | Description | Links | Fees |` / `| 名称 | 说明 | 链接 | 费用 |`).
- Do not create new `docs/qwen/` deep-dive pages.
- Do not add new tool entries (e.g., Qwen Code).
- Run `python3 scripts/format_readmes.py` after any table edit.

---

### Task 1: Update `README.md` Qwen chatbot entry

**Files:**
- Modify: `README.md:103`

**Interfaces:**
- Consumes: Current `qwen` row text in the AI Chatbots table.
- Produces: Updated `qwen` row mentioning Qwen3.8-Max.

- [ ] **Step 1: Read the current row**

Run:
```bash
sed -n '103p' README.md
```

Expected output:
```markdown
| qwen | Alibaba's AI chatbot. Includes Qwen 3.7-Plus/Max in Qwen Chat, supporting 1M context window, native multimodality, and long-horizon agentic reasoning. |[URL](https://chat.qwen.ai/)|Free|
```

- [ ] **Step 2: Replace the row with the updated text**

Use `Edit` to replace the exact line from Step 1 with:

```markdown
| qwen | Alibaba's AI chatbot. Qwen Chat now runs on Qwen3.8-Max, a 2.4T-parameter MoE model with native multimodality, 1M-token context window, and long-horizon agentic reasoning. |[URL](https://chat.qwen.ai/)|Free|
```

- [ ] **Step 3: Verify the change**

Run:
```bash
sed -n '103p' README.md
```

Expected output matches the new line from Step 2.

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "docs: update Qwen chatbot entry to Qwen3.8-Max in README.md"
```

---

### Task 2: Update `README-CN.md` 通义千问 chatbot entry

**Files:**
- Modify: `README-CN.md:108`

**Interfaces:**
- Consumes: Current `通义千问` row text in the AI 聊天机器人 table.
- Produces: Updated `通义千问` row mentioning Qwen3.8-Max.

- [ ] **Step 1: Read the current row**

Run:
```bash
sed -n '108p' README-CN.md
```

Expected output:
```markdown
| 通义千问 |阿里的大语言模型。 <br> Qwen Chat 可体验 Qwen3.7-Plus/Max 等最新模型，支持 100 万超长上下文、原生多模态以及长链路 Agent 推理，并提供深度研究选项。|[URL](https://chat.qwen.ai/)|免费|
```

- [ ] **Step 2: Replace the row with the updated text**

Use `Edit` to replace the exact line from Step 1 with:

```markdown
| 通义千问 |阿里的大语言模型。 <br> Qwen Chat 已升级至 Qwen3.8-Max，2.4T 参数 MoE 架构，支持 100 万超长上下文、原生多模态、长链路 Agent 推理与深度研究。|[URL](https://chat.qwen.ai/)|免费|
```

- [ ] **Step 3: Verify the change**

Run:
```bash
sed -n '108p' README-CN.md
```

Expected output matches the new line from Step 2.

- [ ] **Step 4: Commit**

```bash
git add README-CN.md
git commit -m "docs: update 通义千问 chatbot entry to Qwen3.8-Max in README-CN.md"
```

---

### Task 3: Normalize and verify both READMEs

**Files:**
- Modify: `README.md` and `README-CN.md` (formatter may rewrite whitespace/separators)

**Interfaces:**
- Consumes: Edited bilingual README files.
- Produces: Formatter-normalized README files with valid tables and links.

- [ ] **Step 1: Run the README formatter**

Run:
```bash
python3 scripts/format_readmes.py
```

Expected: Command exits with code 0 and both README files may show minor whitespace/separator normalizations.

- [ ] **Step 2: Inspect the diff**

Run:
```bash
git diff -- README.md README-CN.md
```

Expected: Diff shows the Qwen row updates plus any formatter-only normalizations. No unintended category or row changes.

- [ ] **Step 3: Optional link check**

If `lychee` is installed, run:

```bash
lychee .
```

Expected: The `https://chat.qwen.ai/` link remains reachable. (Other pre-existing failures are out of scope.)

- [ ] **Step 4: Commit formatter changes**

If the formatter produced changes:

```bash
git add README.md README-CN.md
git commit -m "chore: normalize README tables after Qwen update"
```

If the formatter produced no changes, skip this commit.
