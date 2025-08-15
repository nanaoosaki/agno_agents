---
title: SQL Tools
category: tools
source_lines: 26333-26383
line_count: 50
---

# SQL Tools
Source: https://docs.agno.com/examples/concepts/tools/database/sql



## Code

```python cookbook/tools/sql_tools.py
from agno.agent import Agent
from agno.tools.sql import SQLTools

agent = Agent(
    tools=[SQLTools(db_url="sqlite:///database.db")],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Show me all tables in the database and their schemas")
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
    pip install -U sqlalchemy openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/sql_tools.py
      ```

      ```bash Windows
      python cookbook/tools/sql_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


