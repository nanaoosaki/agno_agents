---
title: Custom API
category: misc
source_lines: 75123-75184
line_count: 61
---

# Custom API
Source: https://docs.agno.com/tools/toolkits/others/custom_api



**CustomApiTools** enable an Agent to make HTTP requests to any external API with customizable authentication and parameters.

## Prerequisites

The following example requires the `requests` library.

```shell
pip install requests
```

## Example

The following agent will use CustomApiTools to make API calls to the Dog CEO API.

```python cookbook/tools/custom_api_tools.py
from agno.agent import Agent
from agno.tools.api import CustomApiTools

agent = Agent(
    tools=[CustomApiTools(base_url="https://dog.ceo/api")],
    markdown=True,
)

agent.print_response(
    'Make API calls to the following two different endpoints: /breeds/image/random and /breeds/list/all to get a random dog image and list of dog breeds respectively. Use GET method for both calls.'
)
```

## Toolkit Params

| Parameter      | Type             | Default | Description                                    |
| -------------- | ---------------- | ------- | ---------------------------------------------- |
| `base_url`     | `str`            | `None`  | Base URL for API calls                         |
| `username`     | `str`            | `None`  | Username for basic authentication              |
| `password`     | `str`            | `None`  | Password for basic authentication              |
| `api_key`      | `str`            | `None`  | API key for bearer token authentication        |
| `headers`      | `Dict[str, str]` | `{}`    | Default headers to include in requests         |
| `verify_ssl`   | `bool`           | `True`  | Whether to verify SSL certificates             |
| `timeout`      | `int`            | `30`    | Request timeout in seconds                     |
| `make_request` | `bool`           | `True`  | Whether to register the make\_request function |

## Toolkit Functions

| Function       | Description                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `make_request` | Makes an HTTP request to the API. Takes method (GET, POST, etc.), endpoint, and optional params, data, headers, and json\_data parameters. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/api.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/custom_api_tools.py)

```
```


