# Codex Security 入门介绍

## 什么是 Codex Security？

Codex Security 是 OpenAI 开源的一款 CLI 和 TypeScript SDK，用于发现、验证并修复代码中的安全漏洞。

## 核心功能

- **仓库扫描**：扫描本地代码库中的安全漏洞。
- **漏洞追踪**：跨多次运行追踪漏洞，并对比扫描结果。
- **修复验证**：验证修复是否真正解决了根本问题。
- **CI/CD 集成**：通过 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 在流水线中运行非交互式扫描。
- **TypeScript SDK**：将扫描能力直接嵌入 Node.js 应用。
- **容器化批量扫描**：使用官方 Docker 镜像进行可扩展、可恢复的批量扫描。

## 快速开始

```bash
npm install @openai/codex-security
npx @openai/codex-security login
npx @openai/codex-security scan .
```

在 CI 环境中：

```bash
export OPENAI_API_KEY=sk-...
npx @openai/codex-security scan .
```

## 链接

- [GitHub 仓库](https://github.com/openai/codex-security)
- [OpenAI Codex Security 文档](https://github.com/openai/codex-security/tree/main/docs)
