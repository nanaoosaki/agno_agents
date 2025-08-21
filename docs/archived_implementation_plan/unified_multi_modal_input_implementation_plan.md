This is an excellent observation and a fantastic next step for the user interface. You've correctly identified that the current UI, while functional, forces the user into separate actions for text, voice, and files. A truly modern, multi-modal interface should allow the user to combine these inputs into a single, seamless turn.

The inspiration images you provided are a perfect target. While creating an identical, dynamic overlay in Gradio is complex, we can absolutely achieve the core functional goal: a single "Send" button that captures input from the text box, microphone, and file uploader simultaneously.

This requires a refactor of the UI and the backend handlers, but it's a very logical progression that will significantly improve the user experience.

Here is the updated implementation plan to create this unified, multi-modal input experience.

Implementation Plan: Unified Multi-Modal Input (v3.2)
1. Architectural Goal

We will refactor the Gradio UI (app.py) and its backend handlers to support a single submission action that collects data from all input components (Textbox, Audio, Files). The HealthLoggerWorkflow will be enhanced to process this rich, multi-modal input coherently.

Step 1: Refactor the Gradio UI in app.py

The goal is to simplify the layout and consolidate the submission logic into a single button.

File: app.py

Changes:

Remove the separate "Transcribe & Send" button. We will have only one primary "Send" button.

Create a new, unified submission handler function called unified_submit.

Wire all input components to this single handler. The Send button's click event and the Textbox's submit event will both trigger unified_submit, collecting data from all three input fields.

Here is the updated app.py code. You can replace the entire file with this.

code
Python
download
content_copy
expand_less

# app.py (Revised for Unified Input)

import os
from typing import List, Tuple, Optional
import gradio as gr
from dotenv import load_dotenv

# ... (keep existing imports for OpenAI, pandas, plotly, etc.) ...
from agents import call_agent, AGENTS, get_agent_info

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- (Keep the existing transcribe_audio, normalize_files, and other helper functions) ---
# ...
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

def transcribe_audio(audio_path: str) -> str:
    if not audio_path or not client: return ""
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=f)
    return transcript.text if hasattr(transcript, "text") else ""

def normalize_files(files: Optional[List[gr.File]]) -> List[str]:
    if not files: return []
    return [str(f.name) for f in files]

def format_user_turn(text: str, audio_transcript: str, filepaths: List[str]) -> str:
    """Formats the user's turn for display in the chat history."""
    parts = []
    if audio_transcript:
        parts.append(f"🎤 **Voice Input:** *\"{audio_transcript}\"*")
    if text:
        parts.append(f"✏️ **Typed Notes:** *\"{text}\"*")
    if filepaths:
        file_names = [os.path.basename(p) for p in filepaths]
        # For simplicity, just list names. Can add image markdown here too.
        parts.append(f"📎 **Attachments:** {', '.join(file_names)}")
    return "\n\n".join(parts)

# --- NEW UNIFIED SUBMISSION HANDLER ---
def unified_submit(
    text_message: str,
    audio_path: str,
    files: Optional[List[gr.File]],
    history: List[Tuple[str, str]],
    agent_name: str,
):
    """
    Handles a single submission from any combination of text, audio, and files.
    """
    history = history or []
    
    # 1. Process all inputs
    audio_transcript = transcribe_audio(audio_path)
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
    history.append((display_message, "🤔 *Thinking...*"))
    
    # Yield to update the UI immediately with the user's turn
    yield history, "", None, None

    # 4. Call the agent with all collected information
    result = call_agent(agent_name, combined_prompt, filepaths)
    history[-1] = (display_message, result.text)

    # 5. Yield final result and clear all inputs
    yield history, "", None, None

