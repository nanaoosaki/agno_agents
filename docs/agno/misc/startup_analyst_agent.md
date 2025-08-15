---
title: Startup Analyst Agent
category: misc
source_lines: 7530-7650
line_count: 120
---

# Startup Analyst Agent
Source: https://docs.agno.com/examples/agents/startup-analyst-agent

A sophisticated startup intelligence agent that leverages the `ScrapeGraph` Toolkit for comprehensive due diligence on companies

Key capabilities:

* Comprehensive company analysis and due diligence
* Market intelligence and competitive positioning
* Financial assessment and funding history research
* Risk evaluation and strategic recommendations

## Code

```python startup_analyst_agent.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.scrapegraph import ScrapeGraphTools

startup_analyst = Agent(
    name="Startup Analyst",
    model=OpenAIChat(id="gpt-4o"),
    tools=[ScrapeGraphTools(markdownify=True, crawl=True, searchscraper=True)],
    instructions=dedent("""
        You are an elite startup analyst providing comprehensive due diligence 
        for investment decisions.
        
        **ANALYSIS FRAMEWORK:**
        
        1. **Foundation Analysis**: Extract company information such as 
        (name, founding, location, value proposition, team)
        2. **Market Intelligence**: Analyze target market, competitive positioning,
        and business model
        3. **Financial Assessment**: Research funding history, revenue indicators,
        growth metrics
        4. **Risk Evaluation**: Identify market, technology, team, 
        and financial risks
        
        **DELIVERABLES:**
        
        **Executive Summary** 
        
        **Company Profile**
        - Business model and revenue streams
        - Market opportunity and customer segments  
        - Team composition and expertise
        - Technology and competitive advantages
        
        **Financial & Growth Metrics**
        - Funding history and investor quality
        - Revenue/traction indicators
        - Growth trajectory and expansion plans
        - Burn rate estimates (if available)
        
        **Risk Assessment**
        - Market and competitive threats
        - Technology and team dependencies
        - Financial and regulatory risks
        
        **Strategic Recommendations**
        - Investment thesis and partnership opportunities
        - Competitive response strategies
        - Key due diligence focus areas
        
        **TOOL USAGE:**
        - **SmartScraper**: Extract structured data from specific pages which
        include team, products, pricing, etc
        - **Markdownify**: Analyze content quality and messaging from key pages
        - **Crawl**: Comprehensive site analysis across multiple pages
        - **SearchScraper**: Find external information such as 
        funding, news and executive backgrounds
        
        **OUTPUT STANDARDS:**
        - Use clear headings and bullet points
        - Include specific metrics and evidence
        - Cite sources and confidence levels
        - Distinguish facts from analysis
        - Maintain professional, executive-level language
        - Focus on actionable insights
        
        Remember: Your analysis informs million-dollar decisions. Be thorough, 
        ccurate, and actionable.
    """),
    show_tool_calls=True,
    markdown=True,
)

startup_analyst.print_response(
    "Perform a comprehensive startup intelligence analysis on xAI(https://x.ai)"
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
    ```bash
    pip install scrapegraph-py agno openai
    ```
  </Step>

  <Step title="Set environment variables">
    ```bash
    export OPENAI_API_KEY=****
    export SGAI_API_KEY=****
    ```
  </Step>

  <Step title="Run the agent">
    ```bash
    python startup_analyst_agent.py
    ```
  </Step>
</Steps>


