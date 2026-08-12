# VibeVoice 简介

## 什么是 VibeVoice？

VibeVoice 是微软开源的前沿语音 AI 模型家族，涵盖语音识别（ASR）和语音合成（TTS），专注于长音频处理与实时流式生成。

> 说明：由于被发现存在与研究目的不符的使用场景，VibeVoice-TTS 的训练代码已于 2025 年 9 月从官方仓库中移除。目前仓库仍保留 ASR 和实时 TTS 模型、文档及推理示例。

## 模型家族

### VibeVoice-ASR

统一的语音转文本模型，可在单次前向传播中处理 **60 分钟长音频**。

- **长格式识别**：在 64K token 长度内单次处理 60 分钟连续音频。
- **结构化输出**：同时输出说话人（Who）、时间戳（When）和内容（What）。
- **多语言**：支持 50+ 语言。
- **自定义热词**：可注入领域专有名词、人名或术语，提高识别准确率。
- **推理方式**：支持 Transformers、vLLM，以及无需 GPU 的边缘 CPU 引擎 VibeVoice-ASR-BitNet。

### VibeVoice-TTS

长格式多说话人语音合成模型，适合对话式音频。

- **90 分钟生成**：单次生成长达 90 分钟的语音。
- **多说话人**：支持最多 4 位说话人自然轮替。
- **富有表现力**：能捕捉对话动态和情感细节。
- **多语言**：支持中文、英文等多种语言。

> TTS 训练代码已不在官方仓库，但模型权重仍可通过社区镜像获取。

### VibeVoice-Realtime

轻量级**实时流式 TTS**模型，面向低延迟场景。

- **参数量**：0.5B，便于部署。
- **低延迟**：首段可听语音约 300 毫秒。
- **流式输入**：可在 LLM 仍在生成文本时接收并实时合成。
- **长格式支持**：稳定生成约 10 分钟语音。

## 快速开始

克隆仓库并安装依赖：

```bash
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -r requirements.txt
```

使用 0.5B 模型进行实时 TTS 推理：

```bash
# 请参考仓库 docs/ 目录中的实时模型文档获取最新命令
python -m vibevoice.realtime inference \
  --model microsoft/VibeVoice-Realtime-0.5B \
  --text "你好，这是一个实时语音演示。"
```

对长音频文件进行 ASR 转写：

```bash
python -m vibevoice.asr transcribe \
  --model microsoft/VibeVoice-ASR \
  --audio long_meeting.wav
```

> 具体命令和 Notebook 示例请查看仓库 `docs/` 目录。

## 架构亮点

- **连续语音 tokenizer**：声学 tokenizer 和语义 tokenizer 以较低的 7.5 Hz 帧率运行，在保留音频保真度的同时提升长序列处理效率。
- **Next-token 扩散框架**：由大语言模型理解文本上下文和对话流程，扩散头负责生成高保真声学细节。
- **异构量化**：ASR BitNet 引擎将模型从 4.62 GB 压缩到 1.58 GB，在 3 线程以上 CPU 上 RTF < 1。

## 负责任使用

VibeVoice 面向研究与开发。高质量的合成语音可能被滥用于冒充或传播虚假信息。建议在使用 AI 生成语音时进行披露，并遵守所在地区的法律法规。

## 相关资源

- [GitHub 仓库](https://github.com/microsoft/VibeVoice)
- [项目主页](https://microsoft.github.io/VibeVoice/)
- [Hugging Face - VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)
- [Hugging Face - VibeVoice-Realtime-0.5B](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)

## 许可证

VibeVoice 由微软以 MIT License 开源发布。
