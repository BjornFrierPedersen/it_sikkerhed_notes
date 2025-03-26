# A05:2021 - Security Misconfiguration - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [[[_content/dictionary#X|XML]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/XML_Security_Cheat_Sheet.html)
   - Guidance on securing XML processing
   - Covers [[_content/dictionary#X|XXE]] prevention and secure XML configuration

2. [[[_content/dictionary#X|XML]] External Entity Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
   - Specific guidance on preventing [[_content/dictionary#X|XXE]] attacks
   - Covers secure XML parser configuration

3. [Docker Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Docker_Security_Cheat_Sheet.html)
   - Guidance on securing Docker containers
   - Covers container configuration and hardening

4. [Kubernetes Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)
   - Guidance on securing Kubernetes deployments
   - Covers cluster configuration and hardening

5. [[[_content/dictionary#P|PHP]] Configuration Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/PHP_Configuration_Cheat_Sheet.html)
   - Guidance on secure PHP configuration
   - Covers PHP settings and hardening

6. [Error Handling Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Error_Handling_Cheat_Sheet.html)
   - Guidance on proper error handling
   - Helps prevent information disclosure through error messages

7. [[[_content/dictionary#H|HTTP]] Headers Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
   - Guidance on configuring secure HTTP headers
   - Covers security headers and their proper values

8. [Content Security Policy Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
   - Guidance on implementing Content Security Policy
   - Helps secure web applications against various attacks

9. [Network Segmentation Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Network_Segmentation_Cheat_Sheet.html)
   - Guidance on network segmentation
   - Helps implement effective separation and security controls

10. [Secure Cloud Architecture Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)
    - Guidance on secure cloud configuration
    - Covers cloud service security settings

11. [NodeJS Docker Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/NodeJS_Docker_Cheat_Sheet.html)
    - Guidance on securing NodeJS applications in Docker
    - Covers configuration and hardening

12. [Infrastructure as Code Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)
    - Guidance on securing infrastructure as code
    - Helps automate secure configuration

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-2: 7PK - Environment
- [[_content/dictionary#C|CWE]]-11: [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Misconfiguration: Creating Debug Binary
- [[_content/dictionary#C|CWE]]-13: [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Misconfiguration: Password in Configuration File
- [[_content/dictionary#C|CWE]]-15: External Control of System or Configuration Setting
- [[_content/dictionary#C|CWE]]-16: Configuration
- [[_content/dictionary#C|CWE]]-260: Password in Configuration File
- [[_content/dictionary#C|CWE]]-315: Cleartext Storage of Sensitive Information in a Cookie
- [[_content/dictionary#C|CWE]]-520: .[[_content/dictionary#N|NET]] Misconfiguration: Use of Impersonation
- [[_content/dictionary#C|CWE]]-526: Exposure of Sensitive Information Through Environmental Variables
- [[_content/dictionary#C|CWE]]-537: Java Runtime Error Message Containing Sensitive Information
- [[_content/dictionary#C|CWE]]-541: Inclusion of Sensitive Information in an Include File
- [[_content/dictionary#C|CWE]]-547: Use of Hard-coded, Security-relevant Constants
- [[_content/dictionary#C|CWE]]-611: Improper Restriction of [[_content/dictionary#X|XML]] External Entity Reference
- [[_content/dictionary#C|CWE]]-614: Sensitive Cookie in [[_content/dictionary#H|HTTPS]] Session Without 'Secure' Attribute
- [[_content/dictionary#C|CWE]]-756: Missing Custom Error Page
- [[_content/dictionary#C|CWE]]-776: Improper Restriction of Recursive Entity References in DTDs ('[[_content/dictionary#X|XML]] Entity Expansion')
- [[_content/dictionary#C|CWE]]-942: Permissive Cross-domain Policy with Untrusted Domains
- [[_content/dictionary#C|CWE]]-1004: Sensitive Cookie Without '[[_content/dictionary#H|HttpOnly]]' Flag
- [[_content/dictionary#C|CWE]]-1032: [[_content/dictionary#O|OWASP]] Top Ten 2017 Category A6 - Security Misconfiguration
- [[_content/dictionary#C|CWE]]-1174: [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Misconfiguration: Improper Model Validation 