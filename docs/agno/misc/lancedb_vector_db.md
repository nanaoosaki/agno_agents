---
title: LanceDB Vector DB
category: misc
source_lines: 80597-80604
line_count: 7
---

# LanceDB Vector DB
vector_db = LanceDb(
    table_name="recipes",
    uri="/tmp/lancedb",
    search_type=SearchType.keyword,
)

