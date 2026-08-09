# Codex 简介

## 什么是 Codex？

Codex 是 OpenAI 推出的 AI 编程智能体，核心是一个使用 Rust 编写的开源（Apache-2.0）终端 CLI。它支持在本地仓库中直接理解、编辑和运行代码，并提供 VS Code / Cursor / Windsurf / JetBrains IDE 扩展、Codex App（桌面应用）以及 Codex Web（云端任务）等多种使用方式。通过同一个 ChatGPT 账号，活跃会话可以在手机、桌面和 Web 之间同步。

## 核心思想

### 终端原生
Codex CLI 围绕终端工作流设计，让你在熟悉的 shell 环境中完成探索、编辑、运行、审查等整个开发循环。

### 本地优先 + 云端可选
默认在本地机器上运行，代码和凭证不出本机；也可以把任务提交到 Codex Cloud，在云端沙箱中异步完成。

### 可控的自动化
通过审批模式（approval mode）和沙箱（sandbox）组合，控制 Codex 何时可以读写文件、运行命令、访问网络。

### 可扩展
支持 Skills（可复用指令）、Plugins（团队工具连接）、MCP 服务器、子代理以及 Hooks 等扩展机制。

## 可用界面

| 界面 | 说明 |
| --- | --- |
| 终端 CLI | 开源 Rust 客户端，功能最完整 |
| IDE 扩展 | VS Code / Cursor / Windsurf / JetBrains |
| 桌面 App | `codex app`，可视化管理与多会话 |
| Codex Web | chatgpt.com/codex，云端任务与协作 |
| 手机 App | ChatGPT App 可连接并继续活跃会话 |

## 核心能力

### 代码理解与修改
- 分析项目结构、依赖和调用关系
- 自动修复 bug、重构、添加功能
- 多步骤任务执行与迭代

### 命令行与 CI 集成
- 交互式 TUI 和一次性 prompt 模式
- `codex exec` 用于脚本和流水线
- 管道与 shell 脚本集成

### 代码审查
- `codex review` 对未提交改动、commit 或分支进行审查
- 不修改工作树，只输出风险与建议

### 扩展体系
- **Skills / Plugins**：可复用指令和团队工具连接
- **MCP 服务器**：连接外部工具和数据源
- **子代理**：把复杂调查拆给专业化代理
- **Hooks**：自定义生命周期行为

### 跨端与远程
- **ChatGPT relay**：活跃会话在手机、桌面、Web 之间同步
- **Remote SSH**：直接连接到远程开发环境
- **Codex Cloud**：把任务提交到云端环境，关闭电脑也能继续

## 快速开始

### 安装

官方推荐安装脚本：

```bash
# macOS / Linux
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Homebrew：

```bash
brew install --cask codex
```

npm（备选）：

```bash
npm install -g @openai/codex
```

验证安装：

```bash
codex --version
```

### 登录

```bash
codex
```

选择 **Sign in with ChatGPT**（推荐）或使用 OpenAI API key。

### 常用命令

```bash
codex                                      # 启动交互会话
codex "分析这个项目的结构"                 # 单次 prompt
codex exec "运行测试套件"                  # 非交互 / CI 模式
codex review                               # 审查未提交改动
codex resume                               # 恢复最近会话
codex cloud                                # 管理云端任务
codex mcp list                             # 查看已配置 MCP 服务器
codex --image error.png "这个报错怎么修"   # 传入图片上下文
```

## 审批模式与沙箱

Codex 通过 **approval mode** 控制何时暂停询问，通过 **sandbox** 控制文件/网络访问范围。

### 审批模式

| 模式 | 说明 |
| --- | --- |
| `suggest`（默认） | 每次改动前询问 |
| `auto-edit` | 自动编辑文件，执行命令前询问 |
| `full-auto` | 自动执行编辑和命令（谨慎使用） |

```bash
codex --approval-mode auto-edit
codex --approval-mode full-auto
```

### 沙箱模式

| 模式 | 说明 |
| --- | --- |
| `read-only` | 只读，不修改文件（类似 plan 模式） |
| `workspace-write` | 可在当前工作目录读写 |
| `danger-full-access` | 无沙箱限制 |

```bash
codex -s read-only
codex --sandbox workspace-write
```

> 在交互界面中可通过 `/permissions` 快速切换。不熟悉的项目建议先用 `suggest` + `read-only/workspace-write`。

## 最佳实践

1. **从 suggest 模式开始**：熟悉项目后再提高自动化。
2. **明确任务范围**：说明目标文件、期望行为和要运行的测试。
3. **审查 diff 并运行测试**：AI 改动仍需人工检查。
4. **用 Skills 沉淀重复工作流**：减少每次重复提示。
5. **敏感代码使用严格沙箱**：避免意外文件或网络访问。

## 相关资源

- [GitHub 仓库](https://github.com/openai/codex)
- [Codex CLI 文档](https://developers.openai.com/codex/cli)
- [OpenAI 官方公告：随时随地使用 Codex](https://openai.com/index/work-with-codex-from-anywhere/)

## 许可证

Codex CLI 采用 Apache-2.0 许可证发布。使用 OpenAI 模型服务时请遵循对应服务条款。
