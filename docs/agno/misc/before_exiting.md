---
title: Before exiting
category: misc
source_lines: 72091-72115
line_count: 24
---

# Before exiting
await mcp_tools.close()
```

3. **Clear Instructions**: Provide clear and specific instructions to your agent:

```python
instructions = """
You are a filesystem assistant. Help users explore files and directories.
- Navigate the filesystem to answer questions
- Use the list_allowed_directories tool to find accessible directories
- Provide clear context about files you examine
- Be concise and focus on relevant information
"""
```

## More Information

* Find examples of Agents that use MCP [here](https://docs.agno.com/examples/concepts/tools/mcp/airbnb).
* Find a collection of MCP servers [here](https://github.com/modelcontextprotocol/servers).
* Read the [MCP documentation](https://modelcontextprotocol.io/introduction) to learn more about the Model Context Protocol.
* Checkout the Agno [Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook/tools/mcp) for more examples of Agents that use MCP.


