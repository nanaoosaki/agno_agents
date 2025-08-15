---
title: PgVector Integration
category: misc
source_lines: 33040-33105
line_count: 65
---

# PgVector Integration
Source: https://docs.agno.com/examples/concepts/vectordb/pgvector



## Code

```python cookbook/agent_concepts/vector_dbs/pg_vector.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

vector_db = PgVector(table_name="recipes", db_url=db_url)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("How to make Thai curry?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Start PgVector">
    ```bash
    docker run -d \
      -e POSTGRES_DB=ai \
      -e POSTGRES_USER=ai \
      -e POSTGRES_PASSWORD=ai \
      -e PGDATA=/var/lib/postgresql/data/pgdata \
      -v pgvolume:/var/lib/postgresql/data \
      -p 5532:5432 \
      --name pgvector \
      agnohq/pgvector:16
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U sqlalchemy pgvector psycopg pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/pg_vector.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/pg_vector.py
      ```
    </CodeGroup>
  </Step>
</Steps>


