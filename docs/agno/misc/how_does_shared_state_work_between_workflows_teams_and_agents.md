---
title: How does shared state work between workflows, teams and agents?
category: misc
source_lines: 85018-85055
line_count: 37
---

# How does shared state work between workflows, teams and agents?
Source: https://docs.agno.com/workflows_2/workflow_session_state

Learn to handle shared state between the different components of a Workflow

The workflow session state is a powerful feature of the Workflows system that allows for the persistence and sharing of state information across different components of a workflow.
This state is crucial for maintaining continuity in workflows that involve multiple tasks, agents, and teams.

![Workflow Session State](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/workflow_session_state.png)

## How Workflow Session State Works

### 1. Initialization

The workflow session state is initialized when a Workflow object is created. It can be an empty dictionary or pre-populated with initial state data.

```python
shopping_workflow = Workflow(
    name="Shopping List Workflow",
    steps=[manage_items_step, view_list_step],
    workflow_session_state={},  # Initialize empty workflow session state
)
```

### 2. Access and Modification

Agents and teams can access and modify the workflow session state during task execution. This is typically done through methods or tools that interact with the state.

Consider the following example-

```python
from agno.agent.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow


