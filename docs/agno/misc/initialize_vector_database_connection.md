---
title: Initialize vector database connection
category: misc
source_lines: 61018-61020
line_count: 2
---

# Initialize vector database connection
vector_db = Qdrant(collection="thai-recipes", url="http://localhost:6333", embedder=embedder)
