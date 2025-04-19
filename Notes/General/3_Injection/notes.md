# A03:2021 - Injection

## Description
Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. Attackers can send malicious data to trick the interpreter into executing unintended commands or accessing unauthorized data.

This category has moved down from the #1 position in the 2017 [[_content/dictionary#O|OWASP]] Top 10. 94% of applications were tested for some form of injection vulnerability, with a maximum incidence rate of 19%, an average incidence rate of 3.37%, and the 33 [[_content/dictionary#C|CWE]]s mapped into this category have the second most occurrences in applications, with more than 274k occurrences.

## Common Types of Injection
1. **[[_content/dictionary#S|SQL]] Injection**: Insertion of SQL code into input fields that directly query databases.
2. **[[_content/dictionary#N|NoSQL]] Injection**: Similar to SQL injection but targets NoSQL databases.
3. **[[_content/dictionary#O|OS]] Command Injection**: Executing system commands through vulnerable application inputs.
4. **[[_content/dictionary#L|LDAP]] Injection**: Manipulating LDAP queries to access unauthorized directory information.
5. **[[_content/dictionary#X|XPath]] Injection**: Manipulating XPath queries used for [[_content/dictionary#X|XML]] data.
6. **[[_content/dictionary#O|ORM]] Injection**: Attacks against Object-Relational Mapping code.
7. **[[_content/dictionary#X|XSS]]**: Injecting malicious client-side scripts into web pages viewed by other users.
8. **Template Injection**: Injecting malicious template directives in template engines.

## Prevention
1. Use a safe [[_content/dictionary#A|API]] that avoids the use of interpreters entirely or provides a parameterized interface.
2. Use positive server-side input validation with appropriate encoding and escaping.
3. For [[_content/dictionary#S|SQL]] queries, use parameterized queries, prepared statements, or stored procedures.
4. Use [[_content/dictionary#O|OGNL]] expression language injection defenses such as implementing context-aware encoding and input validation.
5. For any residual dynamic queries, escape special characters using the specific escape syntax for that interpreter.
6. Use automated testing tools to detect injection flaws.
7. Secure code reviews and penetration testing can also help identify injection vulnerabilities.

## Impact
Injection can result in data loss, corruption, disclosure to unauthorized parties, loss of accountability, or denial of access. It may sometimes lead to complete host takeover, allowing attackers to completely compromise systems or create backdoors. 