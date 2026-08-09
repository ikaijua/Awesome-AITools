# Trae Code

Trae Code（原名 Trae Agent）是字节跳动开源的面向通用软件工程任务的 LLM 智能体，提供终端 CLI 界面，能够理解自然语言指令并使用多种工具和 LLM 提供商执行复杂的软件工程工作流。

## 核心特点

- **终端原生 Agent**：通过 `trae-cli run` 和 `trae-cli interactive` 在命令行中直接指派任务、迭代开发。
- **多模型支持**：支持 OpenAI、Anthropic、Google Gemini、OpenRouter、Ollama、Azure、豆包（Doubao）等多种模型提供商。
- **研究友好架构**：透明、模块化的 Agent 架构，便于研究者修改、扩展和分析 Agent 行为。
- **丰富工具生态**：文件编辑、Bash 执行、顺序思考、任务完成等内置工具，并支持 MCP 扩展。
- **轨迹记录**：自动记录 LLM 交互、工具调用和执行元数据，便于调试与分析。
- **Docker 模式**：支持在指定 Docker 容器或镜像中运行任务，隔离开发环境。
- **YAML 配置**：基于 YAML 的配置文件，支持环境变量覆盖，命令行参数优先级最高。

## 安装

需要 Python 3.12+ 和 [uv](https://docs.astral.sh/uv/)：

```bash
git clone https://github.com/bytedance/trae-agent.git
cd trae-agent
uv sync --all-extras
source .venv/bin/activate
```

## 快速使用

```bash
# 执行单个任务
trae-cli run "Create a hello world Python script"

# 交互模式
trae-cli interactive

# 指定模型提供商
trae-cli run "Fix the bug in main.py" --provider anthropic --model claude-sonnet-4-20250514

# 保存执行轨迹
trae-cli run "Debug authentication" --trajectory-file debug_session.json
```

## 与 Claude Code / Codex / Kimi Code 的对比

| 方面 | Trae Code | Claude Code | Codex | Kimi Code |
|------|-----------|-------------|-------|-----------|
| 开发者 | 字节跳动 | Anthropic | OpenAI | Moonshot AI |
| 形态 | 终端 CLI | 终端 CLI + IDE 插件 + 桌面/Web/App | 终端 CLI + IDE 扩展 + 桌面 App + Codex Web | 终端 CLI + ACP 编辑器 + 本地 Web UI |
| 开源 | ✅ MIT | ❌ | ✅ Apache-2.0 | ⚠️ CLI MIT，核心不开源 |
| 多模型 | OpenAI / Anthropic / Gemini / OpenRouter / Ollama / 豆包 等 | Claude 系列 | GPT / Codex 系列 | Kimi / 兼容供应商 |
| 特色 | 研究友好的模块化架构、轨迹记录、Docker 模式 | 项目记忆、Remote Control | 内核级沙箱、ChatGPT relay 同步 | 视频输入、Goal 模式、`kimi web` |

## 相关链接

- 官网: [trae.ai](https://www.trae.ai/)
- GitHub: [bytedance/trae-agent](https://github.com/bytedance/trae-agent)
- 技术报告: [arXiv:2507.23370](https://arxiv.org/abs/2507.23370)
