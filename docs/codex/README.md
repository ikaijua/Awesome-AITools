# Codex Introduction

## What is Codex?

Codex is a lightweight coding agent from OpenAI that runs in your terminal. It's an AI-powered coding assistant that can understand and modify code directly from the command line. Unlike AI tools that require IDEs or browsers, Codex provides developers with a cleaner, workflow-integrated way to interact with code.

## Core Philosophy

### Terminal First
Codex is designed for the command line, perfect for developers who prefer working in terminals:
- Use AI assistance without leaving your terminal
- Seamlessly integrates with existing development workflows
- Lightweight and fast responding

### Understand and Modify
Not just generating code snippets, Codex can:
- Understand your project structure
- Directly modify code in files
- Execute multi-step programming tasks

### Simple and Efficient
- Minimal configuration, works out of the box
- Focused on core programming tasks
- Doesn't disrupt your workflow

## Core Features

### Code Understanding
- Analyze project structure and dependencies
- Understand function and class purposes
- Trace code call relationships

### Code Modification
- Automatically fix bugs
- Refactor code
- Add new features

### Command Line Integration
- Ask questions directly in terminal
- Support pipes and redirections
- Works with shell scripts

## Quick Start

### Installation

```bash
npm install -g @openai/codex
```

### Configuration

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

### Basic Usage

```bash
# Ask a question
codex "What does this function do?"

# Ask it to modify code
codex "Help me refactor this function to be more readable"

# Specify a file
codex "Fix the bug in src/utils.js"
```

## Common Commands

```bash
# Start interactive mode
codex

# Analyze current directory's code
codex "Analyze this project's structure"

# Generate tests
codex "Generate unit tests for src/api.js"
```

## Best Practices

1. **Provide Context** - Tell it what you're doing, and it will give better suggestions
2. **Iterate Gradually** - Start with the big picture, then dive into details
3. **Verify Results** - Always check and test AI-generated code yourself
4. **Use Interactively** - Ask follow-up questions and have it refine solutions

## Related Resources

- [GitHub Repository](https://github.com/openai/codex)
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Get API Key](https://platform.openai.com/api-keys)

## License

Codex is developed by OpenAI and requires an OpenAI API key to use. Please follow OpenAI's terms of service.