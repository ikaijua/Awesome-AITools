# Cua Introduction

## What is Cua?

**Cua** (by [trycua](https://github.com/trycua/cua)) is an open-source infrastructure suite designed for **Computer-Use Agents**—AI models that can control a full desktop environment just like a human would. It provides the "body" (drivers and sandboxes) for an AI "brain" (like Claude or GPT-4) to see the screen, move the mouse, and type across macOS, Windows, Linux, and Android.

## Core Features

### 1. Cua Sandbox
A unified SDK (`pip install cua`) to manage ephemeral environments. It allows developers to spin up isolated virtual machines (VMs) or containers where agents can safely execute tasks without affecting the host machine.

### 2. Cua Driver
A background driver for macOS and Windows that allows agents to drive native apps without "stealing" the user's actual cursor or focus.

### 3. macOS Virtualization (Lume)
Includes **Lume**, a specialized tool for running macOS VMs on Apple Silicon with near-native performance, which is essential for testing Apple-specific workflows.

### 4. CuaBot
A "co-op" tool that lets agents like Claude Code or Cursor run inside a sandbox while projecting their windows onto your desktop via H.265 streaming.

### 5. Benchmark & Training
**Cua-Bench** provides a framework for running reinforcement learning (RL) environments and exporting "trajectories" (recordings of agent actions) for model training and evaluation.

## Who is it for?

- **AI Researchers:** Evaluating models on complex GUI-based tasks (OSWorld, Windows Arena).
- **Software Engineers:** Building "AI employees" that need to use legacy desktop software.
- **QA Automation Teams:** AI-driven cross-platform application testing.

## Quick Start

### Installation

```bash
pip install cua
```

### Basic Usage (Python)

```python
from cua import Cua

# Initialize a sandbox
with Cua().sandbox(os="macos") as sb:
    # Tell the agent to do something
    sb.display.screenshot().save("screen.png")
    sb.keyboard.type("Hello World")
    sb.mouse.click(x=100, y=200)
```

## Related Resources

- [GitHub Repository](https://github.com/trycua/cua)
- [Official Website](https://www.trycua.com/)
- [Documentation](https://docs.trycua.com/)

## License

Cua is an open-source project. Please refer to its repository for licensing details.
