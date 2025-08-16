"""
Script to crawl Anthropic Claude Code documentation
"""

import asyncio
import sys
from pathlib import Path

# Add crawlers directory to path
sys.path.append(str(Path(__file__).parent))

from crawlers.ordered_crawler import OrderedCrawler


async def crawl_anthropic_docs():
    """Crawl the Anthropic Claude Code documentation."""
    
    print("\n🚀 Starting crawl of Anthropic Claude Code documentation...")
    print("=" * 60)
    
    # Configure the crawler
    crawler = OrderedCrawler(
        root_url="https://docs.anthropic.com/en/docs/claude-code/",
        max_depth=1,  # Depth of 1 as requested
        output_dir="anthropic_docs_crawl",
        max_concurrent=1,  # Very conservative to be respectful to the server
        exclude_patterns=[
            "/api/",  # Skip API references if any
            "*.pdf",  # Skip PDF files
            "#"       # Skip anchor links
        ],
        extract_navigation=True,  # Extract the navigation structure
        create_stitched=True      # Create the stitched document
    )
    
    # Run the crawler
    results = await crawler.run()
    
    # Check if successful
    if results.get('stages', {}).get('stitching', {}).get('success'):
        print("\n✅ Crawl completed successfully!")
        
        # Copy the stitched document to the working directory
        source_file = Path(results['stages']['stitching']['output_file'])
        if source_file.exists():
            # Copy to working directory with descriptive name
            dest_file = Path("anthropic_claude_code_documentation.md")
            dest_file.write_text(source_file.read_text(encoding='utf-8'), encoding='utf-8')
            print(f"📄 Documentation saved to: {dest_file}")
            
            # Also copy the reading guide if it exists
            reading_guide = source_file.parent / "reading_guide.md"
            if reading_guide.exists():
                dest_guide = Path("anthropic_claude_code_reading_guide.md")
                dest_guide.write_text(reading_guide.read_text(encoding='utf-8'), encoding='utf-8')
                print(f"📖 Reading guide saved to: {dest_guide}")
        
        return results
    else:
        print("\n❌ Crawl failed. Check the logs for details.")
        return None


if __name__ == "__main__":
    # Run the crawler
    results = asyncio.run(crawl_anthropic_docs())
    
    if results:
        print("\n" + "=" * 60)
        print("📊 Crawl Statistics:")
        print("=" * 60)
        
        if 'crawling' in results.get('stages', {}):
            crawl_stats = results['stages']['crawling']
            print(f"Total pages crawled: {crawl_stats.get('total_crawled', 0)}")
            print(f"Successfully saved: {crawl_stats.get('successful', 0)}")
            print(f"Failed: {crawl_stats.get('failed', 0)}")
        
        print(f"\nDuration: {results.get('duration', 'Unknown')}")
        print("\n✨ Done! Check 'anthropic_claude_code_documentation.md' for the complete documentation.")