# oh-my-pi 介绍

## 什么是 oh-my-pi？

[oh-my-pi](https://github.com/can1357/oh-my-pi)（简称 `omp`）是 [@can1357](https://github.com/can1357) 基于 [Pi](https://github.com/mariozechner/pi) fork 的终端原生 AI 编码 agent。它的定位是 **“A coding agent with the IDE wired in”**——让 agent 在一个 TUI 界面里完成代码编辑、搜索、调试和执行，并能利用 IDE 已掌握的所有代码知识。

项目基于约 5.5 万行 Rust 核心，内置 40+ 模型提供商、32 个工具、14 种 LSP 操作和 28 种 DAP 调试操作。

## 核心功能

### 1. 深度 IDE 集成
- 完整 LSP 支持：agent 可以重命名符号、追踪引用，并像 IDE 一样理解代码库。
- 通过 DAP 接入真实调试器：可附加 `lldb`、`dlv` 或 `debugpy`，让 agent 检查调用栈和变量。

### 2. 支持工具调用的代码执行
- 在 agent 会话内运行持久的 Python 和 Bun 执行环境。
- 两个内核都可以通过回环桥接回调 agent 自身的工具（read、search、task）。
- 可以在 Python 里用 `tool.read` 加载 CSV，再用 JavaScript 绘图，整个过程不离开当前会话。

### 3. 不绑定厂商
- 支持 40+ 模型提供商，可接入自有 API Key 或本地模型。

### 4. 时间回溯流规则
- 用户定义的规则在模型输出匹配正则时才会触发，mid-token 注入提醒并从同一点重试。
- 在不增加每轮上下文开销的情况下实现路线修正。

### 5. 开箱即用
- 32 个内置工具，并针对不同模型优化了提示词，以实现一次性编辑成功、文件摘要式读取和快速搜索。

## 快速开始

### 安装

```bash
# 安装脚本（macOS / Linux）
curl -fsSL https://omp.sh/install | sh

# Windows PowerShell
irm https://omp.sh/install.ps1 | iex

# Homebrew
brew install can1357/tap/omp

# Bun（推荐）
bun install -g @oh-my-pi/pi-coding-agent

# mise
mise use -g github:can1357/oh-my-pi
```

### 使用

在项目目录中运行 `omp` 即可启动 agent 会话。可生成基于实时 CLI 元数据的 shell 补全：

```bash
# zsh — 添加到 ~/.zshrc
eval "$(omp completions zsh)"

# bash — 添加到 ~/.bashrc
eval "$(omp completions bash)"

# fish
omp completions fish > ~/.config/fish/completions/omp.fish
```

## 相关资源

- [官网](https://omp.sh)
- [GitHub 仓库](https://github.com/can1357/oh-my-pi)
