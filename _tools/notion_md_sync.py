import os
import sys
import re
from notion_client import Client
from dotenv import load_dotenv
import json
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
import markdown
import argparse

def setup_notion_client() -> Client:
    """Setup Notion client with token from .env file or environment"""
    load_dotenv()
    token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError(
            "Please set your NOTION_TOKEN environment variable or create a .env file with NOTION_TOKEN=your_token"
        )

    return Client(auth=token)

def extract_module_info(file_path: str) -> Tuple[str, str]:
    """Extract module number and title from file path.
    Returns tuple of (module_number, module_title)
    """
    # Extract module number from path (e.g., module19/ -> 19)
    match = re.match(r'module(\d+)/', file_path)
    if not match:
        raise ValueError(f"Invalid module path format: {file_path}")

    module_number = match.group(1)

    # For now, use a mapping for module titles
    # This could be enhanced to read from a config file
    MODULE_TITLES = {
        "19": "Recommendation Systems",
        # Add more modules as needed
    }

    module_title = MODULE_TITLES.get(module_number)
    if not module_title:
        # If no specific title found, use a generic one
        module_title = f"Module {module_number}"

    return module_number, module_title

def find_module_page(notion: Client, module_number: str, module_title: str) -> Optional[str]:
    """Find the module page ID"""
    full_title = f"Module {module_number}: {module_title}"
    response = notion.search(
        query=full_title,
        filter={"property": "object", "value": "page"}
    ).get("results", [])

    for page in response:
        if page["object"] == "page":
            title = page["properties"]["title"]["title"][0]["text"]["content"]
            if title == full_title:  # Exact match
                return page["id"]

    return None

def find_notes_page(notion: Client, module_id: str) -> Optional[str]:
    """Find the Notes page under a module"""
    # Get all child pages of the module
    children = notion.blocks.children.list(module_id).get("results", [])

    for child in children:
        if child["type"] == "child_page":
            title = child.get("child_page", {}).get("title", "")
            if title == "Notes":
                return child["id"]

    return None

def find_existing_page(notion: Client, notes_page_id: str, title: str) -> Optional[str]:
    """Find an existing page by title under Notes"""
    # Get all child pages of Notes
    children = notion.blocks.children.list(notes_page_id).get("results", [])

    for child in children:
        if child["type"] == "child_page":
            page_title = child.get("child_page", {}).get("title", "")
            if page_title == title:
                return child["id"]

    return None

def extract_first_h1_header(content: str) -> Optional[str]:
    """Extract the first H1 header from markdown content"""
    lines = content.split('\n')
    for line in lines:
        # Look for lines that start with a single # followed by space
        if re.match(r'^# ', line):
            return line.lstrip('# ').strip()
    return None

def parse_table(lines: List[str]) -> Tuple[List[str], List[List[str]]]:
    """Parse a markdown table into headers and rows.
    Returns tuple of (headers, rows)"""
    if not lines or len(lines) < 3:  # Need at least header, separator, and one data row
        return [], []

    # Parse headers
    headers = [cell.strip() for cell in lines[0].strip('|').split('|')]

    # Skip separator line
    data_rows = []
    for line in lines[2:]:
        if line.strip():  # Skip empty lines
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            data_rows.append(cells)

    return headers, data_rows

def parse_code_in_cell(cell_content: str) -> List[Dict[str, Any]]:
    """Parse cell content and convert code blocks to rich text with code formatting"""
    parts = []
    pattern = r'`([^`]+)`'
    last_end = 0

    for match in re.finditer(pattern, cell_content):
        # Add text before code if any
        if match.start() > last_end:
            parts.append({
                "type": "text",
                "text": {"content": cell_content[last_end:match.start()]}
            })

        # Add code part
        parts.append({
            "type": "text",
            "text": {"content": match.group(1)},
            "annotations": {"code": True}
        })

        last_end = match.end()

    # Add remaining text if any
    if last_end < len(cell_content):
        parts.append({
            "type": "text",
            "text": {"content": cell_content[last_end:]}
        })

    return parts if parts else [{
        "type": "text",
        "text": {"content": cell_content}
    }]

def create_table_block(headers: List[str], rows: List[List[str]]) -> Dict[str, Any]:
    """Create a Notion table block from headers and rows"""
    table_rows = []

    # Create header row
    header_cells = []
    for header in headers:
        header_parts = parse_code_in_cell(header)
        for part in header_parts:
            part.get("annotations", {}).update({"bold": True})
        header_cells.append(header_parts)
    table_rows.append({"cells": header_cells})

    # Create data rows
    for row in rows:
        cells = []
        for cell in row:
            cells.append(parse_code_in_cell(cell))
        table_rows.append({"cells": cells})

    return {
        "type": "table",
        "table": {
            "table_width": len(headers),
            "has_column_header": True,
            "has_row_header": False,
            "children": table_rows
        }
    }

