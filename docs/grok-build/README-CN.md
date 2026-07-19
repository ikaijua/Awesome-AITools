# Grok Build 介绍

## 什么是 Grok Build？

Grok Build（即 `grok` CLI/TUI）是 xAI 推出的基于终端的 AI 编程智能体。它以全屏、支持鼠标交互的 TUI 形式运行，能够理解你的代码库、编辑文件、执行 shell 命令、搜索网络并管理长时间运行的任务。可以交互式使用，也可以在脚本/CI 中以无头（headless）模式运行，或通过 Agent Client Protocol（ACP）嵌入编辑器。

该项目开源（Apache-2.0 许可），使用 Rust 编写，并定期从 SpaceXAI 单体仓库同步。仓库根目录的 `SOURCE_REV` 文件记录了当前代码对应的单体仓库提交 SHA。

## 核心理念

### 终端优先的编程智能体
Grok Build 为希望留在终端中工作的开发者而设计：
- 直接在项目目录中启动全屏 TUI
- 用自然语言询问代码库相关问题
- 让智能体在同一会话中规划、编辑文件、运行工具并迭代

### 多种运行模式
- **交互式 TUI** —— 滚动回看、输入提示、模态框、鼠标交互
- **无头模式** —— 用于脚本和 CI 的非交互式运行
- **ACP 集成** —— 将智能体嵌入兼容 ACP 的编辑器

### 可扩展的智能体运行时
Grok Build 内置了智能体开发常用的能力：
- MCP 服务器
- 技能（Skills）与插件
- 生命周期钩子（Hooks）
- 沙箱与工作区检查点（checkpoints）
- 主题与配置

## 核心功能

### 代码理解与编辑
- 分析项目结构和依赖关系
- 读取、搜索和修改文件
- 实现功能、修复 Bug、重构代码

### Shell 与工作流自动化
- 运行构建、测试、lint 和项目脚本
- 在观察工具反馈的同时串联多个步骤
- 管理长时间运行的任务

### 网络与集成
- 在会话内搜索网络
- 配置 MCP 服务器、技能、插件和钩子

## 快速开始

### 安装发布版二进制文件

已为 macOS、Linux 和 Windows 提供预编译二进制文件：

```sh
curl -fsSL https://x.ai/cli/install.sh | bash   # macOS / Linux / Git Bash
irm https://x.ai/cli/install.ps1 | iex          # Windows PowerShell
grok --version
```

首次启动时会打开浏览器进行身份认证。

### 从源码构建

环境要求：
- **Rust** —— 工具链由 `rust-toolchain.toml` 固定版本，`rustup` 会在首次构建时自动安装。
- **[DotSlash](https://dotslash-cli.com)** —— 用于让 `bin/` 下的 hermetic 工具（尤其是 `bin/protoc`）下载并运行。
- **protoc** —— proto 代码生成通过 DotSlash 解析 `bin/protoc`，或回退到 `PATH` / `$PROTOC` 上的 `protoc`。
- 支持 macOS 和 Linux 作为构建主机；Windows 构建为尽力而为（best-effort）。

```sh
cargo run -p xai-grok-pager-bin              # 构建并启动 TUI
cargo build -p xai-grok-pager-bin --release  # 发布版二进制：target/release/xai-grok-pager
cargo check -p xai-grok-pager-bin            # 快速校验
```

二进制产物名为 `xai-grok-pager`；官方安装包将其命名为 `grok`。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `crates/codegen/xai-grok-pager-bin` | 组合根包，构建 `xai-grok-pager` 二进制 |
| `crates/codegen/xai-grok-pager` | TUI：滚动回看、输入提示、模态框、渲染 |
| `crates/codegen/xai-grok-shell` | 智能体运行时 + leader/stdio/无头入口 |
| `crates/codegen/xai-grok-tools` | 工具实现（终端、文件编辑、搜索等） |
| `crates/codegen/xai-grok-workspace` | 主机文件系统、版本控制、执行、检查点 |
| `third_party/` | 引入的上游源码（Mermaid 图表栈） |

## 注意事项

- **不接受外部贡献**（详见仓库中的 `CONTRIBUTING.md`）。
- 根目录的 `Cargo.toml` 是自动生成的，请视为只读，优先编辑各 crate 自身的 `Cargo.toml`。

## 相关资源

- [GitHub 仓库](https://github.com/xai-org/grok-build)
- [官方文档](https://docs.x.ai/build/overview)
- [Grok Build 主页](https://x.ai/cli)
- [更新日志](https://x.ai/build/changelog)
- [与其他工具的对比](../COMPARISON-CN.md)

## 许可证

仓库中的第一方代码采用 Apache License 2.0 许可。第三方和引入的代码仍遵循其原始许可证。
