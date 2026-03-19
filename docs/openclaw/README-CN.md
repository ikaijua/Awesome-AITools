# OpenClaw 简介

## 什么是 OpenClaw？

OpenClaw 是一个开源的自托管 AI 智能体，可以在本地运行并自主执行任务。它能够连接多种消息平台，控制浏览器，访问系统，具有持久记忆功能。由 Peter Steinberger 开发，在 GitHub 上获得了超过 18 万星标，是增长最快的开源项目之一。

## 核心思想

### 真正自主的 AI 助手
普通的 AI 只能陪你聊天，但 OpenClaw 可以真正"动手做事"。你告诉它一个目标，它会自己规划步骤、使用工具、执行任务，直到目标完成。

### 隐私优先
所有数据都在你自己的机器上运行：
- 不需要把敏感信息发给第三方服务
- 完全掌控自己的数据和配置
- 适合对隐私要求高的场景

### 持久记忆
OpenClaw 能记住你们之前的对话：
- 知道你的偏好和习惯
- 能继续之前的任务
- 越用越懂你

## 核心功能

### 多平台连接
支持连接主流消息平台：
- WhatsApp
- Telegram
- Slack
- Discord

### 浏览器控制
- 自动浏览网页
- 提取网页信息
- 填写表单、点击按钮

### 系统访问
- 读写本地文件
- 执行系统命令
- 与本地应用交互

### 工具集成
- 搜索引擎
- 数据分析
- 代码执行

## 快速开始

### 安装

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pip install -r requirements.txt
```

### 配置

1. 复制配置模板：
```bash
cp config.example.yaml config.yaml
```

2. 编辑配置文件，填入你的 API 密钥和平台凭据

### 启动

```bash
python main.py
```

## 最佳实践

1. **明确目标** - 告诉 OpenClaw 你想要什么结果，而不是具体怎么做
2. **设置边界** - 在配置中定义它可以访问哪些资源和执行哪些操作
3. **定期检查** - 查看它的执行日志，了解它在做什么
4. **逐步授权** - 先给它较少的权限，确认可信后再扩展

## 相关资源

- [GitHub 仓库](https://github.com/openclaw/openclaw)
- [官方文档](https://docs.openclaw.ai)
- [社区讨论](https://github.com/openclaw/openclaw/discussions)

## 许可证

OpenClaw 是开源项目，请遵循其开源许可证使用。