---
title: Image Input High Fidelity
category: misc
source_lines: 20330-20391
line_count: 61
---

# Image Input High Fidelity
Source: https://docs.agno.com/examples/concepts/others/image_input_high_fidelity



This example shows how to use high fidelity images in an agent.

## Code

```python cookbook/agent_concepts/other/image_input_high_fidelity.py
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    markdown=True,
)

agent.print_response(
    "What's in these images",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            detail="high",
        )
    ],
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
      python cookbook/agent_concepts/other/image_input_high_fidelity.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/image_input_high_fidelity.py
      ```
    </CodeGroup>
  </Step>
</Steps>


