#!/usr/bin/env python3
import random
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

# Get directory path from command line argument
if len(sys.argv) < 2:
    print("Usage: python main.py <directory_path>")
    sys.exit(1)

directory_path = Path(sys.argv[1])
if not directory_path.exists():
    print(f"Error: Directory '{directory_path}' does not exist")
    sys.exit(1)
if not directory_path.is_dir():
    print(f"Error: '{directory_path}' is not a directory")
    sys.exit(1)

# Get all PDF files in specified directory
pdf_files = sorted(directory_path.glob("*.pdf"))

# Collect all pages
all_pages = []
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        all_pages.append(page)

# Shuffle pages randomly
random.shuffle(all_pages)

# Write to output file
writer = PdfWriter()
for page in all_pages:
    writer.add_page(page)

output_path = directory_path / "merged_shuffled.pdf"
with open(output_path, "wb") as output:
    writer.write(output)

print(
    f"Merged {len(pdf_files)} PDFs with {len(all_pages)} total pages into {output_path}"
)
