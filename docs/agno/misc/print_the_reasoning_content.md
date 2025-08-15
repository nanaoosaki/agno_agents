---
title: Print the reasoning_content
category: misc
source_lines: 21702-21712
line_count: 10
---

# Print the reasoning_content
print("\n--- reasoning_content from response ---")
if hasattr(response, "reasoning_content") and response.reasoning_content:
    print(response.reasoning_content)
else:
    print("No reasoning_content found in response")


print("\n\n=== Example 3: Streaming with reasoning=True ===\n")

