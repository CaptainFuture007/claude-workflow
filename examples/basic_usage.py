#!/usr/bin/env python3
"""
Basic Usage Examples for Multi-Input Document Processor v2.0

This file demonstrates various ways to use the Multi-Input Document Processor
for processing URLs, PDFs, and markdown files in different combinations.
"""

import asyncio
from pathlib import Path
from multi_input_processor import create_multi_input_processor


async def example_single_url():
    """
    Example 1: Single URL Processing (Backward Compatible)
    
    This works exactly like the original FastOrderedCrawler.
    """
    print("🔍 Example 1: Single URL Processing")
    
    processor = create_multi_input_processor(
        "https://docs.anthropic.com/en/docs/claude-code/",
        output_dir="example_single_url",
        max_concurrent=5
    )
    
    stats = await processor.crawl()
    processor.cleanup()
    
    print(f"✅ Processed {stats['successful']} page(s) in {stats['duration_seconds']:.1f}s")
    print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
    print()


async def example_mixed_inputs():
    """
    Example 2: Mixed Input Types
    
    Process a combination of URLs, PDFs, and markdown files in a specific order.
    """
    print("🔍 Example 2: Mixed Input Types")
    
    # Define inputs in the desired processing order
    inputs = (
        "https://docs.anthropic.com/en/docs/claude-code/overview",  # Web documentation
        "./examples/sample_documents/research_paper.pdf",          # PDF document
        "./examples/sample_documents/meeting_notes.md",            # Markdown file
        "https://arxiv.org/pdf/2408.09869.pdf"                    # PDF from URL
    )
    
    processor = create_multi_input_processor(
        inputs,
        output_dir="example_mixed_inputs",
        max_concurrent=10
    )
    
    try:
        stats = await processor.crawl()
        
        print(f"✅ Processed {stats['successful']}/{stats['total_inputs']} inputs")
        print(f"⏱️  Duration: {stats['duration_seconds']:.1f}s")
        print(f"🚀 Speed: {stats['inputs_per_second']:.1f} inputs/second")
        
        if stats.get('results_by_type'):
            results = stats['results_by_type']
            print(f"📊 Results: {results.get('urls', 0)} URLs, {results.get('pdfs', 0)} PDFs, {results.get('markdown', 0)} Markdown")
        
        print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        processor.cleanup()
    
    print()


async def example_pdf_only():
    """
    Example 3: PDF-Only Processing
    
    Process multiple PDF files (both local and from URLs).
    """
    print("🔍 Example 3: PDF-Only Processing")
    
    inputs = (
        "./examples/sample_documents/paper1.pdf",
        "./examples/sample_documents/paper2.pdf",
        "https://arxiv.org/pdf/2408.09869.pdf"
    )
    
    processor = create_multi_input_processor(
        inputs,
        output_dir="example_pdf_only",
        max_concurrent=3  # Lower concurrency for PDF processing
    )
    
    try:
        stats = await processor.crawl()
        
        print(f"✅ Processed {stats['successful']} PDF(s)")
        print(f"📄 Total PDFs: {stats['results_by_type'].get('pdfs', 0)}")
        print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        processor.cleanup()
    
    print()


async def example_markdown_compilation():
    """
    Example 4: Markdown File Compilation
    
    Compile multiple markdown files into a single document.
    """
    print("🔍 Example 4: Markdown File Compilation")
    
    inputs = (
        "./examples/sample_documents/introduction.md",
        "./examples/sample_documents/methodology.md",
        "./examples/sample_documents/results.md",
        "./examples/sample_documents/conclusion.md"
    )
    
    processor = create_multi_input_processor(
        inputs,
        output_dir="example_markdown_compilation"
    )
    
    try:
        stats = await processor.crawl()
        
        print(f"✅ Compiled {stats['successful']} markdown file(s)")
        print(f"📝 Total files: {stats['results_by_type'].get('markdown', 0)}")
        print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        processor.cleanup()
    
    print()


async def example_with_error_handling():
    """
    Example 5: Error Handling
    
    Demonstrate how the processor handles invalid inputs gracefully.
    """
    print("🔍 Example 5: Error Handling")
    
    inputs = (
        "https://docs.anthropic.com/en/docs/claude-code/",  # Valid URL
        "./nonexistent_file.pdf",                          # Invalid PDF
        "./examples/sample_documents/valid_notes.md",      # Valid markdown
        "https://invalid-url-that-doesnt-exist.com"        # Invalid URL
    )
    
    processor = create_multi_input_processor(
        inputs,
        output_dir="example_error_handling"
    )
    
    try:
        stats = await processor.crawl()
        
        print(f"✅ Successful: {stats['successful']}")
        print(f"❌ Failed: {stats['failed']}")
        print(f"📊 Success Rate: {stats['success_rate']:.1%}")
        print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
        print("💡 Check the output file to see how failed inputs are documented")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        processor.cleanup()
    
    print()


