#!/usr/bin/env python3
"""
Multi-Input Document Processor CLI v2.0

Enhanced command-line interface supporting mixed input types (URLs, PDFs, markdown files)
with tuple-based ordering. Maintains backward compatibility with existing URL-only workflows.

Usage Examples:
    # Single URL (backward compatible)
    python multi_input_cli.py https://docs.anthropic.com/en/docs/claude-code/
    
    # Mixed input tuple
    python multi_input_cli.py \
        "https://docs.anthropic.com/en/docs/claude-code/" \
        "./research_paper.pdf" \
        "./notes.md" \
        "https://arxiv.org/pdf/2408.09869.pdf"
    
    # From file list
    python multi_input_cli.py --input-file inputs.txt
"""

import asyncio
import argparse
import sys
import json
from pathlib import Path
from typing import List, Tuple, Union
import logging

from multi_input_processor import create_multi_input_processor
from multi_input_types import detect_input_type, InputType


def setup_logging(verbose: bool = False) -> None:
    """Setup logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def parse_input_file(file_path: str) -> List[str]:
    """
    Parse input file containing one input per line.
    
    Args:
        file_path: Path to input file
        
    Returns:
        List of input strings
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If input file is empty or invalid
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    inputs = []
    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line and not line.startswith('#'):  # Skip empty lines and comments
                inputs.append(line)
    
    if not inputs:
        raise ValueError(f"No valid inputs found in file: {file_path}")
    
    return inputs


def validate_inputs(inputs: List[str]) -> List[Tuple[str, InputType]]:
    """
    Validate and analyze input list.
    
    Args:
        inputs: List of input strings
        
    Returns:
        List of (input_string, input_type) tuples
        
    Raises:
        ValueError: If inputs are invalid
    """
    if not inputs:
        raise ValueError("No inputs provided")
    
    if len(inputs) > 100:
        raise ValueError("Too many inputs (maximum 100)")
    
    validated = []
    for i, input_str in enumerate(inputs):
        if not input_str.strip():
            raise ValueError(f"Empty input at position {i + 1}")
        
        input_type = detect_input_type(input_str)
        validated.append((input_str, input_type))
    
    return validated


def print_input_summary(validated_inputs: List[Tuple[str, InputType]]) -> None:
    """Print summary of inputs to be processed."""
    print(f"\n📊 Processing {len(validated_inputs)} inputs:")
    
    type_counts = {}
    for input_str, input_type in validated_inputs:
        type_counts[input_type] = type_counts.get(input_type, 0) + 1
    
    for input_type, count in type_counts.items():
        icon = {"url": "🌐", "pdf": "📄", "markdown": "📝"}[input_type.value]
        print(f"   {icon} {input_type.value.title()}: {count}")
    
    print(f"\n📝 Input details:")
    for i, (input_str, input_type) in enumerate(validated_inputs, 1):
        icon = {"url": "🌐", "pdf": "📄", "markdown": "📝"}[input_type.value]
        source = Path(input_str).name if input_type != InputType.URL else input_str
        print(f"   {i:2d}. {icon} {source}")
    
    print()


def print_results_summary(stats: dict) -> None:
    """Print processing results summary."""
    print(f"\n🎉 Processing Complete!")
    print(f"   ✅ Successful: {stats['successful']}/{stats['total_inputs']}")
    print(f"   ❌ Failed: {stats['failed']}")
    print(f"   📊 Success Rate: {stats['success_rate']:.1%}")
    print(f"   ⏱️  Duration: {stats['duration_seconds']:.1f}s")
    print(f"   🚀 Speed: {stats['inputs_per_second']:.1f} inputs/second")
    
    if stats.get('results_by_type'):
        print(f"\n📋 Results by Type:")
        results = stats['results_by_type']
        if results.get('urls', 0) > 0:
            print(f"   🌐 URLs: {results['urls']}")
        if results.get('pdfs', 0) > 0:
            print(f"   📄 PDFs: {results['pdfs']}")
        if results.get('markdown', 0) > 0:
            print(f"   📝 Markdown: {results['markdown']}")
    
    print(f"\n📁 Output: {stats.get('concatenated_file', 'N/A')}")


