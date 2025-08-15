---
title: Advanced
category: misc
source_lines: 81631-81654
line_count: 23
---

# Advanced
Source: https://docs.agno.com/workflows/advanced



**Workflows are all about control and flexibility.**

Your workflow logic is just a python function, so you have full control over the workflow logic. You can:

* Validate input before processing
* Depending on the input, spawn agents and run them in parallel
* Cache results as needed
* Correct any intermediate errors
* Stream the output
* Return a single or multiple outputs

**This level of control is critical for reliability.**

## Streaming

It is important to understand that when you build a workflow, you are writing a python function, meaning you decide if the function streams the output or not. To stream the output, yield an `Iterator[RunResponse]` from the `run()` method of your workflow.

```python news_report_generator.py
