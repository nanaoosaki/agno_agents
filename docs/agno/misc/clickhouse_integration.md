---
title: Clickhouse Integration
category: misc
source_lines: 32699-32775
line_count: 76
---

# Clickhouse Integration
Source: https://docs.agno.com/examples/concepts/vectordb/clickhouse



## Code

```python cookbook/agent_concepts/vector_dbs/clickhouse.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.clickhouse import Clickhouse

agent = Agent(
    storage=SqliteStorage(table_name="recipe_agent"),
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=Clickhouse(
            table_name="recipe_documents",
            host="localhost",
            port=8123,
            username="ai",
            password="ai",
        ),
    ),
    show_tool_calls=True,
    search_knowledge=True,
    read_chat_history=True,
)
agent.knowledge.load(recreate=False)  # type: ignore

agent.print_response("How do I make pad thai?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Start Clickhouse">
    ```bash
    docker run -d \
      -e CLICKHOUSE_DB=ai \
      -e CLICKHOUSE_USER=ai \
      -e CLICKHOUSE_PASSWORD=ai \
      -e CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT=1 \
      -v clickhouse_data:/var/lib/clickhouse/ \
      -v clickhouse_log:/var/log/clickhouse-server/ \
      -p 8123:8123 \
      -p 9000:9000 \
      --ulimit nofile=262144:262144 \
      --name clickhouse-server \
      clickhouse/clickhouse-server
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U clickhouse-connect pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/clickhouse.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/clickhouse.py
      ```
    </CodeGroup>
  </Step>
</Steps>


