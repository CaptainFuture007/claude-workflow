# 📚 Ingres Pipeline User Guide

*A simple guide to collecting and organizing information from websites, PDFs, and documents*

---

## 🎯 What Does This Tool Do?

Imagine you need to gather information from multiple sources - websites, PDF documents, and text files - and combine them into a single, well-organized document. That's exactly what the Ingres Pipeline does!

Think of it as a **smart document collector** that:
- 📖 **Reads** web pages, PDFs, and text documents
- 🔄 **Converts** everything into a readable format
- 📂 **Organizes** all the information in order
- 📄 **Creates** one combined document with everything you need

### Real-World Example
Let's say you're researching a topic and have:
- 3 web articles about the subject
- 2 PDF research papers
- Your own notes in a text file

Instead of jumping between all these sources, the Ingres Pipeline combines them into one organized document that you can read from start to finish.

---

## 📦 What You Get

After running the tool, you'll receive:

### 1. **Individual Files** 📄
Each source is saved as a separate, clean text file in the `content/` folder:
- Web pages → converted to readable text
- PDFs → extracted text with tables preserved
- Text files → cleaned up and formatted

### 2. **Combined Document** 📚
One master document (`concatenated_document.md`) that includes:
- **Table of Contents** - Quick links to each section
- **All Content in Order** - Everything arranged as you specified
- **Source Information** - Where each piece came from
- **Clean Formatting** - Easy to read and navigate

### Example Output Structure:
```
simple_output/
├── content/                          # Individual files
│   ├── pos00_website-article.md      # First item
│   ├── pos01_research-paper.md       # Second item
│   └── pos02_my-notes.md            # Third item
└── concatenated_document.md          # Everything combined
```

---

## 🚀 How to Use It

### Basic Usage - Three Simple Steps

#### Step 1: List Your Sources
Create a text file called `inputs.txt` with your sources:
```
https://example.com/article
./documents/research.pdf
./notes/my-notes.md
```

#### Step 2: Run the Tool
Open a command prompt/terminal and type:
```
python simple_cli.py --input-file inputs.txt
```

#### Step 3: Find Your Results
Look in the `simple_output` folder for your combined document!

### Direct Input Method
You can also specify sources directly:
```
python simple_cli.py "https://example.com" "./document.pdf" "./notes.md"
```

### Choosing Output Location
Want to save results somewhere specific?
```
python simple_cli.py --output-dir ./my-research --input-file inputs.txt
```

---

## 📖 Understanding Your Results

### The Combined Document Structure

Your final document will look like this:

```markdown
# Multi-Input Document Compilation

## Table of Contents
1. 🌐 Article Title - Web Page
2. 📄 Research Paper - PDF Document  
3. 📝 My Notes - Markdown File

---

## 🌐 Article Title
**Source**: https://example.com/article
**Type**: Web Page
**Position**: 1

[Content from the web article...]

---

## 📄 Research Paper
**Source**: ./documents/research.pdf
**Type**: PDF Document
**Position**: 2

[Content from the PDF...]
```

### What the Icons Mean
- 🌐 = Web page content
- 📄 = PDF document
- 📝 = Text/Markdown file

### Processing Information
After processing, you'll see a summary:
```
✅ Processing completed successfully!
   Processed: 3/3 inputs
   Duration: 5.2s
   Speed: 0.6 inputs/second
   📄 Concatenated document: simple_output/concatenated_document.md
```

---

## 💡 Common Use Cases

### 1. **Research Projects** 📚
Collecting information from multiple sources for a report:
```
https://wikipedia.org/wiki/Topic
https://scholarly-article.pdf
./my-research-notes.md
```

### 2. **Documentation Compilation** 📖
Combining various documentation sources:
```
https://docs.example.com/getting-started
https://docs.example.com/api-reference
./internal-notes.md
```

### 3. **News Aggregation** 📰
Gathering articles on a specific topic:
```
https://news-site.com/article1
https://news-site.com/article2
https://blog.example.com/analysis
```

