---
title: Set up SQL storage for the agent's data
category: misc
source_lines: 21379-21383
line_count: 4
---

# Set up SQL storage for the agent's data
storage = SqliteStorage(table_name="recipes", db_file="data.db")
storage.create()  # Create the storage if it doesn't exist

