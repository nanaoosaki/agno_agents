---
title: Create PDF URL knowledge base
category: knowledge
source_lines: 13023-13032
line_count: 9
---

# Create PDF URL knowledge base
pdf_url_kb = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url=db_url,
    ),
)

