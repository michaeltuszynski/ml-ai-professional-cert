#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
import re
import os
import json
from notion_client import Client
from dotenv import load_dotenv
from typing import Dict, Any, List, Optional, Tuple

def setup_notion_client() -> Client:
    """Setup Notion client with token from .env file or environment"""
    load_dotenv()
    token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError(
            "Please set your NOTION_TOKEN environment variable or create a .env file with NOTION_TOKEN=your_token"
        )

    return Client(auth=token)

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

def get_repo_info():
    remote_url = run_command("git config --get remote.origin.url")

    # Extract owner and repo name from SSH or HTTPS URL
    # Handle both github.com and custom SSH hosts (like github.personal)
    ssh_match = re.search(r"(?:git@|https://)(?:github\.com|github\.personal):?([^/]+)/([^/.]+)(?:\.git)?", remote_url)

    if not ssh_match:
        print(f"Could not parse GitHub repository information from URL: {remote_url}")
        sys.exit(1)

    return ssh_match.group(1), ssh_match.group(2)

def commit_changes():
    # Stage all changes
    run_command("git add .")

    # Get commit message from user
    commit_msg = input("Enter commit message: ")
    run_command(f'git commit -m "{commit_msg}"')

    # Push to main
    run_command("git push origin main")

    # Get the commit hash
    return run_command("git rev-parse HEAD")

def get_changed_notebooks(commit_hash):
    # Get list of changed files in the commit
    changed_files = run_command(f"git diff-tree --no-commit-id --name-only -r {commit_hash}")
    notebooks = []

    for file in changed_files.split('\n'):
        if file.endswith('.ipynb') and '.ipynb_checkpoints' not in file:
            notebooks.append(file)

    return notebooks

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

    # Extract and add notebook summary if available
    summary = extract_notebook_summary(notebook_path)
    if summary:
        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": "Notebook Summary"}
                        }]
                    }
                },
                *convert_markdown_to_blocks(summary)
            ]
        )

    # Add divider before bookmarks
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "type": "divider",
                "divider": {}
            }
        ]
    )

    # Add bookmarks
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "type": "bookmark",
                "bookmark": {"url": github_url}
            },
            {
                "type": "bookmark",
                "bookmark": {"url": colab_url}
            }
        ]
    )

def sync_notebook_to_notion(notebook_path: str, github_url: str, colab_url: str) -> None:
    """Sync a notebook's URLs and summary to Notion"""
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

    # Find or create notebook page
    notebook_page_id = find_or_create_notebook_page(notion, notes_id, notebook_path)

    # Add or update page content
    add_or_update_page_content(notion, notebook_page_id, notebook_path, github_url, colab_url)
    print(f"Successfully updated content and bookmarks for {notebook_path}")

def main():
    # Get repository information
    owner, repo = get_repo_info()

    # Commit changes and get commit hash
    commit_hash = commit_changes()

    # Get notebooks changed in this commit
    notebooks = get_changed_notebooks(commit_hash)

    if not notebooks:
        print("\nNo notebooks were changed in this commit.")
        return

    print("\nChanged Notebook URLs:")
    print("-" * 50)
    for notebook_path in notebooks:
        # Generate GitHub URL (always using github.com)
        github_url = f"https://github.com/{owner}/{repo}/blob/{commit_hash}/{notebook_path}"

        # Generate Colab URL (always using github.com)
        colab_url = f"https://colab.research.google.com/github/{owner}/{repo}/blob/main/{notebook_path}"

        print(f"\nNotebook: {notebook_path}")
        print(f"GitHub URL: {github_url}")
        print(f"Colab URL: {colab_url}")

        # Sync URLs to Notion
        try:
            sync_notebook_to_notion(notebook_path, github_url, colab_url)
        except Exception as e:
            print(f"Error syncing to Notion: {str(e)}")

if __name__ == "__main__":
    main()