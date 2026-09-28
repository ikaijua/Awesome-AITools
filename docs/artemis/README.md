# ARTEMIS

[ARTEMIS](https://github.com/google/artemis) is Google's open-source framework that turns natural-language instructions into reliable Android automation. It has 10.5k+ stars.

## What it does

- Executes cross-app tasks on Android from plain natural-language instructions.
- Achieves 99%+ completion on the AndroidWorld benchmark (20+ apps, 100+ multi-step tasks).
- Targets UI elements multimodally: element indexing + coordinates + vision, and supports Compose, Flutter, and Canvas-based custom UIs.

## Execution modes

- **Flash**: fast reactive loop (3–5 seconds per step), suited for deterministic tasks.
- **Pro**: multi-agent graph planning and verification (15–40 seconds per step), suited for long-horizon complex workflows.

## Tooling & integration

- Ships a Web UI console, MCP server, Python SDK, and CLI.
- Works on a real device or emulator; the first run installs an accessibility service on the device.
- Integrates with Antigravity, Codex, Claude Code, and other agents via MCP.

## Links

- [GitHub repository](https://github.com/google/artemis)
