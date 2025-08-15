---
title: Authenticate with Agno Platform
category: misc
source_lines: 59407-59445
line_count: 38
---

# Authenticate with Agno Platform
Source: https://docs.agno.com/how-to/authentication

Set up authentication to start monitoring, tracking performance metrics, and managing your Agno workspace.

There are two ways to authenticate with Agno:

1. Using the CLI setup command (`ag setup`)
2. Setting the API key manually in your environment

### Method 1: CLI Authentication

The fastest way to authenticate is using the Agno CLI:

```bash
ag setup
```

This command will open your browser to authenticate with Agno Platform & automatically configure your workspace

### Method 2: Manual API Key Setup

Alternatively, you can manually set up your API key:

1. Get your API key from [app.agno.com/settings](https://app.agno.com/settings)
2. Set the API key in your environment

<CodeGroup>
  ```bash Mac
  export AGNO_API_KEY=ag-***
  ```

  ```bash Windows
  setx AGNO_API_KEY ag-***
  ```
</CodeGroup>


