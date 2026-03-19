# Claude Code 简介

## 什么是 Claude Code？

Claude Code 是 Anthropic 推出的官方命令行工具，将 Claude 的强大能力直接带入您的开发工作流程。它是一个交互式 AI 助手，专门设计用于帮助开发者完成各种软件工程任务。

## 核心思想

### 不只是"补全代码"
普通的 AI 编程助手只会给你补全几行代码。但 Claude Code 更像是一个真正懂你项目的搭档——你告诉它"帮我修一下登录页面的 bug"，它会自己去看代码、找到问题、修好它，甚至帮你提交。

### 记得住你的项目
你有没有遇到过这种尴尬：跟 AI 解释完项目结构，关掉对话后再来一次，又得从头解释？Claude Code 不一样，它能记住：
- 知道你项目里有哪些模块，谁调用谁
- 下次对话还能接着上次的话题聊
- 你可以用 CLAUDE.md 告诉它项目的"规矩"

### 你说了算
Claude Code 会主动问你，不会自作主张：
- 删文件、推代码这种大事，必须你点头
- 它会告诉你它要做什么，让你确认
- 出错了可以随时让它改

### 安全第一
它比你更谨慎：
- 看到可能有问题的地方会主动提醒你
- 不会悄悄执行危险操作
- 你可以在 CLAUDE.md 里写清楚哪些事绝对不能做

## 核心功能

### 1. 代码理解与导航
- 自动探索和理解代码库结构
- 智能搜索文件和代码内容
- 快速定位函数、类和变量定义

### 2. 代码编辑与重构
- 自动修复代码缺陷
- 智能重构和代码优化
- 添加新功能和特性

### 3. 开发工作流集成
- 原生 Git 操作支持
- 与 GitHub/GitLab 等 CI/CD 平台集成
- 自动化测试和代码审查

### 4. 多模型支持
- 支持最新的 Claude 4.5/4.6 系列模型
- 可根据任务需求切换不同模型
- Fast 模式提供更快速的响应

## 主要特点

### 安全可靠
- 内置安全防护，避免危险操作
- 自动检测潜在的安全漏洞
- 敏感操作需要用户确认

### 智能上下文
- 自动压缩对话历史，支持长会话
- 持久化记忆系统，跨会话保留上下文
- 支持项目级别的配置和记忆

### 灵活扩展
- 支持 MCP (Model Context Protocol) 服务器
- 可自定义技能和工具
- 可配置自动化钩子 (hooks)

## 快速开始

### 安装

```bash
npm install -g @anthropic-ai/claude-code
```

### 基本使用

```bash
# 启动 Claude Code
claude

# 在特定目录启动
claude /path/to/project

# 使用 Fast 模式
claude --fast
```

### 常用命令

- `claude` - 启动交互式会话
- `claude "你的问题"` - 直接提问
- `/help` - 获取帮助
- `/clear` - 清除对话历史
- `/commit` - 创建 Git 提交
- `/review-pr` - 审查 Pull Request

## 配置文件

### settings.json
主配置文件，控制 Claude Code 的行为：
- 权限设置
- 环境变量
- 自动化钩子

### CLAUDE.md
项目级指令文件，定义项目特定的规则和上下文。

### keybindings.json
自定义键盘快捷键配置。

## 最佳实践

1. **提供清晰的任务描述** - 越具体的问题会得到越好的回答
2. **利用 CLAUDE.md** - 为项目添加上下文说明
3. **善用技能系统** - 通过 `/技能名` 快速执行常见任务
4. **配置自动化钩子** - 提高开发效率

## 相关资源

- [官方文档](https://docs.anthropic.com/claude-code)
- [GitHub 仓库](https://github.com/anthropics/claude-code)
- [问题反馈](https://github.com/anthropics/claude-code/issues)

## 许可证

Claude Code 由 Anthropic 开发和维护，使用请遵循 Anthropic 的服务条款。