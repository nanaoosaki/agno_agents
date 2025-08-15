---
title: Create output directory
category: misc
source_lines: 19437-19441
line_count: 4
---

# Create output directory
output_dir = Path(output_dir)
output_dir.mkdir(parents=True, exist_ok=True)

