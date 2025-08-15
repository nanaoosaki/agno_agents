---
title: Confluence
category: misc
source_lines: 75055-75074
line_count: 19
---

# Confluence
Source: https://docs.agno.com/tools/toolkits/others/confluence



**ConfluenceTools** enable an Agent to retrieve, create, and update pages in Confluence. They also allow you to explore spaces and page details.

## Prerequisites

The following example requires the `atlassian-python-api` library and Confluence credentials. You can obtain an API token by going [here](https://id.atlassian.com/manage-profile/security).

```shell
pip install atlassian-python-api
```

```shell
export CONFLUENCE_URL="https://your-confluence-instance"
export CONFLUENCE_USERNAME="your-username"
export CONFLUENCE_PASSWORD="your-password"
