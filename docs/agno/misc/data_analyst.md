---
title: Data Analyst
category: misc
source_lines: 11164-11227
line_count: 63
---

# Data Analyst
Source: https://docs.agno.com/examples/concepts/async/data_analyst



## Code

```python cookbook/agent_concepts/async/data_analyst.py
import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckdb import DuckDbTools

duckdb_tools = DuckDbTools(
    create_tables=False, export_tables=False, summarize_tables=False
)
duckdb_tools.create_table_from_path(
    path="https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
    table="movies",
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[duckdb_tools],
    markdown=True,
    show_tool_calls=True,
    additional_context=dedent("""\
    You have access to the following tables:
    - movies: contains information about movies from IMDB.
    """),
)
asyncio.run(
    agent.aprint_response("What is the average rating of movies?", stream=False)
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U openai agno duckdb
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/async/data_analyst.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/async/data_analyst.py
      ```
    </CodeGroup>
  </Step>
</Steps>


