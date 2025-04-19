# A07:2021 - Identification and Authentication Failures

## Description
This category, previously known as "Broken Authentication," shifted from the second position in 2017 to seventh in 2021. It includes [[_content/dictionary#C|CWE]]s related to identification failures and captures the new categories of authentication weaknesses. This category is still an integral part of the Top 10, but the increased availability of standardized frameworks seems to be helping.

## Common Vulnerabilities
1. Permitting automated attacks such as credential stuffing, where attackers use lists of known passwords to gain unauthorized access to accounts.
2. Allowing brute force or other automated attacks.
3. Permitting weak passwords like "Password1" or "admin/admin" despite guidance requiring more complex password rules.
4. Weak or ineffective credential recovery and forgot-password processes, such as "knowledge-based answers," which cannot be made safe.
5. Using plain text, encrypted, or weakly hashed passwords in storage.
6. Missing or ineffective multi-factor authentication ([[_content/dictionary#M|MFA]]).
7. Exposing Session IDs in the [[_content/dictionary#U|URL]].
8. Failing to properly invalidate Session IDs, particularly after successful logout, timeout, or session inactivity.

## Prevention
1. Implement multi-factor authentication ([[_content/dictionary#M|MFA]]) to prevent automated credential stuffing, brute force, and stolen credential reuse attacks.
2. Do not ship or deploy with default credentials, especially for admin users.
3. Enforce strong password checks using recent [[_content/dictionary#N|NIST]] 800-63b guidelines.
4. Ensure registration, credential recovery, and [[_content/dictionary#A|API]] pathways are hardened against account enumeration attacks.
5. Limit or increasingly delay failed login attempts, and log all failures with alert mechanisms when credential stuffing is detected.
6. Use a secure server-side session manager that generates a new random session ID with high entropy after login.
7. Session IDs should not be included in the [[_content/dictionary#U|URL]], be securely stored, and invalidated after logout, idle, and absolute timeouts.

## Impact
The impact can vary widely, from unauthorized access to user accounts, complete system compromise, or identity theft. Depending on the application's purpose, this could result in money laundering, social security fraud, or theft of sensitive private information. 