---
title: - "What's the most upvoted story today?"
category: misc
source_lines: 34947-34970
line_count: 23
---

# - "What's the most upvoted story today?"
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install openai httpx agno
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python custom_tools.py
    ```
  </Step>
</Steps>


