---
title: Success Criteria
category: misc
source_lines: 20929-20997
line_count: 68
---

# Success Criteria
Source: https://docs.agno.com/examples/concepts/others/success_criteria



This example shows how to set the success criteria of an agent.

## Code

```python cookbook/agent_concepts/other/success_criteria.py
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.thinking import ThinkingTools

puzzle_master = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[ThinkingTools(add_instructions=True)],
    instructions="You are a puzzle master for small logic puzzles.",
    show_tool_calls=False,
    markdown=False,
    stream_intermediate_steps=False,
    success_criteria="The puzzle has been solved correctly with all drinks uniquely assigned.",
)


prompt = """
Create a small logic puzzle:
Three friends—Alice, Bob, and Carol—each choose a different drink from tea, coffee, and milk.
Clues:
1. Alice does not drink tea.
2. The person who drinks coffee is not Carol.
Ask: Who drinks which beverage?
"""

puzzle_master.print_response(prompt, stream=True, show_reasoning=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-generativeai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/other/success_criteria.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/success_criteria.py
      ```
    </CodeGroup>
  </Step>
</Steps>


