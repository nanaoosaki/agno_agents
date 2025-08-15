---
title: Image Agent with Memory
category: knowledge
source_lines: 49267-49325
line_count: 58
---

# Image Agent with Memory
Source: https://docs.agno.com/examples/models/xai/image_agent_with_memory



## Code

```python cookbook/models/xai/image_agent_with_memory.py
from agno.agent import Agent
from agno.media import Image
from agno.models.xai import xAI
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-2-vision-latest"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    add_history_to_messages=True,
    num_history_responses=3,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
)

agent.print_response("Tell me where I can get more images?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export XAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai duckduckgo-search agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/image_agent_with_memory.py
    ```
  </Step>
</Steps>


