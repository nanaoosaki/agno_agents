---
title: knowledge_base.load(recreate=True)  # Comment out after first run
category: knowledge
source_lines: 80831-80892
line_count: 61
---

# knowledge_base.load(recreate=True)  # Comment out after first run

agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("How to make Thai curry?", markdown=True)
```

<Card title="Async Support ⚡">
  <div className="mt-2">
    <p>
      MongoDB also supports asynchronous operations, enabling concurrency and leading to better performance.
    </p>

    ```python async_mongodb.py
    import asyncio

    from agno.agent import Agent
    from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
    from agno.vectordb.mongodb import MongoDb

    # MongoDB Atlas connection string
    """
    Example connection strings:
    "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
    "mongodb://localhost:27017/agno?authSource=admin"
    """
    mdb_connection_string = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=MongoDb(
            collection_name="recipes",
            db_url=mdb_connection_string,
        ),
    )

    # Create and use the agent
    agent = Agent(knowledge=knowledge_base, show_tool_calls=True)

    if __name__ == "__main__":
        # Comment out after the first run
        asyncio.run(knowledge_base.aload(recreate=False))

        asyncio.run(agent.aprint_response("How to make Thai curry?", markdown=True))
    ```

    <Tip className="mt-4">
      Use <code>aload()</code> and <code>aprint\_response()</code> methods with <code>asyncio.run()</code> for non-blocking operations in high-throughput applications.
    </Tip>
  </div>
</Card>

## MongoDB Params

<Snippet file="vectordb_mongodb_params.mdx" />

## Developer Resources

* View [Cookbook (Sync)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/mongo_db/mongo_db.py)
* View [Cookbook (Async)](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/mongo_db/async_mongo_db.py)


