# Superpowers 简介

## 什么是 Superpowers？

Superpowers 是一套面向编码代理的完整软件开发方法论，基于一组可组合技能和会话启动指令构建。它由 Jesse Vincent 和 Prime Radiant 团队创建，可将 Claude Code、Codex、Cursor、Kimi Code、OpenCode、Antigravity、GitHub Copilot CLI 和 Pi 等代理转变为系统化的工程搭档。

启用 Superpowers 后，代理不会直接开始写代码，而是先与你一起完善规格说明，获得你的确认后再编写详细的实现计划，并通过测试驱动、评审驱动的工作流执行。技能会自动触发，因此代理"自带 Superpowers"，无需手动提示。

## 核心理念

### 先规格，后代码
每个任务都从理解你真正想构建的东西开始。代理会提出澄清问题、探索替代方案，并以短小、可Review的段落呈现设计方案。

### 测试驱动开发（TDD）
Superpowers 严格执行 RED-GREEN-REFACTOR 循环：先编写失败的测试，观察其失败，编写最少量代码使其通过，然后进行重构。测试之前编写的代码会被删除。

### 系统化而非随意化
调试、规划和代码审查等都通过结构化技能处理，而不是即兴发挥。目标是"用事实验证，而非空口宣称"。

### 子代理驱动开发
计划获批后，代理会派遣子代理逐个执行任务，检查其输出，进行两阶段评审（规格符合性、代码质量），并可长时间自主推进。

## 核心技能

| 技能 | 用途 |
| --- | --- |
| `brainstorming` | 通过苏格拉底式提问细化想法，并以分段形式呈现设计方案供确认。 |
| `writing-plans` | 将获批设计拆分为可执行的小任务，包含确切文件路径和验证步骤。 |
| `using-git-worktrees` | 创建隔离分支、运行项目初始化并验证干净的测试基线。 |
| `subagent-driven-development` / `executing-plans` | 通过子代理或带人工检查点的批量方式执行任务。 |
| `test-driven-development` | 强制执行 RED-GREEN-REFACTOR 并识别测试反模式。 |
| `systematic-debugging` | 四阶段根因分析，并在完成前进行验证。 |
| `requesting-code-review` | 对照计划评审工作，并按严重级别报告问题。 |
| `finishing-a-development-branch` | 验证测试，提供合并/PR/保留/丢弃选项，并清理 worktree。 |
| `writing-skills` | 按照项目最佳实践创建新技能。 |

## 支持的代理平台

Superpowers 可作为插件或包安装到以下平台：

- Claude Code
- Antigravity
- Codex App / Codex CLI
- Cursor
- Factory Droid
- GitHub Copilot CLI
- Kimi Code
- OpenCode
- Pi

## 快速开始

### Kimi Code

```bash
/plugins install https://github.com/obra/superpowers
```

或从 Kimi Code 插件市场安装。

### Claude Code

```bash
/plugin install superpowers@claude-plugins-official
```

其他平台请参考仓库中的[安装说明](https://github.com/obra/superpowers#installation)。

## 基本工作流

1. **头脑风暴** — 细化目标并产出设计文档。
2. **确认设计** — 逐段Review并确认。
3. **制定计划** — 生成任务级实现计划。
4. **执行** — 通过子代理或检查点执行任务。
5. **评审** — 在任务间检查规格符合性和代码质量。
6. **收尾** — 验证测试并决定合并、提PR、保留或丢弃。

## 最佳实践

1. **从清晰的目标开始** — 初始问题描述越清楚，生成的规格说明越好。
2. **认真Review设计段落** — 不要跳过确认检查点，它们能保持代理不跑偏。
3. **让测试引领实现** — 克制住先写实现的冲动。
4. **使用 git worktree** — 将实验性工作与主分支隔离。
5. **检查子代理输出** — 关键评审问题会阻塞进度，这是有意为之。

## 相关资源

- [GitHub 仓库](https://github.com/obra/superpowers)
- [发布声明](https://primeradiant.com/superpowers/)
- [Issues](https://github.com/obra/superpowers/issues)
- [社区 Discord](https://discord.gg/superpowers)

## 许可证

Superpowers 基于 MIT 许可证开源。
