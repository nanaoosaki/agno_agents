---
title: Clickhouse Agent Knowledge
category: knowledge
source_lines: 80207-80256
line_count: 49
---

# Clickhouse Agent Knowledge
Source: https://docs.agno.com/vectordb/clickhouse



## Setup

```shell
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

## Example

```python agent_with_knowledge.py
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
    # Show tool calls in the response
    show_tool_calls=True,
    # Enable the agent to search the knowledge base
    search_knowledge=True,
    # Enable the agent to read the chat history
    read_chat_history=True,
)
