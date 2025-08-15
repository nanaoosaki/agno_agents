---
title: Zep Async Memory Tools
category: knowledge
source_lines: 26454-26536
line_count: 82
---

# Zep Async Memory Tools
Source: https://docs.agno.com/examples/concepts/tools/database/zep_async



## Code

```python cookbook/tools/zep_async_tools.py
import asyncio
import time
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.zep import ZepAsyncTools


async def main():
    # Initialize the ZepAsyncTools
    zep_tools = ZepAsyncTools(
        user_id="agno", session_id="agno-async-session", add_instructions=True
    )

    # Initialize the Agent
    agent = Agent(
        model=OpenAIChat(),
        tools=[zep_tools],
        context={
            "memory": lambda: zep_tools.get_zep_memory(memory_type="context"),
        },
        add_context=True,
    )

    # Interact with the Agent
    await agent.aprint_response("My name is John Billings")
    await agent.aprint_response("I live in NYC")
    await agent.aprint_response("I'm going to a concert tomorrow")

    # Allow the memories to sync with Zep database
    time.sleep(10)

    # Refresh the context
    agent.context["memory"] = await zep_tools.get_zep_memory(memory_type="context")

    # Ask the Agent about the user
    await agent.aprint_response("What do you know about me?")


if __name__ == "__main__":
    asyncio.run(main())
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OPENAI_API_KEY=xxx
    export ZEP_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U zep-cloud openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/zep_async_tools.py
      ```

      ```bash Windows
      python cookbook/tools/zep_async_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


