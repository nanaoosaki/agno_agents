---
title: Named steps for better tracking
category: misc
source_lines: 84637-84838
line_count: 201
---

# Named steps for better tracking
workflow = Workflow(
    name="Content Creation Pipeline",
    steps=[
        Step(name="Research Phase", team=researcher),
        Step(name="Analysis Phase", executor=custom_function), 
        Step(name="Writing Phase", agent=writer),
    ]
)

workflow.print_response(
    "AI trends in 2024",
    markdown=True,
)
```

**See Examples**:

* [Sequence of Steps](/examples/workflows_2/01-basic-workflows/sequence_of_steps)
* [Step with a Custom Function](/examples/workflows_2/01-basic-workflows/step_with_function)

### 4. Conditional Steps

**When to use**: Conditional step execution based on business logic.

**Example Use-Cases**: Topic-specific research strategies, content type routing

![Condition Steps](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/condition_steps.png)

#### Parameters

<Snippet file="condition-step-reference.mdx" />

#### Example

```python
from agno.workflow.v2 import Condition, Step, Workflow

def is_tech_topic(step_input) -> bool:
    topic = step_input.message.lower()
    return any(keyword in topic for keyword in ["ai", "tech", "software"])

workflow = Workflow(
    name="Conditional Research",
    steps=[
        Condition(
            name="Tech Topic Check",
            evaluator=is_tech_topic,
            steps=[Step(name="Tech Research", agent=tech_researcher)]
        ),
        Step(name="General Analysis", agent=general_analyst),
    ]
)

workflow.print_response("Comprehensive analysis of AI and machine learning trends", markdown=True)
```

**More Examples**:

* [Condition Steps Workflow](/examples/workflows_2/02-workflows-conditional-execution/condition_steps_workflow_stream)
* [Condition with List of Steps](/examples/workflows_2/02-workflows-conditional-execution/condition_with_list_of_steps)

### 5. Parallel Execution

**When to use**: Independent tasks that can run simultaneously to save time.

**Example Use-Cases**: Multiple research sources, parallel content creation

![Parallel Steps](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/parallel_steps.png)

#### Parameters

<Snippet file="parallel-step-reference.mdx" />

#### Example

```python
from agno.workflow.v2 import Parallel, Step, Workflow

workflow = Workflow(
    name="Parallel Research Pipeline",
    steps=[
        Parallel(
            Step(name="HackerNews Research", agent=hn_researcher),
            Step(name="Web Research", agent=web_researcher),
            Step(name="Academic Research", agent=academic_researcher),
            name="Research Step"
        ),
        Step(name="Synthesis", agent=synthesizer),  # Combines the results and produces a report
    ]
)

workflow.print_response("Write about the latest AI developments", markdown=True)
```

**More Examples**:

* [Parallel Steps Workflow](/examples/workflows_2/04-workflows-parallel-execution/parallel_steps_workflow)

### 6. Loop/Iteration Workflows

**When to use**: Quality-driven processes, iterative refinement, or retry logic.

**Example Use-Cases**: Research until sufficient quality, iterative improvement

![Loop Steps](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/loop_steps.png)

#### Parameters

<Snippet file="loop-step-reference.mdx" />

#### Example

```python
from agno.workflow.v2 import Loop, Step, Workflow

def quality_check(outputs) -> bool:
    # Return True to break loop, False to continue
    return any(len(output.content) > 500 for output in outputs)

workflow = Workflow(
    name="Quality-Driven Research",
    steps=[
        Loop(
            name="Research Loop",
            steps=[Step(name="Deep Research", agent=researcher)],
            end_condition=quality_check,
            max_iterations=3
        ),
        Step(name="Final Analysis", agent=analyst),
    ]
)

workflow.print_response("Research the impact of renewable energy on global markets", markdown=True)
```

**More Examples**:

* [Loop Steps Workflow](/examples/workflows_2/03-workflows-loop-execution/loop_steps_workflow)

### 7. Branching Workflows

**When to use**: Complex decision trees, topic-specific workflows, dynamic routing.

**Example Use-Cases**: Content type detection, expertise routing

![Router Steps](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/router_steps.png)

#### Parameters

<Snippet file="router-step-reference.mdx" />

#### Example

```python
from agno.workflow.v2 import Router, Step, Workflow

def route_by_topic(step_input) -> List[Step]:
    topic = step_input.message.lower()
    
    if "tech" in topic:
        return [Step(name="Tech Research", agent=tech_expert)]
    elif "business" in topic:
        return [Step(name="Business Research", agent=biz_expert)]
    else:
        return [Step(name="General Research", agent=generalist)]

workflow = Workflow(
    name="Expert Routing",
    steps=[
        Router(
            name="Topic Router",
            selector=route_by_topic,
            choices=[tech_step, business_step, general_step]
        ),
        Step(name="Synthesis", agent=synthesizer),
    ]
)

workflow.print_response("Latest developments in artificial intelligence and machine learning", markdown=True)
```

**More Examples**:

* [Router Steps Workflow](/examples/workflows_2/05-workflows-conditional-branching/router_steps_workflow)

### 8. Steps: Grouping a list of steps

**When to use**: When you need to group multiple steps into logical sequences, create reusable workflows, or organize complex workflows with multiple branching paths.

**Better Routing**: Use with Router for clean branching logic

#### Parameters

<Snippet file="steps-reference.mdx" />

#### Basic Example

```python
from agno.workflow.v2 import Steps, Step, Workflow

