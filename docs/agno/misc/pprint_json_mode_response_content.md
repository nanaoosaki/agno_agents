---
title: pprint(json_mode_response.content)
category: misc
source_lines: 48012-48048
line_count: 36
---

# pprint(json_mode_response.content)

json_mode_agent.print_response("New York")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export TOGETHER_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U together openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/together/structured_output.py
      ```

      ```bash Windows
      python cookbook/models/together/structured_output.py
      ```
    </CodeGroup>
  </Step>
</Steps>


