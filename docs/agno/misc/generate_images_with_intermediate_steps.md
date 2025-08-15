---
title: Generate Images with Intermediate Steps
category: misc
source_lines: 18800-18869
line_count: 69
---

# Generate Images with Intermediate Steps
Source: https://docs.agno.com/examples/concepts/multimodal/generate-image



## Code

```python
from typing import Iterator

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools
from agno.utils.common import dataclass_to_dict
from rich.pretty import pprint

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DalleTools()],
    description="You are an AI agent that can create images using DALL-E.",
    instructions=[
        "When the user asks you to create an image, use the DALL-E tool to create an image.",
        "The DALL-E tool will return an image URL.",
        "Return the image URL in your response in the following format: `![image description](image URL)`",
    ],
    markdown=True,
)

run_stream: Iterator[RunResponse] = image_agent.run(
    "Create an image of a yellow siamese cat",
    stream=True,
    stream_intermediate_steps=True,
)
for chunk in run_stream:
    pprint(dataclass_to_dict(chunk, exclude={"messages"}))
    print("---" * 20)
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
    pip install -U openai rich agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/generate_image_with_intermediate_steps.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/generate_image_with_intermediate_steps.py
      ```
    </CodeGroup>
  </Step>
</Steps>


