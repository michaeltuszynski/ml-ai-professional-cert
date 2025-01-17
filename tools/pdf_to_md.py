#!/usr/bin/env python3

import PyPDF2
import re
import argparse
import os
from typing import List, Optional

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF file and combine all pages."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text.strip():
                    full_text += text + "\n"
        return full_text.strip()
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""

def clean_text(text: str) -> str:
    """Clean and format extracted text."""
    # Remove page numbers and headers more aggressively
    text = re.sub(r'Page\s+\d+\s+of\s+\d+.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)  # Standalone page numbers

    # Fix hyphenated words at line breaks
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)

    # Remove form feed and other special characters
    text = text.replace('\f', '')
    text = text.replace('\r', '')

    # Fix spacing issues
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single space
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Multiple newlines to double newline
    text = re.sub(r'(?<=[.!?])\s+(?=[A-Z])', '\n\n', text)  # Add paragraph breaks after sentences

    # Fix spacing around quotes and punctuation
    text = re.sub(r'\s+"', ' "', text)
    text = re.sub(r'"\s+', '" ', text)
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)

    # Remove any remaining whitespace at start/end of lines
    text = '\n'.join(line.strip() for line in text.split('\n'))

    return text.strip()

def format_headers(text: str) -> str:
    """Format text with proper markdown headers."""
    # First pass: split module and video headers if combined
    text = re.sub(r'(Module [^V]+)Video', r'\1\nVideo', text)

    # Split into lines and process
    lines = text.split('\n')
    formatted_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line:
            formatted_lines.append('')
            i += 1
            continue

        # Module header
        if line.startswith('Module'):
            formatted_lines.extend([
                '',  # Empty line before header
                f"# {line}",
                ''   # Empty line after header
            ])
            i += 1
            continue

        # Video sections
        video_match = re.match(r'^Video\s+(\d+):\s+(.+)', line, re.IGNORECASE)
        if video_match:
            num, title = video_match.groups()
            formatted_lines.extend([
                '',  # Empty line before header
                f"## Video {num}: {title}",
                ''   # Empty line after header
            ])
            i += 1
            continue

        # Subsections
        if re.match(r'^\d+\.?\d*\s+[A-Z]', line) or (len(line) < 60 and line[0].isupper() and not line[-1] in '.,:;?!)'):
            formatted_lines.extend([
                '',  # Empty line before header
                f"### {line}",
                ''   # Empty line after header
            ])
            i += 1
            continue

        # Regular content - check if next line is a header
        next_is_header = False
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            next_is_header = (
                next_line.startswith('Module') or
                re.match(r'^Video\s+\d+:', next_line, re.IGNORECASE) or
                re.match(r'^\d+\.?\d*\s+[A-Z]', next_line) or
                (len(next_line) < 60 and next_line and next_line[0].isupper() and not next_line[-1] in '.,:;?!)')
            )

        formatted_lines.append(line)
        if next_is_header:
            formatted_lines.append('')  # Add space before next header
        i += 1

    # Clean up multiple empty lines
    result = []
    prev_empty = False
    for line in formatted_lines:
        if not line:
            if not prev_empty:
                result.append(line)
            prev_empty = True
        else:
            result.append(line)
            prev_empty = False

    return '\n'.join(result).strip()

def format_code_and_math(text: str) -> str:
    """Format code and mathematical terms."""
    # Format inline code/math terms
    patterns = [
        (r'\b([xyz]\d*)\b(?!\s*[A-Za-z])', r'`\1`'),  # Variables like x1, y2
        (r'\b(bold)\s+([xyz])\b', r'**\2**'),  # Bold variables
        (r'\b(f)\s*\(([^)]+)\)', r'`f(\2)`'),  # Functions
        (r'\b(sum|mean|variance|std)\b', r'`\1`'),  # Statistical terms
        (r'\b(dataframe|DataFrame)\b', r'`DataFrame`'),  # Programming terms
        (r'`([^`]+)`\s*=\s*([^,\n]+)', r'`\1 = \2`'),  # Assignments
        (r'\b(PDF|URL|ID)\b', r'**\1**'),  # Common acronyms
        (r'\b(non-deterministic|data-centric)\b', r'*\1*'),  # Hyphenated terms
    ]

    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    return text

def format_emphasis(text: str) -> str:
    """Add markdown emphasis to text."""
    # Bold important terms and acronyms
    text = re.sub(r'\b([A-Z]{2,})\b(?![A-Z])', r'**\1**', text)

    # Italicize key terms and concepts
    key_terms = (
        r'\b(type|types|keyword|keywords|context|contexts|possibility|possibilities|'
        r'them|distribution|random variable|mean|variance|standard deviation|'
        r'expectation|non-deterministic|data-centric)\b'
    )
    text = re.sub(key_terms, r'*\1*', text, flags=re.IGNORECASE)

    # Format quotes with proper blockquote
    text = re.sub(r'"([^"]+)"', r'\n> "\1"\n', text)
    text = re.sub(r'>\s*"([^"]+)"\s*\n>\s*"', r'> "\1\n> "', text)  # Join adjacent quotes

    # Format important notes
    text = re.sub(r'\b(Note that|Important|Remember|Key concept):', r'**\1:**', text)

    return text

def format_paragraphs(text: str) -> str:
    """Improve paragraph formatting."""
    # Remove any remaining page number artifacts
    text = re.sub(r'\n\s*\d+\s*\n', '\n\n', text)

    # Ensure consistent paragraph spacing
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Add proper spacing after sentences while preserving lists and code blocks
    lines = text.split('\n')
    formatted_lines = []
    in_code_block = False

    for i, line in enumerate(lines):
        # Skip empty lines
        if not line.strip():
            formatted_lines.append('')
            continue

        # Handle code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            formatted_lines.append(line)
            continue

        if in_code_block:
            formatted_lines.append(line)
            continue

        # Handle lists
        if line.strip().startswith(('-', '*', '+', '1.', '>')):
            formatted_lines.append(line)
            continue

        # Regular paragraph text
        if i > 0 and lines[i-1].strip() and not lines[i-1].strip().startswith(('-', '*', '+', '1.', '>')):
            # Join with previous line if it's part of the same paragraph
            if not any(line.endswith(x) for x in '.!?:'):
                formatted_lines[-1] = formatted_lines[-1] + ' ' + line
            else:
                formatted_lines.append(line)
        else:
            formatted_lines.append(line)

    text = '\n'.join(formatted_lines)

    # Clean up spacing
    text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive blank lines
    text = re.sub(r'(?<=\n\n)[\t ]+', '', text)  # Remove leading spaces after blank lines
    text = re.sub(r'[\t ]+(?=\n\n)', '', text)  # Remove trailing spaces before blank lines

    return text.strip()

def convert_pdf_to_markdown(pdf_path: str, output_path: Optional[str] = None) -> None:
    """Convert PDF file to Markdown format."""
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text could be extracted from the PDF.")
        return

    # Clean and format the text
    text = clean_text(text)
    text = format_headers(text)
    text = format_code_and_math(text)
    text = format_emphasis(text)
    text = format_paragraphs(text)

    # Final cleanup
    text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive blank lines

    # Determine output path
    if not output_path:
        output_path = os.path.splitext(pdf_path)[0] + '.md'

    # Write to file
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Successfully converted PDF to Markdown: {output_path}")
    except Exception as e:
        print(f"Error writing markdown file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert PDF files to Markdown format')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Output markdown file path (optional)')

    args = parser.parse_args()
    convert_pdf_to_markdown(args.pdf_path, args.output)

if __name__ == '__main__':
    main()