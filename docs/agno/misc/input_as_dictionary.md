---
title: Input as Dictionary
category: misc
source_lines: 20391-20452
line_count: 61
---

# Input as Dictionary
Source: https://docs.agno.com/examples/concepts/others/input_as_dict



This example shows how to pass a dictionary of messages as input to an agent.

## Code

```python cookbook/agent_concepts/other/input_as_dict.py
from agno.agent import Agent

Agent().print_response(
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            },
        ],
    },
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
      python cookbook/agent_concepts/other/input_as_dict.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/input_as_dict.py
      ```
    </CodeGroup>
  </Step>
</Steps>


