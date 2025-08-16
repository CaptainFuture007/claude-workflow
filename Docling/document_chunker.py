"""
Document Chunking Module with Docling Integration

This module provides intelligent document chunking capabilities specifically
designed for scientific publications, using Docling's HybridChunker with
structure-aware processing to preserve document hierarchy and context.

Key Features:
- Structure-aware chunking that respects document organization
- Hierarchical section preservation
- Table and figure context integration
- Configurable chunk sizes optimized for different content types
- Token counting with popular embedding models
- Context enrichment for better retrieval performance
"""

import logging
import os
from typing import List, Dict, Any, Optional, Union, Iterator
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    from docling_core.types.doc.document import DoclingDocument
    from docling_core.types.doc.labels import DocItemLabel
    from docling_core.transforms.chunker.hierarchical_chunker import HierarchicalChunker
    from docling_core.transforms.chunker.hybrid_chunker import HybridChunker
    from docling_core.transforms.chunker.base import BaseChunk
    DOCLING_AVAILABLE = True
except ImportError:
    # Fallback for when Docling is not available
    DoclingDocument = Any
    DocItemLabel = None
    HierarchicalChunker = None
    HybridChunker = None
    BaseChunk = Any
    DOCLING_AVAILABLE = False

try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
    TRANSFORMERS_AVAILABLE = True  # For backward compatibility with tests
except ImportError:
    tiktoken = None
    TIKTOKEN_AVAILABLE = False
    TRANSFORMERS_AVAILABLE = False  # For backward compatibility with tests

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    openai = None
    OPENAI_AVAILABLE = False

logger = logging.getLogger(__name__)


@dataclass
class ChunkMetadata:
    """Metadata for a document chunk."""
    
    # Chunk identification
    chunk_index: int
    chunk_id: str
    
    # Content properties
    token_count: int
    char_count: int
    chunk_type: str  # 'text', 'table', 'figure', 'abstract', etc.
    
    # Document context
    section_title: Optional[str] = None
    section_hierarchy: List[str] = None  # ['Introduction', 'Methods', 'Subsection']
    page_numbers: List[int] = None
    
    # References
    table_refs: List[str] = None  # References to tables in this chunk
    figure_refs: List[str] = None  # References to figures in this chunk
    formula_refs: List[str] = None  # References to formulas in this chunk
    
    # Quality metrics
    has_complete_sentences: bool = True
    starts_mid_sentence: bool = False
    ends_mid_sentence: bool = False
    
    def __post_init__(self):
        if self.section_hierarchy is None:
            self.section_hierarchy = []
        if self.page_numbers is None:
            self.page_numbers = []
        if self.table_refs is None:
            self.table_refs = []
        if self.figure_refs is None:
            self.figure_refs = []
        if self.formula_refs is None:
            self.formula_refs = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


@dataclass
class DocumentChunk:
    """A chunk of document content with enriched metadata."""
    
    content: str
    metadata: ChunkMetadata
    enriched_content: Optional[str] = None  # Content with context
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            'content': self.content,
            'enriched_content': self.enriched_content,
            'metadata': self.metadata.to_dict()
        }


