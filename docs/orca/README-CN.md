# Orca 介绍

## 什么是 Orca？

Orca 是一款跨平台的 **Agent Development Environment（ADE）**，专为编排并行的 AI 编程智能体舰队而设计。它让你在同一个桌面 IDE 中并排运行 Claude Code、Codex、OpenCode、Pi 以及几乎所有 CLI 智能体——每个智能体都在独立的 git worktree 中工作，便于对比结果并合并最优解。

## 核心理念

### 多个智能体，一个工作区
Orca 不需要你在多个终端窗口之间切换，而是把多个智能体集中到一个桌面 IDE 中。同一个提示词可以同时分发给多个智能体，由你挑选最佳结果。

### 自带订阅
Orca 不替代你已有的智能体，而是运行你已安装的代理。你需要自行准备 Claude、Codex、OpenAI 等 API Key 或订阅。

### 桌面优先，移动协同
Orca 是 macOS、Windows 和 Linux 上的原生桌面应用，并配有 Mobile Companion，可从手机监控和继续智能体任务。

## 核心功能

### 并行 Worktrees
- 将一个提示词同时分发给最多 5 个智能体。
- 每个智能体在独立的 git worktree 中运行。
- 并排对比输出，合并最优方案。

### Mobile Companion
- 智能体完成或需要关注时收到通知。
- 支持 iOS 和 Android 远程发送后续指令。

### 终端与编辑器
- 类 Ghostty 终端，支持 WebGL 渲染、无限分屏和重启后保留的滚动历史。
- 类 VS Code 编辑器，支持自动保存；可直接把文件或图片拖入智能体提示词。

### Design Mode
- 在真实 Chromium 窗口中点击任意 UI 元素。
- 自动将该元素的 HTML、CSS 和裁剪截图送入智能体上下文。

### 原生集成
- 在应用内浏览 GitHub PR、Issue 和 Linear 项目看板。
- 直接从任务打开 worktree。
- 在 Orca 内 review diff、逐行批注，无需切换上下文。

### SSH Worktrees
- 在远程服务器上运行智能体，支持完整的文件编辑、git 和终端访问。
- 自动重连与端口转发。

### Computer Use
- 当工作流需要与真实桌面应用和可见 UI 交互时，让智能体直接操作。

### 支持的智能体
兼容任何 CLI 智能体，包括但不限于：
Claude Code、Codex、Grok、Cursor、GitHub Copilot、OpenCode、MiMo Code、Amp、OpenClaude、Antigravity、Pi、oh-my-pi、Hermes Agent、Devin、Goose、Auggie、Autohand Code、Charm、Cline、Codebuff、Command Code、Continue、Droid、Kilocode、Kimi、Kiro、Mistral Vibe、Qwen Code、Rovo Dev 等。

## 快速开始

### 安装桌面应用

从 [onOrca.dev](https://www.onorca.dev) 下载，或使用包管理器安装：

```bash
# macOS (Homebrew)
brew install --cask stablyai/orca/orca

# Arch Linux (AUR)
yay -S stably-stably-bin
```

官方也提供 macOS Apple Silicon、macOS Intel、Windows (.exe) 和 Linux AppImage 版本。

### 安装 Mobile Companion

- iOS：App Store 或 TestFlight
- Android：官网下载 APK

### 基本用法

1. **打开 Orca**，连接 PATH 中已安装的一个或多个智能体 CLI。
2. **为任务创建 worktree**。
3. **将提示词分发给多个智能体**。
4. **并排对比结果**。
5. **对 diff 进行批注**，把获胜方案发回给智能体。
6. **将最优 worktree 合并回主分支**。

## 常见用例

### 对比智能体输出
用 Claude Code 和 Codex 并行执行同一个编码任务，选择更正确或更符合习惯的实现。

### 长时运行任务
在远程 VPS 或高性能工作站上保持智能体运行，通过手机监控进度。

### 以 UI 为中心的开发
使用 Design Mode 捕获真实浏览器中的 UI 元素，交给智能体进行前端修复或测试。

## 相关资源

- [GitHub 仓库](https://github.com/stablyai/orca)
- [官方网站](https://www.onorca.dev)
- [与其他工具的比较](../COMPARISON-CN.md)

## 许可证

Orca 桌面应用本身可免费使用。智能体运行需使用你自己的订阅和 API Key。