# --- REVISED GRADIO UI LAYOUT ---
with gr.Blocks(title="Agno Health Companion", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Agno Health Companion (Multi-Modal)")
    
    with gr.Row():
        agent_dropdown = gr.Dropdown(choices=list(AGENTS.keys()), value="Health Logger (v3.1 Multi-Modal)", label="Select Agent")
        clear_btn = gr.Button("🗑️ Clear Chat")

    chat_history = gr.Chatbot(height=500, label="Conversation", bubble_fn=lambda x: x)
    
    with gr.Box():
        with gr.Column():
            text_input = gr.Textbox(placeholder="Type any notes here...", label="Text Input", lines=2)
            mic_input = gr.Audio(source="microphone", type="filepath", label="Voice Input (record your main message here)")
            file_input = gr.Files(label="Attach Files (e.g., medication labels, food pictures)", file_count="multiple")
            send_btn = gr.Button("Send All Inputs", variant="primary")

    # ... (Daily History Calendar components remain the same) ...

    # --- Event Wiring ---
    # A single button and the textbox submit event trigger the unified handler
    send_btn.click(
        fn=unified_submit,
        inputs=[text_input, mic_input, file_input, chat_history, agent_dropdown],
        outputs=[chat_history, text_input, mic_input, file_input],
    )
    text_input.submit(
        fn=unified_submit,
        inputs=[text_input, mic_input, file_input, chat_history, agent_dropdown],
        outputs=[chat_history, text_input, mic_input, file_input],
    )
    
    clear_btn.click(fn=lambda: ([], "", None, None), outputs=[chat_history, text_input, mic_input, file_input])
    # ... (demo.load for calendar remains the same) ...

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", inbrowser=True)
Step 2: Update the HealthLoggerWorkflowWrapper in agents.py

The wrapper now receives a combined_prompt that may contain both transcribed audio and typed text. The logic for handling files remains the same.

File: agents.py

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# agents.py
# ... (imports remain the same)

class HealthLoggerWorkflowWrapper:
    name = "Health Logger (v3.1 Multi-Modal)"
    # ... (rest of the class) ...

    def run(self, prompt: str, filepaths: Optional[List[str]] = None) -> ChatResult:
        session_id = "user_main_session"
        
        attachments = process_uploaded_files(filepaths or [])
        images_to_send = [Image(filepath=att.path, meta={"tag": att.tag}) for att in attachments]

        # The prompt is now pre-combined, so we just pass it along.
        # The agent's instructions will guide it to parse this combined input.
        response = self.workflow.run(
            message=prompt,
            images=images_to_send,
            session_id=session_id
        )
        
        return ChatResult(text=response.content, meta={...}) # meta is optional

# ... (rest of agents.py) ...
Step 3: Enhance the Extractor Agent's Instructions (Crucial Final Step)

The ExtractorAgent now needs to be explicitly told that the user's message might be a composite of different input modes.

File: healthlogger/agents.py (or healthlogger/prompts.py)

code
Python
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# healthlogger/agents.py
# In create_extractor_agent function:

    instructions=[
        get_extractor_system_prompt(),
        "CRITICAL CONTEXT: The user's message may be a combination of transcribed voice audio and typed text notes. The prompt will be formatted like: 'User said via voice: '...'. User typed: '...'.'",
        "You must synthesize information from ALL parts of the prompt (voice, text, and any attached images) to create a single, comprehensive log entry.",
        "Analyze the user's LATEST message and ANY ATTACHED IMAGES in context of the chat history.",
        # ... (rest of the multi-modal and episode linking instructions remain the same) ...
    ],
How to Test the New Unified UI

Run the App: python app.py

Select the Agent: Ensure "Health Logger (v3.1 Multi-Modal)" is selected.

Perform a Multi-Modal Submission:

Record Audio: In the Voice Input component, record yourself saying: "I took my morning medication."

Type Text: In the Text Input box, type: "It's amitriptyline, 25 mg."

Attach File: In the Attach Files component, upload a picture of an amitriptyline bottle.

Click the single "Send All Inputs" button.

Verify the Output:

UI Chat History: You should see a single user turn containing your voice transcript, your typed notes, and the attached image.

Agent Response: The agent should provide a single, coherent confirmation, such as: "Got it. I've logged an intervention for 'medication' (amitriptyline, 25mg). The image confirms the details. Hope you have a great day!"

Data Files: Your interventions.json and events.jsonl should contain a single new entry that correctly combines the information from all three input modes.

This plan achieves your goal of a unified, multi-modal input experience. It streamlines the UI and makes the agent interaction far more natural and powerful, all while leveraging the robust architecture we've already built.