class StructureAwareChunker:
    """
    Advanced document chunker that preserves document structure and context.
    
    This chunker is specifically designed for scientific documents, respecting
    section boundaries, preserving mathematical content, and maintaining
    relationships between text, tables, and figures.
    """
    
    def __init__(
        self,
        chunk_size: int = None,
        chunk_overlap: int = None,
        tokenizer_name: str = "tiktoken",
        respect_section_boundaries: bool = True,
        preserve_tables: bool = True,
        preserve_formulas: bool = True,
        min_chunk_size: int = 50,
        max_chunk_size: int = 1000
    ):
        """
        Initialize the structure-aware chunker.
        
        Args:
            chunk_size: Target chunk size in tokens
            chunk_overlap: Overlap between chunks in tokens
            tokenizer_name: Tokenizer for token counting (supports "tiktoken" for OpenAI)
            respect_section_boundaries: Whether to avoid splitting across sections
            preserve_tables: Whether to keep tables intact
            preserve_formulas: Whether to keep formulas intact
            min_chunk_size: Minimum chunk size in tokens
            max_chunk_size: Maximum chunk size in tokens
        """
        # Use environment variables if parameters not provided
        self.chunk_size = chunk_size or int(os.getenv('CHUNK_SIZE', '512'))
        self.chunk_overlap = chunk_overlap or int(os.getenv('CHUNK_OVERLAP', '50'))
        self.tokenizer_name = tokenizer_name
        self.respect_section_boundaries = respect_section_boundaries
        self.preserve_tables = preserve_tables
        self.preserve_formulas = preserve_formulas
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
        
        self.logger = logging.getLogger(__name__)
        
        # Initialize tokenizer if available
        self.tokenizer = self._setup_tokenizer()
        
        # Initialize Docling chunker if available
        self.docling_chunker = self._setup_docling_chunker()
    
    def _setup_tokenizer(self):
        """Setup the tokenizer for token counting."""
        if TIKTOKEN_AVAILABLE and TRANSFORMERS_AVAILABLE:
            try:
                # Use tiktoken for OpenAI-compatible tokenization
                tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
                self.logger.info("Initialized tiktoken tokenizer for OpenAI models")
                return tokenizer
            except Exception as e:
                self.logger.warning(f"Failed to load tiktoken tokenizer: {e}")
        
        self.logger.warning("tiktoken not available, using word-based token estimation")
        return None
    
    def _setup_docling_chunker(self):
        """Setup the Docling chunker if available."""
        if not DOCLING_AVAILABLE:
            self.logger.warning("Docling not available, using basic chunking")
            return None
        
        try:
            # Use HierarchicalChunker to avoid HuggingFace dependency
            chunker = HierarchicalChunker()
            self.logger.info("Initialized Docling HierarchicalChunker (no HuggingFace dependency)")
            return chunker
        except Exception as e:
            self.logger.warning(f"Failed to initialize Docling chunker: {e}")
            return None
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        if self.tokenizer:
            try:
                if TIKTOKEN_AVAILABLE:
                    # Use tiktoken encoding
                    tokens = self.tokenizer.encode(text)
                    return len(tokens)
                else:
                    # Fallback for other tokenizers
                    tokens = self.tokenizer.encode(text, add_special_tokens=False)
                    return len(tokens)
            except Exception:
                # Fallback to word-based estimation
                return int(len(text.split()) * 1.3)
        else:
            # Simple word-based estimation
            return int(len(text.split()) * 1.3)
    
    def chunk_document(self, doc: DoclingDocument, document_id: str = "") -> List[DocumentChunk]:
        """
        Chunk a Docling document with structure preservation.
        
        Args:
            doc: Docling document object
            document_id: Optional document identifier
            
        Returns:
            List of DocumentChunk objects
        """
        if not DOCLING_AVAILABLE or self.docling_chunker is None:
            self.logger.error("Docling chunking not available")
            return []
        
        try:
            # Use Docling's chunker
            raw_chunks = list(self.docling_chunker.chunk(doc))
            
            # Process and enrich chunks
            processed_chunks = []
            for i, chunk in enumerate(raw_chunks):
                processed_chunk = self._process_docling_chunk(chunk, i, document_id)
                if processed_chunk:
                    processed_chunks.append(processed_chunk)
            
            self.logger.info(f"Created {len(processed_chunks)} chunks from document")
            return processed_chunks
            
        except Exception as e:
            self.logger.error(f"Error chunking document: {e}")
            return []
    
    def _process_docling_chunk(self, chunk: BaseChunk, index: int, document_id: str) -> Optional[DocumentChunk]:
        """Process a raw Docling chunk into a DocumentChunk."""
        try:
            # Extract chunk content
            content = chunk.text if hasattr(chunk, 'text') else str(chunk)
            if not content or len(content.strip()) < self.min_chunk_size:
                return None
            
            # Count tokens and characters
            token_count = self.count_tokens(content)
            char_count = len(content)
            
            # Skip chunks that are too large
            if token_count > self.max_chunk_size:
                self.logger.warning(f"Chunk {index} too large ({token_count} tokens), skipping")
                return None
            
            # Extract metadata from chunk
            chunk_metadata = self._extract_chunk_metadata(chunk, index, document_id, token_count, char_count)
            
            # Create enriched content
            enriched_content = self._enrich_chunk_content(chunk, content)
            
            return DocumentChunk(
                content=content,
                metadata=chunk_metadata,
                enriched_content=enriched_content
            )
            
        except Exception as e:
            self.logger.warning(f"Error processing chunk {index}: {e}")
            return None
    
    def _extract_chunk_metadata(
        self, 
        chunk: BaseChunk, 
        index: int, 
        document_id: str, 
        token_count: int, 
        char_count: int
    ) -> ChunkMetadata:
        """Extract metadata from a Docling chunk."""
        
        # Generate chunk ID
        chunk_id = f"{document_id}_chunk_{index}" if document_id else f"chunk_{index}"
        
        # Determine chunk type
        chunk_type = self._determine_chunk_type(chunk)
        
        # Extract section information
        section_title, section_hierarchy = self._extract_section_info(chunk)
        
        # Extract page numbers
        page_numbers = self._extract_page_numbers(chunk)
        
        # Extract references
        table_refs, figure_refs, formula_refs = self._extract_references(chunk)
        
        # Analyze content quality
        content = chunk.text if hasattr(chunk, 'text') else str(chunk)
        has_complete_sentences = self._has_complete_sentences(content)
        starts_mid_sentence = self._starts_mid_sentence(content)
        ends_mid_sentence = self._ends_mid_sentence(content)
        
        return ChunkMetadata(
            chunk_index=index,
            chunk_id=chunk_id,
            token_count=token_count,
            char_count=char_count,
            chunk_type=chunk_type,
            section_title=section_title,
            section_hierarchy=section_hierarchy,
            page_numbers=page_numbers,
            table_refs=table_refs,
            figure_refs=figure_refs,
            formula_refs=formula_refs,
            has_complete_sentences=has_complete_sentences,
            starts_mid_sentence=starts_mid_sentence,
            ends_mid_sentence=ends_mid_sentence
        )
    
    def _determine_chunk_type(self, chunk: BaseChunk) -> str:
        """Determine the type of content in the chunk."""
        try:
            if hasattr(chunk, 'meta') and chunk.meta:
                # Check document items in chunk metadata
                if hasattr(chunk.meta, 'doc_items'):
                    for item in chunk.meta.doc_items:
                        if hasattr(item, 'label'):
                            label_str = str(item.label).lower()
                            if 'abstract' in label_str:
                                return 'abstract'
                            elif 'introduction' in label_str:
                                return 'introduction'
                            elif 'method' in label_str:
                                return 'methods'
                            elif 'result' in label_str:
                                return 'results'
                            elif 'discussion' in label_str:
                                return 'discussion'
                            elif 'conclusion' in label_str:
                                return 'conclusion'
                            elif 'reference' in label_str:
                                return 'references'
            
            # Fallback to content analysis
            content = chunk.text if hasattr(chunk, 'text') else str(chunk)
            return self._determine_text_chunk_type(content)
                
        except Exception:
            return 'text'
    
    def _determine_text_chunk_type(self, content: str) -> str:
        """Determine chunk type from text content using section keywords."""
        content_lower = content.lower().strip()
        
        # Check for section indicators in content
        if content_lower.startswith('abstract') or 'abstract' in content_lower[:50]:
            return 'abstract'
        elif any(keyword in content_lower[:100] for keyword in ['introduction', 'background']):
            return 'introduction'
        elif any(keyword in content_lower[:100] for keyword in ['method', 'methodology', 'approach', 'procedure']):
            return 'methods'
        elif any(keyword in content_lower[:100] for keyword in ['result', 'finding', 'outcome']):
            return 'results'
        elif any(keyword in content_lower[:100] for keyword in ['discussion', 'interpretation', 'analysis']):
            return 'discussion'
        elif any(keyword in content_lower[:100] for keyword in ['conclusion', 'summary', 'concluding']):
            return 'conclusion'
        elif any(keyword in content_lower[:100] for keyword in ['reference', 'bibliography', 'citation']):
            return 'references'
        else:
            return 'text'
    
    def _extract_section_info(self, chunk: BaseChunk) -> tuple[Optional[str], List[str]]:
        """Extract section title and hierarchy from chunk."""
        section_title = None
        section_hierarchy = []
        
        try:
            if hasattr(chunk, 'meta') and chunk.meta:
                # Try to get section hierarchy from metadata
                if hasattr(chunk.meta, 'headings') and chunk.meta.headings:
                    section_hierarchy = chunk.meta.headings[:]
                    section_title = section_hierarchy[-1] if section_hierarchy else None
                elif hasattr(chunk.meta, 'doc_items'):
                    # Extract from document items
                    for item in chunk.meta.doc_items:
                        if hasattr(item, 'label') and 'section' in str(item.label).lower():
                            if hasattr(item, 'text'):
                                section_title = item.text
                                section_hierarchy = [section_title]
                                break
        except Exception as e:
            self.logger.debug(f"Error extracting section info: {e}")
        
        return section_title, section_hierarchy
    
    def _extract_page_numbers(self, chunk: BaseChunk) -> List[int]:
        """Extract page numbers from chunk."""
        page_numbers = []
        
        try:
            if hasattr(chunk, 'meta') and chunk.meta:
                if hasattr(chunk.meta, 'doc_items'):
                    for item in chunk.meta.doc_items:
                        if hasattr(item, 'prov') and item.prov:
                            for prov in item.prov:
                                if hasattr(prov, 'page_no'):
                                    page_numbers.append(prov.page_no)
            
            # Remove duplicates and sort
            page_numbers = sorted(list(set(page_numbers)))
            
        except Exception as e:
            self.logger.debug(f"Error extracting page numbers: {e}")
        
        return page_numbers
    
    def _extract_references(self, chunk: BaseChunk) -> tuple[List[str], List[str], List[str]]:
        """Extract references to tables, figures, and formulas."""
        table_refs = []
        figure_refs = []
        formula_refs = []
        
        try:
            content = chunk.text if hasattr(chunk, 'text') else str(chunk)
            
            # Simple pattern matching for references
            import re
            
            # Table references (preserve original case)
            table_patterns = [
                (r'(Table)\s+(\d+)', 'Table'),
                (r'(Tab)\.\s+(\d+)', 'Table'),
                (r'(table)\s+(\d+)', 'table')
            ]
            for pattern, default_prefix in table_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        prefix, number = match
                        if prefix.lower() == 'tab':
                            # Convert Tab. to Table
                            formatted_ref = f"Table {number}"
                        else:
                            # Preserve original case
                            formatted_ref = f"{prefix} {number}"
                    else:
                        formatted_ref = f"{default_prefix} {match}"
                    table_refs.append(formatted_ref)
            
            # Figure references (preserve original case)
            figure_patterns = [
                (r'(Figure)\s+(\d+)', 'Figure'),
                (r'(Fig)\.\s+(\d+)', 'Figure'),
                (r'(figure)\s+(\d+)', 'figure')
            ]
            for pattern, default_prefix in figure_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        prefix, number = match
                        if prefix.lower() == 'fig':
                            # Convert Fig. to Figure
                            formatted_ref = f"Figure {number}"
                        else:
                            # Preserve original case
                            formatted_ref = f"{prefix} {number}"
                    else:
                        formatted_ref = f"{default_prefix} {match}"
                    figure_refs.append(formatted_ref)
            
            # Formula references (preserve original case)
            formula_patterns = [
                (r'(Equation)\s+(\d+)', 'Equation'),
                (r'(Eq)\.\s+(\d+)', 'Equation'),
                (r'(equation)\s+(\d+)', 'equation')
            ]
            for pattern, default_prefix in formula_patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    if isinstance(match, tuple):
                        prefix, number = match
                        if prefix.lower() == 'eq':
                            # Convert Eq. to Equation
                            formatted_ref = f"Equation {number}"
                        else:
                            # Preserve original case
                            formatted_ref = f"{prefix} {number}"
                    else:
                        formatted_ref = f"{default_prefix} {match}"
                    formula_refs.append(formatted_ref)
            
            # Remove duplicates
            table_refs = list(set(table_refs))
            figure_refs = list(set(figure_refs))
            formula_refs = list(set(formula_refs))
            
        except Exception as e:
            self.logger.debug(f"Error extracting references: {e}")
        
        return table_refs, figure_refs, formula_refs
    
    def _has_complete_sentences(self, content: str) -> bool:
        """Check if chunk contains complete sentences."""
        content = content.strip()
        if not content:
            return False
        
        # Check if text ends with sentence-ending punctuation
        sentence_endings = '.!?'
        if not content.endswith(tuple(sentence_endings)):
            return False
        
        # Check if there are reasonably complete sentences
        sentences = content.split('.')
        complete_sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        return len(complete_sentences) > 0
    
    def _starts_mid_sentence(self, content: str) -> bool:
        """Check if chunk starts mid-sentence."""
        content = content.strip()
        if not content:
            return False
        return content[0].islower()
    
    def _ends_mid_sentence(self, content: str) -> bool:
        """Check if chunk ends mid-sentence."""
        content = content.strip()
        if not content:
            return False
        return not content.endswith(('.', '!', '?', ':', ';'))
    
    def _enrich_chunk_content(self, chunk: BaseChunk, content: str) -> str:
        """Enrich chunk content with context for better retrieval."""
        try:
            # Use Docling's contextualize method if available
            if hasattr(self.docling_chunker, 'contextualize'):
                return self.docling_chunker.contextualize(chunk)
            else:
                # Fallback: add section context manually
                section_title, section_hierarchy = self._extract_section_info(chunk)
                
                if section_hierarchy:
                    context_prefix = " > ".join(section_hierarchy)
                    return f"[{context_prefix}] {content}"
                else:
                    return content
                    
        except Exception as e:
            self.logger.debug(f"Error enriching chunk content: {e}")
            return content
    
    def chunk_text(self, text: str, document_id: str = "") -> List[DocumentChunk]:
        """
        Chunk plain text when Docling document is not available.
        
        Args:
            text: Plain text to chunk
            document_id: Optional document identifier
            
        Returns:
            List of DocumentChunk objects
        """
        chunks = []
        
        # Simple sentence-aware chunking
        sentences = self._split_into_sentences(text)
        current_chunk = ""
        current_tokens = 0
        chunk_index = 0
        
        for sentence in sentences:
            sentence_tokens = self.count_tokens(sentence)
            
            # Check if adding this sentence would exceed chunk size
            if current_tokens + sentence_tokens > self.chunk_size and current_chunk:
                # Create chunk from current content
                chunk = self._create_text_chunk(
                    current_chunk.strip(), 
                    chunk_index, 
                    document_id
                )
                if chunk:
                    chunks.append(chunk)
                    chunk_index += 1
                
                # Start new chunk with overlap
                if self.chunk_overlap > 0:
                    overlap_text = self._get_overlap_text(current_chunk, self.chunk_overlap)
                    current_chunk = overlap_text + " " + sentence
                    current_tokens = self.count_tokens(current_chunk)
                else:
                    current_chunk = sentence
                    current_tokens = sentence_tokens
            else:
                current_chunk += " " + sentence if current_chunk else sentence
                current_tokens += sentence_tokens
        
        # Add final chunk
        if current_chunk.strip():
            chunk = self._create_text_chunk(
                current_chunk.strip(), 
                chunk_index, 
                document_id
            )
            if chunk:
                chunks.append(chunk)
        
        self.logger.info(f"Created {len(chunks)} chunks from text")
        return chunks
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        import re
        
        # Simple sentence splitting
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _get_overlap_text(self, text: str, overlap_tokens: int) -> str:
        """Get overlap text from the end of current chunk."""
        words = text.split()
        if overlap_tokens > 0 and len(words) > overlap_tokens:
            overlap_words = words[-overlap_tokens:]
            return " ".join(overlap_words)
        return ""
    
    def _create_text_chunk(self, content: str, index: int, document_id: str) -> Optional[DocumentChunk]:
        """Create a DocumentChunk from plain text."""
        if len(content.strip()) < self.min_chunk_size:
            return None
        
        token_count = self.count_tokens(content)
        char_count = len(content)
        
        chunk_id = f"{document_id}_chunk_{index}" if document_id else f"chunk_{index}"
        
        # Determine chunk type based on content keywords
        chunk_type = self._determine_text_chunk_type(content)
        
        metadata = ChunkMetadata(
            chunk_index=index,
            chunk_id=chunk_id,
            token_count=token_count,
            char_count=char_count,
            chunk_type=chunk_type,
            has_complete_sentences=self._has_complete_sentences(content),
            starts_mid_sentence=self._starts_mid_sentence(content),
            ends_mid_sentence=self._ends_mid_sentence(content)
        )
        
        return DocumentChunk(
            content=content,
            metadata=metadata,
            enriched_content=content  # No context enrichment for plain text
        )


