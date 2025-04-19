# A09:2021 - Security Logging and Monitoring Failures

## Description
Security Logging and Monitoring Failures refers to inadequate logging, detection, monitoring, and active response to security incidents. This category was previously known as "Insufficient Logging & Monitoring" in the 2017 [[_content/dictionary#O|OWASP]] Top 10 and has moved up from the tenth position to the ninth position in the 2021 edition.

Proper logging and monitoring are critical for detecting, alerting, and responding to security breaches. Without these capabilities, breaches may go undetected for extended periods, allowing attackers to persist within systems, extract data, or cause other damage. This category ranked #3 in the Top 10 community survey, indicating high concern among security professionals.

## Common Vulnerabilities
1. Auditable events, such as logins, failed logins, and high-value transactions, are not logged
2. Warnings and errors generate no, inadequate, or unclear log messages
3. Logs of applications and [[_content/dictionary#A|API]]s are not monitored for suspicious activity
4. Logs are only stored locally
5. Appropriate alerting thresholds and response escalation processes are not in place or effective
6. Penetration testing and scans by dynamic application security testing ([[_content/dictionary#D|DAST]]) tools do not trigger alerts
7. The application cannot detect, escalate, or alert for active attacks in real-time or near real-time
8. The application logs to a local file instead of a remote logging service that's more difficult for attackers to tamper with

## Prevention
1. Ensure all login, access control, and server-side input validation failures can be logged with sufficient user context
2. Ensure logs are generated in a format that log management solutions can easily consume
3. Ensure log data is encoded correctly to prevent injections or attacks on the logging or monitoring systems
4. Ensure high-value transactions have an audit trail with integrity controls to prevent tampering or deletion
5. Establish effective monitoring and alerting so suspicious activities are detected and responded to quickly
6. Establish or adopt an incident response and recovery plan

## Impact
Without proper logging and monitoring, breaches can go undetected for long periods, allowing attackers to establish persistence, pivot to other systems, and extract, destroy, or modify data. The time to detect a breach is often measured in months, which gives attackers plenty of time to cause significant damage. 