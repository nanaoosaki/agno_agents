---
title: Print the response on the terminal
category: misc
source_lines: 42213-42248
line_count: 35
---

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story", stream=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GROQ_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U groq agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/groq/basic_stream.py
      ```

      ```bash Windows
      python cookbook/models/groq/basic_stream.py
      ```
    </CodeGroup>
  </Step>
</Steps>


