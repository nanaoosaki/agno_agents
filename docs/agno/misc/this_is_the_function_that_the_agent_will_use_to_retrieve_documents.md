---
title: This is the function that the agent will use to retrieve documents
category: misc
source_lines: 61032-61096
line_count: 64
---

# This is the function that the agent will use to retrieve documents
def retriever(
    query: str, agent: Optional[Agent] = None, num_documents: int = 5, **kwargs
) -> Optional[list[dict]]:
    """
    Custom retriever function to search the vector database for relevant documents.

    Args:
        query (str): The search query string
        agent (Agent): The agent instance making the query
        num_documents (int): Number of documents to retrieve (default: 5)
        **kwargs: Additional keyword arguments

    Returns:
        Optional[list[dict]]: List of retrieved documents or None if search fails
    """
    try:
        qdrant_client = QdrantClient(url="http://localhost:6333")
        query_embedding = embedder.get_embedding(query)
        results = qdrant_client.query_points(
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

def main():
    """Main function to demonstrate agent usage."""
    # Initialize agent with custom retriever
    # Remember to set search_knowledge=True to use agentic_rag or add_reference=True for traditional RAG
    # search_knowledge=True is default when you add a knowledge base but is needed here
    agent = Agent(
        retriever=retriever,
        search_knowledge=True,
        instructions="Search the knowledge base for information",
        show_tool_calls=True,
    )

    # Example query
    query = "List down the ingredients to make Massaman Gai"
    agent.print_response(query, markdown=True)

if __name__ == "__main__":
    main()
```

#### Asynchronous Implementation

```python
import asyncio
from typing import Optional
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant
from qdrant_client import AsyncQdrantClient

