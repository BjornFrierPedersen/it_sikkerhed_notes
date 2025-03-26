# Update Dictionary Command Guide

## Purpose
The `update_dictionary` command serves two essential functions:
1. Add new cybersecurity abbreviations and terms to the central dictionary
2. Link all instances of these terms in source files back to their dictionary definitions

## Implementation Process

### 1. Dictionary Update Process

#### Scanning for Terms
- Scan all markdown files in the repository (particularly in Articles/ and Notes/ directories)
- Identify potential abbreviations and technical terms using these methods:
  - ALL CAPS words (e.g., "CSRF", "XSS", "TLS")
  - CamelCase technical terms (e.g., "ElGamal", "ChaCha20")
  - Known cybersecurity algorithms and technologies
  - Terms that appear in technical context but may be unfamiliar to readers

#### Updating the Dictionary
- For each identified term, check if it exists in `_content/dictionary.md`
- If the term is new, add it to the appropriate alphabetical section
- Format each entry consistently:
  ```
  - **TERM**: Full expansion - Brief description explaining the concept.
  ```
- Ensure the description is accurate, concise, and informative
- For terms without common expansions (like algorithms), provide a definition that explains its purpose

### 2. Source File Linking Process

#### Link Creation
- For each term in the dictionary, identify all instances in source files
- Replace unlinked terms with proper dictionary links using this format:
  ```
  [[_content/dictionary#X|TERM]]
  ```
  Where X is the first letter of the term (capitalized for the section heading)

#### Link Placement Rules
1. Only link the first occurrence of a term within a paragraph
2. Always link terms in headings and list items
3. Don't modify terms that are already properly linked
4. Preserve the capitalization of the original term in the visible portion
5. If the term is part of a larger word, only link the term itself

### 3. Special Cases

#### Handling Term Variations
- Different forms of the same term should link to the primary entry
  - "encrypting", "encrypted", "encryption" → link to the entry for "encryption" 
- Possessive forms should be handled appropriately:
  - "RSA's algorithm" → "[[_content/dictionary#R|RSA]]'s algorithm"

#### Edge Cases
- For compound terms like "TLS/SSL", link each component separately:
  - "[[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]]"
- For terms with variants, link to the primary form:
  - Both "public key infrastructure" and "PKI" link to "[[_content/dictionary#P|PKI]]"

## Example Transformations

### Standard Abbreviation
Original: `CSRF attacks are dangerous.`  
Linked: `[[_content/dictionary#C|CSRF]] attacks are dangerous.`

### Mid-word or Combined Term
Original: `The HTTPS connection was secure.`  
Linked: `The [[_content/dictionary#H|HTTPS]] connection was secure.`

### Already Linked Term (No Change)
Original: `The [[_content/dictionary#C|CSRF]] attack was mitigated.`  
Final: `The [[_content/dictionary#C|CSRF]] attack was mitigated.`

## Best Practices

1. **Consistency**: Maintain consistent formatting in the dictionary
2. **Accuracy**: Verify definitions before adding to the dictionary
3. **Non-duplication**: Avoid creating duplicate links in the source files
4. **Relevance**: Only link terms that are technical or may be unfamiliar
5. **Maintenance**: Periodically check for broken links

## Troubleshooting

- If a term spans multiple words (e.g., "Key Derivation Function"), link to its abbreviation ("KDF") if it exists
- If unsure about a potential term, err on the side of inclusion and link it
- If a term appears very frequently in a technical document, link only its first occurrence in each major section 