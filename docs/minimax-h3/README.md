# MiniMax H3 Introduction

## What is MiniMax H3?

MiniMax H3 is an **open-source, general-purpose omni-modal generative system** from [MiniMax](https://www.minimax.io/). Unlike MiniMax's consumer-facing video platform [Hailuo AI](https://hailuoai.com/video), H3 is released as a model with inference code, weights, and reference pipelines that developers can run locally or integrate into their own products.

It unifies understanding and generation across text, image, video, and audio in a single model architecture, making it suitable for cross-modal content creation workflows.

## Core Capabilities

H3 is released as task-specific checkpoints. The base model supports:

- **Text-to-Video (T2V)** — generate video from text prompts
- **Image-to-Video (I2V)** — animate a still image
- **First/Last-Frame-to-Video (FL2VA)** — generate video conditioned on start and/or end frames
- **Text-to-Audio-Video (T2VA)** — generate synchronized audio and video from text

The project provides reference pipelines for each task, along with the required processor, tokenizer, text encoder, Visual VAE, and standalone Audio VAE components.

## Deployment Options

The official repository recommends the following inference frameworks:

| Framework | Use Case | Link |
| --- | --- | --- |
| SGLang | High-performance serving | [cookbook](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/sglang) |
| vLLM | Scalable inference | [recipes](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/vllm) |
| diffusers | Easy Python pipeline loading | [docs](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/diffusers) |
| ComfyUI | Visual node-based workflow | [tutorial](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/cookbooks/comfyui) |

## Access

| Resource | Link |
| --- | --- |
| Official repository (code + docs) | https://github.com/MiniMax-AI/MiniMax-H3 |
| Model weights (HuggingFace) | https://huggingface.co/MiniMaxAI/MiniMax-H3 |
| Model weights (ModelScope) | https://modelscope.cn/models/MiniMax/MiniMax-H3 |
| Consumer product | https://hailuoai.com/video |
