---
title: Milvus Integration
category: misc
source_lines: 32934-32986
line_count: 52
---

# Milvus Integration
Source: https://docs.agno.com/examples/concepts/vectordb/milvus



## Code

```python cookbook/agent_concepts/vector_dbs/milvus.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.milvus import Milvus

COLLECTION_NAME = "thai-recipes"

vector_db = Milvus(collection=COLLECTION_NAME, url="http://localhost:6333")

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

  <Step title="Install libraries">
    ```bash
    pip install -U pymilvus pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/milvus.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/milvus.py
      ```
    </CodeGroup>
  </Step>
</Steps>


