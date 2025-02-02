#!/usr/bin/env python3

import sys
from pathlib import Path
import re
import os
import json
from notion_client import Client
from dotenv import load_dotenv
from typing import Dict, Any, List, Optional
import time

def setup_notion_client() -> Client:
    """Setup Notion client with token from .env file or environment"""
    load_dotenv()
    token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError(
            "Please set your NOTION_TOKEN environment variable or create a .env file with NOTION_TOKEN=your_token"
        )

    return Client(auth=token)

def extract_module_number(notebook_path: str) -> Optional[str]:
    """Extract module number from notebook path"""
    match = re.match(r'module(\d+)/', notebook_path)
    return match.group(1) if match else None

def find_module_page(notion: Client, module_number: str) -> Optional[str]:
    """Find the module page ID"""
    response = notion.search(
        query=f"Module {module_number}",
        filter={"property": "object", "value": "page"}
    ).get("results", [])

    for page in response:
        if page["object"] == "page":
            title = page["properties"]["title"]["title"][0]["text"]["content"]
            if f"Module {module_number}" in title:
                return page["id"]

    return None

def find_notes_page(notion: Client, module_id: str) -> Optional[str]:
    """Find the Notes page under a module"""
    children = notion.blocks.children.list(module_id).get("results", [])

    for child in children:
        if child["type"] == "child_page":
            title = child.get("child_page", {}).get("title", "")
            if title == "Notes":
                return child["id"]

    return None

