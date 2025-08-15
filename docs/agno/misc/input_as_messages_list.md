---
title: Input as Messages List
category: misc
source_lines: 20571-20634
line_count: 63
---

# Input as Messages List
Source: https://docs.agno.com/examples/concepts/others/input_as_messages_list



This example shows how to pass a list of messages as input to an agent.

## Code

```python cookbook/agent_concepts/other/input_as_messages_list.py
from agno.agent import Agent, Message

Agent().print_response(
    messages=[
        Message(
            role="user",
            content=[
                {"type": "text", "text": "Hi! My name is John."},
            ],
        ),
        Message(
            role="user",
            content=[
                {"type": "text", "text": "What are you capable of?"},
            ],
        ),
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
      python cookbook/agent_concepts/other/input_as_messages_list.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/input_as_messages_list.py
      ```
    </CodeGroup>
  </Step>
</Steps>


