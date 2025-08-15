---
title: Create and use the agent
category: misc
source_lines: 81564-81631
line_count: 67
---

# Create and use the agent
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      Weaviate also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_weaviate_db.py
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.search import SearchType
    from agno.vectordb.weaviate import Distance, VectorIndex, Weaviate

    vector_db = Weaviate(
        collection="recipes_async",
        search_type=SearchType.hybrid,
        vector_index=VectorIndex.HNSW,
        distance=Distance.COSINE,
        local=True,  # Set to False if using Weaviate Cloud and True if using local instance
    )

    # Create knowledge base
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )

    agent = Agent(
        knowledge=knowledge_base,
        search_knowledge=True,
        show_tool_calls=True,
    )

    if __name__ == "__main__":
        # Comment out after first run
        asyncio.run(knowledge_base.aload(recreate=False))

        # Create and use the agent
        asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))
    ```

    <Tip className="mt-4">
      Weaviate's async capabilities leverage <code>WeaviateAsyncClient</code> to provide non-blocking vector operations. This is particularly valuable for applications requiring high concurrency and throughput.
    </Tip>
  </div>
</Card>

## Weaviate Params

<Snippet file="vectordb_weaviate_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/weaviate_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/async_weaviate_db.py)


