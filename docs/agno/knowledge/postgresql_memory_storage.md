---
title: PostgreSQL Memory Storage
category: knowledge
source_lines: 18002-18079
line_count: 77
---

# PostgreSQL Memory Storage
Source: https://docs.agno.com/examples/concepts/memory/db/mem-postgres-memory



## Code

```python cookbook/agent_concepts/memory/postgres_memory.py
"""
This example shows how to use the Memory class with PostgreSQL storage.
"""

from agno.agent.agent import Agent
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai.chat import OpenAIChat
from agno.storage.postgres import PostgresStorage

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

memory = Memory(db=PostgresMemoryDb(table_name="agent_memories", db_url=db_url))

session_id = "postgres_memories"
user_id = "postgres_user"

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    enable_user_memories=True,
    enable_session_summaries=True,
)

agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    stream=True,
    user_id=user_id,
    session_id=session_id,
)

agent.print_response(
    "What are my hobbies?", stream=True, user_id=user_id, session_id=session_id
)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set environment variables">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno openai sqlalchemy 'psycopg[binary]'
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac/Linux
      python cookbook/agent_concepts/memory/postgres_memory.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/memory/postgres_memory.py
      ```
    </CodeGroup>
  </Step>
</Steps>


