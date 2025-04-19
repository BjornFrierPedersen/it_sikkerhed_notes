---
title: "HTTP Strict Transport Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html"
created: "1741872881.9043517"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#H|HTTP]] Strict Transport Security

## [[_content/dictionary#H|HTTP]] [Strict Transport Security](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/HTTP/Headers/Strict-Transport-Security) Cheat Sheet[[[[[[[¶](#references)](#browser-support)](#problems)](#examples)](#threats)](#introduction)](#http-strict-transport-security-cheat-sheet)
### Introduction¶
HTTP Strict Transport Security (also named [[_content/dictionary#H|HSTS]]) is an opt-in security enhancement that is specified by a web application through the use of a special response header. Once a supported browser receives this header that browser will prevent any communications from being sent over HTTP to the specified domain and will instead send all communications over [[_content/dictionary#H|HTTPS]]. It also prevents HTTPS click through prompts on browsers.
The specification has been released and published end of 2012 as [[[_content/dictionary#R|RFC]] 6797](http://tools.ietf.org/html/rfc6797) (HTTP Strict Transport Security (HSTS)) by the [[_content/dictionary#I|IETF]].
### Threats¶
HSTS addresses the following threats:

- User bookmarks or manually types http://example.com and is subject to a man-in-the-middle attacker
- - - - [[_content/dictionary#H|HSTS]] automatically redirects [[_content/dictionary#H|HTTP]] requests to [[_content/dictionary#H|HTTPS]] for the target domain

- Web application that is intended to be purely [[_content/dictionary#H|HTTPS]] inadvertently contains [[_content/dictionary#H|HTTP]] links or serves content over HTTP
[[_content/dictionary#H|HSTS]] automatically redirects HTTP requests to HTTPS for the target domain

- A man-in-the-middle attacker attempts to intercept traffic from a victim user using an invalid certificate and hopes the user will accept the bad certificate
- - [[_content/dictionary#H|HSTS]] does not allow a user to override the invalid certificate message

### Examples¶
Simple example, using a long (1 year = 31536000 seconds) max-age. This example is dangerous since it lacks includeSubDomains:
Strict-Transport-Security: max-age=31536000
This example is useful if all present and future subdomains will be [[_content/dictionary#H|HTTPS]]. This is a more secure option but will block access to certain pages that can only be served over [[_content/dictionary#H|HTTP]]:
Strict-Transport-Security: max-age=31536000; includeSubDomains
This example is useful if all present and future subdomains will be HTTPS. In this example we set a very short max-age in case of mistakes during initial rollout:
Strict-Transport-Security: max-age=86400; includeSubDomains
Recommended:

If the site owner would like their domain to be included in the [[[_content/dictionary#H|HSTS]] preload list](https://hstspreload.org) maintained by Chrome (and used by Firefox and Safari), then use the header below.
Sending the preload directive from your site can have [[_content/dictionary#P|PERMANENT]] [[_content/dictionary#C|CONSEQUENCES]] and prevent users from accessing your site and any of its subdomains if you find you need to switch back to [[_content/dictionary#H|HTTP]]. Please read the details at [preload removal](https://hstspreload.org/#removal) before sending the header with preload.

Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
The preload flag indicates the site owner's consent to have their domain preloaded. The site owner still needs to then go and submit the domain to the list.
### Problems¶
Site owners can use [[_content/dictionary#H|HSTS]] to identify users without cookies. This can lead to a significant privacy leak. Take a look [here](http://www.leviathansecurity.com/blog/the-double-edged-sword-of-hsts-persistence-and-privacy) for more details.
Cookies can be manipulated from sub-domains, so omitting the includeSubDomains option permits a broad range of cookie-related attacks that HSTS would otherwise prevent by requiring a valid certificate for a subdomain. Ensuring the secure flag is set on all cookies will also prevent, some, but not all, of the same attacks.
### Browser Support¶
As of September 2019 HSTS is supported by [all modern browsers](https://caniuse.com/#feat=stricttransportsecurity), with the only notable exception being Opera Mini.
### References¶

[- Chromium Projects/[[_content/dictionary#H|HSTS]]](https://www.chromium.org/hsts/)
[[Transport_Layer_Security_Cheat_Sheet|- [[_content/dictionary#O|OWASP]] [[_content/dictionary#T|TLS]] Protection Cheat Sheet]]
[- sslstrip](https://github.com/moxie0/sslstrip)
[- [[_content/dictionary#A|AppSecTutorial]] Series - Episode 4](https://www.youtube.com/watch?v=zEV3HOuM_Vw)
[- Nmap [[_content/dictionary#N|NSE]] script to detect HSTS configuration](https://github.com/icarot/NSE_scripts/blob/master/http-hsts-verify.nse)