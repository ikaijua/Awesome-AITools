# Grok 介绍

## 什么是 Grok？

Grok 是 xAI 推出的 AI 助手，可通过网页 [grok.com](https://grok.com/)、X（原 Twitter）平台内集成入口以及移动端 App 使用。当前旗舰模型为 **Grok 4.6**，上下文窗口 500K token，知识截止 2026-02-01。

Grok 的设计围绕两个核心点：**对 X 上公开信息的实时访问**，以及**多模态生成**（文本、图像、视频、语音）统一在同一个账号下。

## 核心理念

### 默认实时
Grok 最具差异化的能力是可以**实时访问 X 上的帖子和公开网络数据**。大多数助手受限于训练截止日期，而 Grok 能够在事件发生当下抓取并引用 X 上的帖子进行推理，X 帖文作为行内引用直接呈现。这让 Grok 成为突发新闻跟进、社交话题追踪、"现在大家在 X 上怎么说 X"这类问题的默认选择。

### 一个订阅，全模态覆盖
一个 Grok 账号即可使用：
- **文本**：Grok 4.6（对话、推理、智能体工具调用）
- **图像生成**：通过 **Imagine** API（Aurora 模型）
- **视频生成**：通过 Imagine API（480p / 720p / 1080p）
- **语音**：**Voice API** —— 实时语音对话、批量 STT 与 TTS

### 智能体与编程能力
Grok 4.6 同时被定位为编程模型，支持智能体工具调用、降低幻觉、可配置推理深度。同一个模型也驱动着 `grok` CLI（[Grok Build](docs/grok-build/README-CN.md)），用于终端编程工作流；并通过 Responses API 暴露，便于嵌入到第三方工具中。

## 核心功能

### 文本与推理
- Grok 4.6：500K token 上下文，可配置推理深度
- 内置 Web Search 和 X Search 工具获取实时数据
- 视觉输入 —— 在对话中直接分析图像
- 文件上传与分析

### 图像与视频（Imagine）
- 图像生成，擅长写实风格和 meme 风格图像
- 视频生成支持 480p / 720p / 1080p
- 支持对已有图像进行编辑和重新生成
- 在 Grok 对话和 API 中均可使用

### 语音
- 实时语音对语音对话
- 批量语音转文字
- 文字转语音合成

### API
- 兼容 OpenAI 风格的端点：`https://api.x.ai/v1`
- 原生 Responses API，用于智能体编程
- 提供官方 Python SDK（`xai_sdk`）、TypeScript SDK（`@ai-sdk/xai`）以及 OpenAI 兼容客户端

## 快速开始

### 网页与 App
- **网页**：[grok.com](https://grok.com/)
- **X 集成**：内置在 [x.com](https://x.com/) 中（侧边栏的 Grok）
- **移动端**：iOS 和 Android 上的 Grok 品牌 App

### API 接入

1. 在 [xAI Console](https://console.x.ai/) 创建 API Key。
2. 设置 `XAI_API_KEY` 环境变量。
3. 调用 OpenAI 兼容端点：

```sh
curl https://api.x.ai/v1/responses \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-4.6",
    "input": "总结 X 上关于 SpaceX 最新发射的热门帖子。"
  }'
```

或使用官方 Python SDK：

```python
import os
from xai_sdk import Client
from xai_sdk.chat import user

client = Client(api_key=os.getenv("XAI_API_KEY"))
chat = client.chat.create(model="grok-4.6")
chat.append(user("总结 X 上关于 SpaceX 最新发射的热门帖子。"))
print(chat.sample().content)
```

## 定价概览

| 项目 | 价格 |
| --- | --- |
| Grok 4.6 输入 | $2.00 / 1M tokens |
| Grok 4.6 输出 | $6.00 / 1M tokens |
| Voice Agent（实时） | $0.05 / 分钟起 |
| TTS | $15.00 / 1M 字符 |
| STT（批量） | $0.10 / 小时 |
| STT（流式） | $0.20 / 小时 |
| Imagine（图像） | 按张计费，详见控制台 |
| Imagine（视频） | $0.05 / 秒起 |

Grok 消费级 App 的免费/付费档位详见 [grok.com](https://grok.com/)，API 价格以 [xAI 定价页](https://docs.x.ai/docs/pricing) 为准。

## 注意事项

- **知识截止**：Grok 4.6 的训练数据截至 2026-02-01。处理该日期之后的事件，请使用 Web Search 或 X Search 工具。
- **对 X 的依赖**：Grok 的核心差异化建立在对 X 平台的持续访问之上，在 X 受限的区域行为可能不同。
- **编程场景**：如需终端编程工作流，请参考 [Grok Build](docs/grok-build/README-CN.md) —— 基于 Grok 4.6 构建的开源 `grok` CLI/TUI。

## 相关资源

- [Grok 主页](https://grok.com/)
- [xAI 官方文档](https://docs.x.ai/docs/overview)
- [xAI 模型列表](https://docs.x.ai/docs/models)
- [xAI 定价](https://docs.x.ai/docs/pricing)
- [API 参考](https://docs.x.ai/docs/api-reference)
- [Grok Build（CLI/TUI）](docs/grok-build/README-CN.md)
- [与其他工具的对比](../COMPARISON-CN.md)

## 许可证

Grok 消费级产品和 xAI API 均为 xAI 自有商业服务。[Grok-1](https://github.com/xai-org/grok-1) 基座模型权重以 Apache 2.0 许可证发布，但 Grok 消费级服务本身不开源。
