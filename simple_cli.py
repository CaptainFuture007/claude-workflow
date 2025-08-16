#!/usr/bin/env python3
"""
Simple CLI for Multi-Input Document Processor

A streamlined command-line interface following KISS principles.
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Tuple

from simple_multi_processor import SimpleMultiProcessor


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Simple Multi-Input Document Processor - Process URLs, PDFs, and Markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single URL (backward compatible)
  python simple_cli.py https://docs.anthropic.com/en/docs/claude-code/

  # Mixed inputs
  python simple_cli.py "https://example.com" "./document.pdf" "./notes.md"

  # From input file
  python simple_cli.py --input-file inputs.txt

  # Custom output directory
  python simple_cli.py --output-dir ./results "https://example.com" "./doc.pdf"
        """
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        'inputs',
        nargs='*',
        help='Input URLs, PDF paths, or markdown paths'
    )
    input_group.add_argument(
        '--input-file', '-f',
        type=str,
        help='Text file containing one input per line'
    )
    
    # Configuration options
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default='./simple_output',
        help='Output directory (default: ./simple_output)'
    )
    parser.add_argument(
        '--max-concurrent', '-c',
        type=int,
        default=10,
        help='Maximum concurrent operations (default: 10)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be processed without actually processing'
    )
    
    return parser.parse_args()


def load_inputs_from_file(file_path: str) -> Tuple[str, ...]:
    """Load inputs from text file."""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out empty lines and comments
    inputs = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            inputs.append(line)
    
    if not inputs:
        raise ValueError(f"No valid inputs found in file: {file_path}")
    
    return tuple(inputs)


def print_processing_summary(inputs: Tuple[str, ...]):
    """Print what will be processed."""
    print(f"\n📋 Processing Summary:")
    print(f"   Total inputs: {len(inputs)}")
    
    from simple_input_types import detect_input_type
    
    type_counts = {"url": 0, "pdf": 0, "markdown": 0}
    
    for i, input_str in enumerate(inputs, 1):
        input_type = detect_input_type(input_str)
        type_counts[input_type] += 1
        
        icon = {"url": "🌐", "pdf": "📄", "markdown": "📝"}[input_type]
        print(f"   {i:2d}. {icon} {input_type:8s} {input_str}")
    
    print(f"\n📊 Input breakdown:")
    for input_type, count in type_counts.items():
        if count > 0:
            icon = {"url": "🌐", "pdf": "📄", "markdown": "📝"}[input_type]
            print(f"   {icon} {input_type.title()}: {count}")


async def main():
    """Main CLI function."""
    args = parse_args()
    
    try:
        # Get inputs
        if args.input_file:
            inputs = load_inputs_from_file(args.input_file)
            print(f"📁 Loaded {len(inputs)} inputs from: {args.input_file}")
        else:
            if not args.inputs:
                print("❌ Error: No inputs provided")
                sys.exit(1)
            inputs = tuple(args.inputs)
        
        # Print summary
        print_processing_summary(inputs)
        
        # Dry run - just show what would be processed
        if args.dry_run:
            print(f"\n🔍 Dry run complete. Would output to: {args.output_dir}")
            return
        
        # Initialize processor
        processor = SimpleMultiProcessor(
            output_dir=args.output_dir,
            max_concurrent=args.max_concurrent
        )
        
        print(f"\n🚀 Starting processing...")
        print(f"   Output directory: {args.output_dir}")
        print(f"   Max concurrent: {args.max_concurrent}")
        
        try:
            # Process inputs
            result = await processor.process_inputs(inputs)
            
            if result['success']:
                stats = result['stats']
                print(f"\n✅ Processing completed successfully!")
                print(f"   Processed: {stats['successful']}/{stats['total_inputs']} inputs")
                print(f"   Duration: {stats['duration_seconds']}s")
                print(f"   Speed: {stats['inputs_per_second']} inputs/second")
                
                if stats['concatenated_file']:
                    print(f"   📄 Concatenated document: {stats['concatenated_file']}")
                
                if stats['failed_inputs']:
                    print(f"\n⚠️  Failed inputs:")
                    for failed in stats['failed_inputs']:
                        print(f"   ❌ Position {failed['position']}: {failed['input']}")
                        if args.verbose:
                            print(f"      Error: {failed['error']}")
                
                print(f"\n📁 Output directory: {stats['output_directory']}")
                
            else:
                print(f"❌ Processing failed: {result.get('error', 'Unknown error')}")
                sys.exit(1)
                
        finally:
            processor.cleanup()
            
    except KeyboardInterrupt:
        print("\n🛑 Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if args.verbose:
            import traceback
            print(f"\nFull traceback:")
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())