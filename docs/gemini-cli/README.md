# Gemini CLI Introduction

## What is Gemini CLI?

Gemini CLI is an open-source command-line AI agent that brings the power of Google Gemini directly into your terminal. It allows you to interact with Gemini AI in a command-line environment for various programming and information processing tasks.

## Core Philosophy

### Command Line Native Experience
Gemini CLI is designed for terminal users:
- No need to switch to browsers or other applications
- Maintains your terminal workflow
- Suitable for server environments and headless operations

### Google AI Capabilities
Direct access to Google's latest Gemini models:
- Powerful code understanding and generation (Gemini 3.1 Pro)
- Multimodal support (text, images, design assets)
- Ultra-long context processing (1M+ tokens)
- Real-time web grounding via Google Search integration

### Open Source and Controllable
- Fully open source with transparent code
- Customizable and extensible
- Community-driven improvements

## Core Features

### Intelligent Q&A
- Ask questions directly in terminal
- Get code suggestions and explanations
- Document queries and summaries

### Code Assistance
- Code completion and generation
- Bug analysis and fix suggestions
- Code review and optimization

### File Operations
- Read and analyze file contents
- Generate and modify code files
- Batch text processing

### Integration Capabilities
- Works with shell scripts
- Pipe operation support
- Output formatting

## Quick Start

### Installation

```bash
# Install via npm
npm install -g @google/gemini-cli

# Or install from source
git clone https://github.com/google-gemini/gemini-cli.git
cd gemini-cli
npm install
npm link
```

### Configuration

Set your Google AI API key:

```bash
export GOOGLE_AI_API_KEY="your-api-key"
```

### Basic Usage

```bash
# Start interactive mode
gemini

# Ask a direct question
gemini "Explain what this regex means"

# Analyze a file
gemini "Analyze the code structure of main.py" < main.py

# Use with pipes
cat error.log | gemini "Help me analyze this error"
```

## Common Use Cases

### Code Debugging
```bash
gemini "What's wrong with this code?" < broken_code.py
```

### Learning New Topics
```bash
gemini "Explain how Docker works"
```

### Documentation Generation
```bash
gemini "Generate documentation comments for this function" < my_function.js
```

## Best Practices

1. **Be Specific** - More specific questions yield more useful answers
2. **Provide Context** - Pipe in relevant file content
3. **Verify Output** - Always test AI-generated code
4. **Use Interactively** - Multiple rounds of dialogue to refine solutions

## Related Resources

- [GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Comparison with Other Tools](../COMPARISON.md)

## License

Gemini CLI is an open-source project. Usage requires a Google AI API key. Please follow Google's terms of service and the open-source license.