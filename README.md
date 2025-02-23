# ml-ai-professional-cert

## Tools Directory (`_tools/`)

This directory contains various utility scripts to help manage course materials and sync with Notion. Here's what each tool does:

### `notebook_commit.py`
A tool that helps commit Jupyter notebooks and sync them with Notion. It:
- Commits changes to git
- Generates GitHub and Colab URLs for changed notebooks
- Syncs the URLs to Notion
- Requires Notion API token in `.env` file

Usage:
```bash
python _tools/notebook_commit.py
# Follow the prompts to enter commit message
```

### `notion_md_sync.py`
Syncs markdown files to Notion pages. Features include:
- Automatic detection of module structure
- Markdown to Notion block conversion
- Table parsing and syncing
- Header-based page organization

Usage:
```bash
# Sync a markdown file to Notion
python _tools/notion_md_sync.py module1/notes.md

# Force create new page even if one exists
python _tools/notion_md_sync.py module1/notes.md --new
```

### `notion_inspector.py`
Helps inspect and manage Notion page hierarchy. Can:
- List all pages in the hierarchy
- Inspect specific module structures
- Find module notes organization

Usage:
```bash
# List all pages in hierarchy
python _tools/notion_inspector.py --list

# Inspect specific module structure
python _tools/notion_inspector.py --inspect 18 --title "Optional Module Title"
```

### `sync_notebook.py`
Syncs a single Jupyter notebook to Notion. Useful for:
- One-off notebook syncs
- Testing notebook conversion
- Debugging sync issues

Usage:
```bash
python _tools/sync_notebook.py module19/colab_activity19_1_starter/colab_activity_19_1.ipynb
```

### `pdf_to_md.py`
Converts PDF files to Markdown format with smart formatting:
- Cleans and formats extracted text
- Handles code blocks and math terms
- Improves paragraph formatting
- Preserves document structure

Usage:
```bash
# Basic conversion
python _tools/pdf_to_md.py input.pdf

# Specify output file
python _tools/pdf_to_md.py input.pdf -o output.md
```

## Setup

1. Install required dependencies:
```bash
pip install -r _tools/requirements.txt
```

2. Set up Notion integration:
   - Create a `.env` file in the root directory
   - Add your Notion API token: `NOTION_TOKEN=your_token_here`
