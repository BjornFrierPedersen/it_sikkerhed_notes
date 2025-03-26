# Cybersecurity Knowledge Base

A comprehensive collection of cybersecurity notes, articles, and reference materials organized in an Obsidian vault with an integrated dictionary system.

## Overview

This repository contains a structured set of cybersecurity knowledge, including:

- Articles on core security concepts
- Notes on specific vulnerabilities and attack vectors
- OWASP security reference materials
- An integrated cybersecurity dictionary for technical terms

## Directory Structure

- `Articles/` - Detailed write-ups on cybersecurity topics and concepts
- `Notes/` - Structured notes on specific security issues, organized by category
- `_content/` - Support content including the centralized dictionary
- `OWASP Cheatsheet/` - Reference materials from the OWASP project
- `update_dictionary.py` - Utility script for maintaining the dictionary system

## The Dictionary System

This project includes an integrated dictionary system that:

1. Maintains a centralized glossary of cybersecurity terms and abbreviations
2. Automatically links terms in markdown files to their definitions
3. Provides consistent explanations for technical terminology

The dictionary file is located at `_content/dictionary.md` and is organized alphabetically by the first letter of each term.

## The Update Dictionary Script

The `update_dictionary.py` script maintains the dictionary system by:

1. Scanning all markdown files for cybersecurity terms and abbreviations
2. Adding new terms to the dictionary with placeholder definitions
3. Creating links in the source files back to dictionary definitions

### Running the Script

```bash
python update_dictionary.py
```

Will run the script and provide a list of terms that need definitions. But it will not add the definitions to the dictionary. To do this automatically use the "update_dictionary" command in Cursor. To make sure that cursor understands the command write .cursorconfig beforehand.

```bash
.cursorconfig update_dictionary
```

## Environment

This project is designed to work with:

- Obsidian for notes viewing and editing
- Cursor IDE with AI assistance for content development
- Python 3.x for running the dictionary update script