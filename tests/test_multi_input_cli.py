"""
Tests for multi_input_cli module

Tests the CLI interface and argument parsing functionality.
"""

import pytest
import tempfile
import os
import json
from pathlib import Path
from unittest.mock import patch, AsyncMock, Mock
from io import StringIO

from multi_input_cli import (
    parse_input_file, validate_inputs, create_argument_parser,
    print_input_summary, print_results_summary
)
from multi_input_types import InputType


class TestParseInputFile:
    """Test input file parsing functionality."""
    
    @pytest.fixture
    def sample_input_file(self):
        """Create a sample input file for testing."""
        content = """# Sample input file
https://docs.anthropic.com/en/docs/claude-code/
./research_paper.pdf
./meeting_notes.md

# Another URL
https://arxiv.org/pdf/2408.09869.pdf
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(content)
            f.flush()
            yield f.name
        os.unlink(f.name)
    
    def test_parse_input_file_success(self, sample_input_file):
        """Test successful input file parsing."""
        inputs = parse_input_file(sample_input_file)
        
        expected = [
            "https://docs.anthropic.com/en/docs/claude-code/",
            "./research_paper.pdf",
            "./meeting_notes.md",
            "https://arxiv.org/pdf/2408.09869.pdf"
        ]
        
        assert inputs == expected
        
    def test_parse_nonexistent_file(self):
        """Test parsing non-existent file."""
        with pytest.raises(FileNotFoundError):
            parse_input_file("/nonexistent/file.txt")
            
    def test_parse_empty_file(self):
        """Test parsing empty file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("# Only comments\n\n# And empty lines\n")
            f.flush()
            file_path = f.name
            
        try:
            with pytest.raises(ValueError, match="No valid inputs found"):
                parse_input_file(file_path)
        finally:
            os.unlink(file_path)
            
    def test_parse_file_with_whitespace(self):
        """Test parsing file with whitespace handling."""
        content = """  https://example.com  
        
  ./file.pdf  
"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(content)
            f.flush()
            file_path = f.name
            
        try:
            inputs = parse_input_file(file_path)
            assert inputs == ["https://example.com", "./file.pdf"]
        finally:
            os.unlink(file_path)


class TestValidateInputs:
    """Test input validation functionality."""
    
    def test_validate_inputs_success(self):
        """Test successful input validation."""
        inputs = ["https://example.com", "./test.pdf", "./notes.md"]
        result = validate_inputs(inputs)
        
        assert len(result) == 3
        assert result[0] == ("https://example.com", InputType.URL)
        assert result[1] == ("./test.pdf", InputType.PDF)
        assert result[2] == ("./notes.md", InputType.MARKDOWN)
        
    def test_validate_empty_inputs(self):
        """Test validation with empty input list."""
        with pytest.raises(ValueError, match="No inputs provided"):
            validate_inputs([])
            
    def test_validate_too_many_inputs(self):
        """Test validation with too many inputs."""
        inputs = [f"input_{i}" for i in range(101)]
        with pytest.raises(ValueError, match="Too many inputs"):
            validate_inputs(inputs)
            
    def test_validate_empty_string_input(self):
        """Test validation with empty string input."""
        with pytest.raises(ValueError, match="Empty input at position"):
            validate_inputs(["valid", "", "also_valid"])


class TestArgumentParser:
    """Test CLI argument parsing."""
    
    def test_parser_creation(self):
        """Test argument parser creation."""
        parser = create_argument_parser()
        assert parser is not None
        
    def test_parse_single_input(self):
        """Test parsing single input argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["https://example.com"])
        
        assert args.inputs == ["https://example.com"]
        assert args.input_file is None
        assert args.output_dir == "multi_input_crawl"
        assert args.max_concurrent == 10
        
    def test_parse_multiple_inputs(self):
        """Test parsing multiple input arguments."""
        parser = create_argument_parser()
        args = parser.parse_args([
            "https://example.com",
            "./test.pdf",
            "./notes.md"
        ])
        
        assert len(args.inputs) == 3
        assert args.inputs[0] == "https://example.com"
        assert args.inputs[1] == "./test.pdf"
        assert args.inputs[2] == "./notes.md"
        
    def test_parse_input_file_option(self):
        """Test parsing input file option."""
        parser = create_argument_parser()
        args = parser.parse_args(["--input-file", "inputs.txt"])
        
        assert args.input_file == "inputs.txt"
        assert args.inputs == []
        
    def test_parse_custom_options(self):
        """Test parsing custom options."""
        parser = create_argument_parser()
        args = parser.parse_args([
            "--output-dir", "custom_output",
            "--max-concurrent", "20",
            "--max-depth", "3",
            "--exclude", "pattern1", "pattern2",
            "--verbose",
            "--dry-run",
            "https://example.com"
        ])
        
        assert args.output_dir == "custom_output"
        assert args.max_concurrent == 20
        assert args.max_depth == 3
        assert args.exclude == ["pattern1", "pattern2"]
        assert args.verbose == True
        assert args.dry_run == True
        
    def test_mutually_exclusive_inputs(self):
        """Test mutually exclusive input options."""
        parser = create_argument_parser()
        
        # Should fail when both inputs and input-file are provided
        with pytest.raises(SystemExit):
            parser.parse_args([
                "https://example.com",
                "--input-file", "inputs.txt"
            ])


