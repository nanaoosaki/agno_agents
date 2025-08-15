---
title: Create and use workflow
category: misc
source_lines: 84259-84289
line_count: 30
---

# Create and use workflow
if __name__ == "__main__":
    response: Iterator[WorkflowRunResponseEvent] = content_creation_workflow.run(
        message="AI trends in 2024",
        markdown=True,
        stream=True,
    )

    pprint_run_response(response, markdown=True)
```

### Streaming Intermediate Steps

<Note>
  In the case where you put `stream_intermediate_steps=False` (or not set it at all), we only yield `WorkflowStartedEvent`, `WorkflowCompletedEvent` along with all the `Agent/Team` events.
</Note>

For even more detailed streaming, you can enable intermediate steps by setting `stream_intermediate_steps=True`. This will provide real-time updates about each step of the workflow.

```python
from typing import Iterator

from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.workflow.v2.condition import Condition
from agno.workflow.v2.step import Step
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow
from agno.run.v2.workflow import WorkflowRunResponseEvent, WorkflowRunEvent

