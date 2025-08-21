# Agno-Chat Project Analysis

## 1. Project File Structure

Key directories and files:

```
D:\AI\AI_agents_agno/
├── app.py                          # Main Gradio application
├── agents.py                       # Agent registry and orchestration
├── requirements.txt                # Dependencies
├── healthlogger/                   # Pure Agno health logging workflow
│   ├── workflow.py                 # Main workflow orchestration
│   ├── workflow_steps.py           # Deterministic processing logic
│   ├── agents.py                   # Extractor and Reply agents
│   ├── schema_router.py            # LLM-compatible schemas
│   └── prompts.py                  # System prompts
├── health_advisor/                 # Health management layer
│   ├── recall/                     # Historical data analysis
│   │   ├── agent.py               # Recall agent implementation
│   │   └── tools.py               # Historical data tools
│   ├── coach/                      # Evidence-based guidance
│   │   ├── agent.py               # Coach agent implementation
│   │   └── tools.py               # Coaching tools
│   ├── router/                     # Intent routing
│   │   ├── agent.py               # Router agent implementation
│   │   └── schema.py              # Router decision schema
│   └── knowledge/                  # Knowledge base management
│       └── loader.py              # ChromaDB knowledge loader
├── data/                           # Data persistence layer
│   ├── json_store.py              # JSON-based storage implementation
│   ├── storage_interface.py        # Abstract storage contracts
│   ├── daily_history.py           # Daily aggregation utilities
│   ├── episodes.json              # Episode data
│   ├── observations.json          # Observation data
│   ├── events.jsonl               # Event audit trail
│   └── schemas/                    # Pydantic data models
│       └── episodes.py            # Episode-related schemas
├── core/                           # Shared business logic
│   ├── ontology.py                # Health condition normalization
│   ├── policies.py                # Application constants
│   └── timeutils.py               # Date/time utilities
└── knowledge/                      # Knowledge base content
    └── migraine_handout.md        # Medical knowledge source
```

## 2. Key File Contents

