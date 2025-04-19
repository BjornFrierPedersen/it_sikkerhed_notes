# A02:2021 - Cryptographic Failures

## Concept

Cryptographic Failures refers to weaknesses in cryptographic implementations that can lead to exposure of sensitive data. This category was previously known as "Sensitive Data Exposure" in the 2017 [[_content/dictionary#O|OWASP]] Top 10, but has been renamed to focus on the root cause (failures in cryptography) rather than the symptom (data exposure).

Cryptographic failures can include issues like using weak encryption algorithms, improper key management, not encrypting sensitive data in transit or at rest, and other cryptographic implementation flaws that can lead to data breaches.

## Key Points

1. **Prevalence**: Moved up from the third position in 2017 to become the second most serious web application security risk in 2021.

2. **Scope Change**: The category has been renamed from "Sensitive Data Exposure" to "Cryptographic Failures" to focus on the root cause rather than the symptom.

3. **Common Vulnerabilities**:
   - Transmitting sensitive data in clear text (e.g., [[_content/dictionary#H|HTTP]] instead of [[_content/dictionary#H|HTTPS]])
   - Using weak or outdated cryptographic algorithms (e.g., [[_content/dictionary#M|MD5]], [[_content/dictionary#S|SHA]]1)
   - Using default, weak, or hardcoded cryptographic keys
   - Not enforcing encryption through security headers or directives
   - Not validating server certificates
   - Using deprecated hash functions or improper hash usage
   - Using cryptographic initialization vectors ([[_content/dictionary#I|IV]]s) incorrectly
   - Using passwords as cryptographic keys without proper key derivation functions
   - Using insecure random number generators
   - Using outdated cryptographic protocols (e.g., [[_content/dictionary#S|SSL]], early [[_content/dictionary#T|TLS]])

4. **Prevention**:
   - Classify data processed, stored, or transmitted by an application
   - Identify which data is sensitive according to privacy laws, regulatory requirements, or business needs
   - Apply controls as per the classification
   - Don't store sensitive data unnecessarily; discard it as soon as possible
   - Ensure up-to-date and strong standard algorithms, protocols, and keys are in place
   - Encrypt all sensitive data at rest
   - Encrypt all data in transit with secure protocols such as [[_content/dictionary#T|TLS]] with forward secrecy ciphers
   - Disable caching for responses that contain sensitive data
   - Store passwords using strong adaptive and salted hashing functions with a work factor
   - Verify independently the effectiveness of configuration and settings

5. **Impact**: Exposure of sensitive data can lead to identity theft, financial fraud, reputational damage, regulatory fines, and other serious consequences. 