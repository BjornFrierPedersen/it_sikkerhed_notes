---
title: "AJAX Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html"
created: "1741872881.716173"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#A|AJAX]] Security

## [[_content/dictionary#A|AJAX]] Security Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[¶](#use-json-and-xml-schema-for-webservices)](#avoid-building-xml-or-json-by-hand-use-the-framework)](#services-can-be-called-by-users-directly)](#avoid-writing-serialization-code-server-side)](#always-return-json-with-an-object-on-the-outside)](#review-angularjs-json-hijacking-defense-mechanism)](#protect-against-json-hijacking-for-older-browsers)](#use-csrf-protection)](#server-side)](#dont-perform-security-impacting-logic-on-client-side)](#dont-perform-encryption-in-client-side-code)](#never-transmit-secrets-to-the-client)](#avoid-building-xml-or-json-dynamically)](#avoid-writing-serialization-code)](#dont-rely-on-client-business-logic)](#dont-rely-on-client-logic-for-security)](#canonicalize-data-to-consumer-read-encode-before-use)](#dont-use-eval-new-function-or-other-code-evaluation-tools)](#use-innertext-instead-of-innerhtml)](#client-side-javascript)](#introduction)](#ajax-security-cheat-sheet)
### Introduction¶
This document will provide a starting point for AJAX security and will hopefully be updated and expanded reasonably often to provide more detailed information about specific frameworks and technologies.
#### Client Side ([[_content/dictionary#J|JavaScript]])¶
##### Use .innerText instead of .innerHTML¶
The use of .innerText will prevent most [[_content/dictionary#X|XSS]] problems as it will automatically encode the text.
##### Don't use eval(), new Function() or other code evaluation tools¶
eval() function is evil, never use it. Needing to use eval usually indicates a problem in your design.
##### Canonicalize data to consumer (read: encode before use)¶
When using data to build [[_content/dictionary#H|HTML]], script, [[_content/dictionary#C|CSS]], XML, JSON, etc. make sure you take into account how that data must be presented in a literal sense to keep its logical meaning.
Data should be properly encoded before used in this manner to prevent injection style issues, and to make sure the logical meaning is preserved.
[Check out the [[_content/dictionary#O|OWASP]] Java Encoder Project.](https://owasp.org/www-project-java-encoder/)
##### Don't rely on client logic for security¶
Don't forget that the user controls the client-side logic. A number of browser plugins are available to set breakpoints, skip code, change values, etc. Never rely on client logic for security.
##### Don't rely on client business logic¶
Just like the security one, make sure any interesting business rules/logic is duplicated on the server side lest a user bypasses needed logic and does something silly, or worse, costly.
##### Avoid writing serialization code¶
This is hard and even a small mistake can cause large security issues. There are already a lot of frameworks to provide this functionality.
Take a look at the [JSON page](http://www.json.org/) for links.
##### Avoid building [[_content/dictionary#X|XML]] or [[_content/dictionary#J|JSON]] dynamically¶
Just like building HTML or [[_content/dictionary#S|SQL]] you will cause XML injection bugs, so stay away from this or at least use an encoding library or safe JSON or XML library to make attributes and element data safe.

[[Cross_Site_Scripting_Prevention_Cheat_Sheet|- [[_content/dictionary#X|XSS]] (Cross Site Scripting) Prevention]]
[[SQL_Injection_Prevention_Cheat_Sheet|- [[_content/dictionary#S|SQL]] Injection Prevention]]

##### Never transmit secrets to the client¶
Anything the client knows the user will also know, so keep all that secret stuff on the server please.
##### Don't perform encryption in client side code¶
Use [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]] and encrypt on the server!
##### Don't perform security impacting logic on client side¶
This is the overall one that gets me out of trouble in case I missed something :)
#### Server Side¶
##### Use [[_content/dictionary#C|CSRF]] Protection¶
Take a look at the [[Cross-Site_Request_Forgery_Prevention_Cheat_Sheet|Cross-Site Request Forgery (CSRF) Prevention]] cheat sheet.
##### Protect against [[_content/dictionary#J|JSON]] Hijacking for Older Browsers¶
###### Review AngularJS [[_content/dictionary#J|JSON]] Hijacking Defense Mechanism¶
See the [JSON Vulnerability Protection](https://docs.angularjs.org/api/ng/service/$http#json-vulnerability-protection) section of the AngularJS documentation.
###### Always return [[_content/dictionary#J|JSON]] with an Object on the outside¶
Always have the outside primitive be an object for JSON strings:
Exploitable:
[{"object": "inside an array"}]

Not exploitable:
{"object": "not inside an array"}

Also not exploitable:
{"result": [{"object": "inside an array"}]}

##### Avoid writing serialization code Server Side¶
Remember ref vs. value types! Look for an existing library that has been reviewed.
##### Services can be called by users directly¶
Even though you only expect your [[_content/dictionary#A|AJAX]] client side code to call those services the users can too.
Make sure you validate inputs and treat them like they are under user control (because they are!).
##### Avoid building [[_content/dictionary#X|XML]] or [[_content/dictionary#J|JSON]] by hand, use the framework¶
Use the framework and be safe, do it by hand and have security issues.
##### Use [[_content/dictionary#J|JSON]] And [[_content/dictionary#X|XML]] Schema for Webservices¶
You need to use a third-party library to validate web services.