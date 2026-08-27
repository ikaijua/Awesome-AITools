# Hugging Face Introduction

## What is Hugging Face?

[Hugging Face](https://huggingface.co/) is the leading open AI platform and community. It started as a chatbot company but evolved into the central hub for open-source machine learning, hosting models, datasets, demo Spaces, and a rich ecosystem of libraries that power model discovery, training, fine-tuning, and deployment.

## Core Positioning

### The Model Hub
The [Hugging Face Hub](https://huggingface.co/models) hosts over one million public models covering LLMs, vision, audio, multimodal, and domain-specific tasks. It is the default distribution channel for open-weight models from Meta, Google, Alibaba, DeepSeek, Moonshot, Mistral, and many others.

### Datasets and Evaluation
The [Datasets Hub](https://huggingface.co/datasets) provides hundreds of thousands of ready-to-use datasets, while [Evaluate](https://huggingface.co/docs/evaluate/index) and [Leaderboards](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) help benchmark models on public tasks.

### Spaces and Demos
[Spaces](https://huggingface.co/spaces) let anyone host interactive ML demos, often built with Gradio or Streamlit, directly from a Git repository. It is one of the fastest ways to share and try new models in the browser.

### Libraries and Tools
- **Transformers** — the de facto library for working with transformer models.
- **Diffusers** — tools for diffusion models and generative AI.
- **Datasets** — efficient data loading and processing.
- **Accelerate** — simple multi-GPU and distributed training.
- **TRL / PEFT** — fine-tuning and parameter-efficient adaptation.
- **Text Generation Inference (TGI)** and **Inference API / Endpoints** — production serving.

## Quick Start

### Install the core libraries

```bash
pip install transformers datasets accelerate
```

### Download and run a model

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("Hugging Face makes open AI easy to use."))
```

### Host a demo on Spaces

Create a new Space at [huggingface.co/new-space](https://huggingface.co/new-space), push a Gradio or Streamlit app, and share the URL.

## Related Resources

- [Hugging Face Website](https://huggingface.co/)
- [GitHub Organization](https://github.com/huggingface)
- [Documentation](https://huggingface.co/docs)
- [Models](https://huggingface.co/models)
- [Datasets](https://huggingface.co/datasets)
- [Spaces](https://huggingface.co/spaces)

## License

Hugging Face platform services and libraries are provided under various open-source licenses; individual models and datasets carry their own licenses.
