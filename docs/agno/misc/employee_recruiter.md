---
title: Employee Recruiter
category: misc
source_lines: 57665-57736
line_count: 71
---

# Employee Recruiter
Source: https://docs.agno.com/examples/workflows_2/employee-recruiter

This example demonstrates how to migrate from the similar workflows 1.0 example to workflows 2.0 structure.

Employee Recruitment Workflow with Simulated Tools

This workflow automates the complete employee recruitment process from resume screening
to interview scheduling and email communication. It demonstrates a multi-agent system
working together to handle different aspects of the hiring pipeline.

Workflow Overview:

1. **Resume Screening**: Analyzes candidate resumes against job requirements and scores them
2. **Interview Scheduling**: Schedules interviews for qualified candidates (score >= 5.0)
3. **Email Communication**: Sends professional interview invitation emails

Key Features:

* **Multi-Agent Architecture**: Uses specialized agents for screening, scheduling, and email writing
* **Async Streaming**: Provides real-time feedback during execution
* **Simulated Tools**: Uses mock Zoom scheduling and email sending for demonstration
* **Resume Processing**: Extracts text from PDF resumes via URLs
* **Structured Responses**: Uses Pydantic models for type-safe data handling
* **Session State**: Caches resume content to avoid re-processing

Agents:

* **Screening Agent**: Evaluates candidates and provides scores/feedback
* **Scheduler Agent**: Creates interview appointments with realistic time slots
* **Email Writer Agent**: Composes professional interview invitation emails
* **Email Sender Agent**: Handles email delivery (simulated)

Usage:
python employee\_recruiter\_async\_stream.py

Input Parameters:

* message: Instructions for the recruitment process
* candidate\_resume\_urls: List of PDF resume URLs to process
* job\_description: The job posting requirements and details

Output:

* Streaming updates on each phase of the recruitment process
* Candidate screening results with scores and feedback
* Interview scheduling confirmations
* Email delivery confirmations

Note: This workflow uses simulated tools for Zoom scheduling and email sending
to demonstrate the concept, you can use the real tools in practice.

Run `pip install openai agno pypdf` to install dependencies.

```python employee_recruiter_async_stream.py

import asyncio
import io
import random
from datetime import datetime, timedelta
from typing import Any, List

import requests
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.workflow.v2.types import WorkflowExecutionInput
from agno.workflow.v2.workflow import Workflow
from pydantic import BaseModel, Field
from pypdf import PdfReader


