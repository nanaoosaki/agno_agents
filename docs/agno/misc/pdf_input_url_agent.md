---
title: PDF Input URL Agent
category: misc
source_lines: 37310-37367
line_count: 57
---

# PDF Input URL Agent
Source: https://docs.agno.com/examples/models/anthropic/pdf_input_url



## Code

```python cookbook/models/anthropic/pdf_input_url.py
from agno.agent import Agent
from agno.media import File
from agno.models.anthropic import Claude

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file.",
    files=[
        File(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"),
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
    pip install -U anthropic agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/anthropic/pdf_input_url.py
      ```

      ```bash Windows
      python cookbook/models/anthropic/pdf_input_url.py 
      ```
    </CodeGroup>
  </Step>
</Steps>


