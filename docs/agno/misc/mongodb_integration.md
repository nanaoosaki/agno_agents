---
title: MongoDB Integration
category: misc
source_lines: 32986-33040
line_count: 54
---

# MongoDB Integration
Source: https://docs.agno.com/examples/concepts/vectordb/mongodb



## Code

```python cookbook/agent_concepts/vector_dbs/mongodb.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.mongodb import MongoDb

mdb_connection_string = "mongodb://ai:ai@localhost:27017/ai?authSource=admin"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=MongoDb(
        collection_name="recipes",
        db_url=mdb_connection_string,
        wait_until_index_ready=60,
        wait_after_insert=300,
    ),
)
knowledge_base.load(recreate=True)

agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("How to make Thai curry?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U pymongo pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/mongodb.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/mongodb.py
      ```
    </CodeGroup>
  </Step>
</Steps>


