---
title: Stream the team response
category: misc
source_lines: 70878-70895
line_count: 17
---

# Stream the team response
market_research_team.print_response(
    "Analyze the technology sector for Q1 2024", 
    stream=True, 
    stream_intermediate_steps=True
)
```

<Note>
  When streaming with teams and structured output, you'll see intermediate steps from individual team members, but the final structured result is delivered as a single complete chunk rather than being streamed progressively.
</Note>

## Developer Resources

* View [Streaming Team Output](https://github.com/agno-agi/agno/blob/main/cookbook/teams/structured_output_streaming.py)


