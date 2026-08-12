# Design: Add Muse Glimmer and Muse Code to Awesome-AITools

## Goal
Add Meta's newly open-sourced **Muse Glimmer** model and the accompanying **Muse Code** terminal coding agent to the Awesome-AITools bilingual list.

## Background
On 2026-08-10, Meta Superintelligence Labs released **Muse Glimmer**, a 30B-parameter open-weight multimodal model under the Apache 2.0 license. It is optimized for local agentic workflows and can run on consumer GPUs (24–32 GB VRAM) via 4-bit quantized variants. The model supports ~131K context, text/image input, tool use, and DFlash speculative decoding, and was distilled from Meta's larger Muse Spark model.

On 2026-08-05, Meta released **Muse Code**, a beta terminal coding agent powered by Muse Spark 1.2. It targets large-repo software engineering tasks with persistent async background agents, parallel subagents in isolated worktrees, and an append-only local event log for crash recovery.

## Category Decision

- **Muse Glimmer** fits the existing **Open Source LLMs** / **开源大语言模型** section, alongside Llama 3, Gemma 4, Qwen3, etc.
- **Muse Code** fits the existing **AI Agent** / **AI Agent** section, alongside Claude Code, Codex, Kimi Code, and Grok Build.

## Changes

### 1. README.md

#### Open Source LLMs
Insert a new row after **Gemma 4** and before **Llama 3**:

```markdown
| Muse Glimmer | Meta's 30B-parameter open-weight multimodal model for local agents, released under Apache 2.0. Features ~131K context, text/image input, tool use, 4-bit quantized variants for 24–32 GB VRAM, and DFlash speculative decoding. Distilled from Muse Spark. | [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B) [Ars Technica coverage](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/) | Free |
```

#### AI Agent
Insert a new row immediately after **Kimi Code**:

```markdown
| Muse Code | Meta's beta terminal coding agent powered by Muse Spark 1.2. Plans changes, writes code, and validates results across large repos using persistent async background agents and an append-only event log. macOS/Linux; pay-as-you-go with an optional Contributor tier that exchanges lower pricing for training-data permission. | [URL](https://www.meta.ai/muse/code) [VentureBeat coverage](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents) | Free/Paid |
```

### 2. README-CN.md

#### 开源大语言模型
在 **Gemma 4** 之后、**Llama 3** 之前插入新行：

```markdown
| Muse Glimmer | Meta 开源的 300 亿参数多模态本地智能体模型，采用 Apache 2.0 许可。支持约 13.1 万 token 上下文、文本/图像输入、工具调用，4-bit 量化后可在 24–32 GB 显存的消费级显卡上运行，并配备 DFlash 投机解码。由 Muse Spark 蒸馏而来。 | [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B) [Ars Technica 报道](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/) | 免费 |
```

#### AI Agent
在 **Kimi Code** 之后立即插入新行：

```markdown
| Muse Code | Meta 推出的基于终端的 AI 编程智能体（Beta），由 Muse Spark 1.2 驱动。支持跨大型代码库的规划、编写代码与验证结果，具备持久异步后台代理和只读追加的本地事件日志，可在崩溃后恢复。支持 macOS/Linux；按量付费，另有 Contributor 档位以允许使用提示/补全训练来换取更低价格。 | [URL](https://www.meta.ai/muse/code) [VentureBeat 报道](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents) | 免费/付费 |
```

### 3. CHANGELOG.md
Add new bullets under `## August 2026`:

```markdown
- Added Muse Glimmer (meta-models/Muse-Glimmer-30B) to Open Source LLMs section (both EN/CN)
- Added Muse Code to AI Agent section (both EN/CN)
```

### 4. Deep-dive documentation
No `docs/<slug>/` page is required. Both entries are recent product/model releases best described by upstream links and short table descriptions.

## Verification
After editing:
1. Run `python3 scripts/format_readmes.py` to normalize tables and anchors.
2. If `lychee .` is available, run it to verify the new links.
3. If the `meta.ai` product link fails link checking due to bot challenges, add `meta.ai` to `.lycheeignore`.
4. Visually confirm both new rows appear in both READMEs with matching structure and bilingual consistency.

## Out of Scope
- No changes to the existing Llama 3 row.
- No new `docs/<slug>/` deep-dive pages.
- No sponsor or asset changes.
