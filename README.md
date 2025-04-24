# Cybersecurity Knowledge Base

A comprehensive collection of cybersecurity notes, articles, and reference materials organized in an Obsidian vault with an integrated dictionary system.

## Overview

This repository contains a structured set of cybersecurity knowledge, including:

- OWASP Top 10 (2021) study materials
- Threat modeling documentation and frameworks
- Social engineering and phishing attack analysis
- Articles on core security concepts
- Security standards and best practices
- Risk assessment templates and methodologies
- OWASP security reference materials
- An integrated cybersecurity dictionary for technical terms

## Directory Structure

- `Notes/` - Main directory containing all security documentation
  - `General/` - Contains OWASP Top 10, threat modeling, and social engineering content
  - `Articles/` - Detailed write-ups on network security, principles, and practices
  - `Models & Templates/` - Risk assessment and other security templates
  - `Standards/` - Security standards documentation and guidelines
  - `OWASP Cheatsheets/` - Reference materials from the OWASP project
- `_content/` - Support content including the centralized dictionary and project index
- `update_dictionary.py` - Utility script for maintaining the dictionary system

## Core Content Areas

1. **OWASP Top 10 (2021)** - Comprehensive study notes on each vulnerability
2. **Threat Modeling** - STRIDE framework and methodology documentation
3. **Social Engineering** - Attack types, methodologies, and prevention strategies
4. **Network Security** - VPN, wireless networks, and protocols
5. **Security Principles** - Security by design, defense in depth, secure coding
6. **Risk Management** - Assessment templates and board-level guidance

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

## Project Index

For a detailed breakdown of all content and its organization, refer to `_content/project_index.md`.