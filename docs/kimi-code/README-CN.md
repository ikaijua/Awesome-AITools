# Kimi Code CLI 简介

## 什么是 Kimi Code CLI？

Kimi Code CLI 是月之暗面（Moonshot AI）推出的终端 AI 编程智能体。它可以读取和编辑代码、执行 shell 命令、搜索文件、抓取网页，并根据工具反馈和用户反馈自主决定下一步。它默认适配 Kimi Code / Moonshot AI 模型，也可以配置其他兼容的模型供应商。

## 核心思想

### 终端优先的 Agent 工作流
Kimi Code 面向希望留在终端里完成开发任务的用户：
- 在项目目录中直接启动交互式 TUI
- 用自然语言询问代码库结构和实现细节
- 让 Agent 在同一个会话中规划、编辑、运行测试并继续迭代

### 可控的自主执行
Kimi Code 不只是回答问题，也可以执行任务，但权限模式是显式的：
- 只读探索默认较顺畅
- 文件修改和 shell 命令可以要求用户确认
- 当你明确希望减少打断时，可以启用 YOLO 或 Auto 模式

### 可扩展的 Agent 平台
Kimi Code 内置了 Agent 开发常用能力：
- 通过自然语言命令配置 MCP
- Skills 和子代理支持专项任务
- 生命周期 hooks 支持本地自动化
- ACP 编辑器集成，可接入 Zed、JetBrains 等 Agent Client Protocol 客户端

## 核心功能

### 代码理解与编辑
- 分析项目结构和依赖
- 读取、搜索和修改文件
- 实现功能、修复 bug、重构代码、生成测试

### Shell 与工作流自动化
- 执行 build、test、lint 和项目脚本
- 根据工具输出连续执行多步骤任务
- 支持非交互式 prompt 模式，适合脚本或 CI 风格任务

### 多模态与编辑器集成
- 当前模型支持时，可以在 TUI 中粘贴截图或视频
- 通过 `kimi acp` 接入 ACP 兼容编辑器和 IDE
- 通过本地 Kimi server 打开浏览器 Web UI

## 快速开始

### 安装

推荐使用官方安装脚本：

```bash
# macOS / Linux
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash

# Windows PowerShell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

Homebrew：

```bash
brew install kimi-code
```

npm / pnpm 安装：

```bash
npm install -g @moonshot-ai/kimi-code
# 或
pnpm add -g @moonshot-ai/kimi-code
```

验证安装：

```bash
kimi --version
```

### 第一次启动

```bash
cd your-project
kimi
```

首次启动后，在 TUI 中输入 `/login`，选择 Kimi Code OAuth 或 Moonshot AI 平台 API key。也可以不进入 TUI，直接在 shell 中登录：

```bash
kimi login
```

## 常用 CLI 命令

```bash
# 在当前目录启动交互式会话
kimi

# 继续当前目录最近一次会话
kimi --continue
kimi -C

# 从历史会话中选择，或恢复指定 session ID
kimi --session
kimi --session <session-id>

# 非交互式执行一次 prompt
kimi --prompt "总结当前仓库状态"
kimi -p "解释最近的 diff"

# 输出 stream-json，便于脚本解析
kimi -p "列出变更文件" --output-format stream-json

# 本次启动指定模型
kimi --model kimi-code/kimi-for-coding
kimi -m kimi-code/kimi-for-coding -p "解释这个项目"

# 以 Plan 模式启动，先只读探索和规划，再修改文件
kimi --plan

# 为本次会话添加额外工作目录
kimi --add-dir ../shared-lib

# 从自定义目录加载 Skills
kimi --skills-dir /path/to/team-skills --skills-dir ./local-skills
```

## 权限模式：Manual、YOLO、Auto 与 Plan

Kimi Code 的常规交互流程会在有副作用的操作前请求确认，例如写文件和执行 shell 命令。你可以根据安全性和效率需求切换不同模式。

### YOLO 模式

YOLO 模式会跳过常规工具调用的审批，包括文件写入和 shell 命令执行。只建议在可信仓库、明确知道任务风险并愿意事后检查 diff 的场景使用。

```bash
# 启动时直接开启 YOLO 模式
kimi --yolo
kimi -y

