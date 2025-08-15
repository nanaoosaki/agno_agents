---
title: Stagehand MCP agent
category: misc
source_lines: 27381-27406
line_count: 25
---

# Stagehand MCP agent
Source: https://docs.agno.com/examples/concepts/tools/mcp/stagehand

A web scraping agent that uses the Stagehand MCP server to automate browser interactions and create a structured content digest from Hacker News.

## Key Features

* **Safe Navigation**: Proper initialization sequence prevents common browser automation errors
* **Structured Data Extraction**: Methodical approach to extracting and organizing web content
* **Flexible Output**: Creates well-structured digests with headlines, summaries, and insights

## Prerequisites

Before running this example, you'll need:

* **Browserbase Account**: Get API credentials from [Browserbase](https://browserbase.com)
* **OpenAI API Key**: Get an API Key from [OpenAI](https://platform.openai.com/settings/organization/api-keys)

## Setup Instructions

### 1. Clone and Build Stagehand MCP Server

```bash
git clone https://github.com/browserbase/mcp-server-browserbase

