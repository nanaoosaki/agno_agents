---
title: Initialize hybrid vector DB
category: misc
source_lines: 61393-61400
line_count: 7
---

# Initialize hybrid vector DB
hybrid_db = PgVector(
    table_name="recipes",
    db_url=db_url,
    search_type=SearchType.hybrid  # Hybrid Search
)

