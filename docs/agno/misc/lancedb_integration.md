---
title: LanceDB Integration
category: misc
source_lines: 32881-32934
line_count: 53
---

# LanceDB Integration
Source: https://docs.agno.com/examples/concepts/vectordb/lancedb



## Code

```python cookbook/agent_concepts/vector_dbs/lance_db.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb

vector_db = LanceDb(
    table_name="recipes",
    uri="/tmp/lancedb",  # You can change this path to store data elsewhere
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("How to make Tom Kha Gai", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install -U lancedb pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/lance_db.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/lance_db.py
      ```
    </CodeGroup>
  </Step>
</Steps>


