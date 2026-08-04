# Add Codex Security Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add OpenAI's `codex-security` project to the Awesome-AITools bilingual READMEs with matching docs pages and a changelog entry.

**Architecture:** Add one row to the AI Coding table in both `README.md` and `README-CN.md`, create bilingual docs under `docs/codex-security/`, update `CHANGELOG.md`, and run the README formatter.

**Tech Stack:** Markdown only; no code. Use `python3 scripts/format_readmes.py` for normalization.

## Global Constraints

- Keep the existing 4-column table schema: `| Name | Description | Links | Fees |` (EN) / `| 名称 | 说明 | 链接 | 费用 |` (CN).
- EN/CN entries must stay in sync: same tool, same section, same links.
- Link docs using `[Intro](docs/codex-security/README.md)` / `[入门介绍](docs/codex-security/README-CN.md)`.
- Fees: use `Free` / `免费` because the CLI and SDK are open source under Apache 2.0.
- Run the formatter before considering the work complete.

---

### Task 1: Create English docs page

**Files:**
- Create: `docs/codex-security/README.md`

**Interfaces:**
- Produces: `docs/codex-security/README.md` to be linked from `README.md`.

- [ ] **Step 1: Write the English docs page**

Create `docs/codex-security/README.md` with the following content:

```markdown
# Codex Security Introduction

## What is Codex Security?

Codex Security is an open-source CLI and TypeScript SDK from OpenAI for finding, validating, and fixing security vulnerabilities in your code.

## Key Features

- **Repository scanning**: Scan local codebases for security vulnerabilities.
- **Finding tracking**: Track findings across multiple runs and compare scan results.
- **Fix verification**: Validate that a fix actually resolves the underlying issue.
- **CI/CD integration**: Run non-interactive scans in pipelines using `OPENAI_API_KEY` or `CODEX_API_KEY`.
- **TypeScript SDK**: Embed scanning capabilities directly into Node.js applications.
- **Containerized bulk scans**: Use the official Docker image for scalable, resumable scans.

## Quick Start

```bash
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
```

For CI environments:

```bash
export OPENAI_API_KEY=sk-...
npx @openai/codex-security scan .
```

## Links

- [GitHub Repository](https://github.com/openai/codex-security)
- [OpenAI Codex Security Documentation](https://github.com/openai/codex-security/tree/main/docs)
```

- [ ] **Step 2: Verify the file exists and renders correctly**

Run:

```bash
ls -la docs/codex-security/README.md
```

Expected: file exists.

---

### Task 2: Create Chinese docs page

**Files:**
- Create: `docs/codex-security/README-CN.md`

**Interfaces:**
- Produces: `docs/codex-security/README-CN.md` to be linked from `README-CN.md`.

- [ ] **Step 1: Write the Chinese docs page**

Create `docs/codex-security/README-CN.md` with the following content:

```markdown
# Codex Security 入门介绍

## 什么是 Codex Security？

Codex Security 是 OpenAI 开源的一款 CLI 和 TypeScript SDK，用于发现、验证并修复代码中的安全漏洞。

## 核心功能

- **仓库扫描**：扫描本地代码库中的安全漏洞。
- **漏洞追踪**：跨多次运行追踪漏洞，并对比扫描结果。
- **修复验证**：验证修复是否真正解决了根本问题。
- **CI/CD 集成**：通过 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 在流水线中运行非交互式扫描。
- **TypeScript SDK**：将扫描能力直接嵌入 Node.js 应用。
- **容器化批量扫描**：使用官方 Docker 镜像进行可扩展、可恢复的批量扫描。

## 快速开始

```bash
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
```

在 CI 环境中：

```bash
export OPENAI_API_KEY=sk-...
npx @openai/codex-security scan .
```

## 链接

- [GitHub 仓库](https://github.com/openai/codex-security)
- [OpenAI Codex Security 文档](https://github.com/openai/codex-security/tree/main/docs)
```

- [ ] **Step 2: Verify the file exists and renders correctly**

Run:

```bash
ls -la docs/codex-security/README-CN.md
```

Expected: file exists.

---

### Task 3: Add Codex Security to English README

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: `docs/codex-security/README.md` created in Task 1.

- [ ] **Step 1: Insert the new row into the AI Coding table**

Find the `### AI Coding` table in `README.md`. Insert the following row after the `CLIProxyAPI` row (last row of the section):

```markdown
| Codex Security | Open-source CLI and TypeScript SDK from OpenAI for finding, validating, and fixing security vulnerabilities in code. Supports repository scanning, finding tracking, fix verification, CI/CD integration, and containerized bulk scans. [Intro](docs/codex-security/README.md) | [Github](https://github.com/openai/codex-security) ![GitHub Repo stars](https://img.shields.io/github/stars/openai/codex-security?style=social) | Free |
```

- [ ] **Step 2: Verify the table still has four columns**

Run:

```bash
grep -n "Codex Security" README.md
```

Expected: one match in the AI Coding table.

---

### Task 4: Add Codex Security to Chinese README

**Files:**
- Modify: `README-CN.md`

**Interfaces:**
- Consumes: `docs/codex-security/README-CN.md` created in Task 2.

- [ ] **Step 1: Insert the new row into the AI Coding table**

Find the `### AI Coding` table in `README-CN.md`. Insert the following row after the `CLIProxyAPI` row (last row of the section):

```markdown
| Codex Security | OpenAI 开源的 CLI 与 TypeScript SDK，用于发现、验证并修复代码中的安全漏洞。支持仓库扫描、漏洞追踪、修复验证、CI/CD 集成以及容器化批量扫描。[入门介绍](docs/codex-security/README-CN.md) | [Github](https://github.com/openai/codex-security) ![GitHub Repo stars](https://img.shields.io/github/stars/openai/codex-security?style=social) | 免费 |
```

- [ ] **Step 2: Verify the table still has four columns**

Run:

```bash
grep -n "Codex Security" README-CN.md
```

Expected: one match in the AI Coding table.

---

### Task 5: Update CHANGELOG.md

**Files:**
- Modify: `CHANGELOG.md`

**Interfaces:**
- Consumes: completed README edits from Tasks 3 and 4.

- [ ] **Step 1: Add a changelog entry under the latest month**

Find `## July 2026` at the top of `CHANGELOG.md` and add the following line at the beginning of the list:

```markdown
- Added Codex Security (openai/codex-security) to AI Coding section with documentation (both EN/CN)
```

- [ ] **Step 2: Verify the entry is present**

Run:

```bash
grep -n "Codex Security" CHANGELOG.md
```

Expected: one match.

---

### Task 6: Format and verify

**Files:**
- Modify: `README.md`, `README-CN.md` (rewritten by formatter)

**Interfaces:**
- Consumes: all previous tasks.

- [ ] **Step 1: Run the README formatter**

Run:

```bash
python3 scripts/format_readmes.py
```

Expected: command exits with code 0.

- [ ] **Step 2: Verify the new entries survived formatting**

Run:

```bash
grep -n "Codex Security" README.md README-CN.md CHANGELOG.md
```

Expected: matches in all three files.

- [ ] **Step 3: Verify docs links resolve**

Run:

```bash
ls -la docs/codex-security/README.md docs/codex-security/README-CN.md
```

Expected: both files exist.

---

## Self-Review

- Spec coverage: every requirement (README EN, README CN, docs EN, docs CN, CHANGELOG, formatting) maps to a task.
- No placeholders: all file content and commands are concrete.
- Type consistency: not applicable for Markdown content edits.
