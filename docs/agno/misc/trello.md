---
title: Trello
category: misc
source_lines: 76908-77005
line_count: 97
---

# Trello
Source: https://docs.agno.com/tools/toolkits/others/trello

Agno TrelloTools helps to integrate Trello functionalities into your agents, enabling management of boards, lists, and cards.

## Prerequisites

The following examples require the `trello` library and Trello API credentials which can be obtained by following Trello's developer documentation.

```shell
pip install -U trello
```

Set the following environment variables:

```shell
export TRELLO_API_KEY="YOUR_API_KEY"
export TRELLO_API_SECRET="YOUR_API_SECRET"
export TRELLO_TOKEN="YOUR_TOKEN"
```

## Example

The following agent will create a board called `ai-agent` and inside it create list called `todo` and `doing` and inside each of them create card called `create agent`.

```python
from agno.agent import Agent
from agno.tools.trello import TrelloTools

agent = Agent(
    instructions=[
        "You are a Trello management assistant that helps organize and manage Trello boards, lists, and cards",
        "Help users with tasks like:",
        "- Creating and organizing boards, lists, and cards",
        "- Moving cards between lists",
        "- Retrieving board and list information",
        "- Managing card details and descriptions",
        "Always confirm successful operations and provide relevant board/list/card IDs and URLs",
        "When errors occur, provide clear explanations and suggest solutions",
    ],
    tools=[TrelloTools()],
    show_tool_calls=True,
)

agent.print_response(
    "Create a board called ai-agent and inside it create list called 'todo' and 'doing' and inside each of them create card called 'create agent'",
    stream=True,
)

```

## Toolkit Functions

| Function          | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `create_card`     | Creates a new card in a specified board and list.             |
| `get_board_lists` | Retrieves all lists on a specified Trello board.              |
| `move_card`       | Moves a card to a different list.                             |
| `get_cards`       | Retrieves all cards from a specified list.                    |
| `create_board`    | Creates a new Trello board.                                   |
| `create_list`     | Creates a new list on a specified board.                      |
| `list_boards`     | Lists all Trello boards accessible by the authenticated user. |

## Toolkit Parameters

These parameters are passed to the `TrelloTools` constructor.

| Parameter         | Type            | Default | Description                                                              |
| ----------------- | --------------- | ------- | ------------------------------------------------------------------------ |
| `api_key`         | `Optional[str]` | `None`  | Trello API key. Defaults to `TRELLO_API_KEY` environment variable.       |
| `api_secret`      | `Optional[str]` | `None`  | Trello API secret. Defaults to `TRELLO_API_SECRET` environment variable. |
| `token`           | `Optional[str]` | `None`  | Trello token. Defaults to `TRELLO_TOKEN` environment variable.           |
| `create_card`     | `bool`          | `True`  | Enable the `create_card` tool.                                           |
| `get_board_lists` | `bool`          | `True`  | Enable the `get_board_lists` tool.                                       |
| `move_card`       | `bool`          | `True`  | Enable the `move_card` tool.                                             |
| `get_cards`       | `bool`          | `True`  | Enable the `get_cards` tool.                                             |
| `create_board`    | `bool`          | `True`  | Enable the `create_board` tool.                                          |
| `create_list`     | `bool`          | `True`  | Enable the `create_list` tool.                                           |
| `list_boards`     | `bool`          | `True`  | Enable the `list_boards` tool.                                           |

### Board Filter Options for `list_boards`

The `list_boards` function accepts a `board_filter` argument with the following options:

* `all` (default)
* `open`
* `closed`
* `organization`
* `public`
* `starred`

## Developer Resources

* View [Tools Source](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/trello.py)
* View [Cookbook Example](https://github.com/agno-agi/agno/blob/main/cookbook/tools/trello_tools.py)