def create_argument_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description='Multi-Input Document Processor v2.0 - Process URLs, PDFs, and Markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single URL (backward compatible)
  %(prog)s https://docs.anthropic.com/en/docs/claude-code/

  # Mixed input tuple  
  %(prog)s "https://docs.anthropic.com/" "./paper.pdf" "./notes.md"

  # From input file
  %(prog)s --input-file inputs.txt

  # With custom settings
  %(prog)s --output-dir ./results --max-concurrent 20 "url1" "file.pdf"

Input file format (one input per line):
  https://docs.anthropic.com/en/docs/claude-code/
  ./research_paper.pdf
  ./meeting_notes.md
  # Comments start with #
  https://arxiv.org/pdf/2408.09869.pdf
        """
    )
    
    # Input specification (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        'inputs',
        nargs='*',
        help='Input URLs, PDF files, or markdown files (in processing order)'
    )
    input_group.add_argument(
        '--input-file', '-f',
        metavar='FILE',
        help='File containing inputs (one per line)'
    )
    
    # Output configuration
    parser.add_argument(
        '--output-dir', '-o',
        default='multi_input_crawl',
        help='Output directory (default: multi_input_crawl)'
    )
    
    # Processing configuration
    parser.add_argument(
        '--max-concurrent', '-c',
        type=int,
        default=10,
        help='Maximum concurrent operations (default: 10)'
    )
    parser.add_argument(
        '--max-depth', '-d',
        type=int,
        default=2,
        help='Maximum crawl depth for URLs (default: 2)'
    )
    
    # Filtering options
    parser.add_argument(
        '--exclude', '-e',
        nargs='*',
        default=[],
        help='URL patterns to exclude'
    )
    
    # Output options
    parser.add_argument(
        '--no-progress',
        action='store_true',
        help='Disable progress indicators'
    )
    parser.add_argument(
        '--json-output',
        action='store_true',
        help='Output results as JSON'
    )
    
    # Debug options
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be processed without actually processing'
    )
    
    return parser


async def main() -> int:
    """Main CLI entry point."""
    parser = create_argument_parser()
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    
    try:
        # Parse inputs
        if args.input_file:
            inputs = parse_input_file(args.input_file)
        else:
            inputs = args.inputs
        
        if not inputs:
            print("❌ Error: No inputs provided", file=sys.stderr)
            parser.print_help()
            return 1
        
        # Validate inputs
        validated_inputs = validate_inputs(inputs)
        
        # Print input summary
        if not args.json_output:
            print_input_summary(validated_inputs)
        
        # Dry run - just show what would be processed
        if args.dry_run:
            print("🔍 Dry run mode - no actual processing will occur")
            return 0
        
        # Prepare input data
        if len(inputs) == 1:
            # Single input - maintain backward compatibility
            input_data = inputs[0]
        else:
            # Multiple inputs - tuple processing
            input_data = tuple(inputs)
        
        # Create processor
        processor = create_multi_input_processor(
            input_data=input_data,
            output_dir=args.output_dir,
            max_concurrent=args.max_concurrent,
            max_depth=args.max_depth,
            exclude_patterns=args.exclude,
            show_progress=not args.no_progress
        )
        
        # Process inputs
        if not args.json_output:
            print("🚀 Starting processing...")
        
        stats = await processor.crawl()
        
        # Clean up
        processor.cleanup()
        
        # Output results
        if args.json_output:
            print(json.dumps(stats, indent=2))
        else:
            print_results_summary(stats)
        
        # Return appropriate exit code
        success_rate = stats.get('success_rate', 0)
        if success_rate >= 0.8:  # 80% success rate threshold
            return 0
        elif success_rate >= 0.5:  # 50% success rate threshold
            return 1
        else:
            return 2  # High failure rate
            
    except KeyboardInterrupt:
        print("\n❌ Processing interrupted by user", file=sys.stderr)
        return 130
    except Exception as e:
        if args.verbose:
            import traceback
            traceback.print_exc()
        else:
            print(f"❌ Error: {e}", file=sys.stderr)
        return 1


def cli_main() -> None:
    """Entry point for console script."""
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    cli_main()