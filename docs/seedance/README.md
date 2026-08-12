# Seedance Introduction

## What is Seedance?

Seedance is **ByteDance Seed**'s video generation model family, designed for high-fidelity text-to-video and image-to-video synthesis with multi-shot narrative continuity. It powers ByteDance's consumer-facing creative products such as [Dreamina](https://dreamina.capcut.com/) (CapCut / 即梦), [Doubao](https://www.doubao.com/), and [Xiaoyunqe](https://xyq.jianying.com/) (小云雀), and is also exposed to developers through [Volcengine](https://www.volcengine.com/).

Compared to general-purpose multimodal models, Seedance focuses specifically on the video generation domain, with emphasis on multi-shot consistency, motion realism, prompt adherence, and cinematic camera control.

## Core Model

### Seedance 2.5

Announced at the **Volcano Engine FORCE conference on 2026-06-23** and launched globally on **Dreamina on 2026-07-31**. Key upgrades over 2.0:

- **30-second single-pass generation** (with long-video extension mode up to ~3 minutes)
- **Native 4K output** (3840×2160) with 10-bit color depth
- **Up to 50 multimodal references** per request, including images, videos, audio, style references, 3D whitebox models, and greenscreen plates
- **Region-level editing** for localized modifications without regenerating the entire clip
- **Maya / Blender plugins** for production pipelines

### Seedance 2.0

Officially launched on **2026-02-12** ([announcement](https://seed.bytedance.com/en/blog)). Previously in production behind Dreamina with 2K output support.

## Access

| Surface | Audience | Link |
| --- | --- | --- |
| Dreamina (CapCut / 即梦) | End users / creators | https://dreamina.capcut.com/ |
| Doubao | End users (chat surface) | https://www.doubao.com/ |
| Xiaoyunqe (小云雀) | Creators (free Seedance 2.5 trial) | https://xyq.jianying.com/ |
| Volcengine Ark | Developers (API) | https://www.volcengine.com/ |

## Agent Skills

| Name | Description | Links | Fees |
| --- | --- | --- | --- |
| dexhunter/seedance2-skill | Skill to create better prompts for Seedance video generation. Covers Jimeng / Seedance input constraints, @ reference syntax, camera language, prompt structures, and templates for ads, dramas, MVs, and educational videos. Compatible with Claude Code, Cursor, Cline, and other agent tools. | [Github](https://github.com/dexhunter/seedance2-skill) ![GitHub Repo stars](https://img.shields.io/github/stars/dexhunter/seedance2-skill?style=social) | Free |

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
- Volcano Engine FORCE conference 2026 (Seedance 2.5 announcement, 2026-06-23): https://www.volcengine.com/
- Volcengine: https://www.volcengine.com/
- Dreamina: https://dreamina.capcut.com/
