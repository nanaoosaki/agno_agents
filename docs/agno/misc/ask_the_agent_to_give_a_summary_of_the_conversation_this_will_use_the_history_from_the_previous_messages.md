---
title: Ask the agent to give a summary of the conversation, this will use the history from the previous messages
category: misc
source_lines: 1800-1815
line_count: 15
---

# Ask the agent to give a summary of the conversation, this will use the history from the previous messages
agent.print_response(
    "Give me a summary of our conversation.",
    user_id=user_1_id,
    session_id=user_1_session_id,
)
```

## Fetch messages from last N sessions

In some scenarios, you might want to fetch messages from the last N sessions to provide context or continuity in conversations.

Here's an example of how you can achieve this:

```python
