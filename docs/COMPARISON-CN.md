# 终端 AI 编程工具对比

本文档对比三款主流的终端 AI 编程工具：Claude Code、Codex 和 Gemini CLI。

## 快速对比

| 方面 | Claude Code | Codex CLI | Gemini CLI |
|------|-------------|-----------|------------|
| 开发者 | Anthropic | OpenAI | Google |
| 开源程度 | 非开源 | 非开源 | 完全开源 |
| 架构 | TypeScript/Node | 基于 Rust | TypeScript/Node |
| API 需求 | Anthropic API | OpenAI API | Google AI API |
| 多模态 | 纯文本 | 纯文本 | 支持图片与设计资产 |
| 持久记忆 | ✅ 有 (完整) | ❌ 无 | ⚠️ 项目上下文 (`GEMINI.md`) |
| 上下文窗口 | 1M Tokens | 128K Tokens | 1M+ Tokens |
| 项目理解 | 深度理解整个项目 | 侧重单文件/函数 | 大规模代码库映射 |
| 安全设计 | 危险操作需确认 | 沙盒优先 | 危险操作需确认 |
| 扩展性 | MCP、技能、钩子 | 安全脚本 | 可自定义（开源） |

## 详细对比

### 上下文与记忆能力

**Claude Code**
- 超长上下文，能理解整个项目结构
- 持久化记忆，跨会话记住项目信息
- 支持 `claude.md` 定义项目规则和风格指南

**Codex CLI**
- 侧重极速单文件或函数级别的理解
- 基于 Rust 架构，实现超低延迟
- 无持久化会话记忆，每次对话独立

**Gemini CLI**
- 1M+ 超长上下文窗口，可摄取整个大规模仓库
- 通过 `GEMINI.md` 文件提供项目级架构指令
- 支持多模态，适用于设计到代码的工作流（图片、PDF）

### 安全与可控性

**Claude Code**
- 危险操作（删除文件、强制推送等）需要用户确认
- 可通过 `claude.md` 配置项目级安全规则
- 自动检测潜在安全漏洞

**Codex CLI**
- 沙盒优先的执行环境
- 在"安全模式"下实时修复漏洞
- 简单但快速的安全设计

**Gemini CLI**
- 开源代码可审计
- `GEMINI.md` 中的项目指令确保架构合规
- 敏感操作需用户确认的基础安全防护

### 扩展与集成

**Claude Code**
- 支持 MCP (Model Context Protocol) 服务器
- 可自定义技能系统
- 可配置自动化钩子 (hooks)
- Git/GitHub/GitLab 深度集成

**Codex CLI**
- 针对 shell 脚本集成进行了优化
- 轻量级的 "Unix 原生" 工作流
- 专注于安全性和性能

**Gemini CLI**
- 完全开源，可自行修改扩展
- 深度集成 Google 搜索，获取最新文档
- 支持 shell 脚本和管道操作
- 与 Google 生态集成

### 使用门槛

**Claude Code**
- 需要 Anthropic API 访问权限
- 功能强大，但需要学习代理工作流

**Codex CLI**
- 需要 OpenAI API 密钥 (GPT-5.4 生态)
- 配置简单，极低延迟

**Gemini CLI**
- 需要 Google AI API 密钥
- 灵活且可高度自定义，适合追求完全控制的开发者

## 选择建议

### 选 Claude Code 如果你需要：
- 深度理解大型项目
- 复杂的自主代码重构
- 高安全性和可控性
- 并行代理协作
- 与 Git 平台的深度集成

### 选 Codex CLI 如果你需要：
- 追求极致的超低延迟性能
- 脚本化的 "Unix 原生" 体验
- 侧重安全的漏洞修复
- 最小化配置

### 选 Gemini CLI 如果你需要：
- 处理超大规模代码库 (1M+ 上下文)
- 多模态能力（处理图片、设计稿）
- 工具本身的自定义和扩展
- 通过 Google 搜索实时获取信息
- 透明可控的开源代码

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