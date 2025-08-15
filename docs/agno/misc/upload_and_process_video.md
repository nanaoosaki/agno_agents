---
title: Upload and process video
category: misc
source_lines: 19399-19405
line_count: 6
---

# Upload and process video
video_file = upload_file(video_path)
while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = get_file(video_file.name)

