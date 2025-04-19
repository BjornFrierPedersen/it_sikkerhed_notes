# Cybersecurity Vault Project Index

This document serves as a master index for the entire vault, providing a quick reference to all content organized by topic and content type.

## Core Content Areas

### 1. OWASP Top 10 (2021) - Study Notes
Located in `/Notes/[number]_[vulnerability name]` folders:

1. **Broken Access Control** - `/Notes/1_Broken_Access_Control/`
   - Authorization failures, privilege escalation, and access control vulnerabilities
   
2. **Cryptographic Failures** - `/Notes/2_Cryptographic_Failures/`
   - Failures related to cryptography that lead to sensitive data exposure
   
3. **Injection** - `/Notes/3_Injection/`
   - SQL, NoSQL, OS, and LDAP injection flaws
   
4. **Insecure Design** - `/Notes/4_Insecure_Design/`
   - Flaws in design and architecture
   
5. **Security Misconfiguration** - `/Notes/5_Security_Misconfiguration/`
   - Improper configuration of applications, frameworks, servers
   
6. **Vulnerable & Outdated Components** - `/Notes/6_Vulnerable_Outdated_Components/`
   - Use of libraries, components with known vulnerabilities
   
7. **Identification & Authentication Failures** - `/Notes/7_Identification_Authentication_Failures/`
   - Broken authentication, session management
   
8. **Software & Data Integrity Failures** - `/Notes/8_Software_Data_Integrity_Failures/`
   - CI/CD pipeline issues, unsigned code, insecure deserialization
   
9. **Security Logging & Monitoring Failures** - `/Notes/9_Security_Logging_Monitoring_Failures/`
   - Insufficient logging, detection, and response
   
10. **Server-Side Request Forgery** - `/Notes/10_Server_Side_Request_Forgery/`
    - SSRF vulnerabilities and prevention

### 2. Threat Modeling
Located in `/Notes/Threat Modelling/`:

- **STRIDE Framework** - Documented with diagrams
  - Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **Threat Modeling Process** - General methodology and approach

### 3. Cryptography
Located in `/Notes/Articles/Cryptography/`:

- Implementation types
- Cryptographic concepts 
- Public key infrastructure
- Asymmetric encryption
- Problems cryptography solves

### 4. Social Engineering & Phishing Attacks
Located in `/Notes/Social_Engineering_Attacks/`:

- What is social engineering and its various types
  - Piggybacking, Shoulder surfing, Baiting, Dumpster diving, Tailgating
- Phishing attack methodologies
  - Email Phishing, Spear Phishing, Whaling, Smishing, Vishing
- Phishing kits and tools
- Prevention and mitigation strategies

### 5. General Security Concepts
Located in `/Notes/General/` and `/Notes/Articles/`:

- Windows Access Controls
- Security by Design Principles
- Defence in Depth
- Secure Coding
- Defensive Programming
- Password security
- Network security (VPN, Wireless)
- Protocols

## Reference Materials

### 1. OWASP Cheatsheets
Located in `/Notes/OWASP Cheatsheets/`:

- 90+ security cheatsheets covering various aspects of application security
- Comprehensive guides on secure implementation of technologies
- Best practices for security controls

### 2. Dictionary
Located in `/_content/dictionary.md`:

- Comprehensive glossary of cybersecurity terms and abbreviations
- Organized alphabetically with explanations

### 3. Standards Documentation
Located in `/Notes/Standards/`:

- OWASP Application Security Verification Standard (ASVS) overview
- OWASP Software Assurance Maturity Model (SAMM)
- Critical Security Controls
- Example security assessment reports

## Tools and Utilities

- **Update Dictionary Script** - `/update_dictionary.py`
  - Python script to update and maintain the dictionary
  - Automatically links terms in markdown files to dictionary definitions

## Project Structure Overview

```
.
├── _content/
│   ├── dictionary.md           # Cybersecurity terms glossary
│   └── project_index.md        # This index file
├── _THE_NOTE_.md               # Temporary note file for content to be organized
├── Notes/
│   ├── Articles/               # Articles on various security topics
│   │   ├── Cryptography/       # Articles on cryptographic topics
│   │   ├── Protocols/          # Articles on security protocols
│   │   └── [Various standalone articles]
│   ├── Standards/              # Security standards documentation
│   │   ├── example_reports/    # Example security assessment reports
│   │   └── [Standard documentation files]
│   ├── 1_Broken_Access_Control/ through 10_Server_Side_Request_Forgery/  # OWASP Top 10 (2021)
│   ├── General/                # General security notes
│   ├── Social_Engineering_Attacks/ # Social engineering and phishing content
│   ├── Threat Modelling/       # Threat modeling content
│   ├── OWASP Cheatsheets/      # Reference cheatsheets from OWASP
│   │   └── [90+ cheatsheet files]
│   └── _THE_NOTE_.md           # Temporary note file for content to be organized
└── [Project files]
    ├── update_dictionary.py    # Script to maintain the dictionary
    ├── update_dictionary_guide.md  # Guide for using the dictionary update script
    └── README.md               # Project readme
```

## How to Use This Vault

1. **Finding Information**:
   - Use this index to locate content by topic
   - Search for terms in the dictionary for definitions
   - Browse the OWASP cheatsheets for implementation guidance

2. **Maintaining Content**:
   - Use _THE_NOTE_.md for temporary content that needs organization
   - Run update_dictionary.py to maintain term definitions and links

3. **Adding New Content**:
   - Add to appropriate existing directories
   - Follow naming conventions of existing content
   - Update this index when creating new major sections

---

*This index was last updated on [current date]. Please ensure it remains up-to-date as the project structure evolves.* 