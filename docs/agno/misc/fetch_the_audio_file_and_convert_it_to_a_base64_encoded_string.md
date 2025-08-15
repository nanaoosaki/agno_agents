---
title: Fetch the audio file and convert it to a base64 encoded string
category: misc
source_lines: 46418-46424
line_count: 6
---

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()
wav_data = response.content

