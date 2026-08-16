# Pi 介绍

## 什么是 Pi？

Pi 是由 [earendil-works](https://github.com/earendil-works) 开源（MIT 许可）的智能体 harness 与自扩展 AI 编程智能体。它采用 TypeScript/Bun Monorepo 架构，设计上让模型负责“大脑”，Pi 负责“手脚”——工具调用、状态管理、界面与执行。

该项目以交互式终端编程智能体最为知名，但也发布了一系列可复用包，用于构建其他类型的智能体。

## 核心包

| 包 | 说明 |
| --- | --- |
| `@earendil-works/pi-coding-agent` | 交互式编程智能体 CLI |
| `@earendil-works/pi-agent-core` | 智能体运行时：工具调用与状态管理 |
| `@earendil-works/pi-ai` | 统一多厂商 LLM API（OpenAI、Anthropic、Google 等） |
| `@earendil-works/pi-telemetry` | 厂商无关的遥测合约与一致性测试 |
| `@earendil-works/pi-tui` | 支持差分渲染的终端 UI 库 |

## 核心理念

### 自扩展智能体
Pi 的设计目标是“一切皆可替换”：模型、工具、界面、审批策略都可以自定义。默认的 coding agent 只是一个起点，而非封闭产品。

### 供应链安全加固
Pi 将依赖变更视为需要人工审查的代码变更：
- 直接依赖精确锁定版本
- `package-lock.json` 是唯一真相源，pre-commit 钩子会阻止意外提交 lockfile 变更
- 发布的 CLI 包内嵌 `npm-shrinkwrap.json`，为 npm 用户锁定传递依赖
- CI 运行 `npm audit --omit=dev` 及签名验证

### 沙箱方案
Pi 默认没有内置权限系统，但文档提供了三种隔离方案：
- **Gondolin 扩展**：Pi 与 provider 认证留在宿主机，内置工具和 `!` 命令路由到本地 Linux 微虚拟机
- **普通 Docker**：将整个 `pi` 进程跑在本地容器中
- **OpenShell**：在受策略控制的沙箱中运行 Pi

## 快速开始

安装依赖时跳过生命周期脚本：

```sh
npm install --ignore-scripts
npm run build
./pi-test.sh   # 从源码运行 pi
```

从发布版源码构建独立二进制：

```sh
VERSION="<release-version>"
tar -xzf "pi-${VERSION}-source.tar.gz"
cd "pi-${VERSION}"
./scripts/build-binaries.sh --offline-model-data --platform linux-x64 --out "$PWD/out"
```

## 注意事项

- 新贡献者提交的 issue 和 PR 默认会被自动关闭，维护者每日会查看这些自动关闭项。
- 如需聊天自动化与工作流场景，可查看相关仓库 [`earendil-works/pi-chat`](https://github.com/earendil-works/pi-chat)。
- 一个知名 fork 是 [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi)，它在 Pi 的基础上增加了 LSP、DAP 调试、Python/Bun 代码执行等 IDE 风格功能。

## 相关资源

- [GitHub 仓库](https://github.com/earendil-works/pi)
- [项目官网](https://pi.dev)
- [Pi Chat](https://github.com/earendil-works/pi-chat)
- [oh-my-pi fork](https://github.com/can1357/oh-my-pi)
- [与其他工具的对比](../COMPARISON-CN.md)

## 许可证

Pi 采用 MIT 许可证发布。
