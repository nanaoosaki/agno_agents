---
title: Agent with Knowledge Base
category: knowledge
source_lines: 39537-39606
line_count: 69
---

# Agent with Knowledge Base
Source: https://docs.agno.com/examples/models/cerebras/knowledge



## Code

```python cookbook/models/cerebras/basic_knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.cerebras import Cerebras
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    knowledge=knowledge_base,
)
agent.print_response("How to make Thai curry?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export CEREBRAS_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno cerebras-cloud-sdk
    ```
  </Step>

  <Step title="Start your Postgres server">
    Ensure your Postgres server is running and accessible at the connection string used in `db_url`.
  </Step>

  <Step title="Run Agent (first time)">
    The first run will load and index the PDF. This may take a while.

    <CodeGroup>
      ```bash Mac
      python cookbook/models/cerebras/basic_knowledge.py
      ```

      ```bash Windows
      python cookbook/models/cerebras/basic_knowledge.py
      ```
    </CodeGroup>
  </Step>

  <Step title="Subsequent Runs">
    After the first run, comment out or remove `knowledge_base.load(recreate=True)` to avoid reloading the PDF each time.
  </Step>
</Steps>


