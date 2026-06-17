# Seedance Introduction

## What is Seedance?

Seedance is **ByteDance Seed**'s video generation model family, designed for high-fidelity text-to-video and image-to-video synthesis with multi-shot narrative continuity. It powers ByteDance's consumer-facing creative products such as [Dreamina](https://dreamina.capcut.com/) (CapCut / 即梦), [Doubao](https://www.doubao.com/), and [Xiaoyunqe](https://xyq.jianying.com/) (小云雀), and is also exposed to developers through [Volcengine](https://www.volcengine.com/).

Compared to general-purpose multimodal models, Seedance focuses specifically on the video generation domain, with emphasis on multi-shot consistency, motion realism, prompt adherence, and cinematic camera control.

## Core Models

### Seedance 1.0

Released alongside the technical report [*Seedance 1.0: Exploring the Boundaries of Video Generation Models*](https://arxiv.org/abs/2506.09113) (arXiv:2506.09113).

- **Tasks**: Text-to-video (T2V) and image-to-video (I2V), with native multi-shot generation
- **Multi-shot**: Generates narrative videos with multiple cohesive shots while keeping subject, style, and atmosphere consistent across transitions
- **Resolution**: 1080p output with smooth motion and cinematic aesthetics
- **Reference performance**: ~41.4 seconds to generate a 5-second 1080p video on NVIDIA-L20 hardware (≈10× speedup over baseline via multi-stage distillation and system optimization)
- **Style range**: Photorealistic, cyberpunk, illustration, felt-texture, and other visual styles
- **Training**: Multi-source video data curation + detailed video captioning; supervised fine-tuning + video-specific RLHF with multi-dimensional rewards
- **Camera & motion control**: Parses natural-language prompts for multi-agent interactions, complex actions, and camera movement
- **Variants**: Volcengine exposes **Seedance 1.0 Pro** and **Seedance 1.0 Lite** SKUs (Pro for higher fidelity, Lite for faster / cheaper inference) <!-- TODO: confirm exact spec differences from Volcengine docs -->

### Seedance 2.0

Officially launched on **2026-02-12** ([announcement](https://seed.bytedance.com/en/blog)). Currently in production behind Dreamina with 2K output support.

<!-- TODO: Fill in once ByteDance Seed publishes the 2.0 technical report:
     - Max resolution / max duration
     - Audio generation support (if any)
     - Multi-shot / camera control improvements over 1.0
     - Architecture changes
-->

## Access

| Surface | Audience | Link |
| --- | --- | --- |
| Dreamina (CapCut / 即梦) | End users / creators | https://dreamina.capcut.com/ |
| Doubao | End users (chat surface) | https://www.doubao.com/ |
| Xiaoyunqe (小云雀) | Creators (free Seedance 2.0 trial) | https://xyq.jianying.com/ |
| Volcengine Ark | Developers (API) | https://www.volcengine.com/ |

## Benchmarks

Seedance 1.0 reports results on:

- **SeedVideoBench-1.0** — ByteDance Seed's internal video benchmark
- **[Artificial Analysis Video Arena](https://artificialanalysis.ai/text-to-video/arena)** — third-party blind evaluation arena

Numeric scores are not reproduced here; check the technical report and the arena leaderboard for current standings.

## Typical Use Cases

- **Short-form video creation**: Generate clips for Douyin / TikTok / Reels directly from prompts or storyboards
- **Image-to-video animation**: Bring static illustrations, product shots, or character art into motion
- **Multi-shot storytelling**: Generate narrative sequences with consistent characters across shots — Seedance's headline capability vs. single-shot competitors
- **Pre-visualization & storyboarding**: Quickly draft scene ideas before committing to traditional production
- **Marketing & e-commerce**: Generate product showcase videos at scale

## Comparison with Other Video Models

Seedance sits alongside:

- **KLING AI** (Kuaishou) — strong on long-form coherence and motion control
- **Wan2.6** (Alibaba) — Alibaba's competing video stack
- **hailuoai** (MiniMax) — known for cinematic output
- **Dream Machine** (Luma) / **Runway Gen series** / **Pika** — Western alternatives

Seedance's competitive positioning centers on **native multi-shot narrative generation** and tight integration with the Dreamina / CapCut editing workflow.

## References

- ByteDance Seed — Seedance product page: https://seed.bytedance.com/en/seedance
- Technical report (Seedance 1.0): https://arxiv.org/abs/2506.09113
- ByteDance Seed blog (Seedance 2.0 launch announcement, 2026-02-12): https://seed.bytedance.com/en/blog
- Volcengine: https://www.volcengine.com/
- Dreamina: https://dreamina.capcut.com/