def convert_markdown_to_blocks(content: str) -> List[Dict[str, Any]]:
    """Convert markdown content to Notion blocks"""
    blocks = []
    current_paragraph = []
    in_table = False
    table_lines = []

    # Split content into lines
    lines = content.split('\n')

    for line in lines:
        # Check if line is part of a table
        if '|' in line and (line.strip().startswith('|') or line.strip().endswith('|')):
            if not in_table:
                # Start of new table
                in_table = True
            table_lines.append(line)
            continue
        elif in_table:
            # End of table
            if table_lines:
                headers, rows = parse_table(table_lines)
                if headers and rows:
                    blocks.append(create_table_block(headers, rows))
            table_lines = []
            in_table = False

        # Handle headers
        if line.startswith('#'):
            if current_paragraph:
                blocks.append({
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": '\n'.join(current_paragraph)}
                        }]
                    }
                })
                current_paragraph = []

            level = len(re.match(r'^#+', line).group())
            text = line.lstrip('#').strip()
            blocks.append({
                "type": f"heading_{level}",
                f"heading_{level}": {
                    "rich_text": [{
                        "type": "text",
                        "text": {"content": text}
                    }]
                }
            })
        # Handle empty lines
        elif not line.strip():
            if current_paragraph:
                blocks.append({
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": '\n'.join(current_paragraph)}
                        }]
                    }
                })
                current_paragraph = []
        # Accumulate paragraph lines
        else:
            current_paragraph.append(line)

    # Add any remaining paragraph
    if current_paragraph:
        blocks.append({
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{
                    "type": "text",
                    "text": {"content": '\n'.join(current_paragraph)}
                }]
            }
        })

    # Handle any remaining table
    if table_lines:
        headers, rows = parse_table(table_lines)
        if headers and rows:
            blocks.append(create_table_block(headers, rows))

    return blocks

def create_module_page(notion: Client, module_number: str, module_title: str) -> str:
    """Create a new module page"""
    full_title = f"Module {module_number}: {module_title}"
    new_page = notion.pages.create(
        parent={"type": "page_id", "page_id": "2f7f4bed-9f8a-4725-b486-afead86f9d64"},  # Root page ID
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": full_title
                        }
                    }
                ]
            }
        }
    )
    return new_page["id"]

def create_notes_page(notion: Client, module_id: str) -> str:
    """Create a Notes page under a module"""
    new_page = notion.pages.create(
        parent={"type": "page_id", "page_id": module_id},
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": "Notes"
                        }
                    }
                ]
            }
        }
    )
    return new_page["id"]

def create_notion_page(notion: Client, parent_id: str, title: str, content: str) -> str:
    """Create a new page in Notion under the specified parent"""
    # Create the page
    new_page = notion.pages.create(
        parent={"type": "page_id", "page_id": parent_id},
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        children=convert_markdown_to_blocks(content)
    )

    return new_page["id"]

def update_notion_page(notion: Client, page_id: str, title: str, content: str) -> str:
    """Update an existing Notion page"""
    # Update the page title
    notion.pages.update(
        page_id=page_id,
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        }
    )

    # Delete existing content
    blocks = notion.blocks.children.list(page_id).get("results", [])
    for block in blocks:
        notion.blocks.delete(block_id=block["id"])

    # Add new content
    notion.blocks.children.append(
        block_id=page_id,
        children=convert_markdown_to_blocks(content)
    )

    return page_id

def sync_markdown_to_notion(file_path: str, force_new: bool = False) -> None:
    """Sync a markdown file to Notion under a module's Notes page"""
    # Setup client
    notion = setup_notion_client()

    # Extract module information from file path
    module_number, module_title = extract_module_info(file_path)

    # Find or create module page
    module_id = find_module_page(notion, module_number, module_title)
    if not module_id:
        print(f"Creating Module {module_number} page...")
        module_id = create_module_page(notion, module_number, module_title)

    # Find or create Notes page
    notes_page_id = find_notes_page(notion, module_id)
    if not notes_page_id:
        print("Creating Notes page...")
        notes_page_id = create_notes_page(notion, module_id)

    # Read the markdown file
    file_path = Path(file_path)
    if not file_path.exists():
        raise ValueError(f"File not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try to get title from first H1 header, fallback to filename
    title = extract_first_h1_header(content)
    if not title:
        title = file_path.stem.replace('-', ' ').title()
        print(f"No H1 header found in markdown, using filename as title: {title}")

    try:
        # Check for existing page unless force_new is True
        existing_page_id = None if force_new else find_existing_page(notion, notes_page_id, title)

        if existing_page_id and not force_new:
            # Update existing page
            page_id = update_notion_page(notion, existing_page_id, title, content)
            print(f"Successfully updated existing page '{title}' in Notion")
        else:
            # Create new page
            page_id = create_notion_page(notion, notes_page_id, title, content)
            print(f"Successfully created new page '{title}' in Notion")

        return page_id
    except Exception as e:
        print(f"Error syncing page: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Sync markdown files to Notion')
    parser.add_argument('file_path', help='Path to the markdown file')
    parser.add_argument('--new', action='store_true', help='Force creation of a new page even if one exists')
    args = parser.parse_args()

    # Validate file path is in a module directory
    if not re.match(r'^module\d+/', args.file_path):
        print("Error: File path must be in a module directory (e.g., module19/)")
        sys.exit(1)

    try:
        sync_markdown_to_notion(args.file_path, force_new=args.new)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()