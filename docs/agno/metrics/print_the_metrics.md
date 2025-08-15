---
title: Print the metrics
category: metrics
source_lines: 20237-20240
line_count: 3
---

# Print the metrics
print("---" * 5, "Aggregated Metrics", "---" * 5)
pprint(agent.run_response.metrics)
