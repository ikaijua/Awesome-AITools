# Seedance 介绍

## Seedance 是什么？

Seedance 是 **字节跳动 Seed 团队**（ByteDance Seed）推出的视频生成模型系列，面向高保真度的文生视频与图生视频任务，主打多镜头叙事连续性。它驱动了字节旗下多个消费端产品：[即梦 / Dreamina](https://dreamina.capcut.com/)、[豆包](https://www.doubao.com/)、[小云雀](https://xyq.jianying.com/)，并通过[火山引擎](https://www.volcengine.com/)对开发者提供 API 能力。

相比通用多模态模型，Seedance 专注于视频生成领域，强调多镜头一致性、运动真实感、prompt 跟随能力以及镜头语言控制。

## 核心模型

### Seedance 2.5

于 **2026-06-23 火山引擎 FORCE 大会**首次发布，并于 **2026-07-31 在即梦平台全球上线**。相比 2.0 的主要升级：

- **30 秒单次生成**（长视频模式可扩展至约 3 分钟）
- **原生 4K 输出**（3840×2160），10-bit 色深
- **单次最多 50 个多模态参考输入**，支持图片、视频、音频、风格参考、3D 白盒与绿幕等
- **局部区域编辑**，可在不重新生成整条视频的情况下修改指定区域
- 提供 **Maya / Blender 插件**，便于生产流程接入

### Seedance 2.0

官方上线时间：**2026-02-12**（[发布公告](https://seed.bytedance.com/en/blog)）。曾在即梦 / Dreamina 中投入生产，支持 2K 输出。

## 入口

| 形态 | 受众 | 链接 |
| --- | --- | --- |
| 即梦 / Dreamina | 终端用户 / 创作者 | https://dreamina.capcut.com/ |
| 豆包 | 终端用户（对话界面） | https://www.doubao.com/ |
| 小云雀 | 创作者（可免费试用 Seedance 2.5） | https://xyq.jianying.com/ |
| 火山引擎方舟 | 开发者（API） | https://www.volcengine.com/ |

## Agent Skills

| 名称 | 描述 | 链接 | 费用 |
| --- | --- | --- | --- |
| dexhunter/seedance2-skill | 用于编写更好 Seedance 视频生成 prompt 的 Skill。覆盖即梦 / Seedance 输入约束、@ 引用语法、镜头语言、prompt 结构，以及广告、短剧、MV、教育视频等模板；兼容 Claude Code、Cursor、Cline 等 Agent 工具。 | [Github](https://github.com/dexhunter/seedance2-skill) ![GitHub Repo stars](https://img.shields.io/github/stars/dexhunter/seedance2-skill?style=social) | Free |

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
- **Dream Machine**（Luma）/ **Runway Gen 系列** / **Pika** —— 海外替代方案

Seedance 的核心差异化在于 **原生多镜头叙事生成** 以及与即梦 / 剪映剪辑工作流的深度整合。

## 参考链接

- ByteDance Seed 产品页：https://seed.bytedance.com/en/seedance
- 技术报告（Seedance 1.0）：https://arxiv.org/abs/2506.09113
- ByteDance Seed 博客（Seedance 2.0 发布，2026-02-12）：https://seed.bytedance.com/en/blog
- 火山引擎 FORCE 大会 2026（Seedance 2.5 发布，2026-06-23）：https://www.volcengine.com/
- 火山引擎：https://www.volcengine.com/
- 即梦：https://dreamina.capcut.com/
