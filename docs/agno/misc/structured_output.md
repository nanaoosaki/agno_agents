---
title: Structured Output
category: misc
source_lines: 70727-70762
line_count: 35
---

# Structured Output
Source: https://docs.agno.com/teams/structured-output



Teams can generate structured data using Pydantic models, just like individual agents. This feature is perfect for coordinated data extraction, analysis, and report generation where multiple agents work together to produce a structured result.

## Example

Let's create a Stock Research Team that produces a structured `StockReport`.

```python stock_team.py
from typing import List
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.yfinance import YFinanceTools

class StockAnalysis(BaseModel):
    symbol: str
    company_name: str
    analysis: str

class CompanyAnalysis(BaseModel):
    company_name: str
    analysis: str

class StockReport(BaseModel):
    symbol: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    current_price: str = Field(..., description="Current stock price")
    analysis: str = Field(..., description="Comprehensive analysis combining multiple perspectives")
    recommendation: str = Field(..., description="Investment recommendation: Buy, Hold, or Sell")

