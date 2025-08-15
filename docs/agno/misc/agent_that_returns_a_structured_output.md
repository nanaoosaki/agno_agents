---
title: Agent that returns a structured output
category: misc
source_lines: 49526-49561
line_count: 35
---

# Agent that returns a structured output
structured_output_agent = Agent(
    model=xAI(id="grok-2-latest"),
    description="You write movie scripts.",
    response_model=MovieScript,
)

structured_output_agent.print_response("Llamas ruling the world")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export XAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno rich
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/structured_output.py
    ```
  </Step>
</Steps>


