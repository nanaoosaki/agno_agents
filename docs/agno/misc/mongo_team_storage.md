---
title: Mongo Team Storage
category: misc
source_lines: 24402-24428
line_count: 26
---

# Mongo Team Storage
Source: https://docs.agno.com/examples/concepts/storage/team_storage/mongodb



Agno supports using MongoDB as a storage backend for Teams using the `MongoDbStorage` class.

## Usage

You need to provide either `db_url` or `client`. The following example uses `db_url`.

```python mongodb_storage_for_team.py
"""
Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean agno` to install the dependencies
"""

from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.mongodb import MongoDbStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel

