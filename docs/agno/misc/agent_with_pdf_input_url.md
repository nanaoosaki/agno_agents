---
title: Agent with PDF Input (URL)
category: misc
source_lines: 47481-47539
line_count: 58
---

# Agent with PDF Input (URL)
Source: https://docs.agno.com/examples/models/openai/responses/pdf_input_url



## Code

```python cookbook/models/openai/responses/pdf_input_url.py
from agno.agent import Agent
from agno.media import File
from agno.models.openai.responses import OpenAIResponses

agent = Agent(
    model=OpenAIResponses(id="gpt-4o-mini"),
    tools=[{"type": "file_search"}, {"type": "web_search_preview"}],
    markdown=True,
)

agent.print_response(
    "Summarize the contents of the attached file and search the web for more information.",
    files=[File(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")],
)

print("Citations:")
print(agent.run_response.citations)
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
      python cookbook/models/openai/responses/pdf_input_url.py
      ```

      ```bash Windows
      python cookbook/models/openai/responses/pdf_input_url.py
      ```
    </CodeGroup>
  </Step>
</Steps>


