# A01:2021 - Broken Access Control

## Description
Broken Access Control refers to failures in enforcing restrictions on authenticated users' actions, leading to unauthorized access to functionality or data. This has moved from the fifth position in 2017 to the most serious web application security risk in 2021. The data shows that on average, 3.81% of applications tested had one or more [[_content/dictionary#C|CWE]]s related to this risk.

## Common Vulnerabilities
1. Violation of the principle of least privilege or deny by default, where access should be granted only for particular capabilities, roles, or users.
2. Bypassing access control checks by modifying the [[_content/dictionary#U|URL]] (parameter tampering or force browsing), internal application state, the [[_content/dictionary#H|HTML]] page, or by using an [[_content/dictionary#A|API]] attack tool.
3. Permitting viewing or editing someone else's account by providing its unique identifier (insecure direct object references).
4. Accessing [[_content/dictionary#A|API]] without access controls for [[_content/dictionary#P|POST]], [[_content/dictionary#P|PUT]], and [[_content/dictionary#D|DELETE]] operations.
5. Elevation of privilege. Acting as a user without being logged in, or acting as an admin when logged in as a user.
   - See [Privilege Escalation Examples](privilege_escalation_examples.md) for detailed explanations of horizontal and vertical privilege escalation with code examples.
6. Metadata manipulation, such as replaying or tampering with a [[_content/dictionary#J|JWT]] access control token, manipulated cookie or a hidden field.
7. [[_content/dictionary#C|CORS]] misconfiguration allowing unauthorized [[_content/dictionary#A|API]] access.
8. Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user.

## Prevention
1. Implement access control mechanisms once and re-use them throughout the application, including minimizing [[_content/dictionary#C|CORS]] usage.
2. Model access controls should enforce record ownership rather than accepting that the user can create, read, update, or delete any record.
3. Unique application business limit requirements should be enforced by domain models.
4. Disable web server directory listing and ensure file metadata (e.g., .git) and backup files are not present within web roots.
5. Log access control failures, alert admins when appropriate.
6. Rate limit [[_content/dictionary#A|API]] and controller access to minimize the harm from automated attack tooling.
7. Stateful session identifiers should be invalidated on the server after logout.
8. **Implement Role-Based Access Control ([[_content/dictionary#R|RBAC]])**: Identify which users and what roles they have that should be able to access the system and implement RBAC to enforce boundaries. Don't reinvent the wheel, use an existing system which has been built for security. Consider extending RBAC with Attribute-Based Access Control ([[_content/dictionary#A|ABAC]]) or Relationship-Based Access Control (ReBAC) for more fine-grained permissions when appropriate.

## Impact
The impact of broken access control can be severe, potentially leading to data theft, system compromise, or business damage. Attackers may access unauthorized functionality or data, such as accessing other users' accounts, viewing sensitive files, modifying data, or changing access rights. 