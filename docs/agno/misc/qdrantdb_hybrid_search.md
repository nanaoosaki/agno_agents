---
title: QdrantDB Hybrid Search
category: misc
source_lines: 12757-12836
line_count: 79
---

# QdrantDB Hybrid Search
Source: https://docs.agno.com/examples/concepts/hybrid-search/qdrantdb



## Code

```python cookbook/agent_concepts/knowledge/vector_dbs/qdrant_db/qdrant_db_hybrid_search.py
from typing import Optional

import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.search import SearchType
from agno.vectordb.qdrant import Qdrant
from rich.prompt import Prompt

COLLECTION_NAME = "thai-recipes"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333", search_type=SearchType.hybrid)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)


def qdrantdb_agent(user: str = "user"):
    agent = Agent(
        user_id=user,
        knowledge=knowledge_base,
        search_knowledge=True,
    )

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)


if __name__ == "__main__":
    # Comment out after first run
    knowledge_base.load(recreate=True)

    typer.run(qdrantdb_agent)
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
    pip install -U qdrant-client fastembed tantivy pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/knowledge/vector_dbs/qdrant_db/qdrant_db_hybrid_search.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/knowledge/vector_dbs/qdrant_db/qdrant_db_hybrid_search.py
      ```
    </CodeGroup>
  </Step>
</Steps>


