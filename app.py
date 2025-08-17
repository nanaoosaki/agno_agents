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

def load_daily_history_ui():
    records = [r.__dict__ for r in load_history()]
    if records:
        df = pd.DataFrame(records)
        df['date'] = pd.to_datetime(df['date'])
        fig = px.density_heatmap(
            df,
            x=df['date'].dt.day,
            y=df['date'].dt.month,
            z='max_pain',
            nbinsx=31,
            nbinsy=12,
            color_continuous_scale='Reds',
            labels={'x': 'Day', 'y': 'Month', 'z': 'Max Pain'}
        )
        table = df[['date','avg_pain','max_pain','episodes','observations']]
    else:
        fig = px.density_heatmap(x=[0], y=[0], z=[0])
        table = pd.DataFrame(columns=['date','avg_pain','max_pain','episodes','observations'])
    return fig, table

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
    
    # Status/info section
    with gr.Row():
        gr.Markdown("""
        ### 💡 Tips:
        - **Text**: Type and press Enter or click Send
        - **Voice**: Record audio and click "Transcribe & Send"
        - **Files**: Attach images, PDFs, or documents for analysis
        - **Agents**: Switch between different AI agents for specialized tasks
        """)

    # Daily history calendar
    with gr.Accordion("📅 Daily History", open=False):
        refresh_history = gr.Button("Refresh")
        calendar_plot = gr.Plot(label="Pain Calendar")
        history_table = gr.Dataframe(interactive=False)
    
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