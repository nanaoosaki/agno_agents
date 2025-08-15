---
title: Print response (which includes processing streaming responses)
category: advanced
source_lines: 21749-21757
line_count: 8
---

# Print response (which includes processing streaming responses)
print("Running with reasoning_model specified (streaming)...")
streaming_agent_with_model.print_response(
    "What is the value of 5! (factorial)?",
    stream=True,
    show_full_reasoning=True,
)

