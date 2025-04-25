# Example Self-Assessment: [[_content/dictionary#M|MediSecure]]

## Product Description

**[[_content/dictionary#M|MediSecure]]** is a web-based electronic health record ([[_content/dictionary#E|EHR]]) system designed for small to medium-sized healthcare providers. The application allows healthcare professionals to:

- Manage patient records and medical histories
- Schedule appointments and send automated reminders
- Process prescriptions and view medication histories
- Generate and share medical reports
- Conduct secure video consultations
- Process patient billing and insurance claims

The system is deployed as a cloud-based SaaS offering with a web application interface and native mobile applications for iOS and Android. It integrates with third-party services for payment processing, [[_content/dictionary#S|SMS]] notifications, and insurance verification.

## Self-Assessment Results

### 1. [[_content/dictionary#O|OWASP]] [[_content/dictionary#A|ASVS]] Assessment

#### Assessment Overview

**Target Verification Level**: [[_content/dictionary#A|ASVS]] Level 2 (suitable for applications handling sensitive healthcare data)

**Assessment Scope**: 
- Web application (v3.2.1)
- RESTful [[_content/dictionary#A|API]] services (v2.1.0)
- Mobile application integration (iOS v2.0, Android v2.1) 

**Out of Scope**:
- Third-party payment gateway (handled via redirect to external [[_content/dictionary#P|PCI]]-[[_content/dictionary#D|DSS]] compliant provider)
- Cloud infrastructure ([[_content/dictionary#A|AWS]]) underlying components
- Physical security of data centers

**Assessment Methodology**:
- Manual code review of security-critical components
- Dynamic application security testing ([[_content/dictionary#D|DAST]]) using [[_content/dictionary#O|OWASP]] [[_content/dictionary#Z|ZAP]]
- [[_content/dictionary#A|API]] security testing using Postman and custom scripts
- Authentication and session management testing
- Access control testing across different user roles
- Penetration testing of key application functions

**Evidence Collection**:
- Screenshots of identified vulnerabilities
- [[_content/dictionary#H|HTTP]] request/response logs from intercepting proxy
- Sample exploit scripts for reproducibility
- Code snippets showing vulnerable sections
- Test cases and results documenting both passed and failed tests

#### Certification Statement

Based on the assessment results, **[[_content/dictionary#M|MediSecure]] does not currently meet [[_content/dictionary#A|ASVS]] Level 2 certification requirements**. The application has 10 non-compliant Level 2 requirements, including 3 failed Level 1 requirements. Therefore, the application cannot be certified at any ASVS level at this time. After remediating the Level 1 findings, the application could potentially qualify for Level 1 certification.

#### Summary of Compliance

| Section | Compliant | Partially Compliant | Non-Compliant | N/A | Total Requirements |
|---------|-----------|---------------------|---------------|-----|-------------------|
| V1: Architecture & Design | 7 | 5 | 2 | 0 | 14 |
| V2: Authentication | 16 | 7 | 3 | 0 | 26 |
| V3: Session Management | 6 | 5 | 0 | 0 | 11 |
| V4: Access Control | 8 | 4 | 1 | 0 | 13 |
| V5: Validation & Encoding | 12 | 5 | 2 | 0 | 19 |
| V6: Cryptography | 6 | 4 | 1 | 0 | 11 |
| V7: Error Handling & Logging | 5 | 4 | 0 | 0 | 9 |
| V8: Data Protection | 9 | 3 | 0 | 0 | 12 |
| V9: Communications | 4 | 1 | 0 | 0 | 5 |
| V10: Malicious Code | 5 | 2 | 0 | 0 | 7 |
| V11: Business Logic | 6 | 1 | 1 | 0 | 8 |
| V12: Files & Resources | 9 | 2 | 0 | 2 | 13 |
| V13: API & Web Services | 5 | 3 | 0 | 0 | 8 |
| V14: Configuration | 6 | 2 | 0 | 0 | 8 |
| **Overall** | **104** | **48** | **10** | **2** | **164** |

#### Non-Applicable Requirements

| Requirement ID | Requirement | Justification for Non-Applicability |
|----------------|-------------|-------------------------------------|
| 12.3.6 | Verify that the application does not include and execute functionality from untrusted sources, such as unverified CDNs, JavaScript libraries, npm libraries, or server-side DLLs. | MediSecure is delivered as a dedicated SaaS offering without user-uploadable code or extensions. Customers cannot introduce untrusted code sources. |
| 12.6.1 | Verify that the web or application server is configured with an allow list of resources or systems to which the server can send requests or load data/files from. | MediSecure does not utilize server-side request functionality to external systems. All integration is performed through controlled API endpoints rather than server-initiated requests. |

#### Failed Requirements and Remediation Steps

| Requirement ID | Description | Finding | Remediation |
|----------------|-------------|---------|-------------|
| V1.5.2 (L1) | Verify that threat modeling is performed as part of every user story or feature, with threats identified, rated according to the risk, and controls developed according to the threat. | No evidence of structured threat modeling for patient data processing flows. Ad-hoc security considerations are made but not systematic. | Implement formal threat modeling using STRIDE or similar methodology for all new features. Retroactively perform threat modeling on existing critical workflows, prioritizing patient data handling components. Document all identified threats and their mitigations. |
| V1.11.3 (L2) | Verify that all high-value business logic flows, including authentication, session management and access control are thread safe and resistant to time-of-check and time-of-use race conditions. | The appointment booking system contains a race condition where two users can book the same slot simultaneously. | Implement proper transaction locking in the appointment booking system. Add optimistic concurrency control for critical transactions. Use database-level constraints to prevent double-booking. |
| V2.2.1 (L1) | Verify that anti-automation controls are effective at mitigating breached credential testing, brute force, and account lockout attacks. | No rate-limiting or anti-automation mechanisms present on authentication endpoints. | Implement progressive delays and account lockout policies after failed login attempts. Add CAPTCHA for login attempts after 3 failures. Implement IP-based rate limiting on authentication endpoints. |
| V2.3.6 (L2) | Verify that credentials can be changed by the user and that strong password policy requirements are enforced. | Password changes do not require verification of the existing password. | Modify password change functionality to require current password verification before allowing changes. Ensure password policies are consistently enforced on all change mechanisms. |
| V2.8.3 (L1) | Verify that multi-factor authentication is required for all sensitive operations like account recovery, email change, and personal data access. | MFA is implemented but not enforced for sensitive operations like accessing medical records or account recovery. | Extend MFA requirements to all sensitive operations. Implement step-up authentication for critical operations like medical record access and account recovery flows. |
| V4.1.3 (L2) | Verify that the principle of least privilege exists - users should only be able to access functions, data files, URLs, controllers, services, and other resources, for which they possess specific authorization. | Analysis identified multiple instances where administrative users have excessive privileges beyond their role requirements. | Implement fine-grained role-based access control. Audit all administrative roles and reduce privileges to minimum required. Create specialized administrative roles instead of general admin access. |
| V5.3.4 (L1) | Verify that output encoding is applied based on the context required when data from potentially untrusted sources is used in browser DOM HTML contexts. | XSS vulnerability discovered in appointment scheduling module where patient comments are rendered without proper encoding. | Implement context-aware output encoding for all user-supplied content. Specifically sanitize and encode patient comments in the appointment scheduling module. Consider using template-based auto-escaping frameworks. |
| V5.5.2 (L2) | Verify that all untrusted file uploads are scanned by antivirus scanners to prevent upload of known malicious content. | Document upload functionality for medical records does not include malware scanning before storage. | Integrate antivirus scanning for all uploaded files. Implement file type verification and validation. Consider using cloud-based malware scanning APIs for uploaded content. |
| V6.2.3 (L2) | Verify that all random numbers, random file names, random GUIDs, and random strings are generated using the cryptographic module's approved random number generator when these random values are intended to be not guessable by an attacker. | Session identifiers are generated using Math.random() instead of cryptographically secure random number generation. | Replace all instances of Math.random() with cryptographically secure alternatives (e.g., crypto.getRandomValues() in JavaScript). Audit all security-sensitive random value generation in the application. |
| V11.1.2 (L1) | Verify that the application will only process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly. | No timing controls exist to prevent automated scripting of business processes. | Implement timing controls to detect and prevent automated submission of forms. Add timestamps to multi-step processes to validate realistic human interaction times. Implement anti-automation measures for critical business workflows. |

#### Strengths and Positive Findings

1. **Strong [[_content/dictionary#T|TLS]] Implementation (V9)**: All client and server communications use TLS 1.2+ with secure cipher configurations.
   - Evidence: [[_content/dictionary#S|SSL]] Labs A+ rating for all endpoints
   - Configuration validation confirmed proper [[_content/dictionary#H|HSTS]] implementation and secure cipher selection

2. **Comprehensive Data Protection for [[_content/dictionary#P|PHI]] (V8)**: 
   - All patient health information is encrypted at rest using [[_content/dictionary#A|AES]]-256
   - Proper access controls limit PHI visibility based on treatment relationship
   - Database-level encryption implemented correctly

3. **Well-designed Session Management (V3)**:
   - Session identifiers are securely generated (except finding noted above)
   - Proper session timeout and invalidation controls
   - Secure cookie configurations with [[_content/dictionary#H|HttpOnly]] and Secure flags

### 2. [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] Assessment

We assessed our software development practices using [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] (Software Assurance Maturity Model), which provides a comprehensive framework for evaluating and improving our software security program.

#### Maturity Levels by Business Function

| Business Function | Security Practice | Current Maturity (0-3) | Target Maturity (0-3) |
|-------------------|-------------------|------------------------|----------------------|
| **Governance** | Strategy & Metrics | 1 | 2 |
| | Policy & Compliance | 2 | 3 |
| | Education & Guidance | 1 | 2 |
| **Design** | Threat Assessment | 1 | 3 |
| | Security Requirements | 2 | 3 |
| | Security Architecture | 1 | 2 |
| **Implementation** | Secure Build | 2 | 3 |
| | Secure Deployment | 2 | 2 |
| | Defect Management | 1 | 2 |
| **Verification** | Architecture Assessment | 1 | 2 |
| | Requirements-driven Testing | 1 | 2 |
| | Security Testing | 2 | 3 |
| **Operations** | Incident Management | 2 | 3 |
| | Environment Management | 2 | 2 |
| | Operational Management | 1 | 2 |

#### Detailed Assessment by Business Function

##### Governance

**Strategy & Metrics (Level 1):**
- We have established a basic understanding of our organization's security posture through interviewing business owners and stakeholders.
- We've documented risk factors and drivers linked to our healthcare application priorities.
- We've defined basic metrics to evaluate the effectiveness of our application security program, including effort spent on security, results of security efforts, and environmental metrics.
- **Gap to Level 2:** We need to develop a strategic security plan and budget with milestones, and establish more meaningful KPIs with thresholds for our security program.

**Policy & Compliance (Level 2):**
- We have a comprehensive library of healthcare-specific security policies and standards based on industry regulations ([[_content/dictionary#H|HIPAA]], [[_content/dictionary#G|GDPR]]).
- We've created a compliance matrix mapping our policies to external requirements.
- We've developed application security requirements and test scripts for verifying compliance.
- **Gap to Level 3:** We need a more robust program to measure and report on compliance status across all applications with defined metrics and remediation processes.

**Education & Guidance (Level 1):**
- Security awareness training is conducted for all staff involved in the management, development, and testing of [[_content/dictionary#M|MediSecure]].
- We've implemented a Security Champion program where each development team has a designated security liaison.
- **Gap to Level 2:** We need to implement role-specific security training (developers, testers, product managers) and establish a formal secure coding center of excellence.

##### Design

**Threat Assessment (Level 1):**
- We perform ad-hoc threat modeling for high-risk components using simple threat checklists ([[_content/dictionary#S|STRIDE]]).
- We have a basic application risk profile system based on data classification and exposure.
- **Gap to Level 3:** We need to implement a standardized threat modeling methodology, provide training to all architects and security champions, and integrate threat modeling artifacts with our security tools.

**Security Requirements (Level 2):**
- We have a structured approach for identifying security requirements from multiple sources including policies and legislation.
- Domain experts are involved in the requirements definition process.
- **Gap to Level 3:** We need to establish a comprehensive security requirements framework with reusable requirements categories and quality guidance.

**Security Architecture (Level 1):**
- Technical staff uses a checklist of security principles during design (defense in depth, least privilege, etc.).
- We have an inventory of technologies and frameworks with documentation of their security features.
- **Gap to Level 2:** We need to establish common design patterns and reference architectures that satisfy our organization's security objectives, particularly for healthcare-specific scenarios.

##### Implementation

**Secure Build (Level 2):**
- We have established secure coding standards for our primary development frameworks.
- Our [[_content/dictionary#C|CI]] pipeline includes automated vulnerability scanning.
- **Gap to Level 3:** We need to implement more comprehensive software composition analysis and formalize a mature secure build process across all applications.

**Secure Deployment (Level 2):**
- We have defined deployment environments with security controls.
- Production deployments follow a standard process with security verification.
- **Gap to Level 2:** Our current level is appropriate for our organization, but we need to maintain consistency and monitor effectiveness.

**Defect Management (Level 1):**
- We track security defects in our issue tracking system but lack a formal prioritization scheme.
- **Gap to Level 2:** We need to implement a risk-based approach to defect management with defined SLAs based on severity.

##### Verification

**Architecture Assessment (Level 1):**
- We perform basic architecture reviews but lack consistency and follow-through.
- **Gap to Level 2:** We need to establish a formal architecture review process with security-focused checkpoints.

**Requirements-driven Testing (Level 1):**
- Some security requirements are tested, but the process is not formalized or comprehensive.
- **Gap to Level 2:** We need to establish security test plans aligned with security requirements and implement coverage tracking.

**Security Testing (Level 2):**
- We conduct regular security testing including both automated scanning and manual testing.
- **Gap to Level 3:** We need to integrate security testing into the development pipeline and establish periodic adversarial testing.

##### Operations

**Incident Management (Level 2):**
- We have established incident response procedures with defined roles.
- Incidents are tracked and analyzed for trends.
- **Gap to Level 3:** We need to improve the integration between development and operations teams for incident handling and implement regular incident response exercises.

**Environment Management (Level 2):**
- Production environments are hardened according to baseline standards.
- We conduct regular vulnerability scans of our infrastructure.
- **Gap to Level 2:** Our current level is appropriate, but we need to monitor effectiveness and improve automation.

**Operational Management (Level 1):**
- Basic operational security processes are in place but lack formalization and complete coverage.
- **Gap to Level 2:** We need to establish a formal process for operational security activities and improve monitoring capabilities.

#### Key Strengths

1. **Policy & Compliance (2/3)**: Strong regulatory compliance with [[_content/dictionary#H|HIPAA]] and [[_content/dictionary#G|GDPR]] requirements, including a well-defined compliance matrix mapping our policies to external requirements.

2. **Secure Build (2/3)**: Established secure coding practices with automated vulnerability scanning integrated into our [[_content/dictionary#C|CI]] pipeline, providing early detection of common security issues.

3. **Incident Management (2/3)**: Well-documented incident response procedures with clearly defined roles and responsibilities, allowing for effective handling of security incidents.

4. **Security Testing (2/3)**: Comprehensive security testing program that includes automated scanning, manual testing, and defined remediation processes.

5. **Environment Management (2/3)**: Production environments are configured according to security baselines with regular vulnerability scanning.

#### Areas Needing Improvement

1. **Threat Assessment (1/3)**: Currently performing ad-hoc threat modeling for some features. Need to implement a formal threat modeling process for all major features and integrate it into the development lifecycle. Healthcare applications are prime targets for attackers seeking protected health information, making this a critical area for improvement.

2. **Education & Guidance (1/2)**: Developer security training is inconsistent. Need to establish a formal security education program for all development staff with role-specific content. Security Champions need more formalized support and training.

3. **Architecture Assessment (1/2)**: Security architecture reviews are performed but not consistently. Need to formalize the process and perform regular assessments, especially for components handling patient data.

4. **Operational Management (1/2)**: Limited visibility into security metrics for systems in production. Need to improve monitoring capabilities and establish formal security operations processes.

5. **Defect Management (1/2)**: Security defects are tracked but lack proper prioritization and consistent remediation timelines. Need to implement a risk-based approach to defect management with clear SLAs.

#### [[_content/dictionary#S|SAMM]] Remediation Roadmap

**Short-term (0-3 months):**
- Establish role-specific security training for developers, testers, and product managers
- Implement a risk-based security defect management process with clear SLAs
- Formalize the Security Champion program with defined responsibilities and support structure

**Medium-term (3-6 months):**
- Develop a standardized threat modeling methodology and train architects and security champions
- Implement formal architecture review process with security checkpoints
- Create a security requirements framework with reusable requirements by category

**Long-term (6-12 months):**
- Integrate security testing fully into the development pipeline
- Establish common design patterns and reference architectures for healthcare applications
- Improve incident response capabilities through cross-team exercises and better integration

### 3. [[_content/dictionary#C|CIS]] Controls Assessment

We assessed our infrastructure and security controls against the [[_content/dictionary#C|CIS]] Critical Security Controls framework.

#### Implementation Status

| Control | Implementation Level | Notes |
|---------|---------------------|-------|
| 1. Inventory and Control of Enterprise Assets | Partial | Need better tracking of cloud resources |
| 2. Inventory and Control of Software Assets | Good | Software inventory well-maintained |
| 3. Data Protection | Good | Strong encryption and access controls for PHI |
| 4. Secure Configuration of Enterprise Assets and Software | Partial | Configuration management needs improvement |
| 5. Account Management | Good | Well-defined identity management |
| 6. Access Control Management | Good | Role-based access control implemented |
| 7. Continuous Vulnerability Management | Partial | Patch management needs improvement |
| 8. Audit Log Management | Partial | Log centralization and monitoring needs improvement |
| 9. Email and Web Browser Protections | Good | Security controls for corporate endpoints |
| 10. Malware Defenses | Good | Anti-malware solutions deployed |
| 11. Data Recovery | Good | Regular backups with testing |
| 12. Network Infrastructure Management | Partial | Network documentation outdated |
| 13. Network Monitoring and Defense | Minimal | Limited network monitoring capabilities |
| 14. Security Awareness and Skills Training | Partial | Training program needs expansion |
| 15. Service Provider Management | Partial | Third-party risk management needs improvement |
| 16. Application Software Security | Partial | SDLC security integration in progress |
| 17. Incident Response Management | Good | Documented incident response procedures |
| 18. Penetration Testing | Minimal | Limited scope penetration testing |

#### Key Findings

**Highest Priority Remediation Areas:**

1. **Control 13 - Network Monitoring and Defense**: Implement a network monitoring solution with intrusion detection capabilities.

2. **Control 18 - Penetration Testing**: Establish a comprehensive penetration testing program covering all application components.

3. **Control 7 - Continuous Vulnerability Management**: Improve patch management processes, especially for third-party components.

**Strengths:**

1. **Control 3 - Data Protection**: Strong encryption and access controls for protected health information.
2. **Control 5 & 6 - Account and Access Management**: Well-implemented identity and access management.
3. **Control 11 - Data Recovery**: Robust backup and recovery procedures.

## Remediation Plan Summary

Based on the combined assessment results, we have identified the following key areas for improvement:

1. **Short-term (0-3 months)**:
   - Implement brute force protection for authentication systems
   - Formalize and expand developer security training program
   - Implement centralized log management and monitoring

2. **Medium-term (3-6 months)**:
   - Establish comprehensive threat modeling for all major features
   - Implement network monitoring with intrusion detection
   - Improve patch management processes

3. **Long-term (6-12 months)**:
   - Conduct full penetration testing of all application components
   - Achieve [[_content/dictionary#A|ASVS]] Level 2 compliance for all requirements
   - Improve [[_content/dictionary#S|SAMM]] maturity levels to target state in all areas 