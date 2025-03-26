# A10:2021 - Server-Side Request Forgery

## Description
Server-Side Request Forgery ([[_content/dictionary#S|SSRF]]) is a vulnerability that occurs when a web application fetches a remote resource without validating the user-supplied [[_content/dictionary#U|URL]]. This allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, [[_content/dictionary#V|VPN]], or another type of network access control list ([[_content/dictionary#A|ACL]]).

[[_content/dictionary#S|SSRF]] is a new addition to the [[_content/dictionary#O|OWASP]] Top 10 for 2021, primarily due to the rise in cloud services and the increasing complexity of architectures. Modern web applications often fetch remote resources, making [[_content/dictionary#S|SSRF]] a common and potentially severe vulnerability. This category ranked #1 in the Top 10 community survey, indicating very high concern among security professionals.

## Common Vulnerabilities
1. Applications that fetch remote resources without validating user-supplied [[_content/dictionary#U|URL]]s
2. Applications that allow [[_content/dictionary#U|URL]] redirection to arbitrary destinations
3. Applications that don't enforce [[_content/dictionary#U|URL]] schemas, allowing attackers to use schemes like file://, dict://, [[_content/dictionary#F|FTP]]://, and gopher://
4. Applications that don't validate or incorrectly validate the destination [[_content/dictionary#I|IP]] address against blocklists or allowlists
5. Applications that forward the complete [[_content/dictionary#U|URL]] without attempting to parse it and check the destination

## Prevention
1. Implement defense in depth controls:
   - **Network layer:** Segment remote resource access functionality in separate networks
   - **Application layer:**
     - Sanitize and validate all client-supplied input data
     - Enforce [[_content/dictionary#U|URL]] schema, port, and destination with a positive allow list
     - Do not send raw responses to clients
     - Disable [[_content/dictionary#H|HTTP]] redirections
     - Be aware of [[_content/dictionary#U|URL]] consistency to avoid attacks like [[_content/dictionary#D|DNS]] rebinding
2. Do not mitigate [[_content/dictionary#S|SSRF]] via the use of a deny list or regular expression. Attackers have payload lists, tools, and skills to bypass deny lists.

## Impact
Successful [[_content/dictionary#S|SSRF]] attacks can lead to:
1. Port scanning internal systems
2. Enumeration of internal services
3. Accessing sensitive data in internal services
4. Accessing metadata storage of cloud services (potentially leading to compromise of cloud environments)
5. Interacting with internal systems that shouldn't be exposed to the internet
6. Remote code execution in some cases 