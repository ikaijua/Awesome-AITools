# Lightpanda 浏览器入门介绍

## 什么是 Lightpanda？

Lightpanda 是首款专为大模型（LLM）时代设计的开源无头浏览器。与传统的无头浏览器（如 Headless Chrome 或 Playwright）不同，Lightpanda 使用 **Zig** 语言从零开始构建，旨在实现极致的轻量化、高性能和 AI 原生支持。

## 核心特性

### 🚀 极致性能
- **快约 9 倍：** 执行速度显著快于 Headless Chrome。
- **内存占用减少约 16 倍：** 极低的资源消耗，允许在相同硬件上运行更多实例。
- **基于 Zig 构建：** 利用 Zig 语言的性能和内存安全性优势。

### 🤖 AI 原生支持
- **MCP 支持：** 原生支持 **Model Context Protocol (MCP)** 协议，使 AI 智能体（如 Claude Code, Gemini CLI 等）能够开箱即用地将其作为工具调用。
- **Markdown 输出：** 可以直接将网页内容转换为干净的 Markdown 格式，为 LLM 提供高质量、无噪声的上下文。

### 🛠️ 开发者友好
- **兼容 CDP：** 支持 Chrome DevTools Protocol，可与许多现有的自动化工具兼容。
- **完善的 JS 支持：** 搭载 V8 引擎，能够处理现代 SPA 和复杂的重 JavaScript 网站。
- **零配置集成：** 轻松集成到现有的智能体工作流中。

## 为什么选择 Lightpanda？

对于正在构建需要浏览网页的 AI 智能体的开发者来说，Lightpanda 解决了几个常见的痛点：
1. **基础设施成本：** 由于内存占用极低，可以在同一台服务器上运行更多数量的智能体。
2. **延迟：** 更快的页面加载和 JS 执行意味着更快的智能体响应速度。
3. **数据质量：** 干净的 Markdown 输出可有效防止因 HTML 噪声过多而导致的“LLM 幻觉”。

## 快速上手

Lightpanda 可以通过 Docker 运行，也可以作为独立二进制文件运行。

### 使用 Docker 运行

```bash
docker run -p 9222:9222 lightpanda/browser
```

### 作为 MCP 工具使用

将 Lightpanda 作为 MCP 服务器添加到您的智能体配置中（例如在 Claude Code 或 Gemini CLI 中），即可开启自主网页浏览能力。

## 相关资源

- [GitHub 仓库](https://github.com/lightpanda-io/browser)
- [官方网站](https://lightpanda.io)
- [项目文档](https://docs.lightpanda.io)

## 许可证

Lightpanda 是一个开源项目，具体许可证信息请参考其代码仓库。
