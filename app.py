# app.py
# Gradio-based chat interface for Agno agents
# Combines features from implementation_plan_o3.md and additional_details_from_gemini2.5pro.md

import os
import uuid
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

def format_user_turn(text: str, audio_transcript: str, filepaths: List[str]) -> str:
    """Formats the user's turn for display in the chat history."""
    parts = []
    if audio_transcript:
        parts.append(f"🎤 **Voice Input:** *\"{audio_transcript}\"*")
    if text:
        parts.append(f"✏️ **Typed Notes:** *\"{text}\"*")
    if filepaths:
        file_names = [os.path.basename(p) for p in filepaths]
        parts.append(f"📎 **Attachments:** {', '.join(file_names)}")
    return "\n\n".join(parts)

def unified_submit(
    text_message: str,
    audio_path: str,
    files: Optional[List[gr.File]],
    history: List[dict],
    dev_mode: bool,
    simple_agent: str,
    dev_agent: str,
    session_id: str = None,
):
    """
    Handles a single submission from any combination of text, audio, and files.
    This is the new unified handler that replaces separate text and audio submission.
    """
    history = history or []
    
    # 1. Process all inputs
    audio_transcript = transcribe_audio(audio_path) if audio_path else ""
    filepaths = normalize_files(files)
    
    # Check if there is any input at all
    if not text_message.strip() and not audio_transcript.strip() and not filepaths:
        # Nothing to do, just return the current state
        return history, "", None, None
    
    # 2. Construct a comprehensive prompt for the agent
    combined_prompt = ""
    if audio_transcript:
        combined_prompt += f"User said via voice: '{audio_transcript}'. "
    if text_message:
        combined_prompt += f"User typed: '{text_message}'."
    
    # 3. Format the message for display in the UI
    display_message = format_user_turn(text_message, audio_transcript, filepaths)
    history.append({"role": "user", "content": display_message})
    history.append({"role": "assistant", "content": "🤔 *Thinking...*"})
    
    # Yield to update the UI immediately with the user's turn
    yield history, "", None, None
    
    # 4. Generate session ID if not provided
    if not session_id:
        session_id = str(uuid.uuid4())
    
    # 5. Determine active agent
    agent_name = get_active_agent_name(dev_mode, simple_agent, dev_agent)
    
    # 6. Call the agent with all collected information
    try:
        result = call_agent(agent_name, combined_prompt, filepaths, session_id)
        
        # Update the last message with the actual response
        response_text = result.text
        
        # Add developer mode route chip if enabled
        if dev_mode and result.meta and "routed_to" not in result.meta:
            # For direct agent calls in dev mode, show which agent was used
            route_chip = f"🔍 **Routed to:** {agent_name}"
            response_text = f"{route_chip}\n\n{result.text}"
        elif result.meta and result.meta.get("routed_to"):
            # For auto-router responses, show routing decision with confidence
            routed_to = result.meta.get("routed_to")
            confidence = result.meta.get("confidence", "N/A")
            route_chip = f"🎯 **Auto-Routed:** {routed_to} ({confidence})"
            response_text = f"{route_chip}\n\n{result.text}"
        
        # Add metadata if available
        if result.meta and "error" not in result.meta:
            model_info = result.meta.get("model", "")
            if model_info:
                response_text = f"{response_text}\n\n*Model: {model_info}*"
        
        history[-1] = {"role": "assistant", "content": response_text}
        
    except Exception as e:
        history[-1] = {"role": "assistant", "content": f"❌ **Error:** {str(e)}"}
    
    # 5. Yield final result and clear all inputs
    yield history, "", None, None

# Legacy mic_submit function removed - now using unified_submit

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

def toggle_dev_mode(dev_mode_enabled):
    """Toggle between simple and developer agent dropdowns."""
    if dev_mode_enabled:
        return (
            gr.update(visible=False),  # Hide simple dropdown
            gr.update(visible=True),   # Show developer dropdown
            "🔧 **Developer Mode Active** - Testing individual specialist agents"
        )
    else:
        return (
            gr.update(visible=True),   # Show simple dropdown
            gr.update(visible=False),  # Hide developer dropdown
            "🤖 **User Mode** - Unified health companion experience"
        )

