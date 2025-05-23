---
title: "DOM based XSS Prevention Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html"
created: "1741872881.8471942"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#D|DOM]] based [[_content/dictionary#X|XSS]] Prevention

## [[_content/dictionary#D|DOM]] based [[[_content/dictionary#X|XSS]]](https://owasp.org/www-community/attacks/xss/) Prevention Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#detect-dom-xss-using-variant-analysis)](#usually-safe-methods)](#encoding-misconceptions)](#inconsistencies-of-encoding-libraries)](#complex-contexts)](#common-problems-associated-with-mitigating-dom-based-xss)](#guideline-10-dont-eval-json-to-convert-it-to-native-javascript-objects)](#guideline-9-run-your-javascript-in-a-ecmascript-5-[canopy](https://github.com/jcoglan/canopy)-or-sandbox)](#guideline-8-limit-access-to-object-properties-when-using-objectx-accessors)](#guideline-7-when-url-encoding-in-dom-be-aware-of-character-set-issues)](#guideline-6-use-untrusted-data-on-only-the-right-side-of-an-expression)](#n-levels-of-encoding)](#utilizing-an-enclosure-as-suggested-by-gaz)](#guideline-5-avoid-the-numerous-methods-which-implicitly-eval-data-passed-to-it)](#guideline-4-avoid-sending-untrusted-data-into-html-rendering-methods)](#guideline-3-use-documentcreateelement-elementsetattributevalue-elementappendchild-and-similar-to-build-dynamic-interfaces)](#guideline-2-always-javascript-encode-and-delimit-untrusted-data-as-quoted-strings-when-entering-the-application-when-building-templated-javascript)](#guideline-1-untrusted-data-should-only-be-treated-as-displayable-text)](#guidelines-for-developing-secure-applications-utilizing-javascript)](#rule-7-fixing-dom-cross-site-scripting-vulnerabilities)](#rule-6-populate-the-dom-using-safe-javascript-functions-or-properties)](#rule-5-url-escape-then-javascript-escape-before-inserting-untrusted-data-into-url-attribute-subcontext-within-the-execution-context)](#rule-4-javascript-escape-before-inserting-untrusted-data-into-the-css-attribute-subcontext-within-the-execution-context)](#html-encodings-disarming-nature)](#rule-3-be-careful-when-inserting-untrusted-data-into-the-event-handler-and-javascript-code-subcontexts-within-an-execution-context)](#safe-and-functionally-correct-example)](#safe-but-broken-example)](#rule-2-javascript-escape-before-inserting-untrusted-data-into-html-attribute-subcontext-within-the-execution-context)](#guideline)](#methods)](#attributes)](#example-dangerous-html-methods)](#rule-1-html-escape-then-javascript-escape-before-inserting-untrusted-data-into-html-subcontext-within-the-execution-context)](#introduction)](#dom-based-xss-prevention-cheat-sheet)
### Introduction¶
When looking at XSS (Cross-Site Scripting), there are three generally recognized forms of XSS:

[- Reflected or Stored](https://owasp.org/www-community/attacks/xss/#stored-and-reflected-xss-attacks)
[[[_content/dictionary#D|DOM]] Based [[_content/dictionary#X|XSS]]](https://owasp.org/www-community/attacks/DOM_Based_XSS).

The [[Cross_Site_Scripting_Prevention_Cheat_Sheet|[[[_content/dictionary#X|XSS]] Prevention Cheatsheet]]](Cross_Site_Scripting_Prevention_Cheat_Sheet.html) does an excellent job of addressing Reflected and Stored XSS. This cheatsheet addresses [[_content/dictionary#D|DOM]] (Document Object Model) based XSS and is an extension (and assumes comprehension) of the XSS Prevention Cheatsheet.
In order to understand DOM based XSS, one needs to see the fundamental difference between Reflected and Stored XSS when compared to DOM based XSS. The primary difference is where the attack is injected into the application.
Reflected and Stored XSS are server side injection issues while DOM based XSS is a client (browser) side injection issue.
All of this code originates on the server, which means it is the application owner's responsibility to make it safe from XSS, regardless of the type of XSS flaw it is. Also, XSS attacks always execute in the browser.
The difference between Reflected/Stored XSS is where the attack is added or injected into the application. With Reflected/Stored the attack is injected into the application during server-side processing of requests where untrusted input is dynamically added to [[_content/dictionary#H|HTML]]. For DOM XSS, the attack is injected into the application during runtime in the client directly.
When a browser is rendering HTML and any other associated content like [[_content/dictionary#C|CSS]] or [[_content/dictionary#J|JavaScript]], it identifies various rendering contexts for the different kinds of input and follows different rules for each context. A rendering context is associated with the parsing of HTML tags and their attributes.

- The [[_content/dictionary#H|HTML]] parser of the rendering context dictates how data is presented and laid out on the page and can be further broken down into the standard contexts of HTML, HTML attribute, [[_content/dictionary#U|URL]], and [[_content/dictionary#C|CSS]].
- The [[_content/dictionary#J|JavaScript]] or VBScript parser of an execution context is associated with the parsing and execution of script code. Each parser has distinct and separate semantics in the way they can possibly execute script code which make creating consistent rules for mitigating vulnerabilities in various contexts difficult. The complication is compounded by the differing meanings and treatment of encoded values within each subcontext ([[_content/dictionary#H|HTML]], HTML attribute, [[_content/dictionary#U|URL]], and [[_content/dictionary#C|CSS]]) within the execution context.

For the purposes of this article, we refer to the [[_content/dictionary#H|HTML]], HTML attribute, [[_content/dictionary#U|URL]], and [[_content/dictionary#C|CSS]] contexts as subcontexts because each of these contexts can be reached and set within a [[_content/dictionary#J|JavaScript]] execution context.
In JavaScript code, the main context is JavaScript but with the right tags and context closing characters, an attacker can try to attack the other 4 contexts using equivalent JavaScript [[_content/dictionary#D|DOM]] methods.
The following is an example vulnerability which occurs in the JavaScript context and HTML subcontext:
 <script>
 var x = '<%= taintedVar %>';
 var d = document.createElement('div');
 d.innerHTML = x;
 document.body.appendChild(d);
 </script>

Let's look at the individual subcontexts of the execution context in turn.
### [[_content/dictionary#R|RULE]] #1 - [[_content/dictionary#H|HTML]] Escape then [[_content/dictionary#J|JavaScript]] Escape Before Inserting Untrusted Data into HTML Subcontext within the Execution Context¶
There are several methods and attributes which can be used to directly render HTML content within JavaScript. These methods constitute the HTML Subcontext within the Execution Context. If these methods are provided with untrusted input, then an [[_content/dictionary#X|XSS]] vulnerability could result. For example:
#### Example Dangerous [[_content/dictionary#H|HTML]] ##### Methods¶
##### Attributes¶
 element.innerHTML = "<HTML> Tags and markup";
 element.outerHTML = "<HTML> Tags and markup";

Methods¶
 document.write("<[[_content/dictionary#H|HTML]]> Tags and markup");
 document.writeln("<HTML> Tags and markup");

#### Guideline¶
To make dynamic updates to [[_content/dictionary#H|HTML]] in the [[_content/dictionary#D|DOM]] safe, we recommend:

1. [[_content/dictionary#H|HTML]] encoding, and then
2. [[_content/dictionary#J|JavaScript]] encoding all untrusted input, as shown in these examples:

 var [[[_content/dictionary#E|ESAPI]]](https://owasp.org/www-project-enterprise-security-api/) = require('[node-esapi](https://github.com/ESAPI/node-esapi/)');
 element.innerHTML = "<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForHTML(untrustedData))%>";
 element.outerHTML = "<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForHTML(untrustedData))%>";

 var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
 document.write("<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForHTML(untrustedData))%>");
 document.writeln("<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForHTML(untrustedData))%>");

### [[_content/dictionary#R|RULE]] #2 - [[_content/dictionary#J|JavaScript]] Escape Before Inserting Untrusted Data into [[_content/dictionary#H|HTML]] Attribute Subcontext within the Execution Context¶
The HTML attribute subcontext within the execution context is divergent from the standard encoding rules. This is because the rule to HTML attribute encode in an HTML attribute rendering context is necessary in order to mitigate attacks which try to exit out of an HTML attributes or try to add additional attributes which could lead to [[_content/dictionary#X|XSS]].
When you are in a [[_content/dictionary#D|DOM]] execution context you only need to JavaScript encode HTML attributes which do not execute code (attributes other than event handler, [[_content/dictionary#C|CSS]], and [[_content/dictionary#U|URL]] attributes).
For example, the general rule is to HTML Attribute encode untrusted data (data from the database, [[_content/dictionary#H|HTTP]] request, user, back-end system, etc.) placed in an HTML Attribute. This is the appropriate step to take when outputting data in a rendering context, however using HTML Attribute encoding in an execution context will break the application display of data.
#### [[_content/dictionary#S|SAFE]] but [[_content/dictionary#B|BROKEN]] example¶
 var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
 var x = document.createElement("input");
 x.setAttribute("name", "company_name");
 // In the following line of code, companyName represents untrusted user input
 // The ESAPI.encoder().encodeForHTMLAttribute() is unnecessary and causes double-encoding
 x.setAttribute("value", '<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForHTMLAttribute(companyName))%>');
 var form1 = document.forms[0];
 form1.appendChild(x);

The problem is that if companyName had the value "Johnson & Johnson". What would be displayed in the input text field would be "Johnson &amp; Johnson". The appropriate encoding to use in the above case would be only [[_content/dictionary#J|JavaScript]] encoding to disallow an attacker from closing out the single quotes and in-lining code, or escaping to [[_content/dictionary#H|HTML]] and opening a new script tag.
#### [[_content/dictionary#S|SAFE]] and [[_content/dictionary#F|FUNCTIONALLY]] [[_content/dictionary#C|CORRECT]] example¶
 var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
 var x = document.createElement("input");
 x.setAttribute("name", "company_name");
 x.setAttribute("value", '<%=ESAPI.encoder().encodeForJavascript(companyName)%>');
 var form1 = document.forms[0];
 form1.appendChild(x);

It is important to note that when setting an [[_content/dictionary#H|HTML]] attribute which does not execute code, the value is set directly within the object attribute of the HTML element so there is no concerns with injecting up.
### [[_content/dictionary#R|RULE]] #3 - Be Careful when Inserting Untrusted Data into the Event Handler and [[_content/dictionary#J|JavaScript]] code Subcontexts within an Execution Context¶
Putting dynamic data within JavaScript code is especially dangerous because JavaScript encoding has different semantics for JavaScript encoded data when compared to other encodings. In many cases, JavaScript encoding does not stop attacks within an execution context. For example, a JavaScript encoded string will execute even though it is JavaScript encoded.
Therefore, the primary recommendation is to avoid including untrusted data in this context. If you must, the following examples describe some approaches that do and do not work.
var x = document.createElement("a");
x.href="#";
// In the line of code below, the encoded data on the right (the second argument to setAttribute)
// is an example of untrusted data that was properly JavaScript encoded but still executes.
x.setAttribute("onclick", "\u0061\u006c\u0065\u0072\u0074\u0028\u0032\u0032\u0029");
var y = document.createTextNode("Click To Test");
x.appendChild(y);
document.body.appendChild(x);

The setAttribute(name_string,value_string) method is dangerous because it implicitly coerces the value_string into the [[_content/dictionary#D|DOM]] attribute datatype of name_string.
In the case above, the attribute name is an [[_content/dictionary#J|JavaScript]] event handler, so the attribute value is implicitly converted to JavaScript code and evaluated. In the case above, JavaScript encoding does not mitigate against DOM based [[_content/dictionary#X|XSS]].
Other JavaScript methods which take code as a string types will have a similar problem as outline above (setTimeout, setInterval, new Function, etc.). This is in stark contrast to JavaScript encoding in the event handler attribute of a [[_content/dictionary#H|HTML]] tag (HTML parser) where JavaScript encoding mitigates against XSS.
<!-- Does [[_content/dictionary#N|NOT]] work  -->
<a id="bb" href="#" onclick="\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0029"> Test Me</a>

An alternative to using Element.setAttribute(...) to set [[_content/dictionary#D|DOM]] attributes is to set the attribute directly. Directly setting event handler attributes will allow [[_content/dictionary#J|JavaScript]] encoding to mitigate against DOM based [[_content/dictionary#X|XSS]]. Please note, it is always dangerous design to put untrusted data directly into a command execution context.
<a id="bb" href="#"> Test Me</a>

//The following does [[_content/dictionary#N|NOT]] work because the event handler is being set to a string.
//"alert(7)" is [[_content/dictionary#J|JavaScript]] encoded.
document.getElementById("bb").onclick = "\u0061\u006c\u0065\u0072\u0074\u0028\u0037\u0029";

//The following does [[_content/dictionary#N|NOT]] work because the event handler is being set to a string.
document.getElementById("bb").onmouseover = "testIt";

//The following does [[_content/dictionary#N|NOT]] work because of the encoded "(" and ")".
//"alert(77)" is [[_content/dictionary#J|JavaScript]] encoded.
document.getElementById("bb").onmouseover = \u0061\u006c\u0065\u0072\u0074\u0028\u0037\u0037\u0029;

//The following does [[_content/dictionary#N|NOT]] work because of the encoded ";".
//"testIt;testIt" is [[_content/dictionary#J|JavaScript]] encoded.
document.getElementById("bb").onmouseover = \u0074\u0065\u0073\u0074\u0049\u0074\u003b\u0074\u0065\u0073
                                            \u0074\u0049\u0074;

//The following [[_content/dictionary#D|DOES]] [[_content/dictionary#W|WORK]] because the encoded value is a valid variable name or function reference.
//"testIt" is [[_content/dictionary#J|JavaScript]] encoded
document.getElementById("bb").onmouseover = \u0074\u0065\u0073\u0074\u0049\u0074;

function testIt() {
   alert("I was called.");
}

There are other places in [[_content/dictionary#J|JavaScript]] where JavaScript encoding is accepted as valid executable code.
 for(var \u0062=0; \u0062 < 10; \u0062++){
     \u0064\u006f\u0063\u0075\u006d\u0065\u006e\u0074
     .\u0077\u0072\u0069\u0074\u0065\u006c\u006e
     ("\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\u0064");
 }
 \u0077\u0069\u006e\u0064\u006f\u0077
 .\u0065\u0076\u0061\u006c
 \u0064\u006f\u0063\u0075\u006d\u0065\u006e\u0074
 .\u0077\u0072\u0069\u0074\u0065(111111111);

or
 var s = "\u0065\u0076\u0061\u006c";
 var t = "\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0031\u0029";
 window[s](t);

Because [[_content/dictionary#J|JavaScript]] is based on an international standard (ECMAScript), JavaScript encoding enables the support of international characters in programming constructs and variables in addition to alternate string representations (string escapes).
However the opposite is the case with HTML encoding. HTML tag elements are well defined and do not support alternate representations of the same tag. So HTML encoding cannot be used to allow the developer to have alternate representations of the <a> tag for example.
#### [[_content/dictionary#H|HTML]] Encoding's Disarming Nature¶
In general, HTML encoding serves to castrate HTML tags which are placed in HTML and HTML attribute contexts. Working example (no HTML encoding):
<a href="..." >

Normally encoded example (Does Not Work – [[_content/dictionary#D|DNW]]):
&#x3c;a href=... &#x3e;

[[_content/dictionary#H|HTML]] encoded example to highlight a fundamental difference with [[_content/dictionary#J|JavaScript]] encoded values ([[_content/dictionary#D|DNW]]):
<&#x61; href=...>

If [[_content/dictionary#H|HTML]] encoding followed the same semantics as JavaScript encoding, the line above could have possibly worked to render a [link](https://semgrep.dev/s/we30). This difference makes JavaScript encoding a less viable weapon in our fight against [[_content/dictionary#X|XSS]].
### [[_content/dictionary#R|RULE]] #4 - [[_content/dictionary#J|JavaScript]] Escape Before Inserting Untrusted Data into the [[_content/dictionary#C|CSS]] Attribute Subcontext within the Execution Context¶
Normally executing JavaScript from a CSS context required either passing javascript:attackCode() to the CSS url() method or invoking the CSS expression() method passing JavaScript code to be directly executed.
From my experience, calling the expression() function from an execution context (JavaScript) has been disabled. In order to mitigate against the CSS url() method, ensure that you are [[_content/dictionary#U|URL]] encoding the data passed to the CSS url() method.
var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
document.body.style.backgroundImage = "url(<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForURL(companyName))%>)";

### [[_content/dictionary#R|RULE]] #5 - [[_content/dictionary#U|URL]] Escape then [[_content/dictionary#J|JavaScript]] Escape Before Inserting Untrusted Data into URL Attribute Subcontext within the Execution Context¶
The logic which parses URLs in both execution and rendering contexts looks to be the same. Therefore there is little change in the encoding rules for URL attributes in an execution ([[_content/dictionary#D|DOM]]) context.
var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
var x = document.createElement("a");
x.setAttribute("href", '<%=ESAPI.encoder().encodeForJavascript(ESAPI.encoder().encodeForURL(userRelativePath))%>');
var y = document.createTextElement("Click Me To Test");
x.appendChild(y);
document.body.appendChild(x);

If you utilize fully qualified URLs then this will break the links as the colon in the protocol identifier (http: or javascript:) will be [[_content/dictionary#U|URL]] encoded preventing the http and javascript protocols from being invoked.
### [[_content/dictionary#R|RULE]] #6 - Populate the [[_content/dictionary#D|DOM]] using safe [[_content/dictionary#J|JavaScript]] functions or properties¶
The most fundamental safe way to populate the DOM with untrusted data is to use the safe assignment property textContent.
Here is an example of safe usage.
<script>
element.textContent = untrustedData;  //does not execute code
</script>

### [[_content/dictionary#R|RULE]] #7 - Fixing [[_content/dictionary#D|DOM]] Cross-site Scripting Vulnerabilities¶
The best way to fix DOM based cross-site scripting is to use the right output method (sink). For example if you want to use user input to write in a div tag element don't use innerHtml, instead use innerText or textContent. This will solve the problem, and it is the right way to re-mediate DOM based [[_content/dictionary#X|XSS]] vulnerabilities.
It is always a bad idea to use a user-controlled input in dangerous sources such as eval. 99% of the time it is an indication of bad or lazy programming practice, so simply don't do it instead of trying to sanitize the input.
Finally, to fix the problem in our initial code, instead of trying to encode the output correctly which is a hassle and can easily go wrong we would simply use element.textContent to write it in a content like this:
<b>Current [[_content/dictionary#U|URL]]:</b> <span id="contentholder"></span>
...
<script>
document.getElementById("contentholder").textContent = document.baseURI;
</script>

It does the same thing but this time it is not vulnerable to [[_content/dictionary#D|DOM]] based cross-site scripting vulnerabilities.
### Guidelines for Developing Secure Applications Utilizing [[_content/dictionary#J|JavaScript]]¶
DOM based [[_content/dictionary#X|XSS]] is extremely difficult to mitigate against because of its large attack surface and lack of standardization across browsers.
The guidelines below are an attempt to provide guidelines for developers when developing Web based JavaScript applications (Web 2.0) such that they can avoid XSS.
#### [[_content/dictionary#G|GUIDELINE]] #1 - Untrusted data should only be treated as displayable text¶
Avoid treating untrusted data as code or markup within JavaScript code.
#### [[_content/dictionary#G|GUIDELINE]] #2 - Always [[_content/dictionary#J|JavaScript]] encode and delimit untrusted data as quoted strings when entering the application when building templated JavaScript¶
Always JavaScript encode and delimit untrusted data as quoted strings when entering the application as illustrated in the following example.
var x = "<%= Encode.forJavaScript(untrustedData) %>";

#### [[_content/dictionary#G|GUIDELINE]] #3 - Use document.createElement("..."), element.setAttribute("...","value"), element.appendChild(...) and similar to build dynamic interfaces¶
document.createElement("..."), element.setAttribute("...","value"), element.appendChild(...) and similar are safe ways to build dynamic interfaces.
Please note, element.setAttribute is only safe for a limited number of attributes.
Dangerous attributes include any attribute that is a command execution context, such as onclick or onblur.
Examples of safe attributes includes: align, alink, alt, bgcolor, border, cellpadding, cellspacing, class, color, cols, colspan, coords, dir, face, height, hspace, ismap, lang, marginheight, marginwidth, multiple, nohref, noresize, noshade, nowrap, ref, rel, rev, rows, rowspan, scrolling, shape, span, summary, tabindex, title, usemap, valign, value, vlink, vspace, width.
#### [[_content/dictionary#G|GUIDELINE]] #4 - Avoid sending untrusted data into [[_content/dictionary#H|HTML]] rendering methods¶
Avoid populating the following methods with untrusted data.

1. element.innerHTML = "...";
2. element.outerHTML = "...";
3. document.write(...);
4. document.writeln(...);

#### [[_content/dictionary#G|GUIDELINE]] #5 - Avoid the numerous methods which implicitly eval() data passed to it¶
There are numerous methods which implicitly eval() data passed to it that must be avoided.
Make sure that any untrusted data passed to these methods is:

1. Delimited with string delimiters
2. Enclosed within a closure or [[_content/dictionary#J|JavaScript]] encoded to N-levels based on usage
3. Wrapped in a custom function.

Ensure to follow step 3 above to make sure that the untrusted data is not sent to dangerous methods within the custom function or handle it by adding an extra layer of encoding.
##### Utilizing an Enclosure (as suggested by Gaz)¶
The example that follows illustrates using closures to avoid double [[_content/dictionary#J|JavaScript]] encoding.
 var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
 setTimeout((function(param) { return function() {
          customFunction(param);
        }
 })("<%=ESAPI.encoder().encodeForJavascript(untrustedData)%>"), y);

The other alternative is using N-levels of encoding.
##### N-Levels of Encoding¶
If your code looked like the following, you would need to only double [[_content/dictionary#J|JavaScript]] encode input data.
setTimeout("customFunction('<%=doubleJavaScriptEncodedData%>', y)");
function customFunction (firstName, lastName)
     alert("Hello" + firstName + " " + lastNam);
}

The doubleJavaScriptEncodedData has its first layer of [[_content/dictionary#J|JavaScript]] encoding reversed (upon execution) in the single quotes.
Then the implicit eval of setTimeout reverses another layer of JavaScript encoding to pass the correct value to customFunction
The reason why you only need to double JavaScript encode is that the customFunction function did not itself pass the input to another method which implicitly or explicitly called eval If firstName was passed to another JavaScript method which implicitly or explicitly called eval() then <%=doubleJavaScriptEncodedData%> above would need to be changed to <%=tripleJavaScriptEncodedData%>.
An important implementation note is that if the JavaScript code tries to utilize the double or triple encoded data in string comparisons, the value may be interpreted as different values based on the number of evals() the data has passed through before being passed to the if comparison and the number of times the value was JavaScript encoded.
If A is double JavaScript encoded then the following if check will return false.
 var x = "doubleJavaScriptEncodedA";  //\u005c\u0075\u0030\u0030\u0034\u0031
 if (x == "A") {
    alert("x is A");
 } else if (x == "\u0041") {
    alert("This is what pops");
 }

This brings up an interesting design point. Ideally, the correct way to apply encoding and avoid the problem stated above is to server-side encode for the output context where data is introduced into the application.
Then client-side encode (using a [[_content/dictionary#J|JavaScript]] encoding library such as node-esapi) for the individual subcontext ([[_content/dictionary#D|DOM]] methods) which untrusted data is passed to.
Here are some examples of how they are used:
//server-side encoding
var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
var input = "<%=ESAPI.encoder().encodeForJavascript(untrustedData)%>";

//[[_content/dictionary#H|HTML]] encoding is happening in [[_content/dictionary#J|JavaScript]]
var [[_content/dictionary#E|ESAPI]] = require('node-esapi');
document.writeln(ESAPI.encoder().encodeForHTML(input));

One option is utilize ECMAScript 5 immutable properties in the [[_content/dictionary#J|JavaScript]] library.
Another option provided by Gaz (Gareth) was to use a specific code construct to limit mutability with anonymous closures.
An example follows:
function escapeHTML(str) {
     str = str + "''";
     var out = "''";
     for(var i=0; i<str.length; i++) {
         if(str[i] === '<') {
             out += '&lt;';
         } else if(str[i] === '>') {
             out += '&gt;';
         } else if(str[i] === "'") {
             out += '&#39;';
         } else if(str[i] === '"') {
             out += '&quot;';
         } else {
             out += str[i];
         }
     }
     return out;
}

#### [[_content/dictionary#G|GUIDELINE]] #6 - Use untrusted data on only the right side of an expression¶
Use untrusted data on only the right side of an expression, especially data that looks like code and may be passed to the application (e.g., location and eval()).
window[userDataOnLeftSide] = "userDataOnRightSide";

Using untrusted user data on the left side of the expression allows an attacker to subvert internal and external attributes of the window object, whereas using user input on the right side of the expression doesn't allow direct manipulation.
#### [[_content/dictionary#G|GUIDELINE]] #7 - When [[_content/dictionary#U|URL]] encoding in [[_content/dictionary#D|DOM]] be aware of character set issues¶
When URL encoding in DOM be aware of character set issues as the character set in [[_content/dictionary#J|JavaScript]] DOM is not clearly defined (Mike Samuel).
#### [[_content/dictionary#G|GUIDELINE]] #8 - Limit access to object properties when using object[x] accessors¶
Limit access to object properties when using object[x] accessors (Mike Samuel). In other words, add a level of indirection between untrusted input and specified object properties.
Here is an example of the problem using map types:
var myMapType = {};
myMapType[<%=untrustedData%>] = "moreUntrustedData";

The developer writing the code above was trying to add additional keyed elements to the myMapType object. However, this could be used by an attacker to subvert internal and external attributes of the myMapType object.
A better approach would be to use the following:
if (untrustedData === 'location') {
  myMapType.location = "moreUntrustedData";
}

#### [[_content/dictionary#G|GUIDELINE]] #9 - Run your [[_content/dictionary#J|JavaScript]] in a ECMAScript 5 canopy or sandbox¶
Run your JavaScript in a ECMAScript 5 canopy or sandbox to make it harder for your JavaScript [[_content/dictionary#A|API]] to be compromised (Gareth Heyes and John Stevens).
Examples of some JavaScript sandbox / sanitizers:

[- js-xss](https://github.com/leizongmin/js-xss)
[- sanitize-html](https://github.com/apostrophecms/sanitize-html)
[- DOMPurify](https://github.com/cure53/DOMPurify)
[- [[_content/dictionary#M|MDN]] - [[_content/dictionary#H|HTML]] Sanitizer [[_content/dictionary#A|API]]](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/API/HTML_Sanitizer_API)
[- [[_content/dictionary#O|OWASP]] Summit 2011 - [[_content/dictionary#D|DOM]] Sandboxing](https://owasp.org/www-pdf-archive/OWASPSummit2011DOMSandboxingBrowserSecurityTrack.pdf)

#### [[_content/dictionary#G|GUIDELINE]] #10 - Don't eval() [[_content/dictionary#J|JSON]] to convert it to native [[_content/dictionary#J|JavaScript]] objects¶
Don't eval() JSON to convert it to native JavaScript objects. Instead use JSON.toJSON() and JSON.parse() (Chris Schmidt).
### Common Problems Associated with Mitigating [[_content/dictionary#D|DOM]] Based [[_content/dictionary#X|XSS]]¶
#### Complex Contexts¶
In many cases the context isn't always straightforward to discern.
<a href="javascript:myFunction('<%=untrustedData%>', 'test');">Click Me</a>
 ...
<script>
Function myFunction (url,name) {
    window.location = url;
}
</script>

In the above example, untrusted data started in the rendering [[_content/dictionary#U|URL]] context (href attribute of an a tag) then changed to a [[_content/dictionary#J|JavaScript]] execution context (javascript: protocol handler) which passed the untrusted data to an execution URL subcontext (window.location of myFunction).
Because the data was introduced in JavaScript code and passed to a URL subcontext the appropriate server-side encoding would be the following:
<a href="javascript:myFunction('<%=[[_content/dictionary#E|ESAPI]].encoder().encodeForJavascript(ESAPI.encoder().encodeForURL(untrustedData)) %>', 'test');">
Click Me</a>
 ...

Or if you were using ECMAScript 5 with an immutable [[_content/dictionary#J|JavaScript]] client-side encoding libraries you could do the following:
<!-- server side [[_content/dictionary#U|URL]] encoding has been removed.  Now only JavaScript encoding on server side. -->
<a href="javascript:myFunction('<%=[[_content/dictionary#E|ESAPI]].encoder().encodeForJavascript(untrustedData)%>', 'test');">Click Me</a>
 ...
<script>
Function myFunction (url,name) {
    var encodedURL = ESAPI.encoder().encodeForURL(url);  //URL encoding using client-side scripts
    window.location = encodedURL;
}
</script>

#### Inconsistencies of Encoding Libraries¶
There are a number of open source encoding libraries out there:

1. [[_content/dictionary#O|OWASP]] [[_content/dictionary#E|ESAPI]]
OWASP [Java Encoder](https://owasp.org/www-project-java-encoder/)
Apache Commons Text [[[_content/dictionary#S|StringEscapeUtils]]](https://commons.apache.org/proper/commons-text/javadocs/api-release/org/apache/commons/text/StringEscapeUtils.html), replace one from [Apache Commons Lang3](https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/StringEscapeUtils.html)
[4. Jtidy](http://jtidy.sourceforge.net/)
5. Your company's custom implementation.

Some work on a denylist while others ignore important characters like "<" and ">".
Java Encoder is an active project providing supports for [[_content/dictionary#H|HTML]], [[_content/dictionary#C|CSS]] and [[_content/dictionary#J|JavaScript]] encoding.
[[_content/dictionary#E|ESAPI]] is one of the few which works on an allowlist and encodes all non-alphanumeric characters. It is important to use an encoding library that understands which characters can be used to exploit vulnerabilities in their respective contexts. Misconceptions abound related to the proper encoding that is required.
#### Encoding Misconceptions¶
Many security training curriculums and papers advocate the blind usage of HTML encoding to resolve [[_content/dictionary#X|XSS]].
This logically seems to be prudent advice as the JavaScript parser does not understand HTML encoding.
However, if the pages returned from your web application utilize a content type of text/xhtml or the file type extension of *.xhtml then HTML encoding may not work to mitigate against XSS.
For example:
<script>
&#x61;lert(1);
</script>

The [[_content/dictionary#H|HTML]] encoded value above is still executable. If that isn't enough to keep in mind, you have to remember that encodings are lost when you retrieve them using the value attribute of a [[_content/dictionary#D|DOM]] element.
Let's look at the sample page and script:
<form name="myForm" ...>
  <input type="text" name="lName" value="<%=[[_content/dictionary#E|ESAPI]].encoder().encodeForHTML(last_name)%>">
 ...
</form>
<script>
  var x = document.myForm.lName.value;  //when the value is retrieved the encoding is reversed
  document.writeln(x);  //any code passed into lName is now executable.
</script>

Finally there is the problem that certain methods in [[_content/dictionary#J|JavaScript]] which are usually safe can be unsafe in certain contexts.
#### Usually Safe Methods¶
One example of an attribute which is thought to be safe is innerText.
Some papers or guides advocate its use as an alternative to innerHTML to mitigate against [[_content/dictionary#X|XSS]] in innerHTML. However, depending on the tag which innerText is applied, code can be executed.
<script>
 var tag = document.createElement("script");
 tag.innerText = "<%=untrustedData%>";  //executes code
</script>

The innerText feature was originally introduced by Internet Explorer, and was formally specified in the [[_content/dictionary#H|HTML]] standard in 2016 after being adopted by all major browser vendors.
#### Detect [[_content/dictionary#D|DOM]] [[_content/dictionary#X|XSS]] using variant analysis¶
Vulnerable code:
<script>
var x = location.hash.split("#")[1];
document.write(x);
</script>

Semgrep rule to identify above dom xss link.