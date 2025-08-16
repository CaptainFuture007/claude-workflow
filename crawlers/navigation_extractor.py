"""
Navigation Structure Extractor using Playwright

Extracts the navigation hierarchy from websites to determine the correct
reading order for documentation and content.
"""

import asyncio
import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse, urldefrag
import json

from playwright.async_api import async_playwright, Page, ElementHandle


@dataclass
class NavigationNode:
    """Represents a node in the navigation hierarchy."""
    title: str
    url: str
    level: int
    order: int
    children: List['NavigationNode'] = field(default_factory=list)
    parent: Optional['NavigationNode'] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'title': self.title,
            'url': self.url,
            'level': self.level,
            'order': self.order,
            'children': [child.to_dict() for child in self.children]
        }
    
    def get_all_urls(self) -> List[str]:
        """Get all URLs in this branch of the tree."""
        urls = [self.url] if self.url else []
        for child in self.children:
            urls.extend(child.get_all_urls())
        return urls


class NavigationExtractor:
    """
    Extracts navigation structure from websites using various strategies.
    """
    
    # Common navigation selectors
    NAVIGATION_SELECTORS = [
        'nav',
        '[role="navigation"]',
        'aside nav',
        '.sidebar',
        '#sidebar',
        '.navigation',
        '#navigation',
        '.toc',
        '#toc',
        '.menu',
        '#menu',
        '[class*="nav-"]',
        '[class*="sidebar"]',
        '[id*="nav-"]',
        '[id*="sidebar"]'
    ]
    
    # Selectors that likely contain main navigation
    PRIORITY_SELECTORS = [
        'nav[aria-label*="main"]',
        'nav[aria-label*="primary"]',
        '.main-nav',
        '.primary-nav',
        '#main-nav',
        '#primary-nav',
        '[role="navigation"][aria-label*="main"]'
    ]
    
    def __init__(self, base_url: str, progress_tracker: Optional[Any] = None):
        self.base_url = self._normalize_url(base_url)
        self.base_domain = urlparse(base_url).netloc
        self.navigation_tree: Optional[NavigationNode] = None
        self.progress_tracker = progress_tracker
        
    def _normalize_url(self, url: str) -> str:
        """Normalize URL for comparison."""
        url = urldefrag(url)[0]
        if url.endswith('/'):
            url = url[:-1]
        return url
    
    def _make_absolute_url(self, url: str) -> str:
        """Convert relative URL to absolute."""
        if not url:
            return ""
        if url.startswith(('http://', 'https://')):
            return url
        if url.startswith('#'):
            return ""  # Skip anchor links
        return urljoin(self.base_url, url)
    
    async def extract(self) -> NavigationNode:
        """
        Extract navigation structure from the website.
        
        Returns:
            Root NavigationNode containing the entire navigation tree
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            try:
                if self.progress_tracker:
                    self.progress_tracker.update_task(
                        "nav_extraction",
                        current_item="Loading website..."
                    )
                
                await page.goto(self.base_url, wait_until='networkidle', timeout=30000)
                
                # Try different extraction strategies
                if self.progress_tracker:
                    self.progress_tracker.update_task(
                        "nav_extraction",
                        current_item="Analyzing semantic navigation..."
                    )
                navigation = await self._extract_semantic_navigation(page)
                
                if not navigation or len(navigation.children) == 0:
                    if self.progress_tracker:
                        self.progress_tracker.update_task(
                            "nav_extraction",
                            current_item="Trying pattern-based extraction..."
                        )
                    navigation = await self._extract_by_patterns(page)
                
                if not navigation or len(navigation.children) == 0:
                    if self.progress_tracker:
                        self.progress_tracker.update_task(
                            "nav_extraction",
                            current_item="Analyzing link clusters..."
                        )
                    navigation = await self._extract_link_clusters(page)
                
                if not navigation or len(navigation.children) == 0:
                    if self.progress_tracker:
                        self.progress_tracker.update_task(
                            "nav_extraction",
                            current_item="Checking sitemap..."
                        )
                    navigation = await self._extract_from_sitemap(page)
                
                self.navigation_tree = navigation
                
            finally:
                await browser.close()
        
        return self.navigation_tree
    
    async def _extract_semantic_navigation(self, page: Page) -> Optional[NavigationNode]:
        """Extract navigation using semantic HTML elements."""
        
        # Try priority selectors first
        for selector in self.PRIORITY_SELECTORS:
            nav_element = await page.query_selector(selector)
            if nav_element:
                navigation = await self._parse_navigation_element(page, nav_element, selector)
                if navigation and len(navigation.children) > 0:
                    return navigation
        
        # Try general navigation selectors
        for selector in self.NAVIGATION_SELECTORS:
            nav_element = await page.query_selector(selector)
            if nav_element:
                navigation = await self._parse_navigation_element(page, nav_element, selector)
                if navigation and len(navigation.children) > 0:
                    return navigation
        
        return None
    
    async def _parse_navigation_element(self, page: Page, element: ElementHandle, selector: str) -> Optional[NavigationNode]:
        """Parse a navigation element into a tree structure."""
        
        # Extract all links within the navigation element
        links_data = await page.evaluate('''(element) => {
            const links = [];
            const processedUrls = new Set();
            
            function extractLinks(el, level = 0) {
                // Find all links in the current element
                const linkElements = el.querySelectorAll('a');
                
                linkElements.forEach((link, index) => {
                    const href = link.getAttribute('href');
                    if (!href || href === '#' || processedUrls.has(href)) return;
                    
                    processedUrls.add(href);
                    
                    // Determine the hierarchy level
                    let linkLevel = level;
                    let parent = link.parentElement;
                    let nestingLevel = 0;
                    
                    while (parent && parent !== el) {
                        if (parent.tagName === 'UL' || parent.tagName === 'OL') {
                            nestingLevel++;
                        }
                        parent = parent.parentElement;
                    }
                    
                    links.push({
                        text: link.textContent.trim(),
                        href: href,
                        level: nestingLevel,
                        order: index,
                        classes: link.className,
                        isActive: link.classList.contains('active') || 
                                 link.getAttribute('aria-current') === 'page'
                    });
                });
            }
            
            extractLinks(element);
            return links;
        }''', element)
        
        if not links_data:
            return None
        
        # Build navigation tree
        root = NavigationNode(
            title=f"Navigation ({selector})",
            url="",
            level=-1,
            order=0
        )
        
        # Group links by level and create hierarchy
        level_nodes = {-1: root}
        
        for link_info in links_data:
            url = self._make_absolute_url(link_info['href'])
            if not url or not self._is_internal_url(url):
                continue
            
            node = NavigationNode(
                title=link_info['text'],
                url=self._normalize_url(url),
                level=link_info['level'],
                order=link_info['order']
            )
            
            # Find parent node
            parent_level = link_info['level'] - 1
            if parent_level in level_nodes:
                parent = level_nodes[parent_level]
            else:
                parent = root
            
            parent.children.append(node)
            node.parent = parent
            level_nodes[link_info['level']] = node
        
        return root
    
    async def _extract_by_patterns(self, page: Page) -> Optional[NavigationNode]:
        """Extract navigation by looking for common patterns."""
        
        # Look for lists of links that appear to be navigation
        nav_data = await page.evaluate('''() => {
            const possibleNavs = [];
            
            // Find all UL/OL elements with multiple links
            const lists = document.querySelectorAll('ul, ol');
            
            for (const list of lists) {
                const links = list.querySelectorAll('a');
                if (links.length < 3) continue;  // Need at least 3 links
                
                // Check if this looks like navigation
                const linkTexts = Array.from(links).map(l => l.textContent.trim());
                const hasNavigationalWords = linkTexts.some(text => 
                    /^(home|about|docs|documentation|guide|tutorial|reference|api|blog|contact)/i.test(text)
                );
                
                if (hasNavigationalWords) {
                    const linkData = Array.from(links).map((link, index) => ({
                        text: link.textContent.trim(),
                        href: link.getAttribute('href'),
                        order: index
                    }));
                    
                    possibleNavs.push({
                        selector: 'pattern-based',
                        links: linkData
                    });
                }
            }
            
            return possibleNavs[0];  // Return the first match
        }''')
        
        if not nav_data or not nav_data.get('links'):
            return None
        
        root = NavigationNode(
            title="Navigation (pattern-based)",
            url="",
            level=-1,
            order=0
        )
        
        for idx, link_info in enumerate(nav_data['links']):
            url = self._make_absolute_url(link_info['href'])
            if not url or not self._is_internal_url(url):
                continue
            
            node = NavigationNode(
                title=link_info['text'],
                url=self._normalize_url(url),
                level=0,
                order=idx
            )
            root.children.append(node)
            node.parent = root
        
        return root
    
    async def _extract_link_clusters(self, page: Page) -> Optional[NavigationNode]:
        """Extract navigation by finding clusters of related links."""
        
        # Get all internal links on the page
        links_data = await page.evaluate('''() => {
            const links = [];
            const linkElements = document.querySelectorAll('a[href]');
            
            linkElements.forEach((link, index) => {
                const href = link.getAttribute('href');
                if (!href || href === '#') return;
                
                links.push({
                    text: link.textContent.trim(),
                    href: href,
                    parent: link.parentElement?.tagName,
                    order: index
                });
            });
            
            return links;
        }''')
        
        if not links_data:
            return None
        
        # Filter for internal links and group by parent element
        internal_links = []
        for link_info in links_data:
            url = self._make_absolute_url(link_info['href'])
            if url and self._is_internal_url(url):
                link_info['url'] = self._normalize_url(url)
                internal_links.append(link_info)
        
        if len(internal_links) < 3:
            return None
        
        # Create a simple flat navigation from the first 20 internal links
        root = NavigationNode(
            title="Navigation (link-based)",
            url="",
            level=-1,
            order=0
        )
        
        for idx, link_info in enumerate(internal_links[:20]):
            node = NavigationNode(
                title=link_info['text'] or f"Page {idx + 1}",
                url=link_info['url'],
                level=0,
                order=idx
            )
            root.children.append(node)
            node.parent = root
        
        return root
    
    async def _extract_from_sitemap(self, page: Page) -> Optional[NavigationNode]:
        """Try to extract navigation from sitemap if available."""
        
        # Check for sitemap link
        sitemap_url = urljoin(self.base_url, '/sitemap.xml')
        
        try:
            response = await page.goto(sitemap_url, wait_until='domcontentloaded', timeout=10000)
            if response and response.status == 200:
                # Parse sitemap XML
                sitemap_data = await page.evaluate('''() => {
                    const urls = [];
                    const urlElements = document.querySelectorAll('url loc');
                    urlElements.forEach(el => {
                        urls.push(el.textContent);
                    });
                    return urls;
                }''')
                
                if sitemap_data:
                    root = NavigationNode(
                        title="Navigation (sitemap)",
                        url="",
                        level=-1,
                        order=0
                    )
                    
                    for idx, url in enumerate(sitemap_data[:30]):  # Limit to 30 URLs
                        if self._is_internal_url(url):
                            # Extract title from URL path
                            path = urlparse(url).path
                            title = path.strip('/').replace('-', ' ').replace('_', ' ').title()
                            if not title:
                                title = "Home"
                            
                            node = NavigationNode(
                                title=title,
                                url=self._normalize_url(url),
                                level=0,
                                order=idx
                            )
                            root.children.append(node)
                            node.parent = root
                    
                    return root
        except:
            pass
        
        return None
    
    def _is_internal_url(self, url: str) -> bool:
        """Check if URL belongs to the same domain."""
        if not url:
            return False
        parsed = urlparse(url)
        return parsed.netloc == self.base_domain or parsed.netloc == ""
    
    def find_position(self, url: str) -> Optional[Tuple[int, List[str]]]:
        """
        Find the position of a URL in the navigation tree.
        
        Returns:
            Tuple of (position_index, breadcrumb_path) or None if not found
        """
        if not self.navigation_tree:
            return None
        
        normalized_url = self._normalize_url(url)
        position = [0]
        
        def search_tree(node: NavigationNode, path: List[str], pos: List[int]) -> Optional[Tuple[int, List[str]]]:
            if node.url == normalized_url:
                return (pos[0], path + [node.title])
            
            for child in node.children:
                pos[0] += 1
                result = search_tree(child, path + [node.title] if node.title else path, pos)
                if result:
                    return result
            
            return None
        
        return search_tree(self.navigation_tree, [], position)
    
    def get_ordered_urls(self) -> List[Dict[str, Any]]:
        """
        Get all URLs in navigation order with metadata.
        
        Returns:
            List of dictionaries with url, title, level, and breadcrumb
        """
        if not self.navigation_tree:
            return []
        
        ordered = []
        
        def traverse(node: NavigationNode, breadcrumb: List[str]):
            if node.url:
                ordered.append({
                    'url': node.url,
                    'title': node.title,
                    'level': node.level,
                    'breadcrumb': breadcrumb + [node.title],
                    'order': len(ordered)
                })
            
            for child in node.children:
                traverse(child, breadcrumb + [node.title] if node.title else breadcrumb)
        
        traverse(self.navigation_tree, [])
        return ordered
    
    def export_structure(self, filepath: str):
        """Export navigation structure to JSON file."""
        if self.navigation_tree:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.navigation_tree.to_dict(), f, indent=2)
    
    def print_structure(self):
        """Print the navigation structure for debugging."""
        if not self.navigation_tree:
            print("No navigation structure extracted")
            return
        
        def print_node(node: NavigationNode, indent: int = 0):
            if node.url:
                print(f"{'  ' * indent}├─ {node.title} ({node.url})")
            for child in node.children:
                print_node(child, indent + 1)
        
        print("\n=== Navigation Structure ===")
        print_node(self.navigation_tree)


async def main():
    """Example usage."""
    extractor = NavigationExtractor("https://docs.anthropic.com/en/docs/claude-code/")
    navigation = await extractor.extract()
    
    if navigation:
        extractor.print_structure()
        
        # Get ordered URLs
        ordered = extractor.get_ordered_urls()
        print(f"\nFound {len(ordered)} pages in navigation order")
        
        # Export structure
        extractor.export_structure("navigation_structure.json")
        print("Navigation structure exported to navigation_structure.json")


if __name__ == "__main__":
    asyncio.run(main())