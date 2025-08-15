---
title: Example usage with a complex reasoning problem
category: misc
source_lines: 23115-23157
line_count: 42
---

# Example usage with a complex reasoning problem
reasoning_agent.print_response(
    "Solve this logic puzzle: A man has to take a fox, a chicken, and a sack of grain across a river. "
    "The boat is only big enough for the man and one item. If left unattended together, the fox will "
    "eat the chicken, and the chicken will eat the grain. How can the man get everything across safely?",
    stream=True,
)


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
      python cookbook/reasoning/tools/reasoning_tools.py
      ```

      ```bash Windows
      python cookbook/reasoning/tools/reasoning_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


