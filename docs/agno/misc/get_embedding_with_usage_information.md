---
title: Get embedding with usage information
category: misc
source_lines: 5955-5963
line_count: 8
---

# Get embedding with usage information
embedding, usage = custom_embedder.get_embedding_and_usage(
    "Advanced text processing with Jina embeddings and late chunking."
)
print(f"Embedding dimensions: {len(embedding)}")
if usage:
    print(f"Usage info: {usage}")

