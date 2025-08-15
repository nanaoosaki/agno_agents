---
title: X (Twitter)
category: misc
source_lines: 78564-78609
line_count: 45
---

# X (Twitter)
Source: https://docs.agno.com/tools/toolkits/social/x



**XTools** allows an Agent to interact with X, providing functionality for posting, messaging, and searching tweets.

## Prerequisites

Install the required library:

```shell
pip install tweepy
```

<Info>Tweepy is a Python library for interacting with the X API.</Info>

## Setup

1. **Create X Developer Account**
   * Visit [developer.x.com](https://developer.x.com) and apply for developer access
   * Create a new project and app in your developer portal

2. **Generate API Credentials**
   * Navigate to your app's "Keys and tokens" section
   * Generate and copy these credentials:
     * API Key & Secret
     * Bearer Token
     * Access Token & Secret

3. **Configure Environment**
   ```shell
   export X_CONSUMER_KEY=your_api_key
   export X_CONSUMER_SECRET=your_api_secret
   export X_ACCESS_TOKEN=your_access_token
   export X_ACCESS_TOKEN_SECRET=your_access_token_secret
   export X_BEARER_TOKEN=your_bearer_token
   ```

## Example

```python cookbook/tools/x_tools.py
from agno.agent import Agent
from agno.tools.x import XTools

