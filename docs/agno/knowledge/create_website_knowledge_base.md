---
title: Create Website knowledge base
category: knowledge
source_lines: 13032-13042
line_count: 10
---

# Create Website knowledge base
website_kb = WebsiteKnowledgeBase(
    urls=["https://docs.agno.com/introduction"],
    max_links=10,
    vector_db=PgVector(
        table_name="website_documents",
        db_url=db_url,
    ),
)

