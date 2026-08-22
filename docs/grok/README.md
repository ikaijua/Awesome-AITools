# Grok Introduction

## What is Grok?

Grok is xAI's AI assistant. It is available as a web app at [grok.com](https://grok.com/), natively inside the X (formerly Twitter) platform, and through mobile apps. The current flagship model is **Grok 4.6**, with a 500K-token context window and a knowledge cutoff of February 1, 2026.

Grok is designed around two ideas: **real-time access to public information on X**, and **multimodal generation** (text, image, video, and voice) under one account.

## Core Philosophy

### Real-time by default
Grok's most distinctive feature is its live access to X posts and public web data. Where most assistants are limited to their training cutoff, Grok can surface and reason about events as they happen, with X-post citations inline. This makes it the default choice for breaking-news follow-up, social-trend tracking, and "what is X saying about Y right now" questions.

### All modalities, one subscription
A single Grok account exposes:
- **Text** via Grok 4.6 (chat, reasoning, agentic tool calling)
- **Image generation** through the **Imagine** API (Aurora model)
- **Video generation** through the Imagine API (480p / 720p / 1080p)
- **Voice** via the **Voice API** — real-time speech-to-speech, plus batch STT and TTS

### Agentic and code-capable
Grok 4.6 is also positioned as a coding model with agentic tool calling, minimal hallucinations, and configurable reasoning effort. The same model powers the `grok` CLI ([Grok Build](docs/grok-build/README.md)) for terminal-based coding workflows, and is exposed through the Responses API for embedding into other tools.

## Core Features

### Text and reasoning
- Grok 4.6: 500K-token context, configurable reasoning effort
- Web Search and X Search tools for live data
- Vision input — analyze images inline in chat
- File upload and analysis

### Image and video (Imagine)
- Image generation tuned for photorealism and meme-style visuals
- Video generation at 480p / 720p / 1080p
- Editing and regeneration on existing images
- Available inside Grok chat and via the API

### Voice
- Real-time speech-to-speech conversations
- Batch speech-to-text
- Text-to-speech synthesis

### API
- OpenAI-compatible endpoint at `https://api.x.ai/v1`
- Native Responses API for agentic coding
- Official SDKs for Python (`xai_sdk`), TypeScript (`@ai-sdk/xai`), and OpenAI-compatible clients

## Quick Start

### Web and apps
- **Web**: [grok.com](https://grok.com/)
- **X integration**: built into [x.com](https://x.com/) (Grok in the sidebar)
- **Mobile**: iOS and Android apps under the Grok brand

### API access

1. Create an API key in the [xAI Console](https://console.x.ai/).
2. Set the `XAI_API_KEY` environment variable.
3. Call the OpenAI-compatible endpoint:

```sh
curl https://api.x.ai/v1/responses \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-4.6",
    "input": "Summarize the top X posts about the latest SpaceX launch."
  }'
```

Or with the official Python SDK:

```python
import os
from xai_sdk import Client
from xai_sdk.chat import user

client = Client(api_key=os.getenv("XAI_API_KEY"))
chat = client.chat.create(model="grok-4.6")
chat.append(user("Summarize the top X posts about the latest SpaceX launch."))
print(chat.sample().content)
```

## Pricing Snapshot

| Item | Price |
| --- | --- |
| Grok 4.6 input | $2.00 / 1M tokens |
| Grok 4.6 output | $6.00 / 1M tokens |
| Voice Agent (real-time) | from $0.05 / min |
| TTS | $15.00 / 1M chars |
| STT (Batch) | $0.10 / hour |
| STT (Streaming) | $0.20 / hour |
| Imagine (image) | per-image, see console |
| Imagine (video) | from $0.05 / second |

Free and paid tiers for the consumer Grok app are listed on [grok.com](https://grok.com/). API pricing is per the [xAI pricing page](https://docs.x.ai/docs/pricing).

## Notes

- **Knowledge cutoff**: Grok 4.6's training data extends to February 1, 2026. For events after that date, use the Web Search or X Search tools.
- **Real-time dependency**: Grok's headline differentiation depends on continued X platform access. Behavior in regions where X is restricted may differ.
- **Coding use cases**: For terminal-based coding workflows, see [Grok Build](docs/grok-build/README.md), the open-source `grok` CLI/TUI built on Grok 4.6.

## Related Resources

- [Grok homepage](https://grok.com/)
- [xAI Documentation](https://docs.x.ai/docs/overview)
- [xAI Models](https://docs.x.ai/docs/models)
- [xAI Pricing](https://docs.x.ai/docs/pricing)
- [API Reference](https://docs.x.ai/docs/api-reference)
- [Grok Build (CLI/TUI)](docs/grok-build/README.md)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Grok (the consumer product) and the xAI API are proprietary services from xAI. The [Grok-1](https://github.com/xai-org/grok-1) base model weights are released under the Apache 2.0 License; the consumer Grok service is not open source.
