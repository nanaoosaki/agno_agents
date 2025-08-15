---
title: Print the aggregated metrics for the whole session
category: metrics
source_lines: 1162-1200
line_count: 38
---

# Print the aggregated metrics for the whole session
print("---" * 5, "Session Metrics", "---" * 5)
pprint(agent.session_metrics)
```

You'd see the outputs with following information:

### Tool Execution Metrics

This section provides metrics for each tool execution. It includes details about the resource usage and performance of individual tool calls.

![Tool Run Message Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/tools-run-message-metrics.png)

### Message Metrics

Here, you can see the metrics for each message response from the agent. All "assistant" responses will have metrics like this, helping you understand the performance and resource usage at the message level.

![Agent Run Message Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent-run-message-metrics.png)

### Aggregated Run Metrics

The aggregated metrics provide a comprehensive view of the entire run. This includes a summary of all messages and tool calls, giving you an overall picture of the agent's performance and resource usage.

![Aggregated Run Metrics](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agent-run-aggregated-metrics.png)

Similarly for the session metrics, you can see the aggregated metrics across all runs in the session, providing insights into the overall performance and resource usage of the agent across multiple runs.

## How Metrics Are Aggregated

* **Per-message**: Each message (assistant, tool, etc.) has its own metrics object.
* **Run-level**: RunResponse.metrics is a dictionary where each key (e.g., input\_tokens) maps to a list of values from all assistant messages in the run.
* **Session-level**: `SessionMetrics` (see `agent.session_metrics`) aggregates metrics across all runs in the session.

## `MessageMetrics` Params

<Snippet file="message_metrics_params.mdx" />


