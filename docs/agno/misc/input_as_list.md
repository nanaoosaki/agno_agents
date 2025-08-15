---
title: Input as List
category: misc
source_lines: 20452-20510
line_count: 58
---

# Input as List
Source: https://docs.agno.com/examples/concepts/others/input_as_list



This example shows how to pass a list of messages as input to an agent.

## Code

```python cookbook/agent_concepts/other/input_as_list.py
from agno.agent import Agent

Agent().print_response(
    [
        {"type": "text", "text": "What's in this image?"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
        },
    ],
    stream=True,
    markdown=True,
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
      python cookbook/agent_concepts/other/input_as_list.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/input_as_list.py
      ```
    </CodeGroup>
  </Step>
</Steps>


