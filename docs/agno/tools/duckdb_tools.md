---
title: DuckDB Tools
category: tools
source_lines: 26089-26141
line_count: 52
---

# DuckDB Tools
Source: https://docs.agno.com/examples/concepts/tools/database/duckdb



## Code

```python cookbook/tools/duckdb_tools.py
from agno.agent import Agent
from agno.tools.duckdb import DuckDbTools

agent = Agent(
    tools=[DuckDbTools()],
    show_tool_calls=True,
    instructions="Use this file for Movies data: https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)
agent.print_response(
    "What is the average rating of movies?", markdown=True, stream=False
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
    pip install -U duckdb openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/duckdb_tools.py
      ```

      ```bash Windows
      python cookbook/tools/duckdb_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


