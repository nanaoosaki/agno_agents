---
title: Postgres Tools
category: tools
source_lines: 26277-26333
line_count: 56
---

# Postgres Tools
Source: https://docs.agno.com/examples/concepts/tools/database/postgres



## Code

```python cookbook/tools/postgres_tools.py
from agno.agent import Agent
from agno.tools.postgres import PostgresTools

agent = Agent(
    tools=[PostgresTools(db_url="postgresql://user:pass@localhost:5432/db")],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Show me all tables in the database")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your database URL">
    ```bash
    export DATABASE_URL=postgresql://user:pass@localhost:5432/db
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U psycopg2-binary sqlalchemy openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/postgres_tools.py
      ```

      ```bash Windows
      python cookbook/tools/postgres_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


