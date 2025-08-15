---
title: Reliability with Single Tool
category: misc
source_lines: 33709-33747
line_count: 38
---

# Reliability with Single Tool
Source: https://docs.agno.com/examples/evals/reliability/basic

Evaluation to assert an Agent is making the expected tool calls.

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


