---
title: Simple Accuracy
category: misc
source_lines: 33502-33535
line_count: 33
---

# Simple Accuracy
Source: https://docs.agno.com/examples/evals/accuracy/basic

Learn to check how complete, correct and accurate an Agno Agent's response is.

This example shows a more complex evaluation that compares the full output of the agent for correctness.

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
        model=OpenAIChat(id="gpt-4o"),
        tools=[CalculatorTools(enable_all=True)],
    ),
    input="What is 10*5 then to the power of 2? do it step by step",
    expected_output="2500",
    additional_guidelines="Agent output should include the steps and the final answer.",
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8
```


