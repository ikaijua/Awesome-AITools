# Lightpanda Browser Introduction

## What is Lightpanda?

Lightpanda is the first open-source headless browser designed specifically for the LLM era. Unlike traditional headless browsers (like Headless Chrome or Playwright), which are often heavyweight and resource-intensive, Lightpanda is built from scratch in **Zig** to be extremely lightweight, fast, and AI-native.

## Key Features

### 🚀 Extreme Performance
- **~9x Faster:** Significantly faster execution than Headless Chrome.
- **~16x Less Memory:** Extremely low footprint, allowing more instances to run on the same hardware.
- **Built in Zig:** Leverages the performance and safety features of the Zig programming language.

### 🤖 AI-Native
- **MCP Support:** Native support for the **Model Context Protocol (MCP)**, allowing AI agents (like Claude Code, Gemini CLI, etc.) to use it as a tool out-of-the-box.
- **Markdown Output:** Can directly convert web pages into clean Markdown, providing high-quality, noise-free context for LLMs.

### 🛠️ Developer Friendly
- **CDP Compatible:** Supports the Chrome DevTools Protocol, making it compatible with many existing automation tools.
- **JavaScript Support:** Powered by the V8 engine, it handles modern SPAs and complex JavaScript-heavy websites.
- **Zero-Config Tooling:** Easy to integrate into existing agentic workflows.

## Why use Lightpanda?

For developers building AI agents that need to browse the web, Lightpanda solves several common pain points:
1. **Infrastructure Costs:** Run many more agents on the same server due to low memory usage.
2. **Latency:** Faster page loads and JS execution mean faster agent responses.
3. **Data Quality:** Clean Markdown output prevents the "LLM hallucinations" often caused by noisy HTML context.

## Quick Start

Lightpanda can be run via Docker or as a standalone binary.

### Running with Docker

```bash
docker run -p 9222:9222 lightpanda/browser
```

### Using as an MCP Tool

Add Lightpanda to your agent's configuration (e.g., in Claude Code or Gemini CLI) as an MCP server to enable autonomous browsing capabilities.

## Related Resources

- [GitHub Repository](https://github.com/lightpanda-io/browser)
- [Official Website](https://lightpanda.io)
- [Documentation](https://docs.lightpanda.io)

## License

Lightpanda is open-source. Please refer to its repository for licensing details.