### 4. **Learning Materials** 🎓
Creating a study guide from various sources:
```
https://tutorial-site.com/lesson1
./textbook-chapter.pdf
./class-notes.md
https://tutorial-site.com/lesson2
```

### 5. **Meeting Preparation** 💼
Combining relevant documents for a meeting:
```
./agenda.md
./previous-meeting-minutes.pdf
https://company.com/quarterly-report
./action-items.md
```

---

## 🎯 Tips for Best Results

### 1. **Order Matters** 📑
The tool processes sources in the exact order you list them. Put the most important content first!

### 2. **Check Your Files** ✅
Before running:
- Make sure PDF files aren't password-protected
- Verify web URLs are accessible
- Ensure local files exist in the specified locations

### 3. **Supported File Types** 📋
- **Web Pages**: Any public website URL
- **PDFs**: Local PDF files or PDF URLs
- **Text Files**: .md, .markdown, .txt files

### 4. **Processing Speed** ⚡
- **Web pages**: Usually 1-2 seconds each
- **PDFs**: 2-5 seconds depending on size
- **Text files**: Almost instant

### 5. **Handling Large Jobs** 📊
For many sources (10+):
- Use an input file instead of typing them all
- Check the preview with `--dry-run` first
- Consider breaking into smaller batches

### 6. **Preview Mode** 👀
Not sure what will be processed? Use dry-run:
```
python simple_cli.py --dry-run --input-file inputs.txt
```
This shows what would be processed without actually doing it.

---

## ❓ Frequently Asked Questions

### Q: Can I process password-protected PDFs?
**A:** No, PDFs must be unlocked/unprotected for the tool to read them.

### Q: What happens if a website is unavailable?
**A:** The tool will note the failure and continue processing other sources. You'll see which ones failed in the summary.

### Q: Can I process private/internal websites?
**A:** Only if they're accessible from your computer without login. The tool cannot handle login-protected pages.

### Q: How large can PDFs be?
**A:** PDFs up to 100 pages work well. Larger ones may take longer but will still process.

### Q: Can I change the order after processing?
**A:** You'll need to re-run with a new order. The combined document always reflects the input order.

### Q: Where do the results go?
**A:** By default, in a folder called `simple_output`. You can change this with `--output-dir`.

---

## 🔧 Quick Command Reference

| What You Want | Command |
|--------------|---------|
| Process files from a list | `python simple_cli.py --input-file inputs.txt` |
| Process specific files | `python simple_cli.py "url" "file.pdf" "notes.md"` |
| Save to specific folder | `python simple_cli.py --output-dir ./my-folder --input-file inputs.txt` |
| Preview without processing | `python simple_cli.py --dry-run --input-file inputs.txt` |
| See detailed output | `python simple_cli.py --verbose --input-file inputs.txt` |
| Process files faster | `python simple_cli.py --max-concurrent 5 --input-file inputs.txt` |

---

## 📞 Getting Help

If something isn't working:

1. **Check your inputs** - Are all files accessible? Are URLs correct?
2. **Try a simple test** - Start with just one web page to verify it's working
3. **Look at the error message** - It usually explains what went wrong
4. **Use verbose mode** - Add `--verbose` to see more details

### Example Test Run
Start with this simple test:
```
python simple_cli.py "https://example.com"
```

If this works, your setup is correct!

---

## 🎉 Summary

The Ingres Pipeline is your helpful assistant for gathering and organizing information from multiple sources. It:

✅ **Saves time** - No more copy-pasting from multiple sources  
✅ **Maintains order** - Everything stays in the sequence you specified  
✅ **Creates clean output** - Easy-to-read formatted documents  
✅ **Handles mixed sources** - Websites, PDFs, and text files all together  
✅ **Works reliably** - Continues even if some sources fail  

Just remember: **List your sources → Run the tool → Get your organized document!**

---

*Happy document collecting! 📚*