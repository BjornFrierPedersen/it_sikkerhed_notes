#!/usr/bin/env python3
"""
update_dictionary - A script to maintain a cybersecurity dictionary and link terms in markdown files

This script:
1. Scans markdown files for cybersecurity terms and abbreviations
2. Updates the central dictionary with new terms
3. Links instances of these terms in source files back to their dictionary definitions
"""

import os
import re
import glob
from pathlib import Path
import argparse

# Configuration
DICTIONARY_FILE = '_content/dictionary.md'
SOURCE_DIRS = ['Articles', 'Notes']
# Terms to exclude from dictionary and processing
EXCLUDED_TERMS = ["ID"]
# Regex patterns for identifying potential terms
ALL_CAPS_PATTERN = r'\b[A-Z]{2,}(?:/[A-Z]{2,})?\b'  # Match ALL CAPS terms like "TLS" or "TLS/SSL"
CAMEL_CASE_PATTERN = r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b'  # Match CamelCase like "ElGamal"

def load_dictionary():
    """Load existing dictionary terms from the dictionary file."""
    dictionary_terms = {}
    
    if not os.path.exists(DICTIONARY_FILE):
        print(f"Dictionary file not found: {DICTIONARY_FILE}")
        return dictionary_terms
    
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract terms from dictionary entries 
    # Format: - **TERM**: Definition
    term_matches = re.finditer(r'- \*\*([^*]+)\*\*:', content)
    for match in term_matches:
        term = match.group(1)
        dictionary_terms[term] = True
    
    return dictionary_terms

def is_in_table(text, position):
    """
    Determine if a given position in text is within a Markdown table.
    Returns True if position is inside a table, False otherwise.
    """
    # Find the start of the paragraph containing this position
    paragraph_start = text.rfind('\n\n', 0, position) + 2
    if paragraph_start < 2:  # Handle case where there's no preceding double newline
        paragraph_start = 0
    
    # Find the end of the paragraph containing this position
    paragraph_end = text.find('\n\n', position)
    if paragraph_end == -1:  # Handle case where there's no following double newline
        paragraph_end = len(text)
    
    paragraph = text[paragraph_start:paragraph_end]
    
    # Check if paragraph contains table markers (pipes)
    lines = paragraph.split('\n')
    
    # If the paragraph doesn't have enough lines, it's probably not a table
    if len(lines) < 2:
        return False
    
    # Check if majority of lines start and end with a pipe
    pipe_lines = 0
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        # Count lines with pipe characters
        if '|' in line:
            pipe_lines += 1
    
    # If more than half the lines contain pipes, it's likely a table
    if pipe_lines > len(lines) / 2:
        return True
    
    # Alternative method: check if there's a separator row (---|---|---)
    for line in lines:
        if re.match(r'^\s*\|[-:\s|]+\|\s*$', line):
            return True
    
    return False