### app.py
```python
# app.py
# Gradio-based chat interface for Agno agents
# Combines features from implementation_plan_o3.md and additional_details_from_gemini2.5pro.md

import os
from typing import List, Tuple, Optional
from datetime import datetime, timedelta
from dotenv import load_dotenv
import gradio as gr
import pandas as pd
import plotly.express as px
from data.daily_history import load_history, compile_day

try:
    from apscheduler.schedulers.background import BackgroundScheduler
except ImportError:
    BackgroundScheduler = None

# OpenAI for speech-to-text transcription
try:
    from openai import OpenAI
except ImportError:
    print("Warning: OpenAI not installed. Audio transcription will be disabled.")
    OpenAI = None

from agents import call_agent, AGENTS, get_agent_info

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client for audio transcription
client = None
if OPENAI_API_KEY and OpenAI:
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        print("✅ OpenAI client initialized for audio transcription")
    except Exception as e:
        print(f"Warning: Could not initialize OpenAI client: {e}")
else:
    print("Warning: OPENAI_API_KEY not set or OpenAI not installed. Audio transcription will be disabled.")

# --- Daily history scheduler ---
if BackgroundScheduler:
    scheduler = BackgroundScheduler()
    scheduler.add_job(compile_day, "cron", hour=23, minute=59)
    scheduler.start()
    # Ensure today's history exists
    try:
        compile_day()
    except Exception as e:
        print(f"Warning: could not compile today's history: {e}")
else:
    print("Warning: APScheduler not installed; daily history compilation disabled.")

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe microphone audio using OpenAI's Whisper.
    Following the pattern from implementation_plan_o3.md
    """
    if not audio_path or not client:
        return ""
    
    try:
        # Debug: print the audio path
        print(f"🎵 Attempting to transcribe: {audio_path}")
        
        # Check if file exists and is accessible
        if not os.path.exists(audio_path):
            return "[Audio file not found]"
            
        if not os.access(audio_path, os.R_OK):
            return "[Audio file not accessible - permission denied]"
        
        with open(audio_path, "rb") as f:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",  # Using standard Whisper model
                file=f
            )
        
        result = getattr(transcript, "text", "")
        print(f"🎵 Transcription result: {result}")
        return result
        
    except PermissionError as e:
        error_msg = f"[Permission denied accessing audio file: {str(e)}]"
        print(f"Transcription permission error: {e}")
        return error_msg
    except Exception as e:
        error_msg = f"[Transcription failed: {str(e)}]"
        print(f"Transcription error: {e}")
        return error_msg

def normalize_files(files: Optional[List[gr.File]]) -> List[str]:
    """
    Convert Gradio file objects to a list of filesystem paths.
    Enhanced from both implementation plans
    """
    if not files:
        return []
    
    paths = []
    for f in files:
        # Handle different Gradio file object formats
        if hasattr(f, 'name') and f.name:
            paths.append(str(f.name))
        elif hasattr(f, 'path') and f.path:
            paths.append(str(f.path))
        elif isinstance(f, str):
            paths.append(f)
    
    return paths

def format_message_with_files(message: str, filepaths: List[str]) -> str:
    """Format user message to show attached files."""
    if not filepaths:
        return message
    
    file_info = "\n\n📎 **Attachments:**"
    for path in filepaths[:5]:  # Show first 5 files
        file_info += f"\n  • {os.path.basename(path)}"
    
    if len(filepaths) > 5:
        file_info += f"\n  • ... and {len(filepaths) - 5} more files"
    
    return f"{message}{file_info}"

def user_submit(
    message: str,
    history: List[dict],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """
    Handle text and file submissions.
    Updated for Gradio messages format (OpenAI-style dictionaries)
    """
    if not message.strip():
        return history, gr.update(value=""), gr.update(value=None)
    
    history = history or []
    filepaths = normalize_files(files)
    
    # Format user message with file information
    display_message = format_message_with_files(message, filepaths)
    
    # Add user message and thinking response using new messages format
    history.append({"role": "user", "content": display_message})
    history.append({"role": "assistant", "content": "🤔 *Thinking...*"})
    
    # Yield intermediate state to show "thinking" message
    yield history, gr.update(value=""), gr.update(value=None)
    
    # Call the agent and get response
    try:
        result = call_agent(agent_name, message, filepaths)
        
        # Update the last message with the actual response
        response_text = result.text
        
        # Add metadata if available
        if result.meta and "error" not in result.meta:
            model_info = result.meta.get("model", "")
            if model_info:
                response_text = f"{result.text}\n\n*Model: {model_info}*"
        
        history[-1] = {"role": "assistant", "content": response_text}
        
    except Exception as e:
        history[-1] = {"role": "assistant", "content": f"❌ **Error:** {str(e)}"}
    
    yield history, gr.update(value=""), gr.update(value=None)

def mic_submit(
    audio_path: str,
    history: List[dict],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """
    Handle microphone submissions by transcribing first.
    Updated for Gradio messages format
    """
    history = history or []
    
    if not audio_path:
        error_msg = "No audio file received"
        history.append({"role": "user", "content": f"🎤 {error_msg}"})
        history.append({"role": "assistant", "content": ""})
        return history, None
    
    # Transcribe audio
    transcribed_text = transcribe_audio(audio_path)
    
    if not transcribed_text:
        transcribed_text = "[Audio input was empty or could not be transcribed]"
    
    # Add microphone indicator to show this came from audio
    mic_message = f"🎤 {transcribed_text}"
    
    # Use the same submission logic as text input but only return 2 values
    for result in user_submit(mic_message, history, agent_name, files):
        # Extract only the first 2 values (history, text_input) and ignore file_input
        if isinstance(result, tuple) and len(result) >= 2:
            yield result[0], None  # Return history and clear mic_input
        else:
            yield result, None

def clear_chat():
    """Clear the chat history."""
    return [], ""

def create_calendar_view(df):
    """Create a calendar-style visualization with color-coded pain levels."""
    import plotly.graph_objects as go
    from datetime import datetime, timedelta
    import calendar
    
    # Get current month and year, or the latest data month
    if not df.empty:
        latest_date = df['date'].max()
        current_month = latest_date.month
        current_year = latest_date.year
    else:
        now = datetime.now()
        current_month = now.month
        current_year = now.year
    
    # Create a calendar grid
    cal = calendar.monthcalendar(current_year, current_month)
    
    # Pain level color mapping
    def get_pain_color(pain_level):
        if pain_level is None or pd.isna(pain_level):
            return '#f0f0f0'  # Light gray for no data
        elif pain_level <= 2:
            return '#4ade80'  # Green - Great
        elif pain_level <= 4:
            return '#fbbf24'  # Yellow/Orange - Okay
        elif pain_level <= 6:
            return '#fb923c'  # Orange - Challenging
        else:
            return '#ef4444'  # Red - Tough
    
    def get_pain_category(pain_level):
        if pain_level is None or pd.isna(pain_level):
            return 'No Data'
        elif pain_level <= 2:
            return 'Great'
        elif pain_level <= 4:
            return 'Okay'
        elif pain_level <= 6:
            return 'Challenging'
        else:
            return 'Tough'
    
    # Create calendar data
    calendar_data = []
    for week_num, week in enumerate(cal):
        for day_num, day in enumerate(week):
            if day == 0:  # Empty cell
                continue
                
            date_str = f"{current_year}-{current_month:02d}-{day:02d}"
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                
                # Find pain data for this day
                day_data = df[df['date'].dt.date == date_obj.date()]
                if not day_data.empty:
                    pain_level = day_data.iloc[0]['max_pain']
                    episodes = day_data.iloc[0]['episodes']
                    avg_pain = day_data.iloc[0]['avg_pain']
                else:
                    pain_level = None
                    episodes = 0
                    avg_pain = None
                
                calendar_data.append({
                    'day': day,
                    'week': week_num,
                    'weekday': day_num,
                    'date': date_str,
                    'pain_level': pain_level,
                    'episodes': episodes,
                    'avg_pain': avg_pain,
                    'color': get_pain_color(pain_level),
                    'category': get_pain_category(pain_level)
                })
            except ValueError:
                # Invalid date (e.g., Feb 30th)
                continue
    
    # Create the calendar visualization
    fig = go.Figure()
    
    # Add calendar squares
    for item in calendar_data:
        # Calculate position (flip week order so week 0 is at top)
        x = item['weekday']
        y = 5 - item['week']  # Flip Y-axis so first week is at top
        
        hover_text = f"<b>{calendar.month_name[current_month]} {item['day']}, {current_year}</b><br>"
        hover_text += f"Status: {item['category']}<br>"
        if item['pain_level'] is not None:
            hover_text += f"Max Pain: {item['pain_level']}/10<br>"
            if item['avg_pain'] is not None:
                hover_text += f"Avg Pain: {item['avg_pain']:.1f}/10<br>"
            hover_text += f"Episodes: {item['episodes']}"
        else:
            hover_text += "No health data logged"
        
        # Add the calendar square
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(
                size=50,
                color=item['color'],
                line=dict(width=2, color='white'),
                symbol='square'
            ),
            text=str(item['day']),
            textfont=dict(color='black', size=14, family='Arial Black'),
            hovertemplate=hover_text + '<extra></extra>',
            showlegend=False
        ))
    
    # Add weekday labels
    weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i, day_name in enumerate(weekdays):
        fig.add_trace(go.Scatter(
            x=[i], y=[6],
            mode='text',
            text=day_name,
            textfont=dict(size=12, color='#666'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Create legend
    legend_items = [
        {'category': 'Great', 'color': '#4ade80', 'range': '1-2'},
        {'category': 'Okay', 'color': '#fbbf24', 'range': '3-4'},
        {'category': 'Challenging', 'color': '#fb923c', 'range': '5-6'},
        {'category': 'Tough', 'color': '#ef4444', 'range': '7-10'},
        {'category': 'No Data', 'color': '#f0f0f0', 'range': '—'}
    ]
    
    for i, item in enumerate(legend_items):
        fig.add_trace(go.Scatter(
            x=[8.5], y=[4.5 - i * 0.5],
            mode='markers+text',
            marker=dict(size=20, color=item['color'], symbol='square'),
            text=f"   {item['category']} ({item['range']})",
            textposition='middle right',
            textfont=dict(size=10),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Update layout
    fig.update_layout(
        title=f"📅 {calendar.month_name[current_month]} {current_year} - Pain Level Calendar",
        xaxis=dict(
            range=[-0.5, 10],
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        yaxis=dict(
            range=[-0.5, 6.5],
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        margin=dict(l=20, r=20, t=60, b=20),
        height=400
    )
    
    return fig

def load_daily_history_ui():
    """Load and display daily health history data."""
    try:
        records = [r.__dict__ for r in load_history()]
        print(f"📊 Loading daily history: {len(records)} records found")
        
        if records:
            df = pd.DataFrame(records)
            df['date'] = pd.to_datetime(df['date'])
            
            # Create a calendar-style visualization
            fig = create_calendar_view(df)
            fig.update_layout(height=500)
            
            # Format table data
            table_df = df[['date','avg_pain','max_pain','episodes','observations']].copy()
            table_df['date'] = table_df['date'].dt.strftime('%Y-%m-%d')
            table_df = table_df.round(1)  # Round pain values
        else:
            # Create empty calendar view
            empty_df = pd.DataFrame()  # Empty dataframe
            fig = create_calendar_view(empty_df)
            fig.update_layout(
                title="📅 No Daily History Data Available Yet - Start logging health episodes to see your pain patterns!",
                height=400
            )
            
            table_df = pd.DataFrame(columns=['Date','Avg Pain','Max Pain','Episodes','Observations'])
            
        return fig, table_df
        
    except Exception as e:
        print(f"❌ Error loading daily history: {e}")
        # Return error visualization
        fig = px.scatter(
            x=[1], y=[1], 
            title=f"Error loading daily history: {str(e)}",
            labels={'x': 'Check console for details', 'y': ''}
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_traces(marker=dict(size=0))
        
        table_df = pd.DataFrame(columns=['Date','Avg Pain','Max Pain','Episodes','Observations'])
        return fig, table_df

def get_agent_description(agent_name: str) -> str:
    """Get description for the selected agent."""
    agent_info = get_agent_info()
    return agent_info.get(agent_name, "No description available")

# --- Gradio UI Layout ---
with gr.Blocks(
    title="Agno Chat Interface",
    theme=gr.themes.Soft(),
    css="""
    .agent-info { 
        background-color: #f0f9ff; 
        padding: 10px; 
        border-radius: 5px; 
        margin: 5px 0;
        border-left: 3px solid #0ea5e9;
    }
    """
) as demo:
    gr.Markdown("# 🤖 Agno Multi-Modal Chat Interface")
    gr.Markdown("Chat with AI agents powered by the Agno framework. Supports text, voice, and file inputs.")
    
    with gr.Row():
        with gr.Column(scale=3):
            agent_dropdown = gr.Dropdown(
                choices=list(AGENTS.keys()),
                value=list(AGENTS.keys())[0] if AGENTS else None,
                label="🔧 Select Agent",
                info="Choose which AI agent to chat with"
            )
        with gr.Column(scale=1):
            clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")
    
    # Agent description
    agent_description = gr.Markdown(
        value=get_agent_description(list(AGENTS.keys())[0]) if AGENTS else "",
        elem_classes="agent-info"
    )

    # Main chat interface
    chat_history = gr.Chatbot(
        height=500,
        show_label=False,
        container=True,
        type="messages",
        avatar_images=("🧑‍💻", "🤖")
    )
    
    # Text input section
    with gr.Row():
        text_input = gr.Textbox(
            placeholder="💬 Type your message here or use the microphone...",
            scale=4,
            lines=2,
            max_lines=5,
            show_label=False
        )
        send_btn = gr.Button("📤 Send", scale=1, variant="primary")

    # Audio input section
    with gr.Row():
        with gr.Column(scale=2):
            mic_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="🎤 Voice Input"
            )
        with gr.Column(scale=1):
            mic_send_btn = gr.Button("🎵 Transcribe & Send", variant="secondary")

    # File attachment section
    with gr.Row():
        file_input = gr.Files(
            label="📎 Attach Files",
            file_count="multiple"
        )
    
    # Daily history calendar - moved up and opened by default
    with gr.Accordion("📅 Daily Health History", open=True):
        gr.Markdown("**View your aggregated daily health metrics and pain patterns**")
        refresh_history = gr.Button("🔄 Refresh Daily History", variant="secondary")
        calendar_plot = gr.Plot(label="📅 Pain Calendar View")
        history_table = gr.Dataframe(
            label="📋 Daily History Table", 
            interactive=False,
            headers=["Date", "Avg Pain", "Max Pain", "Episodes", "Observations"]
        )

    # Status/info section
    with gr.Row():
        gr.Markdown("""
        ### 💡 Tips:
        - **Text**: Type and press Enter or click Send
        - **Voice**: Record audio and click "Transcribe & Send"
        - **Files**: Attach images, PDFs, or documents for analysis
        - **Agents**: Switch between different AI agents for specialized tasks
        """)
    
    # --- Event Handling ---
    
    # Update agent description when selection changes
    agent_dropdown.change(
        fn=get_agent_description,
        inputs=[agent_dropdown],
        outputs=[agent_description]
    )
    
    # Text input handlers
    text_input.submit(
        fn=user_submit,
        inputs=[text_input, chat_history, agent_dropdown, file_input],
        outputs=[chat_history, text_input, file_input],
    )
    send_btn.click(
        fn=user_submit,
        inputs=[text_input, chat_history, agent_dropdown, file_input],
        outputs=[chat_history, text_input, file_input],
    )
    
    # Microphone input handler
    mic_send_btn.click(
        fn=mic_submit,
        inputs=[mic_input, chat_history, agent_dropdown, file_input],
        outputs=[chat_history, mic_input],
    )
    
    # Clear chat handler
    clear_btn.click(
        fn=clear_chat,
        outputs=[chat_history, text_input]
    )

    refresh_history.click(
        fn=load_daily_history_ui,
        outputs=[calendar_plot, history_table],
    )

    demo.load(
        load_daily_history_ui,
        inputs=None,
        outputs=[calendar_plot, history_table],
    )

if __name__ == "__main__":
    print("🚀 Starting Agno Chat Interface...")
    print(f"📊 Available agents: {', '.join(AGENTS.keys())}")
    
    # Launch the Gradio app
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        show_api=False,
        share=False
    )
```

