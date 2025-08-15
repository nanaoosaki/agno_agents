---
title: Test with vulnerable code - workflow stops at security gate
category: misc
source_lines: 82572-82621
line_count: 49
---

# Test with vulnerable code - workflow stops at security gate
workflow.print_response("Scan this code: exec(input('Enter command: '))")
```

**More Examples**:

* [Early Stop Workflow](/examples/workflows_2/06-workflows-advanced-concepts/early_stop_workflow)

## Access Multiple Previous Steps Output

Advanced workflows often need to access data from multiple previous steps, not just the immediate previous step. The `StepInput` object provides powerful methods to access any previous step's output by name or get all previous content.

```python
def create_comprehensive_report(step_input: StepInput) -> StepOutput:
    """
    Custom function that creates a report using data from multiple previous steps.
    This function has access to ALL previous step outputs and the original workflow message.
    """

    # Access original workflow input
    original_topic = step_input.workflow_message or ""

    # Access specific step outputs by name
    hackernews_data = step_input.get_step_content("research_hackernews") or ""
    web_data = step_input.get_step_content("research_web") or ""

    # Or access ALL previous content
    all_research = step_input.get_all_previous_content()

    # Create a comprehensive report combining all sources
    report = f"""
        # Comprehensive Research Report: {original_topic}

        ## Executive Summary
        Based on research from HackerNews and web sources, here's a comprehensive analysis of {original_topic}.

        ## HackerNews Insights
        {hackernews_data[:500]}...

        ## Web Research Findings  
        {web_data[:500]}...
    """

    return StepOutput(
        step_name="comprehensive_report", 
        content=report.strip(), 
        success=True
    )

