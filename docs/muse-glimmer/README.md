# Muse Glimmer Introduction

## What is Muse Glimmer?

Muse Glimmer is a 30-billion-parameter open-weight multimodal model released by Meta Superintelligence Labs on August 10, 2026. It is purpose-built for autonomous agentic tasks that run locally on consumer hardware, and is the first Meta model released under the permissive Apache 2.0 license since the company shifted to the proprietary Muse Spark family.

## Core Features

- **Local-first agent model**: Designed for always-on agents on a single 24–32 GB consumer GPU or Apple Silicon Mac.
- **Multimodal input**: Accepts interleaved text and images via a dedicated ~1.8B-parameter ViT-G/14 perception encoder.
- **Long context**: Supports 131,072+ tokens, enabling long-horizon agent sessions and large document analysis.
- **Tool use and reasoning**: Trained for planning, function calling, failure recovery, and multi-step task execution.
- **Quantized variants**: Full-precision BF16 weights plus two 4-bit quantized builds (K-Quant-17GB for 24 GB VRAM, K-Quant-Dynamic for 32 GB VRAM).
- **DFlash speculative decoding**: Ships with a lightweight drafter that accelerates generation by proposing 16-token blocks for verification.
- **Broad runtime support**: Day-zero integration with Ollama, LM Studio, Unsloth, llama.cpp, ExecuTorch, MLX, vLLM, and SGLang.

## Quick Start

Download the weights from Hugging Face and run them with your preferred local inference stack:

```bash
# Example with vLLM
vllm serve "meta-models/Muse-Glimmer-30B"

# Example with SGLang
python3 -m sglang.launch_server --model-path "meta-models/Muse-Glimmer-30B"
```

For quantized local inference, follow the GGUF or ExecuTorch PTE instructions on the Hugging Face model page.

## Model Card Highlights

| Attribute | Value |
| --- | --- |
| Total parameters | ~29.6B |
| Perception encoder | ~1.8B ViT-G/14 |
| Context length | 131,072+ |
| License | Apache 2.0 |
| Supported modalities | Text + image input, text output |
| Knowledge cutoff | January 4, 2026 |

## Related Resources

- [Hugging Face model card](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [Ars Technica launch coverage](https://arstechnica.com/ai/2026/08/with-new-open-models-meta-pitches-another-reboot-of-its-struggling-ai-strategy/)
- [Muse Glimmer on the Hugging Face blog](https://huggingface.co/blog)

## License

Muse Glimmer weights, quantizations, drafter, and perception encoder are released under the Apache 2.0 license.