def extract_notebook_summary(notebook_path: str) -> Optional[str]:
    """Extract the last markdown cell from a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Find the last markdown cell
        markdown_cells = [
            cell for cell in notebook.get('cells', [])
            if cell.get('cell_type') == 'markdown'
        ]

        if markdown_cells:
            last_markdown = markdown_cells[-1]
            # Join the source lines into a single string
            return ''.join(last_markdown.get('source', []))

        return None
    except Exception as e:
        print(f"Warning: Could not extract summary from notebook: {str(e)}")
        return None

def create_rich_text(content: str, bold: bool = False) -> List[Dict[str, Any]]:
    """Create rich text with proper annotations"""
    return [{
        "type": "text",
        "text": {"content": content},
        "annotations": {
            "bold": bold,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default"
        },
        "plain_text": content
    }]

def convert_markdown_to_blocks(content: str) -> List[Dict[str, Any]]:
    """Convert markdown content to Notion blocks"""
    blocks = []

    if not content or not content.strip():
        return []

    # Split content into lines
    lines = content.split('\n')
    current_paragraph = []

    for line in lines:
        line = line.rstrip()

        # Handle headers - convert all headers to heading_2
        if line.startswith('#'):
            if current_paragraph:
                text_content = '\n'.join(current_paragraph).strip()
                if text_content:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": create_rich_text(text_content)
                        }
                    })
                current_paragraph = []

            text = line.lstrip('#').strip()
            if text:  # Only add if there's actual content
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": create_rich_text(text)
                    }
                })
        # Handle bullet points
        elif line.strip().startswith('- '):
            if current_paragraph:
                text_content = '\n'.join(current_paragraph).strip()
                if text_content:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": create_rich_text(text_content)
                        }
                    })
                current_paragraph = []

            text = line.strip()[2:].strip()  # Remove '- ' and whitespace
            if text:
                # Check for bold text in bullet points
                is_bold = text.startswith('**') and text.endswith('**')
                if is_bold:
                    text = text[2:-2]  # Remove ** markers

                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": create_rich_text(text, bold=is_bold)
                    }
                })
        # Handle numbered lists
        elif re.match(r'^\d+\.\s', line.strip()):
            if current_paragraph:
                text_content = '\n'.join(current_paragraph).strip()
                if text_content:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": create_rich_text(text_content)
                        }
                    })
                current_paragraph = []

            text = re.sub(r'^\d+\.\s', '', line.strip())
            if text:
                # Check for bold text in numbered lists
                is_bold = text.startswith('**') and text.endswith('**')
                if is_bold:
                    text = text[2:-2]  # Remove ** markers

                blocks.append({
                    "object": "block",
                    "type": "numbered_list_item",
                    "numbered_list_item": {
                        "rich_text": create_rich_text(text, bold=is_bold)
                    }
                })
        # Handle empty lines - convert accumulated text to paragraph
        elif not line.strip():
            if current_paragraph:
                text_content = '\n'.join(current_paragraph).strip()
                if text_content:
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": create_rich_text(text_content)
                        }
                    })
                current_paragraph = []
        # Accumulate other lines for paragraph
        else:
            current_paragraph.append(line)

    # Add any remaining paragraph
    if current_paragraph:
        text_content = '\n'.join(current_paragraph).strip()
        if text_content:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": create_rich_text(text_content)
                }
            })

    return blocks

def validate_block(block: Dict[str, Any]) -> bool:
    """Validate a block structure"""
    if not isinstance(block, dict):
        return False

    required_fields = {"object", "type"}
    if not all(field in block for field in required_fields):
        return False

    if block["object"] != "block":
        return False

    block_type = block["type"]
    if block_type not in {"paragraph", "heading_2", "bulleted_list_item", "numbered_list_item", "divider", "bookmark"}:
        return False

    if block_type != "divider" and block_type not in block:
        return False

    return True

def find_or_create_notebook_page(notion: Client, notes_id: str, notebook_path: str) -> str:
    """Find or create a page for the notebook under Notes"""
    # Extract notebook name from path (e.g., "Codio 18.1" from path)
    path_parts = notebook_path.split('/')
    file_name = Path(path_parts[-1]).stem

    # Try to extract assignment number (e.g., "18.1" from various filename patterns)
    number_match = re.search(r'(?:codio_assignment_?|colab_activity_?|try_it_?)(\d+(?:\.\d+)?)', file_name, re.IGNORECASE)
    assignment_number = number_match.group(1) if number_match else ""

    # Determine page title based on path
    if 'codio' in notebook_path.lower():
        page_title = f"Codio {assignment_number}"
    elif 'colab' in notebook_path.lower():
        page_title = f"Self Study Colab {assignment_number}"
    elif 'try-it' in notebook_path.lower() or 'try_it' in notebook_path.lower():
        page_title = f"Try it {assignment_number}"
    else:
        page_title = file_name.replace('_', ' ').title()

    # Check if page already exists
    children = notion.blocks.children.list(notes_id).get("results", [])
    for child in children:
        if child["type"] == "child_page":
            title = child.get("child_page", {}).get("title", "")
            if title == page_title:
                return child["id"]

    # Create new page if it doesn't exist
    new_page = notion.pages.create(
        parent={"type": "page_id", "page_id": notes_id},
        properties={
            "title": {
                "title": [
                    {
                        "text": {
                            "content": page_title
                        }
                    }
                ]
            }
        }
    )
    return new_page["id"]

def add_or_update_page_content(notion: Client, page_id: str, notebook_path: str, github_url: str, colab_url: str) -> None:
    """Add or update page content including summary and bookmarks"""
    # Delete existing content
    blocks = notion.blocks.children.list(page_id).get("results", [])
    for block in blocks:
        notion.blocks.delete(block_id=block["id"])
        time.sleep(0.1)  # Small delay between deletes

    # Prepare blocks to add
    content_blocks = []

    # Extract and add notebook summary if available
    summary = extract_notebook_summary(notebook_path)
    if summary:
        # Convert markdown summary to blocks
        content_blocks.extend(convert_markdown_to_blocks(summary))

    # Add divider
    content_blocks.append({
        "object": "block",
        "type": "divider",
        "divider": {}
    })

    # Add GitHub bookmark
    content_blocks.append({
        "object": "block",
        "type": "bookmark",
        "bookmark": {
            "url": github_url
        }
    })

    # Add Colab bookmark
    content_blocks.append({
        "object": "block",
        "type": "bookmark",
        "bookmark": {
            "url": colab_url
        }
    })

    print("Debug: Content blocks to be added:")
    for i, block in enumerate(content_blocks):
        print(f"Block {i}: {block}")
        if not validate_block(block):
            print(f"Warning: Block {i} failed validation")

    # Add blocks one at a time with retries
    max_retries = 3
    for i, block in enumerate(content_blocks):
        if not validate_block(block):
            print(f"Skipping invalid block {i}")
            continue

        retries = 0
        while retries < max_retries:
            try:
                print(f"Adding block {i}...")
                notion.blocks.children.append(
                    block_id=page_id,
                    children=[block]  # Send single block
                )
                time.sleep(0.2)  # Small delay between blocks
                break
            except Exception as e:
                retries += 1
                print(f"Error adding block {i} (attempt {retries}): {str(e)}")
                if retries == max_retries:
                    raise
                time.sleep(1)  # Longer delay before retry

def sync_notebook_to_notion(notebook_path: str) -> None:
    """Sync an existing notebook to Notion"""
    notion = setup_notion_client()

    # Extract module number from path
    module_number = extract_module_number(notebook_path)
    if not module_number:
        print(f"Could not determine module number from path: {notebook_path}")
        return

    # Find module page
    module_id = find_module_page(notion, module_number)
    if not module_id:
        print(f"Could not find Module {module_number} page in Notion")
        return

    # Find Notes page
    notes_id = find_notes_page(notion, module_id)
    if not notes_id:
        print(f"Could not find Notes page under Module {module_number}")
        return

    # Get repository info for URLs
    repo_url = os.popen("git config --get remote.origin.url").read().strip()
    owner_repo_match = re.search(r"(?:git@|https://)(?:github\.com|github\.personal):?([^/]+)/([^/.]+)(?:\.git)?", repo_url)
    if not owner_repo_match:
        print("Could not determine repository owner and name")
        return

    owner, repo = owner_repo_match.groups()

    # Get current commit hash
    commit_hash = os.popen("git rev-parse HEAD").read().strip()

    # Generate URLs
    github_url = f"https://github.com/{owner}/{repo}/blob/{commit_hash}/{notebook_path}"
    colab_url = f"https://colab.research.google.com/github/{owner}/{repo}/blob/main/{notebook_path}"

    # Find or create notebook page
    notebook_page_id = find_or_create_notebook_page(notion, notes_id, notebook_path)

    # Add or update page content
    add_or_update_page_content(notion, notebook_page_id, notebook_path, github_url, colab_url)
    print(f"Successfully updated content and bookmarks for {notebook_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python sync_notebook.py <path_to_notebook>")
        print("Example: python sync_notebook.py module19/colab_activity19_1_starter/colab_activity_19_1.ipynb")
        sys.exit(1)

    notebook_path = sys.argv[1]
    if not notebook_path.endswith('.ipynb'):
        print("Error: File must be a Jupyter notebook (.ipynb)")
        sys.exit(1)

    if not os.path.exists(notebook_path):
        print(f"Error: File not found: {notebook_path}")
        sys.exit(1)

    try:
        sync_notebook_to_notion(notebook_path)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()