---
title: Print full team session metrics (including all members)
category: metrics
source_lines: 70030-70102
line_count: 72
---

# Print full team session metrics (including all members)
print("---" * 5, "Full Team Session Metrics", "---" * 5)
pprint(team.full_team_session_metrics)
```

## Team Leader Metrics

### Team Leader Message Metrics

This section provides metrics for each message response from the team leader. All "assistant" responses will have metrics like this, helping you understand the performance and resource usage at the message level.

![Team Leader Message Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/team-leader-message-metrics.png)

### Aggregated Team Leader Metrics

The aggregated metrics provide a comprehensive view of the team leader's run. This includes a summary of all messages and tool calls, giving you an overall picture of the team leader's performance and resource usage.

![Aggregated Team Leader Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/team-leader-aggregated-metrics.png)

## Team Member Metrics

### Individual Member Metrics

Each team member has their own metrics that can be accessed through `team.run_response.member_responses`. This allows you to analyze the performance of individual team members.

![Team Member Message Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/team-member-message-metrics.png)

### Member Response Structure

Each member response contains:

* `messages`: List of messages with individual metrics
* `metrics`: Aggregated metrics for that member's run
* `tools`: Tool executions with their own metrics

## Session-Level Metrics

### Team Leader Session Metrics

The `team.session_metrics` provides aggregated metrics across all runs in the session for the team leader only.

![Team Leader Session Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/team-leader-session-metrics.png)

### Full Team Session Metrics

The `team.full_team_session_metrics` provides comprehensive metrics that include both the team leader and all team members across all runs in the session.

![Full Team Session Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/full-team-session-metrics.png)

## How Metrics Are Aggregated

### Team Leader Level

* **Per-message**: Each message (assistant, tool, etc.) has its own metrics object.
* **Run-level**: `TeamRunResponse.metrics` is a dictionary where each key (e.g., input\_tokens) maps to a list of values from all assistant messages in the run.
* **Session-level**: `team.session_metrics` aggregates metrics across all team leader runs in the session.

### Team Member Level

* **Per-member**: Each team member has their own metrics tracked separately.
* **Member aggregation**: Individual member metrics are aggregated within their respective `RunResponse` objects.
* **Full team aggregation**: `team.full_team_session_metrics` combines metrics from the team leader and all team members.

### Cross-Member Aggregation

* **Session-level**: `team.full_team_session_metrics` provides a complete view of all token usage and performance metrics across the entire team.

## Accessing Member Metrics Programmatically

You can access individual member metrics in several ways:

```python
