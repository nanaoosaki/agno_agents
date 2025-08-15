---
title: Accuracy with Teams
category: misc
source_lines: 33415-33430
line_count: 15
---

# Accuracy with Teams
Source: https://docs.agno.com/examples/evals/accuracy/accuracy_with_teams

Learn how to evaluate the accuracy of an Agno Team.

## Code

```python
from typing import Optional

from agno.agent import Agent
from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.openai import OpenAIChat
from agno.team.team import Team

