---
title: Custom function step that has access to ALL previous step outputs
category: misc
source_lines: 56334-56380
line_count: 46
---

# Custom function step that has access to ALL previous step outputs


def create_comprehensive_report(step_input: StepInput) -> StepOutput:
    """
    Custom function that creates a report using data from multiple previous steps.
    This function has access to ALL previous step outputs and the original workflow message.
    """

    # Access original workflow input
    original_topic = step_input.message or ""

    print(f"--> Original topic: {original_topic}")

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
        step_name="comprehensive_report", content=report.strip(), success=True
    )


comprehensive_report_step = Step(
    name="comprehensive_report",
    executor=create_comprehensive_report,
    description="Create comprehensive report from all research sources",
)

