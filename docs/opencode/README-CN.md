# OpenCode 介绍

## 什么是 OpenCode?

OpenCode 是一款开源、终端原生的 AI 编码 agent。它运行在终端中，拥有精致的 TUI 界面和客户端/服务端架构，并且不绑定特定厂商——你可以将它接入 Anthropic、OpenAI、Google 或本地模型，而不必被单一供应商锁定。此外还提供适用于 macOS、Windows 和 Linux 的桌面应用（BETA）。

## 核心功能

### 1. 不绑定厂商
- 支持 Anthropic、OpenAI、Google 以及本地/自托管模型。
- 不绑定任何单一供应商或订阅。

### 2. 终端原生 TUI
- 快速、以键盘操作为主的终端界面。
- 客户端/服务端架构，agent 可与界面分离运行。

### 3. 内置 Agent
- **build** —— 默认的完整权限 agent，用于日常开发。
- **plan** —— 只读 agent，用于分析与代码探索；默认拒绝编辑，执行命令前会先询问。
- **general** —— 用于复杂搜索和多步骤任务的子 agent，通过 `@general` 调用。

### 4. LSP 集成
- 支持语言服务器协议（LSP），提供更懂代码的辅助能力。

### 5. 可扩展
- 支持自定义 agent 和 MCP（Model Context Protocol）服务器。
- 可通过项目级和全局配置进行定制。

## 快速开始

### 安装

```bash
# 安装脚本
curl -fsSL https://opencode.ai/install | bash

# 包管理器
npm i -g opencode-ai@latest          # 或 bun/pnpm/yarn
brew install anomalyco/tap/opencode  # macOS 和 Linux（推荐）
scoop install opencode               # Windows
choco install opencode               # Windows
sudo pacman -S opencode              # Arch Linux
mise use -g opencode                 # 任意系统
```

### 桌面应用（BETA）

可从 [releases 页面](https://github.com/anomalyco/opencode/releases) 或 [opencode.ai/download](https://opencode.ai/download) 直接下载。

### 使用

在项目目录中运行 `opencode`，然后用 `Tab` 键在 **build** 和 **plan** 两个 agent 之间切换。

## 相关资源

- [官网](https://opencode.ai)
- [文档](https://opencode.ai/docs)
- [GitHub 仓库](https://github.com/anomalyco/opencode)
- [Discord](https://discord.gg/opencode)
