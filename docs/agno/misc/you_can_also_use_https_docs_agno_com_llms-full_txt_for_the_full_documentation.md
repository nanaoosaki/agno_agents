---
title: You can also use `https://docs.agno.com/llms-full.txt` for the full documentation
category: misc
source_lines: 60039-60051
line_count: 12
---

# You can also use `https://docs.agno.com/llms-full.txt` for the full documentation
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