def get_active_agent_name(dev_mode, simple_agent, dev_agent):
    """Get the currently active agent name based on mode."""
    if dev_mode:
        return dev_agent
    else:
        return simple_agent

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
        with gr.Column(scale=2):
            # Developer mode toggle
            dev_mode_toggle = gr.Checkbox(
                label="🔧 Developer Mode", 
                value=False,
                info="Enable testing of individual agents"
            )
        with gr.Column(scale=4):
            # Default dropdown (Auto-Router only)
            agent_dropdown_simple = gr.Dropdown(
                choices=["Health Companion (Auto-Router)"],
                value="Health Companion (Auto-Router)",
                label="🤖 Health Companion",
                info="AI-powered health assistant",
                visible=True
            )
            # Developer dropdown (all agents)
            agent_dropdown_dev = gr.Dropdown(
                choices=list(AGENTS.keys()),
                value=list(AGENTS.keys())[0] if AGENTS else None,
                label="🔧 Select Specialist Agent",
                info="Choose which AI agent to test directly",
                visible=False
            )
        with gr.Column(scale=1):
            clear_btn = gr.Button("🗑️ Clear Chat", variant="secondary")
    
    # Mode status indicator
    mode_status = gr.Markdown(
        value="🤖 **User Mode** - Unified health companion experience",
        elem_classes="agent-info"
    )
    
    # Agent description
    agent_description = gr.Markdown(
        value=get_agent_description("Health Companion (Auto-Router)"),
        elem_classes="agent-info"
    )

    # Session state management
    session_id_state = gr.State(value=lambda: str(uuid.uuid4()))
    
    # Main chat interface
    chat_history = gr.Chatbot(
        height=500,
        show_label=False,
        container=True,
        type="messages",
        avatar_images=("🧑‍💻", "🤖")
    )
    
    # --- UNIFIED MULTI-MODAL INPUT SECTION ---
    with gr.Group():
        gr.Markdown("### 🔄 **Multi-Modal Input** - Combine text, voice, and files in one submission")
        with gr.Column():
            text_input = gr.Textbox(
                placeholder="💬 Type any notes here...",
                label="Text Input",
                lines=2,
                max_lines=5
            )
            mic_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="🎤 Voice Input (record your main message here)"
            )
            file_input = gr.Files(
                label="📎 Attach Files (e.g., medication labels, food pictures)",
                file_count="multiple"
            )
            send_btn = gr.Button("📤 Send All Inputs", variant="primary", size="lg")
    
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
        ### 💡 **Unified Multi-Modal Experience**:
        - **Combine Everything**: Use text, voice, and files together in one submission
        - **Text**: Type notes or additional context 
        - **Voice**: Record your main message (automatically transcribed)
        - **Files**: Attach medication labels, nutrition facts, or health documents
        - **Single Send**: One button processes all inputs together for comprehensive analysis
        """)
    
    # --- Event Handling ---
    
    # Developer mode toggle
    dev_mode_toggle.change(
        fn=toggle_dev_mode,
        inputs=[dev_mode_toggle],
        outputs=[agent_dropdown_simple, agent_dropdown_dev, mode_status]
    )
    
    # Update agent description when selection changes
    agent_dropdown_simple.change(
        fn=get_agent_description,
        inputs=[agent_dropdown_simple],
        outputs=[agent_description]
    )
    agent_dropdown_dev.change(
        fn=get_agent_description,
        inputs=[agent_dropdown_dev],
        outputs=[agent_description]
    )
    
    # Unified submission handlers
    send_btn.click(
        fn=unified_submit,
        inputs=[text_input, mic_input, file_input, chat_history, dev_mode_toggle, agent_dropdown_simple, agent_dropdown_dev, session_id_state],
        outputs=[chat_history, text_input, mic_input, file_input],
    )
    text_input.submit(
        fn=unified_submit,
        inputs=[text_input, mic_input, file_input, chat_history, dev_mode_toggle, agent_dropdown_simple, agent_dropdown_dev, session_id_state],
        outputs=[chat_history, text_input, mic_input, file_input],
    )
    
    # Clear chat handler - now clears all inputs
    clear_btn.click(
        fn=lambda: ([], "", None, None),
        outputs=[chat_history, text_input, mic_input, file_input]
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