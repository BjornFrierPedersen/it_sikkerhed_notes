# Cursor Configuration

This directory contains advanced configurations for the Cursor editor to enhance your experience with this Obsidian-based cybersecurity knowledge base.

## Rules

The `rules` directory contains rule-based configurations that define custom behaviors for specific contexts:

- **update_dictionary.json**: Automated tool for maintaining the cybersecurity terminology dictionary. This rule scans all markdown files for technical terms and abbreviations, adds them to the dictionary, and creates proper links throughout the vault.

- **what_do_we_know_about.json**: An assistant-powered rule that activates when you ask "What do we know about X?" questions. It compiles comprehensive information about cybersecurity terms by searching across the entire vault.

## Usage

These rules are automatically loaded by Cursor when you open this project. You don't need to do anything special to activate them.

- To update the dictionary, run the "Update Dictionary" command from the command palette
- To use the "What do we know about" feature, simply ask a question in that format within a markdown file
  - You can also use the shorthand "wdwka" (e.g., "wdwka SSL") to trigger the same functionality

## Benefits of Using Rules

Moving these configurations from .cursorconfig to dedicated rule files provides several advantages:

1. **Better organization**: Each rule is self-contained in its own file
2. **Easier maintenance**: Rules can be updated individually without affecting others
3. **Improved contextualization**: Rules can be scoped to specific file patterns
4. **Enhanced collaboration**: Rules can be shared, versioned, and described independently

## Adding New Rules

To add new rules, create a new JSON file in the `rules` directory following the existing patterns. 