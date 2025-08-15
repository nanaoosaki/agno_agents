---
title: Zoom
category: misc
source_lines: 78686-78727
line_count: 41
---

# Zoom
Source: https://docs.agno.com/tools/toolkits/social/zoom



**Zoom** enables an Agent to interact with Zoom, allowing it to schedule meetings, manage recordings, and handle various meeting-related operations through the Zoom API. The toolkit uses Zoom's Server-to-Server OAuth authentication for secure API access.

## Prerequisites

The Zoom toolkit requires the following setup:

1. Install required dependencies:

```shell
pip install requests
```

2. Set up Server-to-Server OAuth app in Zoom Marketplace:
   * Go to [Zoom Marketplace](https://marketplace.zoom.us/)
   * Click "Develop" → "Build App"
   * Choose "Server-to-Server OAuth" app type
   * Configure the app with required scopes:
     * `/meeting:write:admin`
     * `/meeting:read:admin`
     * `/recording:read:admin`
   * Note your Account ID, Client ID, and Client Secret

3. Set up environment variables:

```shell
export ZOOM_ACCOUNT_ID=your_account_id
export ZOOM_CLIENT_ID=your_client_id
export ZOOM_CLIENT_SECRET=your_client_secret
```

## Example Usage

```python
from agno.agent import Agent
from agno.tools.zoom import ZoomTools

