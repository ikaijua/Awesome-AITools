# OpenChamber 介绍

## 什么是 OpenChamber?

OpenChamber 是为 [OpenCode](https://opencode.ai) AI 编码 agent 打造的功能丰富的桌面、浏览器和移动端界面。你可以查看 diff、管理 agent、运行开发服务器，并在 AI 编码时把握全局——同一个会话可在终端、平板和手机之间无缝延续。

## 为什么使用 OpenChamber?

- **跨设备连续性** —— 在 TUI 中开始，在平板/手机上继续，再回到终端，始终是同一个会话。
- **远程访问** —— 通过浏览器随时随地使用 OpenCode。
- **熟悉的体验** —— 为偏好图形界面工作流的开发者提供可视化替代方案。

## 核心功能

### 通用（所有版本）
- 可分支的聊天时间线，支持 `/undo`、`/redo` 以及从早先回合一键分叉。
- 针对 diff、文件操作、权限和长任务进度的智能工具界面。
- 语音模式，支持语音输入和朗读回复。
- 单条提示即可发起多 agent 运行，使用隔离的 worktree 进行安全的并排对比。
- 应用内 Git 工作流：身份管理、提交、创建 PR、检查和合并。
- GitHub 原生工作流：从 issue 和 PR 启动会话并自动附带上下文。
- Plan/Build 模式，带独立的计划视图。
- 可在 diff、文件和计划上撰写内联评论并回传给 agent。
- 上下文可视化工具（token/成本明细、原始消息查看、活动摘要）。
- 集成终端和内置技能目录。

### Web / PWA
- 通过 Cloudflare 的 `quick`、`managed-remote`、`managed-local` 模式进行隧道访问。
- 扫码即用的引导流程，附带隧道二维码和密码 URL 助手。
- 移动优先的聊天控件、键盘安全布局和后台通知。
- 内置自更新与重启流程。

### 桌面端（macOS + Windows + Linux）
- 悬浮 Mini Chat，可始终置顶显示在编辑器或终端旁边。
- 支持多个原生窗口，分别用于不同项目或会话。
- 原生通知，一键在 VS Code、Cursor、终端、Finder 和资源管理器中打开。
- 本地与远程实例的主机切换，以及支持端口转发的 SSH 远程访问。

## 快速开始

1. 安装并运行 [OpenCode](https://opencode.ai)。
2. 从 [releases 页面](https://github.com/openchamber/openchamber/releases) 下载 OpenChamber，或访问 [openchamber.dev](https://openchamber.dev)。
3. 将 OpenChamber 连接到你的 OpenCode 实例（本地或远程）即可开始使用。

## 相关资源

- [官网](https://openchamber.dev)
- [GitHub 仓库](https://github.com/openchamber/openchamber)
- [OpenCode](https://opencode.ai)
