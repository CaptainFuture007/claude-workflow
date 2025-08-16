"""
Quick test of the progress tracking system
"""

import asyncio
import sys
from pathlib import Path

# Add crawlers directory to path
sys.path.append(str(Path(__file__).parent))

from crawlers.ordered_crawler import OrderedCrawler


async def test_progress():
    """Test progress tracking with a quick crawl."""
    
    print("🧪 Testing progress tracking system...")
    
    # Configure the crawler for a quick test
    crawler = OrderedCrawler(
        root_url="https://docs.anthropic.com/en/docs/claude-code/",
        max_depth=0,  # Only crawl the root page
        output_dir="test_progress_output",
        max_concurrent=1,
        show_progress=True  # Enable progress bars
    )
    
    # Run the crawler
    results = await crawler.run()
    
    print("\n✅ Progress tracking test completed!")
    print(f"Duration: {results.get('duration', 'Unknown')}")
    
    # Check if files were created
    if results.get('stages', {}).get('stitching', {}).get('success'):
        print("📄 Stitched document created successfully!")
        
        # Copy to working directory
        source_file = Path(results['stages']['stitching']['output_file'])
        if source_file.exists():
            dest_file = Path("test_anthropic_docs_sample.md")
            dest_file.write_text(source_file.read_text(encoding='utf-8'), encoding='utf-8')
            print(f"📋 Sample saved to: {dest_file}")


if __name__ == "__main__":
    asyncio.run(test_progress())