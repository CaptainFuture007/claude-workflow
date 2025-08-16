#!/usr/bin/env python3
"""
Script to concatenate all crawled Claude Code documentation pages into a single markdown file.
"""

import os
from pathlib import Path
from datetime import datetime
import re

def extract_title_from_content(content: str) -> str:
    """Extract the first H1 title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "Untitled"

def extract_url_from_frontmatter(content: str) -> str:
    """Extract URL from frontmatter."""
    if content.startswith('---'):
        frontmatter_end = content.find('---', 3)
        if frontmatter_end != -1:
            frontmatter = content[3:frontmatter_end]
            for line in frontmatter.split('\n'):
                if line.startswith('url:'):
                    return line.replace('url:', '').strip()
    return ""

def remove_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from content."""
    if content.startswith('---'):
        frontmatter_end = content.find('---', 3)
        if frontmatter_end != -1:
            return content[frontmatter_end + 3:].strip()
    return content.strip()

def create_concatenated_docs(content_dir: str, output_file: str = "claude_code_complete_documentation.md"):
    """
    Create a concatenated markdown file from all crawled documentation pages.
    
    Args:
        content_dir: Directory containing the crawled markdown files
        output_file: Output file name for the concatenated documentation
    """
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"❌ Error: Content directory {content_dir} does not exist")
        return
    
    # Get all markdown files
    md_files = list(content_path.glob("*.md"))
    
    if not md_files:
        print(f"❌ Error: No markdown files found in {content_dir}")
        return
    
    print(f"📚 Found {len(md_files)} markdown files to concatenate")
    
    # Sort files: main page first, then alphabetically
    main_file = None
    other_files = []
    
    for file in md_files:
        if "depth0_" in file.name:
            main_file = file
        else:
            other_files.append(file)
    
    # Sort other files alphabetically by filename
    other_files.sort(key=lambda x: x.name)
    
    # Prepare the concatenated content
    concatenated_content = []
    
    # Add header
    header = f"""# Claude Code Documentation - Complete Guide

**Generated**: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
**Source**: https://docs.anthropic.com/en/docs/claude-code/
**Total Pages**: {len(md_files)}

This document contains the complete Claude Code documentation concatenated from all individual pages for easy reading and searching.

---

"""
    concatenated_content.append(header)
    
    # Add table of contents
    toc_content = ["## Table of Contents\n"]
    
    # Process main file first
    if main_file:
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        title = extract_title_from_content(remove_frontmatter(content))
        url = extract_url_from_frontmatter(content)
        anchor = re.sub(r'[^a-zA-Z0-9\s]', '', title).lower().replace(' ', '-')
        toc_content.append(f"1. [{title}](#{anchor})")
        if url:
            toc_content.append(f"   - Source: {url}")
        toc_content.append("")
    
    # Add other files to TOC
    for i, file in enumerate(other_files, start=2):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        title = extract_title_from_content(remove_frontmatter(content))
        url = extract_url_from_frontmatter(content)
        anchor = re.sub(r'[^a-zA-Z0-9\s]', '', title).lower().replace(' ', '-')
        toc_content.append(f"{i}. [{title}](#{anchor})")
        if url:
            toc_content.append(f"   - Source: {url}")
        toc_content.append("")
    
    concatenated_content.extend(toc_content)
    concatenated_content.append("\n---\n")
    
    # Process main file content
    if main_file:
        print(f"📄 Processing main file: {main_file.name}")
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        clean_content = remove_frontmatter(content)
        url = extract_url_from_frontmatter(content)
        
        concatenated_content.append(f"\n<!-- Source: {url} -->\n")
        concatenated_content.append(clean_content)
        concatenated_content.append("\n\n---\n")
    
    # Process other files
    for file in other_files:
        print(f"📄 Processing: {file.name}")
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        clean_content = remove_frontmatter(content)
        url = extract_url_from_frontmatter(content)
        
        concatenated_content.append(f"\n<!-- Source: {url} -->\n")
        concatenated_content.append(clean_content)
        concatenated_content.append("\n\n---\n")
    
    # Write the concatenated file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(concatenated_content))
    
    print(f"\n✅ Concatenated documentation created!")
    print(f"📁 Output file: {output_path.absolute()}")
    print(f"📊 Total pages: {len(md_files)}")
    print(f"📏 File size: {output_path.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    # Use the latest crawl results
    content_directory = "claude_docs_final/content"
    output_filename = "claude_code_complete_documentation.md"
    
    create_concatenated_docs(content_directory, output_filename)