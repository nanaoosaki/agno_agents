---
title: RAG Agent
category: misc
source_lines: 43102-43175
line_count: 73
---

# RAG Agent
Source: https://docs.agno.com/examples/models/ibm/knowledge



## Code

```python cookbook/models/ibm/watsonx/knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.ibm import WatsonX
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(
    model=WatsonX(id="ibm/granite-20b-code-instruct"),
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
    export IBM_WATSONX_API_KEY=xxx
    export IBM_WATSONX_PROJECT_ID=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U ibm-watsonx-ai sqlalchemy pgvector psycopg pypdf openai agno
    ```
  </Step>

  <Step title="Set up PostgreSQL with pgvector">
    You need a PostgreSQL database with the pgvector extension installed. Adjust the `db_url` in the code to match your database configuration.
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/ibm/watsonx/knowledge.py
      ```

      ```bash Windows
      python cookbook\models\ibm\watsonx\knowledge.py
      ```
    </CodeGroup>
  </Step>

  <Step title="For subsequent runs">
    After the first run, comment out the `knowledge_base.load(recreate=True)` line to avoid reloading the PDF.
  </Step>
</Steps>

This example shows how to integrate a knowledge base with IBM WatsonX. It loads a PDF from a URL, processes it into a vector database (PostgreSQL with pgvector in this case), and then creates an agent that can query this knowledge base.

Note: You need to install several packages (`pgvector`, `pypdf`, etc.) and have a PostgreSQL database with the pgvector extension available.


