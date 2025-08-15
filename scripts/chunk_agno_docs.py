#!/usr/bin/env python3
"""
Agno Documentation Chunker
Splits the large llms-full.txt file into organized, searchable chunks.

Usage:
    python scripts/chunk_agno_docs.py
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple


def extract_sections(content: str) -> List[Dict[str, any]]:
    """
    Extract sections from the Agno documentation based on headers.
    Returns list of sections with metadata.
    """
    lines = content.split('\n')
    sections = []
    current_section = None
    current_content = []
    line_number = 0
    
    for i, line in enumerate(lines, 1):
        line_number = i
        
        # Detect main headers (# Title)
        if line.startswith('# ') and not line.startswith('## '):
            # Save previous section
            if current_section:
                current_section['content'] = '\n'.join(current_content)
                current_section['line_count'] = len(current_content)
                sections.append(current_section)
            
            # Start new section
            title = line[2:].strip()
            safe_filename = re.sub(r'[^\w\-_]', '_', title.lower())
            safe_filename = re.sub(r'_+', '_', safe_filename).strip('_')
            
            current_section = {
                'title': title,
                'filename': f"{safe_filename}.md",
                'start_line': line_number,
                'level': 1
            }
            current_content = [line]
        
        # Detect sub-headers (## Subtitle)
        elif line.startswith('## ') and current_section:
            current_content.append(line)
        
        # Regular content
        else:
            if current_section:
                current_content.append(line)
    
    # Don't forget the last section
    if current_section:
        current_section['content'] = '\n'.join(current_content)
        current_section['line_count'] = len(current_content)
        sections.append(current_section)
    
    return sections


def create_chunked_files(sections: List[Dict], output_dir: Path):
    """Create individual markdown files for each section."""
    
    # Create main categories
    categories = {
        'core': ['agent_api', 'what_are_agents', 'running_your_agent', 'sessions'],
        'ui': ['a_beautiful_ui_for_your_agents', 'get_started_with_agent_ui'],
        'knowledge': ['knowledge', 'chunking', 'memory'],
        'multimodal': ['multimodal_agents'],
        'tools': ['tools', 'reasoning_tools'],
        'integrations': ['integrations'],
        'metrics': ['metrics'],
        'advanced': ['context', 'prompts', 'streaming']
    }
    
    # Create category directories
    for category in categories.keys():
        (output_dir / category).mkdir(exist_ok=True)
    
    # Create index file
    index_content = []
    index_content.append("# Agno Documentation Index\n")
    index_content.append("*Generated from llms-full.txt*\n")
    
    categorized_sections = {cat: [] for cat in categories.keys()}
    uncategorized = []
    
    for section in sections:
        filename_lower = section['filename'].lower()
        categorized = False
        
        for category, keywords in categories.items():
            if any(keyword in filename_lower for keyword in keywords):
                categorized_sections[category].append(section)
                categorized = True
                break
        
        if not categorized:
            uncategorized.append(section)
    
    # Write categorized sections
    for category, sections_list in categorized_sections.items():
        if sections_list:
            index_content.append(f"\n## {category.title()}\n")
            
            for section in sections_list:
                file_path = output_dir / category / section['filename']
                
                # Add metadata header to each file
                content = f"""---
title: {section['title']}
category: {category}
source_lines: {section['start_line']}-{section['start_line'] + section['line_count']}
line_count: {section['line_count']}
---

{section['content']}
"""
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                index_content.append(f"- [{section['title']}]({category}/{section['filename']}) (lines {section['start_line']}-{section['start_line'] + section['line_count']})")
    
    # Handle uncategorized sections
    if uncategorized:
        misc_dir = output_dir / 'misc'
        misc_dir.mkdir(exist_ok=True)
        index_content.append(f"\n## Miscellaneous\n")
        
        for section in uncategorized:
            file_path = misc_dir / section['filename']
            
            content = f"""---
title: {section['title']}
category: misc
source_lines: {section['start_line']}-{section['start_line'] + section['line_count']}
line_count: {section['line_count']}
---

{section['content']}
"""
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            index_content.append(f"- [{section['title']}](misc/{section['filename']}) (lines {section['start_line']}-{section['start_line'] + section['line_count']})")
    
    # Write index file
    with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))


def create_quick_reference(sections: List[Dict], output_dir: Path):
    """Create a quick reference guide with common patterns."""
    
    # Extract code patterns
    patterns = {
        'Agent Creation': [],
        'Knowledge Bases': [],
        'Chunking Strategies': [],
        'Vector Databases': [],
        'Tools': [],
        'Memory': []
    }
    
    for section in sections:
        content = section['content']
        title = section['title']
        
        # Look for specific patterns
        if 'from agno.agent import Agent' in content:
            patterns['Agent Creation'].append((title, section['filename']))
        
        if 'Knowledge' in title or 'knowledge' in content.lower():
            patterns['Knowledge Bases'].append((title, section['filename']))
        
        if 'chunking' in title.lower() or 'Chunking' in content:
            patterns['Chunking Strategies'].append((title, section['filename']))
        
        if 'vector' in title.lower() or 'PgVector' in content:
            patterns['Vector Databases'].append((title, section['filename']))
        
        if 'tools' in title.lower() or 'ReasoningTools' in content:
            patterns['Tools'].append((title, section['filename']))
        
        if 'memory' in title.lower() or 'Memory' in content:
            patterns['Memory'].append((title, section['filename']))
    
    # Create quick reference
    quick_ref = ["# Agno Quick Reference\n", "*Most commonly used patterns and APIs*\n"]
    
    for pattern_name, matches in patterns.items():
        if matches:
            quick_ref.append(f"\n## {pattern_name}\n")
            for title, filename in matches:
                # Determine category from filename structure
                if '/' in filename:
                    category = filename.split('/')[0]
                else:
                    category = 'misc'
                quick_ref.append(f"- [{title}]({category}/{filename})")
    
    with open(output_dir / 'quick_reference.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(quick_ref))


def main():
    """Main function to chunk the Agno documentation."""
    
    # Paths
    source_file = Path('docs/llms-full.txt')
    output_dir = Path('docs/agno')
    
    if not source_file.exists():
        print(f"Error: {source_file} not found!")
        return
    
    print("🔍 Reading Agno documentation...")
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 Source file: {len(content)} characters, {len(content.splitlines())} lines")
    
    print("✂️  Extracting sections...")
    sections = extract_sections(content)
    print(f"📝 Found {len(sections)} sections")
    
    print("📁 Creating chunked files...")
    create_chunked_files(sections, output_dir)
    
    print("⚡ Creating quick reference...")
    create_quick_reference(sections, output_dir)
    
    print(f"✅ Done! Chunked documentation available in: {output_dir}")
    print(f"📖 Start with: {output_dir}/index.md")
    print(f"🚀 Quick patterns: {output_dir}/quick_reference.md")


if __name__ == '__main__':
    main()