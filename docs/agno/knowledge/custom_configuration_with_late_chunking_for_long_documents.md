---
title: Custom configuration with late chunking for long documents
category: knowledge
source_lines: 5948-5955
line_count: 7
---

# Custom configuration with late chunking for long documents
custom_embedder = JinaEmbedder(
    dimensions=1024,
    late_chunking=True,  # Improved processing for long documents
    timeout=30.0,  # Request timeout in seconds
)

