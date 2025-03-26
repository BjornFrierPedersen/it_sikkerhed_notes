# A08:2021 - Software and Data Integrity Failures

## Description
Software and Data Integrity Failures is a new category for 2021 that focuses on assumptions related to software updates, critical data, and [[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] pipelines without verifying integrity. This category includes insecure deserialization, which was a separate category in the 2017 [[_content/dictionary#O|OWASP]] Top 10.

These failures relate to code and infrastructure that does not protect against integrity violations. Examples include applications that rely upon plugins, libraries, or modules from untrusted sources, repositories, and content delivery networks ([[_content/dictionary#C|CDN]]s) without sufficient integrity verification mechanisms.

## Common Vulnerabilities
1. Using plugins, libraries, or modules from untrusted sources
2. Using insecure [[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] pipelines that can introduce unauthorized access
3. Having auto-update functionality without sufficient integrity verification
4. Using unsigned or unencrypted serialized data without integrity checks
5. Relying on data from untrusted sources without verification
6. Insecure deserialization of user-supplied data
7. Using software from compromised repositories or [[_content/dictionary#C|CDN]]s

## Prevention
1. Use digital signatures to verify that software or data comes from the expected source and hasn't been altered
2. Ensure libraries and dependencies are consuming trusted repositories
3. Use a software supply chain security tool to verify components don't contain known vulnerabilities
4. Implement a review process for code and configuration changes to minimize the chance of introducing malicious code
5. Ensure your [[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] pipeline has proper segregation, configuration, and access control
6. Don't send unsigned or unencrypted serialized data to untrusted clients without integrity checks or digital signatures

## Impact
Successful exploitation can lead to serious consequences, including the execution of malicious code, data theft, and complete system compromise. The business impact depends on the protection needs of the application and data. 