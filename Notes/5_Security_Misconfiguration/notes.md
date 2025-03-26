# A05:2021 - Security Misconfiguration

## Description
Security Misconfiguration occurs when security settings are defined, implemented, and maintained improperly. This can happen at any level of the application stack, including network services, platform, web server, application server, database, frameworks, custom code, and pre-installed virtual machines, containers, or storage.

This category moved up from #6 in the 2017 edition and now includes the former category for [[_content/dictionary#X|XML]] External Entities ([[_content/dictionary#X|XXE]]). With the increasing shift toward highly configurable software, it's not surprising to see this category move up. 90% of applications were tested for some form of misconfiguration, with an average incidence rate of 4.5%, and over 208k occurrences of [[_content/dictionary#C|CWE]]s mapped to this risk category.

## Common Vulnerabilities
1. Missing appropriate security hardening across the application stack
2. Improperly configured permissions on cloud services
3. Unnecessary features enabled or installed (e.g., ports, services, pages, accounts, privileges)
4. Default accounts and their passwords still enabled and unchanged
5. Error handling revealing stack traces or other overly informative error messages to users
6. Upgraded systems with latest security features disabled or not configured securely
7. Security settings in application servers, frameworks, libraries, databases not set to secure values
8. Server not sending security headers or directives, or they are not set to secure values
9. Outdated or vulnerable software
10. [[_content/dictionary#X|XML]] External Entity ([[_content/dictionary#X|XXE]]) processing enabled

## Prevention
1. Implement a secure, repeatable, automated hardening process
2. Remove or disable unnecessary features, components, documentation, and samples
3. Review and update configurations of all security notes, updates, and patches as part of patch management
4. Implement a segmented application architecture with effective separation and security controls
5. Send security directives to clients, such as Security Headers
6. Automate verification of configurations and settings in all environments
7. Disable [[_content/dictionary#X|XML]] external entity processing and implement [[_content/dictionary#X|XML]] parsers with appropriate security settings

## Impact
Security misconfigurations can lead to unauthorized access to system data or functionality, complete system compromise, and data theft. The business impact depends on the protection needs of the application and data. 