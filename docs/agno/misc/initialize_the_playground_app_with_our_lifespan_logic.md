---
title: Initialize the Playground app with our lifespan logic
category: misc
source_lines: 72076-72091
line_count: 15
---

# Initialize the Playground app with our lifespan logic
app = playground.get_app(lifespan=lifespan)


if __name__ == "__main__":
    playground.serve(app="mcp_demo:app", reload=True)
```

## Best Practices

1. **Error Handling**: Always include proper error handling for MCP server connections and operations.

2. **Resource Cleanup**: Remember to close the connection to the MCP server when using `MCPTools` or `MultiMCPTools`:

```python
