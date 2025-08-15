# app.py
import os
from typing import List, Tuple, Optional
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI
from agents import call_agent, AGENTS

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client for audio transcription
client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    print("Warning: OPENAI_API_KEY not set. Audio transcription will be disabled.")

def transcribe_audio(audio_path: str) -> str:
    """Transcribe microphone audio using OpenAI's Whisper."""
    if not audio_path or not client:
        return ""
    
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text if hasattr(transcript, "text") else ""

def normalize_files(files: Optional[List[gr.File]]) -> List[str]:
    """Convert Gradio file objects to a list of filesystem paths."""
    if not files:
        return []
    return [str(f.name) for f in files]

def user_submit(
    message: str,
    history: List[Tuple[str, str]],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """Handle text and file submissions."""
    history = history or []
    filepaths = normalize_files(files)
    
    # Append user message and files to chat history
    display_message = message
    if filepaths:
        display_message += f"\n\n**Attachments:**\n- " + "\n- ".join([os.path.basename(p) for p in filepaths])
    history.append((display_message, ""))
    
    # Call the agent and update the assistant's response
    result = call_agent(agent_name, message, filepaths)
    history[-1] = (display_message, result.text)
    
    return history, gr.update(value=""), gr.update(value=None) # Clear textbox and file uploader

def mic_submit(
    audio_path: str,
    history: List[Tuple[str, str]],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """Handle microphone submissions by transcribing first."""
    history = history or []
    transcribed_text = transcribe_audio(audio_path)
    
    if not transcribed_text:
        transcribed_text = "[Audio input was empty or could not be transcribed]"

    return user_submit(transcribed_text, history, agent_name, files)

def clear_chat():
    """Clear the chat history."""
    return [], []

# --- Gradio UI Layout ---
with gr.Blocks(title="Agno Chat") as demo:
    gr.Markdown("## Agno Multi-Modal Chat")
    
    with gr.Row():
        agent_name = gr.Dropdown(
            choices=list(AGENTS.keys()),
            value=list(AGENTS.keys())[0],
            label="Select Agent"
        )
        clear_btn = gr.Button("Clear Chat")

    chat_history = gr.Chatbot(height=500, bubble_fn=lambda x: x, label="Conversation")
    
    with gr.Row():
        text_input = gr.Textbox(placeholder="Type your message here or use the microphone...", scale=4)
        send_btn = gr.Button("Send", scale=1)

    with gr.Row():
        mic_input = gr.Audio(source="microphone", type="filepath", label="Voice Input")
        mic_send_btn = gr.Button("Transcribe & Send")

    with gr.Row():
        file_input = gr.Files(label="Attach Files (Images, etc.)", file_count="multiple")
    
    # --- Event Handling ---
    text_input.submit(
        fn=user_submit,
        inputs=[text_input, chat_history, agent_name, file_input],
        outputs=[chat_history, text_input, file_input],
    )
    send_btn.click(
        fn=user_submit,
        inputs=[text_input, chat_history, agent_name, file_input],
        outputs=[chat_history, text_input, file_input],
    )
    mic_send_btn.click(
        fn=mic_submit,
        inputs=[mic_input, chat_history, agent_name, file_input],
        outputs=[chat_history, mic_input],
    )
    clear_btn.click(fn=clear_chat, outputs=[chat_history, text_input])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", inbrowser=True)