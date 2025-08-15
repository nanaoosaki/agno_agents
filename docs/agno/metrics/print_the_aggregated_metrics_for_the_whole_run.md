---
title: Print the aggregated metrics for the whole run
category: metrics
source_lines: 1159-1162
line_count: 3
---

# Print the aggregated metrics for the whole run
print("---" * 5, "Collected Metrics", "---" * 5)
pprint(agent.run_response.metrics)
