"""
Document Stitcher - Combines crawled pages in navigation order

Creates a single, well-organized markdown document from multiple crawled pages,
preserving the intended reading order based on site navigation.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set, Any
from dataclasses import dataclass
from datetime import datetime
from urllib.parse import urlparse, urldefrag
import yaml

from .navigation_extractor import NavigationNode


@dataclass
class PageContent:
    """Represents a single page's content with metadata."""
    url: str
    title: str
    content: str
    filepath: Path
    depth: int
    crawled_at: str
    nav_position: Optional[int] = None
    nav_breadcrumb: Optional[List[str]] = None
    nav_level: Optional[int] = None


class DocumentStitcher:
    """
    Stitches together multiple markdown files into a single document
    following the navigation structure of the original website.
    """
    
    def __init__(
        self, 
        content_dir: Path,
        navigation_tree: Optional[NavigationNode] = None,
        output_file: str = "stitched_document.md"
    ):
        self.content_dir = Path(content_dir)
        self.navigation_tree = navigation_tree
        self.output_file = Path(output_file)
        self.pages: List[PageContent] = []
        self.url_to_page: Dict[str, PageContent] = {}
        self.unmatched_pages: List[PageContent] = []
        
    def load_content(self) -> int:
        """
        Load all markdown files from the content directory.
        
        Returns:
            Number of files loaded
        """
        md_files = list(self.content_dir.glob("*.md"))
        
        for filepath in md_files:
            # Skip summary files
            if filepath.name in ['crawl_summary.md', 'stitched_document.md']:
                continue
            
            content = filepath.read_text(encoding='utf-8')
            
            # Extract metadata from frontmatter
            metadata = self._extract_frontmatter(content)
            if not metadata:
                continue
            
            # Extract clean content (without frontmatter)
            clean_content = self._remove_frontmatter(content)
            
            page = PageContent(
                url=self._normalize_url(metadata.get('url', '')),
                title=metadata.get('title', 'Untitled'),
                content=clean_content,
                filepath=filepath,
                depth=metadata.get('depth', 0),
                crawled_at=metadata.get('crawled_at', '')
            )
            
            self.pages.append(page)
            self.url_to_page[page.url] = page
        
        return len(self.pages)
    
    def _normalize_url(self, url: str) -> str:
        """Normalize URL for comparison."""
        url = urldefrag(url)[0]
        if url.endswith('/'):
            url = url[:-1]
        return url
    
    def _extract_frontmatter(self, content: str) -> Optional[Dict]:
        """Extract YAML frontmatter from markdown content."""
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)
        
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except:
                return None
        return None
    
    def _remove_frontmatter(self, content: str) -> str:
        """Remove YAML frontmatter from markdown content."""
        pattern = r'^---\s*\n.*?\n---\s*\n'
        return re.sub(pattern, '', content, flags=re.DOTALL).strip()
    
    def match_to_navigation(self, ordered_urls: List[Dict]) -> Tuple[List[PageContent], List[PageContent]]:
        """
        Match loaded pages to navigation positions.
        
        Args:
            ordered_urls: List of URLs in navigation order from NavigationExtractor
        
        Returns:
            Tuple of (matched_pages, unmatched_pages)
        """
        matched = []
        unmatched = []
        matched_urls = set()
        
        # First pass: exact URL matches
        for nav_item in ordered_urls:
            nav_url = self._normalize_url(nav_item['url'])
            
            if nav_url in self.url_to_page:
                page = self.url_to_page[nav_url]
                page.nav_position = nav_item['order']
                page.nav_breadcrumb = nav_item['breadcrumb']
                page.nav_level = nav_item['level']
                matched.append(page)
                matched_urls.add(nav_url)
        
        # Second pass: fuzzy matching for redirects and variations
        for nav_item in ordered_urls:
            if nav_item['url'] in matched_urls:
                continue
            
            nav_url = self._normalize_url(nav_item['url'])
            nav_path = urlparse(nav_url).path
            
            for page_url, page in self.url_to_page.items():
                if page_url in matched_urls:
                    continue
                
                page_path = urlparse(page_url).path
                
                # Check if paths match (ignoring domain differences)
                if nav_path == page_path:
                    page.nav_position = nav_item['order']
                    page.nav_breadcrumb = nav_item['breadcrumb']
                    page.nav_level = nav_item['level']
                    matched.append(page)
                    matched_urls.add(page_url)
                    break
        
        # Collect unmatched pages
        for page_url, page in self.url_to_page.items():
            if page_url not in matched_urls:
                unmatched.append(page)
        
        return matched, unmatched
    
    def stitch_document(
        self,
        matched_pages: List[PageContent],
        unmatched_pages: List[PageContent],
        include_unmatched: bool = True
    ) -> str:
        """
        Create a single stitched document from all pages.
        
        Args:
            matched_pages: Pages matched to navigation positions
            unmatched_pages: Pages not found in navigation
            include_unmatched: Whether to include unmatched pages at the end
        
        Returns:
            The complete stitched document as markdown
        """
        sections = []
        
        # Add document header
        sections.append(self._create_document_header())
        
        # Add table of contents
        toc = self._create_table_of_contents(matched_pages, unmatched_pages, include_unmatched)
        sections.append(toc)
        
        # Add matched pages in navigation order
        if matched_pages:
            sections.append("\n---\n\n# 📖 Main Content\n\n")
            
            # Sort by navigation position
            sorted_pages = sorted(matched_pages, key=lambda p: p.nav_position or 999)
            
            current_section = None
            for page in sorted_pages:
                # Add section headers based on breadcrumb changes
                if page.nav_breadcrumb and len(page.nav_breadcrumb) > 1:
                    section = page.nav_breadcrumb[0] if len(page.nav_breadcrumb) > 0 else "Content"
                    if section != current_section:
                        sections.append(f"\n\n## 📂 {section}\n\n")
                        current_section = section
                
                # Add page content
                page_section = self._create_page_section(page)
                sections.append(page_section)
        
        # Add unmatched pages if requested
        if include_unmatched and unmatched_pages:
            sections.append("\n---\n\n# 📎 Additional Content\n\n")
            sections.append("*The following pages were crawled but not found in the main navigation:*\n\n")
            
            # Sort by depth and title
            sorted_unmatched = sorted(unmatched_pages, key=lambda p: (p.depth, p.title))
            
            for page in sorted_unmatched:
                page_section = self._create_page_section(page)
                sections.append(page_section)
        
        # Add document footer
        sections.append(self._create_document_footer(len(matched_pages), len(unmatched_pages)))
        
        return "\n".join(sections)
    
    def _create_document_header(self) -> str:
        """Create the document header with metadata."""
        return f"""# 📚 Complete Documentation

> *This document was automatically generated by stitching together multiple pages in their navigation order.*
> 
> **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> **Total Pages**: {len(self.pages)}

---
"""
    
    def _create_table_of_contents(
        self,
        matched_pages: List[PageContent],
        unmatched_pages: List[PageContent],
        include_unmatched: bool
    ) -> str:
        """Create a table of contents with internal links."""
        toc_lines = ["## 📑 Table of Contents\n"]
        
        if matched_pages:
            toc_lines.append("### Main Content\n")
            
            # Sort by navigation position
            sorted_pages = sorted(matched_pages, key=lambda p: p.nav_position or 999)
            
            current_section = None
            for page in sorted_pages:
                # Add section headers
                if page.nav_breadcrumb and len(page.nav_breadcrumb) > 1:
                    section = page.nav_breadcrumb[0]
                    if section != current_section:
                        toc_lines.append(f"\n**{section}**\n")
                        current_section = section
                
                # Create anchor link
                anchor = self._create_anchor(page.title)
                indent = "  " * (page.nav_level if page.nav_level else 0)
                toc_lines.append(f"{indent}- [{page.title}](#{anchor})")
        
        if include_unmatched and unmatched_pages:
            toc_lines.append("\n### Additional Content\n")
            for page in sorted(unmatched_pages, key=lambda p: p.title):
                anchor = self._create_anchor(page.title)
                toc_lines.append(f"- [{page.title}](#{anchor})")
        
        return "\n".join(toc_lines)
    
    def _create_page_section(self, page: PageContent) -> str:
        """Create a section for a single page."""
        lines = []
        
        # Add navigation breadcrumb if available
        if page.nav_breadcrumb and len(page.nav_breadcrumb) > 1:
            breadcrumb = " > ".join(page.nav_breadcrumb)
            lines.append(f"*{breadcrumb}*\n")
        
        # Add page title with anchor
        anchor = self._create_anchor(page.title)
        lines.append(f"<a id=\"{anchor}\"></a>\n")
        lines.append(f"### 📄 {page.title}\n")
        
        # Add source URL
        lines.append(f"*Source: [{page.url}]({page.url})*\n")
        
        # Add content
        lines.append(page.content)
        
        # Add separator
        lines.append("\n---\n")
        
        return "\n".join(lines)
    
    def _create_anchor(self, title: str) -> str:
        """Create a valid anchor ID from a title."""
        # Remove special characters and convert to lowercase
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        # Replace spaces with hyphens
        anchor = re.sub(r'\s+', '-', anchor)
        return anchor
    
    def _create_document_footer(self, matched_count: int, unmatched_count: int) -> str:
        """Create the document footer with statistics."""
        return f"""
---

## 📊 Document Statistics

- **Pages in Navigation Order**: {matched_count}
- **Additional Pages**: {unmatched_count}
- **Total Pages**: {matched_count + unmatched_count}
- **Document Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

*End of Document*
"""
    
    def save_stitched_document(self, content: str) -> Path:
        """Save the stitched document to file."""
        output_path = self.content_dir / self.output_file
        output_path.write_text(content, encoding='utf-8')
        return output_path
    
    def create_reading_guide(self, matched_pages: List[PageContent]) -> str:
        """Create a reading guide showing the recommended order."""
        guide_lines = ["# 📖 Reading Guide\n"]
        guide_lines.append("This guide shows the recommended reading order based on the site's navigation structure.\n")
        
        if not matched_pages:
            guide_lines.append("*No pages were matched to the navigation structure.*")
            return "\n".join(guide_lines)
        
        sorted_pages = sorted(matched_pages, key=lambda p: p.nav_position or 999)
        
        current_section = None
        for idx, page in enumerate(sorted_pages, 1):
            if page.nav_breadcrumb and len(page.nav_breadcrumb) > 1:
                section = page.nav_breadcrumb[0]
                if section != current_section:
                    guide_lines.append(f"\n## {section}\n")
                    current_section = section
            
            guide_lines.append(f"{idx}. **{page.title}**")
            if page.nav_breadcrumb:
                guide_lines.append(f"   - Path: {' > '.join(page.nav_breadcrumb)}")
            guide_lines.append(f"   - File: {page.filepath.name}")
            guide_lines.append("")
        
        return "\n".join(guide_lines)


