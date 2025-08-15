---
title: We will search DDG but limit the site to Politifact
category: misc
source_lines: 29972-30012
line_count: 40
---

# We will search DDG but limit the site to Politifact
agent = Agent(
    tools=[DuckDuckGoTools(modifier="site:politifact.com")], show_tool_calls=True
)
agent.print_response(
    "Is Taylor Swift promoting energy-saving devices with Elon Musk?", markdown=False
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
    pip install -U duckduckgo-search openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/duckduckgo_tools.py
      ```

      ```bash Windows
      python cookbook/tools/duckduckgo_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


