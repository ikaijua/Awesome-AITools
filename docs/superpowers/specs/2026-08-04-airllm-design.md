# Design: Add AirLLM to Awesome-AITools

## Goal
Add the open-source project [lyogavin/airllm](https://github.com/lyogavin/airllm) to the Awesome-AITools bilingual list.

## Background
AirLLM is a Python library that reduces LLM inference memory usage by loading only one layer at a time. It enables running very large open-weight models on consumer GPUs, e.g. 70B models on 4GB VRAM, 405B on 8GB, and 671B DeepSeek-V3 on ~12GB. It supports a wide range of models (Llama, Qwen, DeepSeek, Mistral, Phi, Gemma, ChatGLM, Kimi K3, etc.) through a single `AutoModel.from_pretrained(...)` interface and offers optional 4-bit/8-bit block-wise quantization.

The project has been actively maintained since November 2023 and supports current flagship models.

## Category Decision
The existing READMEs do not have a section dedicated to inference or deployment tooling. After review, the best fit is a new category rather than forcing AirLLM into "Open Source LLMs" (which is for model weights) or "LLM training platform" (which is for training/serving platforms).

- English name: **LLM Inference & Deployment**
- Chinese name: **LLM 推理与部署**

The new section will be placed immediately after the existing **LLM training platform** / **大语言模型训练-评估平台** section in both READMEs.

## Changes

### 1. README.md
- Add `### LLM Inference & Deployment` to the Table of Contents under `## All Categories`.
- Insert the new section after `### LLM training platform` and before `### Writing`.
- Section content:

```markdown
### LLM Inference & Deployment
| Name | Description | Links | Fees |
| --- | --- | --- | --- |
| AirLLM | A Python library that reduces LLM inference memory usage by loading one layer at a time, enabling 70B models on 4GB GPUs, 405B on 8GB, and 671B DeepSeek-V3 on ~12GB. Supports 4-bit/8-bit quantization and a wide range of open models via a single AutoModel interface. | [Github](https://github.com/lyogavin/airllm) ![GitHub Repo stars](https://img.shields.io/github/stars/lyogavin/airllm?style=social) | Free |
```

### 2. README-CN.md
- Add `### LLM 推理与部署` to the Table of Contents under `## 全部分类`.
- Insert the new section after `### 大语言模型训练-评估平台` and before `### 阅读`.
- Section content:

```markdown
### LLM 推理与部署
| 名称 | 说明 | 链接 | 费用 |
| --- | --- | --- | --- |
| AirLLM | 通过逐层加载大幅降低大语言模型推理显存占用的 Python 库，可在 4GB 显存上运行 70B 模型、8GB 上运行 405B 模型、约 12GB 上运行 671B 的 DeepSeek-V3。支持 4 位/8 位量化，并通过统一的 AutoModel 接口支持众多开源模型。 | [Github](https://github.com/lyogavin/airllm) ![GitHub Repo stars](https://img.shields.io/github/stars/lyogavin/airllm?style=social) | 免费 |
```

### 3. CHANGELOG.md
Add a new bullet under `## August 2026`:

```markdown
- Added AirLLM (lyogavin/airllm) to new LLM Inference & Deployment section (both EN/CN)
```

### 4. Deep-dive documentation
No `docs/<slug>/` page is required for this entry. AirLLM is a library with extensive upstream documentation; a short table entry is sufficient.

## Verification
After editing:
1. Run `python3 scripts/format_readmes.py` to normalize tables and anchors.
2. Run `lychee .` (if available) to verify the new GitHub link.
3. Visually confirm that the new section appears in both READMEs with matching structure and links.

## Out of Scope
- No changes to existing tool entries.
- No new docs/ deep-dive page.
- No sponsor or asset changes.
