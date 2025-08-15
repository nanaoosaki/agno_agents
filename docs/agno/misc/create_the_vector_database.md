---
title: Create the vector database
category: misc
source_lines: 21363-21370
line_count: 7
---

# Create the vector database
vector_db = LanceDb(
    table_name="recipes",  # Table name in the vector database
    uri=db_url,  # Location to initiate/create the vector database
    embedder=embedder,  # Without using this, it will use OpenAIChat embeddings by default
)

