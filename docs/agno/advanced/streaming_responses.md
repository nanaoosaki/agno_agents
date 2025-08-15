---
title: Streaming responses
category: advanced
source_lines: 70368-70372
line_count: 4
---

# Streaming responses
for chunk in team.run("What is the weather in Tokyo?", stream=True):
    print(chunk.content, end="", flush=True)

