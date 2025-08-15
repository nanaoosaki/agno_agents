---
title: - "Get the top 5 stories (you can try accepting and declining the confirmation)"
category: misc
source_lines: 35084-35109
line_count: 25
---

# - "Get the top 5 stories (you can try accepting and declining the confirmation)"
agent.print_response(
    "What are the top 2 hackernews stories?", stream=True, console=console
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install openai agno
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python human_in_the_loop.py
    ```
  </Step>
</Steps>


