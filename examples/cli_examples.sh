#!/bin/bash
#
# CLI Examples for Multi-Input Document Processor v2.0
#
# This script demonstrates various command-line usage patterns for the
# Multi-Input Document Processor. Each example shows different features
# and configuration options.
#

echo "🚀 Multi-Input Document Processor v2.0 - CLI Examples"
echo "======================================================"
echo

# Create sample input file for examples
cat > examples_input.txt << 'EOF'
# Sample input file for CLI examples
https://docs.anthropic.com/en/docs/claude-code/overview
./examples/sample_documents/meeting_notes.md
https://docs.anthropic.com/en/docs/claude-code/quickstart
./examples/sample_documents/introduction.md
EOF

echo "📝 Created sample input file: examples_input.txt"
echo

# Example 1: Single URL (Backward Compatible)
echo "🔍 Example 1: Single URL Processing"
echo "Command: python multi_input_cli.py https://docs.anthropic.com/en/docs/claude-code/"
echo "This works exactly like the original FastOrderedCrawler."
echo
# python multi_input_cli.py https://docs.anthropic.com/en/docs/claude-code/
echo "✅ Would process single URL with default settings"
echo

# Example 2: Multiple URLs
echo "🔍 Example 2: Multiple URL Processing"
echo 'Command: python multi_input_cli.py \
    "https://docs.anthropic.com/en/docs/claude-code/" \
    "https://docs.anthropic.com/en/docs/claude-code/quickstart"'
echo
# python multi_input_cli.py \
#     "https://docs.anthropic.com/en/docs/claude-code/" \
#     "https://docs.anthropic.com/en/docs/claude-code/quickstart"
echo "✅ Would process multiple URLs in sequence"
echo

# Example 3: Mixed Input Types
echo "🔍 Example 3: Mixed Input Types"
echo 'Command: python multi_input_cli.py \
    "https://docs.anthropic.com/en/docs/claude-code/" \
    "./examples/sample_documents/meeting_notes.md" \
    "https://docs.anthropic.com/en/docs/claude-code/quickstart"'
echo
# python multi_input_cli.py \
#     "https://docs.anthropic.com/en/docs/claude-code/" \
#     "./examples/sample_documents/meeting_notes.md" \
#     "https://docs.anthropic.com/en/docs/claude-code/quickstart"
echo "✅ Would process URLs and markdown files in specified order"
echo

# Example 4: Input from File
echo "🔍 Example 4: Input from File"
echo "Command: python multi_input_cli.py --input-file examples_input.txt"
echo
# python multi_input_cli.py --input-file examples_input.txt
echo "✅ Would process all inputs listed in the file"
echo

# Example 5: Custom Output Directory
echo "🔍 Example 5: Custom Output Directory"
echo 'Command: python multi_input_cli.py \
    --output-dir ./my_custom_results \
    "https://docs.anthropic.com/en/docs/claude-code/"'
echo
# python multi_input_cli.py \
#     --output-dir ./my_custom_results \
#     "https://docs.anthropic.com/en/docs/claude-code/"
echo "✅ Would save results to custom directory"
echo

# Example 6: High Concurrency
echo "🔍 Example 6: High Concurrency Processing"
echo 'Command: python multi_input_cli.py \
    --max-concurrent 25 \
    --output-dir ./fast_results \
    "https://docs.anthropic.com/en/docs/claude-code/" \
    "https://docs.anthropic.com/en/docs/claude-code/quickstart" \
    "https://docs.anthropic.com/en/docs/claude-code/overview"'
echo
# python multi_input_cli.py \
#     --max-concurrent 25 \
#     --output-dir ./fast_results \
#     "https://docs.anthropic.com/en/docs/claude-code/" \
#     "https://docs.anthropic.com/en/docs/claude-code/quickstart" \
#     "https://docs.anthropic.com/en/docs/claude-code/overview"
echo "✅ Would process with high concurrency for maximum speed"
echo

# Example 7: Deep Crawling with Exclusions
echo "🔍 Example 7: Deep Crawling with Exclusions"
echo 'Command: python multi_input_cli.py \
    --max-depth 3 \
    --exclude "blog" "news" "archive" \
    --output-dir ./deep_crawl \
    "https://docs.anthropic.com/en/docs/claude-code/"'
echo
# python multi_input_cli.py \
#     --max-depth 3 \
#     --exclude "blog" "news" "archive" \
#     --output-dir ./deep_crawl \
#     "https://docs.anthropic.com/en/docs/claude-code/"
echo "✅ Would crawl deeply while excluding specified patterns"
echo

# Example 8: Verbose Output
echo "🔍 Example 8: Verbose Output"
echo 'Command: python multi_input_cli.py \
    --verbose \
    --output-dir ./verbose_results \
    "./examples/sample_documents/meeting_notes.md"'
echo
# python multi_input_cli.py \
#     --verbose \
#     --output-dir ./verbose_results \
#     "./examples/sample_documents/meeting_notes.md"
echo "✅ Would show detailed processing information"
echo

# Example 9: JSON Output
echo "🔍 Example 9: JSON Output for Integration"
echo 'Command: python multi_input_cli.py \
    --json-output \
    --output-dir ./json_results \
    "https://docs.anthropic.com/en/docs/claude-code/" > results.json'
echo
# python multi_input_cli.py \
#     --json-output \
#     --output-dir ./json_results \
#     "https://docs.anthropic.com/en/docs/claude-code/" > results.json
echo "✅ Would output machine-readable JSON results"
echo

# Example 10: Dry Run
echo "🔍 Example 10: Dry Run (Preview Mode)"
echo 'Command: python multi_input_cli.py \
    --dry-run \
    --input-file examples_input.txt'
echo
# python multi_input_cli.py \
#     --dry-run \
#     --input-file examples_input.txt
echo "✅ Would show what would be processed without actually processing"
echo

# Example 11: No Progress Indicators
echo "🔍 Example 11: Quiet Mode (No Progress)"
echo 'Command: python multi_input_cli.py \
    --no-progress \
    --output-dir ./quiet_results \
    "https://docs.anthropic.com/en/docs/claude-code/"'
echo
# python multi_input_cli.py \
#     --no-progress \
#     --output-dir ./quiet_results \
#     "https://docs.anthropic.com/en/docs/claude-code/"
echo "✅ Would process without showing progress indicators"
echo

# Example 12: Complete Configuration
echo "🔍 Example 12: Complete Configuration Example"
echo 'Command: python multi_input_cli.py \
    --input-file examples_input.txt \
    --output-dir ./complete_example \
    --max-concurrent 15 \
    --max-depth 2 \
    --exclude "blog" "comments" \
    --verbose \
    --json-output > complete_results.json'
echo
# python multi_input_cli.py \
#     --input-file examples_input.txt \
#     --output-dir ./complete_example \
#     --max-concurrent 15 \
#     --max-depth 2 \
#     --exclude "blog" "comments" \
#     --verbose \
#     --json-output > complete_results.json
echo "✅ Would use all available options for comprehensive processing"
echo

# Help and Information
echo "🔍 Getting Help"
echo "Command: python multi_input_cli.py --help"
echo "Shows all available options and usage examples."
echo

# Cleanup
echo "🧹 Cleaning up example files..."
rm -f examples_input.txt
echo

echo "💡 Usage Tips:"
echo "  • Use quotes around URLs to prevent shell interpretation"
echo "  • Input files support comments (lines starting with #)"
echo "  • JSON output is perfect for integrating with other tools"
echo "  • Dry run mode helps validate inputs before processing"
echo "  • Adjust concurrency based on your system capabilities"
echo

echo "📚 For more examples, see:"
echo "  • examples/basic_usage.py - Python API examples"
echo "  • README.md - Complete documentation"
echo "  • tests/ - Test files with usage patterns"
echo

echo "🎉 CLI Examples Complete!"
echo "Run any of the above commands to see the processor in action."