---
title: No event storage
category: misc
source_lines: 82725-82796
line_count: 71
---

# No event storage
fast_workflow = Workflow(
    name="Fast Workflow",
    store_events=False,  
    steps=[...]
)
```

**More Examples**:

* [Store Events and Events to Skip in a Workflow](/examples/workflows_2/06-workflows-advanced-concepts/store_events_and_events_to_skip_in_a_workflow)

## Additional Data

**When to use**: When you need to pass metadata, configuration, or contextual information to specific steps without it being part of the main workflow message flow.

* Separation of Concerns: Keep workflow logic separate from metadata
* Step-Specific Context: Access additional information in custom functions
* Clean Message Flow: Main message stays focused on content
* Flexible Configuration: Pass user info, priorities, settings, etc.

Access Pattern: `step_input.additional_data` provides dictionary access to all additional data

```python
from agno.workflow.v2 import Step, Workflow
from agno.workflow.v2.types import StepInput, StepOutput

def custom_content_planning_function(step_input: StepInput) -> StepOutput:
    """Custom function that uses additional_data for enhanced context"""
    
    # Access the main workflow message
    message = step_input.message
    previous_content = step_input.previous_step_content
    
    # Access additional_data that was passed with the workflow
    additional_data = step_input.additional_data or {}
    user_email = additional_data.get("user_email", "No email provided")
    priority = additional_data.get("priority", "normal")
    client_type = additional_data.get("client_type", "standard")
    
    # Create enhanced planning prompt with context
    planning_prompt = f"""
        STRATEGIC CONTENT PLANNING REQUEST:
        
        Core Topic: {message}
        Research Results: {previous_content[:500] if previous_content else "No research results"}
        
        Additional Context:
        - Client Type: {client_type}
        - Priority Level: {priority}
        - Contact Email: {user_email}
        
        {"🚨 HIGH PRIORITY - Expedited delivery required" if priority == "high" else "📝 Standard delivery timeline"}
        
        Please create a detailed, actionable content plan.
    """
    
    response = content_planner.run(planning_prompt)
    
    enhanced_content = f"""
        ## Strategic Content Plan
        
        **Planning Topic:** {message}
        **Client Details:** {client_type} | {priority.upper()} priority | {user_email}
        
        **Content Strategy:**
        {response.content}
    """
    
    return StepOutput(content=enhanced_content, response=response)

