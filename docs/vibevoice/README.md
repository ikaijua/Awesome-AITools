# VibeVoice Introduction

## What is VibeVoice?

VibeVoice is an open-source family of frontier voice AI models from Microsoft. It covers both speech recognition and speech synthesis, with a focus on long-form audio and real-time streaming.

> Note: The original VibeVoice-TTS training code was removed from the repository in September 2025 because of misuse inconsistent with its research purpose. The repository continues to host ASR and real-time TTS models, documentation, and inference examples.

## Model Family

### VibeVoice-ASR

A unified speech-to-text model that processes up to **60 minutes of audio in a single pass**.

- **Long-form recognition**: 60-minute single-pass processing within a 64K token context.
- **Rich structured output**: Produces transcriptions with speaker labels (Who), timestamps (When), and content (What).
- **Multilingual**: Supports 50+ languages.
- **Customized hotwords**: Users can supply domain-specific names or terms to improve accuracy.
- **Inference options**: Transformers, vLLM, and an edge CPU engine (VibeVoice-ASR-BitNet) that runs without a GPU.

### VibeVoice-TTS

A long-form, multi-speaker text-to-speech model for conversational audio.

- **90-minute generation**: Synthesizes long-form speech in a single pass.
- **Multi-speaker**: Supports up to 4 distinct speakers with natural turn-taking.
- **Expressive**: Captures conversational dynamics and emotional nuance.
- **Multilingual**: English, Chinese, and other languages.

> The TTS training code is no longer in the official repository, but model weights remain available through community mirrors.

### VibeVoice-Realtime

A lightweight **real-time streaming TTS** model designed for low-latency applications.

- **Parameter size**: 0.5B (deployment-friendly).
- **Low latency**: First audible speech in ~300 milliseconds.
- **Streaming input**: Accepts streaming text while an LLM is still generating.
- **Long-form capable**: Robust generation up to ~10 minutes.

## Quick Start

Clone the repository and install the dependencies:

```bash
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -r requirements.txt
```

For real-time TTS inference with the 0.5B model:

```bash
# Follow the streaming model docs for the exact command
python -m vibevoice.realtime inference \
  --model microsoft/VibeVoice-Realtime-0.5B \
  --text "Hello, this is a real-time voice demo."
```

For ASR on a long audio file:

```bash
python -m vibevoice.asr transcribe \
  --model microsoft/VibeVoice-ASR \
  --audio long_meeting.wav
```

> See the repository's `docs/` folder for the latest model-specific commands and notebooks.

## Architecture Highlights

- **Continuous speech tokenizers**: Acoustic and semantic tokenizers operate at a low 7.5 Hz frame rate, preserving audio fidelity while improving efficiency for long sequences.
- **Next-token diffusion framework**: An LLM handles textual context and dialogue flow, and a diffusion head generates high-fidelity acoustic details.
- **Heterogeneous quantization**: The ASR BitNet engine compresses the model from 4.62 GB to 1.58 GB while keeping real-time factor (RTF) below 1 on a 3+ thread CPU.

## Responsible Use

VibeVoice is intended for research and development. High-quality synthetic speech can be misused for impersonation or disinformation. Microsoft recommends disclosing AI-generated voice content and complying with applicable laws and regulations.

## Related Resources

- [GitHub Repository](https://github.com/microsoft/VibeVoice)
- [Project Page](https://microsoft.github.io/VibeVoice/)
- [VibeVoice-ASR on Hugging Face](https://huggingface.co/microsoft/VibeVoice-ASR)
- [VibeVoice-Realtime-0.5B on Hugging Face](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B)

## License

VibeVoice is released under the MIT License by Microsoft.