# Kimi Code 文档中记录的隐藏别名
kimi --yes
kimi --auto-approve
```

在 TUI 中切换：

```text
/yolo
/yolo on
/yolo off
/yes
```

注意：YOLO 模式不会跳过退出 Plan 模式时的确认。

### Auto 模式

Auto 模式会自动处理工具审批，并避免向用户追问澄清问题。它适合无人值守任务，介于手动审批和完全 YOLO 之间。

```bash
kimi --auto
kimi --continue --auto
```

在 TUI 中切换：

```text
/auto
/auto on
/auto off
```

### Plan 模式

Plan 模式会让 Agent 先探索并输出计划，在修改文件前等待用户确认。适合复杂任务或风险较高的改动。

```bash
kimi --plan
```

在 TUI 中切换：

```text
/plan
/plan clear
```

快捷键：`Shift-Tab` 可切换 Plan 模式。

## 常用 Slash Commands

| 命令 | 用途 |
| --- | --- |
| `/help` | 查看内置帮助、快捷键和可用命令 |
| `/login` / `/logout` | 登录或清除当前凭证 |
| `/provider` | 管理模型供应商 |
| `/model` | 切换当前会话使用的模型 |
| `/permission` | 选择权限模式 |
| `/settings` 或 `/config` | 在 TUI 中打开设置面板 |
| `/new` 或 `/clear` | 开启新会话并清空当前上下文 |
| `/sessions` 或 `/resume` | 浏览并恢复历史会话 |
| `/compact` | 压缩当前上下文，释放 token |
| `/undo` | 从当前上下文中撤销最近的 prompt |
| `/reload` | 不重启 CLI，重新加载配置 |
| `/init` | 分析代码库并生成 `AGENTS.md` |
| `/add-dir` | 添加额外工作目录 |
| `/mcp` | 查看 MCP server 连接状态 |
| `/mcp-config` | 配置 MCP server 和 MCP OAuth 登录 |
| `/plugins` | 打开插件管理器 |
| `/editor` | 配置 `Ctrl-G` 打开的外部编辑器 |
| `/theme` | 切换终端 UI 主题 |
| `/exit`、`/quit`、`/q` | 退出 Kimi Code CLI |

## 常用快捷键

| 快捷键 | 功能 |
| --- | --- |
| `Enter` | 发送当前输入 |
| `Shift-Enter` / `Ctrl-J` | 插入换行 |
| `↑` / `↓` | 浏览输入历史 |
| `Esc` / `Ctrl-C` | 中断流式输出或关闭弹窗 |
| `Ctrl-D` | 输入框为空时退出 |
| `Shift-Tab` | 切换 Plan 模式 |
| `Ctrl-S` | 将输入即时注入正在运行的回合 |
| `Ctrl-O` | 折叠或展开工具输出 |
| `Ctrl-G` | 用外部编辑器编辑当前输入 |

## 配置文件

Kimi Code 默认把本地数据存放在 `~/.kimi-code/`。如果需要移动目录，可以设置 `KIMI_CODE_HOME`。

主要文件：
- `~/.kimi-code/config.toml`：供应商、模型、默认模型、权限模式、hooks 和 Agent / 运行时设置
- `~/.kimi-code/tui.toml`：终端 UI 偏好，例如主题、编辑器、通知和升级行为
- `~/.kimi-code/mcp.json`：MCP server 声明
- `.kimi-code/local.toml`：项目本地记忆设置，例如额外工作目录

常用维护命令：

```bash
kimi doctor
kimi doctor config
kimi doctor tui
kimi upgrade
```

## Server、Web UI 与 ACP

```bash
# 启动或复用本地后台 server
kimi server run

# 打开浏览器 Web UI
kimi web

# 前台运行 server
kimi server run --foreground

# ACP 兼容编辑器使用的入口
kimi acp
```

如果要接入 Zed 或 JetBrains 等 ACP 编辑器，先在 CLI 中登录一次，然后在编辑器中配置通过 stdio 运行 `kimi acp`。

## 最佳实践

1. **大改动先用 Plan 模式**：先审阅计划，再允许 Agent 修改文件。
2. **YOLO 只在可信目录使用**：它会跳过编辑和命令执行确认。
3. **任务描述要具体**：说明目标文件、期望行为、要跑的测试和约束条件。
4. **检查 diff 并运行测试**：把 Agent 输出当成同事提交的 patch 审查。
5. **用 `/mcp-config` 管理集成**：优先使用内置 MCP 配置流程，少手写 JSON。
6. **自动化用 `-p`**：脚本场景比起驱动 TUI，更适合使用非交互式 prompt 模式。

## 相关资源

- [GitHub 仓库](https://github.com/MoonshotAI/kimi-code)
- [官方文档](https://moonshotai.github.io/kimi-code/en/)
- [命令参考](https://moonshotai.github.io/kimi-code/en/reference/kimi-command)
- [交互与审批](https://moonshotai.github.io/kimi-code/en/guides/interaction)
- [与其他工具对比](../COMPARISON-CN.md)

## 许可证

Kimi Code CLI 使用 MIT License。使用 Kimi Code、Moonshot AI 或第三方模型供应商时，请遵循对应服务条款。
