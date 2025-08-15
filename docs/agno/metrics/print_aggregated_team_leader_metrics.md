---
title: Print aggregated team leader metrics
category: metrics
source_lines: 70007-70011
line_count: 4
---

# Print aggregated team leader metrics
print("---" * 5, "Aggregated Metrics of Team Agent", "---" * 5)
pprint(team.run_response.metrics)

