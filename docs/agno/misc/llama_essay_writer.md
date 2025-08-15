---
title: Llama Essay Writer
category: misc
source_lines: 42686-42741
line_count: 55
---

# Llama Essay Writer
Source: https://docs.agno.com/examples/models/huggingface/llama_essay_writer



## Code

```python cookbook/models/huggingface/llama_essay_writer.py
import os
from getpass import getpass

from agno.agent import Agent
from agno.models.huggingface import HuggingFace

agent = Agent(
    model=HuggingFace(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=4096,
    ),
    description="You are an essay writer. Write a 300 words essay on topic that will be provided by user",
)
agent.print_response("topic: AI")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export HF_TOKEN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U huggingface_hub agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/huggingface/llama_essay_writer.py
      ```

      ```bash Windows
      python cookbook/models/huggingface/llama_essay_writer.py
      ```
    </CodeGroup>
  </Step>
</Steps>


