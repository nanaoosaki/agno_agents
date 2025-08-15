---
title: Qdrant Agent Knowledge
category: knowledge
source_lines: 81131-81252
line_count: 121
---

# Qdrant Agent Knowledge
Source: https://docs.agno.com/vectordb/qdrant



## Setup

Follow the instructions in the [Qdrant Setup Guide](https://qdrant.tech/documentation/guides/installation/) to install Qdrant locally. Here is a guide to get API keys: [Qdrant API Keys](https://qdrant.tech/documentation/cloud/authentication/).

## Example

```python agent_with_knowledge.py
import os
import typer
from typing import Optional
from rich.prompt import Prompt

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant

api_key = os.getenv("QDRANT_API_KEY")
qdrant_url = os.getenv("QDRANT_URL")
collection_name = "thai-recipe-index"

vector_db = Qdrant(
    collection=collection_name,
    url=qdrant_url,
    api_key=api_key,
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

def qdrant_agent(user: str = "user"):
    run_id: Optional[str] = None

    agent = Agent(
        run_id=run_id,
        user_id=user,
        knowledge=knowledge_base,
        tool_calls=True,
        use_tools=True,
        show_tool_calls=True,
        debug_mode=True,
    )

    if run_id is None:
        run_id = agent.run_id
        print(f"Started Run: {run_id}\n")
    else:
        print(f"Continuing Run: {run_id}\n")

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)

if __name__ == "__main__":
    # Comment out after first run
    knowledge_base.load(recreate=True, upsert=True)

    typer.run(qdrant_agent)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      Qdrant also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_qdrant_db.py
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.qdrant import Qdrant

    COLLECTION_NAME = "thai-recipes"

    # Initialize Qdrant with local instance
    vector_db = Qdrant(
        collection=COLLECTION_NAME, 
        url="http://localhost:6333"
    )

    # Create knowledge base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )

    agent = Agent(knowledge=knowledge_base, show_tool_calls=True)

    if __name__ == "__main__":
        # Load knowledge base asynchronously
        asyncio.run(knowledge_base.aload(recreate=False))  # Comment out after first run

        # Create and use the agent asynchronously
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Using <code>aload()</code> and <code>aprint\_response()</code> with asyncio provides non-blocking operations, making your application more responsive under load.
    </Tip>
  </div>
</Card>

## Qdrant Params

<Snippet file="vectordb_qdrant_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/qdrant_db/qdrant_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/qdrant_db/async_qdrant_db.py)


