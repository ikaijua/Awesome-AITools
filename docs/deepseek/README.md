# DeepSeek Introduction

## What is DeepSeek?

DeepSeek is a leading AI research company (DeepSeek-AI) that has made significant breakthroughs in Large Language Models (LLMs). They are known for their high-performance, open-weights models and extremely cost-effective API services. DeepSeek's models, particularly the V4, V3 and R1 series, have set new standards for efficiency and reasoning capabilities in the open-source community.

## Core Models

### DeepSeek-V4: The Trillion-Parameter Frontier
DeepSeek-V4 is the latest flagship series featuring massive scaling and native multimodality.
- **Models**: Includes **V4-Pro** (1.6 Trillion total parameters, 49B active) and **V4-Flash** (284B total parameters, 13B active).
- **1-Million Context**: Standard 1M token context window across both models for repository-level reasoning.
- **Native Multimodality**: Built-in support for text, images, video, and audio.
- **Hybrid Attention**: Combines Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) for 10x KV cache efficiency.
- **Agentic Coding**: Optimized for complex multi-file coding tasks and bug fixing.

### DeepSeek-V3: The Strongest MoE Model
DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters, of which 37B are activated for each token.
- **Performance**: Matches or exceeds GPT-4o and Claude 3.5 Sonnet on various benchmarks.
- **Efficiency**: Multi-head Latent Attention (MLA) and DeepSeek-V3-FP8 training framework significantly reduce inference and training costs.
- **Training**: Pre-trained on 14.8 trillion tokens with a focus on code and math.

### DeepSeek-R1: The Reasoning Revolution
DeepSeek-R1 is a series of reasoning models that achieve performance comparable to OpenAI's o1 series.
- **R1-Zero**: The first model to demonstrate that reasoning capabilities can emerge purely through large-scale Reinforcement Learning (RL) without Supervised Fine-Tuning (SFT).
- **R1**: Refines the reasoning process with a small amount of "cold-start" data and multi-stage training, resulting in more readable and stable "Chain of Thought" (CoT) outputs.
- **Distilled Models**: DeepSeek also released distilled versions of R1 based on Llama and Qwen (from 1.5B to 70B parameters), bringing advanced reasoning to smaller hardware.

## Key Features

### 1. Exceptional Reasoning
DeepSeek-R1 and V4-Pro excel in complex logic, mathematics, and programming tasks. They can spend more time "thinking" (generating internal CoT) to solve difficult problems that stump traditional LLMs.

### 2. High Performance-to-Cost Ratio
DeepSeek's API is significantly cheaper than competitors (often 1/10th to 1/20th the price of GPT-4o/Claude 3.5), making it the top choice for developers and large-scale agentic workflows.

### 3. Open-Source & Transparent
Unlike many "black-box" proprietary models, DeepSeek publishes detailed technical reports and releases model weights under the MIT license, fostering innovation in the global AI community.

### 4. Code & Math Expertise
DeepSeek models are consistently top-tier in coding benchmarks (HumanEval) and math competitions (AIME, MATH), making them ideal for AI-powered software engineering.

## How to Use DeepSeek

### 1. Official Web & App
- **DeepSeek Chat**: [chat.deepseek.com](https://chat.deepseek.com/)
- Available on iOS and Android.

### 2. API Integration
DeepSeek provides an OpenAI-compatible API, allowing it to be easily integrated into existing tools.
- **Base URL**: `https://api.deepseek.com`
- **Platform**: [platform.deepseek.com](https://platform.deepseek.com/)

### 3. Integration with AI Coding Tools
DeepSeek models are widely used as backends for:
- **Aider**: Use `deepseek/deepseek-chat` or `deepseek/deepseek-reasoner`.
- **Cursor**: Add DeepSeek as a custom model.
- **Cline/Roo Code**: Supported via OpenRouter or direct API.
- **Claude Code**: Can be routed via proxies like `claude-code-router`.

## Technical Breakthroughs

- **Multi-head Latent Attention (MLA)**: Optimizes KV cache and speeds up inference.
- **Hybrid Attention (CSA + HCA)**: World-first innovation in V4 that drastically reduces KV cache requirements for long context.
- **DeepSeekMoE**: Specialized architecture for high-performance Mixture-of-Experts.
- **FP8 Training**: First large-scale successful implementation of FP8 training for 600B+ parameter models.
- **Group Relative Policy Optimization (GRPO)**: An efficient RL algorithm that eliminates the need for a critic model, saving significant compute.

## Related Resources

- [Official Website](https://www.deepseek.com/)
- [DeepSeek-V4 Collection (Hugging Face)](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
- [DeepSeek-V3 GitHub](https://github.com/deepseek-ai/DeepSeek-V3)
- [DeepSeek-R1 GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

## License

DeepSeek models are released under the MIT License, allowing for commercial use and modification.
