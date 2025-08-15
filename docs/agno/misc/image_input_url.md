---
title: Image Input URL
category: misc
source_lines: 37028-37089
line_count: 61
---

# Image Input URL
Source: https://docs.agno.com/examples/models/anthropic/image_input_url



## Code

```python cookbook/models/anthropic/image_input_url.py
from agno.agent import Agent
from agno.media import Image
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and search the web for more information.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
        ),
    ],
    stream=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export ANTHROPIC_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U anthropic agno duckduckgo-search
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/anthropic/image_input_url.py
      ```

      ```bash Windows
      python cookbook/models/anthropic/image_input_url.py 
      ```
    </CodeGroup>
  </Step>
</Steps>


