---
title: Create a client
category: misc
source_lines: 81395-81511
line_count: 116
---

# Create a client
client = Surreal(url=SURREALDB_URL)
client.signin({"username": SURREALDB_USER, "password": SURREALDB_PASSWORD})
client.use(namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE)

surrealdb = SurrealDb(
    client=client,
    collection="recipes",  # Collection name for storing documents
    efc=150,  # HNSW construction time/accuracy trade-off
    m=12,  # HNSW max number of connections per element
    search_ef=40,  # HNSW search time/accuracy trade-off
)


def sync_demo():
    """Demonstrate synchronous usage of SurrealDb"""
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=surrealdb,
        embedder=OpenAIEmbedder(),
    )

    # Load data synchronously
    knowledge_base.load(recreate=True)

    # Create agent and query synchronously
    agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
    agent.print_response(
        "What are the 3 categories of Thai SELECT is given to restaurants overseas?",
        markdown=True,
    )


if __name__ == "__main__":
    # Run synchronous demo
    print("Running synchronous demo...")
    sync_demo()
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      SurrealDB also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_surrealdb_db.py
    import asyncio

    from agno.agent import Agent
    from agno.embedder.openai import OpenAIEmbedder
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.surrealdb import SurrealDb
    from surrealdb import AsyncSurreal

    # SurrealDB connection parameters
    SURREALDB_URL = "ws://localhost:8000"
    SURREALDB_USER = "root"
    SURREALDB_PASSWORD = "root"
    SURREALDB_NAMESPACE = "test"
    SURREALDB_DATABASE = "test"

    # Create a client
    client = AsyncSurreal(url=SURREALDB_URL)

    surrealdb = SurrealDb(
    async_client=client,
    collection="recipes",  # Collection name for storing documents
    efc=150,  # HNSW construction time/accuracy trade-off
    m=12,  # HNSW max number of connections per element
    search_ef=40,  # HNSW search time/accuracy trade-off
    )


    async def async_demo():
    """Demonstrate asynchronous usage of SurrealDb"""

    await client.signin({"username": SURREALDB_USER, "password": SURREALDB_PASSWORD})
    await client.use(namespace=SURREALDB_NAMESPACE, database=SURREALDB_DATABASE)

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=surrealdb,
        embedder=OpenAIEmbedder(),
    )

    await knowledge_base.aload(recreate=True)

    agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
    await agent.aprint_response(
        "What are the 3 categories of Thai SELECT is given to restaurants overseas?",
        markdown=True,
    )


    if __name__ == "__main__":
    # Run asynchronous demo
    print("\nRunning asynchronous demo...")
    asyncio.run(async_demo())
    ```

    <Tip className="mt-4">
      Using <code>aload()</code> and <code>aprint\_response()</code> with asyncio provides non-blocking operations, making your application more responsive under load.
    </Tip>
  </div>
</Card>

## SurrealDB Params

<Snippet file="vector_db_surrealdb_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/surrealdb/surreal_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/surrealdb/async_surreal_db.py)


