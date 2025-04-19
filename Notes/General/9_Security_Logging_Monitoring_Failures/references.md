# A09:2021 - Security Logging and Monitoring Failures - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Logging Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Logging_Cheat_Sheet.html)
   - Comprehensive guide on implementing secure logging
   - Covers what to log, how to log, and log security

2. [Logging Vocabulary Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Logging_Vocabulary_Cheat_Sheet.html)
   - Guidance on standardized logging terminology
   - Helps ensure consistent and meaningful log entries

3. [Error Handling Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Error_Handling_Cheat_Sheet.html)
   - Guidance on proper error handling
   - Includes information on logging errors securely

4. [Authentication Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Authentication_Cheat_Sheet.html)
   - Includes sections on logging authentication events
   - Covers what authentication events should be logged

5. [Transaction Authorization Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Transaction_Authorization_Cheat_Sheet.html)
   - Guidance on authorizing transactions
   - Includes information on logging high-value transactions

6. [[[_content/dictionary#R|REST]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/REST_Security_Cheat_Sheet.html)
   - Includes sections on logging for REST APIs
   - Covers [[_content/dictionary#A|API]]-specific logging considerations

7. [Docker Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Docker_Security_Cheat_Sheet.html)
   - Includes sections on logging for containerized applications
   - Covers container-specific logging considerations

8. [Kubernetes Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)
   - Includes sections on logging for Kubernetes deployments
   - Covers Kubernetes-specific logging considerations

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-117: Improper Output Neutralization for Logs
- [[_content/dictionary#C|CWE]]-223: Omission of Security-relevant Information
- [[_content/dictionary#C|CWE]]-532: Insertion of Sensitive Information into Log File
- [[_content/dictionary#C|CWE]]-778: Insufficient Logging
- [[_content/dictionary#C|CWE]]-779: Logging of Excessive Data
- [[_content/dictionary#C|CWE]]-1295: Debug Features Enabled in Production
- [[_content/dictionary#C|CWE]]-1154: Improper Neutralization of Variable Names in Dynamic Evaluation 