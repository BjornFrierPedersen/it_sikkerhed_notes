# A06:2021 - Vulnerable and Outdated Components

## Description
Vulnerable and Outdated Components refers to the use of components (such as libraries, frameworks, and other software modules) that have known vulnerabilities or are out of date. This category was previously titled "Using Components with Known Vulnerabilities" in the 2017 [[_content/dictionary#O|OWASP]] Top 10 and has moved up from #9 to #6 in the 2021 edition.

This is the only category in the [[_content/dictionary#O|OWASP]] Top 10 that doesn't have any Common Vulnerabilities and Exposures ([[_content/dictionary#C|CVE]]s) mapped to the included Common Weakness Enumerations ([[_content/dictionary#C|CWE]]s), indicating the challenges in tracking and categorizing these vulnerabilities. It ranked #2 in the Top 10 community survey, showing high concern among security professionals.

## Common Vulnerabilities
1. Using components with known vulnerabilities
2. Using unsupported or outdated software, including [[_content/dictionary#O|OS]], web/application server, database management system, applications, [[_content/dictionary#A|API]]s, and all components, runtime environments, and libraries
3. Not scanning for vulnerabilities regularly
4. Not fixing or upgrading the underlying platform, frameworks, and dependencies in a timely fashion
5. Not securing the components' configurations
6. Not testing the compatibility of updated, upgraded, or patched libraries

## Prevention
1. Remove unused dependencies, unnecessary features, components, files, and documentation
2. Continuously inventory versions of both client-side and server-side components and their dependencies
3. Only obtain components from official sources over secure links
4. Monitor for libraries and components that are unmaintained or don't create security patches for older versions
5. Establish a patch management process
6. Use software composition analysis tools to automate the process
7. Subscribe to email alerts for security vulnerabilities related to components you use

## Impact
The impact can range from minor to catastrophic, depending on the vulnerability. Exploits can lead to data loss, server takeover, and other serious consequences that might lead to severe business damage. 