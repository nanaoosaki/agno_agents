---
title: Create CSV knowledge base
category: knowledge
source_lines: 13014-13023
line_count: 9
---

# Create CSV knowledge base
csv_kb = CSVKnowledgeBase(
    path=Path("data/csvs"),
    vector_db=PgVector(
        table_name="csv_documents",
        db_url=db_url,
    ),
)

