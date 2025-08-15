---
title: Example 4: Distance Matrix
category: misc
source_lines: 29022-29032
line_count: 10
---

# Example 4: Distance Matrix
print("\n=== Distance Matrix Example ===")
agent.print_response(
    """Calculate the travel time and distance between these locations in Phoenix:
    Origins: ['Phoenix Sky Harbor Airport', 'Downtown Phoenix']
    Destinations: ['Desert Botanical Garden', 'Phoenix Zoo']""",
    markdown=True,
    stream=True,
)

