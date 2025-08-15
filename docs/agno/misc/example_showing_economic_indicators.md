---
title: Example showing economic indicators
category: misc
source_lines: 76594-76624
line_count: 30
---

# Example showing economic indicators
agent.print_response(
    "Show me the latest GDP growth rate and inflation numbers for the US"
)
```

## Toolkit Params

| Parameter         | Type   | Default | Description                                                                        |
| ----------------- | ------ | ------- | ---------------------------------------------------------------------------------- |
| `read_article`    | `bool` | `True`  | Enables the functionality to read the full content of an article.                  |
| `include_summary` | `bool` | `False` | Specifies whether to include a summary of the article along with the full content. |
| `article_length`  | `int`  | -       | The maximum length of the article or its summary to be processed or returned.      |

## Toolkit Functions

| Function                | Description                                                                       |
| ----------------------- | --------------------------------------------------------------------------------- |
| `get_stock_price`       | This function gets the current stock price for a stock symbol or list of symbols. |
| `search_company_symbol` | This function searches for the stock symbol of a company.                         |
| `get_price_targets`     | This function gets the price targets for a stock symbol or list of symbols.       |
| `get_company_news`      | This function gets the latest news for a stock symbol or list of symbols.         |
| `get_company_profile`   | This function gets the company profile for a stock symbol or list of symbols.     |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/openbb.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/openbb_tools.py)


