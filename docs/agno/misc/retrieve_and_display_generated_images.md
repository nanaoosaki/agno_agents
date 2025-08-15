---
title: Retrieve and display generated images
category: misc
source_lines: 35289-35296
line_count: 7
---

# Retrieve and display generated images
images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(f"Generated image URL: {image_url}")

