---
title: Create Local PDF knowledge base
category: knowledge
source_lines: 13042-13051
line_count: 9
---

# Create Local PDF knowledge base
local_pdf_kb = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)

