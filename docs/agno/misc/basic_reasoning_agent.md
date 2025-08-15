---
title: Basic Reasoning Agent
category: misc
source_lines: 21592-21651
line_count: 59
---

# Basic Reasoning Agent
Source: https://docs.agno.com/examples/concepts/reasoning/agents/basic-cot



This is a basic reasoning agent with chain of thought reasoning.

## Code

```python cookbook/reasoning/agents/analyse_treaty_of_versailles.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

task = (
    "Analyze the key factors that led to the signing of the Treaty of Versailles in 1919. "
    "Discuss the political, economic, and social impacts of the treaty on Germany and how it "
    "contributed to the onset of World War II. Provide a nuanced assessment that includes "
    "multiple historical perspectives."
)

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning=True,
    markdown=True,
)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
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

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/agents/analyse_treaty_of_versailles.py
      ```

      ```bash Windows
      python cookbook/reasoning/agents/analyse_treaty_of_versailles.py
      ```
    </CodeGroup>
  </Step>
</Steps>


