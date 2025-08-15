---
title: --- Execution function ---
category: misc
source_lines: 58202-58408
line_count: 206
---

# --- Execution function ---
async def startup_validation_execution(
    workflow: Workflow,
    execution_input: WorkflowExecutionInput,
    startup_idea: str,
    **kwargs: Any,
) -> str:
    """Execute the complete startup idea validation workflow"""

    # Get inputs
    message: str = execution_input.message
    idea: str = startup_idea

    if not idea:
        return "❌ No startup idea provided"

    print(f"🚀 Starting startup idea validation for: {idea}")
    print(f"💡 Validation request: {message}")

    # Phase 1: Idea Clarification
    print(f"\n🎯 PHASE 1: IDEA CLARIFICATION & REFINEMENT")
    print("=" * 60)

    clarification_prompt = f"""
    {message}
    
    Please analyze and refine the following startup idea:
    
    STARTUP IDEA: {idea}
    
    Evaluate:
    1. The originality of this idea compared to existing solutions
    2. Define a clear mission statement for this startup
    3. Outline specific, measurable objectives
    
    Provide insights on how to strengthen and focus the core concept.
    """

    print(f"🔍 Analyzing and refining the startup concept...")

    try:
        clarification_result = await idea_clarifier_agent.arun(clarification_prompt)
        idea_clarification = clarification_result.content

        print(f"✅ Idea clarification completed")
        print(f"📝 Mission: {idea_clarification.mission[:100]}...")

    except Exception as e:
        return f"❌ Failed to clarify idea: {str(e)}"

    # Phase 2: Market Research
    print(f"\n📊 PHASE 2: MARKET RESEARCH & ANALYSIS")
    print("=" * 60)

    market_research_prompt = f"""
    Based on the refined startup idea and clarification below, conduct comprehensive market research:
    
    STARTUP IDEA: {idea}
    ORIGINALITY: {idea_clarification.originality}
    MISSION: {idea_clarification.mission}
    OBJECTIVES: {idea_clarification.objectives}
    
    Please research and provide:
    1. Total Addressable Market (TAM) - overall market size
    2. Serviceable Available Market (SAM) - portion you could serve
    3. Serviceable Obtainable Market (SOM) - realistic market share
    4. Target customer segments with detailed characteristics
    
    Use web search to find current market data and trends.
    """

    print(f"📈 Researching market size and customer segments...")

    try:
        market_result = await market_research_agent.arun(market_research_prompt)
        market_research = market_result.content

        print(f"✅ Market research completed")
        print(f"🎯 TAM: {market_research.total_addressable_market[:100]}...")

    except Exception as e:
        return f"❌ Failed to complete market research: {str(e)}"

    # Phase 3: Competitor Analysis
    print(f"\n🏢 PHASE 3: COMPETITIVE LANDSCAPE ANALYSIS")
    print("=" * 60)

    competitor_prompt = f"""
    Based on the startup idea and market research below, analyze the competitive landscape:
    
    STARTUP IDEA: {idea}
    TAM: {market_research.total_addressable_market}
    SAM: {market_research.serviceable_available_market}
    SOM: {market_research.serviceable_obtainable_market}
    TARGET SEGMENTS: {market_research.target_customer_segments}
    
    Please research and provide:
    1. Identify direct and indirect competitors
    2. SWOT analysis for each major competitor
    3. Assessment of startup's potential competitive positioning
    4. Market gaps and opportunities
    
    Use web search to find current competitor information.
    """

    print(f"🔎 Analyzing competitive landscape...")

    try:
        competitor_result = await competitor_analysis_agent.arun(competitor_prompt)
        competitor_analysis = competitor_result.content

        print(f"✅ Competitor analysis completed")
        print(f"🏆 Positioning: {competitor_analysis.positioning[:100]}...")

    except Exception as e:
        return f"❌ Failed to complete competitor analysis: {str(e)}"

    # Phase 4: Final Validation Report
    print(f"\n📋 PHASE 4: COMPREHENSIVE VALIDATION REPORT")
    print("=" * 60)

    report_prompt = f"""
    Synthesize all the research and analysis into a comprehensive startup validation report:
    
    STARTUP IDEA: {idea}
    
    IDEA CLARIFICATION:
    - Originality: {idea_clarification.originality}
    - Mission: {idea_clarification.mission}
    - Objectives: {idea_clarification.objectives}
    
    MARKET RESEARCH:
    - TAM: {market_research.total_addressable_market}
    - SAM: {market_research.serviceable_available_market}
    - SOM: {market_research.serviceable_obtainable_market}
    - Target Segments: {market_research.target_customer_segments}
    
    COMPETITOR ANALYSIS:
    - Competitors: {competitor_analysis.competitors}
    - SWOT: {competitor_analysis.swot_analysis}
    - Positioning: {competitor_analysis.positioning}
    
    Create a professional validation report with:
    1. Executive summary
    2. Idea assessment (strengths/weaknesses)
    3. Market opportunity analysis
    4. Competitive landscape overview
    5. Strategic recommendations
    6. Specific next steps for the entrepreneur
    """

    print(f"📝 Generating comprehensive validation report...")

    try:
        final_result = await report_agent.arun(report_prompt)
        validation_report = final_result.content

        print(f"✅ Validation report completed")

    except Exception as e:
        return f"❌ Failed to generate final report: {str(e)}"

    # Final summary
    summary = f"""
    🎉 STARTUP IDEA VALIDATION COMPLETED!
    
    📊 Validation Summary:
    • Startup Idea: {idea}
    • Idea Clarification: ✅ Completed
    • Market Research: ✅ Completed
    • Competitor Analysis: ✅ Completed
    • Final Report: ✅ Generated
    
    📈 Key Market Insights:
    • TAM: {market_research.total_addressable_market[:150]}...
    • Target Segments: {market_research.target_customer_segments[:150]}...
    
    🏆 Competitive Positioning:
    {competitor_analysis.positioning[:200]}...
    
    📋 COMPREHENSIVE VALIDATION REPORT:
    
    ## Executive Summary
    {validation_report.executive_summary}
    
    ## Idea Assessment
    {validation_report.idea_assessment}
    
    ## Market Opportunity
    {validation_report.market_opportunity}
    
    ## Competitive Landscape
    {validation_report.competitive_landscape}
    
    ## Strategic Recommendations
    {validation_report.recommendations}
    
    ## Next Steps
    {validation_report.next_steps}
    
    ⚠️ Disclaimer: This validation is for informational purposes only. Conduct additional due diligence before making investment decisions.
    """

    return summary


