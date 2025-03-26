# A08:2021 - Software and Data Integrity Failures - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Deserialization Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Deserialization_Cheat_Sheet.html)
   - Guidance on preventing insecure deserialization
   - Covers safe deserialization practices and mitigation strategies

2. [Software Supply Chain Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)
   - Guidance on securing the software supply chain
   - Covers dependency management and third-party component security

3. [[[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
   - Guidance on securing [[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] pipelines
   - Covers pipeline security and integrity verification

4. [[[_content/dictionary#N|NPM]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/NPM_Security_Cheat_Sheet.html)
   - Guidance on securing Node.js applications using NPM
   - Covers dependency management and security best practices

5. [Docker Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Docker_Security_Cheat_Sheet.html)
   - Guidance on securing Docker containers
   - Covers container integrity and security

6. [Kubernetes Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)
   - Guidance on securing Kubernetes deployments
   - Covers deployment integrity and security

7. [Third Party Javascript Management Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
   - Guidance on managing third-party [[_content/dictionary#J|JavaScript]] libraries
   - Covers security considerations for external dependencies

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-345: Insufficient Verification of Data Authenticity
- [[_content/dictionary#C|CWE]]-353: Missing Support for Integrity Check
- [[_content/dictionary#C|CWE]]-426: Untrusted Search Path
- [[_content/dictionary#C|CWE]]-494: Download of Code Without Integrity Check
- [[_content/dictionary#C|CWE]]-502: Deserialization of Untrusted Data
- [[_content/dictionary#C|CWE]]-565: Reliance on Cookies without Validation and Integrity Checking
- [[_content/dictionary#C|CWE]]-784: Reliance on Cookies without Validation and Integrity Checking in a Security Decision
- [[_content/dictionary#C|CWE]]-829: Inclusion of Functionality from Untrusted Control Sphere
- [[_content/dictionary#C|CWE]]-830: Inclusion of Web Functionality from an Untrusted Source
- [[_content/dictionary#C|CWE]]-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes 