---
title: Execute team workflow
category: misc
source_lines: 66044-66079
line_count: 35
---

# Execute team workflow
reasoning_team.print_response("Analyze Apple (AAPL) investment potential")
```

## Sample Trace

View a complete example trace in the LangDB dashboard: [Finance Reasoning Team Trace](https://app.langdb.ai/sharing/threads/73c91c58-eab7-4c6b-afe1-5ab6324f1ada)

<Frame caption="LangDB Finance Team Thread">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/langdb-finance-thread.png" style={{ borderRadius: '10px', width: '100%', maxWidth: '800px' }} alt="langdb-agno finance team observability" />
</Frame>

## Advanced Features

### LangDB Capabilities

* **Virtual Models**: Save, share, and reuse model configurations—combining prompts, parameters, tools, and routing logic into a single named unit for consistent behavior across apps
* **MCP Support**: Enhanced tool capabilities through Model Context Protocol servers
* **Multi-Provider**: Support for OpenAI, Anthropic, Google, xAI, and other providers

## Notes

* **Initialization Order**: Always call `init()` before creating any Agno agents or teams
* **Environment Variables**: With `LANGDB_API_KEY` and `LANGDB_PROJECT_ID` set, you can create models with just `LangDB(id="model_name")`

## Resources

* [LangDB Documentation](https://docs.langdb.ai/)
* [Building a Reasoning Finance Team Guide](https://docs.langdb.ai/guides/building-agents/building-a-reasoning-finance-team-with-agno)
* [LangDB GitHub Samples](https://github.com/langdb/langdb-samples/tree/main/examples/agno)
* [LangDB Dashboard](https://app.langdb.ai/)

By following these steps, you can effectively integrate Agno with LangDB, enabling comprehensive observability and monitoring of your AI agents.


