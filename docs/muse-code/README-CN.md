# Muse Code 简介

## 什么是 Muse Code？

Muse Code 是 Meta 于 2026 年 8 月 5 日发布的 Beta 版终端编程智能体，基于 Muse Spark 1.2 模型构建。该模型与智能体 harness 共同训练，面向跨大型代码库的完整软件工程任务。

## 核心特性

- **终端原生工作流**：一条命令安装，直接在 macOS 或 Linux 终端中使用。
- **持久后台代理**：专门化的后台代理在整个会话中保持活跃，而不是每次任务重新创建，减少重复探索。
- **并行子代理**：大型任务会被拆分到独立的 git worktree 中并行处理，不会触碰你的工作区。
- **追加式事件日志**：每次模型调用、工具执行、审批和编辑都会被记录到本地日志，会话可精确回放，崩溃后可恢复。
- **内置 Skills**：`/plan`、`/grill`、`/goal` 等命令帮助结构化长时程任务。
- **两档定价**：
  - **Standard（标准档）**：输入 $1.25 / 百万 token，输出 $4.25 / 百万 token。提示与补全不会被用于训练 Meta 模型。
  - **Contributor（贡献档）**：输入 $0.10 / 百万 token，输出 $0.20 / 百万 token，但需明确允许 Meta 使用你的提示和补全进行训练。

## 快速开始

在 macOS 或 Linux 上安装：

```bash
curl -fsSL https://dev.meta.ai/install.sh | bash
```

安装后使用 Meta 账号登录并添加支付方式，然后在项目目录中启动 Muse Code。

## 常用命令

```bash
# 在当前项目中启动交互式会话
muse code

# 先制定计划再修改文件
/plan

# 对计划进行压力测试
/grill

# 追踪既定目标的完成进度
/goal <目标描述>
```

> 注意：Muse Code 目前处于 Beta 阶段，需要 Meta 账号并绑定支付方式才能使用。

## 数据与隐私

Standard 档不会把你的提示和补全用于 Meta 的模型训练；Contributor 档价格显著更低，但明确允许 Meta 使用你的数据进行训练。请根据项目的隐私要求选择合适档位。

## 相关资源

- [官方产品页面](https://www.meta.ai/muse/code)
- [VentureBeat 发布报道](https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents)

## 许可证

Muse Code 与 Muse Spark 1.2 均为 Meta 专有服务，终端智能体和模型权重目前并非开源。
