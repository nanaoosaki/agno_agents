---
title: Together Embedder
category: misc
source_lines: 6240-6254
line_count: 14
---

# Together Embedder
Source: https://docs.agno.com/embedder/together



The `TogetherEmbedder` can be used to embed text data into vectors using the Together API. Together uses the OpenAI API specification, so the `TogetherEmbedder` class is similar to the `OpenAIEmbedder` class, incorporating adjustments to ensure compatibility with the Together platform. Get your key from [here](https://api.together.xyz/settings/api-keys).

## Usage

```python cookbook/embedders/together_embedder.py
from agno.agent import AgentKnowledge
from agno.vectordb.pgvector import PgVector
from agno.embedder.together import TogetherEmbedder

