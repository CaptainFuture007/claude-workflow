"""
Enhanced Markdown Processor with Figure Extraction

This module provides advanced PDF processing with Docling that:
1. Extracts figures as high-quality PNG files
2. Creates markdown with AI-processable figure placeholders
3. Supports automated figure summarization with Ollama/Qwen models
4. Maintains table quality and document structure

Based on research of best practices for PDF figure extraction and 
AI-agent compatible file path formatting.
"""

import logging
import logging.handlers
import time
import os
import hashlib
import json
import psutil
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any
from dataclasses import dataclass
import uuid
import re
import traceback

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Docling imports
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.datamodel.base_models import InputFormat
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem, DoclingDocument

# Ollama imports for figure summarization
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    ollama = None
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


@dataclass
class FigureMetadata:
    """Metadata for an extracted figure."""
    
    figure_id: str
    page_number: int
    figure_index: int  # Index within the page
    bbox: Tuple[float, float, float, float]  # (x1, y1, x2, y2)
    caption: Optional[str] = None
    figure_type: Optional[str] = None  # 'chart', 'diagram', 'photo', etc.
    file_path: Optional[str] = None
    ai_summary: Optional[str] = None
    extraction_time: float = 0.0


@dataclass
class TableMetadata:
    """Metadata for an extracted table."""
    
    table_id: str
    page_number: int
    table_index: int  # Index within the page
    bbox: Tuple[float, float, float, float]  # (x1, y1, x2, y2)
    caption: Optional[str] = None
    table_markdown: Optional[str] = None
    row_count: int = 0
    column_count: int = 0
    section_title: Optional[str] = None
    context: Optional[str] = None
    extraction_time: float = 0.0


@dataclass
class ProcessingResult:
    """Result of enhanced markdown processing."""
    
    success: bool
    document_id: str
    markdown_content: Optional[str] = None
    markdown_file_path: Optional[str] = None
    figures_extracted: int = 0
    tables_extracted: int = 0
    figures_metadata: List[FigureMetadata] = None
    tables_metadata: List[TableMetadata] = None
    pages_processed: int = 0
    ai_summaries_generated: int = 0
    final_markdown_path: Optional[str] = None
    processing_time: float = 0.0
    error_message: Optional[str] = None
    
    def __post_init__(self):
        if self.figures_metadata is None:
            self.figures_metadata = []
        if self.tables_metadata is None:
            self.tables_metadata = []


