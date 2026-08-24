# DeepSeek-V4 介绍

## DeepSeek-V4 是什么？

DeepSeek-V4 是 DeepSeek 第四代旗舰模型，以 MIT 许可在 Hugging Face 发布开源权重。它包括 V4-Pro（1.6T MoE，激活 49B）和 V4-Flash（284B MoE，激活 13B）两个版本，均支持 100 万 token 上下文和原生多模态。

## 核心能力

- **混合专家（MoE）架构**：1.6T 总参数，稀疏激活实现高效推理。
- **超长上下文**：100 万 token 上下文窗口，适用于长文档和仓库级任务。
- **原生多模态**：处理文本、图像和视频的理解与生成。
- **混合注意力机制（CSA + HCA）**：降低长上下文推理的 FLOPs 和 KV 缓存占用。
- **三档推理模式**：Non-think（快速）、Think High 和 Think Max；Pro-Max 在编码与智能体基准上领先。

## 访问方式

| 资源 | 链接 |
| --- | --- |
| Hugging Face 集合 | https://huggingface.co/collections/deepseek-ai/deepseek-v4 |
| DeepSeek 聊天 | https://chat.deepseek.com |
| DeepSeek API | https://platform.deepseek.com |

## 费用

模型权重按 MIT 许可免费；API 按用量计费，V4-Flash 成本更低，V4-Pro 提供顶级性能。
