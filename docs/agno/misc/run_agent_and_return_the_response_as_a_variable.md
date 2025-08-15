---
title: Run agent and return the response as a variable
category: misc
source_lines: 1751-1786
line_count: 35
---

# Run agent and return the response as a variable
agent.print_response("Tell me a 5 second short story about a robot")
```

## Multi-user, multi-session Agents

Each user that is interacting with an Agent gets a unique set of sessions and you can have multiple users interacting with the same Agent at the same time.

Set a `user_id` to connect a user to their sessions with the Agent.

In the example below, we set a `session_id` to demo how to have multi-turn conversations with multiple users at the same time. In production, the `session_id` is auto generated.

<Note>
  Note: Multi-user, multi-session currently only works with `Memory.v2`, which will become the default memory implementation in the next release.
</Note>

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory.v2 import Memory

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Multi-user, multi-session only work with Memory.v2
    memory=Memory(),
    add_history_to_messages=True,
    num_history_runs=3,
)

user_1_id = "user_101"
user_2_id = "user_102"

user_1_session_id = "session_101"
user_2_session_id = "session_102"

