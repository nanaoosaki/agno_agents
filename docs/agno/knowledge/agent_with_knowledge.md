---
title: Agent with Knowledge
category: knowledge
source_lines: 47340-47414
line_count: 74
---

# Agent with Knowledge
Source: https://docs.agno.com/examples/models/openai/responses/knowledge



## Code

```python cookbook/models/openai/responses/knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIResponses
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=OpenAIResponses(id="gpt-4o"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
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
    pip install -U openai sqlalchemy pgvector pypdf agno
    ```
  </Step>

  <Step title="Run PgVector">
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

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/openai/responses/knowledge.py
      ```

      ```bash Windows
      python cookbook/models/openai/responses/knowledge.py
      ```
    </CodeGroup>
  </Step>
</Steps>


