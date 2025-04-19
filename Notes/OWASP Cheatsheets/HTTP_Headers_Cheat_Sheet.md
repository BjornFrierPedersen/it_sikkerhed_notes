---
title: "HTTP Headers Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html"
created: "1741872881.8991263"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#H|HTTP]] Headers

## [[_content/dictionary#H|HTTP]] Security Response Headers Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#references)](#smartscanner)](#mozilla-observatory)](#testing-proper-implementation-of-security-headers)](#express)](#nginx)](#haproxy)](#iis)](#apache)](#php)](#adding-http-headers-in-different-technologies)](#recommendation_20)](#public-key-pins-hpkp)](#recommendation_19)](#x-dns-prefetch-control)](#recommendation_18)](#x-aspnetmvc-version)](#recommendation_17)](#x-aspnet-version)](#recommendation_16)](#x-powered-by)](#recommendation_15)](#server)](#recommendation_14)](#floc-federated-learning-of-cohorts)](#recommendation_13)](#permissions-policy-formerly-feature-policy)](#recommendation_12)](#cross-origin-resource-policy-corp)](#recommendation_11)](#cross-origin-embedder-policy-coep)](#recommendation_10)](#cross-origin-opener-policy-coop)](#recommendation_9)](#access-control-allow-origin)](#recommendation_8)](#content-security-policy-csp)](#recommendation_7)](#expect-ct)](#recommendation_6)](#strict-transport-security-hsts)](#recommendation_5)](#set-cookie)](#recommendation_4)](#content-type)](#recommendation_3)](#referrer-policy)](#recommendation_2)](#x-content-type-options)](#recommendation_1)](#x-xss-protection)](#recommendation)](#x-frame-options)](#security-headers)](#introduction)](#http-security-response-headers-cheat-sheet)
### Introduction¶
HTTP Headers are a great booster for web security with easy implementation. Proper HTTP response headers can help prevent security vulnerabilities like Cross-Site Scripting, Clickjacking, Information disclosure and more.
In this cheat sheet, we will review all security-related HTTP headers, recommended configurations, and reference other [[source](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/HTTP/Headers/X-[[_content/dictionary#X|XSS]]-Protection)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)s for complicated headers.
### Security Headers¶
#### X-Frame-Options¶
The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame>, <iframe>, <embed> or <object>. Sites can use this to avoid [clickjacking](https://owasp.org/www-community/attacks/Clickjacking) attacks, by ensuring that their content is not embedded into other sites.
Content Security Policy ([[_content/dictionary#C|CSP]]) frame-ancestors directive obsoletes X-Frame-Options for supporting browsers (source).
X-Frame-Options header is only useful when the HTTP response where it is included has something to interact with (e.g. links, buttons). If the HTTP response is a redirect or an [[_content/dictionary#A|API]] returning [[_content/dictionary#J|JSON]] data, X-Frame-Options does not provide any security.
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### Recommendation¶
Use Content Security Policy (CSP) frame-ancestors directive if possible.
Do not allow displaying of the page in a frame.

X-Frame-Options: [[_content/dictionary#D|DENY]]

#### X-[[_content/dictionary#X|XSS]]-Protection¶
The [[_content/dictionary#H|HTTP]] X-XSS-Protection response header is a feature of Internet Explorer, Chrome, and Safari that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.
[[_content/dictionary#W|WARNING]]: Even though this header can protect users of older web browsers that don't yet support [[_content/dictionary#C|CSP]], in some cases, this header can create XSS vulnerabilities in otherwise safe websites source.
Recommendation¶
Use a Content Security Policy (CSP) that disables the use of inline [[_content/dictionary#J|JavaScript]].
Do not set this header or explicitly turn it off.

X-[[_content/dictionary#X|XSS]]-Protection: 0

Please see [[Mozilla](https://blog.mozilla.org/en/privacy-security/privacy-analysis-of-floc/) X-[[_content/dictionary#X|XSS]]-Protection](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/X-XSS-Protection) for details.
#### X-Content-Type-Options¶
The X-Content-Type-Options response HTTP header is used by the server to indicate to the browsers that the [[[_content/dictionary#M|MIME]] types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) advertised in the Content-Type headers should be followed and not guessed.
This header is used to block browsers' [MIME type sniffing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types#mime_sniffing), which can transform non-executable MIME types into executable MIME types ([MIME Confusion Attacks](https://blog.mozilla.org/security/2016/08/26/mitigating-mime-confusion-attacks-in-firefox/)).
Recommendation¶
Set the Content-Type header correctly throughout the site.

X-Content-Type-Options: nosniff

#### Referrer-Policy¶
The Referrer-Policy [[_content/dictionary#H|HTTP]] header controls how much referrer information (sent via the Referer header) should be included with requests.
Recommendation¶
Referrer policy has been supported by browsers since 2014. Today, the default behavior in modern browsers is to no longer send all referrer information (origin, path, and query string) to the same site but to only send the origin to other sites. However, since not all users may be using the latest browsers we suggest forcing this behavior by sending this header on all responses.

Referrer-Policy: strict-origin-when-cross-origin

[[_content/dictionary#N|NOTE]]: For more information on configuring this header please see [Mozilla Referrer-Policy](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Referrer-Policy).

#### Content-Type¶
The Content-Type representation header is used to indicate the original media type of the resource (before any content encoding is applied for sending). If not set correctly, the resource (e.g. an image) may be interpreted as [[_content/dictionary#H|HTML]], making [[_content/dictionary#X|XSS]] vulnerabilities possible.
Although it is recommended to always set the Content-Type header correctly, it would constitute a vulnerability only if the content is intended to be rendered by the client and the resource is untrusted (provided or modified by a user).
Recommendation¶

Content-Type: text/html; charset=[[_content/dictionary#U|UTF]]-8

- [[_content/dictionary#N|NOTE]]: the charset attribute is necessary to prevent [[_content/dictionary#X|XSS]] in [[_content/dictionary#H|HTML]] pages
- [[_content/dictionary#N|NOTE]]: the text/html can be any of the possible [[_content/dictionary#M|MIME]] types

#### Set-Cookie¶
The Set-Cookie [[_content/dictionary#H|HTTP]] response header is used to send a cookie from the server to the user agent, so the user agent can send it back to the server later. To send multiple cookies, multiple Set-Cookie headers should be sent in the same response.
This is not a security header per se, but its security attributes are crucial.
Recommendation¶

Please read [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#cookies) for a detailed explanation on cookie configuration options.

#### Strict-Transport-Security ([[_content/dictionary#H|HSTS]])¶
The [[_content/dictionary#H|HTTP]] Strict-Transport-Security response header (often abbreviated as HSTS) lets a website tell browsers that it should only be accessed using [[_content/dictionary#H|HTTPS]], instead of using HTTP.
Recommendation¶

Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

- [[_content/dictionary#N|NOTE]]: Read carefully how this header works before using it. If the [[_content/dictionary#H|HSTS]] header is misconfigured or if there is a problem with the [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] certificate being used, legitimate users might be unable to access the website. For example, if the HSTS header is set to a very long duration and the [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] certificate expires or is revoked, legitimate users might be unable to access the website until the HSTS header duration has expired.

Please checkout [[HTTP_Strict_Transport_Security_Cheat_Sheet|[[_content/dictionary#H|HTTP]] Strict Transport Security Cheat Sheet]] for more information.
#### Expect-[[_content/dictionary#C|CT]] ❌¶
The Expect-CT header lets sites opt-in to reporting of Certificate Transparency (CT) requirements. Given that mainstream clients now require CT qualification, the only remaining value is reporting such occurrences to the nominated report-uri value in the header. The header is now less about enforcement and more about detection/reporting.
Recommendation¶
Do not use it. Mozilla [recommends](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/HTTP/Headers/Expect-CT) avoiding it, and removing it from existing code if possible.
#### Content-Security-Policy ([[_content/dictionary#C|CSP]])¶
Content Security Policy (CSP) is a security feature that is used to specify the origin of content that is allowed to be loaded on a website or in a web applications. It is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross-Site Scripting ([[_content/dictionary#X|XSS]]) and data injection attacks. These attacks are used for everything from data theft to site defacement to distribution of malware.

- [[_content/dictionary#N|NOTE]]: This header is relevant to be applied in pages which can load and interpret scripts and code, but might be meaningless in the response of a [[_content/dictionary#R|REST]] [[_content/dictionary#A|API]] that returns content that is not going to be rendered.

Recommendation¶
Content Security Policy is complex to configure and maintain. For an explanation on customization options, please read [[Content_Security_Policy_Cheat_Sheet|Content Security Policy Cheat Sheet]]
#### [Access-Control-Allow-Origin](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Access-Control-Allow-Origin)¶
If you don't use this header, your site is protected by default by the Same Origin Policy ([[_content/dictionary#S|SOP]]). What this header does is relax this control in specified circumstances.
The Access-Control-Allow-Origin is a [[_content/dictionary#C|CORS]] (cross-origin resource sharing) header. This header indicates whether the response it is related to can be shared with requesting code from the given origin. In other words, if siteA requests a resource from siteB, siteB should indicate in its Access-Control-Allow-Origin header that siteA is allowed to fetch that resource, if not, the access is blocked due to Same Origin Policy (SOP).
Recommendation¶
If you use it, set specific [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin) instead of *. Checkout Access-Control-Allow-Origin for details.

Access-Control-Allow-Origin: https://yoursite.com

- [[_content/dictionary#N|NOTE]]: The use of '*' might be necessary depending on your needs. For example, for a public [[_content/dictionary#A|API]] that should be accessible from any origin, it might be necessary to allow '*'.

#### Cross-Origin-Opener-Policy ([[_content/dictionary#C|COOP]])¶
The [[_content/dictionary#H|HTTP]] Cross-Origin-Opener-Policy (COOP) response header allows you to ensure a top-level document does not share a browsing context group with cross-origin documents.
This header works together with Cross-Origin-Embedder-Policy ([[_content/dictionary#C|COEP]]) and Cross-Origin-Resource-Policy ([[[_content/dictionary#C|CORP]]](#cross-origin-resource-policy)) explained below.
This mechanism protects against attacks like [Spectre](https://meltdownattack.com/) which can cross the security boundary established by Same Origin Policy ([[_content/dictionary#S|SOP]]) for resources in the same browsing context group.
As this headers are very related to browsers, it may not make sense to be applied to [[_content/dictionary#R|REST]] APIs or clients that are not browsers.
Recommendation¶
Isolates the browsing context exclusively to same-origin documents.

Cross-Origin-Opener-Policy: same-origin

#### Cross-Origin-Embedder-Policy ([[_content/dictionary#C|COEP]])¶
The [[_content/dictionary#H|HTTP]] Cross-Origin-Embedder-Policy (COEP) response header prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using [[_content/dictionary#C|CORP]] or [[_content/dictionary#C|CORS]]).

- [[_content/dictionary#N|NOTE]]: Enabling this will block cross-origin resources not configured correctly from loading.

Recommendation¶
A document can only load resources from the same origin, or resources explicitly marked as loadable from another origin.

Cross-Origin-Embedder-Policy: require-corp

- [[_content/dictionary#N|NOTE]]: you can bypass it for specific resources by adding the crossorigin attribute:
- <img src="https://thirdparty.com/img.png" crossorigin>

#### Cross-Origin-Resource-Policy ([[_content/dictionary#C|CORP]])¶
The Cross-Origin-Resource-Policy (CORP) header allows you to control the set of origins that are empowered to include a resource. It is a robust defense against attacks like Spectre, as it allows browsers to block a given response before it enters an attacker's process.
Recommendation¶
Limit current resource loading to the site and sub-domains only.

Cross-Origin-Resource-Policy: same-site

#### [Permissions-Policy](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Permissions-Policy) (formerly Feature-Policy)¶
Permissions-Policy allows you to control which origins can use which browser features, both in the top-level page and in embedded frames. For every feature controlled by Feature Policy, the feature is only enabled in the current document or frame if its origin matches the allowed list of origins. This means that you can configure your site to never allow the camera or microphone to be activated. This prevents that an injection, for example an [[_content/dictionary#X|XSS]], enables the camera, the microphone, or other browser feature.
More information: Permissions-Policy
Recommendation¶
Set it and disable all the features that your site does not need or allow them only to the authorized domains:

Permissions-Policy: geolocation=(), camera=(), microphone=()

- [[_content/dictionary#N|NOTE]]: This example is disabling geolocation, camera, and microphone for all domains.

#### FLoC (Federated Learning of Cohorts)¶
FLoC is a method proposed by Google in 2021 to deliver interest-based advertisements to groups of users ("cohorts"). The [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2021/03/googles-floc-terrible-idea), Mozilla, and others believe FLoC does not do enough to protect users' privacy.
Recommendation¶
A site can declare that it does not want to be included in the user's list of sites for cohort calculation by sending this [[_content/dictionary#H|HTTP]] header.

Permissions-Policy: interest-cohort=()

#### Server¶
The Server header describes the software used by the origin server that handled the request — that is, the server that generated the response.
This is not a security header, but how it is used is relevant for security.
Recommendation¶
Remove this header or set non-informative values.

Server: webserver

- [[_content/dictionary#N|NOTE]]: Remember that attackers have other means of fingerprinting the server technology.

#### X-Powered-By¶
The X-Powered-By header describes the technologies used by the webserver. This information exposes the server to attackers. Using the information in this header, attackers can find vulnerabilities easier.
Recommendation¶
Remove all X-Powered-By headers.

- - - [[_content/dictionary#N|NOTE]]: Remember that attackers have other means of fingerprinting your tech stack.

#### X-[[_content/dictionary#A|AspNet]]-Version¶
Provides information about the .[[_content/dictionary#N|NET]] version.
Recommendation¶
Disable sending this header. Add the following line in your web.config in the <system.web> section to remove it.
<httpRuntime enableVersionHeader="false" />

[[_content/dictionary#N|NOTE]]: Remember that attackers have other means of fingerprinting your tech stack.

#### X-[[_content/dictionary#A|AspNetMvc]]-Version¶
Provides information about the .[[_content/dictionary#N|NET]] version.
Recommendation¶
Disable sending this header. To remove the X-AspNetMvc-Version header, add the below line in Global.asax file.
[[_content/dictionary#M|MvcHandler]].[[_content/dictionary#D|DisableMvcResponseHeader]] = true;

[[_content/dictionary#N|NOTE]]: Remember that attackers have other means of fingerprinting your tech stack.

#### X-[[_content/dictionary#D|DNS]]-Prefetch-Control¶
The X-DNS-Prefetch-Control [[_content/dictionary#H|HTTP]] response header controls DNS prefetching, a feature by which browsers proactively perform domain name resolution on both links that the user may choose to follow as well as URLs for items referenced by the document, including images, [[_content/dictionary#C|CSS]], [[_content/dictionary#J|JavaScript]], and so forth.
Recommendation¶
The default behavior of browsers is to perform DNS caching which is good for most websites.
If you do not control links on your website, you might want to set off as a value to disable DNS prefetch to avoid leaking information to those domains.

X-[[_content/dictionary#D|DNS]]-Prefetch-Control: off

- [[_content/dictionary#N|NOTE]]: Do not rely in this functionality for anything production sensitive: it is not standard or fully supported and implementation may vary among browsers.

#### Public-Key-Pins ([[_content/dictionary#H|HPKP]])¶
The HTTP Public-Key-Pins response header is used to associate a specific cryptographic public key with a certain web server to decrease the risk of [[_content/dictionary#M|MITM]] attacks with forged certificates.
Recommendation¶
This header is deprecated and should not be used anymore.
### Adding [[_content/dictionary#H|HTTP]] Headers in Different Technologies¶
#### [[_content/dictionary#P|PHP]]¶
The sample code below sets the X-Frame-Options header in PHP.
header("X-Frame-Options: [[_content/dictionary#D|DENY]]");

#### Apache¶
Below is an .htaccess sample configuration which sets the X-Frame-Options header in Apache. Note that without the always option, the header will only be sent for certain status codes, as described in [the Apache documentation](https://httpd.apache.org/docs/2.4/mod/mod_headers.html#header).
<[[_content/dictionary#I|IfModule]] mod_headers.c>
Header always set X-Frame-Options "[[_content/dictionary#D|DENY]]"
</IfModule>

#### [[_content/dictionary#I|IIS]]¶
Add configurations below to your Web.config in IIS to send the X-Frame-Options header.
<system.webServer>
...
 <httpProtocol>
   <customHeaders>
     <add name="X-Frame-Options" value="[[_content/dictionary#D|DENY]]" />
   </customHeaders>
 </httpProtocol>
...
</system.webServer>

#### HAProxy¶
Add the line below to your front-end, listen, or backend configurations to send the X-Frame-Options header.
http-response set-header X-Frame-Options [[_content/dictionary#D|DENY]]

#### Nginx¶
Below is a sample configuration, it sets the X-Frame-Options header in Nginx. Note that without the always option, the header will only be sent for certain status codes, as described in [the nginx documentation](https://nginx.org/en/docs/http/ngx_http_headers_module.html#add_header).
add_header "X-Frame-Options" "[[_content/dictionary#D|DENY]]" always;

#### Express¶
You can use [helmet](https://www.npmjs.com/package/helmet) to setup [[_content/dictionary#H|HTTP]] headers in Express. The code below is sample for adding the X-Frame-Options header.
const helmet = require('helmet');
const app = express();
// Sets "X-Frame-Options: [[_content/dictionary#S|SAMEORIGIN]]"
app.use(
 helmet.frameguard({
   action: "sameorigin",
 })
);

### Testing Proper Implementation of Security Headers¶
#### [Mozilla Observatory](https://observatory.mozilla.org/)¶
The Mozilla Observatory is an online tool which helps you to check your website's header status.
#### [[[_content/dictionary#S|SmartScanner]]](https://www.thesmartscanner.com/)¶
SmartScanner has a dedicated [test profile](https://www.thesmartscanner.com/docs/configuring-security-tests) for testing security of [[_content/dictionary#H|HTTP]] headers.
Online tools usually test the homepage of the given address. But SmartScanner scans the whole website. So, you can make sure all of your web pages have the right HTTP Headers in place.
### References¶

[- Mozilla: X-Frame-Options](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/X-Frame-Options)
[- Mozilla: X-[[_content/dictionary#X|XSS]]-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)
[- hstspreload.org](https://hstspreload.org/)
[- Mozilla: Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
[- Mozilla: Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)
[- Mozilla: Expect-[[_content/dictionary#C|CT]]](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect-CT)
[- Mozilla: Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
[- content-security-policy.com](https://content-security-policy.com/)
[- Mozilla: Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)
[- resourcepolicy.fyi](https://resourcepolicy.fyi/)
[- Mozilla: Cross-Origin-Resource-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy)
[- Mozilla: Cross-Origin-Embedder-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy)
[- Mozilla: Server Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server)
[- Linked [[_content/dictionary#O|OWASP]] project: Secure Headers Project](https://owasp.org/www-project-secure-headers/)