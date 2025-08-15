---
title: Personalized Email Generator
category: misc
source_lines: 53112-53182
line_count: 70
---

# Personalized Email Generator
Source: https://docs.agno.com/examples/workflows/personalized-email-generator



This workflow helps sales professionals craft highly personalized cold emails by:

1. Researching target companies through their websites
2. Analyzing their business model, tech stack, and unique attributes
3. Generating personalized email drafts
4. Sending test emails to yourself for review before actual outreach

## Why is this helpful?

• You always have an extra review step—emails are sent to you first.
This ensures you can fine-tune messaging before reaching your actual prospect.
• Ideal for iterating on tone, style, and personalization en masse.

## Who should use this?

• SDRs, Account Executives, Business Development Managers
• Founders, Marketing Professionals, B2B Sales Representatives
• Anyone building relationships or conducting outreach at scale

## Example use cases:

• SaaS sales outreach
• Consulting service proposals
• Partnership opportunities
• Investor relations
• Recruitment outreach
• Event invitations

## Quick Start:

1. Install dependencies:
   pip install openai agno

2. Set environment variables:
   * export OPENAI\_API\_KEY="xxxx"

3. Update sender\_details\_dict with YOUR info.

4. Add target companies to "leads" dictionary.

5. Run:
   python personalized\_email\_generator.py

The script will send draft emails to your email first if DEMO\_MODE=False.
If DEMO\_MODE=True, it prints the email to the console for review.

Then you can confidently send the refined emails to your prospects!

## Code

```python personalized_email_generator.py
import json
from datetime import datetime
from textwrap import dedent
from typing import Dict, Iterator, List, Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.exa import ExaTools
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import RunResponse, Workflow
from pydantic import BaseModel, Field

