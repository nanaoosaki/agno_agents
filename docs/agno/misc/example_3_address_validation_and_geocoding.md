---
title: Example 3: Address Validation and Geocoding
category: misc
source_lines: 29013-29022
line_count: 9
---

# Example 3: Address Validation and Geocoding
print("\n=== Address Validation and Geocoding Example ===")
agent.print_response(
    """Please validate and geocode this address: 
    '1600 Amphitheatre Parkway, Mountain View, CA'""",
    markdown=True,
    stream=True,
)

