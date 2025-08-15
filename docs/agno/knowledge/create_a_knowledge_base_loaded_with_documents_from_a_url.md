---
title: Create a knowledge base, loaded with documents from a URL
category: knowledge
source_lines: 62452-62493
line_count: 41
---

# Create a knowledge base, loaded with documents from a URL
knowledge_base = UrlKnowledge(
    urls=["https://docs.agno.com/introduction/agents.md"],
    # Use LanceDB as the vector database, store embeddings in the `agno_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=CohereEmbedder(id="embed-v4.0"),
        reranker=CohereReranker(model="rerank-v3.5"),
    ),
)

agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    # Agentic RAG is enabled by default when `knowledge` is provided to the Agent.
    knowledge=knowledge_base,
    # search_knowledge=True gives the Agent the ability to search on demand
    # search_knowledge is True by default
    search_knowledge=True,
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Include sources in your response.",
        "Always search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    # knowledge_base.load(recreate=True)
    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )
```


