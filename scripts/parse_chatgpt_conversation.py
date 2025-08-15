#!/usr/bin/env python3
"""
Final ChatGPT History Parser
Correctly extracts conversation turns based on <article> elements.

Usage:
    python scripts/parse_chatgpt_final.py <html_file> [output_file]
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup


def clean_text_content(text):
    """Clean and format text content."""
    if not text:
        return ""
    
    # Remove excessive whitespace and normalize
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def extract_conversation_from_articles(html_content):
    """
    Extract conversation turns based on <article> elements.
    Each article represents one complete conversation turn.
    """
    print("Parsing HTML with BeautifulSoup...")
    
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return []
    
    # Find all article elements that represent conversation turns
    articles = soup.find_all('article', {'data-testid': re.compile(r'conversation-turn-\d+')})
    
    print(f"Found {len(articles)} conversation articles")
    
    messages = []
    
    for i, article in enumerate(articles):
        try:
            # Determine if this is user or AI turn
            turn_type = article.get('data-turn', '')
            
            # Extract the actual content
            content_text = ""
            
            if turn_type == 'user':
                # User messages - look for the bubble content
                user_bubble = article.find('div', class_='user-message-bubble-color')
                if user_bubble:
                    content_text = clean_text_content(user_bubble.get_text())
                else:
                    # Fallback - get all text from the article
                    content_text = clean_text_content(article.get_text())
                
                role = 'user'
                
            elif turn_type == 'assistant':
                # AI messages - get all content from the markdown prose area
                prose_div = article.find('div', class_='markdown prose dark:prose-invert w-full break-words light markdown-new-styling')
                if prose_div:
                    content_text = clean_text_content(prose_div.get_text())
                else:
                    # Fallback - get all text from the article
                    content_text = clean_text_content(article.get_text())
                
                role = 'ai'
            else:
                # Unknown turn type - skip
                continue
            
            # Skip empty messages
            if not content_text or len(content_text.strip()) < 5:
                continue
            
            # Clean up common UI elements that might leak through
            content_text = re.sub(r'You said:|ChatGPT said:|Copy|Good response|Bad response|Read aloud|Edit|Copy Table', '', content_text)
            content_text = re.sub(r'\s+', ' ', content_text).strip()
            
            if content_text and len(content_text) > 10:  # Ensure substantial content
                message = {
                    'role': role,
                    'content': content_text,
                    'turn_type': turn_type,
                    'article_index': i,
                    'extraction_method': 'article_parsing'
                }
                
                messages.append(message)
                print(f"  Turn {i+1}: [{role.upper()}] {content_text[:100]}...")
        
        except Exception as e:
            print(f"  WARNING: Error processing article {i}: {e}")
            continue
    
    print(f"Successfully extracted {len(messages)} conversation turns")
    return messages


def format_conversation_json(messages, source_info):
    """Format the conversation into a structured JSON format."""
    
    conversation = {
        'metadata': {
            'source': source_info.get('type', 'html_file'),
            'file_path': source_info.get('file_path'),
            'extracted_at': datetime.now().isoformat(),
            'total_messages': len(messages),
            'user_messages': len([m for m in messages if m['role'] == 'user']),
            'ai_messages': len([m for m in messages if m['role'] == 'ai']),
            'extraction_method': 'article_parsing',
            'parser_version': 'final_v1'
        },
        'messages': []
    }
    
    # Process and clean messages
    for i, msg in enumerate(messages):
        formatted_msg = {
            'index': i,
            'role': msg['role'],
            'content': msg['content'],
            'timestamp': None,
            'message_id': f"turn_{msg.get('article_index', i)}",
            'word_count': len(msg['content'].split()) if msg['content'] else 0,
            'char_count': len(msg['content']) if msg['content'] else 0,
            'extraction_method': msg.get('extraction_method', 'article_parsing'),
            'turn_type': msg.get('turn_type', 'unknown')
        }
        
        conversation['messages'].append(formatted_msg)
    
    return conversation


def main():
    """Main function to parse ChatGPT conversation with correct article-based parsing."""
    
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_chatgpt_final.py <html_file> [output_file]")
        print("Example: python scripts/parse_chatgpt_final.py conversation.html")
        sys.exit(1)
    
    html_file = Path(sys.argv[1])
    
    if not html_file.exists():
        print(f"❌ File not found: {html_file}")
        sys.exit(1)
    
    # Determine output file
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = html_file.parent / f"{html_file.stem}_conversation_final.json"
    
    try:
        # Read HTML file
        print(f"Reading HTML file: {html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract conversation turns
        messages = extract_conversation_from_articles(html_content)
        
        if not messages:
            print("No conversation turns found in the HTML file")
            sys.exit(1)
        
        # Format conversation
        source_info = {
            'type': 'html_file',
            'file_path': str(html_file)
        }
        
        conversation_data = format_conversation_json(messages, source_info)
        
        # Save to file
        print(f"Saving conversation to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(conversation_data, f, indent=2, ensure_ascii=False)
        
        # Print summary
        metadata = conversation_data['metadata']
        print(f"SUCCESS: Conversation saved!")
        print(f"Summary:")
        print(f"   - Total turns: {metadata['total_messages']}")
        print(f"   - User turns: {metadata['user_messages']}")
        print(f"   - AI turns: {metadata['ai_messages']}")
        print(f"   - Parser version: {metadata['parser_version']}")
    
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()