### agents.py

```python
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
    from health_advisor.recall.agent import recall_agent
    
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

# Coach Agent import - Following docs/agno/core/what_are_agents.md
try:
    from health_advisor.coach.agent import coach_agent
    
    class CoachAgentWrapper:
        name = "Coach Agent"
        description = "Provides empathetic, non-medication health guidance based on current episode and migraine knowledge base"
        
        def __init__(self):
            self._knowledge_loaded = False
        
        def _ensure_knowledge_loaded(self):
            """Lazy load knowledge base only when first needed"""
            if not self._knowledge_loaded:
                try:
                    from health_advisor.knowledge.loader import load_knowledge_if_needed
                    load_knowledge_if_needed()
                    self._knowledge_loaded = True
                    print("✅ Coach knowledge base loaded successfully")
                except Exception as e:
                    print(f"Warning: Coach knowledge base could not be loaded: {e}")
                    print("Coach Agent will use fallback advice instead")
                    self._knowledge_loaded = False
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            """Run the Coach Agent with the user's query"""
            try:
                # Try to load knowledge base on first use
                self._ensure_knowledge_loaded()
                
                response = coach_agent.run(prompt)
                return ChatResult(
                    text=response.content,
                    meta={
                        "agent": "CoachAgent",
                        "model": "gpt-4o-mini-2024-07-18",
                        "tool_calls": getattr(response, 'tool_calls', None),
                        "metrics": getattr(response, 'metrics', None),
                        "knowledge_available": self._knowledge_loaded
                    }
                )
            except Exception as e:
                return ChatResult(
                    text=f"❌ Error running coach agent: {str(e)}",
                    meta={"error": str(e), "agent": "CoachAgent"}
                )
    
    coach_agent_wrapper = CoachAgentWrapper()
except ImportError as e:
    print(f"Warning: Coach Agent not available: {e}")
    coach_agent_wrapper = None

# Router Agent import - Following router_agent_implementation_plan.md
try:
    from health_advisor.router.agent import router_agent
    from health_advisor.router.schema import RouterDecision
    
    # --- THE NEW, STATEFUL MASTER ORCHESTRATOR ---
    class MasterAgent:
        name = "Health Companion"
        description = "Intelligent orchestrator that routes to the right specialist based on your needs"
        
        def __init__(self):
            self.session_storage = {}  # Simple in-memory session storage for MVP
        
        def _get_session_state(self, session_id: str) -> Dict[str, Any]:
            """Get or create session state for a given session ID"""
            if session_id not in self.session_storage:
                self.session_storage[session_id] = {
                    "pending_action": None,
                    "open_episode_id": None,
                    "conversation_context": []
                }
            return self.session_storage[session_id]
        
        def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
            print(f"\n--- MasterAgent: Routing user prompt: '{prompt}' ---")
            
            # In a real app, session_id would be managed per user conversation.
            # We use a fixed one here for simplicity.
            session_id = "user_main_session"
            session_state = self._get_session_state(session_id)
            
            # 1. HANDLE CONTROL MESSAGES & PENDING ACTIONS (SHORT-CIRCUIT)
            if prompt.startswith("/resolve") and session_state.get("pending_action"):
                print("--> Handling resolved action directly.")
                # For MVP, we'll just clear the pending action
                session_state["pending_action"] = None
                return ChatResult(
                    text="✅ Action resolved successfully.",
                    meta={"action": "control_resolved", "session_id": session_id}
                )
            
            # 2. GET ROUTING DECISION (STATE-AWARE)
            try:
                router_response = router_agent.run(prompt)
                
                # Handle both structured and text responses
                if hasattr(router_response, 'content') and isinstance(router_response.content, RouterDecision):
                    decision = router_response.content
                elif hasattr(router_response, 'content'):
                    # Fallback if structured output fails
                    print("⚠️ Router returned non-structured response. Defaulting to logger.")
                    decision = RouterDecision(
                        primary_intent="log",
                        secondary_intent=None,
                        confidence=0.5,
                        rationale="Router failed to return structured output"
                    )
                else:
                    raise Exception("Invalid router response format")
                    
            except Exception as e:
                print(f"⚠️ Router agent failed: {e}. Defaulting to logger.")
                decision = RouterDecision(
                    primary_intent="log",
                    secondary_intent=None,
                    confidence=0.3,
                    rationale="Router agent error - defaulting to health logging"
                )
            
            print(f"🧠 Router Decision: Primary='{decision.primary_intent}', Secondary='{decision.secondary_intent}', Confidence={decision.confidence:.2f}")
            print(f"📝 Rationale: {decision.rationale}")
            
            # 3. APPLY CONFIDENCE THRESHOLDS & HEURISTICS
            final_intent = decision.primary_intent
            if decision.confidence < 0.7:
                # Simple heuristic fallback
                if any(word in prompt.lower() for word in ["when", "did i", "show me", "history", "last time"]):
                    final_intent = "recall"
                elif any(word in prompt.lower() for word in ["what should i do", "help", "advice", "recommend"]):
                    final_intent = "coach"
                print(f"⚠️ Confidence low ({decision.confidence:.2f}), applying heuristic. Final intent: '{final_intent}'")
            
            # 4. EXECUTE THE WORKFLOW (potentially multi-step)
            primary_result = None
            if final_intent == "recall":
                print("--> Routing to Recall Specialist")
                if recall_agent_wrapper:
                    primary_result = recall_agent_wrapper.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Recall Agent not available", meta={"error": "agent_unavailable"})
            
            elif final_intent == "coach":
                print("--> Routing to Coach Specialist")
                if coach_agent_wrapper:
                    primary_result = coach_agent_wrapper.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Coach Agent not available", meta={"error": "agent_unavailable"})
            
            elif final_intent == "control_action":
                print("--> Handling control action")
                primary_result = ChatResult(
                    text="🤖 Control action received. Use specific commands like '/resolve' for actions.",
                    meta={"action": "control_acknowledged"}
                )
            
            elif final_intent == "unknown":
                print("--> Unknown intent - asking for clarification")
                primary_result = ChatResult(
                    text="I'm not sure what you'd like me to help with. You can:\n• Log health information (e.g., 'I have a headache')\n• Ask about your history (e.g., 'Show me my recent episodes')\n• Get advice (e.g., 'What should I do for this pain?')",
                    meta={"action": "clarification_request"}
                )
            
            else:  # Default to logger (including "log" and "clarify_response")
                print("--> Routing to Logger Workflow")
                if health_logger_v3:
                    primary_result = health_logger_v3.run(prompt, files)
                else:
                    primary_result = ChatResult(text="❌ Health Logger not available", meta={"error": "agent_unavailable"})
            
            # 5. HANDLE SECONDARY INTENT (CHAINING)
            if decision.secondary_intent and primary_result and not primary_result.text.startswith("❌"):
                print(f"--- Handling secondary intent: '{decision.secondary_intent}' ---")
                
                if decision.secondary_intent == "coach" and coach_agent_wrapper:
                    print("--> Chaining to Coach Specialist")
                    secondary_result = coach_agent_wrapper.run(
                        "Given what I just told you, what should I do?", 
                        files=None
                    )
                    # Combine the results
                    combined_text = f"{primary_result.text}\n\n---\n\n**🩺 Health Guidance:**\n{secondary_result.text}"
                    return ChatResult(
                        text=combined_text,
                        meta={
                            "primary_agent": final_intent,
                            "secondary_agent": decision.secondary_intent,
                            "router_confidence": decision.confidence,
                            "chained_response": True
                        }
                    )
                
                elif decision.secondary_intent == "recall" and recall_agent_wrapper:
                    print("--> Chaining to Recall Specialist")
                    secondary_result = recall_agent_wrapper.run(
                        "Show me recent episodes related to what I just mentioned",
                        files=None
                    )
                    combined_text = f"{primary_result.text}\n\n---\n\n**📊 Related History:**\n{secondary_result.text}"
                    return ChatResult(
                        text=combined_text,
                        meta={
                            "primary_agent": final_intent,
                            "secondary_agent": decision.secondary_intent,
                            "router_confidence": decision.confidence,
                            "chained_response": True
                        }
                    )
            
            # Add routing metadata to the response
            if primary_result:
                if not primary_result.meta:
                    primary_result.meta = {}
                primary_result.meta.update({
                    "routed_by": "MasterAgent",
                    "final_intent": final_intent,
                    "router_confidence": decision.confidence,
                    "had_secondary_intent": decision.secondary_intent is not None
                })
            
            return primary_result if primary_result else ChatResult(
                text="❌ Unknown error in routing",
                meta={"error": "routing_failure"}
            )
    
    master_agent = MasterAgent()
    
except ImportError as e:
    print(f"Warning: Router Agent not available: {e}")
    master_agent = None

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

# Add Coach Agent if available
if coach_agent_wrapper:
    AGENTS["Coach Agent"] = coach_agent_wrapper

# Add Master Agent (Health Companion) if available - This should be the DEFAULT
if master_agent:
    AGENTS["Health Companion (Auto-Router)"] = master_agent

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
```

## 3. Dependencies and Configuration

### requirements.txt
```
python-dotenv==1.0.1
gradio==4.44.0
openai==1.35.14
agno==0.2.5
apscheduler==3.10.4
pandas==2.2.2
plotly==5.24.0
```

### .env.example
```
# Core LLM / STT
OPENAI_API_KEY=sk-...

# If you'll use other APIs, add here and read with dotenv in agents.py or app.py:
# EXA_API_KEY=...
# NEBIUS_API_KEY=...
# ANTHROPIC_API_KEY=...
# GROQ_API_KEY=...
```