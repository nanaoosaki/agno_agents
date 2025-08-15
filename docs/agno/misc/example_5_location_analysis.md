---
title: Example 5: Location Analysis
category: misc
source_lines: 29032-29046
line_count: 14
---

# Example 5: Location Analysis
print("\n=== Location Analysis Example ===")
agent.print_response(
    """Analyze this location in Phoenix:
    Address: '2301 N Central Ave, Phoenix, AZ 85004'
    Please provide:
    1. Exact coordinates
    2. Nearby landmarks
    3. Elevation data
    4. Local timezone""",
    markdown=True,
    stream=True,
)

