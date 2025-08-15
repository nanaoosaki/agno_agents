---
title: Financial Datasets API
category: misc
source_lines: 75630-75675
line_count: 45
---

# Financial Datasets API
Source: https://docs.agno.com/tools/toolkits/others/financial_datasets



**FinancialDatasetsTools** provide a comprehensive API for retrieving and analyzing diverse financial datasets, including stock prices, financial statements, company information, SEC filings, and cryptocurrency data from multiple providers.

## Prerequisites

The toolkit requires a Financial Datasets API key that can be obtained by creating an account at [financialdatasets.ai](https://financialdatasets.ai).

```bash
pip install agno
```

Set your API key as an environment variable:

```bash
export FINANCIAL_DATASETS_API_KEY=your_api_key_here
```

## Example

Basic usage of the Financial Datasets toolkit:

```python
from agno.agent import Agent
from agno.tools.financial_datasets import FinancialDatasetsTools

agent = Agent(
    name="Financial Data Agent",
    tools=[FinancialDatasetsTools()],
    description="You are a financial data specialist that helps analyze financial information for stocks and cryptocurrencies.",
    instructions=[
        "When given a financial query:",
        "1. Use appropriate Financial Datasets methods based on the query type",
        "2. Format financial data clearly and highlight key metrics",
        "3. For financial statements, compare important metrics with previous periods when relevant",
        "4. Calculate growth rates and trends when appropriate",
        "5. Handle errors gracefully and provide meaningful feedback",
    ],
    markdown=True,
    show_tool_calls=True,
)

