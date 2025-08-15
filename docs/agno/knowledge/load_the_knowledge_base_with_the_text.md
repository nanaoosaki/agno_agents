---
title: Load the knowledge base with the text
category: knowledge
source_lines: 61743-61753
line_count: 10
---

# Load the knowledge base with the text
asyncio.run(
    knowledge_base.load_text(text="Agno is the best framework for building Agents")
)

```

Then use the `lightrag_knowledge_base` with an Agent:

```python agent.py
