---
title: Image to Text Agent
category: misc
source_lines: 19222-19287
line_count: 65
---

# Image to Text Agent
Source: https://docs.agno.com/examples/concepts/multimodal/image-to-text



## Code

```python
from pathlib import Path

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    agent_id="image-to-text",
    name="Image to Text Agent",
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    instructions=[
        "You are an AI agent that can generate text descriptions based on an image.",
        "You have to return a text response describing the image.",
    ],
)
image_path = Path(__file__).parent.joinpath("sample.jpg")
agent.print_response(
    "Write a 3 sentence fiction story about the image",
    images=[Image(filepath=image_path)],
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/image_to_text_agent.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/image_to_text_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


