---
title: Performance with Teams
category: misc
source_lines: 33643-33672
line_count: 29
---

# Performance with Teams
Source: https://docs.agno.com/examples/evals/performance/performance_team_instantiation

Learn how to analyze the runtime and memory usage of an Agno Team.

## Code

```python
"""Run `pip install agno openai` to install dependencies."""

from agno.agent import Agent
from agno.eval.performance import PerformanceEval
from agno.models.openai import OpenAIChat
from agno.team.team import Team

team_member = Agent(model=OpenAIChat(id="gpt-4o"))


def instantiate_team():
    return Team(members=[team_member])


instantiation_perf = PerformanceEval(func=instantiate_team, num_iterations=1000)

if __name__ == "__main__":
    instantiation_perf.run(print_results=True, print_summary=True)
```


