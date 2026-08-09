# Trae

Trae 是字节跳动推出的 AI 编程与工作智能体产品族，覆盖终端 CLI、IDE 和 Web/桌面/移动工作空间，为开发者和知识工作者提供从代码生成到通用办公任务的 AI 能力。

## 产品形态

| 产品/模式 | 形态 | 适用场景 |
|-----------|------|----------|
| **Trae Code** | 终端 CLI（`trae-cli`） | 喜欢在命令行中驱动 Agent 的开发者；支持自然语言任务、文件编辑、Bash、MCP、Docker 模式与轨迹记录。 |
| **Trae IDE – IDE Mode** | AI 原生 IDE | 传统 IDE 工作流：代码补全、聊天、仓库上下文、源码控制与终端。 |
| **Trae IDE – SOLO Mode** | IDE 内 Agent 模式 | 多文件开发任务：规划、编辑、运行命令并完成较大范围的功能实现或重构。 |
| **Trae Work – Code Mode** | Web/桌面/移动云端编程工作区 | 委派构建或编码任务，异步检查结果。 |
| **Trae Work – Work Mode** | Web/桌面/移动通用工作区 | 研究、写作、规划、数据分析、文档生产等通用办公任务。 |

## Trae Code 核心特点

- **终端原生 Agent**：通过 `trae-cli run` 和 `trae-cli interactive` 指派任务、迭代开发。
- **多模型支持**：OpenAI、Anthropic、Google Gemini、OpenRouter、Ollama、Azure、豆包（Doubao）等。
- **研究友好架构**：透明、模块化的 Agent 架构，便于扩展与分析。
- **丰富工具生态**：文件编辑、Bash 执行、顺序思考、任务完成，支持 MCP。
- **轨迹记录**：自动记录 LLM 交互、工具调用和执行元数据。
- **Docker 模式**：在指定容器或镜像中运行任务，隔离环境。

## Trae Work 核心特点

- **双模式工作空间**：Code Mode 专注编程任务，Work Mode 面向通用办公。
- **云端任务**：支持并发 Cloud tasks，可在后台运行多个长时任务。
- **多端覆盖**：同一账号可在 Web、桌面和移动端继续查看任务进展。
- **与 Trae IDE 共享能力**：代码库索引、规则、自定义 Agent 和 MCP 扩展。

## 快速安装 Trae Code

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
```

## 相关链接

- 官网: [trae.ai](https://www.trae.ai/)
- Trae Work Web: [trae.ai](https://www.trae.ai/)
- GitHub: [bytedance/trae-agent](https://github.com/bytedance/trae-agent)
- 技术报告: [arXiv:2507.23370](https://arxiv.org/abs/2507.23370)
