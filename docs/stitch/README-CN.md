# Stitch 介绍

## 什么是 Stitch？

[Stitch](https://stitch.withgoogle.com/) 是 Google Labs 推出的实验性 **AI 驱动 UI 设计工具**。它可以将文字提示、草图或语音描述转化为高保真界面原型与前端代码，弥合设计思路与可用 UI 之间的差距。

Stitch 的核心理念是 **"氛围设计（vibe design）"**：你描述界面应该给人什么感觉或达成什么目标，工具就会自动生成视觉布局、设计系统和交互流程。设计结果可以导出到 Figma，也可以输出 HTML/CSS 代码供进一步开发。

## 核心定位

### 面向智能体时代的设计
Stitch 专为与 AI 编码代理协同工作而设计。它提供 SDK 和 MCP Server，让 Claude Code、Cursor、Gemini CLI 等代理能够以编程方式读取设计 token、组件和原型，从而把氛围设计直接连接到氛围编码（vibe coding）。

### 从提示到交互原型
设计师和开发者无需从空白画布开始，只需描述希望用户感受到什么、完成什么任务，Stitch 就能生成多屏原型、应用设计系统，并支持通过语音或直接操作进行迭代。

### 现有工具的补充
Stitch 并不打算取代 Figma 或 Android Studio，而是作为快速构思与原型层：在 Stitch 中生成概念，到 Figma 中精修，再导入常用 IDE 实现。

## 核心功能

- **文生 UI** — 通过自然语言提示生成高保真界面。
- **草图与语音输入** — 将手绘草图或语音描述转化为布局。
- **多屏原型** — 创建相互关联的页面与交互流程。
- **设计系统支持** — 内置多种设计系统，也可导入自有系统。
- **代码导出** — 将生成的设计导出为 HTML/CSS，或在 Google AI Studio 中进一步生成代码。
- **Figma 集成** — 将设计发送到 Figma 进行细节打磨。
- **MCP Server 与 SDK** — 将 Stitch 接入编码代理和编辑器工作流。
- **实时引导** — 通过对话或直接操作实时调整布局与样式，无需重写提示词。

## 快速开始

### 使用网页版

访问 [stitch.withgoogle.com](https://stitch.withgoogle.com/) 并使用 Google 账号登录。

### 创建设计

1. 输入提示词，例如：
   > "为一家让用户学习 AI 与自动化的教育平台设计一个仪表盘。"
2. Stitch 生成多屏布局。
3. 通过提示词、语音或直接编辑进行迭代。
4. 导出到 Figma，或复制生成的前端代码。

### 接入编码代理

安装 Stitch MCP Server 和 SDK（官方文档中有说明），让代理直接访问你的设计 token 和组件。

## 最佳实践

1. **从用户目标出发，而非组件** — 先描述用户应该感受到什么、完成什么，再细化视觉。
2. **用 Figma 做最终精修** — 把 Stitch 的输出当作设计系统细化的起点。
3. **尽早固定设计 token** — 一致的 token 能大幅提升代理实现代码的成功率。
4. **用语音迭代更快捷** — 对于布局微调，语音引导通常比重写提示词更快。
5. **导出的代码需人工审查** — 与所有 AI 生成内容一样，代码应经过 review 和测试后再上线。

## 局限性

- 更适合概念与原型，而非可直接投产的应用。
- 预览期有月度使用额度限制。
- 当前预览版仅支持英文。
- 生成质量高度依赖提示词的具体程度。

## 相关资源

- [官方网站](https://stitch.withgoogle.com/)
- [Stitch 使用指南](https://scriptbyai.com/google-stitch/) — 社区整理的优缺点参考
- [Google AI Studio](https://aistudio.google.com/) — 可基于 Stitch 设计进一步生成代码
- [Figma](https://www.figma.com/) — 推荐的精修目的地

## 许可证

Stitch 是 Google Labs 的实验性产品，使用条款见 [stitch.withgoogle.com](https://stitch.withgoogle.com/)。