class EnhancedMarkdownProcessor:
    """
    Advanced PDF processor that creates AI-ready markdown with extracted figures.
    
    Features:
    - High-quality figure extraction as PNG files
    - AI-processable figure placeholders in markdown
    - Optional automated figure summarization
    - Preserved table structure and document hierarchy
    """
    
    def __init__(
        self,
        output_base_dir: Union[str, Path] = "processed_documents",
        figures_subdir: str = "figures",
        markdown_subdir: str = "markdown_with_figures",
        temp_markdown_subdir: str = "markdown_temp_figures",
        final_markdown_dir: Optional[Union[str, Path]] = None,
        image_scale: float = 3.0,
        image_dpi: int = 300,
        ollama_host: str = "http://localhost:11434",
        ollama_model: str = "qwen2.5vl:7b",
        ollama_timeout: float = 120.0,
        enable_ai_summarization: bool = False
    ):
        """
        Initialize the enhanced markdown processor.
        
        Args:
            output_base_dir: Base directory for all outputs
            figures_subdir: Subdirectory name for figures
            markdown_subdir: Subdirectory name for final markdown
            temp_markdown_subdir: Subdirectory name for temp markdown with figure placeholders
            final_markdown_dir: Optional separate directory for final markdown files (for integration)
            image_scale: Scale factor for image extraction (3.0 = 300% = 900 DPI)
            image_dpi: Target DPI for extracted images
            ollama_host: Ollama server URL
            ollama_model: Ollama model to use for figure summarization
            ollama_timeout: Timeout for Ollama requests in seconds
            enable_ai_summarization: Whether to automatically summarize figures
        """
        self.output_base_dir = Path(output_base_dir)
        self.figures_subdir = figures_subdir
        self.markdown_subdir = markdown_subdir
        self.temp_markdown_subdir = temp_markdown_subdir
        self.final_markdown_dir = Path(final_markdown_dir) if final_markdown_dir else None
        self.image_scale = image_scale
        self.image_dpi = image_dpi
        self.enable_ai_summarization = enable_ai_summarization
        self.ollama_host = ollama_host
        self.ollama_model = ollama_model
        self.ollama_timeout = ollama_timeout
        
        # Setup comprehensive logging
        self.logger = self._setup_logging()
        
        # Setup Ollama client if available
        self.ollama_client = None
        if OLLAMA_AVAILABLE and enable_ai_summarization:
            try:
                # Test Ollama connection
                self.ollama_client = ollama.Client(host=self.ollama_host)
                # Verify model is available
                try:
                    models_response = self.ollama_client.list()
                    # Handle the ListResponse object
                    if hasattr(models_response, 'models'):
                        model_names = [m.model for m in models_response.models if hasattr(m, 'model')]
                    else:
                        model_names = []
                        
                    if self.ollama_model not in model_names:
                        self.logger.warning(f"Ollama model '{self.ollama_model}' not found. Available models: {model_names}")
                        # Don't fail - model might still work
                    else:
                        self.logger.info(f"Ollama client initialized with model '{self.ollama_model}' for figure summarization")
                except Exception as e:
                    self.logger.warning(f"Could not verify Ollama models: {e}")
                    # Continue anyway - model might still work
            except Exception as e:
                self.logger.warning(f"Failed to initialize Ollama client: {e}")
                self.ollama_client = None
        elif enable_ai_summarization:
            self.logger.warning("AI summarization requested but Ollama not available")
        
        # Setup Docling converter
        self.converter = self._setup_converter()
        
        # Create output directories
        self._setup_directories()
    
    def _setup_logging(self) -> logging.Logger:
        """Setup comprehensive logging with file output to configured logs directory."""
        # Create logs directory using configured path
        log_path = os.getenv('LOG_PATH', './logs')
        logs_dir = Path(log_path) / "chunking"
        logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Create logger
        logger = logging.getLogger(f"{__name__}.{id(self)}")  # Unique logger per instance
        logger.setLevel(logging.DEBUG)
        
        # Clear any existing handlers to avoid duplication
        if logger.handlers:
            logger.handlers.clear()
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        simple_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # File handler for detailed logs
        log_file = logs_dir / f"enhanced_markdown_processor_{int(time.time())}.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, 
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        
        # Console handler for important messages
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        logger.info(f"Enhanced Markdown Processor logging initialized - Log file: {log_file}")
        logger.debug(f"Configuration: image_scale={self.image_scale}, image_dpi={self.image_dpi}, ai_summarization={self.enable_ai_summarization}")
        
        return logger
    
    def _setup_converter(self) -> DocumentConverter:
        """Setup the Docling converter with optimized settings for figure extraction."""
        self.logger.debug("Starting Docling converter setup")
        
        try:
            pipeline_options = PdfPipelineOptions()
            
            # Enable high-quality image processing
            pipeline_options.images_scale = self.image_scale
            pipeline_options.generate_page_images = False  # We don't need full page images
            pipeline_options.generate_picture_images = True  # We need individual figures
            
            self.logger.debug(f"Image processing configured: scale={self.image_scale}, generate_pictures=True")
            
            # Enable advanced table processing
            pipeline_options.do_table_structure = True
            self.logger.debug("Table structure processing enabled")
            
            # Try to configure table options if available
            try:
                if hasattr(pipeline_options, 'table_structure_options'):
                    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
                    pipeline_options.table_structure_options.do_cell_matching = True
                    self.logger.debug("Table structure options configured with ACCURATE mode")
                else:
                    self.logger.warning("table_structure_options not available in this Docling version")
            except Exception as e:
                self.logger.warning(f"Could not configure table options: {e}")
                self.logger.debug(f"Table options error details: {traceback.format_exc()}")
            
            # Try to enable other enrichments if available
            enrichment_options = [
                'do_formula_enrichment',
                'do_picture_classification'
            ]
            
            for option in enrichment_options:
                try:
                    if hasattr(pipeline_options, option):
                        setattr(pipeline_options, option, True)
                        self.logger.debug(f"Enabled enrichment option: {option}")
                    else:
                        self.logger.debug(f"Enrichment option not available: {option}")
                except Exception as e:
                    self.logger.warning(f"Could not set {option}: {e}")
            
            converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
            
            self.logger.info(f"Docling converter initialized successfully with {self.image_scale}x image scaling")
            self.logger.debug("Available pipeline options: " + str(dir(pipeline_options)))
            
            return converter
            
        except Exception as e:
            self.logger.error(f"Failed to setup Docling converter: {e}")
            self.logger.debug(f"Converter setup error details: {traceback.format_exc()}")
            raise
    
    def _setup_directories(self):
        """Create necessary output directories."""
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"Output directory setup: {self.output_base_dir}")
    
    def _log_system_info(self):
        """Log system information for debugging."""
        try:
            memory = psutil.virtual_memory()
            cpu_count = psutil.cpu_count()
            self.logger.info(f"System info - RAM: {memory.total // (1024**3)}GB (available: {memory.available // (1024**3)}GB), CPUs: {cpu_count}")
        except Exception as e:
            self.logger.warning(f"Could not get system info: {e}")
    
    def _log_file_info(self, pdf_path: Path):
        """Log PDF file information."""
        try:
            file_size = pdf_path.stat().st_size
            file_size_mb = file_size / (1024 * 1024)
            self.logger.info(f"PDF file info - Size: {file_size_mb:.2f}MB ({file_size:,} bytes)")
        except Exception as e:
            self.logger.warning(f"Could not get file info: {e}")
    
    def _log_memory_usage(self, context: str):
        """Log current memory usage."""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / (1024 * 1024)
            self.logger.debug(f"Memory usage at {context}: {memory_mb:.1f}MB RSS")
        except Exception as e:
            self.logger.debug(f"Could not log memory usage at {context}: {e}")
    
    def _generate_document_id(self, pdf_path: Path) -> str:
        """Generate a unique document ID based on file content."""
        # Use file hash + timestamp for uniqueness
        with open(pdf_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()[:12]
        
        timestamp = int(time.time())
        return f"doc_{file_hash}_{timestamp}"
    
    def _create_document_directories(self, document_id: str) -> Dict[str, Path]:
        """Create directory structure for a specific document."""
        doc_dir = self.output_base_dir / document_id
        
        directories = {
            'base': doc_dir,
            'figures': doc_dir / self.figures_subdir,
            'markdown': doc_dir / self.markdown_subdir,
            'temp_markdown': doc_dir / self.temp_markdown_subdir
        }
        
        for dir_path in directories.values():
            dir_path.mkdir(parents=True, exist_ok=True)
        
        return directories
    
    def _extract_figures(
        self, 
        document: DoclingDocument, 
        document_id: str,
        figures_dir: Path
    ) -> List[FigureMetadata]:
        """Extract figures from the document and save as PNG files."""
        figures_metadata = []
        figure_counter = 0
        
        self.logger.info("Starting figure extraction...")
        self.logger.debug(f"Extracting figures to directory: {figures_dir}")
        
        # Validate figures directory is writable
        try:
            test_file = figures_dir / ".write_test"
            test_file.touch()
            test_file.unlink()
            self.logger.debug("Figures directory is writable")
        except Exception as e:
            self.logger.error(f"Figures directory not writable: {e}")
            return figures_metadata
        
        for element, _level in document.iterate_items():
            if isinstance(element, PictureItem):
                start_time = time.time()
                figure_counter += 1
                
                self.logger.debug(f"Processing figure {figure_counter}")
                
                # Generate figure metadata with improved consistency
                figure_id = f"fig_{figure_counter:03d}"
                
                # Fix page number handling - default to 1 instead of 0
                page_number = getattr(element, 'page_no', 1)
                if page_number <= 0:
                    page_number = 1
                    self.logger.warning(f"Invalid page number for {figure_id}, defaulting to 1")
                
                # Safe bbox extraction with validation
                bbox = (0, 0, 0, 0)
                try:
                    if hasattr(element, 'bbox') and element.bbox:
                        if all(hasattr(element.bbox, attr) for attr in ['l', 't', 'r', 'b']):
                            bbox = (element.bbox.l, element.bbox.t, element.bbox.r, element.bbox.b)
                            self.logger.debug(f"Figure {figure_id} bbox: {bbox}")
                        else:
                            self.logger.warning(f"Figure {figure_id} has invalid bbox structure")
                    else:
                        self.logger.debug(f"Figure {figure_id} has no bbox information")
                except Exception as e:
                    self.logger.warning(f"Error extracting bbox for {figure_id}: {e}")
                
                # Extract caption if available
                caption = None
                try:
                    if hasattr(element, 'caption') and element.caption:
                        if hasattr(element.caption, 'text'):
                            caption = element.caption.text
                        else:
                            caption = str(element.caption)
                        self.logger.debug(f"Figure {figure_id} caption: {caption[:50]}..." if len(caption) > 50 else f"Figure {figure_id} caption: {caption}")
                    else:
                        self.logger.debug(f"Figure {figure_id} has no caption")
                except Exception as e:
                    self.logger.warning(f"Error extracting caption for {figure_id}: {e}")
                
                # Determine figure type
                figure_type = 'unknown'
                try:
                    figure_type = getattr(element, 'classification', 'unknown')
                    self.logger.debug(f"Figure {figure_id} type: {figure_type}")
                except Exception as e:
                    self.logger.warning(f"Error determining figure type for {figure_id}: {e}")
                
                # Fix filename generation - use consistent 0-based indexing
                figure_filename = f"fig{figure_counter:02d}_p{page_number}_{figure_counter-1:02d}.png"
                figure_path = figures_dir / figure_filename
                
                self.logger.debug(f"Saving figure {figure_id} to: {figure_filename}")
                
                # Save the figure with enhanced error handling
                try:
                    saved = False
                    image_info = "unknown"
                    
                    if hasattr(element, 'image') and element.image:
                        # Determine what kind of image object we have
                        if hasattr(element.image, 'pil_image') and element.image.pil_image:
                            # Save PIL image
                            pil_img = element.image.pil_image
                            image_info = f"PIL {pil_img.format} {pil_img.size} {pil_img.mode}"
                            
                            with figure_path.open('wb') as f:
                                pil_img.save(f, format='PNG', dpi=(self.image_dpi, self.image_dpi))
                            saved = True
                            self.logger.debug(f"Saved {figure_id} as PIL image: {image_info}")
                            
                        elif hasattr(element.image, 'save'):
                            # Direct save method
                            element.image.save(str(figure_path))
                            saved = True
                            image_info = "direct save method"
                            self.logger.debug(f"Saved {figure_id} using direct save method")
                            
                        elif hasattr(element.image, 'data'):
                            # Raw image data
                            with figure_path.open('wb') as f:
                                f.write(element.image.data)
                            saved = True
                            image_info = f"raw data ({len(element.image.data)} bytes)"
                            self.logger.debug(f"Saved {figure_id} as raw image data")
                            
                        else:
                            # Log what attributes the image object has
                            img_attrs = [attr for attr in dir(element.image) if not attr.startswith('_')]
                            self.logger.warning(f"Figure {figure_id} image object has unsupported format. Available attributes: {img_attrs}")
                            continue
                    else:
                        self.logger.warning(f"Figure {figure_id} has no image data")
                        continue
                    
                    if not saved:
                        self.logger.error(f"Failed to save figure {figure_id} - no valid save method found")
                        continue
                    
                    # Validate saved file
                    if not figure_path.exists():
                        self.logger.error(f"Figure {figure_id} file was not created: {figure_path}")
                        continue
                    
                    file_size = figure_path.stat().st_size
                    if file_size == 0:
                        self.logger.error(f"Figure {figure_id} saved as empty file")
                        figure_path.unlink()  # Remove empty file
                        continue
                    
                    processing_time = time.time() - start_time
                    
                    # Safe path handling for metadata
                    try:
                        relative_path = str(figure_path.relative_to(self.output_base_dir))
                    except ValueError:
                        # Fallback if path is not relative to output_base_dir
                        relative_path = str(figure_path)
                        self.logger.warning(f"Could not create relative path for {figure_id}, using absolute path")
                    
                    # Create metadata
                    metadata = FigureMetadata(
                        figure_id=figure_id,
                        page_number=page_number,
                        figure_index=figure_counter - 1,  # 0-based index
                        bbox=bbox,
                        caption=caption,
                        figure_type=figure_type,
                        file_path=relative_path,
                        extraction_time=processing_time
                    )
                    
                    figures_metadata.append(metadata)
                    self.logger.info(f"Successfully extracted figure {figure_id} from page {page_number}: {figure_filename} ({file_size} bytes, {image_info})")
                    
                except Exception as e:
                    self.logger.error(f"Error extracting figure {figure_id}: {e}")
                    self.logger.debug(f"Figure extraction error details: {traceback.format_exc()}")
                    continue
        
        self.logger.info(f"Figure extraction complete: {len(figures_metadata)} figures extracted from {figure_counter} found")
        
        if figure_counter > len(figures_metadata):
            failed_count = figure_counter - len(figures_metadata)
            self.logger.warning(f"{failed_count} figures failed to extract properly")
        
        return figures_metadata
    
    def _extract_tables(
        self, 
        document: DoclingDocument, 
        document_id: str
    ) -> List[TableMetadata]:
        """Extract tables from the document and capture their markdown content."""
        tables_metadata = []
        table_counter = 0
        
        self.logger.info("Starting table extraction...")
        
        for element, _level in document.iterate_items():
            if isinstance(element, TableItem):
                start_time = time.time()
                table_counter += 1
                
                self.logger.debug(f"Processing table {table_counter}")
                
                # Generate table metadata
                table_id = f"table_{table_counter:03d}"
                
                # Fix page number handling - default to 1 instead of 0
                page_number = getattr(element, 'page_no', 1)
                if page_number <= 0:
                    page_number = 1
                    self.logger.warning(f"Invalid page number for {table_id}, defaulting to 1")
                
                # Safe bbox extraction with validation
                bbox = (0, 0, 0, 0)
                try:
                    if hasattr(element, 'bbox') and element.bbox:
                        if all(hasattr(element.bbox, attr) for attr in ['l', 't', 'r', 'b']):
                            bbox = (element.bbox.l, element.bbox.t, element.bbox.r, element.bbox.b)
                            self.logger.debug(f"Table {table_id} bbox: {bbox}")
                        else:
                            self.logger.warning(f"Table {table_id} has invalid bbox structure")
                    else:
                        self.logger.debug(f"Table {table_id} has no bbox information")
                except Exception as e:
                    self.logger.warning(f"Error extracting bbox for {table_id}: {e}")
                
                # Extract caption if available
                caption = None
                try:
                    if hasattr(element, 'caption') and element.caption:
                        if hasattr(element.caption, 'text'):
                            caption = element.caption.text
                        else:
                            caption = str(element.caption)
                        self.logger.debug(f"Table {table_id} caption: {caption[:50]}...") if len(caption) > 50 else self.logger.debug(f"Table {table_id} caption: {caption}")
                    else:
                        self.logger.debug(f"Table {table_id} has no caption")
                except Exception as e:
                    self.logger.warning(f"Error extracting caption for {table_id}: {e}")
                
                # Extract table markdown content
                table_markdown = None
                row_count = 0
                column_count = 0
                try:
                    if hasattr(element, 'export_to_markdown'):
                        table_markdown = element.export_to_markdown()
                        self.logger.debug(f"Table {table_id} markdown extracted: {len(table_markdown)} characters")
                        
                        # Calculate row/column counts from markdown
                        if table_markdown:
                            lines = table_markdown.strip().split('\n')
                            # Filter out header separator lines (containing only |, -, and spaces)
                            data_lines = [line for line in lines if line.strip() and not all(c in '|-: ' for c in line.strip())]
                            if data_lines:
                                row_count = len(data_lines)
                                # Count columns from first row
                                first_row = data_lines[0]
                                column_count = len([cell for cell in first_row.split('|') if cell.strip()])
                                self.logger.debug(f"Table {table_id} calculated size: {row_count}x{column_count}")
                    elif hasattr(element, 'table_data'):
                        # Alternative: extract from table_data if available
                        table_data = element.table_data
                        if table_data and hasattr(table_data, 'table_cells'):
                            # Simple markdown generation from table cells
                            rows = []
                            for row in table_data.table_cells:
                                cells = [cell.get('content', '') for cell in row]
                                rows.append('| ' + ' | '.join(cells) + ' |')
                                if len(rows) == 1:  # Add header separator
                                    header_sep = '| ' + ' | '.join(['---'] * len(cells)) + ' |'
                                    rows.append(header_sep)
                            table_markdown = '\n'.join(rows)
                            row_count = len(table_data.table_cells)
                            column_count = len(table_data.table_cells[0]) if table_data.table_cells else 0
                        self.logger.debug(f"Table {table_id} generated from table_data: {row_count}x{column_count}")
                    else:
                        # Fallback: try to get text content
                        if hasattr(element, 'text'):
                            table_markdown = f"```\n{element.text}\n```"
                            self.logger.debug(f"Table {table_id} fallback to text content")
                        else:
                            table_markdown = f"[Table {table_counter} - content not extractable]"
                            self.logger.warning(f"Table {table_id} content could not be extracted")
                except Exception as e:
                    self.logger.warning(f"Error extracting table content for {table_id}: {e}")
                    table_markdown = f"[Table {table_counter} - extraction error: {str(e)}]"
                
                # Try to determine section context
                section_title = ""
                try:
                    # This would need to be enhanced with document structure analysis
                    section_title = getattr(element, 'section', '')
                except:
                    pass
                
                processing_time = time.time() - start_time
                
                # Create metadata
                metadata = TableMetadata(
                    table_id=table_id,
                    page_number=page_number,
                    table_index=table_counter - 1,  # 0-based index
                    bbox=bbox,
                    caption=caption,
                    table_markdown=table_markdown,
                    row_count=row_count,
                    column_count=column_count,
                    section_title=section_title,
                    extraction_time=processing_time
                )
                
                tables_metadata.append(metadata)
                self.logger.info(f"Successfully extracted table {table_id} from page {page_number}: {row_count}x{column_count} ({len(table_markdown or '') if table_markdown else 0} chars)")
        
        self.logger.info(f"Table extraction complete: {len(tables_metadata)} tables extracted from {table_counter} found")
        
        return tables_metadata
    
    def _create_ai_figure_placeholder(self, figure_metadata: FigureMetadata, document_id: str) -> str:
        """Create an AI-processable figure placeholder for markdown."""
        # Use relative path from the document base directory
        relative_path = f"{self.figures_subdir}/{Path(figure_metadata.file_path).name}"
        
        # Create the placeholder with metadata for AI processing
        placeholder = f"""
![Figure {figure_metadata.figure_id}]({relative_path})

**Figure Metadata:**
- ID: {figure_metadata.figure_id}
- Page: {figure_metadata.page_number}
- Position: [{figure_metadata.bbox[0]:.1f}, {figure_metadata.bbox[1]:.1f}] - [{figure_metadata.bbox[2]:.1f}, {figure_metadata.bbox[3]:.1f}]
- Type: {figure_metadata.figure_type or 'unknown'}
- Caption: {figure_metadata.caption or 'No caption available'}

<!-- AI_FIGURE_PLACEHOLDER:{figure_metadata.figure_id}:{relative_path} -->
"""
        
        return placeholder.strip()
    
    def _summarize_figure_with_ai(self, figure_path: Path, figure_metadata: FigureMetadata) -> Optional[str]:
        """Generate AI summary for a figure using Ollama/Qwen Vision models."""
        if not self.ollama_client:
            return None
        
        start_time = time.time()
        self.logger.debug(f"Starting AI summarization for {figure_metadata.figure_id}")
        
        try:
            # Read the image file
            self.logger.debug(f"Reading image file: {figure_path}")
            with open(figure_path, 'rb') as f:
                import base64
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            image_size_kb = len(image_data) / 1024
            self.logger.debug(f"Image encoded, size: {image_size_kb:.1f}KB")
            
            # Create the prompt for figure analysis
            prompt = f"""Analyze this figure and provide a concise, informative summary. Focus on:
1. What type of visualization this is (chart, diagram, photograph, etc.)
2. Key data trends or patterns if it's a chart/graph
3. Main visual elements and their relationships
4. Any text or labels visible in the figure
5. The scientific or informational content conveyed

Context from document:
- Page: {figure_metadata.page_number}
- Original caption: {figure_metadata.caption or 'No caption provided'}
- Figure type: {figure_metadata.figure_type or 'Unknown'}

Provide a clear, factual summary in 2-3 sentences."""

            self.logger.debug(f"Making Ollama API call for {figure_metadata.figure_id} using model {self.ollama_model}")
            api_start = time.time()
            
            # Prepare the request for Ollama with vision capabilities
            response = self.ollama_client.chat(
                model=self.ollama_model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                        "images": [image_data]  # Ollama expects base64 images in the images field
                    }
                ],
                options={
                    "temperature": 0.7,
                    "num_predict": 300  # Similar to max_tokens
                }
            )
            
            api_time = time.time() - api_start
            total_time = time.time() - start_time
            
            # Extract the response content
            summary = response['message']['content']
            self.logger.info(f"Generated AI summary for {figure_metadata.figure_id} (API: {api_time:.2f}s, total: {total_time:.2f}s)")
            self.logger.debug(f"Summary length: {len(summary)} characters")
            return summary
            
        except Exception as e:
            total_time = time.time() - start_time
            self.logger.error(f"Error generating AI summary for {figure_metadata.figure_id} after {total_time:.2f}s: {e}")
            self.logger.debug(f"AI summarization error details: {traceback.format_exc()}")
            return None
    
    def _create_enhanced_markdown(
        self, 
        document: DoclingDocument, 
        figures_metadata: List[FigureMetadata],
        document_id: str,
        temp_markdown_dir: Path,
        final_markdown_dir: Path
    ) -> Tuple[str, str]:
        """Create markdown with figure placeholders and optionally process with AI summaries."""
        
        # Export basic markdown from Docling
        base_markdown = document.export_to_markdown(image_mode=ImageRefMode.PLACEHOLDER)
        
        # Create temp markdown with figure placeholders
        enhanced_markdown = base_markdown
        
        # Replace image placeholders with our AI-processable placeholders
        figure_placeholder_pattern = r'<!-- image -->'
        figure_iter = iter(figures_metadata)
        
        def replace_placeholder(match):
            try:
                figure_meta = next(figure_iter)
                return self._create_ai_figure_placeholder(figure_meta, document_id)
            except StopIteration:
                return match.group(0)  # Return original if no more figures
        
        enhanced_markdown = re.sub(figure_placeholder_pattern, replace_placeholder, enhanced_markdown)
        
        # Save temporary markdown with placeholders
        temp_markdown_file = temp_markdown_dir / f"{document_id}_temp.md"
        with open(temp_markdown_file, 'w', encoding='utf-8') as f:
            f.write(enhanced_markdown)
        
        # Create final markdown with AI summaries if enabled
        final_markdown = enhanced_markdown
        
        if self.enable_ai_summarization and self.ollama_client:
            ai_start = time.time()
            figure_count = len(figures_metadata)
            self.logger.info(f"Generating AI summaries for {figure_count} figures...")
            
            for i, figure_meta in enumerate(figures_metadata, 1):
                self.logger.debug(f"Processing figure {i}/{figure_count}: {figure_meta.figure_id}")
                
                # Generate AI summary
                figure_full_path = self.output_base_dir / figure_meta.file_path
                ai_summary = self._summarize_figure_with_ai(figure_full_path, figure_meta)
                
                if ai_summary:
                    figure_meta.ai_summary = ai_summary
                    
                    # Replace placeholder with summary
                    placeholder_pattern = f"<!-- AI_FIGURE_PLACEHOLDER:{figure_meta.figure_id}:.*? -->"
                    summary_content = f"""
**AI Analysis:** {ai_summary}

<!-- AI_SUMMARY_GENERATED:{figure_meta.figure_id} -->"""
                    
                    final_markdown = re.sub(
                        placeholder_pattern, 
                        lambda m: m.group(0) + summary_content,
                        final_markdown
                    )
                else:
                    self.logger.warning(f"No AI summary generated for {figure_meta.figure_id}")
            
            ai_time = time.time() - ai_start
            self.logger.info(f"AI summarization phase completed in {ai_time:.2f}s")
        
        # Save final markdown
        self.logger.debug("Saving final markdown file...")
        final_markdown_file = final_markdown_dir / f"{document_id}_final.md"
        
        try:
            with open(final_markdown_file, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            
            # Verify file was saved
            if final_markdown_file.exists():
                file_size = final_markdown_file.stat().st_size
                self.logger.info(f"Final markdown saved: {final_markdown_file} ({file_size:,} bytes)")
            else:
                self.logger.error(f"Final markdown file was not created: {final_markdown_file}")
                
        except Exception as e:
            self.logger.error(f"Error saving final markdown: {e}")
            self.logger.debug(f"Markdown save error details: {traceback.format_exc()}")
        
        return str(temp_markdown_file), str(final_markdown_file)
    
    def process_pdf(self, pdf_path: Union[str, Path]) -> ProcessingResult:
        """
        Process a PDF file with enhanced markdown generation and figure extraction.
        
        Args:
            pdf_path: Path to the PDF file to process
            
        Returns:
            ProcessingResult with details of the processing
        """
        start_time = time.time()
        pdf_path = Path(pdf_path)
        
        if not pdf_path.exists():
            return ProcessingResult(
                success=False,
                document_id="",
                error_message=f"PDF file not found: {pdf_path}"
            )
        
        # Generate document ID and create directories
        document_id = self._generate_document_id(pdf_path)
        directories = self._create_document_directories(document_id)
        
        result = ProcessingResult(
            success=False,
            document_id=document_id
        )
        
        try:
            self.logger.info(f"Processing PDF: {pdf_path.name}")
            self.logger.debug(f"PDF path: {pdf_path}")
            self.logger.debug(f"Document ID: {document_id}")
            self.logger.debug(f"Output directories: {directories}")
            
            # Log system and file info
            self._log_system_info()
            self._log_file_info(pdf_path)
            self._log_memory_usage("start")
            
            # Convert PDF with Docling
            self.logger.info("Starting Docling conversion...")
            self.logger.debug("Initializing Docling converter...")
            conversion_start = time.time()
            
            conversion_result = self.converter.convert(str(pdf_path))
            
            conversion_time = time.time() - conversion_start
            self.logger.info(f"Docling conversion completed in {conversion_time:.2f}s")
            self._log_memory_usage("post-conversion")
            
            if not conversion_result:
                error_msg = "Docling conversion returned None"
                self.logger.error(error_msg)
                return ProcessingResult(
                    success=False,
                    document_id=document_id,
                    error_message=error_msg
                )
            
            if conversion_result.status.name.lower() != "success":
                error_msg = f"Docling conversion failed with status {conversion_result.status.name}: {conversion_result.errors if conversion_result.errors else 'No error details'}"
                self.logger.error(error_msg)
                return ProcessingResult(
                    success=False,
                    document_id=document_id,
                    error_message=error_msg
                )
            
            self.logger.info("Docling conversion successful")
            
            document = conversion_result.document
            
            # Log document stats
            try:
                total_elements = sum(1 for _ in document.iterate_items())
                self.logger.info(f"Document parsed: {total_elements} total elements found")
            except Exception as e:
                self.logger.warning(f"Could not count document elements: {e}")
            
            # Extract figures
            self.logger.info("Starting figure extraction phase...")
            extraction_start = time.time()
            self._log_memory_usage("pre-extraction")
            
            figures_metadata = self._extract_figures(
                document, 
                document_id, 
                directories['figures']
            )
            
            # Extract tables
            self.logger.info("Starting table extraction phase...")
            tables_metadata = self._extract_tables(
                document, 
                document_id
            )
            
            extraction_time = time.time() - extraction_start
            self.logger.info(f"Figure and table extraction completed in {extraction_time:.2f}s")
            self._log_memory_usage("post-extraction")
            
            # Create enhanced markdown
            self.logger.info("Starting markdown generation phase...")
            markdown_start = time.time()
            
            temp_markdown_path, final_markdown_path = self._create_enhanced_markdown(
                document,
                figures_metadata,
                document_id,
                directories['temp_markdown'],
                directories['markdown']
            )
            
            markdown_time = time.time() - markdown_start
            self.logger.info(f"Markdown generation completed in {markdown_time:.2f}s")
            self._log_memory_usage("post-markdown")
            
            # Count AI summaries generated
            ai_summaries_count = sum(1 for fig in figures_metadata if fig.ai_summary)
            
            # Update result
            result.success = True
            result.figures_extracted = len(figures_metadata)
            result.tables_extracted = len(tables_metadata)
            result.figures_metadata = figures_metadata
            result.tables_metadata = tables_metadata
            result.pages_processed = len(set(getattr(element, 'page_no', 1) for element, _ in document.iterate_items()))
            result.ai_summaries_generated = ai_summaries_count
            result.final_markdown_path = final_markdown_path
            result.markdown_file_path = final_markdown_path
            result.processing_time = time.time() - start_time
            
            # Save metadata as JSON
            metadata_file = directories['base'] / f"{document_id}_metadata.json"
            metadata_dict = {
                'document_id': document_id,
                'source_pdf': str(pdf_path),
                'processing_time': result.processing_time,
                'figures_extracted': result.figures_extracted,
                'tables_extracted': result.tables_extracted,
                'pages_processed': result.pages_processed,
                'ai_summaries_generated': result.ai_summaries_generated,
                'temp_markdown_path': temp_markdown_path,
                'final_markdown_path': final_markdown_path,
                'figures_metadata': [
                    {
                        'figure_id': fig.figure_id,
                        'page_number': fig.page_number,
                        'file_path': fig.file_path,
                        'caption': fig.caption,
                        'figure_type': fig.figure_type,
                        'ai_summary': fig.ai_summary
                    }
                    for fig in figures_metadata
                ],
                'tables_metadata': [
                    {
                        'table_id': table.table_id,
                        'page_number': table.page_number,
                        'caption': table.caption,
                        'row_count': table.row_count,
                        'column_count': table.column_count,
                        'section_title': table.section_title
                    }
                    for table in tables_metadata
                ]
            }
            
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata_dict, f, indent=2, ensure_ascii=False)
            
            self.logger.info(
                f"Successfully processed {pdf_path.name}: "
                f"{result.figures_extracted} figures, {result.tables_extracted} tables "
                f"in {result.processing_time:.2f}s"
            )
            
            return result
            
        except Exception as e:
            result.error_message = str(e)
            result.processing_time = time.time() - start_time
            self.logger.error(f"Error processing {pdf_path.name}: {e}")
            return result


