---
title: Usage examples
category: misc
source_lines: 84912-84970
line_count: 58
---

# Usage examples
media_workflow.print_response("Create an image of a magical forest", markdown=True)
media_workflow.print_response("Create a cinematic video of city timelapse", markdown=True)
```

**More Examples**:

* [`workflow_using_steps.py`](/examples/workflows_2/01-basic-workflows/workflow_using_steps)
* [`workflow_using_steps_nested.py`](/examples/workflows_2/01-basic-workflows/workflow_using_steps_nested)
* [`selector_for_image_video_generation_pipelines.py`](/examples/workflows_2/05-workflows-conditional-branching/selector_for_image_video_generation_pipelines)

### 9. Advanced Workflow Patterns

You can use the patterns above to construct sophisticated workflows.

**Example Usage**: Conditions + Parallel + Loops + Custom Post-Processing Function + Routing

```python
from agno.workflow.v2 import Condition, Loop, Parallel, Router, Step, Workflow

def research_post_processor(step_input) -> StepOutput:
    """Post-process and consolidate research data from parallel conditions"""
    research_data = step_input.previous_step_content or ""
    
    try:
        # Analyze research quality and completeness
        word_count = len(research_data.split())
        has_tech_content = any(keyword in research_data.lower() 
                              for keyword in ["technology", "ai", "software", "tech"])
        has_business_content = any(keyword in research_data.lower() 
                                  for keyword in ["market", "business", "revenue", "strategy"])
        
        # Create enhanced research summary
        enhanced_summary = f"""
            ## Research Analysis Report
            
            **Data Quality:** {"✓ High-quality" if word_count > 200 else "⚠ Limited data"}
            
            **Content Coverage:**
            - Technical Analysis: {"✓ Completed" if has_tech_content else "✗ Not available"}
            - Business Analysis: {"✓ Completed" if has_business_content else "✗ Not available"}
            
            **Research Findings:**
            {research_data}
        """.strip()
        
        return StepOutput(
            content=enhanced_summary,
            success=True,
        )
        
    except Exception as e:
        return StepOutput(
            content=f"Research post-processing failed: {str(e)}",
            success=False,
            error=str(e)
        )

