# 终端 AI 编程工具对比

本文档对比三款主流的终端 AI 编程工具：Claude Code、Codex 和 Gemini CLI。

## 快速对比

| 方面 | Claude Code | Codex | Gemini CLI |
|------|-------------|-------|------------|
| 开发者 | Anthropic | OpenAI | Google |
| 开源程度 | 非开源 | 非开源 | 完全开源 |
| API 需求 | Anthropic API | OpenAI API | Google AI API |
| 多模态 | 纯文本 | 纯文本 | 支持图片 |
| 持久记忆 | ✅ 有 | ❌ 无 | ❌ 无 |
| 项目理解 | 深度理解整个项目 | 侧重单文件/函数 | 中等 |
| 安全设计 | 危险操作需确认 | 相对简单 | 相对简单 |
| 扩展性 | MCP、技能、钩子 | 较少 | 可自定义（开源） |

## 详细对比

### 上下文与记忆能力

**Claude Code**
- 超长上下文，能理解整个项目结构
- 持久化记忆，跨会话记住项目信息
- 支持 CLAUDE.md 定义项目规则

**Codex**
- 侧重单个文件或函数级别的理解
- 无持久记忆，每次对话独立

**Gemini CLI**
- 长上下文处理能力
- 无持久记忆
- 可通过管道传入文件内容

### 安全与可控性

**Claude Code**
- 危险操作（删除文件、强制推送等）需要用户确认
- 可通过 CLAUDE.md 配置项目级安全规则
- 自动检测潜在安全漏洞

**Codex**
- 相对简单的安全设计
- 修改代码需用户触发

**Gemini CLI**
- 开源代码可审计
- 基础的安全防护

### 扩展与集成

**Claude Code**
- 支持 MCP (Model Context Protocol) 服务器
- 可自定义技能系统
- 可配置自动化钩子 (hooks)
- Git/GitHub/GitLab 深度集成

**Codex**
- 较少扩展选项
- 基础命令行集成

**Gemini CLI**
- 完全开源，可自行修改扩展
- 支持 shell 脚本和管道操作
- 与 Google 生态集成

### 使用门槛

**Claude Code**
- 需要 Anthropic API 访问权限
- 配置相对复杂，但功能强大

**Codex**
- 需要 OpenAI API 密钥
- 配置简单，开箱即用

**Gemini CLI**
- 需要 Google AI API 密钥
- 可从源码安装，适合开发者

## 选择建议

### 选 Claude Code 如果你需要：
- 深度理解大型项目
- 跨会话的项目记忆
- 高安全性和可控性
- 复杂的工作流集成
- 与 Git 平台的深度集成

### 选 Codex 如果你需要：
- 快速的单文件辅助
- 简单直接的体验
- 最小化配置
- 已经熟悉 OpenAI 生态

### 选 Gemini CLI 如果你需要：
- 完全开源的解决方案
- 多模态能力（处理图片）
- 可自定义和扩展
- 与 Google 服务集成
- 透明可控的代码

## 组合使用

这三款工具并不互斥，可以根据场景灵活选择：

- **日常开发**：Claude Code 处理复杂任务
- **快速问答**：Codex 或 Gemini CLI 轻量查询
- **多模态需求**：Gemini CLI 处理图片相关任务
- **服务器环境**：Gemini CLI 开源可审计

## 相关链接

- [Claude Code 入门介绍](claude-code/README-CN.md)
- [Codex 入门介绍](codex/README-CN.md)
- [Gemini CLI 入门介绍](gemini-cli/README-CN.md)