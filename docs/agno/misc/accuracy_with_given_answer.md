---
title: Accuracy with Given Answer
category: misc
source_lines: 33387-33415
line_count: 28
---

# Accuracy with Given Answer
Source: https://docs.agno.com/examples/evals/accuracy/accuracy_with_given_answer

Learn how to evaluate the accuracy of an Agno Agent's response with a given answer.

For this example an agent won't be executed, but the given result will be evaluated against the expected output for correctness.

## Code

```python
from typing import Optional

from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.openai import OpenAIChat

evaluation = AccuracyEval(
    model=OpenAIChat(id="o4-mini"),
    input="What is 10*5 then to the power of 2? do it step by step",
    expected_output="2500",
    num_iterations=1,
)
result_with_given_answer: Optional[AccuracyResult] = evaluation.run_with_output(
    output="2500", print_results=True
)
assert result_with_given_answer is not None and result_with_given_answer.avg_score >= 8
```


