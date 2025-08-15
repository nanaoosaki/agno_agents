---
title: Access metrics for a specific member
category: metrics
source_lines: 70102-70131
line_count: 29
---

# Access metrics for a specific member
for member_response in team.run_response.member_responses:
    print(f"Member: {member_response.member_id}")
    print(f"Member metrics: {member_response.metrics}")
    
    # Access individual messages
    for message in member_response.messages:
        if message.role == "assistant":
            print(f"Message metrics: {message.metrics}")
```

## Metrics Comparison

| Metric Level            | Access Method                    | Description                                    |
| ----------------------- | -------------------------------- | ---------------------------------------------- |
| **Team Leader Run**     | `team.run_response.metrics`      | Aggregated metrics for the current run         |
| **Team Leader Session** | `team.session_metrics`           | Aggregated metrics across all team leader runs |
| **Individual Member**   | `member_response.metrics`        | Metrics for a specific team member's run       |
| **Full Team Session**   | `team.full_team_session_metrics` | Complete team metrics including all members    |

## `MessageMetrics` Params

<Snippet file="message_metrics_params.mdx" />

## `SessionMetrics` Params

<Snippet file="session_metrics_params.mdx" />


