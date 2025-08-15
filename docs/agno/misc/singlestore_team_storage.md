---
title: Singlestore Team Storage
category: misc
source_lines: 24729-24759
line_count: 30
---

# Singlestore Team Storage
Source: https://docs.agno.com/examples/concepts/storage/team_storage/singlestore



Agno supports using Singlestore as a storage backend for Teams using the `SingleStoreStorage` class.

## Usage

Obtain the credentials for Singlestore from [here](https://portal.singlestore.com/)

```python singlestore_storage_for_team.py
"""
Run: `pip install openai duckduckgo-search newspaper4k lxml_html_clean agno` to install the dependencies
"""

import os
from os import getenv
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.singlestore import SingleStoreStorage
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.utils.certs import download_cert
from pydantic import BaseModel
from sqlalchemy.engine import create_engine

