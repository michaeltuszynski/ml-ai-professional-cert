#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path
import re

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

if __name__ == "__main__":
    main()