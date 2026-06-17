# Seedance 介绍

## Seedance 是什么？

Seedance 是 **字节跳动 Seed 团队**（ByteDance Seed）推出的视频生成模型系列，面向高保真度的文生视频与图生视频任务，主打多镜头叙事连续性。它驱动了字节旗下多个消费端产品：[即梦 / Dreamina](https://dreamina.capcut.com/)、[豆包](https://www.doubao.com/)、[小云雀](https://xyq.jianying.com/)，并通过[火山引擎](https://www.volcengine.com/)对开发者提供 API 能力。

相比通用多模态模型，Seedance 专注于视频生成领域，强调多镜头一致性、运动真实感、prompt 跟随能力以及镜头语言控制。

## 核心模型

### Seedance 1.0

随技术报告 [*Seedance 1.0: Exploring the Boundaries of Video Generation Models*](https://arxiv.org/abs/2506.09113)（arXiv:2506.09113）一同发布。

- **任务**：文生视频（T2V）、图生视频（I2V），原生支持多镜头生成
- **多镜头**：生成包含多个连续镜头的叙事视频，主体、风格、氛围在镜头切换间保持一致
- **分辨率**：1080p 输出，运动流畅，具备电影感
- **参考性能**：在 NVIDIA-L20 上生成 5 秒 1080p 视频约需 41.4 秒（通过多阶段蒸馏与系统优化达成 ~10× 推理加速）
- **风格覆盖**：写实、赛博朋克、插画、毛毡质感等多种视觉风格
- **训练方法**：多源视频数据清洗 + 精细视频字幕；监督微调（SFT）+ 视频专用 RLHF，配合多维度奖励
- **运动与镜头控制**：从自然语言 prompt 解析多主体交互、复杂动作和镜头运动
- **产品 SKU**：火山引擎上提供 **Seedance 1.0 Pro** 与 **Seedance 1.0 Lite** 两档（Pro 主打高保真，Lite 主打快/低成本推理） <!-- TODO: 通过火山引擎官方文档核对两档的具体差异 -->

### Seedance 2.0

官方上线时间：**2026-02-12**（[发布公告](https://seed.bytedance.com/en/blog)）。当前在 Dreamina 中投入生产，支持 2K 输出。

<!-- TODO: 待 ByteDance Seed 发布 2.0 正式技术报告后补充：
     - 最大分辨率 / 最大时长
     - 是否支持音频生成
     - 多镜头 / 镜头控制相对 1.0 的提升
     - 架构变化
-->

## 入口

| 形态 | 受众 | 链接 |
| --- | --- | --- |
| 即梦 / Dreamina | 终端用户 / 创作者 | https://dreamina.capcut.com/ |
| 豆包 | 终端用户（对话界面） | https://www.doubao.com/ |
| 小云雀 | 创作者（可免费试用 Seedance 2.0） | https://xyq.jianying.com/ |
| 火山引擎方舟 | 开发者（API） | https://www.volcengine.com/ |

## 评测基准

Seedance 1.0 公开过以下评测：

- **SeedVideoBench-1.0** —— ByteDance Seed 自建的视频评测基准
- **[Artificial Analysis Video Arena](https://artificialanalysis.ai/text-to-video/arena)** —— 第三方盲评竞技场

具体分数请参考技术报告与上述竞技场的实时榜单，本文不复述。

## 典型场景

- **短视频创作**：为抖音 / TikTok / Reels 直接生成素材
- **图生视频**：让静态插画、商品图、角色立绘动起来
- **多镜头叙事**：生成跨镜头主体一致的叙事片段——Seedance 相对单镜头同类的核心差异点
- **分镜与预演**：在进入传统制作流程前快速试错场景构思
- **营销与电商**：批量生成商品展示视频

## 与其他视频模型的对比

Seedance 同期对位的有：

- **KLING AI**（快手可灵）—— 长序列连贯性与运动控制突出
- **Wan2.6**（阿里通义万相）—— 阿里的视频生成方案
- **hailuoai**（海螺/MiniMax）—— 电影感输出见长
- **Dream Machine**（Luma）/ **Runway Gen 系列** / **Pika** —— 海外主流方案

Seedance 的差异化点在于：**原生多镜头叙事生成**，以及与即梦 / 剪映剪辑链路的紧密整合。

## 参考链接

- ByteDance Seed —— Seedance 产品页：https://seed.bytedance.com/en/seedance
- 技术报告（Seedance 1.0）：https://arxiv.org/abs/2506.09113
- ByteDance Seed 博客（Seedance 2.0 发布公告，2026-02-12）：https://seed.bytedance.com/en/blog
- 火山引擎：https://www.volcengine.com/
- 即梦 / Dreamina：https://dreamina.capcut.com/