def scan_for_terms(file_path, dictionary_terms):
    """
    Scan a markdown file for potential new terms and update existing terms with links.
    Returns a tuple of (new_terms, updated_content)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find potential new terms
    new_terms = set()
    
    # Search for ALL CAPS terms
    all_caps_matches = re.finditer(ALL_CAPS_PATTERN, content)
    for match in all_caps_matches:
        term = match.group(0)
        # Skip excluded terms
        if term in EXCLUDED_TERMS:
            continue
            
        if '/' in term:  # Handle compound terms like "TLS/SSL"
            for subterm in term.split('/'):
                if subterm not in dictionary_terms and subterm not in EXCLUDED_TERMS:
                    new_terms.add(subterm)
        elif term not in dictionary_terms:
            new_terms.add(term)
    
    # Search for CamelCase terms
    camel_case_matches = re.finditer(CAMEL_CASE_PATTERN, content)
    for match in camel_case_matches:
        term = match.group(0)
        if term not in dictionary_terms and term not in EXCLUDED_TERMS:
            new_terms.add(term)
    
    # Update content with dictionary links
    updated_content = content
    for term in dictionary_terms:
        # Skip excluded terms
        if term in EXCLUDED_TERMS:
            continue
            
        # Skip terms that are too short (likely false positives)
        if len(term) <= 1:
            continue
        
        # Create link format [[_content/dictionary#X|TERM]] where X is first letter
        section = term[0].upper()
        link_format = f"[[_content/dictionary#{section}|{term}]]"
        
        # Replace terms that aren't already linked
        # Only replace first occurrence per paragraph
        paragraphs = re.split(r'\n\s*\n', updated_content)
        for i, paragraph in enumerate(paragraphs):
            # Skip if already contains the link for this term
            if f"[[_content/dictionary#{section}|{term}]]" in paragraph:
                continue
            
            # Skip tables
            if '|' in paragraph and '\n' in paragraph and (
                re.search(r'^\s*\|', paragraph, re.MULTILINE) or 
                re.search(r'\|\s*$', paragraph, re.MULTILINE) or
                re.search(r'[-:]+\s*\|\s*[-:]+', paragraph)):
                continue
            
            # Replace first occurrence only in this paragraph
            # Use word boundaries to ensure we only match whole words
            pattern = r'\b' + re.escape(term) + r'\b'
            replacement_made = False
            
            # Handle terms in headings and list items first (always link these)
            for heading_match in re.finditer(r'^(#+|[-*+]\s+).*\b' + re.escape(term) + r'\b', paragraph, re.MULTILINE):
                heading_text = heading_match.group(0)
                updated_heading = re.sub(pattern, link_format, heading_text, count=1)
                paragraph = paragraph.replace(heading_text, updated_heading, 1)
                replacement_made = True
            
            # If no replacements in headings/lists, replace first occurrence in paragraph
            if not replacement_made:
                paragraph = re.sub(pattern, link_format, paragraph, count=1)
            
            paragraphs[i] = paragraph
        
        updated_content = '\n\n'.join(paragraphs)
    
    # Special handling for compound terms like TCP/IP after all individual terms are processed
    # Find and process compound terms with slashes
    compound_pattern = r'\b([A-Z]{2,})/([A-Z]{2,})\b'
    paragraphs = re.split(r'\n\s*\n', updated_content)
    for i, paragraph in enumerate(paragraphs):
        # Skip tables
        if '|' in paragraph and '\n' in paragraph and (
            re.search(r'^\s*\|', paragraph, re.MULTILINE) or 
            re.search(r'\|\s*$', paragraph, re.MULTILINE) or
            re.search(r'[-:]+\s*\|\s*[-:]+', paragraph)):
            continue
            
        # Find compound terms
        compound_matches = re.finditer(compound_pattern, paragraph)
        for match in compound_matches:
            full_match = match.group(0)
            term1 = match.group(1)
            term2 = match.group(2)
            
            # Check if each part is in our dictionary
            if term1 in dictionary_terms and term2 in dictionary_terms:
                # Create correctly formatted compound link
                section1 = term1[0].upper()
                section2 = term2[0].upper()
                compound_link = f"[[_content/dictionary#{section1}|{term1}]]/[[_content/dictionary#{section2}|{term2}]]"
                
                # Fix any incorrectly nested links first
                nested_link_pattern = r'\[\[_content/dictionary#[A-Z]\|[A-Z]{2,}/\[\[_content/dictionary#[A-Z]\|[A-Z]{2,}\]\]\]\]'
                if re.search(nested_link_pattern, paragraph):
                    paragraph = re.sub(nested_link_pattern, compound_link, paragraph)
                else:
                    # Replace the compound term with proper links
                    paragraph = paragraph.replace(full_match, compound_link)
        
        paragraphs[i] = paragraph
    
    updated_content = '\n\n'.join(paragraphs)
    
    return new_terms, updated_content

def update_dictionary_file(new_terms):
    """Add new terms to the dictionary file in their appropriate alphabetical sections."""
    if not new_terms:
        return
    
    # Read the existing dictionary
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    # Organize terms by their first letter
    terms_by_section = {}
    for term in new_terms:
        section = term[0].upper()
        if section not in terms_by_section:
            terms_by_section[section] = []
        terms_by_section[section].append(term)
    
    # Add new terms to their respective sections
    updated_content = []
    current_section = None
    
    for line in content:
        updated_content.append(line)
        
        # Check if this line starts a new section
        section_match = re.match(r'^## ([A-Z])$', line.strip())
        if section_match:
            current_section = section_match.group(1)
            
            # Add new terms for this section
            if current_section in terms_by_section:
                for term in sorted(terms_by_section[current_section]):
                    # Add placeholder definition that needs to be filled in
                    term_entry = f"- **{term}**: [NEEDS DEFINITION] - Add a brief description here.\n"
                    updated_content.append(term_entry)
                # Remove the terms we've added
                del terms_by_section[current_section]
    
    # Add any sections that were missing
    for section, terms in sorted(terms_by_section.items()):
        # Find where to insert this section
        section_added = False
        for i, line in enumerate(updated_content):
            section_match = re.match(r'^## ([A-Z])$', line.strip())
            if section_match and section_match.group(1) > section:
                # Insert new section before this one
                updated_content.insert(i, f"\n## {section}\n")
                for term in sorted(terms):
                    term_entry = f"- **{term}**: [NEEDS DEFINITION] - Add a brief description here.\n"
                    updated_content.insert(i + 1, term_entry)
                section_added = True
                break
        
        # If we didn't find a place to insert, add at the end
        if not section_added:
            updated_content.append(f"\n## {section}\n")
            for term in sorted(terms):
                term_entry = f"- **{term}**: [NEEDS DEFINITION] - Add a brief description here.\n"
                updated_content.append(term_entry)
    
    # Write the updated dictionary back to the file
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as f:
        f.writelines(updated_content)

def update_file_with_links(file_path, updated_content):
    """Write the updated content with links back to the file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def main():
    parser = argparse.ArgumentParser(description='Update cybersecurity dictionary and link terms in markdown files')
    parser.add_argument('--scan-only', action='store_true', help='Only scan for new terms without updating files')
    args = parser.parse_args()
    
    # Load existing dictionary terms
    dictionary_terms = load_dictionary()
    print(f"Loaded {len(dictionary_terms)} terms from dictionary")
    
    # Find all markdown files in source directories
    all_md_files = []
    for source_dir in SOURCE_DIRS:
        if os.path.exists(source_dir):
            md_files = glob.glob(f"{source_dir}/**/*.md", recursive=True)
            all_md_files.extend(md_files)
    
    print(f"Found {len(all_md_files)} markdown files to process")
    
    # Scan files for terms and update content
    all_new_terms = set()
    files_updated = 0
    
    for file_path in all_md_files:
        print(f"Processing {file_path}...")
        new_terms, updated_content = scan_for_terms(file_path, dictionary_terms)
        
        # Add new terms to the overall set
        all_new_terms.update(new_terms)
        
        # Update the file with links if content changed and not in scan-only mode
        if not args.scan_only and updated_content != open(file_path, 'r', encoding='utf-8').read():
            update_file_with_links(file_path, updated_content)
            files_updated += 1
    
    # Report new terms found
    if all_new_terms:
        print(f"Found {len(all_new_terms)} new terms to add to dictionary:")
        for term in sorted(all_new_terms):
            print(f"  - {term}")
        
        # Update the dictionary with new terms if not in scan-only mode
        if not args.scan_only:
            update_dictionary_file(all_new_terms)
            print(f"Updated dictionary with {len(all_new_terms)} new terms")
    else:
        print("No new terms found")
    
    print(f"Updated {files_updated} files with term links")

if __name__ == "__main__":
    main() 