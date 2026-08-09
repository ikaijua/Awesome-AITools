# Qoder 简介

## 什么是 Qoder？

Qoder 是阿里云推出的 AI 智能编程助手与智能体产品族，主打“自主编程新范式”。它通过多智能体协同、长时委派执行、记忆与知识引擎，与代码库和工具链深度连接，围绕真实软件开发任务持续完成理解、规划、执行、验证与迭代，直到交付可用结果。

## 核心思想

### 从“代码补全”到“自主交付”

传统编程助手主要提供单行或函数级补全，Qoder 则希望让 AI 围绕真实任务端到端地推进：

- 理解代码库结构与业务目标
- 自主规划实现步骤
- 调用工具、编辑文件、运行命令
- 验证结果并持续迭代

### 多智能体协同

Qoder 将复杂开发任务拆分为多个可协作的智能体，各自负责规划、编码、测试、审查等角色，通过协同完成比单轮对话更复杂的工程目标。

### 深度上下文与记忆

通过深度代码库分析和自适应记忆，Qoder 能在长会话甚至跨会话中保留项目上下文，减少重复解释，让 AI 真正伴随项目成长。

### 目标导向的闭环

以清晰的目标和交付物驱动智能体，形成“规划 → 执行 → 验证 → 迭代”的闭环，直到任务完成。

## 产品族

| 产品 | 定位 | 适用场景 |
| --- | --- | --- |
| **Qoder Desktop** | 原生桌面 IDE，自主开发工作台 | 日常软件开发、代码编辑、调试 |
| **Qoder CLI** | 终端原生 AI 编程搭档 / 可集成的智能体引擎 | 命令行开发、CI/CD、自动化脚本 |
| **QoderWork** | 本地运行、自主规划、安全可控的 AI 工作搭子 | 本地文件处理、数据分析、内容创作 |
| **QoderWake** | 全天在线的数字员工 | 定时任务、持续监控、自动执行 |
| **Cloud Agents** | 面向企业的云端全托管 AI Agent 平台 | 企业多场景集成、团队协作 |

此外，Qoder 也提供 JetBrains 插件和 VS Code 插件，方便在现有 IDE 中使用。

## 核心能力

### 智能体自主性

- 理解意图、拆解任务、调用工具
- 在复杂工作流中独立推进执行
- 遇到问题时自主决策或请求确认

### 上下文工程

- 深度代码库分析
- 自适应记忆与知识库
- 长上下文保持

### 工具链集成

- 内置多种编程工具
- 支持 MCP（Model Context Protocol）工具
- 可执行终端命令、调用 IDE 能力

### 多模型支持

- 支持阿里云百炼等模型服务
- 可配置不同专项模型（如代码模型）
- 满足不同任务对性能与成本的偏好

## 快速开始

### 下载桌面端

访问 [Qoder 下载中心](https://qoder.com.cn/download)，选择对应系统安装包：

- macOS 12+
- Windows 10+
- Linux（.deb / .rpm）

安装后使用阿里云账号登录即可开始使用。

### 安装 Qoder CLI

**macOS / Linux**

```bash
curl -fsSL https://qoder.com.cn/install | bash
```

**Windows PowerShell**

```powershell
irm https://qoder.com.cn/install.ps1 | iex
```

**Windows CMD**

```cmd
curl -fsSL https://qoder.com.cn/install.cmd -o install.cmd && install.cmd
```

安装完成后，可在终端中使用 `qodercli` 启动。

> 更详细的 CLI 安装与使用说明可参考 [Qoder 官方文档](https://docs.qoder.com/zh/cli/installation)。

### 安装 IDE 插件

- **VS Code**：在扩展市场搜索“Qoder CN”，安装阿里云官方插件。
- **JetBrains**：从官网下载插件包后，通过 `File → Settings → Plugins → Install Plugin from Disk` 安装。

## 常用场景

1. **需求到代码**：描述功能需求，让 Qoder 自主完成实现、测试与验证。
2. **Bug 修复**：提供错误现象，Qoder 定位问题并给出修复方案。
3. **代码重构**：在保持行为不变的前提下，进行大规模结构调整。
4. **自动化脚本**：使用 Qoder CLI 在 CI/CD 或本地脚本中集成 AI 能力。
5. **本地办公自动化**：通过 QoderWork 处理文件、生成报告、分析数据。

## 最佳实践

1. **先描述目标再描述细节** - 让智能体理解“要做什么”，而不是只给局部提示。
2. **从可信仓库开始** - 在熟悉、已备份的项目中体验高自主度模式。
3. **审阅中间产物** - 把 Qoder 的改动当作同事的 PR 来 review。
4. **善用 Plan 模式** - 复杂任务先让 AI 输出计划，确认后再执行。
5. **配置项目记忆** - 利用记忆与知识引擎，减少每次重复交代项目背景。

## 相关资源

- [官方网站](https://qoder.com.cn/)
- [下载中心](https://qoder.com.cn/download)
- [官方文档](https://docs.qoder.com/zh/cli/installation)
- [阿里云开发者社区 - Qoder 专栏](https://developer.aliyun.com/)

## 许可证

Qoder 由阿里云提供服务，使用前请遵循阿里云相关服务条款与许可协议。
