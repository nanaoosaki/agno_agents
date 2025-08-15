---
title: Metrics
category: metrics
source_lines: 69930-69972
line_count: 42
---

# Metrics
Source: https://docs.agno.com/teams/metrics

Understanding team run and session metrics in Agno

## Overview

When you run a team in Agno, the response you get (**TeamRunResponse**) includes detailed metrics about the run. These metrics help you understand resource usage (like **token usage** and **time**), performance, and other aspects of the model and tool calls across both the team leader and team members.

Metrics are available at multiple levels:

* **Per-message**: Each message (assistant, tool, etc.) has its own metrics.
* **Per-tool call**: Each tool execution has its own metrics.
* **Per-member run**: Each team member run has its own metrics.
* **Team-level**: The `TeamRunResponse` aggregates metrics across all team leader messages.
* **Session-level**: Aggregated metrics across all runs in the session, for both the team leader and all team members.

<Note>
  Where Metrics Live

  * `TeamRunResponse.metrics`: Aggregated metrics for the team leader's run, as a dictionary.
  * `TeamRunResponse.member_responses`: Individual member responses with their own metrics.
  * `ToolExecution.metrics`: Metrics for each tool call.
  * `Message.metrics`: Metrics for each message (assistant, tool, etc.).
  * `Team.session_metrics`: Session-level metrics for the team leader.
  * `Team.full_team_session_metrics`: Session-level metrics including all team member metrics.
</Note>

## Example Usage

Suppose you have a team that performs some tasks and you want to analyze the metrics after running it. Here's how you can access and print the metrics:

```python
from typing import Iterator

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools
from agno.utils.pprint import pprint_run_response
from rich.pretty import pprint

