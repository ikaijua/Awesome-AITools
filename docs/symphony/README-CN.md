# Symphony 介绍

## 什么是 Symphony？

[Symphony](https://github.com/openai/symphony) 是 OpenAI 开源的**项目需求到交付 harness**。它将项目工作转化为隔离、自主的实施运行，让团队从“监督编码代理”转向“管理工作”。

与传统编码代理不同，Symphony 会监听工作看板（如 Linear），自动派发代理处理任务，并在提交 PR 前收集 CI 状态、审查反馈、复杂度分析和演示视频等工作证明，最终由工程师决定是否合并。人类工程师专注于目标和审查，执行过程由系统负责。

## 核心定位

### 从编码代理到工作管理
Symphony 代表了从“管理编码代理”到“管理工作”的范式转变。harness 负责任务生命周期、上下文、验证和交付，人类工程师只需把握高层方向。

### 隔离、自主的运行
每个任务都在隔离的实施环境中运行。代理自主规划、编码、测试和汇报，任何变更在落地前都必须通过检查点和验证门。

### 与现有工具兼容
Symphony 旨在与现有编码代理工具协同工作，而不是替代 Claude Code、Codex 或 Cursor；它围绕真实项目工作流编排这些工具。

## 核心功能

- **工作看板集成** — 监听 Linear 等任务跟踪器，自动启动实施运行。
- **自主 PR 生命周期** — 生成分支、提交、Pull Request，并在验证后合并。
- **工作证明** — 为每次变更收集 CI 状态、审查反馈、复杂度分析和演示视频。
- **人工审批** — 工程师审查结果后决定是否合并。
- **两种实现方式** — 基于开源规范自行实现 harness，或使用实验性 Elixir 参考实现。
- **代理无关** — 兼容现有编码代理和工具链。

## 快速开始

> **注意：** Symphony 目前处于低调的工程预览阶段，OpenAI 建议仅在可信环境中测试。

### 方式一：使用实验性 Elixir 参考实现

```bash
git clone https://github.com/openai/symphony.git
cd symphony
# 按照仓库中的 Elixir 参考实现说明完成 setup
```

### 方式二：基于开源规范自行实现

阅读仓库中的 [Symphony 规范](https://github.com/openai/symphony)，按照自己的技术栈实现 harness。

## 最佳实践

1. **从可信代码库开始** — 预览版软件应在错误可恢复的仓库上运行。
2. **明确任务边界** — 范围清晰的 Issue 和 Ticket 能带来更可靠的自主运行。
3. **保留 CI 和审查门控** — 合并前保持人工审批和自动化检查。
4. **定期检查代理输出** — 经常审查工作证明产物，尽早发现潜在错误。
5. **使用隔离环境** — 尽可能在沙箱或受限 CI 环境中运行代理。

## 安全提示

Symphony 能够读取代码库上下文、执行测试、开启 Pull Request 并合并代码。请仅授予其必要权限，启用分支保护规则，并审查每一次合并的变更。

## 相关资源

- [GitHub 仓库](https://github.com/openai/symphony)
- [OpenAI Codex](https://github.com/openai/codex) — Symphony 可编排的编码代理
- [Linear](https://linear.app/) — 参考实现支持的工作看板示例

## 许可证

Symphony 使用其 [GitHub 仓库](https://github.com/openai/symphony) 中指定的许可证。
