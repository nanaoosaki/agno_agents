---
title: Define the structured message data
category: misc
source_lines: 56099-56109
line_count: 10
---

# Define the structured message data
class MediaRequest(BaseModel):
    topic: str
    content_type: str  # "image" or "video"
    prompt: str
    style: Optional[str] = "realistic"
    duration: Optional[int] = None  # For video, duration in seconds
    resolution: Optional[str] = "1024x1024"  # For image resolution


