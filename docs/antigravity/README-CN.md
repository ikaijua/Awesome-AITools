# Antigravity 简介

## 什么是 Antigravity？

Antigravity（当前版本为 Antigravity 2.0）是 Google 推出的以智能体为先的 AI 编程平台，用于替代已被废弃的 Gemini CLI。它不再只是一个 IDE 插件，而是一套包含四种形态的产品族：

- **Antigravity 桌面 App**：独立的智能体开发工作台
- **Antigravity IDE**：内置 Agent Manager、Artifacts 和深度代码库理解的智能体 IDE
- **Antigravity CLI (`agy`)**：轻量、快速的终端原生智能体
- **Antigravity SDK**：用 Python 脚本快速构建自定义智能体的开发套件

Antigravity 默认围绕 Gemini 3.5 / 3.6 Flash 等模型运行，同时也支持通过模型选择器切换 Claude、GPT-OSS 等第三方模型。

## 核心思想

### 以智能体为先，而非补全为先
Antigravity 把开发者定位成“智能体的管理者”：
- 工作的最小单元是任务或计划，不是按键
- 智能体可以直接使用编辑器、终端和内置浏览器
- 每次运行都会产出**可核验的 Artifacts**（任务清单、实施计划、截图、浏览器录屏），方便人工在接受前核对

### 多种形态，同一套智能体能力
无论你用桌面 App、IDE、终端 CLI 还是 SDK，底层都是同一套 Antigravity 智能体引擎，支持 Projects、多工作区、子代理和定时任务。

### 多模型，以 Gemini 为中心
- 默认模型：Gemini 3.5 Flash / 3.6 Flash
- 可选模型：Gemini 3 Pro、Claude 系列、GPT-OSS-120B 等
- 通过 `/model` 或配置快速切换

### 可核验的产出
- Artifacts 让智能体的运行可审计
- 智能体会跨会话积累项目相关的“经验”，而不是每次都从零开始

## 产品形态

| 形态 | 定位 | 适用场景 |
| --- | --- | --- |
| **桌面 App** | 独立智能体开发工作台 | 日常开发、多项目管理 |
| **IDE** | 内置 Agent Manager 的智能体 IDE | 需要深度代码编辑与多代理并行 |
| **CLI (`agy`)** | 终端原生智能体 | 习惯命令行、脚本/CI 集成 |
| **SDK** | Python 可编程接口 | 自定义智能体、自动化评估 |

## 核心能力

### 自主编程智能体
- 多步任务执行：规划 → 编辑 → 运行 → 验证
- 支持跨文件、跨仓库的并行智能体协作
- 适合长链路重构与迁移，而不只是单段代码修改

### 多智能体管理
- **Agent Manager**：在多个工作区、多个智能体之间分发与并行编排任务
- **Projects**：把相关对话和任务分组管理
- **子代理（Subagents）**：把复杂任务拆给专业化代理

### 内置浏览器控制
- 智能体可以驱动真实浏览器去验证自己的修改
- 自动捕获截图与录屏作为行为证据

### 项目记忆与学习
- 跨智能体运行携带项目上下文
- 会从历史交互（包括你提出的修正）中学习
- 支持 Hooks 和定时任务（Scheduled Tasks）

## 快速开始

### 下载

Antigravity 目前为公开预览，个人用户可免费使用。从官网下载对应系统的桌面 App 或 IDE：

- <https://antigravity.google/>

系统要求：
- Windows 10 64 位及以上
- macOS Monterey (12) 及以上
- 64 位 Linux（较新的 glibc / glibcxx）

### 登录与选择模型

1. 启动 Antigravity，使用 Google 账号登录
2. 选择默认模型——Gemini 3.5 Flash 是不错的起点
3. 打开一个工作区，进入 **Editor/IDE** 开始编码，或切换到 **Manager** 视图编排多智能体任务

### 典型工作流

1. 用自然语言描述任务（例如“为 `auth/` 目录补单元测试”、“把这个服务从 REST 迁到 gRPC”）
2. 智能体先产出一份**计划 Artifact** 供你确认
3. 智能体编辑文件、在终端中执行命令，必要时驱动浏览器进行验证
4. 审阅 diff 与 Artifacts（截图、录屏、日志），接受或继续迭代

## CLI 使用方法

Antigravity 2.0 的终端入口是 `agy`（Antigravity CLI），是 Gemini CLI 的继任者。

### 安装

- **通过 IDE/桌面 App 安装**：打开命令面板（F1 / Ctrl+Shift+P），搜索并执行 `Shell Command: Install 'agy' command in PATH`
- **独立安装**（参考官方文档）：
  ```bash
  # 具体安装方式以 Antigravity 官方文档为准
  ```

### 基本命令

```bash
# 启动交互式终端会话
agy

# 直接运行一个命令任务
agy "分析当前项目结构"

# 非交互（无头/脚本）模式
agy -p "为 src/auth.js 编写单元测试"

# 从 Gemini CLI 迁移插件
agy plugin import gemini
```

### 常用选项

- `-m, --model <model>`：指定模型，例如 `gemini-3.5-flash`
- `-p, --prompt <prompt>`：非交互模式直接执行 prompt
- `--approval-mode <mode>`：审批模式，可选 `default`、`auto_edit`、`yolo`、`plan`
- `-s, --sandbox`：在沙盒环境中运行
- `agy mcp list` / `agy skills list` / `agy hooks list`：管理 MCP、Skills、Hooks

> 注意：`gemini` 命令已于 2026 年 6 月 18 日停止为个人用户服务，新脚本请迁移到 `agy`。

## 常见场景

### 长链路重构
把多文件的重构任务交给智能体，自己只需评审它产出的计划和 diff，而不必逐处手改。

### 端到端特性开发
从规格 → 实现 → 测试 → 浏览器中验证的 UI 变更，全部由一个或多个智能体在同一工作区内推进。

### 并行任务流
用 Manager 视图同时跑多个智能体处理不同任务/分支，结果通过 Artifacts 集中查看。

### 自定义智能体（SDK）
通过 Antigravity SDK 用 Python 脚本快速原型化自定义智能体，并跑评估。

## 最佳实践

1. **任务描述要清晰** —— 提示越具体，规划越靠谱
2. **看 Artifact，不只是看 diff** —— 截图和录屏能暴露 diff 无法体现的行为问题
3. **让智能体自己去验证** —— 授权它运行测试、驱动浏览器，可核验的产出才是目标
4. **把修正反馈进去** —— Antigravity 会跨运行学习，明确的反馈会越用越值钱
5. **从桌面 App 或 IDE 开始** —— 熟悉后再使用 `agy` CLI 进行脚本化集成

## 相关资源

- [Antigravity 官网](https://antigravity.google/)
- [Google Antigravity 2.0 公告](https://blog.google/products/antigravity/)

## 许可证

Antigravity 是 Google 的专有产品。当前公开预览期个人用户可免费使用，部分高级功能或更高配额可能需要 Google AI 订阅。使用须遵循 Google 服务条款。