def chunk_document(
    doc: DoclingDocument, 
    document_id: str = "",
    chunk_size: int = None,
    chunk_overlap: int = None,
    tokenizer_name: str = "tiktoken"
) -> List[DocumentChunk]:
    """
    Convenience function to chunk a Docling document.
    
    Args:
        doc: Docling document object
        document_id: Optional document identifier
        chunk_size: Target chunk size in tokens
        chunk_overlap: Overlap between chunks in tokens
        tokenizer_name: Tokenizer for token counting (supports "tiktoken" for OpenAI)
        
    Returns:
        List of DocumentChunk objects
    """
    # Use environment variables if parameters not provided
    chunk_size = chunk_size or int(os.getenv('CHUNK_SIZE', '512'))
    chunk_overlap = chunk_overlap or int(os.getenv('CHUNK_OVERLAP', '50'))
    
    chunker = StructureAwareChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        tokenizer_name=tokenizer_name
    )
    return chunker.chunk_document(doc, document_id)


def chunk_text(
    text: str,
    document_id: str = "",
    chunk_size: int = None,
    chunk_overlap: int = None,
    tokenizer_name: str = "tiktoken"
) -> List[DocumentChunk]:
    """
    Convenience function to chunk plain text.
    
    Args:
        text: Plain text to chunk
        document_id: Optional document identifier
        chunk_size: Target chunk size in tokens
        chunk_overlap: Overlap between chunks in tokens
        tokenizer_name: Tokenizer for token counting (supports "tiktoken" for OpenAI)
        
    Returns:
        List of DocumentChunk objects
    """
    # Use environment variables if parameters not provided
    chunk_size = chunk_size or int(os.getenv('CHUNK_SIZE', '512'))
    chunk_overlap = chunk_overlap or int(os.getenv('CHUNK_OVERLAP', '50'))
    
    chunker = StructureAwareChunker(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        tokenizer_name=tokenizer_name
    )
    return chunker.chunk_text(text, document_id)