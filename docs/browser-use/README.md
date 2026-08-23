# browser-use

[browser-use](https://github.com/browser-use/browser-use) is an open-source Python library that enables AI agents to control web browsers through natural language.

## What it does

- Converts high-level natural-language instructions into browser actions (click, type, scroll, navigate).
- Extracts structured DOM content for agent reasoning.
- Supports multi-step workflows such as form filling, search, checkout, and data collection.
- Works with any LLM provider via a simple API.

## Quick start

```bash
pip install browser-use
```

```python
from browser_use import Agent
import asyncio

async def main():
    agent = Agent(
        task="Find the cheapest flight from San Francisco to Tokyo next week",
        llm="openai/gpt-4o",
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

## Common use cases

- Building web agents that perform tasks on public websites.
- Automated end-to-end testing with LLM-driven instructions.
- Structured data extraction and monitoring.

## Links

- [GitHub repository](https://github.com/browser-use/browser-use)
- [Official documentation](https://docs.browser-use.com/)
