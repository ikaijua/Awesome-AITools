# Dexter Introduction

## What is Dexter?

**Dexter** is an autonomous financial research agent designed to perform deep analysis by thinking, planning, and learning through iteration. It functions similarly to "Claude Code" but is specialized for the financial domain. It takes complex financial queries, decomposes them into structured research plans, and executes them using real-time market data.

## Core Philosophy

### Specialized for Finance
Unlike general-purpose agents, Dexter is specifically engineered for financial analysis, understanding market concepts, financial statements, and quantitative data.

### Autonomous Research
Dexter doesn't just answer questions; it conducts research. It plans multiple steps, fetches data, validates its findings, and iterates until it reaches a high-confidence conclusion.

### Transparent Reasoning
With its "scratchpad" logging system and built-in reflection, Dexter provides clear visibility into how it reached its conclusions, making it suitable for data-heavy research that requires high precision.

## Core Features

### Intelligent Task Planning
Automatically breaks down complex financial questions into actionable, step-by-step research tasks.

### Autonomous Execution
Independently selects and utilizes tools to fetch financial data (e.g., income statements, balance sheets, cash flow).

### Self-Validation & Reflection
Critically evaluates its own findings and iterates until it reaches a data-backed conclusion.

### Real-Time Data Integration
Connects to institutional-grade financial datasets and web search tools (Exa/Tavily).

### Multi-Channel Access
Supports interaction via a CLI and a WhatsApp gateway.

### Evaluation Suite
Features a built-in testing framework using LangSmith to score the agent's accuracy against financial datasets.

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/virattt/dexter.git
cd dexter

# Install dependencies using Bun
bun install
```

### Configuration

You will need API keys for the LLM providers and data sources (e.g., OpenAI, Financial Datasets API). Configure them in a `.env` file as specified in the repository's documentation.

### Basic Usage

```bash
# Run the CLI
bun run start
```

## Common Use Cases

### Financial Statement Analysis
"Analyze the cash flow trends of Apple Inc. over the last 3 years and identify potential risks."

### Market Comparison
"Compare the profitability ratios of Tesla vs BYD for the fiscal year 2024."

### Investment Hypothesis Testing
"Research the impact of rising interest rates on the regional banking sector's net interest margin."

## Related Resources

- [GitHub Repository](https://github.com/virattt/dexter)
- [LangSmith Evaluation](https://docs.smith.langchain.com/)
- [Financial Datasets API](https://financialdatasets.ai/)

## License

Dexter is licensed under the MIT License.
