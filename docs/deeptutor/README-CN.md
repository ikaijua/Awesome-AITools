# DeepTutor 简介

## 什么是 DeepTutor？

DeepTutor 是香港大学数据科学研究院（HKUDS）开源的 **AI 原生学习/辅导工作区**。它将 AI 辅导、解题、测验生成、研究、可视化和掌握式学习路径整合在一个可扩展系统中，所有模式都运行在同一个 Agent 循环上，让学习上下文在不同工作流之间自然延续。

## 核心能力

- **Chat、Quiz、Solve、Research** —— 切换目标而不是切换引擎，同一个 Agent 循环即可完成辅导对话、生成测验、逐步解题和深度研究。
- **Visualize 与 Mastery Path** —— 将概念转化为交互式可视化，并通过结构化学习路径与掌握关卡推进学习。
- **Partner 与 My Agents** —— 在任意回合中调用实时编程 CLI（Claude Code、Codex、Gemini CLI、Kimi Code、opencode、MiMo）或自定义 Partner 智能体。
- **连通的学习上下文** —— 知识库、Book、Co-Writer 草稿、笔记本、题库、人格设定和 Memory 在所有工作流中共享，而不是孤立存在。

## 知识库与 RAG

DeepTutor 支持多种检索引擎和文档解析器：

- **多引擎 RAG** —— 可选 LlamaIndex、PageIndex、GraphRAG、LightRAG，或链接 Obsidian 笔记库。
- **可插拔文档解析** —— 通过 MinerU、Docling、PyMuPDF4LLM 等后端摄入 PDF、DOCX、XLSX、PPTX 等格式。
- **版本化索引** —— 知识库索引支持版本管理，可在不丢失历史快照的情况下重新构建。

## 安装方式

支持四种部署形态：

1. **PyPI** —— `pip install deeptutor && deeptutor init && deeptutor start`
2. **源码** —— 克隆仓库，安装 Python 依赖与 Next.js 前端，然后 `deeptutor start`
3. **Docker** —— 运行预构建镜像 `ghcr.io/hkuds/deeptutor:latest`
4. **纯 CLI** —— 安装 `packaging/deeptutor-cli`，无需 Web UI 即可在终端使用

详细的安装步骤、模型供应商配置和 Docker Compose 示例请参考 [GitHub 仓库](https://github.com/HKUDS/DeepTutor)。

## 典型使用场景

- **自主学习** —— 上传教材或论文，提问、生成测验并跟踪掌握进度。
- **研究助手** —— 基于 arXiv 论文构建知识库，运行带可追溯引用的 Agentic 深度研究。
- **编程辅导** —— 接入编程 CLI Partner，以交互方式讲解代码、调试并解释算法。
- **课程创作** —— 使用 Book 引擎和 Co-Writer 编写包含嵌入式测验与可视化的动态课程材料。
