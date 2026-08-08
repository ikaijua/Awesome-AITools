# Conductor 入门介绍

## 什么是 Conductor？

[Conductor](https://github.com/conductor-oss/conductor) 是一个开源的事件驱动 **AI Agentic 工作流引擎**，最初由 Netflix 构建，现由 Orkes 与开源社区积极维护。它为微服务编排、AI Agent 和长周期工作流提供持久化、高弹性的执行引擎，已在互联网规模的生产环境中得到验证。

Conductor 将编排逻辑与业务逻辑解耦：工作流图是声明式且确定性的，而 Worker 可以是任意语言的普通代码。这使其非常适合需要 survived 崩溃、重试和人工审批的 AI Agent 循环，而不会丢失执行状态。

## 核心定位

### 从微服务编排到 AI Agent 引擎

Conductor 最初是 Netflix 的微服务工作流引擎。随着 Agentic AI 的兴起，它逐步演进为面向 AI Agent 的持久化执行平台，增加了原生 LLM 任务类型、MCP 工具调用、function calling、面向 RAG 的向量数据库支持以及人工审批节点。

### 持久化设计

每个工作流步骤都会被持久化。即使发生服务器重启、网络故障或长时间暂停（数天、数周甚至数月）等待外部信号或人工审批，执行也能恢复。失败的步骤可以单独重试，无需重放整个工作流。

### 多语言、解耦的 Worker

Worker 从 Conductor 服务器轮询任务，执行后上报结果。Worker 可以用 Java、Python、Go、JavaScript、C#、Ruby 或 Rust 编写，业务逻辑不受框架约束。

## 核心功能

- **持久化执行** — 持久化状态，支持可配置的重试、超时和补偿任务。
- **AI Agent 编排** — 原生支持 14+ LLM 提供商、MCP 工具调用、function calling 以及面向 RAG 的向量数据库集成。
- **声明式工作流** — JSON/YAML 定义的工作流支持版本管理、可观测性，并可在内置 UI 中调试。
- **动态运行时行为** — 支持动态分支、子工作流和运行时解析的任务；LLM 可生成工作流，Conductor 立即执行。
- **完整可重放性** — 支持从头重启、从任意任务重跑，或仅重试失败步骤。
- **人工介入** — 内置审批任务和等待外部信号的能力。
- **自托管、无锁定** — Apache 2.0 许可证，支持 5 种持久化后端和 6 种消息代理。

## 快速开始

### 使用官方 CLI 本地运行

前置条件：Node.js v16+ 和 Java 21+。

```bash
npm install -g @conductor-oss/conductor-cli
conductor server start
```

打开 http://localhost:8080 使用内置 UI。

### 使用 Docker 运行

```bash
docker run -p 5000:5000 -p 8080:8080 conductoross/conductor:next
```

UI 地址 http://localhost:5000，API 地址 http://localhost:8080。

### 定义并运行第一个工作流

```bash
curl -s https://raw.githubusercontent.com/conductor-oss/conductor/main/docs/quickstart/workflow.json -o workflow.json
conductor workflow create workflow.json
conductor workflow start -w hello_workflow --sync
```

## 最佳实践

1. **Worker 保持无状态** — 让 Conductor 拥有状态和编排逻辑，Worker 本身应是幂等的。
2. **使用版本化的工作流定义** — 部署新版本时不会破坏正在运行的执行实例。
3. **设置合理的重试和超时** — Conductor 可以重试失败任务，但策略应与下游服务行为匹配。
4. **启用可观测性** — 使用内置 UI 检查每个任务的输入、输出、耗时和重试历史。
5. **限制 Worker 权限** — 仅授予 Worker 所需凭证，对破坏性或高风险操作设置审批任务。

## 安全提示

Conductor 可以执行任意 Worker 代码、通过 MCP 调用外部 API，并读写向量数据库。请在隔离环境中运行 Worker，限制网络访问，并对危险操作要求人工审批。

## 相关资源

- [GitHub 仓库](https://github.com/conductor-oss/conductor)
- [官方文档](https://conductor-oss.github.io/conductor/)
- [面向 AI 编程助手的 Conductor Skills](https://github.com/conductor-oss/conductor-skills)

## 许可证

Conductor 采用 Apache 2.0 许可证。
