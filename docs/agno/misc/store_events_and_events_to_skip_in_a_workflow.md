---
title: Store Events and Events to Skip in a Workflow
category: misc
source_lines: 56813-56846
line_count: 33
---

# Store Events and Events to Skip in a Workflow
Source: https://docs.agno.com/examples/workflows_2/06-workflows-advanced-concepts/store_events_and_events_to_skip_in_a_workflow

This example demonstrates **Workflows 2.0** event storage capabilities

This example demonstrates **Workflows 2.0** event storage capabilities, showing how to:

1. **Store execution events** for debugging/auditing (`store_events=True`)
2. **Filter noisy events** (`events_to_skip`) to focus on critical workflow milestones
3. **Access stored events** post-execution via `workflow.run_response.events`

## Key Features:

* **Selective Storage**: Skip verbose events (e.g., `step_started`) while retaining key milestones.
* **Debugging/Audit**: Capture execution flow for analysis without manual logging.
* **Performance Optimization**: Reduce storage overhead by filtering non-essential events.

```python store_events_and_events_to_skip_in_a_workflow.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run.response import (
    RunResponseContentEvent,
    ToolCallCompletedEvent,
    ToolCallStartedEvent,
)
from agno.run.v2.workflow import WorkflowRunEvent
from agno.storage.sqlite import SqliteStorage
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow.v2.parallel import Parallel
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow

