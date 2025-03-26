# A01:2021 - Broken Access Control - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Authorization Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authorization_Cheat_Sheet.html)
   - Comprehensive guide on implementing proper authorization mechanisms
   - Covers principles like "deny by default" and "prefer attribute-based access control"
   - Provides guidance on handling authorization failures safely

2. [Access Control Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Access_Control_Cheat_Sheet.html)
   - Note: This has been deprecated in favor of the Authorization Cheat Sheet

3. [Insecure Direct Object Reference Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)
   - Addresses a common broken access control vulnerability
   - Provides guidance on preventing unauthorized access to resources via direct references

4. [Cross-Site Request Forgery Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
   - Helps prevent attackers from tricking users into making unintended state-changing requests
   - Important for protecting against certain types of access control bypasses

5. [[[_content/dictionary#J|JSON]] Web Token for Java Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
   - Guidance on securely implementing [[_content/dictionary#J|JWT]] tokens
   - Helps prevent token tampering that could lead to access control bypasses

6. [[[_content/dictionary#R|REST]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/REST_Security_Cheat_Sheet.html)
   - Contains sections on access control for REST APIs
   - Addresses common [[_content/dictionary#A|API]] security issues related to access control

7. [Authorization Testing Automation Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html)
   - Provides guidance on testing access control mechanisms
   - Helps identify broken access control vulnerabilities

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
- [[_content/dictionary#C|CWE]]-23: Relative Path Traversal
- [[_content/dictionary#C|CWE]]-35: Path Traversal: '.../...//'
- [[_content/dictionary#C|CWE]]-59: Improper Link Resolution Before File Access ('Link Following')
- [[_content/dictionary#C|CWE]]-200: Exposure of Sensitive Information to an Unauthorized Actor
- [[_content/dictionary#C|CWE]]-201: Exposure of Sensitive Information Through Sent Data
- [[_content/dictionary#C|CWE]]-219: Storage of File with Sensitive Data Under Web Root
- [[_content/dictionary#C|CWE]]-264: Permissions, Privileges, and Access Controls
- [[_content/dictionary#C|CWE]]-275: Permission Issues
- [[_content/dictionary#C|CWE]]-276: Incorrect Default Permissions
- [[_content/dictionary#C|CWE]]-284: Improper Access Control
- [[_content/dictionary#C|CWE]]-285: Improper Authorization
- [[_content/dictionary#C|CWE]]-352: Cross-Site Request Forgery
- [[_content/dictionary#C|CWE]]-359: Exposure of Private Personal Information to an Unauthorized Actor
- [[_content/dictionary#C|CWE]]-377: Insecure Temporary File
- [[_content/dictionary#C|CWE]]-402: Transmission of Private Resources into a New Sphere
- [[_content/dictionary#C|CWE]]-425: Direct Request ('Forced Browsing')
- [[_content/dictionary#C|CWE]]-441: Unintended Proxy or Intermediary ('Confused Deputy')
- [[_content/dictionary#C|CWE]]-497: Exposure of Sensitive System Information to an Unauthorized Control Sphere
- [[_content/dictionary#C|CWE]]-538: Insertion of Sensitive Information into Externally-Accessible File or Directory
- [[_content/dictionary#C|CWE]]-540: Inclusion of Sensitive Information in Source Code
- [[_content/dictionary#C|CWE]]-548: Exposure of Information Through Directory Listing
- [[_content/dictionary#C|CWE]]-552: Files or Directories Accessible to External Parties
- [[_content/dictionary#C|CWE]]-566: Authorization Bypass Through User-Controlled [[_content/dictionary#S|SQL]] Primary Key
- [[_content/dictionary#C|CWE]]-601: [[_content/dictionary#U|URL]] Redirection to Untrusted Site ('Open Redirect')
- [[_content/dictionary#C|CWE]]-639: Authorization Bypass Through User-Controlled Key
- [[_content/dictionary#C|CWE]]-651: Exposure of [[_content/dictionary#W|WSDL]] File Containing Sensitive Information
- [[_content/dictionary#C|CWE]]-668: Exposure of Resource to Wrong Sphere
- [[_content/dictionary#C|CWE]]-706: Use of Incorrectly-Resolved Name or Reference
- [[_content/dictionary#C|CWE]]-862: Missing Authorization
- [[_content/dictionary#C|CWE]]-863: Incorrect Authorization
- [[_content/dictionary#C|CWE]]-913: Improper Control of Dynamically-Managed Code Resources
- [[_content/dictionary#C|CWE]]-922: Insecure Storage of Sensitive Information
- [[_content/dictionary#C|CWE]]-1275: Sensitive Cookie with Improper [[_content/dictionary#S|SameSite]] Attribute 