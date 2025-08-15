---
title: Initialize knowledge base
category: knowledge
source_lines: 69658-69702
line_count: 44
---

# Initialize knowledge base
agno_docs_knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/llms-full.txt"],
    vector_db=LanceDb(
        uri=str(tmp_dir.joinpath("lancedb")),
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
)

team_with_knowledge = Team(
    name="Team with Knowledge",
    members=[web_agent],
    model=OpenAIChat(id="gpt-4o"),
    knowledge=agno_docs_knowledge,
    show_members_responses=True,
    markdown=True,
)

if __name__ == "__main__":
    # Set to False after the knowledge base is loaded
    load_knowledge = True
    if load_knowledge:
        agno_docs_knowledge.load()

    team_with_knowledge.print_response("Tell me about the Agno framework", stream=True)
```

The team can also manage user memories:

```python
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

