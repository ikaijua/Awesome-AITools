# Claude Code 简介

## 什么是 Claude Code？

Claude Code 是 Anthropic 推出的官方 AI 编程智能体。它不仅提供终端 CLI，也提供 VS Code / Cursor / JetBrains IDE 插件、独立桌面 App、Web 版（claude.ai/code），以及通过 Remote Control 与 iOS / Android 移动端 App 联动的能力。所有界面共享同一套底层引擎，因此 CLAUDE.md、MCP 服务器、Skills、Hooks 和记忆可以在不同表面之间保持一致。

## 核心思想

### 以 Agent 为中心，而不只是补全
Claude Code 能够理解整个代码库，跨文件规划、编辑、运行命令、检查测试结果，并根据反馈迭代，直到完成你描述的任务。

### 项目级记忆
通过 `CLAUDE.md` 项目指令文件和自动记忆，Claude Code 能记住项目结构、规范、常用命令，减少每次重复交代背景。

### 可控的自主性
从严格的计划模式到自动模式，再到完全跳过权限确认的 YOLO 模式，你可以根据任务风险和信任程度选择让 Claude 自主到什么程度。

### 多面统一
无论你在终端、IDE、桌面 App、Web 还是手机上操作，底层都连接到同一个 Claude Code 引擎，会话和配置可以跨设备延续。

## 可用界面

| 界面 | 说明 |
| --- | --- |
| 终端 CLI | 完整功能，最适合深度开发 |
| VS Code / Cursor | 插件形式，提供内联 diff 和对话面板 |
| JetBrains | IDEA / PyCharm / WebStorm 等插件 |
| 桌面 App | 可视化 diff、多会话并排、定时任务 |
| Web | claude.ai/code，无需本地安装 |
| 手机 App | Claude iOS / Android App，通过 Remote Control 连接本地会话 |

## 核心能力

### 代码理解与编辑
- 自动探索代码库结构、依赖和调用关系
- 多文件重构、添加功能、修复 bug
- 内联 diff 和视觉化审阅

### 终端与工具链集成
- 运行 shell 命令、测试、构建脚本
- 原生 Git 操作与 GitHub / GitLab 集成
- 支持 CI/CD、Slack、Chrome 等扩展场景

### 扩展体系
- **MCP 服务器**：连接数据库、浏览器、外部 API
- **Skills**：可复用的项目级工作流（通过 `/skill` 调用）
- **Hooks**：在文件写入、命令执行等生命周期点触发脚本
- **子代理（Subagents）**：把复杂任务拆给多个专业化代理并行处理

### 跨端协作
- **Remote Control**：从手机或浏览器继续本地 Claude Code 会话
- **Cloud 会话**：`claude --cloud` 启动可在移动端继续的任务
- 文件、凭证和本地环境始终保留在运行 Claude Code 的机器上

## 快速开始

### 安装

官方推荐安装脚本（macOS / Linux）：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Homebrew：

```bash
brew install claude-code
```

npm（备选）：

```bash
npm install -g @anthropic-ai/claude-code
```

Windows 可用 WinGet 或 PowerShell 安装脚本，详见 [官方文档](https://docs.anthropic.com/en/docs/claude-code/overview)。

首次运行：

```bash
claude
```

按提示登录 Anthropic 账号，或提前设置 `ANTHROPIC_API_KEY`。

### 常用命令

```bash
claude                          # 启动交互会话
claude /path/to/project         # 在指定目录启动
claude "修复登录 bug"           # 直接提问
claude --permission-mode plan   # 先规划再执行
claude --permission-mode auto   # 自动批准常规操作
claude --cloud                  # 启动可在手机继续的 cloud 会话
```

### 权限模式

| 模式 | 说明 |
| --- | --- |
| `default` | 敏感操作前询问（推荐日常使用） |
| `plan` | 只探索和规划，改动前等待确认 |
| `auto` | 自动批准低风险常规操作，敏感操作仍询问 |
| `--dangerously-skip-permissions` | 跳过所有确认（仅建议可信仓库 / CI 使用） |

> 在不熟悉的项目上建议先用 `default` 或 `plan`，信任后再切换到 `auto`。

## 常用 Slash 命令

- `/help` - 查看帮助
- `/clear` - 清空当前会话
- `/commit` - 创建 Git 提交
- `/review-pr` - 审查 Pull Request
- `/remote-control` - 开启跨设备 Remote Control
- `/mcp` - 查看 MCP 服务器状态
- `/settings` 或 `/config` - 打开设置

## 配置文件

- `~/.claude/settings.json`：用户级配置（权限、模型、hooks、环境变量）
- `CLAUDE.md`：项目级指令与规则
- `.claude/`：项目本地记忆和配置

## 最佳实践

1. **写清楚任务目标**：描述期望行为、相关文件、要运行的测试。
2. **使用 CLAUDE.md**：把项目规范、安全红线和常用命令写进去。
3. **从 plan/default 开始**：熟悉项目后再提高自动化程度。
4. **审阅 diff 并运行测试**：把 Claude 的输出当作同事的 PR 来 review。
5. **善用 Skills 和 Hooks**：把重复工作流封装成可复用能力。

## 相关资源

- [官方文档](https://docs.anthropic.com/en/docs/claude-code/overview)
- [GitHub 仓库](https://github.com/anthropics/claude-code)
- [Claude Code Remote Control](https://docs.anthropic.com/en/docs/claude-code/remote-control)

## 许可证

Claude Code 由 Anthropic 开发和维护，使用请遵循 Anthropic 的服务条款。
