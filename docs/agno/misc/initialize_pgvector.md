---
title: Initialize PgVector
category: misc
source_lines: 14451-14456
line_count: 5
---

# Initialize PgVector
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

vector_db = PgVector(table_name="recipes", db_url=db_url)

