# Muse Glimmer 简介

## 什么是 Muse Glimmer？

Muse Glimmer 是 Meta Superintelligence Labs 于 2026 年 8 月 10 日发布的 300 亿参数开源多模态模型，专为在本地消费级硬件上运行的自主智能体任务而设计。这也是 Meta 自转向专有 Muse Spark 模型家族以来，首个以宽松 Apache 2.0 许可发布的模型。

## 核心特性

- **本地优先的智能体模型**：面向单张 24–32 GB 消费级显卡或 Apple Silicon Mac 上的常驻 Agent。
- **多模态输入**：通过约 18 亿参数的 ViT-G/14 感知编码器，支持交错的文本与图像输入。
- **长上下文**：支持 131,072+ token 上下文，适合长时程 Agent 会话和长文档分析。
- **工具调用与推理**：针对规划、函数调用、故障恢复和多步骤任务执行进行训练。
- **量化版本**：提供 BF16 全精度权重，以及两个 4-bit 量化版本（K-Quant-17GB 面向 24 GB 显存，K-Quant-Dynamic 面向 32 GB 显存）。
- **DFlash 投机解码**：附带轻量级 draft 模型，通过一次性预测 16 个 token 块并验证来加速生成。
- **多运行时支持**：发布首日即支持 Ollama、LM Studio、Unsloth、llama.cpp、ExecuTorch、MLX、vLLM 和 SGLang。

## 快速开始

从 Hugging Face 下载权重后，用你喜欢的本地推理框架加载：

```bash
# vLLM 示例
vllm serve "meta-models/Muse-Glimmer-30B"

# SGLang 示例
python3 -m sglang.launch_server --model-path "meta-models/Muse-Glimmer-30B"
```

如需量化本地推理，请参考 Hugging Face 模型页面上的 GGUF 或 ExecuTorch PTE 说明。

## 模型卡要点

| 属性 | 数值 |
| --- | --- |
| 总参数量 | 约 296 亿 |
| 感知编码器 | 约 18 亿参数 ViT-G/14 |
| 上下文长度 | 131,072+ |
| 许可协议 | Apache 2.0 |
| 支持模态 | 文本+图像输入，文本输出 |
| 知识截止 | 2026-01-04 |

## 相关资源

- [Hugging Face 模型卡](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [Ars Technica 发布报道](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/)
- [Hugging Face 博客](https://huggingface.co/blog)

## 许可证

Muse Glimmer 的权重、量化版本、投机解码 draft 和感知编码器均采用 Apache 2.0 许可发布。
