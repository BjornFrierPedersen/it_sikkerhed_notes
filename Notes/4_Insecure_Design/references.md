# A04:2021 - Insecure Design - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Threat Modeling Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
   - Provides guidance on identifying and addressing security threats during design
   - Covers methodologies, tools, and best practices for threat modeling

2. [Attack Surface Analysis Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
   - Helps identify and minimize the attack surface of an application
   - Important for secure design considerations

3. [Secure Product Design Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Secure_Product_Design_Cheat_Sheet.html)
   - Guidance on incorporating security into product design
   - Covers security requirements, threat modeling, and design reviews

4. [Abuse Case Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Abuse_Case_Cheat_Sheet.html)
   - Helps identify how an application might be misused or abused
   - Important for understanding potential attack scenarios during design

5. [Microservices Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Microservices_Security_Cheat_Sheet.html)
   - Security considerations for microservices architecture
   - Covers design patterns and security controls specific to microservices

6. [Microservices based Security Arch Doc Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Microservices_based_Security_Arch_Doc_Cheat_Sheet.html)
   - Guidance on documenting security architecture for microservices
   - Helps ensure security is considered in architectural documentation

7. [Secure Cloud Architecture Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)
   - Security considerations for cloud architecture
   - Covers design patterns and security controls for cloud environments

8. [Infrastructure as Code Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)
   - Security considerations for infrastructure as code
   - Helps ensure security is built into infrastructure design

9. [Authentication Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authentication_Cheat_Sheet.html)
   - Design considerations for secure authentication systems
   - Covers authentication mechanisms and security controls

10. [Authorization Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authorization_Cheat_Sheet.html)
    - Design considerations for secure authorization systems
    - Covers authorization models and security controls

11. [Session Management Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Session_Management_Cheat_Sheet.html)
    - Design considerations for secure session management
    - Covers session handling mechanisms and security controls

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-73: External Control of File Name or Path
- [[_content/dictionary#C|CWE]]-183: Permissive List of Allowed Inputs
- [[_content/dictionary#C|CWE]]-209: Generation of Error Message Containing Sensitive Information
- [[_content/dictionary#C|CWE]]-213: Exposure of Sensitive Information Due to Incompatible Policies
- [[_content/dictionary#C|CWE]]-235: Improper Handling of Extra Parameters
- [[_content/dictionary#C|CWE]]-256: Unprotected Storage of Credentials
- [[_content/dictionary#C|CWE]]-257: Storing Passwords in a Recoverable Format
- [[_content/dictionary#C|CWE]]-266: Incorrect Privilege Assignment
- [[_content/dictionary#C|CWE]]-269: Improper Privilege Management
- [[_content/dictionary#C|CWE]]-280: Improper Handling of Insufficient Permissions or Privileges
- [[_content/dictionary#C|CWE]]-311: Missing Encryption of Sensitive Data
- [[_content/dictionary#C|CWE]]-312: Cleartext Storage of Sensitive Information
- [[_content/dictionary#C|CWE]]-313: Cleartext Storage in a File or on Disk
- [[_content/dictionary#C|CWE]]-316: Cleartext Storage of Sensitive Information in Memory
- [[_content/dictionary#C|CWE]]-419: Unprotected Primary Channel
- [[_content/dictionary#C|CWE]]-430: Deployment of Wrong Handler
- [[_content/dictionary#C|CWE]]-434: Unrestricted Upload of File with Dangerous Type
- [[_content/dictionary#C|CWE]]-444: Inconsistent Interpretation of [[_content/dictionary#H|HTTP]] Requests
- [[_content/dictionary#C|CWE]]-451: User Interface ([[_content/dictionary#U|UI]]) Misrepresentation of Critical Information
- [[_content/dictionary#C|CWE]]-472: External Control of Assumed-Immutable Web Parameter
- [[_content/dictionary#C|CWE]]-501: Trust Boundary Violation
- [[_content/dictionary#C|CWE]]-522: Insufficiently Protected Credentials
- [[_content/dictionary#C|CWE]]-525: Use of Web Browser Cache Containing Sensitive Information
- [[_content/dictionary#C|CWE]]-539: Use of Persistent Cookies Containing Sensitive Information
- [[_content/dictionary#C|CWE]]-579: J2EE Bad Practices: Non-serializable Object Stored in Session
- [[_content/dictionary#C|CWE]]-598: Use of [[_content/dictionary#G|GET]] Request Method With Sensitive Query Strings
- [[_content/dictionary#C|CWE]]-602: Client-Side Enforcement of Server-Side Security
- [[_content/dictionary#C|CWE]]-642: External Control of Critical State Data
- [[_content/dictionary#C|CWE]]-646: Reliance on File Name or Extension of Externally-Supplied File
- [[_content/dictionary#C|CWE]]-650: Trusting [[_content/dictionary#H|HTTP]] Permission Methods on the Server Side
- [[_content/dictionary#C|CWE]]-653: Insufficient Compartmentalization
- [[_content/dictionary#C|CWE]]-656: Reliance on Security Through Obscurity
- [[_content/dictionary#C|CWE]]-657: Violation of Secure Design Principles
- [[_content/dictionary#C|CWE]]-799: Improper Control of Interaction Frequency
- [[_content/dictionary#C|CWE]]-807: Reliance on Untrusted Inputs in a Security Decision
- [[_content/dictionary#C|CWE]]-840: Business Logic Errors
- [[_content/dictionary#C|CWE]]-841: Improper Enforcement of Behavioral Workflow
- [[_content/dictionary#C|CWE]]-927: Use of Implicit Intent for Sensitive Communication
- [[_content/dictionary#C|CWE]]-1021: Improper Restriction of Rendered [[_content/dictionary#U|UI]] Layers or Frames
- [[_content/dictionary#C|CWE]]-1173: Improper Use of Validation Framework 