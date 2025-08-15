---
title: Get the most recent income statement for Apple
category: misc
source_lines: 75675-75724
line_count: 49
---

# Get the most recent income statement for Apple
agent.print_response("Get the most recent income statement for AAPL and highlight key metrics")
```

For more examples, see the [Financial Datasets Examples](/examples/concepts/tools/others/financial_datasets).

## Toolkit Params

| Parameter                     | Type            | Default | Description                                                                                |
| ----------------------------- | --------------- | ------- | ------------------------------------------------------------------------------------------ |
| `api_key`                     | `Optional[str]` | `None`  | Optional API key. If not provided, uses FINANCIAL\_DATASETS\_API\_KEY environment variable |
| `enable_financial_statements` | `bool`          | `True`  | Enable financial statement related functions (income statements, balance sheets, etc.)     |
| `enable_company_info`         | `bool`          | `True`  | Enable company information related functions                                               |
| `enable_market_data`          | `bool`          | `True`  | Enable market data related functions (stock prices, earnings, metrics)                     |
| `enable_ownership_data`       | `bool`          | `True`  | Enable ownership data related functions (insider trades, institutional ownership)          |
| `enable_news`                 | `bool`          | `True`  | Enable news related functions                                                              |
| `enable_sec_filings`          | `bool`          | `True`  | Enable SEC filings related functions                                                       |
| `enable_crypto`               | `bool`          | `True`  | Enable cryptocurrency related functions                                                    |
| `enable_search`               | `bool`          | `True`  | Enable search related functions                                                            |

## Toolkit Functions

| Function                                                                         | Description                                                                                                     |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `get_income_statements(ticker: str, period: str = "annual", limit: int = 10)`    | Get income statements for a company with options for annual, quarterly, or trailing twelve months (ttm) periods |
| `get_balance_sheets(ticker: str, period: str = "annual", limit: int = 10)`       | Get balance sheets for a company with period options                                                            |
| `get_cash_flow_statements(ticker: str, period: str = "annual", limit: int = 10)` | Get cash flow statements for a company                                                                          |
| `get_company_info(ticker: str)`                                                  | Get company information including business description, sector, and industry                                    |
| `get_crypto_prices(symbol: str, interval: str = "1d", limit: int = 100)`         | Get cryptocurrency prices with configurable time intervals                                                      |
| `get_earnings(ticker: str, limit: int = 10)`                                     | Get earnings reports with EPS estimates, actuals, and revenue data                                              |
| `get_financial_metrics(ticker: str)`                                             | Get key financial metrics and ratios for a company                                                              |
| `get_insider_trades(ticker: str, limit: int = 50)`                               | Get data on insider buying and selling activity                                                                 |
| `get_institutional_ownership(ticker: str)`                                       | Get information about institutional investors and their positions                                               |
| `get_news(ticker: Optional[str] = None, limit: int = 50)`                        | Get market news, optionally filtered by company                                                                 |
| `get_stock_prices(ticker: str, interval: str = "1d", limit: int = 100)`          | Get historical stock prices with configurable time intervals                                                    |
| `search_tickers(query: str, limit: int = 10)`                                    | Search for stock tickers based on a query string                                                                |
| `get_sec_filings(ticker: str, form_type: Optional[str] = None, limit: int = 50)` | Get SEC filings with optional filtering by form type (10-K, 10-Q, etc.)                                         |
| `get_segmented_financials(ticker: str, period: str = "annual", limit: int = 10)` | Get segmented financial data by product category and geographic region                                          |

## Rate Limits and Usage

The Financial Datasets API may have usage limits based on your subscription tier. Please refer to their documentation for specific rate limit information.

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/financial_datasets.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/financial_datasets_tools.py)


