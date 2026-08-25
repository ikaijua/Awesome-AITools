# Dify 入门介绍

## Dify 是什么？

[Dify](https://github.com/langgenius/dify) 是一个开源的 LLM 应用开发平台。它将可视化应用构建、RAG 知识库、Agent 工作流编排、模型路由和可观测性集成在一起，帮助团队更快地将 AI 应用从原型推进到生产环境。

## 核心定位

### 可视化 LLM 应用构建
Dify 提供拖拽式界面来设计聊天机器人、Agent 和复杂工作流，无需编写样板代码。内置提示词版本管理、结构化输出和多轮对话管理。

### RAG 与知识库
上传文档、网页或结构化数据，即可构建检索增强生成应用。Dify 负责文本分块、嵌入、向量存储和重排序，并支持可配置的检索策略。

### Agent 与工作流编排
创建多步骤工作流和自主 Agent，支持调用工具、调用 API、条件判断和循环执行，直到任务完成。支持条件分支、循环和人机协同审批。

### 模型编排
通过统一接口接入 OpenAI、Anthropic、Gemini、DeepSeek、Ollama 本地模型等众多模型提供商。无需重写应用逻辑即可切换模型或按任务路由。

### 可观测性与运维
内置日志、追踪、标注和评估工具，帮助团队监控生产使用、调试失败并持续优化提示词和检索质量。

## 快速开始

### 使用 Docker 自托管

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
```

默认打开 `http://localhost` 即可访问 Web UI。

### 托管云版本

访问 [dify.ai](https://dify.ai/) 注册使用托管版。

## 相关资源

- [GitHub 仓库](https://github.com/langgenius/dify)
- [官方文档](https://docs.dify.ai/)
- [官方网站](https://dify.ai/)

## 许可证

Dify 采用 Apache 2.0 许可证。
