---
title: Example: File operations
category: misc
source_lines: 28615-28664
line_count: 49
---

# Example: File operations
agent.print_response("Create a text file with the current date and time, then read it back")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Create an E2B account">
    Create an account at [E2B](https://e2b.dev/) and get your API key from the dashboard.
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install e2b_code_interpreter
    ```
  </Step>

  <Step title="Set your API Key">
    <CodeGroup>
      ```bash Mac/Linux
      export E2B_API_KEY=your_api_key_here
      ```

      ```bash Windows (Command Prompt)
      set E2B_API_KEY=your_api_key_here
      ```

      ```bash Windows (PowerShell)
      $env:E2B_API_KEY="your_api_key_here"
      ```
    </CodeGroup>
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac/Linux
      python cookbook/tools/e2b_tools.py
      ```

      ```bash Windows
      python cookbook\tools\e2b_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


