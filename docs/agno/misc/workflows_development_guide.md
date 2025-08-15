---
title: Workflows Development Guide
category: misc
source_lines: 84525-84637
line_count: 112
---

# Workflows Development Guide
Source: https://docs.agno.com/workflows_2/types_of_workflows

Explore the different types of workflows in the Agno workflow system, including sequential, parallel, conditional, and looping workflows.

Agno Workflows provides a powerful, declarative way to orchestrate multi-step AI processes. Unlike traditional linear workflows, you can now create sophisticated branching logic, parallel execution, and dynamic routing based on content analysis.

This guide covers all workflow patterns, from simple linear sequences to complex conditional logic with parallel execution.

## Building Blocks

The core building blocks of Agno Workflows are:

| Component     | Purpose                         |
| ------------- | ------------------------------- |
| **Step**      | Basic execution unit            |
| **Agent**     | AI assistant with specific role |
| **Team**      | Coordinated group of agents     |
| **Function**  | Custom Python logic             |
| **Parallel**  | Concurrent execution            |
| **Condition** | Conditional execution           |
| **Loop**      | Iterative execution             |
| **Router**    | Dynamic routing                 |

## Workflow Patterns

### 1. Basic Sequential Workflows

**When to use**: Linear processes where each step depends on the previous one.

**Example Steps**: Research → Process research data in a function before next step → Content Creation

```python
from agno.workflow.v2 import Step, Workflow, StepOutput

def data_preprocessor(step_input):
    # Custom preprocessing logic

    # Or you can also run any agent/team over here itself
    # response = some_agent.run(...)
    return StepOutput(content=f"Processed: {step_input.message}") # <-- Now pass the agent/team response in content here

workflow = Workflow(
    name="Mixed Execution Pipeline",
    steps=[
        research_team,      # Team
        data_preprocessor,  # Function
        content_agent,      # Agent
    ]
)

workflow.print_response("Analyze the competitive landscape for fintech startups", markdown=True)
```

<Note>
  For more information on how to use custom functions, refer to the [Advanced](/workflows_2/advanced) page.
</Note>

**See Example**:

* [Sequence of Functions and Agents](/examples/workflows_2/01-basic-workflows/sequence_of_functions_and_agents) - Complete workflow with functions and agents

<Note>
  `StepInput` and `StepOutput` provides standardized interfaces for data flow between steps:
  So if you make a custom function as an executor for a step, make sure that the input and output types are compatible with the `StepInput` and `StepOutput` interfaces.
  This will ensure that your custom function can seamlessly integrate into the workflow system.

  Take a look at the schemas for [`StepInput`](/reference/workflows_2/step_input) and [`StepOutput`](/reference/workflows_2/step_output).
</Note>

### 2. Fully Python Workflow

**Keep it Simple with Pure Python**: If you prefer the Workflows 1.0 approach or need maximum flexibility, you can still use a single Python function to handle everything.
This approach gives you complete control over the execution flow while still benefiting from workflow features like storage, streaming, and session management.

Replace all the steps in the workflow with a single executable function where you can control everything.

```python
def custom_workflow_function(workflow: Workflow, execution_input: WorkflowExecutionInput):
    # Custom orchestration logic
    research_result = research_team.run(execution_input.message)
    analysis_result = analysis_agent.run(research_result.content)
    return f"Final: {analysis_result.content}"

workflow = Workflow(
    name="Function-Based Workflow",
    steps=custom_workflow_function  # Single function replaces all steps
)

workflow.print_response("Evaluate the market potential for quantum computing applications", markdown=True)
```

**See Example**:

* [Function-Based Workflow](/examples/workflows_2/01-basic-workflows/function_instead_of_steps) - Complete function-based workflow

For migration from 1.0 style workflows, refer to the page for [Migrating to Workflows 2.0](./migration)

### 3. Step-Based Workflows

**You can name your steps** for better logging and future support on the Agno platform.\
This also changes the name of a step when accessing that step's output inside a `StepInput` object.

#### Parameters

<Snippet file="step-reference.mdx" />

#### Example

```python
from agno.workflow.v2 import Step, Workflow

