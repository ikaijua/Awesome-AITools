# Add Xuanshu API Sponsor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the Xuanshu API sponsor to both `README.md` and `README-CN.md`, displayed side-by-side with the existing Doloffer sponsor.

**Architecture:** Convert the existing single-column HTML sponsor table into a two-column table with Doloffer in the first cell and Xuanshu API in the second. Keep all existing copy and links intact, clean up malformed trailing `</tr>` tags, and run the repository formatter.

**Tech Stack:** Markdown / HTML in README files; `python3 scripts/format_readmes.py` for normalization.

## Global Constraints
- Preserve bilingual parity between `README.md` and `README-CN.md`.
- Keep the existing Doloffer sponsor content unchanged except for table layout.
- Link Xuanshu API logo and text to `https://www.xuanshuapi.com/`.
- Use the provided logo URL: `https://www.xuanshuapi.com/brand/logo.svg`.
- Do not add a `CHANGELOG.md` entry (sponsor display updates are not logged per repo convention).
- Run `python3 scripts/format_readmes.py` after editing and verify it exits cleanly.

---

### Task 1: Update `README.md` sponsor section

**Files:**
- Modify: `README.md:19-40`

**Interfaces:**
- Consumes: Existing Doloffer sponsor HTML block.
- Produces: Two-column sponsor table containing Doloffer and Xuanshu API.

- [ ] **Step 1: Replace the sponsor table block**

Replace lines 19-40 in `README.md` with the following content (keep the leading `## 💎 Sponsor` heading and the preceding `<p>` thank-you paragraph):

```markdown
## 💎 Sponsor

<p align="center">
  A huge thank you to our sponsors for their generous support!
</p>

<table align="center" cellpadding="10" style="width:100%; border-collapse:collapse;">
  <tr align="center">
    <td width="50%" valign="middle" align="center">
      <sub>
        <a href="https://doloffer.com/" target="_blank">
          <img alt="Visit DOLOFFER website" src="https://github.com/user-attachments/assets/94c3e24b-c0ce-4b07-8a80-76c21856f74c" />
        </a>
         【"Doloffer"--One-stop digital subscription and top-up platform
        , We specialize in offering genuine subscriptions to various AI-powered digital services, including GPT and Claude. Get a 10% discount with code AI8888. Fast shipping and worry-free after-sales service.】
      </sub>
    </td>
    <td width="50%" valign="middle" align="center">
      <sub>
        <a href="https://www.xuanshuapi.com/" target="_blank">
          <img alt="Xuanshu API" src="https://www.xuanshuapi.com/brand/logo.svg" />
        </a>
        【Xuanshu API is a next-generation AI model routing gateway for enterprises, technical teams, and individual developers. It provides one-stop API access to world-class top models (Claude, GPT, Grok, etc.) with enterprise-grade stability. Recharge and enjoy 20% off, models starting from 20% of the original price, $5 free upon registration, invoice support for enterprises. Click this link to register and get an extra $5 credit.】
      </sub>
    </td>
  </tr>
</table>
```

- [ ] **Step 2: Verify the replacement visually**

Open `README.md` and confirm:
- The `## 💎 Sponsor` heading remains.
- The thank-you paragraph is unchanged.
- The table has exactly one `<tr>` with two `<td>` cells.
- Doloffer content matches the original exactly.
- Xuanshu API content uses the English copy and logo URL.
- No extra `</tr>` tags remain after the table.

---

### Task 2: Update `README-CN.md` sponsor section

**Files:**
- Modify: `README-CN.md:19-39`

**Interfaces:**
- Consumes: Existing Doloffer Chinese sponsor HTML block.
- Produces: Two-column sponsor table containing Doloffer and Xuanshu API in Chinese.

- [ ] **Step 1: Replace the sponsor table block**

Replace lines 19-39 in `README-CN.md` with the following content (keep the leading `## 💎 赞助商` heading and the preceding `<p>` thank-you paragraph):

```markdown
## 💎 赞助商

<p align="center">
  非常感谢赞助商的慷慨支持！
</p>

<table align="center" cellpadding="10" style="width:100%; border-collapse:collapse;">
  <tr align="center">
    <td width="50%" valign="middle" align="center">
      <sub>
        <a href="https://doloffer.com/zh/" target="_blank">
          <img src="https://github.com/user-attachments/assets/cd93d75f-c7f0-4295-9bf5-a2ae412feefc" alt="Visit DOLOFFER website">
        </a>
        【“Doloffer”--一站式数字订阅充值平台, 主营 GPT、Claude 等 AI多类数字服务会员正版订阅，9 折优惠码 AI8888，极速发货，售后无忧】
      </sub>
    </td>
    <td width="50%" valign="middle" align="center">
      <sub>
        <a href="https://www.xuanshuapi.com/" target="_blank">
          <img src="https://www.xuanshuapi.com/brand/logo.svg" alt="玄枢 API">
        </a>
        【玄枢API是面向企业、技术团队和个人开发者的新一代 AI 模型路由网关，提供企业级稳定性的全球顶级模型（Claude, GPT, Grok等）一站式API 接入。充值享八折，模型2折起，注册送5美金，企业支持开票，点此链接注册额外获赠5美金额度。】
      </sub>
    </td>
  </tr>
</table>
```

- [ ] **Step 2: Verify the replacement visually**

Open `README-CN.md` and confirm:
- The `## 💎 赞助商` heading remains.
- The thank-you paragraph is unchanged.
- The table has exactly one `<tr>` with two `<td>` cells.
- Doloffer content matches the original exactly.
- Xuanshu API content uses the Chinese copy and logo URL.
- No extra `</tr>` tags remain after the table.

---

### Task 3: Normalize READMEs and verify

**Files:**
- Modify: `README.md`, `README-CN.md` (via formatter rewrite)

**Interfaces:**
- Consumes: Updated `README.md` and `README-CN.md`.
- Produces: Normalized README files.

- [ ] **Step 1: Run the README formatter**

Run:

```bash
python3 scripts/format_readmes.py
```

Expected: The command exits with code 0 and no error output.

- [ ] **Step 2: Inspect formatter output**

Run:

```bash
git diff -- README.md README-CN.md
```

Expected:
- The sponsor table in each file now has two columns.
- Doloffer content is unchanged in meaning.
- Xuanshu API content is present in both languages.
- No unexpected rewrites outside the sponsor section (minor whitespace normalization by the formatter is acceptable).

- [ ] **Step 3: Validate the logo URL is reachable (optional but recommended)**

Run:

```bash
curl -I https://www.xuanshuapi.com/brand/logo.svg
```

Expected: HTTP 200 OK (or a redirect to a successful response).

---

## Self-Review

**1. Spec coverage:**
- Add Xuanshu API to `README.md` → Task 1.
- Add Xuanshu API to `README-CN.md` → Task 2.
- Display side-by-side with Doloffer → both tasks use two-column table.
- Use provided copy and logo URL → included verbatim in each task.
- Clean up malformed `</tr>` tags → included in replacement blocks.
- Run formatter → Task 3.

**2. Placeholder scan:**
- No TBD/TODO/"implement later"/"fill in details" markers.
- All code blocks contain the exact HTML to write.
- Exact commands and expected outputs are provided.

**3. Type consistency:**
- Not applicable; this is a Markdown/HTML change with no code interfaces.
