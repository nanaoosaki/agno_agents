---
title: -*- Print a response to the cli
category: misc
source_lines: 11135-11164
line_count: 29
---

# -*- Print a response to the cli
asyncio.run(agent.aprint_response("Share a breakfast recipe.", stream=True))
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/async/basic.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/async/basic.py
      ```
    </CodeGroup>
  </Step>
</Steps>


