---
title: Advanced Concepts in Workflows
category: misc
source_lines: 82322-82435
line_count: 113
---

# Advanced Concepts in Workflows
Source: https://docs.agno.com/workflows_2/advanced

Explore advanced features and concepts in the Agno workflow system, including custom functions, error handling, and streaming capabilities.

## How Custom Functions Work

Custom functions provide flexibility by allowing developers to define specific logic for step execution. They can be used to `preprocess inputs`, `call agents`, and `postprocess outputs`.

* **executor**: Step can be defined with a custom execution function that handles the step logic.
* **Integration with Agents and Teams**: Custom functions can interact with agents and teams, leveraging their capabilities.

While defining a `Step`, you can specify a custom function as an `executor`. This function should accept a `StepInput` object and return a `StepOutput` object.

```python
content_planning_step = Step(
    name="Content Planning Step",
    executor=custom_content_planning_function,
)

def custom_content_planning_function(step_input: StepInput) -> StepOutput:
    """
    Custom function that does intelligent content planning with context awareness
    """
    message = step_input.message
    previous_step_content = step_input.previous_step_content

    # Create intelligent planning prompt
    planning_prompt = f"""
        STRATEGIC CONTENT PLANNING REQUEST:

        Core Topic: {message}

        Research Results: {previous_step_content[:500] if previous_step_content else "No research results"}

        Planning Requirements:
        1. Create a comprehensive content strategy based on the research
        2. Leverage the research findings effectively
        3. Identify content formats and channels
        4. Provide timeline and priority recommendations
        5. Include engagement and distribution strategies

        Please create a detailed, actionable content plan.
    """

    try:
        response = content_planner.run(planning_prompt)

        enhanced_content = f"""
            ## Strategic Content Plan

            **Planning Topic:** {message}

            **Research Integration:** {"✓ Research-based" if previous_step_content else "✗ No research foundation"}

            **Content Strategy:**
            {response.content}

            **Custom Planning Enhancements:**
            - Research Integration: {"High" if previous_step_content else "Baseline"}
            - Strategic Alignment: Optimized for multi-channel distribution
            - Execution Ready: Detailed action items included
        """.strip()

        return StepOutput(content=enhanced_content, response=response)

    except Exception as e:
        return StepOutput(
            content=f"Custom content planning failed: {str(e)}",
            success=False,
        )
```

Just make sure to follow this structure and return the output as a `StepOutput` object.

```python
def custom_content_planning_function(step_input: StepInput) -> StepOutput:
    # Custom preprocessing
    # Call the agent
    # Custom postprocessing
    return StepOutput(content=enhanced_content)
```

**More Examples**:

* [Step with a Custom Function](/examples/workflows_2/01-basic-workflows/step_with_function)

## Run a Workflow non-blocking (in the background)

You can run a workflow as a non-blocking task by passing `background=True` to `Workflow.arun()`. This will return a `WorkflowRunResponse` object with a `run_id` that you can use to poll for the result of the workflow until it is completed.

<Note>
  This feature is only available for async workflows using `.arun()`.
  For long-running workflows, you can poll for the result using `result = workflow.get_run(run_id)` which returns the updated `WorkflowRunResponse`.

  Use `.has_completed()` to check if the workflow has finished executing. This is particularly useful for workflows that involve time-consuming operations like large-scale data processing, multi-step research tasks, or batch operations that you don't want to block your main application thread.
</Note>

```python
import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run.base import RunStatus
from agno.run.v2.workflow import WorkflowRunResponse
from agno.storage.sqlite import SqliteStorage
from agno.team import Team
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow

