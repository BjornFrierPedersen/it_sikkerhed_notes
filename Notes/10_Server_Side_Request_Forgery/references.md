# A10:2021 - Server-Side Request Forgery - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Server Side Request Forgery Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
   - Comprehensive guide on preventing [[_content/dictionary#S|SSRF]] attacks
   - Covers defense in depth strategies and implementation details

2. [Input Validation Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Input_Validation_Cheat_Sheet.html)
   - Guidance on validating user input
   - Important for preventing [[_content/dictionary#S|SSRF]] by validating URLs

3. [[[_content/dictionary#R|REST]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/REST_Security_Cheat_Sheet.html)
   - Includes sections relevant to securing REST APIs against [[_content/dictionary#S|SSRF]]
   - Covers [[_content/dictionary#A|API]]-specific security considerations

4. [Docker Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Docker_Security_Cheat_Sheet.html)
   - Includes sections on network security for containerized applications
   - Relevant for preventing [[_content/dictionary#S|SSRF]] in containerized environments

5. [Kubernetes Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)
   - Includes sections on network security for Kubernetes deployments
   - Relevant for preventing [[_content/dictionary#S|SSRF]] in Kubernetes environments

6. [Network Segmentation Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Network_Segmentation_Cheat_Sheet.html)
   - Guidance on network segmentation
   - Important for limiting the impact of [[_content/dictionary#S|SSRF]] attacks

7. [Secure Cloud Architecture Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet.html)
   - Guidance on securing cloud architectures
   - Includes information relevant to preventing [[_content/dictionary#S|SSRF]] in cloud environments

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-918: Server-Side Request Forgery ([[_content/dictionary#S|SSRF]])
- [[_content/dictionary#C|CWE]]-611: Improper Restriction of [[_content/dictionary#X|XML]] External Entity Reference
- [[_content/dictionary#C|CWE]]-20: Improper Input Validation
- [[_content/dictionary#C|CWE]]-400: Uncontrolled Resource Consumption
- [[_content/dictionary#C|CWE]]-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')
- [[_content/dictionary#C|CWE]]-375: Returning a Mutable Object to an Untrusted Caller 