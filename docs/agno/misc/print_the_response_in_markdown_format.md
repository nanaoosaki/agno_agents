---
title: Print the response in markdown format
category: misc
source_lines: 1537-1569
line_count: 32
---

# Print the response in markdown format
pprint_run_response(response, markdown=True)
```

## RunResponse

The `Agent.run()` function returns a `RunResponse` object when not streaming. It has the following attributes:

<Note>
  Understanding Metrics

  For a detailed explanation of how metrics are collected and used, please refer to the [Metrics Documentation](/agents/metrics).
</Note>

See detailed documentation in the [RunResponse](/reference/agents/run-response) documentation.

## Streaming Responses

To enable streaming, set `stream=True` when calling `run()`. This will return an iterator of `RunResponseEvent` objects instead of a single response.

<Note>
  From `agno` version `1.6.0`, the `Agent.run()` function returns an iterator of `RunResponseEvent`, not of `RunResponse` objects.
</Note>

```python
from typing import Iterator
from agno.agent import Agent, RunResponseEvent
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4-mini"))

