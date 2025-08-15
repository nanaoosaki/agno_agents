---
title: Extract and cut video segments
category: misc
source_lines: 19441-19491
line_count: 50
---

# Extract and cut video segments
def extract_segments(response_text):
    import re

    segments_pattern = r"\|\s*(\d+:\d+)\s*\|\s*(\d+:\d+)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|"
    segments: list[dict] = []

    for match in re.finditer(segments_pattern, str(response_text)):
        start_time = match.group(1)
        end_time = match.group(2)
        description = match.group(3)
        score = int(match.group(4))

        start_seconds = sum(x * int(t) for x, t in zip([60, 1], start_time.split(":")))
        end_seconds = sum(x * int(t) for x, t in zip([60, 1], end_time.split(":")))
        duration = end_seconds - start_seconds

        if 15 <= duration <= 60 and score > 7:
            output_path = output_dir / f"short_{len(segments) + 1}.mp4"

            command = [
                "ffmpeg",
                "-ss",
                str(start_seconds),
                "-i",
                video_path,
                "-t",
                str(duration),
                "-vf",
                "scale=1080:1920,setsar=1:1",
                "-c:v",
                "libx264",
                "-c:a",
                "aac",
                "-y",
                str(output_path),
            ]

            try:
                subprocess.run(command, check=True)
                segments.append(
                    {"path": output_path, "description": description, "score": score}
                )
            except subprocess.CalledProcessError:
                print(f"Failed to process segment: {start_time} - {end_time}")

    return segments

logger.debug(f"{response.content}")

