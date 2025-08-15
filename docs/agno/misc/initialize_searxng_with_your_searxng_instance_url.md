---
title: Initialize Searxng with your Searxng instance URL
category: misc
source_lines: 77725-77734
line_count: 9
---

# Initialize Searxng with your Searxng instance URL
searxng = SearxngTools(
    host="http://localhost:53153",
    engines=[],
    fixed_max_results=5,
    news=True,
    science=True
)

