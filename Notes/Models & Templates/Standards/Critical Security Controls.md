# [[_content/dictionary#C|CIS]] Critical Security Controls

## Overview

The [[_content/dictionary#C|CIS]] Critical Security Controls® (CIS Controls®) started as a grassroots activity to identify the most common and important real-world cyber attacks that affect enterprises every day. The goal was to translate that knowledge into positive, constructive actions for defenders, and share that information with a wider audience.

Led by the Center for Internet Security® ([[_content/dictionary#C|CIS]]®), the CIS Controls have evolved into an international community of volunteer individuals and institutions that:

- Share insights into attacks and attackers, identify root causes, and translate that into classes of defensive action
- Create and share tools, working aids, and stories of adoption and problem-solving
- Map the [[_content/dictionary#C|CIS]] Controls to regulatory and compliance frameworks
- Identify and solve common problems and barriers as a community

## Structure of [[_content/dictionary#C|CIS]] Controls

The [[_content/dictionary#C|CIS]] Controls are organized into a structure that includes:

- **Controls**: 18 high-level categories of cybersecurity actions
- **Safeguards**: Specific actions within each Control to improve security posture
- **Implementation Groups (IGs)**: Categories that help organize Safeguards by complexity and resource requirements

### Implementation Groups

**IG1 - Basic Cyber Hygiene**
- For small to medium-sized enterprises with limited [[_content/dictionary#I|IT]] and cybersecurity expertise
- Focuses on keeping the business operational with limited tolerance for downtime
- Implements fundamental safeguards to protect against general, non-targeted attacks

**IG2 - Foundational Cyber Hygiene** (Includes IG1)
- For enterprises with individuals responsible for managing and protecting [[_content/dictionary#I|IT]] infrastructure
- Supports multiple departments with differing risk profiles
- May have regulatory compliance burdens
- Can withstand short interruptions of service
- Implements safeguards to help security teams cope with increased operational complexity

**IG3 - Organizational Cyber Hygiene** (Includes IG1 and IG2)
- For enterprises with security experts specializing in different facets of cybersecurity
- Assets and data contain sensitive information subject to regulatory and compliance oversight
- Must address availability of services and the confidentiality and integrity of sensitive data
- Implements advanced safeguards to abate targeted attacks and reduce the impact of zero-day attacks

## Asset Classes

The [[_content/dictionary#C|CIS]] Controls organize assets into various classes:

### Devices
- **Enterprise Assets**: Assets with the potential to store or process data
  - **End-user Devices**: [[_content/dictionary#I|IT]] assets used by members of an enterprise (desktops, workstations)
    - **Portable Devices**: End-user devices that can wirelessly connect to a network
      - **Mobile Devices**: Small enterprise-issued devices with intrinsic wireless capability
  - **Servers**: Devices that provide resources, data, services, or programs
  - **[[_content/dictionary#I|IoT]] and Non-computing Devices**: Devices embedded with sensors, software, and other technologies
  - **Network Devices**: Electronic devices for network communication and interaction
- **Removable Media**: Storage devices that can be removed while a system is running

### Software
- **Applications**: Programs running on top of an operating system
- **Operating Systems**: Software that manages computer hardware and software resources
  - **Services**: Programs performing well-defined critical tasks for the operating system
  - **Library**: Shareable pre-compiled codebase used to develop software
  - **[[_content/dictionary#A|API]]**: Rules and interfaces for software components to interact
- **Firmware**: Software stored within a device's non-volatile memory

### Data
- **Sensitive Data**: Data that must be kept private and would cause harm if compromised
- **Log Data**: Computer-generated data files recording events
- **Physical Data**: Data stored in physical documents or on physical removable devices

### Users
- **Workforce**: Individuals employed or engaged by an organization with access to systems
- **Service Providers**: Entities offering platforms, software, and services to enterprises
- **User Accounts**: Standard user accounts with limited privileges
- **Administrator Accounts**: Accounts with escalated privileges for management functions
- **Service Accounts**: Accounts created specifically to run applications, services, and tasks

### Network
- **Network Infrastructure**: Collection of hardware and software enabling connectivity
- **Network Architecture**: Physical and logical design of a network

### Documentation
- **Plan**: Documents that implement policies
- **Policy**: Official governance statements outlining security program objectives
- **Process**: Set of general tasks and activities to achieve security-related goals
- **Procedure**: Ordered steps for accomplishing specific tasks

## [[_content/dictionary#C|CIS]] Controls List

### Control 1: Inventory and Control of Enterprise Assets
*Safeguards: 5 | IG1: 2/5 | IG2: 4/5 | IG3: 5/5*

**Overview**: Actively manage all enterprise assets connected to the infrastructure to ensure proper security monitoring, incident response, and recovery.

**Why is this Control critical?**: Enterprises cannot defend what they don't know they have. Attackers constantly scan for unprotected assets, and unidentified assets can be security weak points.

**Key Safeguards**:
1. Establish and maintain a detailed enterprise asset inventory
2. Address unauthorized assets
3. Utilize an active discovery tool
4. Use [[_content/dictionary#D|DHCP]] logging to update asset inventory
5. Use a passive asset discovery tool

### Control 2: Inventory and Control of Software Assets
*Safeguards: 7 | IG1: 3/7 | IG2: 6/7 | IG3: 7/7*

**Overview**: Actively manage all software on the network so that only authorized software is installed and executed.

**Why is this Control critical?**: A complete software inventory prevents attacks by identifying vulnerable software and closing the door on potential backdoors.

**Key Safeguards**:
1. Establish and maintain a software inventory
2. Ensure authorized software is currently supported
3. Address unauthorized software
4. Utilize automated software inventory tools
5. Allowlist authorized software
6. Allowlist authorized libraries
7. Allowlist authorized scripts

### Control 3: Data Protection
*Safeguards: 14 | IG1: 6/14 | IG2: 12/14 | IG3: 14/14*

**Overview**: Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data.

**Why is this Control critical?**: Data is no longer contained within an enterprise's border, making data protection crucial to prevent exfiltration and ensure compliance with privacy regulations.

**Key Safeguards**:
1. Establish and maintain a data management process
2. Establish and maintain a data inventory
3. Configure data access control lists
4. Enforce data retention
5. Securely dispose of data
6. Encrypt data on end-user devices
7. Establish and maintain a data classification scheme
8. Document data flows
9. Encrypt data on removable media
10. Encrypt sensitive data in transit
11. Encrypt sensitive data at rest
12. Segment data processing and storage based on sensitivity
13. Deploy a data loss prevention solution
14. Log sensitive data access

### Control 4: Secure Configuration of Enterprise Assets and Software
*Safeguards: 12 | IG1: 7/12 | IG2: 11/12 | IG3: 12/12*

**Overview**: Establish and maintain secure configurations for all enterprise assets and software.

**Why is this Control critical?**: Default configurations are often geared toward ease-of-deployment rather than security. Maintaining secure configurations prevents exploitation.

**Key Safeguards**:
1. Establish and maintain a secure configuration process
2. Establish and maintain a secure configuration process for network infrastructure
3. Configure automatic session locking on enterprise assets
4. Implement and manage a firewall on servers
5. Implement and manage a firewall on end-user devices
6. Securely manage enterprise assets and software
7. Manage default accounts on enterprise assets and software
8. Uninstall or disable unnecessary services
9. Configure trusted [[_content/dictionary#D|DNS]] servers
10. Enforce automatic device lockout on portable end-user devices
11. Enforce remote wipe capability on portable end-user devices
12. Separate enterprise workspaces on mobile end-user devices

### Control 5: Account Management
*Safeguards: 6 | IG1: 4/6 | IG2: 6/6 | IG3: 6/6*

**Overview**: Use processes and tools to assign and manage authorization to credentials for user accounts, including administrator and service accounts.

**Why is this Control critical?**: It's easier for attackers to gain unauthorized access through valid user credentials than through "hacking" the environment.

**Key Safeguards**:
1. Establish and maintain an inventory of accounts
2. Use unique passwords
3. Disable dormant accounts
4. Restrict administrator privileges to dedicated administrator accounts
5. Establish and maintain an inventory of service accounts
6. Centralize account management

### Control 6: Access Control Management
*Safeguards: 8 | IG1: 5/8 | IG2: 7/8 | IG3: 8/8*

**Overview**: Use processes and tools to create, assign, manage, and revoke access credentials and privileges.

**Why is this Control critical?**: Proper access control ensures users only have access to data and assets appropriate for their role.

**Key Safeguards**:
1. Establish an access granting process
2. Establish an access revoking process
3. Require [[_content/dictionary#M|MFA]] for externally-exposed applications
4. Require MFA for remote network access
5. Require MFA for administrative access
6. Establish and maintain an inventory of authentication and authorization systems
7. Centralize access control
8. Define and maintain role-based access control

### Control 7: Continuous Vulnerability Management
*Safeguards: 7 | IG1: 4/7 | IG2: 7/7 | IG3: 7/7*

**Overview**: Continuously assess and track vulnerabilities to remediate and minimize the window of opportunity for attackers.

**Why is this Control critical?**: Attackers exploit vulnerabilities quickly, making timely remediation crucial for defense.

**Key Safeguards**:
1. Establish and maintain a vulnerability management process
2. Establish and maintain a remediation process
3. Perform automated operating system patch management
4. Perform automated application patch management
5. Perform automated vulnerability scans of internal enterprise assets
6. Perform automated vulnerability scans of externally-exposed enterprise assets
7. Remediate detected vulnerabilities

### Control 8: Audit Log Management
*Safeguards: 12 | IG1: 3/12 | IG2: 11/12 | IG3: 12/12*

**Overview**: Collect, alert, review, and retain audit logs to detect, understand, or recover from an attack.

**Why is this Control critical?**: Log collection and analysis are critical for detecting malicious activity and understanding the extent of attacks.

**Key Safeguards**:
1. Establish and maintain an audit log management process
2. Collect audit logs
3. Ensure adequate audit log storage
4. Standardize time synchronization
5. Collect detailed audit logs
6. Collect [[_content/dictionary#D|DNS]] query audit logs
7. Collect [[_content/dictionary#U|URL]] request audit logs
8. Collect command-line audit logs
9. Centralize audit logs
10. Retain audit logs
11. Conduct audit log reviews
12. Collect service provider logs

### Control 9: Email and Web Browser Protections
*Safeguards: 7 | IG1: 2/7 | IG2: 6/7 | IG3: 7/7*

**Overview**: Improve protections against threats from email and web vectors, which are common entry points for attackers.

**Why is this Control critical?**: Email and web browsers are prime targets for malicious code and social engineering due to their direct interaction with users.

**Key Safeguards**:
1. Ensure use of only fully supported browsers and email clients
2. Use [[_content/dictionary#D|DNS]] filtering services
3. Maintain and enforce network-based [[_content/dictionary#U|URL]] filters
4. Restrict unnecessary or unauthorized browser and email client extensions
5. Implement [[_content/dictionary#D|DMARC]]
6. Block unnecessary file types
7. Deploy and maintain email server anti-malware protections

### Control 10: Malware Defenses
*Safeguards: 5 | IG1: 2/5 | IG2: 3/5 | IG3: 5/5*

**Overview**: Prevent or control the installation, spread, and execution of malicious applications, code, or scripts.

**Key Safeguards**:
1. Deploy and maintain anti-malware software
2. Configure automatic anti-malware signature updates
3. Disable autorun and autoplay for removable media
4. Configure automatic scanning of removable media
5. Enable anti-exploitation features

### Control 11: Data Recovery
*Safeguards: 5 | IG1: 4/5 | IG2: 5/5 | IG3: 5/5*

**Overview**: Establish and maintain data recovery practices sufficient to restore in-scope enterprise assets to a pre-incident and trusted state.

**Key Safeguards**:
1. Establish and maintain a data recovery process
2. Perform automated backups
3. Protect recovery data
4. Establish and maintain an isolated instance of recovery data
5. Test data recovery

### Control 12: Network Infrastructure Management
*Safeguards: 8 | IG1: 2/8 | IG2: 6/8 | IG3: 8/8*

**Overview**: Establish, implement, and actively manage network devices to prevent attackers from exploiting vulnerable network services and access points.

**Key Safeguards**:
1. Ensure network infrastructure is up-to-date
2. Establish and maintain a secure network architecture
3. Securely manage network infrastructure
4. Establish and maintain architecture diagram(s)
5. Centralize network authentication, authorization, and auditing ([[_content/dictionary#A|AAA]])
6. Use secure network management and communication protocols
7. Ensure remote devices utilize a [[_content/dictionary#V|VPN]] and are connecting to an enterprise's AAA infrastructure
8. Establish and maintain dedicated computing resources for all administrative work

### Control 13: Network Monitoring and Defense
*Safeguards: 8 | IG1: 0/8 | IG2: 6/8 | IG3: 8/8*

**Overview**: Operate processes and tooling to establish and maintain comprehensive network monitoring and defense against security threats.

**Key Safeguards**:
1. Centralize security event alerting
2. Deploy a host-based intrusion detection solution
3. Deploy a network intrusion detection solution
4. Perform traffic filtering between network segments
5. Manage access control for remote assets
6. Collect network traffic flow logs
7. Deploy a network-based intrusion prevention solution
8. Deploy a host-based intrusion prevention solution

### Control 14: Security Awareness and Skills Training
*Safeguards: 9 | IG1: 3/9 | IG2: 8/9 | IG3: 9/9*

**Overview**: Establish and maintain a security awareness program to influence behavior among the workforce to be security conscious and properly skilled to reduce cybersecurity risks.

**Key Safeguards**:
1. Establish and maintain a security awareness program
2. Train workforce members to recognize social engineering attacks
3. Train workforce members on authentication best practices
4. Train workforce on data handling best practices
5. Train workforce members on causes of unintentional data exposure
6. Train workforce members on recognizing and reporting security incidents
7. Train workforce on how to identify and report if their enterprise assets are missing security updates
8. Train workforce on the dangers of connecting to and transmitting enterprise data over insecure networks
9. Conduct role-specific security awareness and skills training

### Control 15: Service Provider Management
*Safeguards: 7 | IG1: 1/7 | IG2: 3/7 | IG3: 7/7*

**Overview**: Develop a process to evaluate service providers who hold sensitive data, or provide critical services to the enterprise.

**Key Safeguards**:
1. Establish and maintain an inventory of service providers
2. Establish and maintain a service provider management policy
3. Classify service providers
4. Ensure service provider contracts include security requirements
5. Assess service providers
6. Monitor service providers
7. Securely decommission service providers

### Control 16: Application Software Security
*Safeguards: 14 | IG1: 0/14 | IG2: 8/14 | IG3: 14/14*

**Overview**: Manage the security life cycle of in-house developed, hosted, or acquired software to prevent, detect, and remediate security weaknesses.

**Key Safeguards**:
1. Establish and maintain a secure application development process
2. Establish and maintain a process to accept and address software vulnerabilities
3. Perform root cause analysis on security vulnerabilities
4. Establish and manage an inventory of third-party software components
5. Use up-to-date and trusted third-party software components
6. Establish and maintain a severity rating system and process for application vulnerabilities
7. Use standard hardening configuration templates for application infrastructure
8. Separate production and non-production systems
9. Train developers in secure coding
10. Apply secure design principles in application architectures
11. Implement code-level security checks
12. Implement secure software development life cycle ([[_content/dictionary#S|SSDLC]]) processes
13. Conduct threat modeling
14. Establish and maintain a secure application deployment process

### Control 17: Incident Response Management
*Safeguards: 9 | IG1: 1/9 | IG2: 7/9 | IG3: 9/9*

**Overview**: Establish a program to develop and maintain an incident response capability.

**Key Safeguards**:
1. Designate personnel to manage incident handling
2. Establish and maintain contact information for reporting security incidents
3. Establish and maintain an enterprise process for the workforce to report security incidents
4. Establish and maintain an incident response process
5. Assign key roles and responsibilities
6. Define mechanisms for communicating during incident response
7. Conduct routine incident response exercises
8. Conduct post-incident reviews
9. Establish and maintain security incident thresholds

### Control 18: Penetration Testing
*Safeguards: 5 | IG1: 0/5 | IG2: 4/5 | IG3: 5/5*

**Overview**: Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses.

**Key Safeguards**:
1. Establish and maintain a penetration testing program
2. Perform periodic external penetration tests
3. Perform periodic internal penetration tests
4. Include tests for presence of unprotected system information and credentials
5. Validate security measures after each penetration test 