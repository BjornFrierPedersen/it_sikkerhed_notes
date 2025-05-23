---
title: "LDAP Injection Prevention Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html"
created: "1741872881.976484"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#L|LDAP]] Injection Prevention

## [[[_content/dictionary#L|LDAP]] Injection](https://owasp.org/www-community/attacks/LDAP_Injection) Prevention Cheat Sheet[[[[[[[[[[[[[[[¶](#related-articles)](#allow-list-input-validation)](#enabling-bind-authentication)](#least-privilege)](#additional-defenses)](#safe-net-example)](#defense-option-2-use-frameworks-that-automatically-protect-from-ldap-injection)](#safe-c-sharp-net-tba-example)](#safe-java-escaping-example)](#search-filter-escaping)](#distinguished-name-escaping)](#defense-option-1-escape-all-variables-using-the-right-ldap-encoding-function)](#primary-defenses)](#introduction)](#ldap-injection-prevention-cheat-sheet)
### Introduction¶
The Lightweight Directory Access Protocol (LDAP) allows an application to remotely perform operations such as searching and modifying records in
directories. [LDAP injection](https://owasp.org/www-community/attacks/LDAP_Injection) results from inadequate input sanitization and validation and allows malicious users to glean restricted information using the
directory service. For general information about LDAP please visit [lightweight directory access protocol (LDAP)](https://www.redhat.com/en/topics/security/what-is-ldap-authentication).
LDAP Injection is an attack used to exploit web based applications that construct LDAP statements based on user input. When an application fails to properly sanitize user input, it's possible to modify LDAP statements through techniques similar to [[[_content/dictionary#S|SQL]] Injection](https://owasp.org/www-community/attacks/SQL_Injection).
This cheatsheet is focused on providing clear, simple, actionable guidance for preventing LDAP Injection flaws in your applications. LDAP injection attacks are common due to two factors:

1. The lack of safer, parameterized [[_content/dictionary#L|LDAP]] query interfaces
2. The widespread use of LDAP to authenticate users to systems.

[[_content/dictionary#L|LDAP]] injection attacks could result in the granting of permissions to unauthorized queries, and content modification inside the LDAP tree.
Primary Defenses:

- Escape all variables using the right [[_content/dictionary#L|LDAP]] encoding function
- Use a framework that escapes automatically.

Additional Defenses:

- - Least Privilege
- - Allow-List Input Validation

### Primary Defenses¶
#### Defense Option 1: Escape all variables using the right [[_content/dictionary#L|LDAP]] encoding function¶
##### Distinguished Name Escaping¶
The main way LDAP stores names is based on [[_content/dictionary#D|DN]] (distinguished name). You can think of this like a unique identifier. These are sometimes used to access resources, like a username.
A DN might look like this
cn=Richard Feynman, ou=Physics Department, dc=Caltech, dc=edu
or
uid=inewton, ou=Mathematics Department, dc=Cambridge, dc=com
An allowlist can be used to restrict input to a list of valid characters. Characters and character sequences that must be excluded from allowlists — including
Java Naming and Directory Interface ([[_content/dictionary#J|JNDI]]) metacharacters and LDAP special characters — are listed in the following list.
The [exhaustive list](https://ldapwiki.com/wiki/Wiki.jsp?page=DN%20Escape%20Values) is the following: \ # + < > , ; " = and leading or trailing spaces.
Some "special" characters that are allowed in Distinguished Names and do not need to be escaped include:
* ( ) . & - _ [ ] ` ~ | @ $ % ^ ? : { } ! '

##### Search Filter Escaping¶
Each DN points to exactly 1 entry, which can be thought of sort of like a row in a RDBMS. For each entry, there will be 1 or more attributes which are analogous to RDBMS columns. If you are interested in searching through LDAP for users with certain attributes, you may do so with search filters.
In a search filter, you can use standard boolean logic to get a list of users matching an arbitrary constraint. Search filters are written in Polish notation AKA prefix notation.
Example:
(&(ou=Physics)(|
(manager=cn=Freeman Dyson,ou=Physics,dc=Caltech,dc=edu)
(manager=cn=Albert Einstein,ou=Physics,dc=Princeton,dc=edu)
))

When building [[_content/dictionary#L|LDAP]] queries in application code, you [[_content/dictionary#M|MUST]] escape any untrusted data that is added to any LDAP query. There are two forms of LDAP escaping. Encoding for LDAP Search and Encoding for LDAP [[_content/dictionary#D|DN]] (distinguished name). The proper escaping depends on whether you are sanitizing input for a search filter, or you are using a DN as a username-like credential for accessing some resource.
Some "special" characters that are allowed in search filters and must be escaped include:
* ( ) \ [[_content/dictionary#N|NUL]]

For more information on search filter escaping visit [[RFC4515](https://tools.ietf.org/search/rfc4515)](https://datatracker.ietf.org/doc/html/rfc4515#section-3).
##### Safe Java Escaping Example¶
The following solution uses an allowlist to sanitize user input so that the filter string contains only valid characters. In this code, userSN may contain
only letters and spaces, whereas a password may contain only alphanumeric characters:
// String userSN = "Sherlock Holmes"; // Valid
// String userPassword = "secret2"; // Valid
// ... beginning of LDAPInjection.searchRecord()...
sc.setSearchScope([[_content/dictionary#S|SearchControls]].SUBTREE_SCOPE);
String base = "dc=example,dc=com";

if (!userSN.matches("[\\w\\s]*") || !userPassword.matches("[\\w]*")) {
 throw new [[_content/dictionary#I|IllegalArgumentException]]("Invalid input");
}

String filter = "(&(sn = " + userSN + ")(userPassword=" + userPassword + "))";
// ... remainder of LDAPInjection.searchRecord()... 

When a database field such as a password must include special characters, it is critical to ensure that the authentic data is stored in sanitized form in the
database and also that any user input is normalized before the validation or comparison takes place. Using characters that have special meanings in [[_content/dictionary#J|JNDI]]
and LDAP in the absence of a comprehensive normalization and allowlisting-based routine is discouraged. Special characters must be transformed to
sanitized, safe values before they are added to the allowlist expression against which input will be validated. Likewise, normalization of user input should
occur before the validation step (source: [Prevent LDAP injection](https://wiki.sei.cmu.edu/confluence/spaces/flyingpdf/pdfpageexport.action?pageId=88487534)).
For further information visit [[[_content/dictionary#O|OWASP]] [[_content/dictionary#E|ESAPI]] Java Encoder Project which includes encodeForLDAP(String) and encodeForDN(String)](https://owasp.org/www-project-java-encoder/).
##### Safe C Sharp .[[_content/dictionary#N|NET]] [[_content/dictionary#T|TBA]] Example¶
[.NET AntiXSS](https://blogs.msdn.microsoft.com/securitytools/2010/09/30/antixss-4-0-released/) (now the Encoder class) has LDAP encoding functions including Encoder.[[_content/dictionary#L|LdapFilterEncode]](string), Encoder.[[_content/dictionary#L|LdapDistinguishedNameEncode]](string) and Encoder.LdapDistinguishedNameEncode(string, bool, bool).
Encoder.LdapFilterEncode encodes input according to RFC4515 where unsafe values are converted to \[[_content/dictionary#X|XX]] where XX is the representation of the unsafe character.
Encoder.LdapDistinguishedNameEncode encodes input according to [RFC2253](https://tools.ietf.org/html/rfc2253) where unsafe characters are converted to #XX where XX is the representation of the unsafe character and the comma, plus, quote, slash, less than and great than signs are escaped using slash notation (\X). In addition to this a space or octothorpe (#) at the beginning of the input string is \ escaped as is a space at the end of a string.
LdapDistinguishedNameEncode(string, bool, bool) is also provided so you may turn off the initial or final character escaping rules, for example if you are concatenating the escaped distinguished name fragment into the midst of a complete distinguished name.
#### Defense Option 2: Use Frameworks that Automatically Protect from [[_content/dictionary#L|LDAP]] Injection¶
##### Safe .[[_content/dictionary#N|NET]] Example¶
We recommend using [[[_content/dictionary#L|LINQ]] to LDAP](https://www.nuget.org/packages/[[_content/dictionary#L|LinqToLdap]]/) (for .NET Framework 4.5 or lower [until it has been updated](https://github.com/madhatter22/LinqToLdap/issues/31)) in [[_content/dictionary#D|DotNet]]. It provides automatic LDAP encoding when building LDAP queries.
Contact the [Readme file](https://github.com/madhatter22/LinqToLdap/blob/master/[[_content/dictionary#R|README]].md) in the project repository.
### Additional Defenses¶
Beyond adopting one of the two primary defenses, we also recommend adopting all of these additional defenses in order to provide defense in depth. These additional defenses are:

Least Privilege
Allow-List Input Validation

#### Least Privilege¶
To minimize the potential damage of a successful [[_content/dictionary#L|LDAP]] injection attack, you should minimize the privileges assigned to the LDAP binding account in your environment.
#### Enabling Bind Authentication¶
If LDAP protocol is configured with bind Authentication, attackers would not be able to perform LDAP injection attacks because of verification
and authorization checks that are performed against valid credentials passed by the user.
An attacker can still bypass bind authentication through an anonymous connection or by exploiting the use of unauthenticated bind: Anonymous Bind (LDAP) and Unauthenticated Bind (LDAP).
#### Allow-List Input Validation¶
Input validation can be used to detect unauthorized input before it is passed to the LDAP query. For more information please see the [[Input_Validation_Cheat_Sheet|Input Validation Cheat Sheet]].
### Related Articles¶

- [[_content/dictionary#O|OWASP]] article on [[_content/dictionary#L|LDAP]] Injection Vulnerabilities.
[OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) article on how to [Test for LDAP Injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/06-Testing_for_LDAP_Injection.html) Vulnerabilities.