---
title: Apify
category: misc
source_lines: 74506-74539
line_count: 33
---

# Apify
Source: https://docs.agno.com/tools/toolkits/others/apify



This guide demonstrates how to integrate and use [Apify](https://apify.com/actors) Actors within the Agno framework to enhance your AI agents with web scraping, crawling, data extraction, and web automation capabilities.

## What is Apify?

[Apify](https://apify.com/) is a platform that provides:

* Data collection services for AI Agents, specializing in extracting data from social media, search engines, online maps, e-commerce sites, travel portals, or general websites
* A marketplace of ready-to-use Actors (specialized tools) for various data tasks
* Infrastructure to run and monetize our own AI Agents

## Prerequisites

1. Sign up for an [Apify account](https://console.apify.com/sign-up)
2. Obtain your Apify API token (can be obtained from [Apify](https://docs.apify.com/platform/integrations/api))
3. Install the required packages:

```bash
pip install agno apify-client
```

## Basic Usage

The Agno framework makes it easy to integrate Apify Actors into your agents. Here's a simple example:

```python
from agno.agent import Agent
from agno.tools.apify import ApifyTools

