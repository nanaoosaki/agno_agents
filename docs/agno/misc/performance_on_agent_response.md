---
title: Performance on Agent Response
category: misc
source_lines: 33609-33643
line_count: 34
---

# Performance on Agent Response
Source: https://docs.agno.com/examples/evals/performance/performance_simple_response

Example showing how to analyze the runtime and memory usage of an Agent's run, given its response.

## Code

```python

"""Run `pip install openai agno memory_profiler` to install dependencies."""

from agno.agent import Agent
from agno.eval.performance import PerformanceEval
from agno.models.openai import OpenAIChat


def simple_response():
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        system_message="Be concise, reply with one sentence.",
    )
    response = agent.run("What is the capital of France?")
    return response


simple_response_perf = PerformanceEval(
    func=simple_response, num_iterations=1, warmup_runs=0
)

if __name__ == "__main__":
    simple_response_perf.run(print_results=True, print_summary=True)
```


