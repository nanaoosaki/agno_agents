---
title: Create team with structured output
category: misc
source_lines: 70790-70852
line_count: 62
---

# Create team with structured output
stock_research_team = Team(
    name="Stock Research Team",
    mode="coordinate",
    model=OpenAIChat("gpt-4o"),
    members=[stock_searcher, company_info_agent],
    response_model=StockReport,
    markdown=True,
    show_members_responses=True,
)

stock_research_team.print_response("Give me a comprehensive stock report for NVDA")
```

The team will coordinate between its members and produce a structured `StockReport` object:

```python
StockReport(
│   symbol='NVDA',
│   company_name='NVIDIA Corporation',
│   current_price='$875.42',
│   analysis='NVIDIA continues to dominate the AI chip market with strong demand for its H100 and upcoming H200 GPUs. The company has shown exceptional growth in data center revenue, driven by enterprise AI adoption and cloud provider expansion. Recent partnerships with major tech companies strengthen its market position, though competition from AMD and Intel is intensifying.',
│   recommendation='Buy'
)
```

## Using a Parser Model

You can use an additional model to parse and structure the output from your primary model. This approach is particularly effective when the primary model is optimized for reasoning tasks, as such models may not consistently produce detailed structured responses.

```python
team = Team(
    name="Stock Research Team",
    mode="coordinate",
    model=Claude(id="claude-sonnet-4-20250514"),
    members=[stock_searcher, company_info_agent],
    response_model=StockReport,
    parser_model=OpenAIChat(id="gpt-4o"),
)
```

You can also provide a custom `parser_model_prompt` to your Parser Model.

## Streaming Structured Output

Teams support streaming with structured output, where the `content` event contains the complete structured result as a single event.

```python streaming_team.py
from typing import List
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools

class MarketAnalysis(BaseModel):
    sector: str = Field(..., description="Market sector being analyzed")
    key_trends: List[str] = Field(..., description="Major trends affecting the sector")
    top_performers: List[str] = Field(..., description="Best performing stocks in the sector")
    market_outlook: str = Field(..., description="Overall market outlook and predictions")
    risk_factors: List[str] = Field(..., description="Key risks to consider")

