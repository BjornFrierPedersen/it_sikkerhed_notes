# A02:2021 - Cryptographic Failures - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Cryptographic Storage Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
   - Provides guidance on properly implementing cryptographic storage
   - Covers algorithm selection, key management, and implementation details

2. [Key Management Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Key_Management_Cheat_Sheet.html)
   - Focuses on the management of cryptographic keys
   - Covers key generation, storage, rotation, and destruction

3. [Password Storage Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Password_Storage_Cheat_Sheet.html)
   - Guidance on securely storing passwords
   - Covers hashing algorithms, salting, and work factors

4. [Transport Layer Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
   - Provides guidance on implementing [[_content/dictionary#T|TLS]] for secure data transmission
   - Covers protocol versions, cipher suites, and certificate management

5. [[[_content/dictionary#T|TLS]] Cipher String Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html)
   - Detailed information on TLS cipher strings
   - Helps configure secure TLS implementations

6. [[[_content/dictionary#H|HTTP]] Strict Transport Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
   - Guidance on implementing [[_content/dictionary#H|HSTS]] to enforce secure connections
   - Helps prevent protocol downgrade attacks and cookie hijacking

7. [Pinning Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Pinning_Cheat_Sheet.html)
   - Information on certificate and public key pinning
   - Helps prevent man-in-the-middle attacks

8. [[[_content/dictionary#X|XML]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/XML_Security_Cheat_Sheet.html)
   - Covers secure handling of XML data
   - Includes cryptographic considerations for XML processing

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-261: Weak Encoding for Password
- [[_content/dictionary#C|CWE]]-296: Improper Following of a Certificate's Chain of Trust
- [[_content/dictionary#C|CWE]]-310: Cryptographic Issues
- [[_content/dictionary#C|CWE]]-319: Cleartext Transmission of Sensitive Information
- [[_content/dictionary#C|CWE]]-321: Use of Hard-coded Cryptographic Key
- [[_content/dictionary#C|CWE]]-322: Key Exchange without Entity Authentication
- [[_content/dictionary#C|CWE]]-323: Reusing a Nonce, Key Pair in Encryption
- [[_content/dictionary#C|CWE]]-324: Use of a Key Past its Expiration Date
- [[_content/dictionary#C|CWE]]-325: Missing Required Cryptographic Step
- [[_content/dictionary#C|CWE]]-326: Inadequate Encryption Strength
- [[_content/dictionary#C|CWE]]-327: Use of a Broken or Risky Cryptographic Algorithm
- [[_content/dictionary#C|CWE]]-328: Reversible One-Way Hash
- [[_content/dictionary#C|CWE]]-329: Not Using a Random [[_content/dictionary#I|IV]] with [[_content/dictionary#C|CBC]] Mode
- [[_content/dictionary#C|CWE]]-330: Use of Insufficiently Random Values
- [[_content/dictionary#C|CWE]]-331: Insufficient Entropy
- [[_content/dictionary#C|CWE]]-335: Incorrect Usage of Seeds in Pseudo-Random Number Generator
- [[_content/dictionary#C|CWE]]-336: Same Seed in Pseudo-Random Number Generator
- [[_content/dictionary#C|CWE]]-337: Predictable Seed in Pseudo-Random Number Generator
- [[_content/dictionary#C|CWE]]-338: Use of Cryptographically Weak Pseudo-Random Number Generator
- [[_content/dictionary#C|CWE]]-340: Generation of Predictable Numbers or Identifiers
- [[_content/dictionary#C|CWE]]-347: Improper Verification of Cryptographic Signature
- [[_content/dictionary#C|CWE]]-523: Unprotected Transport of Credentials
- [[_content/dictionary#C|CWE]]-720: [[_content/dictionary#O|OWASP]] Top Ten 2007 Category A9 - Insecure Communications
- [[_content/dictionary#C|CWE]]-757: Selection of Less-Secure Algorithm During Negotiation
- [[_content/dictionary#C|CWE]]-759: Use of a One-Way Hash without a Salt
- [[_content/dictionary#C|CWE]]-760: Use of a One-Way Hash with a Predictable Salt
- [[_content/dictionary#C|CWE]]-780: Use of [[_content/dictionary#R|RSA]] Algorithm without [[_content/dictionary#O|OAEP]]
- [[_content/dictionary#C|CWE]]-818: Insufficient Transport Layer Protection
- [[_content/dictionary#C|CWE]]-916: Use of Password Hash With Insufficient Computational Effort 