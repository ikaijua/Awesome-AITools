# browser-use

[browser-use](https://github.com/browser-use/browser-use) 是一个开源 Python 库，能够让 AI 智能体通过自然语言控制网页浏览器。

## 主要功能

- 将自然语言指令转换为浏览器操作（点击、输入、滚动、跳转）。
- 提取结构化 DOM 内容供智能体推理。
- 支持多步工作流，如表单填写、搜索、下单和数据采集。
- 通过简单 API 与任意大模型提供商集成。

## 快速开始

```bash
pip install browser-use
```

```python
from browser_use import Agent
import asyncio

async def main():
    agent = Agent(
        task="查找下周从旧金山到东京的最便宜航班",
        llm="openai/gpt-4o",
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

## 常见使用场景

- 构建能够在公共网站上执行任务的网页智能体。
- 使用大模型驱动的指令进行端到端自动化测试。
- 结构化数据提取与监控。

## 链接

- [GitHub 仓库](https://github.com/browser-use/browser-use)
- [官方文档](https://docs.browser-use.com/)
