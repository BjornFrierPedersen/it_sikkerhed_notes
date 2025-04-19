---
title: "Server Side Request Forgery Prevention Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html"
created: "1741872882.1395655"
tags: [owasp, cheatsheet, security]
---
# Server Side Request Forgery Prevention

## Server-Side Request Forgery Prevention Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[¶](#tools-and-code-used-for-schemas)](#references)](#semgrep-rules)](#imdsv2-in-aws)](#network-layer_1)](#application-layer_1)](#available-protections_1)](#challenges-in-blocking-urls-at-application-layer)](#case-2-application-can-send-requests-to-any-external-ip-address-or-domain-name)](#network-layer)](#url)](#domain-name)](#[ip-address](https://www.npmjs.com/package/ip-address))](#string)](#application-layer)](#available-protections)](#[example](Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#example))](#case-1-application-can-send-request-only-to-identified-and-trusted-applications)](#cases)](#overview-of-a-ssrf-common-flow)](#context)](#introduction)](#server-side-request-forgery-prevention-cheat-sheet)
### Introduction¶
The objective of the cheat sheet is to provide advices regarding the protection against [Server Side Request Forgery](https://www.acunetix.com/blog/[article](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b)s/server-side-request-forgery-vulnerability/) ([[_content/dictionary#S|SSRF]]) attack.
This cheat sheet will focus on the defensive point of view and will not explain how to perform this attack. This [[[talk](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_Orange_Tsai_Talk.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_Orange_Tsai_Talk.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_Orange_Tsai_Talk.pdf) from the security researcher [[[Orange Tsai](https://twitter.com/orange_8361)](https://twitter.com/orange_8361)](https://twitter.com/orange_8361) as well as this [[[[[document](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf)](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf) provide techniques on how to perform this kind of attack.
### Context¶
SSRF is an attack vector that abuses an application to interact with the internal/external network or the machine itself. One of the enablers for this vector is the mishandling of URLs, as showcased in the following examples:

- Image on an external server (e.g. user enters image [[_content/dictionary#U|URL]] of their avatar for the application to download and use).
Custom [[[_content/dictionary#W|WebHook]]](https://en.wikipedia.org/wiki/Webhook) (users have to specify Webhook handlers or Callback URLs).
- Internal requests to interact with another service to serve a specific functionality. Most of the times, user data is sent along to be processed, and if poorly handled, can perform specific injection attacks.

### Overview of a [[_content/dictionary#S|SSRF]] common flow¶

Notes:

[[_content/dictionary#S|SSRF]] is not limited to the [[_content/dictionary#H|HTTP]] protocol. Generally, the first request is HTTP, but in cases w[here](https://stackoverflow.com/a/26987741) the application itself performs the second request, it could use different protocols (e.g. [[_content/dictionary#F|FTP]], [[_content/dictionary#S|SMB]], [[_content/dictionary#S|SMTP]], etc.) and schemes (e.g. file://, phar://, gopher://, data://, dict://, etc.).
If the application is vulnerable to [[[_content/dictionary#X|XML]] eXternal Entity ([[_content/dictionary#X|XXE]]) injection](https://portswigger.net/web-security/xxe) then it can be exploited to perform a [SSRF attack](https://portswigger.net/web-security/xxe#exploiting-xxe-to-perform-ssrf-attacks), take a look at the [[XML_External_Entity_Prevention_Cheat_Sheet|XXE cheat sheet]] to learn how to prevent the exposure to XXE.

### Cases¶
Depending on the application's functionality and requirements, there are two basic cases in which [[_content/dictionary#S|SSRF]] can happen:

Application can send request only to identified and trusted applications: Case when [[allowlist](https://en.wikipedia.org/wiki/Whitelisting)](https://en.wikipedia.org/wiki/Whitelisting) approach is available.
Application can send requests to [[_content/dictionary#A|ANY]] external [[_content/dictionary#I|IP]] address or domain name: Case when [allowlist approach](Input_Validation_Cheat_Sheet.html#allow-list-vs-block-list) is unavailable.

Because these two cases are very different, this cheat sheet will describe defences against them separately.
#### Case 1 - Application can send request only to identified and trusted applications¶
Sometimes, an application needs to perform a request to another application, often located on another network, to perform a specific task. Depending on the business case, user input is required for the functionality to work.
##### Example¶

Take the example of a web application that receives and uses personal information from a user, such as their first name, last name, birth date etc. to create a profile in an internal [[_content/dictionary#H|HR]] system. By design, that web application will have to communicate using a protocol that the HR system understands to process that data.
Basically, the user cannot reach the HR system directly, but, if the web application in charge of receiving user information is vulnerable to [[_content/dictionary#S|SSRF]], the user can leverage it to access the HR system.
The user leverages the web application as a proxy to the HR system.

The allowlist approach is a viable option since the internal application called by the [[_content/dictionary#V|VulnerableApplication]] is clearly identified in the technical/business flow. It can be stated that the required calls will only be targeted between those identified and trusted applications.
##### ##### Available protections¶
Several protective measures are possible at the Application and Network layers. To apply the defense in depth principle, both layers will be hardened against such attacks.
###### ###### Application layer¶
The first level of protection that comes to mind is [[Input_Validation_Cheat_Sheet|Input validation]].
Based on that point, the following question comes to mind: How to perform this input validation?
As Orange Tsai shows in his talk, depending on the programming language used, parsers can be abused. One possible countermeasure is to apply the allowlist approach when input validation is used because, most of the time, the format of the information expected from the user is globally known.
The request sent to the internal application will be based on the following information:

- String containing business data.
- [[_content/dictionary#I|IP]] address (V4 or V6).
- Domain name.
- [[_content/dictionary#U|URL]].

Note: Disable the support for the following of the [[redirection](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Redirections)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections) in your web client in order to prevent the bypass of the input validation described in the [[section](Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#network-layer)](Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#application-layer) Exploitation tricks > Bypassing restrictions > Input validation > Unsafe redirect of this document.
###### String¶
In the context of [[_content/dictionary#S|SSRF]], validations can be added to ensure that the input string respects the business/technical format expected.
A [regex](https://www.regular-expressions.info/) can be used to ensure that data received is valid from a security point of view if the input data have a simple format (e.g. token, zip code, etc.). Otherwise, validation should be conducted using the libraries available from the string object because regex for complex formats are difficult to maintain and are highly error-prone.
User input is assumed to be non-network related and consists of the user's personal information.
Example:
//Regex validation for a data having a simple format
if(Pattern.matches("[a-zA-Z0-9\\s\\-]{1,50}", userInput)){
    //Continue the processing because the input data is valid
}else{
    //Stop the processing and reject the request
}

###### [[_content/dictionary#I|IP]] address¶
In the context of [[_content/dictionary#S|SSRF]], there are 2 possible validations to perform:

1. Ensure that the data provided is a valid [[_content/dictionary#I|IP]] V4 or V6 address.
2. Ensure that the IP address provided belongs to one of the IP addresses of the identified and trusted applications.

The first layer of validation can be applied using libraries that ensure the security of the [[_content/dictionary#I|IP]] address format, based on the technology used (library option is proposed here to delegate the managing of the IP address format and leverage battle-tested validation function):

Verification of the proposed libraries has been performed regarding the exposure to bypasses (Hex, Octal, Dword, [[_content/dictionary#U|URL]] and Mixed encoding) described in this article.

[[_content/dictionary#J|JAVA]]: Method [[[_content/dictionary#I|InetAddressValidator]].isValid](http://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/InetAddressValidator.html#isValid(java.lang.String)) from the [[Apache Commons Validator](http://commons.apache.org/proper/commons-validator/)](http://commons.apache.org/proper/commons-validator/) library.
- - - - - - It is [[_content/dictionary#N|NOT]] exposed to bypass using Hex, Octal, Dword, [[_content/dictionary#U|URL]] and Mixed encoding.

.[[_content/dictionary#N|NET]]: Method [[IPAddr](https://ruby-doc.org/stdlib-2.0.0/libdoc/ipaddr/rdoc/IPAddr.html)ess.[[_content/dictionary#T|TryParse]]](https://docs.microsoft.com/en-us/dotnet/api/system.net.ipaddress.tryparse?view=netframework-4.8) from the [[_content/dictionary#S|SDK]].
- - It is exposed to bypass using Hex, Octal, Dword and Mixed encoding but [[_content/dictionary#N|NOT]] the [[_content/dictionary#U|URL]] encoding.
- - As allowlisting is used here, any bypass tentative will be blocked during the comparison against the allowed list of [[_content/dictionary#I|IP]] addresses.

- [[_content/dictionary#J|JavaScript]]: Library ip-address.
It is [[_content/dictionary#N|NOT]] exposed to bypass using Hex, Octal, Dword, [[_content/dictionary#U|URL]] and Mixed encoding.

- Ruby: Class IPAddr from the [[_content/dictionary#S|SDK]].
It is [[_content/dictionary#N|NOT]] exposed to bypass using Hex, Octal, Dword, [[_content/dictionary#U|URL]] and Mixed encoding.

Use the output value of the method/library as the [[_content/dictionary#I|IP]] address to compare against the allowlist.

After ensuring the validity of the incoming [[_content/dictionary#I|IP]] address, the second layer of validation is applied. An allowlist is created after determining all the IP addresses (v4 and v6 to avoid bypasses) of the identified and trusted applications. The valid IP is cross-checked with that list to ensure its communication with the internal application (string strict comparison with case sensitive).
###### Domain name¶
In the attempt of validate domain names, it is apparent to do a [[_content/dictionary#D|DNS]] resolution to verify the existence of the domain. In general, it is not a bad idea, yet it opens up the application to attacks depending on the configuration used regarding the DNS servers used for the domain name resolution:

- It can disclose information to external [[_content/dictionary#D|DNS]] resolvers.
- It can be used by an attacker to bind a legit domain name to an internal [[_content/dictionary#I|IP]] address. See the section Exploitation tricks > Bypassing restrictions > Input validation > [[_content/dictionary#D|DNS]] pinning of this document.
- An attacker can use it to deliver a malicious payload to the internal [[_content/dictionary#D|DNS]] resolvers and the [[_content/dictionary#A|API]] ([[_content/dictionary#S|SDK]] or third-party) used by the application to handle the DNS communication and then, potentially, trigger a vulnerability in one of these components.

In the context of [[_content/dictionary#S|SSRF]], there are two validations to perform:

1. Ensure that the data provided is a valid domain name.
2. Ensure that the domain name provided belongs to one of the domain names of the identified and trusted applications (the allowlisting comes to action here).

Similar to the [[_content/dictionary#I|IP]] address validation, the first layer of validation can be applied using libraries that ensure the security of the domain name format, based on the technology used (library option is proposed here in order to delegate the managing of the domain name format and leverage battle tested validation function):

Verification of the proposed libraries has been performed to ensure that the proposed functions do not perform any [[_content/dictionary#D|DNS]] resolution query.

[[_content/dictionary#J|JAVA]]: Method [[[_content/dictionary#D|DomainValidator]].isValid](https://commons.apache.org/proper/commons-validator/apidocs/org/apache/commons/validator/routines/DomainValidator.html#isValid(java.lang.String)) from the Apache Commons Validator library.
.[[_content/dictionary#N|NET]]: Method [Uri.[[_content/dictionary#C|CheckHostName]]](https://docs.microsoft.com/en-us/dotnet/api/system.uri.checkhostname?view=netframework-4.8) from the [[_content/dictionary#S|SDK]].
[[_content/dictionary#J|JavaScript]]: Library [is-valid-domain](https://www.npmjs.com/package/is-valid-domain).
Python: Module [validators.domain](https://validators.readthedocs.io/en/latest/#module-validators.domain).
Ruby: No valid dedicated gem has been found.
[domainator](https://github.com/mhuggins/domainator), [public_suffix](https://github.com/weppos/publicsuffix-ruby) and [addressable](https://github.com/sporkmonger/addressable) has been tested but unfortunately they all consider <script>alert(1)</script>.owasp.org as a valid domain name.
- - This regex, taken from here, can be used: ^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$

Example of execution of the proposed regex for Ruby:
domain_names = ["owasp.org","owasp-test.org","doc-test.owasp.org","doc.owasp.org",
                "<script>alert(1)</script>","<script>alert(1)</script>.owasp.org"]
domain_names.each { |domain_name|
    if ( domain_name =~ /^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ )
        puts "[i] #{domain_name} is VALID"
    else
        puts "[!] #{domain_name} is INVALID"
    end
}

$ ruby test.rb
[i] owasp.org is [[_content/dictionary#V|VALID]]
[i] owasp-test.org is VALID
[i] doc-test.owasp.org is VALID
[i] doc.owasp.org is VALID
[!] <script>alert(1)</script> is [[_content/dictionary#I|INVALID]]
[!] <script>alert(1)</script>.owasp.org is INVALID

After ensuring the validity of the incoming domain name, the second layer of validation is applied:

1. Build an allowlist with all the domain names of every identified and trusted applications.
2. Verify that the domain name received is part of this allowlist (string strict comparison with case sensitive).

Unfortunately here, the application is still vulnerable to the [[_content/dictionary#D|DNS]] pinning bypass mentioned in this document. Indeed, a DNS resolution will be made when the business code will be executed. To address that issue, the following action must be taken in addition of the validation on the domain name:

1. Ensure that the domains that are part of your organization are resolved by your internal [[_content/dictionary#D|DNS]] server first in the chains of DNS resolvers.
2. Monitor the domains allowlist in order to detect when any of them resolves to a/an:
   - Local [[_content/dictionary#I|IP]] address (V4 + V6).
   - Internal IP of your organization (expected to be in private IP ranges) for the domain that are not part of your organization.

The following Python3 script can be used, as a starting point, for the monitoring mentioned above:
# Dependencies: pip install ipaddress dnspython
import ipaddress
import dns.resolver

# Configure the allowlist to check
DOMAINS_ALLOWLIST = ["owasp.org", "labslinux"]

# Configure the [[_content/dictionary#D|DNS]] resolver to use for all DNS queries
DNS_RESOLVER = dns.resolver.Resolver()
DNS_RESOLVER.nameservers = ["1.1.1.1"]

def verify_dns_records(domain, records, type):
    """
    Verify if one of the [[_content/dictionary#D|DNS]] records resolve to a non public [[_content/dictionary#I|IP]] address.
    Return a boolean indicating if any error has been detected.
    """
    error_detected = False
    if records is not None:
        for record in records:
            value = record.to_text().strip()
            try:
                ip = ipaddress.ip_address(value)
                # See https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global
                if not ip.is_global:
                    print("[!] DNS record type '%s' for domain name '%s' resolve to
                    a non public IP address '%s'!" % (type, domain, value))
                    error_detected = True
            except [[_content/dictionary#V|ValueError]]:
                error_detected = True
                print("[!] '%s' is not valid IP address!" % value)
    return error_detected

def check():
    """
    Perform the check of the allowlist of domains.
    Return a boolean indicating if any error has been detected.
    """
    error_detected = False
    for domain in DOMAINS_ALLOWLIST:
        # Get the IPs of the current domain
        # See https://en.wikipedia.org/wiki/List_of_DNS_record_types
        try:
            # A = IPv4 address record
            ip_v4_records = DNS_RESOLVER.query(domain, "A")
        except Exception as e:
            ip_v4_records = None
            print("[i] Cannot get A record for domain '%s': %s\n" % (domain,e))
        try:
            # [[_content/dictionary#A|AAAA]] = IPv6 address record
            ip_v6_records = DNS_RESOLVER.query(domain, "AAAA")
        except Exception as e:
            ip_v6_records = None
            print("[i] Cannot get AAAA record for domain '%s': %s\n" % (domain,e))
        # Verify the IPs obtained
        if verify_dns_records(domain, ip_v4_records, "A")
        or verify_dns_records(domain, ip_v6_records, "AAAA"):
            error_detected = True
    return error_detected

if __name__== "__main__":
    if check():
        exit(1)
    else:
        exit(0)

###### [[_content/dictionary#U|URL]]¶
Do not accept complete URLs from the user because URL are difficult to validate and the parser can be abused depending on the technology used as showcased by the following talk of Orange Tsai.
If network related information is really needed then only accept a valid [[_content/dictionary#I|IP]] address or domain name.
###### ###### Network layer¶
The objective of the Network layer security is to prevent the [[_content/dictionary#V|VulnerableApplication]] from performing calls to arbitrary applications. Only allowed routes will be available for this application in order to limit its network access to only those that it should communicate with.
The Firewall component, as a specific device or using the one provided within the operating system, will be used here to define the legitimate flows.
In the schema below, a Firewall component is leveraged to limit the application's access, and in turn, limit the impact of an application vulnerable to [[_content/dictionary#S|SSRF]]:

[Network segregation](https://www.mwrinfosecurity.com/our-thinking/making-the-case-for-network-segregation) (see this set of [implementation advice](https://www.cyber.gov.au/acsc/view-all-content/publications/implementing-network-segmentation-and-segregation) can also be leveraged and is highly recommended in order to block illegitimate calls directly at network level itself.
#### Case 2 - Application can send requests to [[_content/dictionary#A|ANY]] external [[_content/dictionary#I|IP]] address or domain name¶
This case happens when a user can control a [[_content/dictionary#U|URL]] to an External resource and the application makes a request to this URL (e.g. in case of [[[_content/dictionary#W|WebHooks]]](https://en.wikipedia.org/wiki/Webhook)). Allow lists cannot be used here because the list of IPs/domains is often unknown upfront and is dynamically changing.
In this scenario, External refers to any IP that doesn't belong to the internal network, and should be reached by going over the public internet.
Thus, the call from the Vulnerable Application:

- Is [[_content/dictionary#N|NOT]] targeting one of the [[_content/dictionary#I|IP]]/domain located inside the company's global network.
- Uses a convention defined between the [[_content/dictionary#V|VulnerableApplication]] and the expected [[_content/dictionary#I|IP]]/domain in order to prove that the call has been legitimately initiated.

##### Challenges in blocking URLs at application layer¶
Based on the business requirements of the above mentioned applications, the allowlist approach is not a valid solution. Despite knowing that the block-list approach is not an impenetrable wall, it is the best solution in this scenario. It is informing the application what it should not do.
Here is why filtering URLs is hard at the Application layer:

It implies that the application must be able to detect, at the code level, that the provided [[_content/dictionary#I|IP]] (V4 + V6) is not part of the official [private networks ranges](https://en.wikipedia.org/wiki/Private_network) including also localhost and IPv4/v6 Link-Local addresses. Not every [[_content/dictionary#S|SDK]] provides a built-in feature for this kind of verification, and leaves the handling up to the developer to understand all of its pitfalls and possible values, which makes it a demanding task.
- Same remark for domain name: The company must maintain a list of all internal domain names and provide a centralized service to allow an application to verify if a provided domain name is an internal one. For this verification, an internal [[_content/dictionary#D|DNS]] resolver can be queried by the application but this internal DNS resolver must not resolve external domain names.

Available protections¶
Taking into consideration the same assumption in the following example for the following sections.
Application layer¶
Like for the case [[n°1](Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#application-layer)](Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html#case-1-application-can-send-request-only-to-identified-and-trusted-applications), it is assumed that the [[_content/dictionary#I|IP]] Address or domain name is required to create the request that will be sent to the [[_content/dictionary#T|TargetApplication]].
The first validation on the input data presented in the case n°1 on the 3 types of data will be the same for this case [[_content/dictionary#B|BUT]] the second validation will differ. Indeed, here we must use the block-list approach.

Regarding the proof of legitimacy of the request: The [[_content/dictionary#T|TargetedApplication]] that will receive the request must generate a random token (ex: alphanumeric of 20 characters) that is expected to be passed by the caller (in body via a parameter for which the name is also defined by the application itself and only allow characters set [a-z]{1,10}) to perform a valid request. The receiving endpoint must only accept [[_content/dictionary#H|HTTP]] [[_content/dictionary#P|POST]] requests.

Validation flow (if one the validation steps fail then the request is rejected):

1. The application will receive the IP address or domain name of the [[_content/dictionary#T|TargetedApplication]] and it will apply the first validation on the input data using the libraries/regex mentioned in this section.
The second validation will be applied against the IP address or domain name of the TargetedApplication using the following block-list approach:
   - For IP address:
- 3. The application will verify that it is a public one (see the hint provided in the next paragraph with the python code sample).
- For domain name:
- 5. 1. The application will verify that it is a public one by trying to resolve the domain name against the [[_content/dictionary#D|DNS]] resolver that will only resolve internal domain name. Here, it must return a response indicating that it do not know the provided domain because the expected value received must be a public domain.
- 6. 2. To prevent the [[_content/dictionary#D|DNS]] pinning attack described in this document, the application will retrieve all the [[_content/dictionary#I|IP]] addresses behind the domain name provided (taking records A + [[_content/dictionary#A|AAAA]] for IPv4 + IPv6) and it will apply the same verification described in the previous point about IP addresses.

7. The application will receive the protocol to use for the request via a dedicated input parameter for which it will verify the value against an allowed list of protocols ([[_content/dictionary#H|HTTP]] or [[_content/dictionary#H|HTTPS]]).
8. The application will receive the parameter name for the token to pass to the [[_content/dictionary#T|TargetedApplication]] via a dedicated input parameter for which it will only allow the characters set [a-z]{1,10}.
9. The application will receive the token itself via a dedicated input parameter for which it will only allow the characters set [a-zA-Z0-9]{20}.
10. The application will receive and validate (from a security point of view) any business data needed to perform a valid call.
11. The application will build the HTTP [[_content/dictionary#P|POST]] request using only validated information and will send it (don't forget to disable the support for redirection in the web client used).

Network layer¶
Similar to the following section.
### [[IMDSv2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/) in [[_content/dictionary#A|AWS]]¶
In cloud environments [[_content/dictionary#S|SSRF]] is often used to access and steal credentials and access tokens from metadata services (e.g. AWS Instance Metadata Service, Azure Instance Metadata Service, [[_content/dictionary#G|GCP]] metadata server).
IMDSv2 is an additional defence-in-depth mechanism for AWS that mitigates some of the instances of SSRF.
To leverage this protection migrate to IMDSv2 and disable old IMDSv1. Check out [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) for more details.
### [Semgrep](https://semgrep.dev/) Rules¶
Semgrep is a command-line tool for offline static analysis. Use pre-built or custom rules to enforce code and security standards in your codebase.
Checkout the Semgrep rule for SSRF to identify/investigate for SSRF vulnerabilities in Java
[https://semgrep.dev/salecharohit:owasp_java_ssrf](https://semgrep.dev/salecharohit:owasp_java_ssrf)
### References¶
Online version of the [SSRF bible](https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM) ([[_content/dictionary#P|PDF]] version is used in this cheat sheet).
Article about [Bypassing SSRF Protection](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b).
Articles about SSRF attacks: [Part 1](https://medium.com/poka-techblog/server-side-request-forgery-ssrf-attacks-part-1-the-basics-a42ba5cc244a), [part 2](https://medium.com/poka-techblog/server-side-request-forgery-ssrf-attacks-part-2-fun-with-ipv4-addresses-eb51971e476d) and  [part 3](https://medium.com/poka-techblog/server-side-request-forgery-ssrf-part-3-other-advanced-techniques-3f48cbcad27e).
Article about IMDSv2
### Tools and code used for schemas¶

[Mermaid Online Editor](https://mermaidjs.github.io/mermaid-live-editor) and [Mermaid documentation](https://mermaidjs.github.io/).
[Draw.io Online Editor](https://www.draw.io/).

Mermaid code for [[_content/dictionary#S|SSRF]] common flow (printscreen are used to capture [[_content/dictionary#P|PNG]] image inserted into this cheat sheet):
sequenceDiagram
    participant Attacker
    participant [[_content/dictionary#V|VulnerableApplication]]
    participant [[_content/dictionary#T|TargetedApplication]]
    Attacker->>VulnerableApplication: Crafted [[_content/dictionary#H|HTTP]] request
    VulnerableApplication->>TargetedApplication: Request (HTTP, [[_content/dictionary#F|FTP]]...)
    Note left of TargetedApplication: Use payload included<br>into the request to<br>VulnerableApplication
    TargetedApplication->>VulnerableApplication: Response
    VulnerableApplication->>Attacker: Response
    Note left of VulnerableApplication: Include response<br>from the<br>TargetedApplication

Draw.io schema [[_content/dictionary#X|XML]] code for the "[case 1 for network layer protection about flows that we want to prevent](../assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_Case1_NetworkLayer_PreventFlow.xml)" schema (printscreen are used to capture [[_content/dictionary#P|PNG]] image inserted into this cheat sheet).