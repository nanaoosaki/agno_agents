---
title: Reliability with Multiple Tools
category: tools
source_lines: 33747-33785
line_count: 38
---

# Reliability with Multiple Tools
Source: https://docs.agno.com/examples/evals/reliability/reliability_with_multiple_tools

Learn how to assert an Agno Agent is making multiple expected tool calls.

## Code

```python
from typing import Optional

from agno.agent import Agent
from agno.eval.reliability import ReliabilityEval, ReliabilityResult
from agno.models.openai import OpenAIChat
from agno.run.response import RunResponse
from agno.tools.calculator import CalculatorTools


def multiply_and_exponentiate():
    agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(add=True, multiply=True, exponentiate=True)],
    )
    response: RunResponse = agent.run(
        "What is 10*5 then to the power of 2? do it step by step"
    )
    evaluation = ReliabilityEval(
        agent_response=response,
        expected_tool_calls=["multiply", "exponentiate"],
    )
    result: Optional[ReliabilityResult] = evaluation.run(print_results=True)
    result.assert_passed()


if __name__ == "__main__":
    multiply_and_exponentiate()
```


