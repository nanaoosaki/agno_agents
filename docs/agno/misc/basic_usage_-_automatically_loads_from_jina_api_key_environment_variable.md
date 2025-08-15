---
title: Basic usage - automatically loads from JINA_API_KEY environment variable
category: misc
source_lines: 5939-5944
line_count: 5
---

# Basic usage - automatically loads from JINA_API_KEY environment variable
embeddings = JinaEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

