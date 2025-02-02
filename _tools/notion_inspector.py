import os
from notion_client import Client
from dotenv import load_dotenv
import json
from typing import Dict, Any, List
from collections import defaultdict
import argparse
import sys

def setup_notion_client() -> Client:
    """Setup Notion client with token from .env file or environment"""
    load_dotenv()  # Load environment variables from .env file if it exists
    token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError(
            "Please set your NOTION_TOKEN environment variable or create a .env file with NOTION_TOKEN=your_token"
        )

    return Client(auth=token)

def get_page_title(page: Dict[str, Any]) -> str:
    """Extract title from a page object"""
    if "properties" not in page:
        return "Untitled"

    title_prop = page["properties"].get("title", {})
    if not title_prop.get("title"):
        return "Untitled"

    return title_prop["title"][0]["text"]["content"]

def get_page_parent(page: Dict[str, Any]) -> str:
    """Get parent ID of a page"""
    if "parent" not in page:
        return None

    parent = page["parent"]
    if parent["type"] == "page_id":
        return parent["page_id"]
    return None

def build_page_hierarchy(pages: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """Build a hierarchy of pages based on parent-child relationships"""
    hierarchy = defaultdict(list)
    page_titles = {}

    # First pass: collect all page IDs and titles
    for page in pages:
        page_id = page["id"]
        page_titles[page_id] = get_page_title(page)

    # Second pass: build hierarchy
    for page in pages:
        page_id = page["id"]
        parent_id = get_page_parent(page)
        if parent_id:
            hierarchy[parent_id].append(page_id)

    return hierarchy, page_titles

def print_hierarchy(hierarchy: Dict[str, List[str]], page_titles: Dict[str, str], root_id: str = None, level: int = 0):
    """Print page hierarchy in a tree-like format"""
    if root_id not in hierarchy:
        return

    for child_id in hierarchy[root_id]:
        print("  " * level + "- " + page_titles.get(child_id, "Untitled"))
        print_hierarchy(hierarchy, page_titles, child_id, level + 1)

def list_page_hierarchy(notion: Client) -> None:
    """List all pages in a hierarchical structure"""
    print("\nListing page hierarchy...")

    # Get all pages
    response = notion.search(
        filter={"property": "object", "value": "page"}
    ).get("results", [])

    if not response:
        print("No pages found. Make sure you've shared pages with the integration.")
        return

    # Build and print hierarchy
    hierarchy, page_titles = build_page_hierarchy(response)

    # Find root pages (those with no parent or parent not in our list)
    root_pages = [
        page for page in response
        if not get_page_parent(page) or get_page_parent(page) not in page_titles
    ]

    # Print each root page and its descendants
    for root_page in root_pages:
        root_id = root_page["id"]
        print("\n" + page_titles.get(root_id, "Untitled"))
        print_hierarchy(hierarchy, page_titles, root_id)

def find_module_notes_structure(notion: Client, module_number: str) -> None:
    """Find and print the structure of a module's Notes page"""
    # Find the module page
    response = notion.search(
        query=f"Module {module_number}: Recommendation Systems",
        filter={"property": "object", "value": "page"}
    ).get("results", [])

    print(f"\nSearching for Module {module_number}...")
    module_id = None
    for page in response:
        if page["object"] == "page":
            title = page["properties"]["title"]["title"][0]["text"]["content"]
            print(f"Found page: {title}")
            if f"Module {module_number}: Recommendation Systems" == title:
                module_id = page["id"]
                print(f"Selected as module page (ID: {module_id})")
                break

    if not module_id:
        print(f"Could not find main Module {module_number} page")
        print("Creating Module 19 page...")
        module_id = notion.pages.create(
            parent={"type": "page_id", "page_id": "2f7f4bed-9f8a-4725-b486-afead86f9d64"},  # Root page ID
            properties={
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": f"Module {module_number}: Recommendation Systems"
                            }
                        }
                    ]
                }
            }
        )["id"]
        print(f"Created Module {module_number} page (ID: {module_id})")

        print("Creating Notes page...")
        notes_id = notion.pages.create(
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
        )["id"]
        print(f"Created Notes page (ID: {notes_id})")
        return

    # Find Notes page
    print("\nLooking for Notes page...")
    children = notion.blocks.children.list(module_id).get("results", [])
    notes_id = None
    for child in children:
        if child["type"] == "child_page":
            title = child.get("child_page", {}).get("title", "")
            print(f"Found child page: {title}")
            if title == "Notes":
                notes_id = child["id"]
                print(f"Selected as Notes page (ID: {notes_id})")
                break

    if not notes_id:
        print("Notes page not found, creating it...")
        notes_id = notion.pages.create(
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
        )["id"]
        print(f"Created Notes page (ID: {notes_id})")
        return

    # Print Notes page structure
    print(f"\nStructure of Module {module_number} Notes:")
    notes_children = notion.blocks.children.list(notes_id).get("results", [])
    for child in notes_children:
        if child["type"] == "child_page":
            title = child.get("child_page", {}).get("title", "")
            print(f"- {title}")
            # Get child page content to look for bookmarks
            child_content = notion.blocks.children.list(child["id"]).get("results", [])
            for block in child_content:
                if block["type"] == "bookmark":
                    url = block.get("bookmark", {}).get("url", "")
                    print(f"  - Bookmark: {url}")

def main():
    parser = argparse.ArgumentParser(description='Sync markdown files to Notion')
    parser.add_argument('--inspect', help='Inspect module structure (e.g., "18")', required=False)
    parser.add_argument('file_path', help='Path to the markdown file', nargs='?')
    parser.add_argument('--new', action='store_true', help='Force creation of a new page even if one exists')
    args = parser.parse_args()

    try:
        notion = setup_notion_client()

        if args.inspect:
            find_module_notes_structure(notion, args.inspect)
            return

        if not args.file_path:
            parser.print_help()
            return

        if not args.file_path.startswith('module19/'):
            print("Error: Can only sync files from the module19 directory")
            sys.exit(1)

        sync_markdown_to_notion(args.file_path, force_new=args.new)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()