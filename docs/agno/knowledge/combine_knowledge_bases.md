---
title: Combine knowledge bases
category: knowledge
source_lines: 13051-13065
line_count: 14
---

# Combine knowledge bases
knowledge_base = CombinedKnowledgeBase(
    sources=[
        csv_kb,
        pdf_url_kb,
        website_kb,
        local_pdf_kb,
    ],
    vector_db=PgVector(
        table_name="combined_documents",
        db_url=db_url,
    ),
)

