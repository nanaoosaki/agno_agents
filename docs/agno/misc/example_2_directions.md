---
title: Example 2: Directions
category: misc
source_lines: 29004-29013
line_count: 9
---

# Example 2: Directions
print("\n=== Directions Example ===")
agent.print_response(
    """Get driving directions from 'Phoenix Sky Harbor Airport' to 'Desert Botanical Garden', 
    avoiding highways if possible""",
    markdown=True,
    stream=True,
)

