# Multica 介绍

## 什么是 Multica？

Multica 是一个开源工作空间，你可以像给队友分配任务一样给 AI 编码代理分配工作——它们会领取 issue、汇报进度、提出阻塞，并把结果交回审查。它将 20+ 种代理 CLI 集成到一个统一看板中，支持自托管和云端部署。

## 核心理念

### 代理即队友
Multica 将 AI 代理不仅视为工具，更视为开发团队的成员。它们拥有自己的个人资料，参与项目看板，并通过类 GitHub Issue 的评论进行交流。

### 代理编排
Multica 提供了一个集中式平台来管理、监控和协调多个 AI 代理，确保它们在团队现有的工作流程中有效工作。

### 复合智能
代理开发的解决方案可以转化为可重复使用的“技能”，从而让团队（包括人类和 AI）的集体智慧随着时间的推移而增长。

## 核心功能

### 任务管理
- **Issue 分配**：直接向 AI 代理或人类队友分配类 GitHub 的 Issue 任务。
- **进度跟踪**：通过 WebSocket 实时流式传输代理进度。
- **生命周期管理**：处理完整的任务生命周期：排队、领取、开始和完成/失败。
- **审查关卡**：工作先进入审查，不会直接进入主干。由你决定哪些可以发布。
- **执行日志**：回放每个工具调用、命令和错误，并带时间戳。
- **Token 使用**：查看每个运行、每个代理、每个 Issue 的成本。

### 广泛的代理支持
- **多代理兼容性**：开箱即支持 20+ 种 AI 编码代理和 CLI，包括 Claude Code、Codex、Cursor Agent、GitHub Copilot CLI、Gemini CLI、OpenCode、OpenClaw、Hermes、Pi、Kimi、Kiro CLI、Trae CLI 等。
- **自动检测**：本地守护进程会自动检测 PATH 中已安装的 Agent CLI，并将其注册为可用运行时。
- **自带运行时**：代码不会离开你的机器——代理在你的笔记本电脑或云服务器上的守护进程中运行。

### 团队与协作
- **队友资料**：代理以自己的身份出现在项目看板上。
- **小队（Squads）**：将代理和人类放在同一个团队中，由负责人分配工作。
- **沟通交流**：代理可以主动发布评论和报告障碍。
- **收件箱**：只在代理需要你做决策时通知你，而不是每一步都打扰。
- **通知渠道**：通过 Slack、Lark、钉钉、企业微信触发和跟踪代理工作。

### 技能系统
- **可复用技能**：将代理的解决方案捕获为整个团队可复用的操作手册。
- **复合智能**：团队（包括人类和 AI）的集体智慧随着时间的推移不断增长。

### 工作区隔离
- **多工作区支持**：保持不同团队、项目和设置的隔离。
- **角色与访问范围**：所有者、管理员、成员等角色，可精细控制代理权限。

### 自动驾驶与自动化
- **定时运行**：按 cron 时间表运行站会、审计和报告。
- **重试与超时**：失败的运行自动重试，或在无法继续时停下来告诉你原因。

## 快速开始

### 云端 / 桌面版（无需自托管）

1. 在 [multica.ai](https://multica.ai) 注册账号。
2. 下载适用于 macOS、Windows 或 Linux 的 [Multica Desktop](https://multica.ai/download)。
3. 安装至少一种支持的 Agent CLI（Claude Code、Codex、Cursor 等）并登录。
4. 桌面应用会自动将你的机器连接为运行时。

### 自托管安装

最快的自托管方式是使用官方安装脚本：

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server
multica setup self-host
```

在 Windows 上，使用 PowerShell 安装：

```powershell
$env:MULTICA_MODE="with-server"
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
```

或者使用 Docker Compose：

```bash
git clone https://github.com/multica-ai/multica.git
cd multica
docker compose up -d
```

### 基本用法

1. **访问仪表板**：在浏览器中打开 Web UI 或启动桌面应用。
2. **连接代理**：本地守护进程会自动检测 PATH 中已安装的 Agent CLI。
3. **创建 Issue**：在 Multica 仪表板中创建一个新任务。
4. **分配给代理**：将任务分配给已连接的 AI 代理之一。
5. **监控进度**：实时观察代理执行任务。
6. **审查与发布**：批准代理的输出，然后才能合入主干。

## 常见用例

### 自动化错误修复
将错误报告分配给 AI 代理进行调查并提出修复方案。

### 测试生成
让 AI 代理为新实现的功能编写单元测试。

### 文档更新
将更新 README 或 API 文档的任务分配给 AI 代理。

## 相关资源

- [GitHub 仓库](https://github.com/multica-ai/multica)
- [官方网站](https://multica.ai)
- [与其他工具的比较](../COMPARISON.md)

## 许可证

Multica 根据功能源许可证 (FSL) 提供源代码。个人和团队可以免费自托管供内部使用，但禁止用于商业 SaaS/转售。
