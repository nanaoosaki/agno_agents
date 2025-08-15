---
title: Gather Multiple Agents
category: misc
source_lines: 11227-11303
line_count: 76
---

# Gather Multiple Agents
Source: https://docs.agno.com/examples/concepts/async/gather_agents



## Code

```python cookbook/agent_concepts/async/gather_agents.py
import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.pretty import pprint

providers = ["openai", "anthropic", "ollama", "cohere", "google"]
instructions = [
    "Your task is to write a well researched report on AI providers.",
    "The report should be unbiased and factual.",
]


async def get_reports():
    tasks = []
    for provider in providers:
        agent = Agent(
            model=OpenAIChat(id="gpt-4"),
            instructions=instructions,
            tools=[DuckDuckGoTools()],
        )
        tasks.append(
            agent.arun(f"Write a report on the following AI provider: {provider}")
        )

    results = await asyncio.gather(*tasks)
    return results


async def main():
    results = await get_reports()
    for result in results:
        print("************")
        pprint(result.content)
        print("************")
        print("\n")


if __name__ == "__main__":
    asyncio.run(main())
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno rich duckduckgo-search
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/async/gather_agents.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/async/gather_agents.py
      ```
    </CodeGroup>
  </Step>
</Steps>


