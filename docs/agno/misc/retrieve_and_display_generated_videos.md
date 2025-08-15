---
title: Retrieve and display generated videos
category: misc
source_lines: 36524-36530
line_count: 6
---

# Retrieve and display generated videos
videos = video_agent.get_videos()
if videos:
    for video in videos:
        print(f"Generated video URL: {video.url}")

