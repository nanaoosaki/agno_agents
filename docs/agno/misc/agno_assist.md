---
title: Agno Assist
category: misc
source_lines: 8672-8693
line_count: 21
---

# Agno Assist
Source: https://docs.agno.com/examples/applications/playground/agno_assist



## Code

````python cookbook/apps/playground/agno_assist.py 
from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.dalle import DalleTools
from agno.tools.eleven_labs import ElevenLabsTools
from agno.tools.python import PythonTools
from agno.vectordb.lancedb import LanceDb, SearchType

