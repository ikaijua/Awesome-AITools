# Antigravity 简介

## 什么是 Antigravity？

Antigravity 是 Google 推出的"以智能体为先"的 AI 编程平台，围绕 Gemini 3 系列模型构建。它与 Gemini 3 一同发布，以深度改造过的、基于 VS Code 的 IDE 形态交付（常被视为 Windsurf 的接任者 / 衍生产品），让开发者把端到端的软件任务交给自主智能体执行，而不仅仅是行内补全。

> ℹ️ Antigravity 是 Google 在智能体化编程方向上的新主推产品，用于替代正在被废弃的 Gemini CLI。原 Gemini CLI 的能力被吸纳进 Antigravity 更完整的智能体工作流中。

## 核心思想

### 以智能体为先，而非补全为先
Antigravity 把开发者定位成"智能体的管理者"：
- 工作的最小单元是任务或计划，不是按键
- 智能体可以直接使用编辑器、终端和内置浏览器
- 每次智能体运行都会产出**可核验的 Artifacts**（任务清单、实施计划、截图、浏览器录屏），方便人工在接受前进行核对

### 两种内置视图
- **Editor 视图**：类 VS Code 的 IDE，附带智能体侧边栏，用于贴近代码的协作
- **Manager 视图**：用于在多个工作区、多个智能体之间分发与并行编排任务

### 多模型，以 Gemini 为中心
开箱即用可选：
- Gemini 3 Pro（默认，预览期提供宽松速率限制）
- Gemini 3 Flash
- Anthropic Claude Sonnet 4.6 / Claude Opus 4.6
- GPT-OSS-120B

### 可核验的产出
- 通过 Artifacts（计划、截图、录屏）让智能体的运行可审计
- 智能体会跨会话积累项目相关的"经验"，而不是每次都从零开始

## 核心功能

### 自主编程智能体
- 多步任务执行：规划 → 编辑 → 运行 → 验证
- 支持跨文件、跨仓库的并行智能体协作
- 适合长链路重构与迁移，而不只是单段代码修改

### 内置浏览器控制
- 智能体可以驱动真实浏览器去验证自己的修改
- 自动捕获截图与录屏作为行为证据

### 项目记忆与学习
- 跨智能体运行携带项目上下文
- 会从历史交互（包括你提出的修正）中学习

### IDE 集成
- 大多数开发者熟悉的 VS Code 式编辑体验
- 终端、源代码管理、扩展等如常工作

## 快速开始

### 下载

Antigravity 以桌面 IDE 形式发布（目前为公开预览，预览期免费）。从官网获取：

- <https://antigravity.google/>

系统要求：
- Windows 10 64 位 及以上
- macOS Monterey (12) 及以上
- 64 位 Linux（较新的 glibc / glibcxx）

### 登录与选择模型

1. 启动 Antigravity，使用 Google 账号登录
2. 选择默认模型——Gemini 3 Pro 是不错的起点
3. 打开一个工作区，进入 **Editor 视图** 开始编码，或切换到 **Manager 视图** 编排多智能体任务

### 典型工作流

1. 用自然语言描述任务（例如"为 `auth/` 目录补单元测试"、"把这个服务从 REST 迁到 gRPC"）
2. 智能体先产出一份**计划 Artifact** 供你确认
3. 智能体编辑文件、在终端中执行命令，必要时驱动浏览器进行验证
4. 审阅 diff 与 Artifacts（截图、录屏、日志），接受或继续迭代

## 常见场景

### 长链路重构
把多文件的重构任务交给智能体，自己只需评审它产出的计划和 diff，而不必逐处手改。

### 端到端特性开发
从规格 → 实现 → 测试 → 浏览器中验证的 UI 变更，全部由一个或多个智能体在同一工作区内推进。

### 并行任务流
用 Manager 视图同时跑多个智能体处理不同任务/分支，结果通过 Artifacts 集中查看。

## 最佳实践

1. **任务描述要清晰** —— 提示越具体，规划越靠谱
2. **看 Artifact，不只是看 diff** —— 截图和录屏能暴露 diff 无法体现的行为问题
3. **让智能体自己去验证** —— 授权它运行测试、驱动浏览器，可核验的产出才是目标
4. **把修正反馈进去** —— Antigravity 会跨运行学习，明确的反馈会越用越值钱

## 相关资源

- [Antigravity 官网](https://antigravity.google/)
- [Wikipedia：Google Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity)
- [与其他工具对比](../COMPARISON-CN.md)

## 许可证

Antigravity 是 Google 的专有产品。当前为公开预览期，免费使用，对内置的 Gemini 3 Pro 提供较宽松的速率限制。使用须遵循 Google 服务条款。
