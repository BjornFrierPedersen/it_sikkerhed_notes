#!/usr/bin/env python3
"""
A script to identify and optionally remove CamelCase entries from the dictionary
that aren't true abbreviations.
"""

import re
import argparse

DICTIONARY_FILE = '_content/dictionary.md'

def identify_camelcase_entries():
    """Identify CamelCase entries in the dictionary that aren't true abbreviations."""
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    camelcase_pattern = r'- \*\*([A-Z][a-z]+(?:[A-Z][a-z]+)+)\*\*:'
    camelcase_entries = []
    
    for i, line in enumerate(content):
        match = re.search(camelcase_pattern, line)
        if match:
            term = match.group(1)
            camelcase_entries.append((i+1, term, line.strip()))
    
    return camelcase_entries, content

def remove_camelcase_entries(entries_to_remove, content):
    """Remove specified CamelCase entries from the dictionary content."""
    line_numbers = [entry[0] for entry in entries_to_remove]
    new_content = [line for i, line in enumerate(content, 1) if i not in line_numbers]
    
    return new_content

def main():
    parser = argparse.ArgumentParser(description='Identify and optionally remove CamelCase entries from the dictionary')
    parser.add_argument('--remove', action='store_true', help='Remove identified CamelCase entries')
    parser.add_argument('--output', type=str, default='', help='Output file for cleaned dictionary (default: overwrite original)')
    args = parser.parse_args()
    
    camelcase_entries, content = identify_camelcase_entries()
    
    # Print identified entries
    print(f"Found {len(camelcase_entries)} CamelCase entries in the dictionary:")
    for line_num, term, line_text in camelcase_entries:
        print(f"Line {line_num}: {term} - {line_text}")
    
    # Remove entries if requested
    if args.remove:
        new_content = remove_camelcase_entries(camelcase_entries, content)
        
        output_file = args.output if args.output else DICTIONARY_FILE
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        
        print(f"Removed {len(camelcase_entries)} CamelCase entries, saved to {output_file}")
    elif not args.remove:
        print("\nTo remove these entries, run the script with the --remove flag")
        print("You can also specify an output file with --output filename.md")

if __name__ == "__main__":
    main() 