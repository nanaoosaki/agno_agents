---
title: --- PDF utility ---
category: misc
source_lines: 57756-57768
line_count: 12
---

# --- PDF utility ---
def extract_text_from_pdf(url: str) -> str:
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        reader = PdfReader(io.BytesIO(resp.content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        print(f"Error extracting PDF from {url}: {e}")
        return ""


