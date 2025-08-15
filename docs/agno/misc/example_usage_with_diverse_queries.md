---
title: Example usage with diverse queries
category: misc
source_lines: 34273-34285
line_count: 12
---

# Example usage with diverse queries
agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA", stream=True
)
agent_team.print_response(
    "What's the market outlook and financial performance of AI semiconductor companies?",
    stream=True,
)
agent_team.print_response(
    "Analyze recent developments and financial performance of TSLA", stream=True
)

