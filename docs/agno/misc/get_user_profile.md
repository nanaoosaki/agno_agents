---
title: Get user profile
category: misc
source_lines: 78650-78686
line_count: 36
---

# Get user profile
agent.print_response("Get my X profile", markdown=True)
```

<Note> Check out the [Tweet Analysis Agent](/examples/agents/tweet-analysis-agent) for a more advanced example. </Note>

## Toolkit Params

| Parameter              | Type   | Default | Description                                                    |
| ---------------------- | ------ | ------- | -------------------------------------------------------------- |
| `bearer_token`         | `str`  | `None`  | Bearer token for authentication                                |
| `consumer_key`         | `str`  | `None`  | Consumer key for authentication                                |
| `consumer_secret`      | `str`  | `None`  | Consumer secret for authentication                             |
| `access_token`         | `str`  | `None`  | Access token for authentication                                |
| `access_token_secret`  | `str`  | `None`  | Access token secret for authentication                         |
| `include_post_metrics` | `bool` | `False` | Include post metrics (likes, retweets, etc.) in search results |
| `wait_on_rate_limit`   | `bool` | `False` | Retry when rate limits are reached                             |

## Toolkit Functions

| Function            | Description                                 |
| ------------------- | ------------------------------------------- |
| `create_post`       | Creates and posts a new post                |
| `reply_to_post`     | Replies to an existing post                 |
| `send_dm`           | Sends a direct message to a X user          |
| `get_user_info`     | Retrieves information about a X user        |
| `get_home_timeline` | Gets the authenticated user's home timeline |
| `search_posts`      | Searches for tweets                         |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/x.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/x_tools.py)
* View [Tweet Analysis Agent Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/social_media_agent.py)


