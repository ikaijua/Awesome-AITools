# QM 介绍

## 什么是 QM？

[QM](https://github.com/yc-software/qm) 是 Y Combinator 开源的**面向企业组织的 multi-agent harness**，运行在 Slack 和 Web 上。它的核心设计不是成为个人助理，而是围绕公司组织结构来编排智能体。

QM 的核心概念是 **scope（作用域）**：每个员工、项目、频道都拥有隔离的工作区，包含各自的记忆、文件、凭据、权限和定时任务。代理以所服务对象的身份工作，继承其凭据和权限，因此访问控制遵循真实的组织边界。

## 核心定位

### 从个人助理到组织级代理
YC 在经历过三轮尝试（基础 agent loop、增加 cron/webhook、使用 OpenClaw/Hermes agents）后发现，管理公司里的几十个代理非常麻烦，因此催生了 QM。QM 把“组织”本身作为协调单元。

### 基于作用域的隔离
每个作用域都是一个自包含单元：记忆、文件、凭据、权限和定时任务都绑定到具体的人、项目或频道。这避免了“拥有全部权限的超级代理”问题，同时让所有操作可审计。

### 无界面、可替换的核心
QM 采用 headless core（API、身份、策略、调度）与 Web UI / Slack 客户端分离的架构。PostgreSQL 提供持久化，模型提供商和 agent harness 均可替换，团队不会被锁定在单一厂商。

## 核心功能

- **基于作用域的工作区** — 按员工/项目/频道隔离记忆、文件、凭据和权限。
- **Slack 与 Web 客户端** — 在团队日常工作的场景中调用代理。
- **Headless 核心** — API 优先设计，UI 和聊天界面可插拔。
- **代理身份镜像** — 代理以所服务人员的身份行动，继承其凭据和权限。
- **可审计** — 所有代理行为都可追溯，且处于明确作用域内。
- **可自托管** — 支持通过 Docker、Fly.io 或 AWS 部署。
- **人类可读贡献** — 接受人类编写的 `.txt` / `.md` 文本贡献，而非直接提交代码。

## 快速开始

### 环境要求
- Node.js 与 pnpm
- PostgreSQL
- Slack 工作区（可选，用于 Slack 集成）

### 本地安装运行

```bash
git clone https://github.com/yc-software/qm.git
cd qm
# 按照仓库 README 的指引完成配置
pnpm install
pnpm dev
```

### Docker 部署

```bash
# 使用仓库提供的 Dockerfile 和 compose 配置
docker build -t qm .
docker run -e DATABASE_URL=postgres://... qm
```

## 最佳实践

1. **严格限定代理作用域** — 为团队、项目和敏感职能创建独立作用域。
2. **镜像真实权限** — 让代理使用所服务人员的凭据，而非共享的超级凭据。
3. **审查审计日志** — 定期检查代理执行了什么操作、代表谁执行。
4. **从低风险工作流开始** — 先自动化报告、摘要、通知等，再考虑开放写入权限。
5. **敏感数据自托管** — 将公司数据和凭据保留在自己的基础设施内。

## 安全提示

QM 是早期实验性软件。项目透明地列出了已知限制（例如命令策略可被绕过、sandbox 凭据明文存储等）。在部署到生产环境或授予敏感系统访问权限之前，请务必阅读仓库的安全文档。

## 相关资源

- [GitHub 仓库](https://github.com/yc-software/qm)
- [Y Combinator](https://www.ycombinator.com/)
- [OpenClaw](https://github.com/openclaw/openclaw) — QM 演进过程中参考的 harness 之一
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — QM 生态中的另一款代理框架

## 许可证

QM 使用其 [GitHub 仓库](https://github.com/yc-software/qm) 中指定的许可证。
