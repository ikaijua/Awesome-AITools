# Codex 简介

## 什么是 Codex？

Codex CLI 是 OpenAI 推出的基于 Rust 开发的高性能编程智能体，专门在终端中运行。它是一个 AI 驱动的编程助手，能够直接从命令行极速理解和修改代码。基于 GPT-5.4 生态，Codex CLI 为开发者提供了一种更简洁、更接近原生工作流的代码交互方式。

## 核心思想

### 终端优先与高性能
Codex CLI 采用 Rust 构建，旨在提供极致的响应速度：
- 由 GPT-5.4 mini 驱动的超低延迟响应
- 无需离开终端即可使用 AI 辅助编程
- 与现有 shell 脚本和管道无缝集成

### 理解与修改
不只是生成代码片段，Codex CLI 能够：
- 理解你的项目结构
- 直接修改文件中的代码
- 极速执行多步骤的编程任务

### 简洁高效
- 最小化配置，开箱即用
- 专注于核心编程任务
- 不打扰你的工作流

## 核心功能

### 代码理解
- 分析项目结构和依赖
- 理解函数和类的用途
- 追踪代码调用关系

### 代码修改
- 自动修复 bug
- 重构代码
- 添加新功能

### 命令行集成
- 直接在终端提问
- 支持管道和重定向
- 与 shell 脚本配合使用

## 快速开始

### 安装

```bash
npm install -g @openai/codex
```

### 配置

设置你的 OpenAI API 密钥：

```bash
export OPENAI_API_KEY="your-api-key"
```

### 基本使用

```bash
# 提问
codex "这个函数是做什么的？"

# 让它修改代码
codex "帮我重构这个函数，让它更易读"

# 指定文件
codex "修复 src/utils.js 中的 bug"
```

## 审批模式与沙箱

Codex CLI 从两个维度控制自动化程度：**审批策略**（何时暂停询问你）和**沙箱**（允许它操作什么）。这是 Codex 对应 Claude Code `--permission-mode` 的机制。

### `--full-auto` —— 低摩擦的"自动"模式

最接近"自动"模式的等价物：Codex 会自动执行常规操作，只在真正需要时才打断你。

```bash
codex --full-auto
```

### 审批策略 —— `--ask-for-approval`（简写 `-a`）

- `untrusted` - 只有可信命令自动执行，其它都需要确认
- `on-failure` - 先在沙箱里运行，只有命令失败需要提权时才询问
- `on-request` - 由模型自己决定何时请求审批（默认）
- `never` - 从不询问（完全自主）

### 沙箱 —— `--sandbox`（简写 `-s`）

- `read-only` - 只能读文件，不能修改（适合安全探索，类似 plan 模式）
- `workspace-write` - 可在当前工作目录内读写
- `danger-full-access` - 无沙箱限制

### 便捷组合

```bash
# 低摩擦自动模式
codex --full-auto

# 只读探索（类似 plan）
codex -s read-only

# 完全放开（谨慎使用）
codex --dangerously-bypass-approvals-and-sandbox
```

> 在交互界面中，这些被封装成 **Read Only / Auto / Full Access** 三种模式，可通过 `/approvals` 切换。在不熟悉的项目上建议先用较严格的模式，等你放心让 Codex 更快处理工作后再切换到 `--full-auto`。

## 常用命令

```bash
# 启动交互模式
codex

# 分析当前目录的代码
codex "分析这个项目的结构"

# 生成测试
codex "为 src/api.js 生成单元测试"
```

## 最佳实践

1. **提供上下文** - 告诉它你在做什么，它会给出更好的建议
2. **逐步细化** - 从大方向开始，逐步深入细节
3. **验证结果** - AI 生成的代码要自己检查和测试
4. **善用交互** - 可以追问和让它修改方案

## 相关资源

- [GitHub 仓库](https://github.com/openai/codex)
- [OpenAI 文档](https://platform.openai.com/docs)
- [API 密钥获取](https://platform.openai.com/api-keys)
- [与其他工具对比](../COMPARISON-CN.md)

## 许可证

Codex 由 OpenAI 开发，使用需要 OpenAI API 密钥。请遵循 OpenAI 的服务条款。