async def example_custom_configuration():
    """
    Example 6: Custom Configuration
    
    Demonstrate various configuration options.
    """
    print("🔍 Example 6: Custom Configuration")
    
    inputs = (
        "https://docs.anthropic.com/en/docs/claude-code/",
        "./examples/sample_documents/document.pdf"
    )
    
    processor = create_multi_input_processor(
        inputs,
        output_dir="example_custom_config",
        max_concurrent=20,           # High concurrency
        max_depth=3,                 # Deep crawling for URLs
        exclude_patterns=["blog", "news"],  # Exclude certain URL patterns
        show_progress=True           # Show progress indicators
    )
    
    try:
        stats = await processor.crawl()
        
        print(f"✅ Processed with custom configuration")
        print(f"📊 Results: {stats['successful']}/{stats['total_inputs']}")
        print(f"📁 Output: {stats.get('concatenated_file', 'N/A')}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        processor.cleanup()
    
    print()


def create_sample_documents():
    """
    Create sample documents for examples.
    """
    sample_dir = Path("examples/sample_documents")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Sample markdown files
    documents = {
        "meeting_notes.md": """# Team Meeting Notes

**Date**: August 16, 2025
**Attendees**: Development Team

## Agenda

1. Multi-Input Processor v2.0 Review
2. Performance Testing Results
3. Next Steps

## Key Points

- Successfully implemented mixed input processing
- Achieved >95% backward compatibility
- Performance targets met for all input types

## Action Items

- [ ] Complete documentation
- [ ] Finalize release notes
- [ ] Schedule deployment
""",
        "introduction.md": """# Introduction

This document serves as an introduction to the Multi-Input Document Processor.

## Overview

The Multi-Input Document Processor v2.0 extends the capabilities of FastOrderedCrawler
to support multiple input types while maintaining full backward compatibility.

## Key Features

- URL processing (web pages)
- PDF document conversion
- Markdown file compilation
- Tuple-based ordering
- Enhanced concatenation
""",
        "methodology.md": """# Methodology

## Approach

Our implementation follows a modular design pattern:

1. Input type detection
2. Specialized processors for each type
3. Unified result format
4. Order-preserving concatenation

## Technical Details

- Uses Docling for PDF processing
- Maintains FastOrderedCrawler performance
- Supports concurrent and sequential processing
""",
        "results.md": """# Results

## Performance Metrics

- URL Processing: 2.1+ pages/second
- PDF Processing: 1.0+ pages/second
- Markdown Processing: <0.1s per file
- Overall Success Rate: >95%

## Validation Results

All success criteria have been met:
✅ Mixed input processing
✅ Order preservation
✅ Backward compatibility
✅ Performance targets
""",
        "conclusion.md": """# Conclusion

The Multi-Input Document Processor v2.0 successfully achieves all project objectives:

## Summary

- Extended functionality without breaking changes
- High performance across all input types
- Robust error handling and validation
- Comprehensive test coverage

## Future Work

- Additional input formats (DOCX, PPTX)
- Cloud storage integration
- AI-enhanced processing
- Web-based interface
""",
        "valid_notes.md": """# Valid Notes

This is a valid markdown file for testing purposes.

## Content

- Point 1
- Point 2
- Point 3

## Summary

This file should process successfully.
"""
    }
    
    for filename, content in documents.items():
        file_path = sample_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"📁 Created sample documents in: {sample_dir}")


async def main():
    """
    Run all examples.
    """
    print("🚀 Multi-Input Document Processor v2.0 - Example Usage\n")
    
    # Create sample documents
    create_sample_documents()
    print()
    
    # Run examples
    examples = [
        example_single_url,
        example_mixed_inputs,
        example_pdf_only,
        example_markdown_compilation,
        example_with_error_handling,
        example_custom_configuration
    ]
    
    for example in examples:
        try:
            await example()
        except Exception as e:
            print(f"❌ Example failed: {e}")
            print()
    
    print("🎉 All examples completed!")
    print("\n💡 Tips:")
    print("- Check the output directories for generated files")
    print("- Review the concatenated documents to see the results")
    print("- Modify the inputs to test with your own content")


if __name__ == "__main__":
    asyncio.run(main())