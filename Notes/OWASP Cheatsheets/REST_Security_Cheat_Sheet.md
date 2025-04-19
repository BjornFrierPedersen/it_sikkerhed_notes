---
title: "REST Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html"
created: "1741872882.0994334"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#R|REST]] Security

## [[[_content/dictionary#R|REST]]](http://en.wikipedia.org/wiki/Representational_state_transfer) Security Cheat Sheet[[[[[[[[[[[[[[[[[[¶](#http-return-code)](#sensitive-information-in-http-requests)](#cors)](#security-headers)](#audit-logs)](#error-handling)](#management-endpoints)](#send-safe-response-content-types)](#validate-request-content-types)](#validate-content-types)](#input-validation)](#restrict-http-methods)](#api-keys)](#jwt)](#access-control)](#https)](#introduction)](#rest-security-cheat-sheet)
### Introduction¶
REST (or REpresentational State Transfer) is an architectural style first described in [Roy Fielding](https://en.wikipedia.org/wiki/Roy_Fielding)'s Ph.D. dissertation on [Architectural Styles and the Design of Network-based Software Architectures](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm).
It evolved as Fielding wrote the [[_content/dictionary#H|HTTP]]/1.1 and [[_content/dictionary#U|URI]] specs and has been proven to be well-suited for developing distributed hypermedia applications. While REST is more widely applicable, it is most commonly used within the context of communicating with services via HTTP.
The key abstraction of information in REST is a resource. A REST [[_content/dictionary#A|API]] resource is identified by a URI, usually a HTTP [[_content/dictionary#U|URL]]. REST components use connectors to perform actions on a resource by using a representation to capture the current or intended state of the resource and transferring that representation.
The primary connector types are client and server, secondary connectors include cache, resolver and tunnel.
REST APIs are stateless. Stateful APIs do not ad[[[[[[here](https://restfulapi.net/http-status-codes)](https://www.restapitutorial.com/httpstatuscodes.html)](https://www.youtube.com/watch?v=bW5pS4e_MX8>)](https://www.chosenplaintext.ca/2015/03/31/jwt-algorithm-confusion.html)](https://tools.ietf.org/html/rfc7515#section-10.5)](https://tools.ietf.org/html/rfc7519#section-6.1) to the REST architectural style. State in the REST acronym refers to the state of the resource which the API accesses, not the state of a session within which the API is called. While there may be good reasons for building a stateful API, it is important to realize that managing sessions is complex and difficult to do securely.
Stateful services are out of scope of this Cheat Sheet: Passing state from client to backend, while making the service technically stateless, is an anti-pattern that should also be avoided as it is prone to replay and impersonation attacks.
In order to implement flows with REST APIs, resources are typically created, read, updated and deleted. For example, an ecommerce site may offer methods to create an empty shopping cart, to add items to the cart and to check out the cart. Each of these REST calls is stateless and the endpoint should check whether the caller is authorized to perform the requested operation.
Another key feature of REST applications is the use of standard HTTP verbs and error codes in the pursuit or removing unnecessary variation among different services.
Another key feature of REST applications is the use of [[[_content/dictionary#H|HATEOAS]] or Hypermedia As The Engine of Application State](https://en.wikipedia.org/wiki/HATEOAS). This provides REST applications a self-documenting nature making it easier for developers to interact with a REST service without prior knowledge.
### [[_content/dictionary#H|HTTPS]]¶
Secure REST services must only provide HTTPS endpoints. This protects authentication credentials in transit, for example passwords, API keys or [[[_content/dictionary#J|JSON]] Web Tokens](https://tools.ietf.org/html/rfc7519). It also allows clients to authenticate the service and guarantees integrity of the transmitted data.
See the [[Transport_Layer_Security_Cheat_Sheet|Transport Layer Security Cheat Sheet]] for additional information.
Consider the use of mutually authenticated client-side certificates to provide additional protection for highly privileged web services.
### Access Control¶
Non-public REST services must perform access control at each API endpoint. Web services in monolithic applications implement this by means of user authentication, authorization logic and session management. This has several drawbacks for modern architectures which compose multiple microservices following the RESTful style.

- in order to minimize latency and reduce coupling between services, the access control decision should be taken locally by [[_content/dictionary#R|REST]] endpoints
- user authentication should be centralised in a Identity Provider (IdP), which issues access tokens

### [[_content/dictionary#J|JWT]]¶
There seems to be a convergence towards using [[_content/dictionary#J|JSON]] Web Tokens (JWT) as the format for security tokens. JWTs are JSON data structures containing a set of claims that can be used for access control decisions. A cryptographic signature or message authentication code ([[_content/dictionary#M|MAC]]) can be used to protect the integrity of the JWT.

- Ensure JWTs are integrity protected by either a signature or a [[_content/dictionary#M|MAC]]. Do not allow the unsecured JWTs: {"alg":"none"}.
- - See here

- In general, signatures should be preferred over MACs for integrity protection of JWTs.

If MACs are used for integrity protection, every service that is able to validate JWTs can also create new JWTs using the same key. This means that all services using the same key have to mutually trust each other. Another consequence of this is that a compromise of any service also compromises all other services sharing the same key. See here for additional information.
The relying party or token consumer validates a [[_content/dictionary#J|JWT]] by verifying its integrity and claims contained.

- A relying party must verify the integrity of the [[_content/dictionary#J|JWT]] based on its own configuration or hard-coded logic. It must not rely on the information of the JWT header to select the verification algorithm. See here and here

Some claims have been standardized and should be present in [[_content/dictionary#J|JWT]] used for access controls. At least the following of the standard claims should be verified:

- iss or issuer - is this a trusted issuer? Is it the expected owner of the signing key?
- aud or audience - is the relying party in the target audience for this [[_content/dictionary#J|JWT]]?
- exp or expiration time - is the current time before the end of the validity period of this token?
- nbf or not before time - is the current time after the start of the validity period of this token?

As JWTs contain details of the authenticated entity (user etc.) a disconnect can occur between the [[_content/dictionary#J|JWT]] and the current state of the users session, for example, if the session is terminated earlier than the expiration time due to an explicit logout or an idle timeout. When an explicit session termination event occurs, a digest or hash of any associated JWTs should be submitted to a denylist on the API which will invalidate that JWT for any requests until the expiration of the token. See the [JSON_Web_Token_for_Java_Cheat_Sheet](JSON_Web_Token_for_Java_Cheat_Sheet.html#token-explicit-revocation-by-the-user) for further details.
### [[_content/dictionary#A|API]] Keys¶
Public [[_content/dictionary#R|REST]] services without access control run the risk of being farmed leading to excessive bills for bandwidth or compute cycles. API keys can be used to mitigate this risk. They are also often used by organisation to monetize APIs; instead of blocking high-frequency calls, clients are given access in accordance to a purchased access plan.
API keys can reduce the impact of denial-of-service attacks. However, when they are issued to third-party clients, they are relatively easy to compromise.

- Require [[_content/dictionary#A|API]] keys for every request to the protected endpoint.
- Return 429 Too Many Requests [[_content/dictionary#H|HTTP]] response code if requests are coming in too quickly.
- Revoke the [[_content/dictionary#A|API]] key if the client violates the usage agreement.
- Do not rely exclusively on [[_content/dictionary#A|API]] keys to protect sensitive, critical or high-value resources.

### Restrict [[_content/dictionary#H|HTTP]] methods¶

- Apply an allowlist of permitted [[_content/dictionary#H|HTTP]] Methods e.g. [[_content/dictionary#G|GET]], [[_content/dictionary#P|POST]], [[_content/dictionary#P|PUT]].
- Reject all requests not matching the allowlist with [[_content/dictionary#H|HTTP]] response code 405 Method not allowed.
- Make sure the caller is authorised to use the incoming [[_content/dictionary#H|HTTP]] method on the resource collection, action, and record

In Java [[_content/dictionary#E|EE]] in particular, this can be difficult to implement properly. See [Bypassing Web Authentication and Authorization with [[_content/dictionary#H|HTTP]] Verb Tampering](../assets/REST_Security_Cheat_Sheet_Bypassing_VBAAC_with_HTTP_Verb_Tampering.pdf) for an explanation of this common misconfiguration.
### Input validation¶

- Do not trust input parameters/objects.
- Validate input: length / range / format and type.
- Achieve an implicit input validation by using strong types like numbers, booleans, dates, times or fixed data ranges in [[_content/dictionary#A|API]] parameters.
- Constrain string inputs with regexps.
- Reject unexpected/illegal content.
- Make use of validation/sanitation libraries or frameworks in your specific language.
- Define an appropriate request size limit and reject requests exceeding the limit with [[_content/dictionary#H|HTTP]] response status 413 Request Entity Too Large.
- Consider logging input validation failures. Assume that someone who is performing hundreds of failed input validations per second is up to no good.
- Have a look at input validation cheat sheet for comprehensive explanation.
Use a secure parser for parsing the incoming messages. If you are using [[_content/dictionary#X|XML]], make sure to use a parser that is not vulnerable to [[[_content/dictionary#X|XXE]]](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_%28XXE%29_Processing) and similar attacks.

### Validate content types¶
A [[_content/dictionary#R|REST]] request or response body should match the intended content type in the header. Otherwise this could cause misinterpretation at the consumer/producer side and lead to code injection/execution.

- Document all supported content types in your [[_content/dictionary#A|API]].

#### Validate request content types¶

- Reject requests containing unexpected or missing content type headers with [[_content/dictionary#H|HTTP]] response status 406 Unacceptable or 415 Unsupported Media Type. For requests with Content-Length: 0 however, a Content-type header is optional.
For [[_content/dictionary#X|XML]] content types ensure appropriate XML parser hardening, see the [[XML_External_Entity_Prevention_Cheat_Sheet|[[_content/dictionary#X|XXE]] cheat sheet]].
Avoid accidentally exposing unintended content types by explicitly defining content types e.g. [Jersey](https://jersey.github.io/) (Java) @consumes("application/json"); @produces("application/json"). This avoids [XXE-attack](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_%28XXE%29_Processing) vectors for example.

#### Send safe response content types¶
It is common for [[_content/dictionary#R|REST]] services to allow multiple response types (e.g. application/xml or application/json, and the client specifies the preferred order of response types by the Accept header in the request.

- Do [[_content/dictionary#N|NOT]] simply copy the Accept header to the Content-type header of the response.
- Reject the request (ideally with a 406 Not Acceptable response) if the Accept header does not specifically contain one of the allowable types.

Services including script code (e.g. [[_content/dictionary#J|JavaScript]]) in their responses must be especially careful to defend against header injection attack.

- Ensure sending intended content type headers in your response matching your body content e.g. application/json and not application/javascript.

### Management endpoints¶

- Avoid exposing management endpoints via Internet.
- If management endpoints must be accessible via the Internet, make sure that users must use a strong authentication mechanism, e.g. multi-factor.
- Expose management endpoints via different [[_content/dictionary#H|HTTP]] ports or hosts preferably on a different [[_content/dictionary#N|NIC]] and restricted subnet.
- Restrict access to these endpoints by firewall rules  or use of access control lists.

### Error handling¶

- Respond with generic error messages - avoid revealing details of the failure unnecessarily.
- Do not pass technical details (e.g. call stacks or other internal hints) to the client.

### Audit logs¶

- Write audit logs before and after security related events.
- Consider logging token validation errors in order to detect attacks.
- Take care of log injection attacks by sanitizing log data beforehand.

### Security Headers¶
There are a number of [security related headers](https://owasp.org/www-project-secure-headers/) that can be returned in the [[_content/dictionary#H|HTTP]] responses to instruct browsers to act in specific ways. However, some of these headers are intended to be used with [[_content/dictionary#H|HTML]] responses, and as such may provide little or no security benefits on an [[_content/dictionary#A|API]] that does not return HTML.
The following headers should be included in all API responses:

Header
Rationale

Cache-Control: no-store
Header used to direct caching done by browsers. Providing no-store indicates that any caches of any kind (private or shared) should not store the response that contains the header. A browser must make a new request everytime the [[_content/dictionary#A|API]] is called to fetch the latest response. This header with a no-store value prevents sensitive information from being cached or stored.

Content-Security-Policy: frame-ancestors 'none'
Header used to specify whether a response can be framed in a <frame>, <iframe>, <embed> or <object> element. For an [[_content/dictionary#A|API]] response, there is no requirement to be framed in any of those elements. Providing frame-ancestors 'none' prevents any domain from framing the response returned by the API call. This header protects against [[drag-and-drop](https://www.w3.org/Security/wiki/Clickjacking_Threats#Drag_and_drop_attacks)](https://www.w3.org/Security/wiki/Clickjacking_Threats#Drag_and_drop_attacks) style clickjacking attacks.

Content-Type
Header to specify the content type of a response. This must be specified as per the type of content returned by an [[_content/dictionary#A|API]] call. If not specified or if specified incorrectly, a browser might attempt to guess the content type of the response. This can return in [[_content/dictionary#M|MIME]] sniffing attacks. One common content type value is application/json if the API response is [[_content/dictionary#J|JSON]].

Strict-Transport-Security
Header to instruct a browser that the domain should only be accessed using [[_content/dictionary#H|HTTPS]], and that any future attempts to access it using [[_content/dictionary#H|HTTP]] should automatically be converted to HTTPS. This header ensures that [[_content/dictionary#A|API]] calls are made over HTTPS and protects against spoofed certificates.

X-Content-Type-Options: nosniff
Header to instruct a browser to always use the [[_content/dictionary#M|MIME]] type that is declared in the Content-Type header rather than trying to determine the MIME type based on the file's content. This header with a nosniff value prevents browsers from performing MIME sniffing, and inappropriately interpreting responses as [[_content/dictionary#H|HTML]].

X-Frame-Options: [[_content/dictionary#D|DENY]]
Header used to specify whether a response can be framed in a <frame>, <iframe>, <embed> or <object> element. For an [[_content/dictionary#A|API]] response, there is no requirement to be framed in any of those elements. Providing DENY prevents any domain from framing the response returned by the API call. This header with a DENY value protects protect against drag-and-drop style clickjacking attacks.

The headers below are only intended to provide additional security when responses are rendered as [[_content/dictionary#H|HTML]]. As such, if the [[_content/dictionary#A|API]] will never return HTML in responses, then these headers may not be necessary. However, if there is any uncertainty about the function of the headers, or the types of information that the API returns (or may return in future), then it is recommended to include them as part of a defence-in-depth approach.

Header
Example
Rationale

Content-Security-Policy
Content-Security-Policy: default-src 'none'
The majority of [[_content/dictionary#C|CSP]] functionality only affects pages rendered as [[_content/dictionary#H|HTML]].

Permissions-Policy
Permissions-Policy: accelerometer=(), ambient-light-sensor=(), autoplay=(), battery=(), camera=(), cross-origin-isolated=(), display-capture=(), document-domain=(), encrypted-media=(), execution-while-not-rendered=(), execution-while-out-of-viewport=(), fullscreen=(), geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(), midi=(), navigation-override=(), payment=(), picture-in-picture=(), publickey-credentials-get=(), screen-wake-lock=(), sync-xhr=(), usb=(), web-share=(), xr-spatial-tracking=()
This header used to be named Feature-Policy. When browsers heed this header, it is used to control browser features via directives. The example disables features with an empty allowlist for a number of permitted [directive names](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Permissions-Policy#directives). When you apply this header, verify that the directives are up-to-date and fit your needs. Please have a look at this [article](https://developer.chrome.com/en/docs/privacy-sandbox/permissions-policy) for a detailed explanation on how to control browser features.

Referrer-Policy
Referrer-Policy: no-referrer
Non-[[_content/dictionary#H|HTML]] responses should not trigger additional requests.

### [[_content/dictionary#C|CORS]]¶
Cross-Origin Resource Sharing (CORS) is a W3C standard to flexibly specify what cross-domain requests are permitted. By delivering appropriate CORS Headers your [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]] signals to the browser which domains, [[_content/dictionary#A|AKA]] origins, are allowed to make [[_content/dictionary#J|JavaScript]] calls to the REST service.

- Disable [[_content/dictionary#C|CORS]] headers if cross-domain calls are not supported/expected.
- Be as specific as possible and as general as necessary when setting the origins of cross-domain calls.

### Sensitive information in [[_content/dictionary#H|HTTP]] requests¶
RESTful web services should be careful to prevent leaking credentials. Passwords, security tokens, and [[_content/dictionary#A|API]] keys should not appear in the [[_content/dictionary#U|URL]], as this can be captured in web server logs, which makes them intrinsically valuable.

- In [[_content/dictionary#P|POST]]/[[_content/dictionary#P|PUT]] requests sensitive data should be transferred in the request body or request headers.
- In [[_content/dictionary#G|GET]] requests sensitive data should be transferred in an [[_content/dictionary#H|HTTP]] Header.

[[_content/dictionary#O|OK]]:
https://example.com/resourceCollection/[ID]/action
https://twitter.com/vanderaj/lists
[[_content/dictionary#N|NOT]] OK:
https://example.com/controller/123/action?apiKey=a53f435643de32 because the apiKey is in the [[_content/dictionary#U|URL]].
### [[_content/dictionary#H|HTTP]] Return Code¶
HTTP defines [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). When designing [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]], don't just use 200 for success or 404 for error. Always use the semantically appropriate status code for the response.
Here is a non-exhaustive selection of security related REST API status codes. Use it to ensure you return the correct code.

Code
Message
Description

200
[[_content/dictionary#O|OK]]
Response to a successful [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]] action. The [[_content/dictionary#H|HTTP]] method can be [[_content/dictionary#G|GET]], [[_content/dictionary#P|POST]], [[_content/dictionary#P|PUT]], [[_content/dictionary#P|PATCH]] or [[_content/dictionary#D|DELETE]].

201
Created
The request has been fulfilled and resource created. A [[_content/dictionary#U|URI]] for the created resource is returned in the Location header.

202
Accepted
The request has been accepted for processing, but processing is not yet complete.

301
Moved Permanently
Permanent redirection.

304
Not Modified
Caching related response that returned when the client has the same copy of the resource as the server.

307
Temporary Redirect
Temporary redirection of resource.

400
Bad Request
The request is malformed, such as message body format error.

401
Unauthorized
Wrong or no authentication ID/password provided.

403
Forbidden
It's used when the authentication succeeded but authenticated user doesn't have permission to the request resource.

404
Not Found
When a non-existent resource is requested.

405
Method Not Acceptable
The error for an unexpected [[_content/dictionary#H|HTTP]] method. For example, the [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]] is expecting HTTP [[_content/dictionary#G|GET]], but HTTP [[_content/dictionary#P|PUT]] is used.

406
Unacceptable
The client presented a content type in the Accept header which is not supported by the server [[_content/dictionary#A|API]].

413
Payload too large
Use it to signal that the request size exceeded the given limit e.g. regarding file uploads.

415
Unsupported Media Type
The requested content type is not supported by the [[_content/dictionary#R|REST]] service.

429
Too Many Requests
The error is used when there may be [[_content/dictionary#D|DOS]] attack detected or the request is rejected due to rate limiting.

500
Internal Server Error
An unexpected condition prevented the server from fulfilling the request. Be aware that the response should not reveal internal  information that helps an attacker, e.g. detailed error messages or  stack traces.

501
Not Implemented
The [[_content/dictionary#R|REST]] service does not implement the requested operation yet.

503
Service Unavailable
The [[_content/dictionary#R|REST]] service is temporarily unable to process the request. Used to inform the client it should retry at a later time.

Additional information about [[_content/dictionary#H|HTTP]] return code usage in [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]] can be found here and here.