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
    # Remove page numbers/headers
    text = re.sub(r'Page \d+ of \d+\s*', '', text)

    # Fix hyphenated words at line breaks (more comprehensive)
    text = re.sub(r'(\w+)\s*-\s*\n\s*(\w+)', r'\1\2', text)
    text = re.sub(r'(\w+)\s+-\s+(\w+)', r'\1-\2', text)

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove form feed characters
    text = text.replace('\f', '')

    # Clean up newlines
    text = text.replace('\r', '\n')
    text = re.sub(r'\n\s*\n', '\n\n', text)

    # Fix spacing around quotes
    text = re.sub(r'\s+"', ' "', text)
    text = re.sub(r'"\s+', '" ', text)

    return text.strip()

def format_headers(text: str) -> str:
    """Format text with proper markdown headers."""
    lines = text.split('\n')
    formatted_lines = []
    current_video = None

    for line in lines:
        line = line.strip()
        if not line:
            formatted_lines.append(line)
            continue

        # Module header
        if line.startswith('Module'):
            formatted_lines.append(f"# {line}")
            continue

        # Video sections
        video_match = re.match(r'^Video\s+(\d+):\s+(.+)', line, re.IGNORECASE)
        if video_match:
            num, title = video_match.groups()
            current_video = num
            formatted_lines.append(f"\n## Video {num}: {title}")
            continue

        # Subsections (numbered or key concepts)
        if re.match(r'^\d+\.?\d*\s+[A-Z]', line) or (len(line) < 60 and line[0].isupper() and not line[-1] in '.,:;?!)'):
            formatted_lines.append(f"\n### {line}")
        else:
            formatted_lines.append(line)

    return '\n'.join(formatted_lines)

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
    # Ensure consistent paragraph spacing
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Add proper spacing after sentences
    text = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\n\2', text)

    # Ensure lists have proper spacing
    text = re.sub(r'\n([-*])\s', r'\n\n\1 ', text)

    # Clean up extra spaces around blockquotes
    text = re.sub(r'\n\s*>\s*', r'\n> ', text)
    text = re.sub(r'\n>\s*\n\s*>\s*', r'\n> \n> ', text)

    # Fix spacing around mathematical expressions
    text = re.sub(r'(\w+)\s*=\s*(\w+)', r'\1 = \2', text)

    # Join short lines that are part of the same sentence
    lines = text.split('\n')
    result = []
    current = []

    for line in lines:
        if not line.strip():
            if current:
                result.append(' '.join(current))
                current = []
            result.append('')
        elif len(line) < 60 and not line.rstrip().endswith(('.', '?', '!', ':', '>')):
            current.append(line)
        else:
            if current:
                current.append(line)
                result.append(' '.join(current))
                current = []
            else:
                result.append(line)

    if current:
        result.append(' '.join(current))

    text = '\n'.join(result)

    return text

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