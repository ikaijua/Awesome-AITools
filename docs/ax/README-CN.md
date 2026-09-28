# AX

[AX](https://github.com/google/ax) 是 Google 开源的 agentic 编排运行时，定位为"Agent 时代的 Kubernetes"。项目创建于 2026-03-30，目前已获得 12.2k+ stars，仍在活跃开发中，官方 README 提示正式发布前可能出现重大破坏性变更。

## 主要功能

- 通过声明式 YAML 清单（而非命令式代码）定义智能体工作负载。
- 每个智能体任务在沙箱中运行，具备资源隔离和 CPU/内存限制。
- 提供 `ax suspend/resume` 暂停/恢复长时间任务、`ax ssh` 进入沙箱调试等生命周期控制能力。

## 核心抽象

- **Workspace**：预置的运行环境（Git 仓库、MCP 服务器、技能包），任务在其上运行。
- **Task**：在沙箱中执行的智能体任务，可配置 CPU/内存限制。
- **Model**：平台自身使用的大模型配置。

## 架构

AX 运行在 Google 的 **Agent Substrate** 之上，采用单集群设计，目标是支撑十亿级自主智能体工作负载。

## 快速开始

安装 `ax` CLI，具体安装与上手步骤详见官方仓库 README：<https://github.com/google/ax>。

## 链接

- [GitHub 仓库](https://github.com/google/ax)
