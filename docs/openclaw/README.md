# OpenClaw Introduction

## What is OpenClaw?

OpenClaw is an open-source self-hosted AI agent that runs locally and autonomously executes tasks. It can connect to multiple messaging platforms, control browsers, access systems, and has persistent memory. Developed by Peter Steinberger, it has gained over 180K GitHub stars, making it one of the fastest-growing open-source projects.

## Core Philosophy

### Truly Autonomous AI Assistant
Most AI can only chat with you, but OpenClaw can actually "get things done." You tell it a goal, and it will plan the steps, use tools, and execute tasks until the goal is achieved.

### Privacy First
All data runs on your own machine:
- No need to send sensitive information to third-party services
- Full control over your data and configuration
- Ideal for privacy-sensitive scenarios

### Persistent Memory
OpenClaw remembers your previous conversations:
- Knows your preferences and habits
- Can continue previous tasks
- Gets smarter the more you use it

## Core Features

### Multi-Platform Connectivity
Supports major messaging platforms:
- WhatsApp
- Telegram
- Slack
- Discord

### Browser Control
- Automatically browse websites
- Extract web information
- Fill forms and click buttons

### System Access
- Read and write local files
- Execute system commands
- Interact with local applications

### Tool Integration
- Search engines
- Data analysis
- Code execution

## Quick Start

### Installation

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pip install -r requirements.txt
```

### Configuration

1. Copy the configuration template:
```bash
cp config.example.yaml config.yaml
```

2. Edit the configuration file with your API keys and platform credentials

### Running

```bash
python main.py
```

## Best Practices

1. **Be Clear About Goals** - Tell OpenClaw what result you want, not how to do it
2. **Set Boundaries** - Define what resources it can access and what operations it can perform
3. **Check Regularly** - Review its execution logs to understand what it's doing
4. **Gradual Authorization** - Start with limited permissions, expand after confirming trust

## Related Resources

- [GitHub Repository](https://github.com/openclaw/openclaw)
- [Official Documentation](https://docs.openclaw.ai)
- [Community Discussions](https://github.com/openclaw/openclaw/discussions)

## License

OpenClaw is an open-source project. Please follow its open-source license when using it.