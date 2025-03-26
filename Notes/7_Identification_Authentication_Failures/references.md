# A07:2021 - Identification and Authentication Failures - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Authentication Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authentication_Cheat_Sheet.html)
   - Comprehensive guide on implementing secure authentication
   - Covers authentication mechanisms, password policies, and session management

2. [Credential Stuffing Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)
   - Guidance on preventing credential stuffing attacks
   - Covers detection and mitigation strategies

3. [Forgot Password Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Forgot_Password_Cheat_Sheet.html)
   - Guidance on implementing secure password recovery mechanisms
   - Covers secure workflows and anti-enumeration techniques

4. [Session Management Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Session_Management_Cheat_Sheet.html)
   - Guidance on secure session management
   - Covers session creation, storage, and termination

5. [Password Storage Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Password_Storage_Cheat_Sheet.html)
   - Guidance on securely storing passwords
   - Covers hashing algorithms, salting, and work factors

6. [Multifactor Authentication Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)
   - Guidance on implementing multi-factor authentication
   - Covers different types of factors and implementation considerations

7. [[[_content/dictionary#J|JSON]] Web Token for Java Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
   - Guidance on securely implementing [[_content/dictionary#J|JWT]] tokens
   - Covers token creation, validation, and security considerations

8. [[[_content/dictionary#S|SAML]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/SAML_Security_Cheat_Sheet.html)
   - Guidance on securing [[_content/dictionary#S|SAML]] implementations
   - Covers [[_content/dictionary#S|SAML]]-based authentication and [[_content/dictionary#S|SSO]]

9. [Choosing and Using Security Questions Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Choosing_and_Using_Security_Questions_Cheat_Sheet.html)
   - Guidance on implementing security questions
   - Covers question selection and implementation considerations

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-255: Credentials Management Errors
- [[_content/dictionary#C|CWE]]-259: Use of Hard-coded Password
- [[_content/dictionary#C|CWE]]-287: Improper Authentication
- [[_content/dictionary#C|CWE]]-288: Authentication Bypass Using an Alternate Path or Channel
- [[_content/dictionary#C|CWE]]-290: Authentication Bypass by Spoofing
- [[_content/dictionary#C|CWE]]-294: Authentication Bypass by Capture-replay
- [[_content/dictionary#C|CWE]]-295: Improper Certificate Validation
- [[_content/dictionary#C|CWE]]-297: Improper Validation of Certificate with Host Mismatch
- [[_content/dictionary#C|CWE]]-300: Channel Accessible by Non-Endpoint
- [[_content/dictionary#C|CWE]]-302: Authentication Bypass by Assumed-Immutable Data
- [[_content/dictionary#C|CWE]]-304: Missing Critical Step in Authentication
- [[_content/dictionary#C|CWE]]-306: Missing Authentication for Critical Function
- [[_content/dictionary#C|CWE]]-307: Improper Restriction of Excessive Authentication Attempts
- [[_content/dictionary#C|CWE]]-346: Origin Validation Error
- [[_content/dictionary#C|CWE]]-384: Session Fixation
- [[_content/dictionary#C|CWE]]-521: Weak Password Requirements
- [[_content/dictionary#C|CWE]]-613: Insufficient Session Expiration
- [[_content/dictionary#C|CWE]]-620: Unverified Password Change
- [[_content/dictionary#C|CWE]]-640: Weak Password Recovery Mechanism for Forgotten Password
- [[_content/dictionary#C|CWE]]-798: Use of Hard-coded Credentials
- [[_content/dictionary#C|CWE]]-940: Improper Verification of Source of a Communication Channel
- [[_content/dictionary#C|CWE]]-1216: Lockout Mechanism Errors 