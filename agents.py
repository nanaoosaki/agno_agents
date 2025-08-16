# agents.py
# Following docs/agno/core/running_your_agent.md and docs/agno/misc/basic_agents.md
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv

# Agno imports
try:
    from agno.agent import Agent, RunResponse
    from agno.models.openai import OpenAIChat
    from agno.tools.duckduckgo import DuckDuckGoTools
    from agno.tools.website import WebsiteTools
except ImportError as e:
    print(f"Warning: Agno imports failed: {e}")
    # Fallback for development/testing
    Agent = object
    RunResponse = object
    OpenAIChat = object
    DuckDuckGoTools = object
    WebsiteTools = object

load_dotenv()

@dataclass
class ChatResult:
    text: str
    meta: Optional[Dict[str, Any]] = None

# --- Example 1: Echo Agent (no external calls, for testing) ---
class EchoAgent:
    name = "EchoAgent"
    description = "Simple echo agent for testing - repeats your input"

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        suffix = ""
        if files:
            suffix = f"\n\n📁 **Files received:** {len(files)} file(s)"
            for file in files[:3]:  # Show first 3 files
                suffix += f"\n  - {os.path.basename(file)}"
            if len(files) > 3:
                suffix += f"\n  - ... and {len(files) - 3} more"
        
        response_text = f"🔄 **Echo:** {prompt}{suffix}"
        return ChatResult(text=response_text)

# --- Example 2: Research Agent with Agno integration ---
class ResearchAgent:
    name = "ResearchAgent"
    description = "AI research agent powered by Agno with web search capabilities"

    def __init__(self):
        try:
            # Following docs/agno/misc/basic_agents.md pattern
            self.agent = Agent(
                name="Research Assistant",
                model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),  # Using correct model ID from workspace rules
                instructions="""You are a helpful research assistant. When asked questions:
1. Search for current information using available tools
2. Provide comprehensive, well-structured answers
3. Include sources and references when possible
4. If files are attached, analyze them in context of the question""",
                tools=[DuckDuckGoTools(), WebsiteTools()],
                add_history_to_messages=True,
                markdown=True,
                stream=True
            )
        except Exception as e:
            print(f"Warning: Could not initialize ResearchAgent: {e}")
            self.agent = None

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        if not self.agent:
            return ChatResult(
                text="❌ ResearchAgent is not available. Please check your Agno installation and API keys.",
                meta={"error": "agent_not_initialized"}
            )

        try:
            # Add file context to prompt if files are provided
            enhanced_prompt = prompt
            if files:
                file_info = f"\n\nAttached files: {', '.join([os.path.basename(f) for f in files])}"
                enhanced_prompt = f"{prompt}{file_info}"

            # Following docs/agno/core/running_your_agent.md
            response = self.agent.run(enhanced_prompt)
            
            # Extract text content from RunResponse
            response_text = getattr(response, 'content', str(response))
            
            return ChatResult(
                text=response_text,
                meta={
                    "model": getattr(response, 'model', None),
                    "metrics": getattr(response, 'metrics', None)
                }
            )
        except Exception as e:
            return ChatResult(
                text=f"❌ Error running research agent: {str(e)}",
                meta={"error": str(e)}
            )

# --- Example 3: General Purpose Agent ---
class GeneralAgent:
    name = "GeneralAgent"
    description = "General purpose AI assistant for various tasks"

    def __init__(self):
        try:
            self.agent = Agent(
                name="General Assistant",
                model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
                instructions="""You are a helpful AI assistant. You can:
- Answer questions on various topics
- Help with analysis and problem-solving
- Process and analyze attached files
- Provide explanations and tutorials
- Assist with creative tasks

Always be helpful, accurate, and provide well-structured responses.""",
                add_history_to_messages=True,
                markdown=True,
            )
        except Exception as e:
            print(f"Warning: Could not initialize GeneralAgent: {e}")
            self.agent = None

    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        if not self.agent:
            return ChatResult(
                text="❌ GeneralAgent is not available. Please check your Agno installation and API keys.",
                meta={"error": "agent_not_initialized"}
            )

        try:
            enhanced_prompt = prompt
            if files:
                file_info = f"\n\nNote: User has attached {len(files)} file(s): {', '.join([os.path.basename(f) for f in files])}"
                enhanced_prompt = f"{prompt}{file_info}"

            response = self.agent.run(enhanced_prompt)
            response_text = getattr(response, 'content', str(response))
            
            return ChatResult(
                text=response_text,
                meta={
                    "model": getattr(response, 'model', None),
                    "metrics": getattr(response, 'metrics', None)
                }
            )
        except Exception as e:
            return ChatResult(
                text=f"❌ Error running general agent: {str(e)}",
                meta={"error": str(e)}
            )

# Health Logger v3 import
try:
    from healthlogger.workflow import HealthLoggerWorkflowWrapper
    health_logger_v3 = HealthLoggerWorkflowWrapper()
except ImportError as e:
    print(f"Warning: Health Logger v3 not available: {e}")
    health_logger_v3 = None

# Recall Agent import - Following docs/agno/tools/writing_your_own_tools.md
try:
    from healthlogger.recall.agent import recall_agent
    
    class RecallAgentWrapper:
        name = "Recall Agent"
        description = "Analyzes historical health data patterns and correlations using intelligent querying"
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            """Run the Recall Agent with the user's query"""
            try:
                response = recall_agent.run(prompt)
                return ChatResult(
                    text=response.content,
                    meta={
                        "agent": "RecallAgent",
                        "model": "gpt-4o-mini-2024-07-18",
                        "tool_calls": getattr(response, 'tool_calls', None),
                        "metrics": getattr(response, 'metrics', None)
                    }
                )
            except Exception as e:
                return ChatResult(
                    text=f"❌ Error running recall agent: {str(e)}",
                    meta={"error": str(e), "agent": "RecallAgent"}
                )
    
    recall_agent_wrapper = RecallAgentWrapper()
except ImportError as e:
    print(f"Warning: Recall Agent not available: {e}")
    recall_agent_wrapper = None

# Registry of available agents
AGENTS: Dict[str, Any] = {
    "EchoAgent": EchoAgent(),
    "ResearchAgent": ResearchAgent(),
    "GeneralAgent": GeneralAgent(),
}

# Add Health Logger v3 if available
if health_logger_v3:
    AGENTS["Health Logger (v3)"] = health_logger_v3

# Add Recall Agent if available
if recall_agent_wrapper:
    AGENTS["Recall Agent"] = recall_agent_wrapper

def call_agent(agent_name: str, user_text: str, filepaths: Optional[List[str]] = None) -> ChatResult:
    """
    Call the specified agent with user input and optional file attachments.
    
    Args:
        agent_name: Name of the agent to use
        user_text: User's text input
        filepaths: List of file paths (optional)
    
    Returns:
        ChatResult with the agent's response
    """
    agent = AGENTS.get(agent_name)
    if not agent:
        return ChatResult(
            text=f"❌ Unknown agent: {agent_name}. Available agents: {', '.join(AGENTS.keys())}",
            meta={"error": "unknown_agent"}
        )
    
    try:
        return agent.run(user_text, files=filepaths)
    except Exception as e:
        return ChatResult(
            text=f"❌ Error calling agent {agent_name}: {str(e)}",
            meta={"error": str(e), "agent": agent_name}
        )

def get_agent_info() -> Dict[str, str]:
    """Get information about all available agents."""
    return {name: getattr(agent, 'description', 'No description available') 
            for name, agent in AGENTS.items()}