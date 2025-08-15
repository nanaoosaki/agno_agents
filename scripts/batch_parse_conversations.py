#!/usr/bin/env python3
"""
Batch ChatGPT Conversation Parser
Parses all HTML files in a directory using the ChatGPT conversation parser.

Usage:
    python scripts/batch_parse_conversations.py [directory_path]
"""

import sys
import os
import subprocess
from pathlib import Path
import glob


def find_html_files(directory):
    """Find all HTML files that look like ChatGPT conversation exports."""
    html_files = []
    
    # Look for files matching the pattern
    patterns = [
        "Migraine-Asthma-AcidReflux-Sleep Logger - daily log *.html",
        "*daily log*.html",
        "*conversation*.html"
    ]
    
    for pattern in patterns:
        search_path = Path(directory) / pattern
        matches = glob.glob(str(search_path))
        html_files.extend(matches)
    
    # Remove duplicates and sort
    html_files = sorted(list(set(html_files)))
    
    return html_files


def parse_single_conversation(html_file, parser_script):
    """Parse a single conversation file."""
    print(f"📄 Processing: {Path(html_file).name}")
    
    try:
        # Run the parser script
        result = subprocess.run(
            ["python", parser_script, html_file],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output to extract summary
        output_lines = result.stdout.split('\n')
        summary_info = {}
        
        for line in output_lines:
            if "Total turns:" in line:
                summary_info['total_turns'] = line.split(':')[1].strip()
            elif "User turns:" in line:
                summary_info['user_turns'] = line.split(':')[1].strip()
            elif "AI turns:" in line:
                summary_info['ai_turns'] = line.split(':')[1].strip()
        
        return {
            'success': True,
            'file': html_file,
            'summary': summary_info,
            'output': result.stdout
        }
        
    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'file': html_file,
            'error': e.stderr,
            'output': e.stdout
        }
    except Exception as e:
        return {
            'success': False,
            'file': html_file,
            'error': str(e),
            'output': ''
        }


def main():
    """Main function to batch parse conversations."""
    
    # Determine directory to search
    if len(sys.argv) >= 2:
        search_dir = sys.argv[1]
    else:
        search_dir = "linda_core/user_messages"
    
    if not Path(search_dir).exists():
        print(f"❌ Directory not found: {search_dir}")
        sys.exit(1)
    
    # Find the parser script
    parser_script = "scripts/parse_chatgpt_conversation.py"
    if not Path(parser_script).exists():
        print(f"❌ Parser script not found: {parser_script}")
        sys.exit(1)
    
    print(f"🔍 Searching for HTML files in: {search_dir}")
    
    # Find all HTML files
    html_files = find_html_files(search_dir)
    
    if not html_files:
        print(f"❌ No HTML files found in {search_dir}")
        sys.exit(1)
    
    print(f"📁 Found {len(html_files)} HTML files to process")
    print()
    
    # Process each file
    results = []
    successful = 0
    failed = 0
    
    for i, html_file in enumerate(html_files, 1):
        print(f"[{i}/{len(html_files)}] ", end="")
        result = parse_single_conversation(html_file, parser_script)
        results.append(result)
        
        if result['success']:
            successful += 1
            summary = result['summary']
            total = summary.get('total_turns', '?')
            user = summary.get('user_turns', '?')
            ai = summary.get('ai_turns', '?')
            print(f"✅ Success! Turns: {total} (User: {user}, AI: {ai})")
        else:
            failed += 1
            print(f"❌ Failed: {result.get('error', 'Unknown error')}")
        
        print()
    
    # Print final summary
    print("=" * 60)
    print(f"📊 BATCH PROCESSING COMPLETE")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Total files: {len(html_files)}")
    print()
    
    # List all generated JSON files
    if successful > 0:
        print("📄 Generated conversation files:")
        json_files = glob.glob(f"{search_dir}/*conversation*.json")
        for json_file in sorted(json_files):
            file_path = Path(json_file)
            size_kb = file_path.stat().st_size // 1024
            print(f"   - {file_path.name} ({size_kb}KB)")
    
    # Show any failures
    if failed > 0:
        print("\n❌ Failed files:")
        for result in results:
            if not result['success']:
                print(f"   - {Path(result['file']).name}: {result.get('error', 'Unknown error')}")


if __name__ == '__main__':
    main()