---
title: Accuracy with Tools
category: tools
source_lines: 33470-33502
line_count: 32
---

# Accuracy with Tools
Source: https://docs.agno.com/examples/evals/accuracy/accuracy_with_tools

Learn how to evaluate the accuracy of an Agent that is using tools.

This example shows an evaluation that runs the provided agent with the provided input and then evaluates the answer that the agent gives.

## Code

```python
from typing import Optional

from agno.agent import Agent
from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools

evaluation = AccuracyEval(
    model=OpenAIChat(id="o4-mini"),
    agent=Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[CalculatorTools(factorial=True)],
    ),
    input="What is 10!?",
    expected_output="3628800",
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8
```


