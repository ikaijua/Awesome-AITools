# MiniMax H3 介绍

## MiniMax H3 是什么？

MiniMax H3 是 [MiniMax](https://www.minimax.io/) 开源的**通用多模态生成系统**。与 MiniMax 面向 C 端用户的视频平台 [海螺 AI](https://hailuoai.com/video) 不同，H3 以模型形式发布，提供推理代码、权重和参考流水线，开发者可以在本地部署或集成到自己的产品中。

它在一个模型架构内统一了文本、图像、视频和音频的理解与生成，适合跨模态内容创作工作流。

## 核心能力

H3 以任务专用 checkpoint 形式发布，基础模型支持：

- **文生视频（T2V）** — 根据文本提示生成视频
- **图生视频（I2V）** — 为静态图片生成动画
- **首尾帧生视频（FL2VA）** — 根据起始帧和/或结束帧生成中间视频
- **文生音视频（T2VA）** — 根据文本同步生成音频和视频

项目为每种任务提供参考流水线，以及所需的 processor、tokenizer、text encoder、Visual VAE 和独立 Audio VAE 组件。

## 部署方式

官方仓库推荐以下推理框架：

| 框架 | 适用场景 | 链接 |
| --- | --- | --- |
| SGLang | 高性能服务化部署 | [cookbook](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/sglang) |
| vLLM | 可扩展推理 | [recipes](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/vllm) |
| diffusers | 轻量 Python 流水线加载 | [docs](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/diffusers) |
| ComfyUI | 可视化节点工作流 | [tutorial](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/comfyui) |

## 入口

| 资源 | 链接 |
| --- | --- |
| 官方仓库（代码 + 文档） | https://github.com/MiniMax-AI/MiniMax-H3 |
| 模型权重（HuggingFace） | https://huggingface.co/MiniMaxAI/MiniMax-H3 |
| 模型权重（ModelScope） | https://modelscope.cn/models/MiniMax/MiniMax-H3 |
| C 端产品 | https://hailuoai.com/video |
