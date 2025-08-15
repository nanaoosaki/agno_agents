---
title: Serper Tools
category: tools
source_lines: 30356-30437
line_count: 81
---

# Serper Tools
Source: https://docs.agno.com/examples/concepts/tools/search/serper



**[Serper](https://serper.dev/)** is a Google Search API that provides access to Google search results, news articles, academic papers from Google Scholar, business reviews, and web scraping capabilities.

## Setup

Get an API key from [Serper Console](https://serper.dev/api-keys).

## Examples

```python cookbook/tools/serper_tools.py
from agno.agent import Agent
from agno.tools.serper import SerperTools

agent = Agent(
    tools=[SerperTools()],
    show_tool_calls=True,
)

agent.print_response(
    "Search for the latest news about artificial intelligence developments",
    markdown=True,
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export SERPER_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U requests openai agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/tools/serper_tools.py
    ```
  </Step>
</Steps>

### Google Scholar Search

```python
agent.print_response(
    "Find recent academic papers about large language model safety",
    markdown=True,
)
```

### Reviews Search

```python
agent.print_response(
    "Analyze reviews for this Google Place ID: ChIJ_Yjh6Za1j4AR8IgGUZGDDTs",
    markdown=True
)
```

### Web Scraping

```python
agent.print_response(
    "Scrape and summarize content from https://openai.com/index/gpt-4/",
    markdown=True
)
```


