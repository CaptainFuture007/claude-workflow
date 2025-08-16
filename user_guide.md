# Website Content Crawler - User Guide

## What Does This Tool Do?

The Website Content Crawler is like a smart assistant that visits websites for you and saves their content in an organized, readable format. Think of it as a digital librarian that:

- Visits a website you specify
- Reads and extracts the main content (articles, blog posts, documentation)
- Follows links to related pages (like clicking through a website manually)
- Saves everything as clean, readable documents on your computer

## What You Get

After running the crawler, you'll receive:

### 📁 Individual Page Files
- Each webpage is saved as a separate `.md` (Markdown) file
- Files are named clearly so you know what they contain
- Each file includes:
  - The page's title
  - The main content (without ads, menus, or sidebars)
  - The original web address (URL)
  - When it was downloaded

### 📊 Summary Report
A single overview file (`crawl_summary.md`) that shows:
- How many pages were successfully downloaded
- A list of all saved files with links
- Any pages that couldn't be accessed
- Statistics about your crawl

## How to Use It

### Basic Usage

1. **Specify a website**: Provide the starting web address (like `https://example.com`)

2. **Set the depth**: Choose how many "clicks deep" to go
   - Depth 0 = Just the starting page
   - Depth 1 = Starting page + all pages it links to
   - Depth 2 = All of the above + pages those link to
   - (Recommended: Start with depth 1 or 2)

3. **Choose output location**: Specify where to save the files (default: `crawled_content` folder)

4. **Run and wait**: The crawler will work automatically and show progress

### Example Scenarios

**Research a Topic:**
```
Starting URL: https://docs.example.com/getting-started
Depth: 2
Result: All getting-started documentation and related guides
```

**Archive a Blog:**
```
Starting URL: https://blog.example.com
Depth: 1
Result: Main blog page and all recent posts
```

**Save Documentation:**
```
Starting URL: https://help.example.com/user-manual
Depth: 3
Result: Complete user manual with all sub-sections
```

## Understanding Your Results

### File Organization

Files are organized by how "deep" they were found:
- `depth0_index.md` - The starting page
- `depth1_blog_post.md` - Pages linked from the starting page
- `depth2_tutorial_advanced.md` - Pages found two clicks away

### Reading the Files

Each saved file can be opened with:
- Any text editor (Notepad, TextEdit, etc.)
- Word processors (Microsoft Word, Google Docs)
- Markdown readers (for better formatting)
- Web browsers (drag and drop the file)

### The Summary File

Open `crawl_summary.md` first to see:
- What was successfully saved
- Quick links to all downloaded pages
- Any issues encountered

## Common Use Cases

### 📚 Research & Documentation
- Save online documentation for offline reading
- Collect articles on a specific topic
- Archive tutorials and guides

### 📰 Content Archiving
- Preserve blog posts before they're updated
- Save news articles for future reference
- Create backups of important web content

### 📖 Offline Reading
- Download content to read without internet
- Create portable documentation
- Build a personal knowledge library

### 🔍 Content Analysis
- Gather website content for review
- Extract text for analysis or translation
- Compile information from multiple pages

## Tips for Best Results

### Choose the Right Depth
- **Depth 1-2**: Best for most purposes
- **Depth 3+**: Only for comprehensive archiving (takes longer)
- Start small and increase if needed

### Target Specific Sections
- Use specific URLs like `/blog` or `/docs` instead of the homepage
- This gives you more relevant content with less noise

### Check Available Space
- Each depth level can multiply the number of pages
- Ensure you have enough disk space
- A typical crawl might save 10-500 files

### Understanding Limitations
- Only saves text content (not videos or interactive features)
- Stays within the same website (won't jump to other sites)
- Skips login-required pages
- Excludes files like PDFs, ZIPs, etc.

## Troubleshooting

### "No content extracted"
- The page might require login
- The page might be mostly images/videos
- Try a different starting URL

### "Failed to access"
- The website might be temporarily down
- The page might not exist anymore
- Your internet connection might be interrupted

### Taking too long
- Reduce the depth setting
- Start with a more specific URL
- The website might be very large

## Output Example

After crawling a documentation site, your folder might look like:

```
crawled_content/
├── crawl_summary.md          (Overview and statistics)
├── depth0_index.md           (Homepage)
├── depth1_getting_started.md (Getting Started guide)
├── depth1_installation.md    (Installation guide)
├── depth2_windows_setup.md   (Windows-specific instructions)
├── depth2_mac_setup.md       (Mac-specific instructions)
└── depth2_troubleshooting.md (Common problems and solutions)
```

## Privacy & Ethics

- Only crawl websites you have permission to access
- Respect website terms of service
- Don't overload websites (the tool manages this automatically)
- Downloaded content is for personal use unless otherwise permitted

## Getting Help

If you encounter issues or have questions:
1. Check the `crawl_summary.md` file for error messages
2. Try reducing the depth or using a different starting URL
3. Ensure you have a stable internet connection
4. Verify the website is accessible in your browser

---

*This tool helps you create your own organized library of web content, making online information accessible offline and easier to review.*