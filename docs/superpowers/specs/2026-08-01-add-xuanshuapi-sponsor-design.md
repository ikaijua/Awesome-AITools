# Add Xuanshu API Sponsor

## Summary
Add a new sponsor, **Xuanshu API**, to the sponsor section of both `README.md` (English) and `README-CN.md` (Chinese), displayed side-by-side with the existing Doloffer sponsor.

## Motivation
The repository maintains a sponsor section at the top of each README. A new sponsor has been secured and should be exposed to visitors in both language versions, using the same visual style as the existing sponsor.

## Current State
Both READMEs currently use a single-column HTML table to display one sponsor (Doloffer). The table is wrapped in a `<table>` with one `<tr>` containing one `<td width="500">`. Both files also contain malformed extra `</tr>` tags after the closing `</tr>`.

## Proposed Change
Convert the sponsor table from one column to two columns in a single row:

```html
<table align="center" cellpadding="10" style="width:100%; border-collapse:collapse;">
  <tr align="center">
    <td width="50%" valign="middle" align="center">
      <!-- Existing Doloffer sponsor content -->
    </td>
    <td width="50%" valign="middle" align="center">
      <!-- New Xuanshu API sponsor content -->
    </td>
  </tr>
</table>
```

### Xuanshu API Content

**English (`README.md`)**
- Link target: `https://www.xuanshuapi.com/`
- Logo: `https://www.xuanshuapi.com/brand/logo.svg`
- Description: "Xuanshu API is a next-generation AI model routing gateway for enterprises, technical teams, and individual developers. It provides one-stop API access to world-class top models (Claude, GPT, Grok, etc.) with enterprise-grade stability. Recharge and enjoy 20% off, models starting from 20% of the original price, $5 free upon registration, invoice support for enterprises. Click this link to register and get an extra $5 credit."

**Chinese (`README-CN.md`)**
- Link target: `https://www.xuanshuapi.com/`
- Logo: `https://www.xuanshuapi.com/brand/logo.svg`
- Description: "玄枢API是面向企业、技术团队和个人开发者的新一代 AI 模型路由网关，提供企业级稳定性的全球顶级模型（Claude, GPT, Grok等）一站式API 接入。充值享八折，模型2折起，注册送5美金，企业支持开票，点此链接注册额外获赠5美金额度。"

## Additional Cleanup
Remove the malformed extra `</tr>` tags that currently appear after the sponsor table's closing `</tr>` in both READMEs.

## Out of Scope
- No new `docs/<slug>/` deep-dive page.
- No `CHANGELOG.md` entry (per repository convention, only tool additions/removals/renames are logged; sponsor display updates are not).

## Verification
- Both READMEs render the sponsor section with two side-by-side cells.
- Doloffer and Xuanshu API content remain bilingual and correctly linked.
- `python3 scripts/format_readmes.py` runs without error after the edit.
