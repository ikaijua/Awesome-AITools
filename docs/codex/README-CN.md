# Codex 简介

## 什么是 Codex？

Codex 是 OpenAI 推出的轻量级编程智能体，专门在终端中运行。它是一个 AI 驱动的编程助手，能够直接从命令行理解和修改代码。与需要在 IDE 或浏览器中使用的 AI 工具不同，Codex 为开发者提供了一种更简洁、更接近工作流的代码交互方式。

## 核心思想

### 终端优先
Codex 专为命令行设计，适合习惯在终端工作的开发者：
- 无需离开终端即可使用 AI 辅助编程
- 与现有开发工作流无缝集成
- 轻量级，响应快速

### 理解与修改
不只是生成代码片段，Codex 能够：
- 理解你的项目结构
- 直接修改文件中的代码
- 执行多步骤的编程任务

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