import os
from notion_client import Client
from dotenv import load_dotenv
import json
from typing import Dict, Any, List, Optional
from pathlib import Path
import markdown
import re
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

def find_module_19_page(notion: Client) -> Optional[str]:
    """Find the Module 19 page ID"""
    response = notion.search(
        query="Module 19: Recommendation Systems",
        filter={"property": "object", "value": "page"}
    ).get("results", [])

    for page in response:
        if page["object"] == "page":
            title = page["properties"]["title"]["title"][0]["text"]["content"]
            if "Module 19" in title:
                return page["id"]

    return None

def find_notes_page(notion: Client, module_19_id: str) -> Optional[str]:
    """Find the Notes page under Module 19"""
    # Get all child pages of Module 19
    children = notion.blocks.children.list(module_19_id).get("results", [])

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

def convert_markdown_to_blocks(content: str) -> List[Dict[str, Any]]:
    """Convert markdown content to Notion blocks"""
    blocks = []

    # Split content into lines
    lines = content.split('\n')
    current_paragraph = []

    for line in lines:
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

    return blocks

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
    """Sync a markdown file to Notion under Module 19's Notes page"""
    # Setup client
    notion = setup_notion_client()

    # Find Module 19 page
    module_19_id = find_module_19_page(notion)
    if not module_19_id:
        raise ValueError("Could not find Module 19 page in Notion")

    # Find Notes page
    notes_page_id = find_notes_page(notion, module_19_id)
    if not notes_page_id:
        raise ValueError("Could not find Notes page under Module 19")

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

    if not args.file_path.startswith('module19/'):
        print("Error: Can only sync files from the module19 directory")
        sys.exit(1)

    try:
        sync_markdown_to_notion(args.file_path, force_new=args.new)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()