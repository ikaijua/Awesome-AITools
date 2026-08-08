# Agency Agents 简介

## 什么是 Agency Agents？

[Agency Agents](https://github.com/msitarzewski/agency-agents) 是一个开源的 **AI 代理角色集合**，包含 **230+ 个专业领域的代理人设，像一个完整的数字化代理公司。每个代理都是特定领域的专家，拥有独特的人设、工作流、可交付成果和成功指标，覆盖工程、设计、营销、销售、金融、游戏开发、医疗等多个领域。

该项目还提供一个**原生桌面应用**（[agencyagents.app](https://agencyagents.app/)），支持 macOS、Linux 和 Windows，可以浏览完整代理列表并一键安装到 Claude Code、Cursor、Codex、Gemini、Kimi Code、Aider、Windsurf 等 AI 开发工具中。

## 核心定位

### 每个任务都有专家
与泛泛的"扮演开发者"提示词不同，Agency Agents 提供深入、角色特定的专家人设——从前端开发、后端架构，到 Reddit 社区运营、FinOps 工程师、临床证据代理等。每个人设都包含身份、记忆、使命、规则、可交付成果和工作流。

### 原生桌面应用
桌面应用省去了手动克隆仓库或运行安装脚本的步骤。它能自动检测已支持的工具，安装所选代理并保持同步更新。

### 多工具支持
代理文件兼容主流 Agentic 编码平台，包括 Claude Code、GitHub Copilot、Cursor、Aider、Windsurf、Codex、Gemini CLI、Kimi Code、OpenCode、Antigravity、Osaurus 等。

## 核心功能

- **230+ 个专业代理**，覆盖 15+ 个部门（工程、设计、营销、销售、产品、测试、安全、金融、游戏开发、GIS、医疗等）。
- **人设驱动** — 每个代理都有独特的声音、沟通风格和工作方式。
- **以交付物为核心** — 输出包括代码、文档、审计报告、计划书等具体成果。
- **工作流模板** — 包含分步流程、成功指标和质量门槛。
- **原生桌面应用** — 跨工具浏览、安装和更新代理。
- **开源且可分叉** — 基于 Markdown 的透明代理文件，可根据自身需求调整。

## 快速开始

### 方式一：桌面应用（推荐）

从 [agencyagents.app](https://agencyagents.app/) 下载原生应用，或在 macOS 上通过 Homebrew 安装：

```bash
brew install --cask msitarzewski/agency-agents/agency-agents
```

然后选择需要的工具和部门，应用会自动完成代理安装。

### 方式二：为 Claude Code 手动安装

```bash
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents
./scripts/install.sh --tool claude-code
```

或只复制某个部门：

```bash
cp engineering/*.md ~/.claude/agents/
```

### 方式三：转换为多种工具格式

```bash
./scripts/convert.sh
./scripts/install.sh
```

安装程序会自动检测已支持的工具，并安装对应格式。

## 最佳实践

1. **选择具体角色** — 根据任务选择最具体的代理，而不是通用代理。
2. **按需安装部门** — 一次性安装所有代理可能会让工具菜单过于拥挤，只安装实际需要的团队。
3. **提前确认交付物** — 每个代理都列出了预期输出，可用于明确你的请求。
4. **组合使用代理** — 针对跨职能项目，可以按顺序或并行使用多个代理。
5. **保持桌面应用更新** — 桌面应用会自动同步新代理和已支持工具的格式变更。

## 相关资源

- [GitHub 仓库](https://github.com/msitarzewski/agency-agents)
- [桌面应用](https://agencyagents.app/)
- [代理列表](https://github.com/msitarzewski/agency-agents#-the-agency-roster)

## 许可证

详见仓库中的 [LICENSE](https://github.com/msitarzewski/agency-agents/blob/main/LICENSE) 文件。
