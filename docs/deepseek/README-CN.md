# DeepSeek 介绍

## 什么是 DeepSeek？

DeepSeek（深度求索）是一家领先的 AI 研究公司，在大语言模型（LLM）领域取得了重大突破。他们以高性能、开源权重模型和极具性价比的 API 服务而闻名。DeepSeek 的模型，特别是 V4、V3 和 R1 系列，为开源社区的效率和推理能力树立了新标准。

## 核心模型

### DeepSeek-V4：万亿参数的新境界
DeepSeek-V4 是最新的旗舰系列，实现了大规模参数扩展和原生多模态支持。
- **模型版本**：包含 **V4-Pro**（总参数 1.6 万亿，激活 49B）和 **V4-Flash**（总参数 284B，激活 13B）。
- **100 万超长上下文**：两款模型均标配 1M token 上下文窗口，支持对整个代码仓库进行推理。
- **原生多模态**：原生支持文本、图像、视频和音频的输入与处理。
- **混合注意力机制 (Hybrid Attention)**：结合压缩稀疏注意力 (CSA) 和重压缩注意力 (HCA)，将 KV 缓存效率提升 10 倍。
- **Agent 编程优化**：针对复杂的跨文件编码任务和 Bug 修复进行了深度优化。

### DeepSeek-V3：最强 MoE 模型
DeepSeek-V3 是一款强大的混合专家（MoE）语言模型，总参数量为 671B，每个 token 激活 37B。
- **性能**：在各项基准测试中匹配或超越了 GPT-4o 和 Claude 3.5 Sonnet。
- **效率**：采用了多头潜在注意力（MLA）和 DeepSeek-V3-FP8 训练框架，显著降低了推理和训练成本。
- **训练**：在 14.8 万亿个 token 上进行了预训练，重点加强了代码和数学能力。

### DeepSeek-R1：推理革命
DeepSeek-R1 是一系列推理模型，其性能可与 OpenAI 的 o1 系列相媲美。
- **R1-Zero**：首个证明推理能力可以纯粹通过大规模强化学习（RL）涌现，而无需监督微调（SFT）的模型。
- **R1**：通过少量“冷启动”数据和多阶段训练优化了推理过程，产出更具可读性和稳定性的“思维链”（CoT）。
- **蒸馏模型**：DeepSeek 还发布了基于 Llama 和 Qwen 的 R1 蒸馏版本（从 1.5B 到 70B），将先进的推理能力带到了更小的硬件上。

## 核心特性

### 1. 卓越的推理能力
DeepSeek-R1 和 V4-Pro 在复杂的逻辑、数学和编程任务中表现出色。它可以花更多时间“思考”（生成内部思维链），解决传统 LLM 难以应对的难题。

### 2. 极高的性价比
DeepSeek 的 API 价格显著低于竞争对手（通常仅为 GPT-4o/Claude 3.5 的 1/10 到 1/20），是开发者和大规模 Agent 工作流的首选。

### 3. 开源透明
与许多“黑盒”商业模型不同，DeepSeek 发布了详细的技术报告，并以 MIT 许可证发布模型权重，促进了全球 AI 社区的创新。

### 4. 代码与数学专家
DeepSeek 模型在代码基准测试（HumanEval）和数学竞赛（AIME, MATH）中始终处于顶尖水平，非常适合 AI 辅助软件工程。

## 如何使用 DeepSeek

### 1. 官方网页与 App
- **DeepSeek Chat**: [chat.deepseek.com](https://chat.deepseek.com/)
- 已在 iOS 和 Android 商店上架。

### 2. API 集成
DeepSeek 提供兼容 OpenAI 的 API，可以轻松集成到现有工具中。
- **Base URL**: `https://api.deepseek.com`
- **开发者平台**: [platform.deepseek.com](https://platform.deepseek.com/)

### 3. 与 AI 编程工具集成
DeepSeek 模型被广泛用作以下工具的后端：
- **Aider**: 使用 `deepseek/deepseek-chat` 或 `deepseek/deepseek-reasoner`。
- **Cursor**: 添加 DeepSeek 作为自定义模型。
- **Cline/Roo Code**: 通过 OpenRouter 或 direct API 支持。
- **Claude Code**: 可以通过 `claude-code-router` 等代理进行路由。

## 技术突破

- **MLA (Multi-head Latent Attention)**：优化 KV 缓存，加速推理。
- **混合注意力机制 (Hybrid Attention)**：V4 引入的世界首创技术，大幅降低长上下文下的 KV 缓存占用。
- **DeepSeekMoE**：专为高性能混合专家模型设计的架构。
- **FP8 训练**：首次在 600B+ 参数模型上成功实现大规模 FP8 训练。
- **GRPO (Group Relative Policy Optimization)**：一种高效的强化学习算法，无需评论员（Critic）模型，大幅节省计算资源。

## 相关资源

- [官方网站](https://www.deepseek.com/)
- [DeepSeek-V4 Hugging Face 集合](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
- [DeepSeek-V3 GitHub](https://github.com/deepseek-ai/DeepSeek-V3)
- [DeepSeek-R1 GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

## 许可证

DeepSeek 模型采用 MIT 许可证发布，允许商业使用和修改。
