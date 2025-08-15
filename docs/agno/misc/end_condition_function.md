---
title: End condition function
category: misc
source_lines: 55663-55689
line_count: 26
---

# End condition function
def research_evaluator(outputs: List[StepOutput]) -> bool:
    """
    Evaluate if research results are sufficient
    Returns True to break the loop, False to continue
    """
    # Check if we have good research results
    if not outputs:
        return False

    # Calculate total content length from all outputs
    total_content_length = sum(len(output.content or "") for output in outputs)

    # Check if we have substantial content (more than 500 chars total)
    if total_content_length > 500:
        print(
            f"✅ Research evaluation passed - found substantial content ({total_content_length} chars total)"
        )
        return True

    print(
        f"❌ Research evaluation failed - need more substantial research (current: {total_content_length} chars)"
    )
    return False


