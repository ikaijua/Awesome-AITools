# Qwen README Update Design

## Objective

Update the Qwen / 通义千问 chatbot entry in both `README.md` and `README-CN.md` to reflect the latest Qwen3.8-Max model available in Qwen Chat.

## Background

- The repository maintains bilingual EN/CN README files with mirrored category structure and 4-column tables.
- Current Qwen chatbot entry mentions `Qwen 3.7-Plus/Max`.
- `chat.qwen.ai` now highlights `Qwen3.8-Max` as the latest model.
- Official/community sources describe Qwen3.8-Max as a 2.4T-parameter MoE model with native multimodality and 1M-token context.

## Proposed Changes

### Files Affected

- `README.md`
- `README-CN.md`

### Detailed Changes

#### `README.md` (AI Chatbots section)

Update the `qwen` row from:

```markdown
| qwen | Alibaba's AI chatbot. Includes Qwen 3.7-Plus/Max in Qwen Chat, supporting 1M context window, native multimodality, and long-horizon agentic reasoning. |[URL](https://chat.qwen.ai/)|Free|
```

To:

```markdown
| qwen | Alibaba's AI chatbot. Qwen Chat now runs on Qwen3.8-Max, a 2.4T-parameter MoE model with native multimodality, 1M-token context window, and long-horizon agentic reasoning. |[URL](https://chat.qwen.ai/)|Free|
```

#### `README-CN.md`（AI 聊天机器人分类）

Update the `通义千问` row from:

```markdown
| 通义千问 |阿里的大语言模型。 <br> Qwen Chat 可体验 Qwen3.7-Plus/Max 等最新模型，支持 100 万超长上下文、原生多模态以及长链路 Agent 推理，并提供深度研究选项。|[URL](https://chat.qwen.ai/)|免费|
```

To:

```markdown
| 通义千问 |阿里的大语言模型。 <br> Qwen Chat 已升级至 Qwen3.8-Max，2.4T 参数 MoE 架构，支持 100 万超长上下文、原生多模态、长链路 Agent 推理与深度研究。|[URL](https://chat.qwen.ai/)|免费|
```

## Out of Scope

- The `Qwen3` entry in the Open Source LLMs / 开源 LLMs section remains unchanged.
- No new `docs/qwen/` deep-dive pages will be created.
- No new tool entries (e.g., Qwen Code) will be added.

## Verification

1. Run `python3 scripts/format_readmes.py` to normalize table formatting in both READMEs.
2. Optionally run `lychee .` to verify that the existing `chat.qwen.ai` link is still reachable.

## References

- Qwen Chat: https://chat.qwen.ai/
- Qwen official blog: https://qwenlm.github.io/blog/
