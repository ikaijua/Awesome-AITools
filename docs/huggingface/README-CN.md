# Hugging Face 入门介绍

## Hugging Face 是什么？

[Hugging Face](https://huggingface.co/) 是领先的开源 AI 平台与社区。它最初是一家聊天机器人公司，后来发展成为开源机器学习的中心枢纽，托管模型、数据集、Spaces 演示，并提供丰富的工具库生态，支持模型发现、训练、微调和部署。

## 核心定位

### 模型中心（Model Hub）
[Hugging Face Hub](https://huggingface.co/models) 托管超过 100 万个公开模型，涵盖大语言模型、视觉、音频、多模态和领域专用任务。它是 Meta、Google、阿里、DeepSeek、Moonshot、Mistral 等众多厂商发布开源权重模型的默认渠道。

### 数据集与评测
[Hugging Face Datasets](https://huggingface.co/datasets) 提供数十万个即用型数据集，[Evaluate](https://huggingface.co/docs/evaluate/index) 和各类[排行榜](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)帮助在公开任务上评测模型。

### Spaces 与演示
[Spaces](https://huggingface.co/spaces) 让任何人都能通过 Git 仓库直接托管交互式 ML 演示，通常基于 Gradio 或 Streamlit 构建。它是分享和试用新模型最快捷的方式之一。

### 核心工具库
- **Transformers** — 使用 Transformer 模型的事实标准库。
- **Diffusers** — 扩散模型与生成式 AI 工具。
- **Datasets** — 高效的数据加载与处理。
- **Accelerate** — 简化的多 GPU 与分布式训练。
- **TRL / PEFT** — 微调与参数高效适配。
- **Text Generation Inference (TGI)** 和 **Inference API / Endpoints** — 生产级推理服务。

## 快速开始

### 安装核心库

```bash
pip install transformers datasets accelerate
```

### 下载并运行模型

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("Hugging Face 让开源 AI 变得简单易用。"))
```

### 在 Spaces 上托管演示

访问 [huggingface.co/new-space](https://huggingface.co/new-space) 创建新 Space，推送 Gradio 或 Streamlit 应用，即可分享 URL。

## 相关资源

- [Hugging Face 官网](https://huggingface.co/)
- [GitHub 组织](https://github.com/huggingface)
- [官方文档](https://huggingface.co/docs)
- [Models](https://huggingface.co/models)
- [Datasets](https://huggingface.co/datasets)
- [Spaces](https://huggingface.co/spaces)

## 许可证

Hugging Face 平台服务和工具库采用多种开源许可证；具体模型和数据集各有其独立许可证。
