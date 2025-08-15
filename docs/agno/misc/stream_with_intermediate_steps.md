---
title: Stream with intermediate steps
category: misc
source_lines: 70384-70504
line_count: 120
---

# Stream with intermediate steps
response_stream = team.run(
    "What is the weather in Tokyo?",
    stream=True,
    stream_intermediate_steps=True
)
```

### Handling Events

You can process events as they arrive by iterating over the response stream:

```python
response_stream = team.run("Your prompt", stream=True, stream_intermediate_steps=True)

for event in response_stream:
    if event.event == "TeamRunResponseContent":
        print(f"Content: {event.content}")
    elif event.event == "TeamToolCallStarted":
        print(f"Tool call started: {event.tool}")
    elif event.event == "ToolCallStarted":
        print(f"Member tool call started: {event.tool}")
    elif event.event == "ToolCallCompleted":
        print(f"Member tool call completed: {event.tool}")
    elif event.event == "TeamReasoningStep":
        print(f"Reasoning step: {event.content}")
    ...
```

<Note>
  Team member events are yielded during team execution when a team member is being executed.  You can disable this by setting `stream_member_events=False`.
</Note>

### Storing Events

You can store all the events that happened during a run on the `RunResponse` object.

```python
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

team = Team(model=OpenAIChat(id="gpt-4o-mini"), members=[], store_events=True)

response = team.run("Tell me a 5 second short story about a lion", stream=True, stream_intermediate_steps=True)
pprint_run_response(response)

for event in agent.run_response.events:
    print(event.event)
```

By default the `TeamRunResponseContentEvent` and `RunResponseContentEvent` events are not stored. You can modify which events are skipped by setting the `events_to_skip` parameter.

For example:

```python
team = Team(model=OpenAIChat(id="gpt-4o-mini"), members=[], store_events=True, events_to_skip=[TeamRunEvent.run_started.value])
```

### Event Types

The following events are sent by the `Team.run()` and `Team.arun()` functions depending on team's configuration:

#### Core Events

| Event Type               | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| `TeamRunStarted`         | Indicates the start of a run                            |
| `TeamRunResponseContent` | Contains the model's response text as individual chunks |
| `TeamRunCompleted`       | Signals successful completion of the run                |
| `TeamRunError`           | Indicates an error occurred during the run              |
| `TeamRunCancelled`       | Signals that the run was cancelled                      |

#### Tool Events

| Event Type              | Description                                                    |
| ----------------------- | -------------------------------------------------------------- |
| `TeamToolCallStarted`   | Indicates the start of a tool call                             |
| `TeamToolCallCompleted` | Signals completion of a tool call, including tool call results |

#### Reasoning Events

| Event Type               | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| `TeamReasoningStarted`   | Indicates the start of the agent's reasoning process |
| `TeamReasoningStep`      | Contains a single step in the reasoning process      |
| `TeamReasoningCompleted` | Signals completion of the reasoning process          |

#### Memory Events

| Event Type                  | Description                                     |
| --------------------------- | ----------------------------------------------- |
| `TeamMemoryUpdateStarted`   | Indicates that the agent is updating its memory |
| `TeamMemoryUpdateCompleted` | Signals completion of a memory update           |

See detailed documentation in the [TeamRunResponse](/reference/teams/team-response) documentation.

## Structured Input

A team can be provided with structured input (i.e a pydantic model) by passing it in the `Team.run()` or `Team.print_response()` as the `message` parameter.

```python
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel, Field


class ResearchTopic(BaseModel):
    """Structured research topic with specific requirements"""

    topic: str
    focus_areas: List[str] = Field(description="Specific areas to focus on")
    target_audience: str = Field(description="Who this research is for")
    sources_required: int = Field(description="Number of sources needed", default=5)


