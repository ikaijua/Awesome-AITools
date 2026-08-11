# TencentDB Agent Memory 入门介绍

## 什么是 TencentDB Agent Memory？

[TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) 是腾讯云开源的 AI 智能体记忆基础设施。它要解决一个实际问题：如何在使用 Agent 时减少重复劳动，让经验可以积累、流动并传递给下一个 Agent。

它不是把记忆简单等同于对话历史，而是把有价值的信息转化为可复用的记忆资产——包括 Chat Memory、Skill、Wiki 和 CodeGraph——让新的会话和新的 Agent 都能从已有经验出发，而不是从零开始。

## 核心概念

### 面向智能体团队的 Memory Hub
Memory Hub 覆盖智能体经验的全生命周期：

- **自动资产抽取**：从对话和任务中提取 Chat Memory 与 Skill；把文档和代码转化为 Wiki 与 CodeGraph。
- **可移植、多 Agent 兼容**：记忆资产与具体 Agent 框架解耦，可在不同框架之间流转，也可在多个 Agent 和团队成员之间共享。
- **冷启动友好**：支持导入现有文档、代码库和历史 Agent 会话，新团队可以直接从沉淀的经验开始。

### 记住人和上下文的“大脑”
- **Chat Memory** 保留偏好、事实、决策和交互历史。
- 每个 Agent 创建时自动获得自己的记忆，下次无需重新自我介绍。
- 原始对话经过四层蒸馏：L0 原始对话 → L1 原子 → L2 场景 → L3 人格。

### 沉淀专业知识的 Skill 库
- 完成复杂工作后，Agent 可以从对话和工具调用中提取可复用的 Skill。
- Skill 不只是提示词片段，还包含版本、资源文件、触发边界、执行步骤和校验规则。
- 个人 Skill 默认私有，经过审核后可共享给团队。

### 阅读文档和代码的知识地图
- **Wiki**：把产品文档、设计规范和运维手册转化为带链接图谱的结构化页面。
- **CodeGraph**：索引代码库，让 Agent 无需重读每个文件即可理解和推理项目。

## 核心功能

- **跨会话记忆**：在不同 Agent 会话之间保持上下文。
- **跨 Agent 共享**：记忆资产可被不同 Agent 和框架复用。
- **Skill 提取与版本管理**：把重复工作流转化为可版本化的可复用 Skill。
- **文档与代码索引**：基于现有知识构建 Wiki 和 CodeGraph。
- **本地优先部署**：可自托管 memory-core、memory-hub 和 proxy 服务。
- **IDE/Agent 集成**：通过 proxy 与 Claude Code、CodeBuddy 等 Agent 协同工作。

## 系统要求

上游仓库没有公布明确的 CPU/内存/GPU 配置要求。根据默认本地部署方式，整体资源占用较轻：

- **操作系统**：Linux、macOS 或 Windows（Windows 建议用 WSL2）
- **CPU**：任意现代 x86_64 或 ARM64 CPU，无需 GPU
- **内存**：最低 4 GB；如果与 Agent 框架（如 OpenClaw 或 Hermes）同机运行，建议 8 GB
- **磁盘**：取决于会话量，建议预留数 GB 可用空间
- **运行环境依赖**
  - Node.js >= 22.16.0 和 npm
  - Python 3.x
  - Docker 和 Docker Compose（推荐一键部署时使用）
- **外部依赖**
  - LLM API key：用于记忆提取和 proxy 推理，支持 OpenAI 兼容接口
  - 默认本地后端使用 SQLite + sqlite-vec，无需单独部署向量数据库

## 快速开始

### 前置要求
- Docker 和 Docker Compose（推荐）
- 两组 LLM API 凭证：一组给 memory 服务，一组给 proxy 服务

### 一键本地启动

```bash
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images
cp .env.example .env
# 编辑 .env，填入你的 LLM 参数
./start-all.sh
```

启动完成后，脚本会输出一行配置，可直接粘贴到 Claude Code 或 CodeBuddy 中使用。

打开 Web 面板：http://localhost:8125

关于独立部署、仅部署 Proxy，或从旧版本迁移，详见上游仓库中的 `INSTALL.md`（英文）和 `INSTALL_CN.md`（中文）。
