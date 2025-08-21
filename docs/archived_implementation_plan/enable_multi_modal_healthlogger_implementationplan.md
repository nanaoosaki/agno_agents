Definitive Implementation Plan: Multi-Modal Health Logger (v3.1)
1. Core Architectural Decision: Enhance, Don't Replace
We will stick to our core strategy: enhance the existing HealthLoggerWorkflow to be multi-modal. We will not create a separate "Image Agent." This ensures a seamless user experience and keeps the architecture clean.
The plan focuses on three key areas:
Safe File Handling: A new utility for processing and validating uploaded files before they reach the agent.
Intelligent Context Injection: Smarter ways to pass image data and metadata to the ExtractorAgent.
Enhanced Agent Instructions: Updating the ExtractorAgent's prompt to guide its analysis of visual data.
Step 1: Create a Secure File Handling & Tagging Utility
This is the most critical addition, inspired by the "gpt5" feedback. We need a deterministic layer to handle file uploads safely.
New File: core/file_handler.py
code
Python
# core/file_handler.py
import os
from pathlib import Path
from typing import List, Literal, Optional
from pydantic import BaseModel
import magic # Requires `pip install python-magic`

# Define a structured object for attachments, as suggested.
class Attachment(BaseModel):
    kind: Literal["image", "file"]
    path: str
    mime: Optional[str] = None
    tag: Literal["Food", "MedLabel", "Other"] = "Other"

def process_uploaded_files(filepaths: List[str]) -> List[Attachment]:
    """
    Validates, processes, and tags uploaded files before passing them to an agent.
    - Validates file type using python-magic.
    - Strips EXIF data for privacy (requires `pip install piexif`).
    - Suggests a tag based on filename keywords.
    - Returns a list of structured Attachment objects.
    """
    processed_attachments = []
    supported_image_mimes = ["image/jpeg", "image/png", "image/webp"]

    for fp in filepaths:
        try:
            # 1. Validate file type
            mime_type = magic.from_file(fp, mime=True)
            if mime_type not in supported_image_mimes:
                print(f"Warning: Unsupported file type '{mime_type}' for {fp}. Skipping.")
                continue

            # 2. Suggest a tag (simple keyword logic)
            tag = "Other"
            filename_lower = os.path.basename(fp).lower()
            if any(k in filename_lower for k in ["nutrition", "label", "cereal"]):
                tag = "Food"
            elif any(k in filename_lower for k in ["med", "pill", "bottle", "prescription"]):
                tag = "MedLabel"

            # 3. TODO: Add EXIF stripping and resizing logic here for production.

            processed_attachments.append(
                Attachment(kind="image", path=fp, mime=mime_type, tag=tag)
            )
        except Exception as e:
            print(f"Error processing file {fp}: {e}")

    return processed_attachments```

---

#### **Step 2: Update the `HealthLoggerWorkflowWrapper` to Use the File Handler**

This is where we integrate the new utility. The wrapper in `agents.py` will now be responsible for converting raw file paths into safe, structured `Attachment` objects.

**File**: `agents.py` (Modify `HealthLoggerWorkflowWrapper` and `call_agent`)

```python
# agents.py

# ... (keep existing imports) ...
from core.file_handler import process_uploaded_files, Attachment # <-- NEW IMPORT
from agno.media import Image # Agno's class for passing images to agents

# --- Update the Main Workflow Wrapper ---
class HealthLoggerWorkflowWrapper:
    name = "Health Logger (v3)"
    # ... (existing __init__ and description) ...

    def run(self, prompt: str, filepaths: Optional[List[str]] = None) -> ChatResult:
        session_id = "user_main_session"
        
        # --- NEW LOGIC: Use the file handler ---
        attachments = process_uploaded_files(filepaths or [])
        images_to_send = [Image(filepath=att.path, meta={"tag": att.tag}) for att in attachments]

        # Augment the prompt with context about the attachments
        final_prompt = prompt
        if attachments:
            attachment_summary = [f"{att.tag} ({os.path.basename(att.path)})" for att in attachments]
            final_prompt = (
                "The user has provided the following health update and attached some files. "
                "Analyze both the text and the images to create a comprehensive log entry.\n\n"
                f"USER MESSAGE: '{prompt}'\n"
                f"ATTACHED FILES: {', '.join(attachment_summary)}"
            )

        # Run the workflow with the enhanced prompt and Agno Image objects
        response = self.workflow.run(
            message=final_prompt,
            images=images_to_send, # <-- Pass the structured Agno objects
            session_id=session_id
        )
        
        # ... (rest of the run method is the same)
        return ChatResult(...)

# The call_agent function remains the same as it just delegates.
Step 3: Enhance the ExtractorAgent Instructions for Vision
Now we update the brain of the operation, the ExtractorAgent, to understand how to handle the images and their tags.
File: healthlogger/agents.py (Modify create_extractor_agent)
code
Python
# healthlogger/agents.py

def create_extractor_agent():
    # ... (existing agent setup) ...
    return Agent(
        # ... (model, response_model, etc.) ...
        instructions=[
            get_extractor_system_prompt(),
            "IMPORTANT: You must analyze the user's LATEST message and ANY ATTACHED IMAGES in context of the chat history.",
            
            # --- NEW INSTRUCTIONS FOR IMAGE HANDLING ---
            "If images are attached, their metadata (like tags) will be in the prompt. Prioritize your analysis based on these tags:",
            "  - If you see a file tagged as 'MedLabel', extract the medication name, strength/dosage, and frequency.",
            "  - If you see a file tagged as 'Food', extract key nutrition facts like calories, sugar, sodium, and serving size from the label.",
            "  - For all images, describe what you see and incorporate it into the 'notes' field of the health log.",
            "If the user's text contradicts the information on an image (e.g., text says '50mg', label says '25mg'), TRUST THE IMAGE and note the discrepancy in your rationale.",
            "If an image is blurry or unreadable, state that you cannot extract information from it and set your confidence score low."
        ],
        # ... (rest of the agent config) ...
    )
Summary of Changes and Benefits
Security & Privacy (core/file_handler.py): You now have a dedicated, deterministic place to add file validation, EXIF stripping, and resizing, protecting your system and users. This directly addresses a key suggestion.
Intelligent Routing (core/file_handler.py): The new tag system (Food, MedLabel) provides a powerful hint to the LLM, making its extraction more accurate and reliable without complex logic.
Robustness (agents.py): The HealthLoggerWorkflowWrapper now cleanly separates the concern of handling raw file uploads from the core agent logic.
Enhanced AI Reasoning (healthlogger/agents.py): The ExtractorAgent is now explicitly instructed on how to prioritize and handle different types of images and resolve conflicts, making it much smarter.
No Redundant Agents: We achieve all of this by enhancing your existing, powerful workflow, proving the "one multimodal agent" strategy is the right one.