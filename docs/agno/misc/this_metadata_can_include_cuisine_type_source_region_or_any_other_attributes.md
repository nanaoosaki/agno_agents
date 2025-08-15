---
title: This metadata can include cuisine type, source, region, or any other attributes
category: misc
source_lines: 15921-15945
line_count: 24
---

# This metadata can include cuisine type, source, region, or any other attributes

knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        {
            "url": "https://agno-public.s3.amazonaws.com/recipes/thai_recipes_short.pdf",
            "metadata": {
                "cuisine": "Thai",
                "source": "Thai Cookbook",
                "region": "Southeast Asia",
            },
        },
        {
            "url": "https://agno-public.s3.amazonaws.com/recipes/cape_recipes_short_2.pdf",
            "metadata": {
                "cuisine": "Cape",
                "source": "Cape Cookbook",
                "region": "South Africa",
            },
        },
    ],
    vector_db=vector_db,
)

