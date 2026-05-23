# Understand Anything 简介

## 什么是 Understand Anything?

**Understand Anything** 是一款基于 AI 的代码库和知识库分析工具，它能将复杂的项目转化为交互式的可视化知识图谱。它旨在通过交互式仪表盘提供“大局观”，帮助开发者快速掌握大型或陌生的代码库。

## 核心理念

### 可视化带来清晰度
传统的代码阅读是线性的，且容易让人疲于应付。Understand Anything 构建了文件、函数、类和依赖关系的图谱，使各种关系变得清晰且易于导航。

### 多智能体智能
该系统采用了一套由专业智能体（项目扫描器、文件分析器、架构分析器等）组成的流水线，自主提取逻辑、业务领域和架构模式。

### 上下文管理
它作为原始代码与 AI 智能体之间的关键桥梁，提供高层级上下文，从而减少 Token 消耗并提高 AI 编码助手的准确性。

## 核心功能

### 交互式知识图谱
- **可视化导航：** 代表文件、函数和类的可点击节点。
- **依赖映射：** 可视化系统中不同部分如何交互。

### 架构引导教程
- **逻辑顺序：** 自动生成按依赖关系排序的架构演练。
- **循序渐进学习：** 以逻辑化、结构化的方式教你理解代码库。

### 多平台集成
- **插件支持：** Claude Code 的原生插件。
- **广泛兼容：** 作为技能或自动发现的插件，支持 Cursor、VS Code (GitHub Copilot)、Cline 等。

### 高级分析
- **领域视图：** 将代码映射到现实世界的业务流程和流转。
- **变更影响分析：** 预测提议的更改将如何波及整个系统。
- **语义搜索：** 针对代码库结构提出自然语言问题。

## 快速入门

### 安装

Understand Anything 可以作为全局 CLI 工具安装，或集成到你喜爱的 AI 智能体中。

```bash
npm install -g understand-anything
```

### 基本用法

1. **扫描项目：** 运行扫描器以构建知识图谱。
   ```bash
   understand scan .
   ```
2. **打开仪表盘：** 启动交互式可视化。
   ```bash
   understand dashboard
   ```
3. **Claude Code 集成：** 直接在 Claude Code 中使用插件。
   ```bash
   /understand "身份验证流程是如何工作的？"
   ```

## 相关资源

- [GitHub 仓库](https://github.com/Lum1104/Understand-Anything)
- [官方网站](https://understandanything.ai)

## 开源协议

Understand Anything 是开源的，采用 MIT 协议。
