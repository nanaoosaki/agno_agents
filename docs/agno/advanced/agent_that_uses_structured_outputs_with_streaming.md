---
title: Agent that uses structured outputs with streaming
category: advanced
source_lines: 2462-2481
line_count: 19
---

# Agent that uses structured outputs with streaming
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You write movie scripts.",
    response_model=MovieScript,
)

structured_output_agent.print_response(
    "New York", stream=True, stream_intermediate_steps=True
)
```

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/async/structured_output.py)
* View [Parser Model Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/other/parse_model.py)
* View [Streaming Structured Output](https://github.com/agno-agi/agno/blob/main/cookbook/models/openai/chat/structured_output_stream.py)


