Source:
- https://owasp.org/www-community/Threat_Modeling_Process
- https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- https://github.com/[[_content/dictionary#O|OWASP]]/threat-dragon

## Introduction
- Purpose: Structured approach to identify, quantify, and address security risks in applications.
- Perspective: Looks at systems from an attacker's viewpoint.

## Steps in Threat Modeling

### Scope Your Work:

- Draw diagrams (e.g., Data Flow Diagrams).
- Identify entry points, assets, and trust levels.

### Determine Threats:

- Use methodologies like [[_content/dictionary#S|STRIDE]].
- Identify threats using threat trees and common threat lists.

#### [[_content/dictionary#S|STRIDE]] Threat Categories

| Threat Category         | Violates          | Examples                                                                                                    |
| ----------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Spoofing                | Authenticity      | An attacker steals the authentication token of a legitimate user and uses it to impersonate the user.       |
| Tampering               | Integrity         | An attacker abuses the application to perform unintended updates to a database.                             |
| Repudiation             | Non-repudiability | An attacker manipulates logs to cover their actions.                                                        |
| Information Disclosure  | Confidentiality   | An attacker extract data from a database containing user account info.                                      |
| Denial of Service       | Availability      | An attacker locks a legitimate user out of their account by performing many failed authentication attempts. |
| Elevation of Privileges | Authorization     | An attacker tampers with a JWT to change their role.                                                        |

### Determine Countermeasures and Mitigation:

- Map threats to countermeasures.
- Prioritize based on factors like likelihood and impact.

### Assess Your Work:

- Ensure documentation of diagrams, threat lists, and control lists.

## Additional Information

- Data Flow Diagrams (DFDs): Visual representation of data movement and trust boundaries.
- Trust Levels: Define access rights for external entities.
- Example Diagrams and Threat Lists: Provide practical illustrations and common threats.

This page emphasizes the importance of integrating threat modeling into the Software Development Life Cycle ([[_content/dictionary#S|SDLC]]) to enhance application security.

A big part of threat modelling is Data Flow Diagrams ([[_content/dictionary#D|DFD]]) which are used to gain an understanding of the system we are trying to protect. Without understanding the system, we cannot possibly fathom the attack vectors that might be present. This is why we start of by creating DFD's.

## Comprehensive Threat Model Example

### Threat Model Information (Sample)

**Application Version:** 1.0

**Description:** College library website providing services to librarians, students, and staff. Students and staff can log in and search; staff can request books. Librarians can log in, add books, add users, and search.

**Document Owner:** David Lowry  
**Participants:** David Rook  
**Reviewer:** Eoin Keary

### External Dependencies

External dependencies are items outside the application code that may pose security threats. Document how the application is intended to be run, including security controls.

#### External Dependencies (Sample)

| ID | Description |
|---|---|
| 1 | Linux server running Apache with college's hardening standard |
| 2 | MySQL database on hardened Linux server |
| 3 | Private network between web and database servers |
| 4 | Firewall-protected server with TLS-only communication |

### Entry Points

Entry points are interfaces through which attackers can interact with the application. They define where data enters the system and trust boundaries.

#### Entry Points

| ID    | Name              | Description                            | Trust Levels                                                                            |
| ----- | ----------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| 1     | HTTPS Port        | TLS-secured access point for all pages | (1) Anonymous User<br>(2) Valid Credentials<br>(3) Invalid Credentials<br>(4) Librarian |
| 1.1   | Library Main Page | Initial landing page                   | (1) Anonymous User<br>(2) Valid Credentials<br>(3) Invalid Credentials<br>(4) Librarian |
| 1.2   | Login Page        | Authentication portal                  | (1) Anonymous User<br>(2) Valid Credentials<br>(3) Invalid Credentials<br>(4) Librarian |
| 1.2.1 | Login Function    | Credential validation                  | (2) Valid Credentials<br>(3) Invalid Credentials<br>(4) Librarian                       |
| 1.3   | Search Entry Page | Search functionality                   | (2) Valid Credentials<br>(4) Librarian                                                  |

### Exit Points

Exit points are where data leaves the system and can be targeted in attacks like [[_content/dictionary#X|XSS]] and information disclosure. Exit points without proper security controls may leak confidential information. Error messages at exit points can enable attacks like account harvesting or [[_content/dictionary#S|SQL]] injection.

### Assets

Assets are items attackers target, both physical (user data) and abstract (reputation). Document each with an ID, name, description and required trust levels.

#### Assets

| ID  | Name                        | Description                 | Trust Levels       |
| --- | --------------------------- | --------------------------- | ------------------ |
| 1   | Library Users and Librarian | User-related assets         |                    |
| 1.1 | User Login Details          | Student/faculty credentials | (2)(4)(5)(7)(8)(9) |
| 1.2 | Librarian Login Details     | Librarian credentials       | (4)(5)(7)(8)(9)    |
| 1.3 | Personal Data               | User personal information   | (4)(5)(6)(7)(8)(9) |
| 2   | System                      | Infrastructure assets       |                    |
| 2.1 | Website Availability        | 24/7 system uptime          | (5)(6)             |
| 2.2 | Web Server Code Execution   | Server-side code execution  | (6)(7)             |
| 2.3 | Database Read Access        | SQL select capability       | (5)(8)(9)          |
| 2.4 | Database Read/Write Access  | Full SQL capability         | (5)(9)             |
| 3   | Website                     | Web application assets      |                    |
| 3.1 | Login Session               | User session data           | (2)(4)             |
| 3.2 | Database Server Access      | Database administration     | (5)                |
| 3.3 | User Creation Ability       | Account management          | (4)(6)             |
| 3.4 | Audit Data Access           | Security logging            | (6)                |

### Trust Levels

Trust levels define access rights granted to external entities, cross-referenced with entry points and assets.

#### Trust Levels

| ID  | Name                          | Description                                 |
| --- | ----------------------------- | ------------------------------------------- |
| 1   | Anonymous Web User            | Unauthenticated website visitor             |
| 2   | User with Valid Credentials   | Authenticated student/staff                 |
| 3   | User with Invalid Credentials | Failed authentication attempt               |
| 4   | Librarian                     | Elevated access for user/content management |
| 5   | Database Administrator        | Database read/write access                  |
| 6   | Website Administrator         | Site configuration control                  |
| 7   | Web Server Process            | Server execution context                    |
| 8   | Database Read User            | Read-only database account                  |
| 9   | Database Read/Write User      | Full database access account                |

## A Visual Example

- Do Threat Model (Microsoft Threat Modeling Tool)
- Check the table guide ![Threat Model Example]([[_content/dictionary#T|ThreatModelExampleTable]].png)
- Check appropriate [[_content/dictionary#O|OWASP]] cheat sheet reference for solution to the found problem. [[00_index|Threat Modeling Cheat Sheet]]

