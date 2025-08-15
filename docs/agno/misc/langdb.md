---
title: LangDB
category: misc
source_lines: 65932-65981
line_count: 49
---

# LangDB
Source: https://docs.agno.com/observability/langdb

Integrate Agno with LangDB to trace agent execution, tool calls, and gain comprehensive observability into your agent's performance.

## Integrating Agno with LangDB

[LangDB](https://langdb.ai/) provides an AI Gateway platform for comprehensive observability and tracing of AI agents and LLM interactions. By integrating Agno with LangDB, you can gain full visibility into your agent's operations, including agent runs, tool calls, team interactions, and performance metrics.

For detailed integration instructions, see the [LangDB Agno documentation](https://docs.langdb.ai/getting-started/working-with-agent-frameworks/working-with-agno).

<Frame caption="LangDB Finance Team Trace">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/langdb-finance-trace.png" style={{ borderRadius: '10px', width: '100%', maxWidth: '800px' }} alt="langdb-agno finance team observability" />
</Frame>

## Prerequisites

1. **Install Dependencies**

   Ensure you have the necessary packages installed:

   ```bash
   pip install agno 'pylangdb[agno]'
   ```

2. **Setup LangDB Account**

   * Sign up for an account at [LangDB](https://app.langdb.ai/signup)
   * Create a new project in the LangDB dashboard
   * Obtain your API key and Project ID from the project settings

3. **Set Environment Variables**

   Configure your environment with the LangDB credentials:

   ```bash
   export LANGDB_API_KEY="<your_langdb_api_key>"
   export LANGDB_PROJECT_ID="<your_langdb_project_id>"
   ```

## Sending Traces to LangDB

### Example: Basic Agent Setup

This example demonstrates how to instrument your Agno agent with LangDB tracing.

```python
from pylangdb.agno import init

