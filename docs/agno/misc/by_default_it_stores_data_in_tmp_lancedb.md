---
title: By default, it stores data in /tmp/lancedb
category: misc
source_lines: 16392-16398
line_count: 6
---

# By default, it stores data in /tmp/lancedb
vector_db = LanceDb(
    table_name="recipes",
    uri="tmp/lancedb",  # You can change this path to store data elsewhere
)

