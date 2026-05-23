# ml-intern 入门介绍

## 什么是 ml-intern？

`ml-intern` 是由 Hugging Face 开发的一款开源、自主的 AI Agent，定位为专业的 **机器学习工程师 (Machine Learning Engineer)**。它旨在处理机器学习任务的端到端全生命周期，从初始研究到模型部署。

## 核心理念

### 专业化的 ML 工程
与通用的编程助手不同，`ml-intern` 专门针对机器学习工作流进行了优化。它理解数据处理、模型训练和评估中的各种细节。

### 深度生态集成
`ml-intern` 拥有与 Hugging Face Hub（数据集、模型、Spaces）、文档以及计算任务交互的内置工具，使其成为 HF 生态系统中研究人员和开发者的强大伙伴。

### 自主研究能力
它可以浏览网页、搜索 GitHub 并阅读学术论文 (PDF)，从而为编码决策提供信息，并与最新研究保持同步。

## 核心功能

### 自主任务执行
- 根据学术论文提出假设。
- 编写高质量的 ML 代码（训练脚本、评估循环）。
- 运行实验并跟踪结果。
- 直接将模型和数据集部署到 Hugging Face。

### 高级代理逻辑
- **死循环检测器 (Doom Loop Detector)**：检测 Agent 是否陷入重复循环，并注入纠正性提示。
- **自动压缩 (Auto-Compaction)**：自动管理长会话上下文，确保 LLM 窗口中保留最相关的信息。
- **可追溯性**：会话会自动上传到私有的 HF 数据集，以便通过 HF Agent Trace Viewer 进行调试和审计。

### 多模型支持
- 支持 Claude (Anthropic)、GPT (OpenAI) 以及通过 Ollama、vLLM 或 LM Studio 运行的本地模型。

## 快速入门

### 安装

请确保已安装 [uv](https://github.com/astral-sh/uv)。

```bash
# 克隆仓库
git clone https://github.com/huggingface/ml-intern.git
cd ml-intern

# 同步依赖
uv sync

# 安装 CLI 工具
uv tool install -e .
```

### 配置

设置环境变量（在 `.env` 文件或 shell 中）：

```bash
export ANTHROPIC_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
export HF_TOKEN="your-huggingface-token"
export GITHUB_TOKEN="your-github-token"
```

### 基本用法

```bash
# 启动交互模式
ml-intern

# 以无头模式运行单个任务
ml-intern "在 CIFAR-10 数据集上微调 ResNet 模型"

# 指定特定模型
ml-intern --model anthropic/claude-3-5-sonnet-latest "你的提示词"
```

## 相关资源

- [GitHub 仓库](https://github.com/huggingface/ml-intern)
- [Hugging Face Hub](https://huggingface.co/)
- [HF Agent Trace Viewer](https://huggingface.co/spaces/huggingface/agent-trace-viewer)

## 许可证

`ml-intern` 是 Hugging Face 的开源项目。请遵守其许可条款以及你所使用的 LLM 提供商的服务条款。