def create_enhanced_processor(
    output_dir: str = "processed_documents",
    final_markdown_dir: Optional[str] = None,
    ollama_host: str = "http://localhost:11434",
    ollama_model: str = "qwen2.5vl:7b",
    ollama_timeout: float = 120.0,
    enable_ai_summarization: bool = False,
    **kwargs
) -> EnhancedMarkdownProcessor:
    """
    Convenience function to create an enhanced markdown processor.
    
    Args:
        output_dir: Output directory for processed documents
        final_markdown_dir: Optional separate directory for final markdown files
        ollama_host: Ollama server URL
        ollama_model: Ollama model for figure summarization
        ollama_timeout: Timeout for Ollama requests
        enable_ai_summarization: Whether to enable AI figure summarization
        **kwargs: Additional configuration options
        
    Returns:
        EnhancedMarkdownProcessor instance
    """
    return EnhancedMarkdownProcessor(
        output_base_dir=output_dir,
        final_markdown_dir=final_markdown_dir,
        ollama_host=ollama_host,
        ollama_model=ollama_model,
        ollama_timeout=ollama_timeout,
        enable_ai_summarization=enable_ai_summarization,
        **kwargs
    )


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python enhanced_markdown_processor.py <pdf_path> [enable_ai_summary]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    enable_ai = len(sys.argv) > 2 and sys.argv[2].lower() in ['true', '1', 'yes']
    
    if not DOTENV_AVAILABLE:
        print("Warning: python-dotenv not available. Environment variables loaded from system only.")
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create processor with Ollama configuration
    processor = create_enhanced_processor(
        ollama_host=os.getenv('OLLAMA_HOST', 'http://localhost:11434'),
        ollama_model=os.getenv('OLLAMA_MODEL', 'qwen2.5vl:7b'),
        enable_ai_summarization=enable_ai
    )
    
    # Process PDF
    result = processor.process_pdf(pdf_path)
    
    if result.success:
        print(f"\n✅ Successfully processed {Path(pdf_path).name}")
        print(f"📁 Document ID: {result.document_id}")
        print(f"🖼️  Figures extracted: {result.figures_extracted}")
        print(f"📊 Tables extracted: {result.tables_extracted}")
        print(f"📝 Markdown file: {result.markdown_file_path}")
        print(f"⏱️  Processing time: {result.processing_time:.2f}s")
        
        if result.figures_metadata:
            print("\nFigures extracted:")
            for fig in result.figures_metadata:
                print(f"  - {fig.figure_id}: {fig.file_path}")
                if fig.ai_summary:
                    print(f"    AI Summary: {fig.ai_summary[:100]}...")
    else:
        print(f"\n❌ Processing failed: {result.error_message}")