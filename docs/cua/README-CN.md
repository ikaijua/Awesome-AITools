# Cua 简介

## 什么是 Cua？

**Cua**（由 [trycua](https://github.com/trycua/cua) 开发）是一套专为 **计算机使用代理 (Computer-Use Agents)** 设计的开源基础设施。它为 AI “大脑”（如 Claude 或 GPT-4）提供“身体”（驱动程序和沙箱），使其能够像人类一样在 macOS、Windows、Linux 和 Android 上查看屏幕、移动鼠标和打字。

## 核心特性

### 1. Cua Sandbox (沙箱)
统一的 SDK（`pip install cua`），用于管理临时环境。它允许开发者启动隔离的虚拟机 (VM) 或容器，使代理可以安全地执行任务而不会影响宿主机。

### 2. Cua Driver (驱动)
适用于 macOS 和 Windows 的后台驱动程序，允许代理驱动原生应用程序，而不会“抢夺”用户的实际光标或焦点。

### 3. macOS 虚拟化 (Lume)
包含 **Lume**，这是一个专门用于在 Apple Silicon 上运行 macOS 虚拟机的工具，具有近乎原生的性能，对于测试 Apple 特有的工作流至关重要。

### 4. CuaBot
一个“协作”工具，允许像 Claude Code 或 Cursor 这样的代理在沙箱内运行，同时通过 H.265 流将其窗口投影到您的桌面上。

### 5. 基准测试与训练
**Cua-Bench** 提供了一个运行强化学习 (RL) 环境和导出“轨迹”（代理操作录制）的框架，用于模型训练和评估。

## 适用人群

- **AI 研究员**：在复杂的基于 GUI 的任务（如 OSWorld、Windows Arena）上评估模型。
- **软件工程师**：构建需要使用传统桌面软件的“AI 员工”。
- **QA 自动化团队**：利用 AI 驱动进行跨平台应用程序测试。

## 快速上手

### 安装

```bash
pip install cua
```

### 基础用法 (Python)

```python
from cua import Cua

# 初始化沙箱
with Cua().sandbox(os="macos") as sb:
    # 让代理执行操作
    sb.display.screenshot().save("screen.png")
    sb.keyboard.type("Hello World")
    sb.mouse.click(x=100, y=200)
```

## 相关资源

- [GitHub 仓库](https://github.com/trycua/cua)
- [官方网站](https://www.trycua.com/)
- [文档](https://docs.trycua.com/)

## 许可证

Cua 是一个开源项目。许可详情请参考其 GitHub 仓库。
