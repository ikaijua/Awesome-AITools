# Gemini CLI 简介

## 什么是 Gemini CLI？

Gemini CLI 是一个开源的命令行终端 AI 智能体，将 Google Gemini 的强大能力直接带入你的终端。它让你可以在命令行环境中与 Gemini AI 进行交互，完成各种编程和信息处理任务。

## 核心思想

### 命令行原生体验
Gemini CLI 专为终端用户设计：
- 无需切换到浏览器或其他应用
- 保持你在终端的工作流
- 适合服务器环境和无头操作

### Google AI 能力
直接调用 Google 最新的 Gemini 模型：
- 强大的代码理解和生成能力
- 多模态支持（文本、图片）
- 长上下文处理

### 开源可控
- 完全开源，代码透明
- 可以自定义和扩展
- 社区驱动改进

## 核心功能

### 智能问答
- 在终端直接提问
- 获取代码建议和解释
- 文档查询和总结

### 代码辅助
- 代码补全和生成
- Bug 分析和修复建议
- 代码审查和优化

### 文件操作
- 读取和分析文件内容
- 生成和修改代码文件
- 批量处理文本

### 集成能力
- 与 shell 脚本配合
- 管道操作支持
- 输出格式化

## 快速开始

### 安装

```bash
# 使用 npm 安装
npm install -g @google/gemini-cli

# 或从源码安装
git clone https://github.com/google-gemini/gemini-cli.git
cd gemini-cli
npm install
npm link
```

### 配置

设置你的 Google AI API 密钥：

```bash
export GOOGLE_AI_API_KEY="your-api-key"
```

### 基本使用

```bash
# 启动交互模式
gemini

# 直接提问
gemini "解释一下这个正则表达式的含义"

# 分析文件
gemini "分析 main.py 的代码结构" < main.py

# 管道使用
cat error.log | gemini "帮我分析这个错误"
```

## 常用场景

### 代码调试
```bash
gemini "这段代码有什么问题？" < broken_code.py
```

### 学习新知识
```bash
gemini "解释一下 Docker 的工作原理"
```

### 文档生成
```bash
gemini "为这个函数生成文档注释" < my_function.js
```

## 与其他工具的对比

### Gemini CLI vs Claude Code

| 方面 | Gemini CLI | Claude Code |
|------|------------|-------------|
| 开发者 | Google | Anthropic |
| 开源程度 | 完全开源 | 非开源 |
| 多模态 | 支持图片等多模态 | 纯文本 |
| 记忆系统 | 无持久记忆 | 有持久化记忆 |
| 集成能力 | 与 Google 生态集成 | Git/GitHub/GitLab 深度集成 |

**选择建议**：如果你重视开源透明、需要多模态能力，选 Gemini CLI；如果需要项目级记忆和深度工作流集成，选 Claude Code。

### Gemini CLI vs Codex

| 方面 | Gemini CLI | Codex |
|------|------------|-------|
| 开发者 | Google | OpenAI |
| 开源程度 | 完全开源 | 非开源 |
| 多模态 | 支持图片等多模态 | 纯文本 |
| 使用门槛 | 需要 Google AI API 密钥 | 需要 OpenAI API 密钥 |
| 生态集成 | Google 服务 | OpenAI 服务 |

**选择建议**：如果你重视开源、需要多模态能力，选 Gemini CLI；如果你更熟悉 OpenAI 生态，选 Codex。

## 最佳实践

1. **明确提问** - 问题越具体，回答越有用
2. **提供上下文** - 用管道传入相关文件内容
3. **验证输出** - AI 生成的代码要经过测试
4. **利用交互** - 可以多轮对话逐步完善方案

## 相关资源

- [GitHub 仓库](https://github.com/google-gemini/gemini-cli)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API 文档](https://ai.google.dev/docs)

## 许可证

Gemini CLI 是开源项目，使用需要 Google AI API 密钥。请遵循 Google 的服务条款和开源许可证。