---
title: Steps reference these agents
category: misc
source_lines: 82881-82933
line_count: 52
---

# Steps reference these agents
workflow = Workflow(steps=[
    Step(agent=research_agent),  # Will output ResearchFindings
    Step(agent=analysis_agent)   # Will output AnalysisResults
])
```

### Structured Data Transformation in Custom Functions

Custom functions in workflows can access the structured output of previous steps via `step_input.previous_step_content`, which preserves the original Pydantic model type (e.g., ResearchFindings). To transform data:

* Type-Check Inputs: Use `isinstance(step_input.previous_step_content, ModelName)` to verify the input structure.
* Modify Data: Extract fields (e.g., `step_input.previous_step_content.topic`), process them, and construct a new Pydantic model (e.g., AnalysisReport).
* Return Typed Output: Wrap the new model in `StepOutput(content=new_model)`. This ensures type safety for downstream steps. Example:

```python
   def transform_data(step_input: StepInput) -> StepOutput:
       research = step_input.previous_step_content  # Type: ResearchFindings
       analysis = AnalysisReport(
           analysis_type="Custom",
           key_findings=[f"Processed: {research.topic}"],
           ...  # Modified fields
       )
       return StepOutput(content=analysis)
```

**More Examples**:

* [Structured IO at each Step Level](/examples/workflows_2/06-workflows-advanced-concepts/structured_io_at_each_step_level)

## Media Input

Workflows seamlessly handle media artifacts (images, videos, audio) throughout the execution pipeline.
Media can be provided as input for `Workflow.run()` and `Workflow.print_response()` and is passed through to individual steps (whether Agent, Team or Custom Function).

During execution, media artifacts accumulate across steps - each step receives shared media from previous steps and can
produce additional media outputs. The `Step` class handles automatic conversion between artifact formats, ensuring compatibility between
workflow components and `agent/team` executors. All media artifacts are preserved in `StepOutput` and propagated to
subsequent steps, creating a comprehensive flow where the final `WorkflowRunResponse` contains all accumulated
`images`, `videos`, and `audio` from the entire execution chain.

Here's an example of how to pass image as input:

```python
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.workflow.v2.step import Step
from agno.workflow.v2.workflow import Workflow
from agno.storage.sqlite import SqliteStorage

