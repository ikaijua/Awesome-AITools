# ml-intern Introduction

## What is ml-intern?

`ml-intern` is an open-source, autonomous AI agent developed by Hugging Face, designed to function as a specialized **Machine Learning Engineer**. It is built to handle the end-to-end lifecycle of ML tasks, from initial research to model deployment.

## Core Philosophy

### Specialized ML Engineering
Unlike general-purpose coding assistants, `ml-intern` is specifically optimized for the machine learning workflow. It understands the nuances of data processing, model training, and evaluation.

### Deep Ecosystem Integration
`ml-intern` has native tools to interact with the Hugging Face Hub (datasets, models, spaces), documentation, and compute jobs, making it a powerful companion for researchers and developers in the HF ecosystem.

### Autonomous Research
It can browse the web, search GitHub, and read academic papers (PDFs) to inform its coding decisions and stay up-to-date with the latest research.

## Core Features

### Autonomous Task Execution
- Formulate hypotheses based on research papers.
- Write high-quality ML code (training scripts, evaluation loops).
- Run experiments and track results.
- Deploy models and datasets directly to Hugging Face.

### Advanced Agent Logic
- **Doom Loop Detector**: Detects when the agent is stuck in repetitive loops and injects corrective prompts.
- **Auto-Compaction**: Automatically manages long-running session contexts to keep the most relevant info in the LLM window.
- **Traceability**: Sessions are auto-uploaded to a private HF dataset for debugging and auditing via the HF Agent Trace Viewer.

### Multi-Model Support
- Supports Claude (Anthropic), GPT (OpenAI), and local models (via Ollama, vLLM, or LM Studio).

## Quick Start

### Installation

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

```bash
# Clone the repository
git clone https://github.com/huggingface/ml-intern.git
cd ml-intern

# Sync dependencies
uv sync

# Install the CLI tool
uv tool install -e .
```

### Configuration

Set up your environment variables (in `.env` or your shell):

```bash
export ANTHROPIC_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
export HF_TOKEN="your-huggingface-token"
export GITHUB_TOKEN="your-github-token"
```

### Basic Usage

```bash
# Start interactive mode
ml-intern

# Run a single task headlessly
ml-intern "fine-tune a ResNet model on the CIFAR-10 dataset"

# Specify a specific model
ml-intern --model anthropic/claude-3-5-sonnet-latest "your prompt"
```

## Related Resources

- [GitHub Repository](https://github.com/huggingface/ml-intern)
- [Hugging Face Hub](https://huggingface.co/)
- [HF Agent Trace Viewer](https://huggingface.co/spaces/huggingface/agent-trace-viewer)

## License

`ml-intern` is an open-source project by Hugging Face. Please follow their licensing terms and the terms of service of the LLM providers you use.
