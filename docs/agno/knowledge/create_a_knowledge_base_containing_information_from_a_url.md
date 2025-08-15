---
title: Create a knowledge base containing information from a URL
category: knowledge
source_lines: 72559-72609
line_count: 50
---

# Create a knowledge base containing information from a URL
agno_docs = UrlKnowledge(
    urls=["https://docs.agno.com/llms-full.txt"],
    # Use LanceDB as the vector database and store embeddings in the `agno_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

knowledge_tools = KnowledgeTools(
    knowledge=agno_docs,
    think=True,
    search=True,
    analyze=True,
    add_few_shot=True,
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[knowledge_tools],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment after first run
    agno_docs.load(recreate=True)
    agent.print_response("How do I build multi-agent teams with Agno?", stream=True)
```

The toolkit comes with default instructions and few-shot examples to help the Agent use the tools effectively. Here is how you can configure them:

```python
from agno.tools.knowledge import KnowledgeTools

knowledge_tools = KnowledgeTools(
    knowledge=my_knowledge_base,
    think=True,                # Enable the think tool
    search=True,               # Enable the search tool
    analyze=True,              # Enable the analyze tool
    add_instructions=True,     # Add default instructions
    add_few_shot=True,         # Add few-shot examples
    few_shot_examples=None,    # Optional custom few-shot examples
)
```


