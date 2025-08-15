---
title: Ask a question that would likely trigger tool use
category: misc
source_lines: 43886-43921
line_count: 35
---

# Ask a question that would likely trigger tool use
openai_agent.print_response("How is TSLA stock doing right now?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export LITELLM_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U litellm openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/litellm/tool_use.py
      ```

      ```bash Windows
      python cookbook/models/litellm/tool_use.py
      ```
    </CodeGroup>
  </Step>
</Steps>


