#!/usr/bin/env python3
"""
PDF to Markdown Converter
Extracts all text from a PDF file and converts it to markdown format.

Usage:
    python scripts/pdf_to_markdown.py <pdf_path> [output_path]
"""

import sys
import fitz  # PyMuPDF
from pathlib import Path
import re


def clean_text(text):
    """Clean and format extracted text."""
    # Remove excessive whitespace while preserving paragraph breaks
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    # Remove trailing whitespace from lines
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    # Fix common PDF extraction issues
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between camelCase
    return text.strip()


def extract_text_from_pdf(pdf_path):
    """Extract all text from PDF file."""
    doc = fitz.open(pdf_path)
    full_text = []
    
    print(f"📄 Processing PDF: {pdf_path}")
    print(f"📝 Total pages: {len(doc)}")
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        if text.strip():  # Only add non-empty pages
            # Add page marker
            full_text.append(f"\n---\n**Page {page_num + 1}**\n---\n")
            full_text.append(clean_text(text))
            print(f"✅ Extracted page {page_num + 1}")
        else:
            print(f"⚠️  Page {page_num + 1} appears to be empty")
    
    doc.close()
    return '\n\n'.join(full_text)


def convert_to_markdown(text, title="Migraine Headache Megahandout"):
    """Convert extracted text to markdown format."""
    
    # Create markdown header
    markdown_content = [
        f"# {title}",
        "",
        "*Extracted from PDF document*",
        "",
        "---",
        "",
    ]
    
    # Split text into sections and try to identify headers
    lines = text.split('\n')
    current_section = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines at the beginning of sections
        if not line and not current_section:
            continue
            
        # Detect potential headers (all caps, short lines, etc.)
        if line and len(line) < 100 and (
            line.isupper() or 
            line.endswith(':') or
            re.match(r'^[A-Z][A-Z\s&-]+$', line)
        ):
            # Add previous section
            if current_section:
                markdown_content.extend(current_section)
                markdown_content.append("")
                current_section = []
            
            # Add header
            if not line.startswith('**Page'):
                markdown_content.append(f"## {line}")
                markdown_content.append("")
            else:
                markdown_content.append(line)  # Keep page markers as-is
                markdown_content.append("")
        else:
            current_section.append(line)
    
    # Add final section
    if current_section:
        markdown_content.extend(current_section)
    
    return '\n'.join(markdown_content)


def main():
    """Main function to convert PDF to markdown."""
    
    if len(sys.argv) < 2:
        print("Usage: python scripts/pdf_to_markdown.py <pdf_path> [output_path]")
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    # Determine output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        # Same directory as PDF, with .md extension
        output_path = pdf_path.with_suffix('.md')
    
    try:
        # Extract text from PDF
        print("🔍 Extracting text from PDF...")
        extracted_text = extract_text_from_pdf(pdf_path)
        
        if not extracted_text.strip():
            print("❌ No text found in PDF!")
            sys.exit(1)
        
        # Convert to markdown
        print("📝 Converting to markdown...")
        markdown_content = convert_to_markdown(
            extracted_text, 
            title=pdf_path.stem.replace('_', ' ').replace('-', ' ').title()
        )
        
        # Save markdown file
        print(f"💾 Saving to: {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # Show statistics
        char_count = len(markdown_content)
        word_count = len(markdown_content.split())
        line_count = len(markdown_content.split('\n'))
        
        print(f"✅ Conversion complete!")
        print(f"📊 Statistics:")
        print(f"   - Characters: {char_count:,}")
        print(f"   - Words: {word_count:,}")
        print(f"   - Lines: {line_count:,}")
        print(f"📁 Output file: {output_path}")
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()