class TestOutputFormatting:
    """Test output formatting functions."""
    
    def test_print_input_summary(self):
        """Test input summary printing."""
        validated_inputs = [
            ("https://example.com", InputType.URL),
            ("./test.pdf", InputType.PDF),
            ("./notes.md", InputType.MARKDOWN)
        ]
        
        # Capture output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_input_summary(validated_inputs)
            output = mock_stdout.getvalue()
            
        assert "Processing 3 inputs:" in output
        assert "🌐 Url: 1" in output
        assert "📄 Pdf: 1" in output
        assert "📝 Markdown: 1" in output
        assert "Input details:" in output
        
    def test_print_results_summary(self):
        """Test results summary printing."""
        stats = {
            'total_inputs': 5,
            'successful': 4,
            'failed': 1,
            'success_rate': 0.8,
            'duration_seconds': 15.5,
            'inputs_per_second': 0.26,
            'concatenated_file': './output/result.md',
            'results_by_type': {
                'urls': 2,
                'pdfs': 1,
                'markdown': 1
            }
        }
        
        # Capture output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_results_summary(stats)
            output = mock_stdout.getvalue()
            
        assert "Processing Complete!" in output
        assert "Successful: 4/5" in output
        assert "Failed: 1" in output
        assert "Success Rate: 80.0%" in output
        assert "Duration: 15.5s" in output
        assert "🌐 URLs: 2" in output
        assert "📄 PDFs: 1" in output
        assert "📝 Markdown: 1" in output


class TestMainFunction:
    """Test main CLI function."""
    
    @pytest.mark.asyncio
    @patch('multi_input_cli.create_multi_input_processor')
    async def test_main_single_input(self, mock_create_processor):
        """Test main function with single input."""
        # Mock processor
        mock_processor = Mock()
        mock_processor.crawl = AsyncMock(return_value={
            'total_inputs': 1,
            'successful': 1,
            'failed': 0,
            'success_rate': 1.0,
            'duration_seconds': 2.5,
            'inputs_per_second': 0.4,
            'concatenated_file': './output/result.md'
        })
        mock_processor.cleanup = Mock()
        mock_create_processor.return_value = mock_processor
        
        # Import main function
        from multi_input_cli import main
        
        # Mock sys.argv
        with patch('sys.argv', ['cli', 'https://example.com']):
            exit_code = await main()
            
        assert exit_code == 0
        mock_processor.crawl.assert_called_once()
        mock_processor.cleanup.assert_called_once()
        
    @pytest.mark.asyncio
    @patch('multi_input_cli.parse_input_file')
    @patch('multi_input_cli.create_multi_input_processor')
    async def test_main_input_file(self, mock_create_processor, mock_parse_file):
        """Test main function with input file."""
        # Mock file parsing
        mock_parse_file.return_value = ["https://example.com", "./test.pdf"]
        
        # Mock processor
        mock_processor = Mock()
        mock_processor.crawl = AsyncMock(return_value={
            'total_inputs': 2,
            'successful': 2,
            'failed': 0,
            'success_rate': 1.0,
            'duration_seconds': 5.0,
            'inputs_per_second': 0.4,
            'concatenated_file': './output/result.md'
        })
        mock_processor.cleanup = Mock()
        mock_create_processor.return_value = mock_processor
        
        # Import main function
        from multi_input_cli import main
        
        # Mock sys.argv
        with patch('sys.argv', ['cli', '--input-file', 'inputs.txt']):
            exit_code = await main()
            
        assert exit_code == 0
        mock_parse_file.assert_called_once_with('inputs.txt')
        
    @pytest.mark.asyncio
    async def test_main_no_inputs(self):
        """Test main function with no inputs."""
        from multi_input_cli import main
        
        # Mock sys.argv with no inputs
        with patch('sys.argv', ['cli']):
            with patch('sys.stderr', new_callable=StringIO):
                exit_code = await main()
                
        assert exit_code == 1
        
    @pytest.mark.asyncio
    async def test_main_dry_run(self):
        """Test main function in dry run mode."""
        from multi_input_cli import main
        
        # Mock sys.argv
        with patch('sys.argv', ['cli', '--dry-run', 'https://example.com']):
            exit_code = await main()
            
        assert exit_code == 0
        
    @pytest.mark.asyncio
    @patch('multi_input_cli.create_multi_input_processor')
    async def test_main_json_output(self, mock_create_processor):
        """Test main function with JSON output."""
        # Mock processor
        mock_processor = Mock()
        mock_processor.crawl = AsyncMock(return_value={
            'total_inputs': 1,
            'successful': 1,
            'failed': 0,
            'success_rate': 1.0
        })
        mock_processor.cleanup = Mock()
        mock_create_processor.return_value = mock_processor
        
        from multi_input_cli import main
        
        # Capture output
        with patch('sys.argv', ['cli', '--json-output', 'https://example.com']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                exit_code = await main()
                output = mock_stdout.getvalue()
                
        assert exit_code == 0
        
        # Should be valid JSON
        result = json.loads(output)
        assert result['total_inputs'] == 1
        assert result['successful'] == 1


class TestExitCodes:
    """Test CLI exit codes."""
    
    def test_exit_code_high_success_rate(self):
        """Test exit code for high success rate."""
        stats = {'success_rate': 0.9}
        # Would need to test the actual main function logic
        # This is a placeholder for the concept
        
    def test_exit_code_medium_success_rate(self):
        """Test exit code for medium success rate."""
        stats = {'success_rate': 0.6}
        # Would need to test the actual main function logic
        
    def test_exit_code_low_success_rate(self):
        """Test exit code for low success rate."""
        stats = {'success_rate': 0.3}
        # Would need to test the actual main function logic


if __name__ == "__main__":
    pytest.main([__file__])