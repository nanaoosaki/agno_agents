---
title: Initialize the Agent with the combined knowledge base
category: knowledge
source_lines: 13065-13073
line_count: 8
---

# Initialize the Agent with the combined knowledge base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

knowledge_base.load(recreate=False)

