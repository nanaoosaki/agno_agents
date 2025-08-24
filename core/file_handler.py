# core/file_handler.py
# Secure file handling and tagging utility for multi-modal health logger
# Following enable_multi_modal_healthlogger_implementationplan.md

import os
from pathlib import Path
from typing import List, Literal, Optional
from pydantic import BaseModel

# Try to import magic for MIME type detection
try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False
    print("Warning: python-magic not available. File type validation will be limited.")

# Define a structured object for attachments, as suggested
class Attachment(BaseModel):
    """Represents a processed file attachment with metadata"""
    kind: Literal["image", "file"]
    path: str
    mime: Optional[str] = None
    tag: Literal["Food", "MedLabel", "Other"] = "Other"

def process_uploaded_files(filepaths: List[str]) -> List[Attachment]:
    """
    Validates, processes, and tags uploaded files before passing them to an agent.
    
    Features:
    - Validates file type using python-magic (if available)
    - Suggests a tag based on filename keywords
    - Returns a list of structured Attachment objects
    
    Args:
        filepaths: List of file paths to process
        
    Returns:
        List of Attachment objects with metadata
    """
    processed_attachments = []
    supported_image_mimes = ["image/jpeg", "image/png", "image/webp", "image/gif"]
    supported_image_extensions = [".jpg", ".jpeg", ".png", ".webp", ".gif"]
    
    for fp in filepaths:
        try:
            # Check if file exists
            if not os.path.exists(fp):
                print(f"Warning: File {fp} does not exist. Skipping.")
                continue
            
            # 1. Validate file type
            mime_type = None
            is_supported_image = False
            
            if MAGIC_AVAILABLE:
                try:
                    mime_type = magic.from_file(fp, mime=True)
                    is_supported_image = mime_type in supported_image_mimes
                except Exception as e:
                    print(f"Warning: Could not determine MIME type for {fp}: {e}")
                    # Fallback to extension-based detection
                    file_ext = Path(fp).suffix.lower()
                    is_supported_image = file_ext in supported_image_extensions
            else:
                # Fallback: Use file extension
                file_ext = Path(fp).suffix.lower()
                is_supported_image = file_ext in supported_image_extensions
                if is_supported_image:
                    # Map extensions to MIME types
                    ext_to_mime = {
                        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                        ".png": "image/png", ".webp": "image/webp",
                        ".gif": "image/gif"
                    }
                    mime_type = ext_to_mime.get(file_ext, "image/unknown")
            
            if not is_supported_image:
                print(f"Warning: Unsupported file type '{mime_type or 'unknown'}' for {fp}. Skipping.")
                continue
            
            # 2. Suggest a tag based on filename keywords
            tag = "Other"
            filename_lower = os.path.basename(fp).lower()
            
            # Food-related keywords
            food_keywords = [
                "nutrition", "label", "cereal", "food", "ingredient", 
                "calories", "carbs", "protein", "vitamin", "supplement"
            ]
            
            # Medical-related keywords  
            med_keywords = [
                "med", "pill", "bottle", "prescription", "dosage", 
                "tablet", "capsule", "drug", "pharmacy", "rx"
            ]
            
            if any(k in filename_lower for k in food_keywords):
                tag = "Food"
            elif any(k in filename_lower for k in med_keywords):
                tag = "MedLabel"
            
            # 3. Create attachment object
            processed_attachments.append(
                Attachment(
                    kind="image", 
                    path=fp, 
                    mime=mime_type, 
                    tag=tag
                )
            )
            
            print(f"Processed file: {os.path.basename(fp)} (tagged as {tag})")
            
        except Exception as e:
            print(f"Error processing file {fp}: {e}")
            continue
    
    return processed_attachments

def validate_image_safety(filepath: str) -> bool:
    """
    Basic safety validation for image files.
    
    Args:
        filepath: Path to the image file
        
    Returns:
        True if file appears safe, False otherwise
    """
    try:
        # Check file size (limit to 10MB)
        file_size = os.path.getsize(filepath)
        if file_size > 10 * 1024 * 1024:  # 10MB
            print(f"Warning: File {filepath} is too large ({file_size} bytes)")
            return False
        
        # Check if file is readable
        with open(filepath, 'rb') as f:
            # Try to read first few bytes
            header = f.read(1024)
            if len(header) == 0:
                print(f"Warning: File {filepath} appears to be empty")
                return False
        
        return True
        
    except Exception as e:
        print(f"Error validating file {filepath}: {e}")
        return False

def strip_exif_data(filepath: str) -> str:
    """
    Strip EXIF data from image files for privacy.
    
    Note: This is a placeholder implementation. 
    For production, implement using piexif or PIL.
    
    Args:
        filepath: Path to the image file
        
    Returns:
        Path to the processed file (may be the same as input)
    """
    # TODO: Implement EXIF stripping with piexif
    # For now, return the original file path
    print(f"📝 Note: EXIF stripping not yet implemented for {filepath}")
    return filepath

def get_image_description(attachment: Attachment) -> str:
    """
    Generate a description for the attachment to include in prompts.
    
    Args:
        attachment: The attachment object
        
    Returns:
        Human-readable description of the attachment
    """
    filename = os.path.basename(attachment.path)
    
    descriptions = {
        "Food": f"nutrition label or food-related image ({filename})",
        "MedLabel": f"medication label or prescription bottle ({filename})", 
        "Other": f"health-related image ({filename})"
    }
    
    return descriptions.get(attachment.tag, f"image file ({filename})")