---
title: This should route to the stock_searcher
category: misc
source_lines: 70333-70339
line_count: 6
---

# This should route to the stock_searcher
response = team.run("What is the current stock price of NVDA?")
assert isinstance(response.content, StockAnalysis)
```


