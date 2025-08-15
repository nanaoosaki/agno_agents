---
title: Process the audio and get a response
category: misc
source_lines: 34744-34750
line_count: 6
---

# Process the audio and get a response
agent.run(
    "What's in this recording? Please analyze the content and tone.",
    audio=[Audio(content=response.content, format="wav")],
)