def stitch_crawled_content(
    content_dir: str,
    navigation_tree: Optional[NavigationNode] = None,
    ordered_urls: Optional[List[Dict]] = None,
    output_file: str = "stitched_document.md",
    include_unmatched: bool = True,
    progress_tracker: Optional[Any] = None
) -> Path:
    """
    Main function to stitch crawled content into a single document.
    
    Args:
        content_dir: Directory containing crawled markdown files
        navigation_tree: NavigationNode tree from NavigationExtractor
        ordered_urls: Ordered list of URLs from navigation
        output_file: Name of the output file
        include_unmatched: Whether to include pages not in navigation
        progress_tracker: Optional progress tracker for status updates
    
    Returns:
        Path to the created stitched document
    """
    stitcher = DocumentStitcher(content_dir, navigation_tree, output_file)
    
    # Load all content
    if progress_tracker:
        stitch_task = progress_tracker.create_task(
            "stitching",
            "📝 Loading and organizing content",
            total=None
        )
        progress_tracker.update_task("stitching", current_item="Loading markdown files...")
    
    num_loaded = stitcher.load_content()
    
    if progress_tracker:
        progress_tracker.log(f"Loaded {num_loaded} pages from {content_dir}")
    else:
        print(f"Loaded {num_loaded} pages from {content_dir}")
    
    if ordered_urls:
        if progress_tracker:
            progress_tracker.update_task("stitching", current_item="Matching pages to navigation...")
        
        # Match pages to navigation
        matched, unmatched = stitcher.match_to_navigation(ordered_urls)
        
        if progress_tracker:
            progress_tracker.log(f"Matched {len(matched)} pages to navigation, {len(unmatched)} additional pages")
            progress_tracker.update_task("stitching", current_item="Creating stitched document...")
        else:
            print(f"Matched {len(matched)} pages to navigation")
            print(f"Found {len(unmatched)} additional pages")
        
        # Create stitched document
        stitched_content = stitcher.stitch_document(matched, unmatched, include_unmatched)
        
        if progress_tracker:
            progress_tracker.update_task("stitching", current_item="Generating reading guide...")
        
        # Save reading guide
        guide = stitcher.create_reading_guide(matched)
        guide_path = Path(content_dir) / "reading_guide.md"
        guide_path.write_text(guide, encoding='utf-8')
        
        if progress_tracker:
            progress_tracker.log(f"Reading guide saved to {guide_path.name}")
        else:
            print(f"Reading guide saved to {guide_path}")
    else:
        if progress_tracker:
            progress_tracker.log("No navigation structure provided - using depth-based ordering")
            progress_tracker.update_task("stitching", current_item="Organizing by depth...")
        else:
            print("No navigation structure provided - using depth-based ordering")
        
        sorted_pages = sorted(stitcher.pages, key=lambda p: (p.depth, p.title))
        stitched_content = stitcher.stitch_document(sorted_pages, [], False)
    
    # Save stitched document
    if progress_tracker:
        progress_tracker.update_task("stitching", current_item="Saving final document...")
    
    output_path = stitcher.save_stitched_document(stitched_content)
    
    if progress_tracker:
        progress_tracker.complete_task("stitching", f"✅ Stitched document saved to {output_path.name}")
    else:
        print(f"Stitched document saved to {output_path}")
    
    return output_path


if __name__ == "__main__":
    # Example usage
    import asyncio
    from .navigation_extractor import NavigationExtractor
    
    async def main():
        # Extract navigation from a website
        extractor = NavigationExtractor("https://example.com")
        navigation = await extractor.extract()
        
        if navigation:
            ordered_urls = extractor.get_ordered_urls()
            
            # Stitch crawled content
            output = stitch_crawled_content(
                content_dir="crawled_content",
                navigation_tree=navigation,
                ordered_urls=ordered_urls,
                include_unmatched=True
            )
            
            print(f"\n✅ Document stitched successfully: {output}")
    
    asyncio.run(main())