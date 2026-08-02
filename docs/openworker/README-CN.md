# OpenWorker 简介

## 什么是 OpenWorker？

OpenWorker 是吴恩达（Andrew Ng）发布的开源、本地优先桌面 AI 同事。它不是简单地返回聊天回复，而是把日常工作从头到尾执行完成：起草文档、发送 Slack 回复、更新日程、整理收件箱，并产出可直接使用的完整交付物。它运行在你自己的电脑上，连接你已有的工作工具，并允许你自带模型。

## 核心思想

### 以成果为目标的委托
用“我要什么结果”来下达任务——例如“准备周一简报”“起草客户跟进邮件”“理顺我的日程”——OpenWorker 会拆解步骤、跨工具协作，并返回可用的交付物。

### 本地优先的隐私
智能体循环、对话记录、连接器令牌和模型密钥都保存在你的设备上。数据只在经过你选择的模型和集成时离开本机。

### 模型无关
没有厂商锁定。你可以使用云服务商模型、开源权重模型，或通过 Ollama 完全本地运行，还能按任务切换模型。

## 核心功能

### 产出真实交付物
可生成文档、电子表格、报告、网页和消息草稿等成品，而不是待办清单或半成品草稿。

### 25+ 工具集成
可连接 Slack、Gmail、Outlook、Google Calendar、Notion、HubSpot、GitHub、Jira、Linear、Asana、Dropbox 等。任何支持 MCP 的工具也能按工具粒度加入并设置访问权限。

### 关键操作前确认
在发送消息、修改日程、写入文件或执行 shell 命令前，OpenWorker 会先询问并获得你的批准。

### 定时自动化
可设置周期性任务，如晨间简报、周报、收件箱检查、频道监控等。

### Slack 集成
在 Slack 频道中 @OpenWorker 即可开启桌面会话，处理结果会作为帖内回复返回。

## 快速开始

### 下载预编译应用

访问 [openworker.com](https://openworker.com) 下载 macOS（Apple Silicon）或 Windows（x64）桌面应用。

### 从源码运行

```bash
git clone https://github.com/andrewyng/openworker
cd openworker

# 一次性初始化（创建 .venv）
bash packaging/setup_dev_env.sh

# 启动本地智能体服务器
.venv/bin/openworker-server --cwd ~/some/project --port 8765

# 在另一个终端启动 UI
cd surfaces/gui
npm install
npm run dev
```

如需完整桌面应用，将最后一步替换为 `npm run tauri dev`。

## 最佳实践

1. **描述成果，而非步骤** - 说明你想要什么交付物，而不是逐项指挥工作流。
2. **从有限权限开始** - 随着信任建立，逐步批准工具访问权限。
3. **留意确认提示** - 关键操作都会被拦截确认，利用它们保持掌控。
4. **敏感工作使用本地模型** - Ollama 支持让数据完全不出本机。

## 相关资源

- [GitHub 仓库](https://github.com/andrewyng/openworker)
- [官方网站](https://openworker.com)
- [问题与讨论](https://github.com/andrewyng/openworker/issues)

## 许可证

OpenWorker 采用 MIT 许可证发布，使用时请遵循其开源许可证。
