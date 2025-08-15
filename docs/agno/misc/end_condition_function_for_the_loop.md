---
title: End condition function for the loop
category: misc
source_lines: 55965-55988
line_count: 23
---

# End condition function for the loop


def research_quality_check(outputs: List[StepOutput]) -> bool:
    """
    Evaluate if research results are sufficient
    Returns True to break the loop, False to continue
    """
    if not outputs:
        return False

    # Check if any output contains substantial content
    for output in outputs:
        if output.content and len(output.content) > 300:
            print(
                f"✅ Research quality check passed - found substantial content ({len(output.content)} chars)"
            )
            return True

    print("❌ Research quality check failed - need more substantial research")
    return False


