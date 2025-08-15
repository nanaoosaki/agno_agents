---
title: Evaluate the accuracy of the Team's responses
category: misc
source_lines: 33456-33470
line_count: 14
---

# Evaluate the accuracy of the Team's responses
evaluation = AccuracyEval(
    model=OpenAIChat(id="o4-mini"),
    team=multi_language_team,
    input="Comment allez-vous?",
    expected_output="I can only answer in the following languages: English and Spanish.",
    num_iterations=1,
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8
```


