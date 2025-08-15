---
title: Define the custom async retriever
category: misc
source_lines: 61106-61168
line_count: 62
---

# Define the custom async retriever
async def retriever(
    query: str, agent: Optional[Agent] = None, num_documents: int = 5, **kwargs
) -> Optional[list[dict]]:
    """
    Custom async retriever function to search the vector database for relevant documents.
    """
    try:
        qdrant_client = AsyncQdrantClient(path="tmp/qdrant")
        query_embedding = embedder.get_embedding(query)
        results = await qdrant_client.query_points(
            collection_name="thai-recipes",
            query=query_embedding,
            limit=num_documents,
        )
        results_dict = results.model_dump()
        if "points" in results_dict:
            return results_dict["points"]
        else:
            return None
    except Exception as e:
        print(f"Error during vector database search: {str(e)}")
        return None

async def main():
    """Async main function to demonstrate agent usage."""
    agent = Agent(
        retriever=retriever,
        search_knowledge=True,
        instructions="Search the knowledge base for information",
        show_tool_calls=True,
    )

    # Load the knowledge base (uncomment for first run)
    await knowledge_base.aload(recreate=True)

    # Example query
    query = "List down the ingredients to make Massaman Gai"
    await agent.aprint_response(query, markdown=True)

if __name__ == "__main__":
    asyncio.run(main())
```

### Explanation

1. **Embedder and Vector Database Setup**: We start by defining an embedder and initializing a connection to a vector database. This setup is crucial for converting queries into embeddings and storing them in the database.

2. **Loading the Knowledge Base**: The knowledge base is loaded with PDF documents. This step involves converting the documents into embeddings and storing them in the vector database.

3. **Custom Retriever Function**: The `retriever` function is defined to handle the retrieval of documents. It takes a query, converts it into an embedding, and searches the vector database for relevant documents.

4. **Agent Initialization**: An agent is initialized with the custom retriever. The agent uses this retriever to search the knowledge base and retrieve information.

5. **Example Query**: The `main` function demonstrates how to use the agent to perform a query and retrieve information from the knowledge base.

## Developer Resources

* View [Sync Retriever](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/custom/retriever.py)
* View [Async Retriever](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/custom/async_retriever.py)


