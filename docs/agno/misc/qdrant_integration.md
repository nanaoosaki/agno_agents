---
title: Qdrant Integration
category: misc
source_lines: 33178-33238
line_count: 60
---

# Qdrant Integration
Source: https://docs.agno.com/examples/concepts/vectordb/qdrant



## Code

```python cookbook/agent_concepts/vector_dbs/qdrant_db.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "thai-recipes"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("List down the ingredients to make Massaman Gai", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Start Qdrant">
    ```bash
    docker run -p 6333:6333 -p 6334:6334 \
      -v $(pwd)/qdrant_storage:/qdrant/storage:z \
      qdrant/qdrant
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U qdrant-client pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/qdrant_db.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/qdrant_db.py
      ```
    </CodeGroup>
  </Step>
</Steps>


