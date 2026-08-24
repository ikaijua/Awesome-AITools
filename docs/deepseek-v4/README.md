# DeepSeek-V4 Introduction

## What is DeepSeek-V4?

DeepSeek-V4 is DeepSeek's fourth-generation flagship model, released as open weights under the MIT license on Hugging Face. It includes V4-Pro (1.6T MoE, 49B activated) and V4-Flash (284B MoE, 13B activated), both supporting a 1-million-token context and native multimodality.

## Core Capabilities

- **Mixture-of-Experts architecture**: 1.6T total parameters with sparse activation for efficient inference.
- **Long context**: 1M-token context window for long-document and repository-scale tasks.
- **Native multimodality**: handles text, image, and video understanding and generation.
- **Hybrid Attention (CSA + HCA)**: reduces long-context inference FLOPs and KV-cache usage.
- **Three reasoning modes**: Non-think (fast), Think High, and Think Max; Pro-Max leads on coding and agentic benchmarks.

## Access

| Resource | Link |
| --- | --- |
| Hugging Face collection | https://huggingface.co/collections/deepseek-ai/deepseek-v4 |
| DeepSeek chat | https://chat.deepseek.com |
| DeepSeek API | https://platform.deepseek.com |

## Pricing

The model weights are free under MIT. API access is usage-based; V4-Flash offers a lower-cost option while V4-Pro delivers top-tier performance.
