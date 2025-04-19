---
title: "Threat Modeling Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html"
created: "1741872882.17345"
tags: [owasp, cheatsheet, security, threat-modeling]
---

# Threat Modeling Cheat Sheet

## Introduction and Mindset

Threat modeling is a structured activity for identifying and documenting adverse actions that may negatively impact a system being developed. It's a proactive approach where teams identify and classify threats in an iterative process to inform design decisions and drive security requirements.

This cheat sheet focuses on providing an entry point for implementing a structured threat modeling process, especially for software projects in a Continuous Integration/Deployment ([[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]) environment.

## When to Do Threat Modeling

Threat modeling can be performed:

1. **During design**: Ideal time to influence security architecture
2. **During development**: To capture threats introduced during implementation
3. **For legacy applications**: To understand existing vulnerabilities
4. **After security incidents**: To understand how to better design systems

Threat modeling should be integrated into your Software Development Life Cycle ([[_content/dictionary#S|SDLC]]).

## Four Question Framework

Effective threat modeling addresses these four questions:

1. **What are we building?** (Scope)
2. **What can go wrong?** (Threats)
3. **What are we going to do about it?** (Mitigations)
4. **Did we do a good enough job?** (Validation)

## Threat Modeling Process

### 1. Scope Your Work

- **Create a data flow diagram ([[_content/dictionary#D|DFD]])**
  - Identify system boundaries
  - Define trust boundaries
  - Map data flows
- **Identify entry points** where attackers can interact with the application
- **Identify assets** that need protection
- **Establish trust levels** for different users/components

### 2. Identify Threats

- Use a methodology like [[_content/dictionary#S|STRIDE]] to discover potential threats
- Consider threat trees and attack vectors
- Create a list of threats applicable to your system

#### [[_content/dictionary#S|STRIDE]] Threat Categories

| Threat Category         | Violates          | Examples                                                                                                    |
| ----------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Spoofing                | Authenticity      | An attacker steals the authentication token of a legitimate user and uses it to impersonate the user.       |
| Tampering               | Integrity         | An attacker abuses the application to perform unintended updates to a database.                             |
| Repudiation             | Non-repudiability | An attacker manipulates logs to cover their actions.                                                        |
| Information Disclosure  | Confidentiality   | An attacker extracts data from a database containing user account info.                                      |
| Denial of Service       | Availability      | An attacker locks a legitimate user out of their account by performing many failed authentication attempts. |
| Elevation of Privileges | Authorization     | An attacker tampers with a JWT to change their role.                                                        |

### 3. Determine Countermeasures and Mitigations

- Identify security controls for each threat
- Prioritize based on risk (likelihood × impact)
- Document mitigation strategies
- Update design documentation to include security controls

### 4. Validate and Verify

- Review the threat model for completeness
- Cross-check threats against countermeasures
- Conduct security testing to verify effectiveness of controls
- Continuously update the threat model as the system evolves

## Data Flow Diagrams (DFDs)

Data Flow Diagrams (DFDs) are a core component of threat modeling. They help visualize how data moves through your system, making it easier to identify potential vulnerabilities.

### [[_content/dictionary#D|DFD]] Elements

1. **External Entities**: Users, other systems, or external services that interact with your system (squares)
2. **Processes**: Operations performed on data (circles)
3. **Data Stores**: Where data is stored (parallel lines)
4. **Data Flows**: Movement of data between elements (arrows)
5. **Trust Boundaries**: Points where data crosses security domains (dashed lines)

### Sample [[_content/dictionary#D|DFD]] Notation

```
┌───────────┐         ┌───────────┐
│           │         │           │
│   User    │──────▶  │   Web     │
│           │         │   Server  │
└───────────┘         └─────┬─────┘
                            │
                            ▼
                      ┌───────────┐
                      │           │
                      │ Database  │
                      │           │
                      └───────────┘
```

## Microsoft Threat Modeling Tool

The Microsoft Threat Modeling Tool ([[_content/dictionary#T|TMT]]) provides a structured approach for creating threat models. The tool allows you to:

1. Create data flow diagrams using drag-and-drop interfaces
2. Auto-generate threats based on the diagrams
3. Document and track mitigations
4. Generate reports

### Using Microsoft [[_content/dictionary#T|TMT]]

1. **Create a Model**: Start by mapping out your system
2. **Add Components**: Including processes, data stores, external entities, and data flows
3. **Define Trust Boundaries**: Show where security contexts change
4. **Generate Threats**: The tool auto-generates threats based on the [[_content/dictionary#S|STRIDE]] model
5. **Document Mitigations**: For each identified threat
6. **Save as .tm7 file**: The default [[_content/dictionary#T|TMT]] file format

## Comprehensive Threat Model Documentation

A complete threat model should include:

### 1. Threat Model Information

- **Application Version**
- **Description** of the system
- **Document Owner**, participants, and reviewers

### 2. External Dependencies

Document items outside the application code that may pose security threats:

| ID | Description |
|---|---|
| 1 | Linux server running Apache with hardening standard |
| 2 | MySQL database on hardened Linux server |
| 3 | Private network between web and database servers |
| 4 | Firewall-protected server with TLS-only communication |

### 3. Entry Points

Document interfaces through which attackers can interact with the application:

| ID    | Name          | Description           | Trust Levels |
| ----- | ------------- | --------------------- | ------------ |
| 1     | HTTPS Port    | TLS-secured access    | (1) Anonymous User (2) Authenticated User |
| 1.1   | Login Page    | Authentication portal | (1) Anonymous User |
| 1.2   | API Endpoint  | Data access interface | (2) Authenticated User |

### 4. Assets

Document items attackers might target:

| ID | Name | Description | Trust Levels |
|---|---|---|---|
| 1 | User Credentials | Login information | (2)(3) |
| 2 | Personal Data | Customer information | (2)(3) |
| 3 | System Availability | Service uptime | (3) |

### 5. Trust Levels

Define access rights granted to different entities:

| ID | Name | Description |
|---|---|---|
| 1 | Anonymous User | Unauthenticated visitor |
| 2 | Authenticated User | Logged-in regular user |
| 3 | Administrator | System administrator |

## Best Practices

1. **Keep it simple**: Focus on most relevant threats first
2. **Use existing resources**: Leverage threat databases and knowledge bases
3. **Collaborate**: Involve security experts, developers, and business stakeholders
4. **Iterate**: Threat modeling is not a one-time activity
5. **Automate where possible**: Use tools to help identify and track threats
6. **Document decisions**: Record why certain threats were addressed or accepted

## [[_content/dictionary#O|OWASP]] Resources

- [[[_content/dictionary#O|OWASP]] Threat Dragon](https://owasp.org/www-project-threat-dragon/): Open-source threat modeling tool
- [[[_content/dictionary#O|OWASP]] Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/): Security requirements by threat categories
- [[[_content/dictionary#O|OWASP]] Top Ten](https://owasp.org/www-project-top-ten/): Most critical web application security risks

## Integration with Development Workflow

Integrating threat modeling into development workflows:

- **Design phase**: Create initial threat model
- **Development phase**: Update as new features are implemented
- **Code reviews**: Check for security controls addressing identified threats
- **Testing**: Verify mitigations with security tests
- **Deployment**: Review and update for production concerns
- **Maintenance**: Update threat model as system evolves

Remember that threat modeling is an iterative process that evolves with your system. Regular updates and reviews are essential to maintaining security throughout the application lifecycle.