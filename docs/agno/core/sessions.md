---
title: Sessions
category: core
source_lines: 1723-1751
line_count: 28
---

# Sessions
Source: https://docs.agno.com/agents/sessions



When we call `Agent.run()`, it creates a stateless, singular Agent run.

But what if we want to continue this run i.e. have a multi-turn conversation? That's where `sessions` come in. A session is collection of consecutive runs.

In practice, a session is a multi-turn conversation between a user and an Agent. Using a `session_id`, we can connect the conversation history and state across multiple runs.

Let's outline some key concepts:

* **User:** A user represents an individual that interacts with the Agent. Each user has associated memories, sessions, and conversation history separate from other users.
* **Session:** A session is collection of consecutive runs like a multi-turn conversation between a user and an Agent. Sessions are identified by a `session_id` and each turn is a **run**.
* **Run:** Every interaction (i.e. chat or turn) with an Agent is called a **run**. Runs are identified by a `run_id` and `Agent.run()` creates a new `run_id` when called.
* **Messages:** are the individual messages sent between the model and the Agent. Messages are the communication protocol between the Agent and model.

Let's start with an example where a single run is created with an Agent. A `run_id` is automatically generated, as well as a `session_id` (because we didn't provide one to continue the conversation). This run is not yet associated with a user.

```python
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

