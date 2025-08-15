---
title: Weaviate Hybrid Search
category: misc
source_lines: 12836-12917
line_count: 81
---

# Weaviate Hybrid Search
Source: https://docs.agno.com/examples/concepts/hybrid-search/weaviate



## Code

```python cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/weaviate_db_hybrid_search.py
import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.search import SearchType
from agno.vectordb.weaviate import Distance, VectorIndex, Weaviate
from rich.prompt import Prompt

vector_db = Weaviate(
    collection="recipes",
    search_type=SearchType.hybrid,
    vector_index=VectorIndex.HNSW,
    distance=Distance.COSINE,
    local=False,  # Set to True if using Weaviate Cloud and False if using local instance
    hybrid_search_alpha=0.6, # Adjust alpha for hybrid search (0.0-1.0, default is 0.5), where 0 is pure keyword search, 1 is pure vector search
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

def weaviate_agent(user: str = "user"):
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

    typer.run(weaviate_agent)
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
    pip install -U weaviate-client tantivy pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/weaviate_db_hybrid_search.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/weaviate_db_hybrid_search.py
      ```
    </CodeGroup>
  </Step>
</Steps>


