#!/usr/bin/env python3
"""
Script to analyze repetitive content in the concatenated documentation file.
"""

import re
from pathlib import Path
from collections import Counter

def analyze_repetitive_content(file_path: str):
    """Analyze the file for repetitive content patterns."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into sections by source comments
    sections = re.split(r'<!-- Source: .* -->', content)
    
    print(f"📊 Analysis of repetitive content in {file_path}")
    print(f"📄 Total sections found: {len(sections)}")
    print("\n" + "="*60)
    
    # 1. Check for navigation menu repetition
    nav_pattern = r'Navigation\s+Getting started.*?##### Resources.*?Legal and compliance'
    nav_matches = re.findall(nav_pattern, content, re.DOTALL)
    print(f"\n🔄 NAVIGATION MENU REPETITION:")
    print(f"   Found {len(nav_matches)} instances of full navigation menu")
    
    # 2. Check for repeated headers
    headers = re.findall(r'^# (.+)$', content, re.MULTILINE)
    header_counts = Counter(headers)
    duplicated_headers = {h: count for h, count in header_counts.items() if count > 1}
    
    print(f"\n📋 DUPLICATED HEADERS:")
    for header, count in duplicated_headers.items():
        print(f"   '{header}': appears {count} times")
    
    # 3. Check for repeated breadcrumb/navigation patterns
    breadcrumb_pattern = r'\[Welcome\].*?\[Release Notes\]'
    breadcrumb_matches = re.findall(breadcrumb_pattern, content)
    print(f"\n🍞 BREADCRUMB REPETITION:")
    print(f"   Found {len(breadcrumb_matches)} instances of breadcrumb navigation")
    
    # 4. Check for repeated footer/header elements
    anthropic_logo_pattern = r'Anthropic home page.*?dark\.svg\]\]'
    logo_matches = re.findall(anthropic_logo_pattern, content, re.DOTALL)
    print(f"\n🏠 HEADER/LOGO REPETITION:")
    print(f"   Found {len(logo_matches)} instances of Anthropic logo/header")
    
    # 5. Check for repeated search elements
    search_pattern = r'Search\.\.\.\s*⌘K'
    search_matches = re.findall(search_pattern, content)
    print(f"\n🔍 SEARCH ELEMENT REPETITION:")
    print(f"   Found {len(search_matches)} instances of search interface")
    
    # 6. Calculate potential space savings
    total_chars = len(content)
    
    # Estimate repetitive content size
    nav_size = sum(len(match) for match in nav_matches)
    breadcrumb_size = sum(len(match) for match in breadcrumb_matches)
    logo_size = sum(len(match) for match in logo_matches)
    search_size = sum(len(match) for match in search_matches)
    
    # Keep only one instance of each, remove the rest
    removable_size = (nav_size - (len(nav_matches[0]) if nav_matches else 0) +
                     breadcrumb_size - (len(breadcrumb_matches[0]) if breadcrumb_matches else 0) +
                     logo_size - (len(logo_matches[0]) if logo_matches else 0) +
                     search_size - (len(search_matches[0]) if search_matches else 0))
    
    print(f"\n💾 POTENTIAL SPACE SAVINGS:")
    print(f"   Current file size: {total_chars:,} characters")
    print(f"   Removable repetitive content: {removable_size:,} characters")
    print(f"   Potential size after cleanup: {total_chars - removable_size:,} characters")
    print(f"   Space savings: {(removable_size / total_chars) * 100:.1f}%")
    
    # 7. Identify specific repetitive patterns to remove
    print(f"\n🧹 RECOMMENDED CLEANUP ACTIONS:")
    
    if len(nav_matches) > 1:
        print(f"   ✂️  Remove {len(nav_matches) - 1} duplicate navigation menus")
    
    if len(breadcrumb_matches) > 1:
        print(f"   ✂️  Remove {len(breadcrumb_matches) - 1} duplicate breadcrumb navigations")
        
    if len(logo_matches) > 1:
        print(f"   ✂️  Remove {len(logo_matches) - 1} duplicate header/logo sections")
        
    if len(search_matches) > 1:
        print(f"   ✂️  Remove {len(search_matches) - 1} duplicate search interfaces")
    
    if duplicated_headers:
        print(f"   ✂️  Review and potentially merge duplicated content sections")
    
    print("\n" + "="*60)
    return {
        'nav_count': len(nav_matches),
        'breadcrumb_count': len(breadcrumb_matches),
        'logo_count': len(logo_matches),
        'search_count': len(search_matches),
        'duplicate_headers': duplicated_headers,
        'potential_savings': removable_size,
        'current_size': total_chars
    }

if __name__ == "__main__":
    file_path = "claude_code_complete_documentation.md"
    results = analyze_repetitive_content(file_path)