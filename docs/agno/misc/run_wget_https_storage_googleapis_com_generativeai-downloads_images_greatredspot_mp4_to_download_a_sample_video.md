---
title: Run: `wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4` to download a sample video
category: misc
source_lines: 42019-42029
line_count: 10
---

# Run: `wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4` to download a sample video
video_path = Path(__file__).parent.joinpath("samplevideo.mp4")
video_file = None
remote_file_name = f"files/{video_path.stem.lower().replace('_', '')}"
try:
    video_file = model.get_client().files.get(name=remote_file_name)
except Exception as e:
    logger.info(f"Error getting file {video_path.stem}: {e}")
    pass

