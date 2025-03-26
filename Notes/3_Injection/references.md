# A03:2021 - Injection - References

## Relevant [[_content/dictionary#O|OWASP]] Cheatsheets

1. [Injection Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
   - General guidance on preventing injection attacks
   - Covers principles applicable to all types of injection

2. [[[_content/dictionary#S|SQL]] Injection Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
   - Comprehensive guide on preventing SQL injection
   - Covers parameterized queries, stored procedures, and input validation

3. [Query Parameterization Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Query_Parameterization_Cheat_Sheet.html)
   - Detailed guidance on parameterizing database queries
   - Provides examples in various programming languages

4. [[[_content/dictionary#O|OS]] Command Injection Defense Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
   - Guidance on preventing OS command injection
   - Covers safe APIs and input validation techniques

5. [[[_content/dictionary#L|LDAP]] Injection Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)
   - Guidance on preventing LDAP injection
   - Covers input validation and safe LDAP APIs

6. [Cross Site Scripting Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
   - Comprehensive guide on preventing [[_content/dictionary#X|XSS]] attacks
   - Covers output encoding, input validation, and [[_content/dictionary#C|CSP]]

7. [[[_content/dictionary#D|DOM]] based [[_content/dictionary#X|XSS]] Prevention Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
   - Specific guidance on preventing DOM-based XSS
   - Covers [[_content/dictionary#J|JavaScript]] security and safe DOM manipulation

8. [[[_content/dictionary#X|XSS]] Filter Evasion Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
   - Catalog of XSS attack vectors
   - Helps understand how attackers bypass XSS filters

9. [Injection Prevention in Java Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html)
   - Java-specific guidance on preventing injection attacks
   - Covers [[_content/dictionary#J|JDBC]], Hibernate, and other Java frameworks

10. [[[_content/dictionary#X|XML]] Security Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/XML_Security_Cheat_Sheet.html)
    - Guidance on preventing XML injection attacks
    - Covers [[_content/dictionary#X|XXE]] and [[_content/dictionary#X|XPath]] injection

11. [Input Validation Cheat Sheet](../../[[_content/dictionary#O|OWASP]]%20Cheatsheet/cheatsheets/Input_Validation_Cheat_Sheet.html)
    - General guidance on validating user input
    - Important foundation for preventing injection attacks

## Key CWEs (Common Weakness Enumeration)

- [[_content/dictionary#C|CWE]]-20: Improper Input Validation
- [[_content/dictionary#C|CWE]]-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')
- [[_content/dictionary#C|CWE]]-75: Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)
- [[_content/dictionary#C|CWE]]-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')
- [[_content/dictionary#C|CWE]]-78: Improper Neutralization of Special Elements used in an [[_content/dictionary#O|OS]] Command ('OS Command Injection')
- [[_content/dictionary#C|CWE]]-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- [[_content/dictionary#C|CWE]]-80: Improper Neutralization of Script-Related [[_content/dictionary#H|HTML]] Tags in a Web Page (Basic [[_content/dictionary#X|XSS]])
- [[_content/dictionary#C|CWE]]-83: Improper Neutralization of Script in Attributes in a Web Page
- [[_content/dictionary#C|CWE]]-87: Improper Neutralization of Alternate [[_content/dictionary#X|XSS]] Syntax
- [[_content/dictionary#C|CWE]]-88: Improper Neutralization of Argument Delimiters in a Command ('Argument Injection')
- [[_content/dictionary#C|CWE]]-89: Improper Neutralization of Special Elements used in an [[_content/dictionary#S|SQL]] Command ('SQL Injection')
- [[_content/dictionary#C|CWE]]-90: Improper Neutralization of Special Elements used in an [[_content/dictionary#L|LDAP]] Query ('LDAP Injection')
- [[_content/dictionary#C|CWE]]-91: [[_content/dictionary#X|XML]] Injection (aka Blind [[_content/dictionary#X|XPath]] Injection)
- [[_content/dictionary#C|CWE]]-93: Improper Neutralization of [[_content/dictionary#C|CRLF]] Sequences ('CRLF Injection')
- [[_content/dictionary#C|CWE]]-94: Improper Control of Generation of Code ('Code Injection')
- [[_content/dictionary#C|CWE]]-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')
- [[_content/dictionary#C|CWE]]-96: Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection')
- [[_content/dictionary#C|CWE]]-97: Improper Neutralization of Server-Side Includes ([[_content/dictionary#S|SSI]]) Within a Web Page
- [[_content/dictionary#C|CWE]]-98: Improper Control of Filename for Include/Require Statement in [[_content/dictionary#P|PHP]] Program ('PHP Remote File Inclusion')
- [[_content/dictionary#C|CWE]]-99: Improper Control of Resource Identifiers ('Resource Injection')
- [[_content/dictionary#C|CWE]]-100: Deprecated: Was catch-all for input validation issues
- [[_content/dictionary#C|CWE]]-113: Improper Neutralization of [[_content/dictionary#C|CRLF]] Sequences in [[_content/dictionary#H|HTTP]] Headers ('HTTP Response Splitting')
- [[_content/dictionary#C|CWE]]-116: Improper Encoding or Escaping of Output
- [[_content/dictionary#C|CWE]]-138: Improper Neutralization of Special Elements
- [[_content/dictionary#C|CWE]]-184: Incomplete List of Disallowed Inputs
- [[_content/dictionary#C|CWE]]-470: Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')
- [[_content/dictionary#C|CWE]]-471: Modification of Assumed-Immutable Data ([[_content/dictionary#M|MAID]])
- [[_content/dictionary#C|CWE]]-564: [[_content/dictionary#S|SQL]] Injection: Hibernate
- [[_content/dictionary#C|CWE]]-610: Externally Controlled Reference to a Resource in Another Sphere
- [[_content/dictionary#C|CWE]]-643: Improper Neutralization of Data within [[_content/dictionary#X|XPath]] Expressions ('XPath Injection')
- [[_content/dictionary#C|CWE]]-644: Improper Neutralization of [[_content/dictionary#H|HTTP]] Headers for Scripting Syntax
- [[_content/dictionary#C|CWE]]-652: Improper Neutralization of Data within XQuery Expressions ('XQuery Injection')
- [[_content/dictionary#C|CWE]]-917: Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection') 