# Qoder Introduction

## What is Qoder?

Qoder is an AI intelligent programming assistant and agent product family from Alibaba Cloud, built around the idea of an "autonomous programming paradigm." It connects deeply with codebases and toolchains through multi-agent collaboration, long-term delegation, memory, and knowledge engines, continuously understanding, planning, executing, verifying, and iterating on real software development tasks until delivery.

## Core Philosophy

### From Code Completion to Autonomous Delivery

Traditional coding assistants mainly provide line- or function-level completions. Qoder aims to let AI drive tasks end-to-end:

- Understand codebase structure and business goals
- Autonomously plan implementation steps
- Invoke tools, edit files, and run commands
- Verify results and keep iterating

### Multi-Agent Collaboration

Qoder breaks complex engineering tasks into multiple collaborating agents responsible for planning, coding, testing, reviewing, and more, achieving goals that go far beyond a single chat turn.

### Deep Context and Memory

Through deep codebase analysis and adaptive memory, Qoder retains project context across long and even multi-session conversations, reducing repeated explanations and growing with the project.

### Goal-Oriented Closed Loop

Clear goals and deliverables drive the agent through a "plan → execute → verify → iterate" loop until the task is finished.

## Product Family

| Product | Positioning | Best For |
| --- | --- | --- |
| **Qoder Desktop** | Native desktop IDE and autonomous dev workbench | Daily software development, editing, debugging |
| **Qoder CLI** | Terminal-native AI coding partner / integrable agent engine | Command-line development, CI/CD, automation scripts |
| **QoderWork** | Local, autonomous, secure AI work companion | Local file processing, data analysis, content creation |
| **QoderWake** | Always-online digital employee | Scheduled tasks, continuous monitoring, autonomous execution |
| **Cloud Agents** | Enterprise-grade fully managed cloud AI Agent platform | Enterprise integrations and team collaboration |

Qoder also provides JetBrains and VS Code plugins for use inside existing IDEs.

## Core Capabilities

### Agent Autonomy

- Understand intent, break down tasks, invoke tools
- Drive execution independently in complex workflows
- Decide autonomously or ask for confirmation when needed

### Context Engineering

- Deep codebase analysis
- Adaptive memory and knowledge base
- Long-context retention

### Toolchain Integration

- Built-in programming tools
- MCP (Model Context Protocol) tool support
- Terminal commands and IDE capabilities

### Multi-Model Support

- Supports Alibaba Cloud Bailian and other model services
- Configurable domain-specific models (e.g., coding models)
- Balances performance and cost for different tasks

## Quick Start

### Download the Desktop App

Visit the [Qoder download center](https://qoder.com.cn/download) and choose the installer for your system:

- macOS 12+
- Windows 10+
- Linux (.deb / .rpm)

After installation, log in with your Alibaba Cloud account to start using it.

### Install Qoder CLI

**macOS / Linux**

```bash
curl -fsSL https://qoder.com.cn/install | bash
```

**Windows PowerShell**

```powershell
irm https://qoder.com.cn/install.ps1 | iex
```

**Windows CMD**

```cmd
curl -fsSL https://qoder.com.cn/install.cmd -o install.cmd && install.cmd
```

Once installed, launch the CLI with `qodercli`.

> For more detailed CLI instructions, see the [Qoder official docs](https://docs.qoder.com/zh/cli/installation).

### Install IDE Plugins

- **VS Code**: Search for "Qoder CN" in the Extensions marketplace and install the official Alibaba Cloud plugin.
- **JetBrains**: Download the plugin package from the official site and install it via `File → Settings → Plugins → Install Plugin from Disk`.

## Common Use Cases

1. **From requirement to code** - Describe a feature and let Qoder implement, test, and verify it.
2. **Bug fixing** - Provide the symptom and let Qoder locate and fix the issue.
3. **Code refactoring** - Restructure code at scale while preserving behavior.
4. **Automation scripts** - Use Qoder CLI to add AI capabilities to CI/CD or local scripts.
5. **Local office automation** - Use QoderWork to process files, generate reports, and analyze data.

## Best Practices

1. **State the goal before the details** - Help the agent understand what you want, not just isolated local hints.
2. **Start with a trusted repository** - Experiment with high-autonomy modes on familiar, backed-up projects.
3. **Review intermediate outputs** - Treat Qoder's changes like a colleague's PR.
4. **Use Plan mode for complex tasks** - Let the agent present a plan before executing.
5. **Leverage project memory** - Use memory and knowledge features to avoid repeating project context.

## Related Resources

- [Official Website](https://qoder.com.cn/)
- [Download Center](https://qoder.com.cn/download)
- [Official Documentation](https://docs.qoder.com/zh/cli/installation)
- [Alibaba Cloud Developer Community](https://developer.aliyun.com/)

## License

Qoder is provided by Alibaba Cloud. Please follow the relevant Alibaba Cloud service terms and license agreements when using it.
