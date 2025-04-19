---
title: "XML External Entity Prevention Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html"
created: "1741872882.2362938"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#X|XML]] External Entity Prevention

## [[_content/dictionary#X|XML]] External Entity Prevention Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#references)](#xmlreader_2)](#xmlinputfactory)](#saxreader_1)](#saxparserfactory)](#saxbuilder_1)](#documentbuilderfactory)](#digester)](#java_1)](#semgrep-rules)](#python)](#php)](#nsxmldocument)](#libxml2_1)](#ios)](#xslcompiledtransform)](#xpathnavigator)](#net-452-and-later)](#net-40-net-452)](#prior-to-net-40)](#xmltextreader)](#xmlreader_1)](#xmlnodereader)](#xmldocument)](#xmldictionaryreader)](#linq-to-xml)](#aspnet)](#xmldictionaryreader-xmlnodereader-xmlreader-default-safety-levels)](#xmldocument-xmltextreader-xpathnavigator-default-safety-levels)](#overview-of-net-parser-safety-levels)](#net)](#castor)](#spring-framework-mvcoxm-xxe-vulnerabilities)](#other-xml-parsers)](#javabeansxmldecoder)](#xpathexpression)](#jaxb-unmarshaller)](#no-op-entityresolver)](#saxbuilder)](#saxreader)](#xmlreader)](#saxtransformerfactory)](#schemafactory)](#validator)](#transformerfactory)](#oracle-dom-parser)](#xmlinputfactory-a-stax-parser)](#jaxp-documentbuilderfactory-saxparserfactory-and-dom4j)](#java)](#lucee)](#adobe-coldfusion)](#coldfusion)](#libxerces-c)](#libxml2)](#cc)](#general-guidance)](#introduction)](#xml-external-entity-prevention-cheat-sheet)
### Introduction¶
An XML eXternal Entity injection ([[_content/dictionary#X|XXE]]), which is now part of the [[[_content/dictionary#O|OWASP]] Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A4-XML_External_Entities_%28XXE%29) via the point A4, is attack against applications that parse XML input. This issue is referenced in the ID [611](https://cwe.mitre.org/data/definitions/611.html) in the [Common Weakness Enumeration](https://cwe.mitre.org/index.html) referential. An XXE attack occurs when untrusted XML input with a reference to an external entity is processed by a weakly configured XML parser, and this attack could be used to stage multiple incidents, including:

- A denial of service attack on the system
A [Server Side Request Forgery](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery) ([[_content/dictionary#S|SSRF]]) attack
The ability to scan ports from the machine w[[here](https://gist.github.com/asudhakar02/45e2e6fd8bcdfb4bc3b2)](https://docs.oracle.com/en/java/javase/13/security/java-api-xml-processing-jaxp-security-guide.html#[[_content/dictionary#G|GUID]]-88B04BE2-35EF-4F61-B4FA-57A0E9102342) the parser is located
- Other system impacts.

This cheat sheet will help you prevent this vulnerability.
For more information on [[_content/dictionary#X|XXE]], please visit [[[_content/dictionary#X|XML]] External Entity (XXE)](https://en.wikipedia.org/wiki/XML_external_entity_attack).
### General Guidance¶
The safest way to prevent XXE is always to disable [[[_content/dictionary#D|DTD]]](https://www.w3schools.com/xml/xml_dtd.asp)s (External Entities) completely. Depending on the parser, the method should be similar to the following:
factory.[[setFeature](https://docs.oracle.com/javase/7/docs/api/org/xml/sax/XMLReader.html#setFeature%28java.lang.String,%20boolean%29)](https://docs.oracle.com/javase/7/docs/api/javax/xml/parsers/[[_content/dictionary#D|DocumentBuilderFactory]].html#setFeature(java.lang.String,%20boolean))("http://apache.org/xml/features/disallow-doctype-decl", true);

Disabling DTDs also makes the parser secure against denial of services ([[_content/dictionary#D|DOS]]) attacks such as [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack). If it is not possible to disable DTDs completely, then external entities and external document type declarations must be disabled in the way that's specific to each parser.
Detailed [[_content/dictionary#X|XXE]] Prevention guidance is provided below for multiple languages (C++, Cold Fusion, Java, .[[_content/dictionary#N|NET]], iOS, [[_content/dictionary#P|PHP]], Python, [Semgrep](https://semgrep.dev/) Rules) and their commonly used [[_content/dictionary#X|XML]] parsers.
### C/C++¶
#### #### libxml2¶
The Enum [xmlParserOption](http://xmlsoft.org/html/libxml-parser.html#xmlParserOption) should not have the following options defined:

- XML_PARSE_NOENT: Expands entities and substitutes them with replacement text
- XML_PARSE_DTDLOAD: Load the external [[_content/dictionary#D|DTD]]

Note:
Per: According to [this post](https://mail.gnome.org/archives/xml/2012-October/msg00045.html), starting with libxml2 version 2.9, [[_content/dictionary#X|XXE]] has been [disabled by default](https://docs.microsoft.com/en-us/dotnet/standard/linq/linq-xml-security) as committed by the following [patch](https://gitlab.gnome.org/[[_content/dictionary#G|GNOME]]/libxml2/commit/4629ee02ac649c27f9c0cf98ba017c6b5526070f).
Search whether the following APIs are being used and make sure there is no XML_PARSE_NOENT and XML_PARSE_DTDLOAD defined in the parameters:

- xmlCtxtReadDoc
- xmlCtxtReadFd
- xmlCtxtReadFile
- xmlCtxtReadIO
- xmlCtxtReadMemory
- xmlCtxtUseOptions
- xmlParseInNodeContext
- xmlReadDoc
- xmlReadFd
- xmlReadFile
- xmlReadIO
- xmlReadMemory

#### libxerces-c¶
Use of XercesDOMParser do this to prevent [[_content/dictionary#X|XXE]]:
XercesDOMParser *parser = new XercesDOMParser;
parser->setCreateEntityReferenceNodes(true);
parser->setDisableDefaultEntityResolution(true);

Use of SAXParser, do this to prevent [[_content/dictionary#X|XXE]]:
SAXParser* parser = new SAXParser;
parser->setDisableDefaultEntityResolution(true);

Use of SAX2XMLReader, do this to prevent [[_content/dictionary#X|XXE]]:
SAX2XMLReader* reader = XMLReaderFactory::createXMLReader();
parser->setFeature(XMLUni::fgXercesDisableDefaultEntityResolution, true);

### [[_content/dictionary#C|ColdFusion]]¶
Per [this blog post](https://hoyahaxa.blogspot.com/2022/11/on-coldfusion-xxe-and-other-xml-attacks.html), both Adobe ColdFusion and Lucee have built-in mechanisms to disable support for external [[_content/dictionary#X|XML]] entities.
#### Adobe [[_content/dictionary#C|ColdFusion]]¶
As of ColdFusion 2018 Update 14 and ColdFusion 2021 Update 4, all native ColdFusion functions that process XML have a XML parser argument that disables support for external XML entities. Since there is no global setting that disables external entities, developers must ensure that every XML function call uses the correct security options.
From the [documentation for the [[_content/dictionary#X|XmlParse]]() function](https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-functions/functions-t-z/xmlparse.html), you can disable [[_content/dictionary#X|XXE]] with the code below:
<cfset parseroptions = structnew()>
<cfset parseroptions.[[_content/dictionary#A|ALLOWEXTERNALENTITIES]] = false>
<cfscript>
a = XmlParse("xml.xml", false, parseroptions);
writeDump(a);
</cfscript>

You can use the "parseroptions" structure shown above as an argument to secure other functions that process [[_content/dictionary#X|XML]] as well, such as:
[[_content/dictionary#X|XxmlSearch]](xmldoc, xpath,parseroptions);

[[_content/dictionary#X|XmlTransform]](xmldoc,xslt,parseroptions);

isXML(xmldoc,parseroptions);

#### Lucee¶
As of Lucee 5.3.4.51 and later, you can disable support for [[_content/dictionary#X|XML]] external entities by adding the following to your Application.cfc:
this.xml[[Features](https://xerces.apache.org/xerces2-j/features.html)](https://xerces.apache.org/xerces-j/features.html) = {
     externalGeneralEntities: false,
     secure: true,
     disallowDoctypeDecl: true
};

Support for external [[_content/dictionary#X|XML]] entities is disabled by default as of Lucee 5.4.2.10 and Lucee 6.0.0.514.
### #### Java¶
Since most Java XML parsers have [[_content/dictionary#X|XXE]] [enabled by default](https://referencesource.microsoft.com/#System.Xml.Linq/System/Xml/Linq/XLinq.cs,71f4626a3d6f9bad), this language is especially vulnerable to XXE attack, so you must explicitly disable XXE to use these parsers safely. This section describes how to disable XXE in the most commonly used Java XML parsers.
#### [[_content/dictionary#J|JAXP]] [[_content/dictionary#D|DocumentBuilderFactory]], SAXParserFactory and DOM4J¶
[[_content/dictionary#T|TheDocumentBuilderFactory]], SAXParserFactory and DOM4J XML parsers can be protected against XXE attacks with the same techniques.
For brevity, we will only show you how to protect the DocumentBuilderFactory parser. Additional instructions for protecting this parser are embedded within the example code
The JAXP DocumentBuilderFactory setFeature method allows a developer to control which implementation-specific XML processor features are enabled or disabled.
These features can either be set on the factory or the underlying XMLReader setFeature method.
Each XML processor implementation has its own features that govern how DTDs and external entities are processed. By disabling [[_content/dictionary#D|DTD]] processing entirely, most XXE attacks can be averted, although it is also necessary to disable or verify that XInclude is not enabled.
Since the [[_content/dictionary#J|JDK]] 6, the flag [FEATURE_SECURE_PROCESSING](https://docs.oracle.com/javase/6/docs/api/javax/xml/XMLConstants.html#FEATURE_SECURE_PROCESSING) can be used to instruct the implementation of the parser to process XML securely. Its behavior is implementation-dependent. It may help with resource exhaustion but it may not always mitigate entity expansion. More details on this flag can be found here.
For a syntax highlighted example code snippet using SAXParserFactory, look here.
Example code disabling DTDs (doctypes) altogether:
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.[[_content/dictionary#P|ParserConfigurationException]]; // catching unsupported features
import javax.xml.XMLConstants;

...

[[_content/dictionary#D|DocumentBuilderFactory]] dbf = DocumentBuilderFactory.newInstance();
String [[_content/dictionary#F|FEATURE]] = null;
try {
    // This is the [[_content/dictionary#P|PRIMARY]] defense. If DTDs (doctypes) are disallowed, almost all
    // [[_content/dictionary#X|XML]] entity attacks are prevented
    // [Xerces 2](https://xerces.apache.org/xerces2-j/) only - http://xerces.apache.org/xerces2-j/features.html#disallow-doctype-decl
    FEATURE = "http://apache.org/xml/features/disallow-doctype-decl";
    dbf.setFeature(FEATURE, true);

    // and these as well, per [- Timothy Morgan's 2014 paper: "[[_content/dictionary#X|XML]] Schema, [[_content/dictionary#D|DTD]], and Entity Attacks"](https://vsecurity.com//download/papers/XMLDTDEntityAttacks.pdf)
    dbf.setXIncludeAware(false);

    // remaining parser logic
    ...
} catch ([[_content/dictionary#P|ParserConfigurationException]] e) {
    // This should catch a failed setFeature feature
    // [[_content/dictionary#N|NOTE]]: Each call to setFeature() should be in its own try/catch otherwise subsequent calls will be skipped.
    // This is only important if you're ignoring errors for multi-provider support.
    logger.info("ParserConfigurationException was thrown. The feature '" + [[_content/dictionary#F|FEATURE]]
    + "' is not supported by your [[_content/dictionary#X|XML]] processor.");
    ...
} catch (SAXException e) {
    // On Apache, this should be thrown when disallowing [[_content/dictionary#D|DOCTYPE]]
    logger.warning("A DOCTYPE was passed into the XML document");
    ...
} catch (IOException e) {
    // [[_content/dictionary#X|XXE]] that points to a file that doesn't exist
    logger.error("IOException occurred, XXE may still possible: " + e.getMessage());
    ...
}

// Load [[_content/dictionary#X|XML]] file or stream using a [[_content/dictionary#X|XXE]] agnostic configured parser...
[[_content/dictionary#D|DocumentBuilder]] safebuilder = dbf.newDocumentBuilder();

If you can't completely disable DTDs:
import javax.xml.parsers.[[_content/dictionary#D|DocumentBuilderFactory]];
import javax.xml.parsers.[[_content/dictionary#P|ParserConfigurationException]]; // catching unsupported features
import javax.xml.XMLConstants;

...

[[_content/dictionary#D|DocumentBuilderFactory]] dbf = DocumentBuilderFactory.newInstance();

String[] featuresToDisable = {
    // [Xerces 1](https://xerces.apache.org/xerces-j/) - http://xerces.apache.org/xerces-j/features.html#external-general-entities
    // Xerces 2 - http://xerces.apache.org/xerces2-j/features.html#external-general-entities
    // JDK7+ - http://xml.org/sax/features/external-general-entities
    //This feature has to be used together with the following one, otherwise it will not protect you from [[_content/dictionary#X|XXE]] for sure
    "http://xml.org/sax/features/external-general-entities",

    // Xerces 1 - http://xerces.apache.org/xerces-j/features.html#external-parameter-entities
    // Xerces 2 - http://xerces.apache.org/xerces2-j/features.html#external-parameter-entities
    // JDK7+ - http://xml.org/sax/features/external-parameter-entities
    //This feature has to be used together with the previous one, otherwise it will not protect you from [[_content/dictionary#X|XXE]] for sure
    "http://xml.org/sax/features/external-parameter-entities",

    // Disable external DTDs as well
    "http://apache.org/xml/features/nonvalidating/load-external-dtd"
}

for (String feature : featuresToDisable) {
    try {    
        dbf.setFeature([[_content/dictionary#F|FEATURE]], false); 
    } catch ([[_content/dictionary#P|ParserConfigurationException]] e) {
        // This should catch a failed setFeature feature
        logger.info("ParserConfigurationException was thrown. The feature '" + feature
        + "' is probably not supported by your [[_content/dictionary#X|XML]] processor.");
        ...
    }
}

try {
    // Add these as per Timothy Morgan's 2014 paper: "[[_content/dictionary#X|XML]] Schema, [[_content/dictionary#D|DTD]], and Entity Attacks"
    dbf.setXIncludeAware(false);
    dbf.setExpandEntityReferences(false);

    // As stated in the documentation, "Feature for Secure Processing ([[_content/dictionary#F|FSP]])" is the central mechanism that will
    // help you safeguard [[_content/dictionary#X|XML]] processing. It instructs XML processors, such as parsers, validators, 
    // and transformers, to try and process XML securely, and the FSP can be used as an alternative to
    // dbf.setExpandEntityReferences(false); to allow some safe level of Entity Expansion
    // Exists from JDK6.
    dbf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

    // And, per Timothy Morgan: "If for some reason support for inline DOCTYPEs are a requirement, then
    // ensure the entity settings are disabled (as shown above) and beware that [[_content/dictionary#S|SSRF]] attacks
    // (http://cwe.mitre.org/data/definitions/918.html) and denial
    // of service attacks (such as billion laughs or decompression bombs via "jar:") are a risk."

    // remaining parser logic
    ...
} catch ([[_content/dictionary#P|ParserConfigurationException]] e) {
    // This should catch a failed setFeature feature
    logger.info("ParserConfigurationException was thrown. The feature 'XMLConstants.FEATURE_SECURE_PROCESSING'"
    + " is probably not supported by your [[_content/dictionary#X|XML]] processor.");
    ...
} catch (SAXException e) {
    // On Apache, this should be thrown when disallowing [[_content/dictionary#D|DOCTYPE]]
    logger.warning("A DOCTYPE was passed into the XML document");
    ...
} catch (IOException e) {
    // [[_content/dictionary#X|XXE]] that points to a file that doesn't exist
    logger.error("IOException occurred, XXE may still possible: " + e.getMessage());
    ...
}

// Load [[_content/dictionary#X|XML]] file or stream using a [[_content/dictionary#X|XXE]] agnostic configured parser...
[[_content/dictionary#D|DocumentBuilder]] safebuilder = dbf.newDocumentBuilder();

Xerces 1 Features:

Do not include external entities by setting [[[[[[[this feature](https://xerces.apache.org/xerces-j/features.html#load-external-dtd)](https://xerces.apache.org/xerces2-j/features.html#external-parameter-entities)](https://xerces.apache.org/xerces2-j/features.html#external-general-entities)](https://xerces.apache.org/xerces2-j/features.html#disallow-doctype-decl)](https://xerces.apache.org/xerces-j/features.html#load-external-dtd)](https://xerces.apache.org/xerces-j/features.html#external-parameter-entities)](https://xerces.apache.org/xerces-j/features.html#external-general-entities) to false.
- - Do not include parameter entities by setting this feature to false.
- - Do not include external DTDs by setting this feature to false.

Xerces 2 Features:

- Disallow an inline [[_content/dictionary#D|DTD]] by setting this feature to true.
- - Do not include external entities by setting this feature to false.
Do not include parameter entities by setting this feature to false.
Do not include external DTDs by setting this feature to false.

Note: The above defenses require Java 7 update 67, Java 8 update 20, or above, because the countermeasures for [[_content/dictionary#D|DocumentBuilderFactory]] and SAXParserFactory are broken in earlier Java versions, per: [[[_content/dictionary#C|CVE]]-2014-6517](http://www.cvedetails.com/cve/CVE-2014-6517/).
#### [XMLInputFactory](http://docs.oracle.com/javase/7/docs/api/javax/xml/stream/XMLInputFactory.html) (a [StAX](http://en.wikipedia.org/wiki/StAX) parser)¶
StAX parsers such as XMLInputFactory allow various properties and features to be set.
To protect a Java XMLInputFactory from [[_content/dictionary#X|XXE]], disable DTDs (doctypes) altogether:
// This disables DTDs entirely for that factory
xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, false);

or if you can't completely disable DTDs:
// This causes XMLStreamException to be thrown if external DTDs are accessed.
xmlInputFactory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
// disable external entities
xmlInputFactory.setProperty("javax.xml.stream.isSupportingExternalEntities", false);

The setting xmlInputFactory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, ""); is not required, as XMLInputFactory is dependent on [Validator](#Validator) to perform [[_content/dictionary#X|XML]] validation against Schemas. Check the Validator section for the specific configuration.
#### Oracle [[_content/dictionary#D|DOM]] Parser¶
Follow [Oracle recommendation](https://docs.oracle.com/en/database/oracle/oracle-database/18/adxdk/security-considerations-oracle-xml-developers-kit.html#[[_content/dictionary#G|GUID]]-45303542-41DE-4455-93B3-854A826EF8BB) e.g.:
    // Extend oracle.xml.parser.v2.XMLParser
    DOMParser domParser = new DOMParser();

    // Do not expand entity references
    domParser.setAttribute(DOMParser.EXPAND_ENTITYREF, false);

    // dtdObj is an instance of oracle.xml.parser.v2.[[_content/dictionary#D|DTD]]
    domParser.setAttribute(DOMParser.DTD_OBJECT, dtdObj);

    // Do not allow more than 11 levels of entity expansion
    domParser.setAttribute(DOMParser.ENTITY_EXPANSION_DEPTH, 12);

#### [[_content/dictionary#T|TransformerFactory]]¶
To protect a javax.xml.transform.TransformerFactory from [[_content/dictionary#X|XXE]], do this:
TransformerFactory tf = TransformerFactory.newInstance();
tf.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
tf.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");

#### Validator¶
To protect a javax.xml.validation.Validator from [[_content/dictionary#X|XXE]], do this:
[[_content/dictionary#S|SchemaFactory]] factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
Schema schema = factory.newSchema();
Validator validator = schema.newValidator();
validator.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
validator.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");

#### [[_content/dictionary#S|SchemaFactory]]¶
To protect a javax.xml.validation.SchemaFactory from [[_content/dictionary#X|XXE]], do this:
SchemaFactory factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
Schema schema = factory.newSchema(Source);

#### SAXTransformerFactory¶
To protect a javax.xml.transform.sax.SAXTransformerFactory from [[_content/dictionary#X|XXE]], do this:
SAXTransformerFactory sf = SAXTransformerFactory.newInstance();
sf.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
sf.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
sf.newXMLFilter(Source);

Note: Use of the following XMLConstants requires [[_content/dictionary#J|JAXP]] 1.5, which was added to Java in 7u40 and Java 8:

- javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD
- javax.xml.XMLConstants.ACCESS_EXTERNAL_SCHEMA
- javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET

#### ##### XMLReader¶
To protect the Java org.xml.sax.XMLReader from an [[_content/dictionary#X|XXE]] attack, do this:
XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
// This may not be strictly required as DTDs shouldn't be allowed at all, per previous line.
reader.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
reader.setFeature("http://xml.org/sax/features/external-general-entities", false);
reader.setFeature("http://xml.org/sax/features/external-parameter-entities", false);

#### ##### SAXReader¶
To protect a Java org.dom4j.io.SAXReader from an [[_content/dictionary#X|XXE]] attack, do this:
saxReader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
saxReader.setFeature("http://xml.org/sax/features/external-general-entities", false);
saxReader.setFeature("http://xml.org/sax/features/external-parameter-entities", false);

If your code does not have all of these lines, you could be vulnerable to an [[_content/dictionary#X|XXE]] attack.
#### ##### SAXBuilder¶
To protect a Java org.jdom2.input.SAXBuilder from an XXE attack, disallow DTDs (doctypes) entirely:
SAXBuilder builder = new SAXBuilder();
builder.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);
Document doc = builder.build(new File(fileName));

Alternatively, if DTDs can't be completely disabled, disable external entities and entity expansion:
SAXBuilder builder = new SAXBuilder();
builder.setFeature("http://xml.org/sax/features/external-general-entities", false);
builder.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
builder.setExpandEntities(false);
Document doc = builder.build(new File(fileName));

#### No-op [[_content/dictionary#E|EntityResolver]]¶
For APIs that take an EntityResolver, you can neutralize an [[_content/dictionary#X|XML]] parser's ability to resolve entities by [supplying a no-op implementation](https://wiki.sei.cmu.edu/confluence/display/java/IDS17-J.+Prevent+XML+External+Entity+Attacks):
public final class [[_content/dictionary#N|NoOpEntityResolver]] implements EntityResolver {
    public [[_content/dictionary#I|InputSource]] resolveEntity(String publicId, String systemId) {
        return new InputSource(new [[_content/dictionary#S|StringReader]](""));
    }
}

// ...

xmlReader.setEntityResolver(new [[_content/dictionary#N|NoOpEntityResolver]]());
documentBuilder.setEntityResolver(new NoOpEntityResolver());

or more simply:
[[_content/dictionary#E|EntityResolver]] noop = (publicId, systemId) -> new [[_content/dictionary#I|InputSource]](new [[_content/dictionary#S|StringReader]](""));
xmlReader.setEntityResolver(noop);
documentBuilder.setEntityResolver(noop);

#### [[_content/dictionary#J|JAXB]] Unmarshaller¶
You should ensure that the source to the unmarshal function of javax.xml.bind.Unmarshaller is javax.xml.stream.XMLStreamReader that was generated using javax.xml.stream.XMLInputFactory with safe properties, i.e. XMLInputFactory.SUPPORT_DTD and XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES set to false. For example:
File file = new File(xmlPath);
XMLInputFactory xif = XMLInputFactory.newFactory();
xif.setProperty(XMLInputFactory.SUPPORT_DTD, false);
xif.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
XMLStreamReader xsr = null;
try {
    xsr = xif.createXMLStreamReader(new [[_content/dictionary#S|StreamSource]](file));
} catch (XMLStreamException e) {
    throw new [[_content/dictionary#R|RuntimeException]](e);
}  
Unmarshaller um = jc.createUnmarshaller();
um.unmarshal(xsr);

Note that both the createXMLStreamReader and unmarshal methods have several overloads with various source types, so you need to pick the right one and do a possible conversion.
#### XPathExpression¶
Since javax.xml.xpath.XPathExpression can not be configured securely by itself, the untrusted data must be parsed through another securable [[_content/dictionary#X|XML]] parser first.
For example:
[[_content/dictionary#D|DocumentBuilderFactory]] df = DocumentBuilderFactory.newInstance();
df.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
df.setAttribute(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
[[_content/dictionary#D|DocumentBuilder]] builder = df.newDocumentBuilder();
String result = new XPathExpression().evaluate( builder.parse(
                            new [[_content/dictionary#B|ByteArrayInputStream]](xml.getBytes())) );

#### java.beans.XMLDecoder¶
The [readObject()](https://docs.oracle.com/javase/8/docs/api/java/beans/XMLDecoder.html#readObject--) method in this class is fundamentally unsafe.
Not only is the XML it parses subject to XXE, but the method can be used to construct any Java object, and [execute arbitrary code as described here](http://stackoverflow.com/questions/14307442/is-it-safe-to-use-xmldecoder-to-read-document-files).
And there is no way to make use of this class safe except to trust or properly validate the input being passed into it.
As such, we'd strongly recommend completely avoiding the use of this class and replacing it with a safe or properly configured XML parser as described elsewhere in this cheat sheet.
#### Other [[_content/dictionary#X|XML]] Parsers¶
There are many third-party libraries that parse XML either directly or through their use of other libraries. Please test and verify their XML parser is secure against XXE by default. If the parser is not secure by default, look for flags supported by the parser to disable all possible external resource inclusions like the examples given above. If there's no control exposed to the outside, make sure the untrusted content is passed through a secure parser first and then passed to insecure third-party parser similar to how the Unmarshaller is secured.
##### Spring Framework [[_content/dictionary#M|MVC]]/[[_content/dictionary#O|OXM]] [[_content/dictionary#X|XXE]] Vulnerabilities¶
**Some XXE vulnerabilities were found in [Spring OXM](https://pivotal.io/security/cve-2013-4152) and [Spring MVC](https://pivotal.io/security/cve-2013-7315) . The following versions of the Spring Framework are vulnerable to XXE:

- 3.0.0 to 3.2.3 (Spring [[_content/dictionary#O|OXM]] & Spring [[_content/dictionary#M|MVC]])
- 4.0.0.M1 (Spring [[_content/dictionary#O|OXM]])
- 4.0.0.M1-4.0.0.M2 (Spring [[_content/dictionary#M|MVC]])

There were other issues as well that were fixed later, so to fully address these issues, Spring recommends you upgrade to Spring Framework 3.2.8+ or 4.0.2+.
For Spring [[_content/dictionary#O|OXM]], this is referring to the use of org.springframework.oxm.jaxb.Jaxb2Marshaller. Note that the [[_content/dictionary#C|CVE]] for Spring OXM specifically indicates that two [[_content/dictionary#X|XML]] parsing situations are up to the developer to get right, and the other two are the responsibility of Spring and were fixed to address this CVE.
Here's what they say:
Two situations developers must handle:

- For a DOMSource, the [[_content/dictionary#X|XML]] has already been parsed by user code and that code is responsible for protecting against [[_content/dictionary#X|XXE]].
- For a StAXSource, the XMLStreamReader has already been created by user code and that code is responsible for protecting against [[_content/dictionary#X|XXE]].

The issue Spring fixed:
For SAXSource and [[_content/dictionary#S|StreamSource]] instances, Spring processed external entities by default thereby creating this vulnerability.
Here's an example of using a StreamSource that was vulnerable, but is now safe, if you are using a fixed version of Spring [[_content/dictionary#O|OXM]] or Spring [[_content/dictionary#M|MVC]]:
import org.springframework.oxm.Jaxb2Marshaller;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;

Jaxb2Marshaller marshaller = new Jaxb2Marshaller();
// Must cast return Object to whatever type you are unmarshalling
marshaller.unmarshal(new [[_content/dictionary#S|StreamSource]](new [[_content/dictionary#S|StringReader]](some_string_containing_XML));

So, per the [Spring [[_content/dictionary#O|OXM]] [[_content/dictionary#C|CVE]] writeup](https://pivotal.io/security/cve-2013-4152), the above is now safe. But if you were to use a DOMSource or StAXSource instead, it would be up to you to configure those sources to be safe from [[_content/dictionary#X|XXE]].
##### Castor¶
Castor is a data binding framework for Java. It allows conversion between Java objects, [[_content/dictionary#X|XML]], and relational tables. The XML features in Castor prior to version 1.3.3 are vulnerable to XXE, and should be upgraded to the latest version. For additional information, check the official [XML configuration file](https://castor-data-binding.github.io/castor/reference-guide/reference/xml/xml-properties.html)
### .[[_content/dictionary#N|NET]]¶
Up-to-date information for XXE injection in .NET is taken directly from the [web application of unit tests by Dean Fleming](https://github.com/deanf1/dotnet-security-unit-tests), which covers all currently supported .NET XML parsers, and has test cases that demonstrate when they are safe from XXE injection and when they are not, but these tests are only with injection from file and not direct [[_content/dictionary#D|DTD]] (used by [[_content/dictionary#D|DoS]] attacks).
For DoS attacks using a direct DTD (such as the [Billion laughs attack](https://en.wikipedia.org/wiki/Billion_laughs_attack)), a [separate testing application from Josh Grossman at Bounce Security](https://github.com/[[_content/dictionary#B|BounceSecurity]]/[[_content/dictionary#B|BillionLaughsTester]]) has been created to verify that .NET >=4.5.2 is safe from these attacks.
Previously, this information was based on some older articles which may not be 100% accurate including:

[James Jardine's excellent .[[_content/dictionary#N|NET]] [[_content/dictionary#X|XXE]] article](https://www.jardinesoftware.net/2016/05/26/xxe-and-net/).
[Guidance from Microsoft on how to prevent XXE and [[_content/dictionary#X|XML]] Denial of Service in .NET](http://msdn.microsoft.com/en-us/magazine/ee335713.aspx).

#### Overview of .[[_content/dictionary#N|NET]] Parser Safety Levels¶
**Below is an overview of all supported .NET XML parsers and their default safety levels. More details about each parser are included after this list.
**XDocument (Ling to XML)
This parser is protected from external entities at .NET Framework version 4.5.2 and protected from Billion Laughs at version 4.5.2 or greater, but it is uncertain if this parser is protected from Billion Laughs before version 4.5.2.
##### [[_content/dictionary#X|XmlDocument]], [[_content/dictionary#X|XmlTextReader]], XPathNavigator default safety levels¶
These parsers are vulnerable to external entity attacks and Billion Laughs at versions below version 4.5.2 but protected at versions equal or greater than 4.5.2.
##### [[_content/dictionary#X|XmlDictionaryReader]], [[_content/dictionary#X|XmlNodeReader]], [[_content/dictionary#X|XmlReader]] default safety levels¶
These parsers are not vulnerable to external entity attacks or Billion Laughs before or after version 4.5.2. Also, at or greater than versions ≥4.5.2, these libraries won't even process the in-line [[_content/dictionary#D|DTD]] by default. Even if you change the default to allow processing a DTD, if a [[_content/dictionary#D|DoS]] attempt is performed an exception will still be thrown as documented above.
#### [[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]]¶
ASP.NET applications ≥ .NET 4.5.2 must also ensure setting the <httpRuntime targetFramework="..." /> in their Web.config to ≥4.5.2 or risk being vulnerable regardless or the actual .NET version. Omitting this tag will also result in unsafe-by-default behavior.
For the purpose of understanding the above table, the .NET Framework Version for an ASP.NET applications is either the .NET version the application was build with or the httpRuntime's targetFramework (Web.config), whichever is lower.
This configuration tag should not be confused with a similar configuration tag: <compilation targetFramework="..." /> or the assemblies / projects targetFramework, which are not sufficient for achieving secure-by-default behaviour as advertised in the above table.
#### [[_content/dictionary#L|LINQ]] to [[_content/dictionary#X|XML]]¶
Both the XElement and XDocument objects in the System.Xml.Linq library are safe from [[_content/dictionary#X|XXE]] injection from external file and DoS attack by default. XElement parses only the elements within the XML file, so DTDs are ignored altogether. XDocument has [[_content/dictionary#X|XmlResolver]] disabled by default so it's safe from [[_content/dictionary#S|SSRF]]. Whilst DTDs are enabled by default, from Framework versions ≥4.5.2, it is not vulnerable to DoS as noted but it may be vulnerable in earlier Framework versions. For more information, see [Microsoft's guidance on how to prevent XXE and XML Denial of Service in .NET](http://msdn.microsoft.com/en-us/magazine/ee335713.aspx)
#### [[_content/dictionary#X|XmlDictionaryReader]]¶
System.Xml.XmlDictionaryReader is safe by default, as when it attempts to parse the DTD, the compiler throws an exception saying that "CData elements not valid at top level of an XML document". It becomes unsafe if constructed with a different unsafe XML parser.
#### [[_content/dictionary#X|XmlDocument]]¶
Prior to .NET Framework version 4.5.2, System.Xml.XmlDocument is unsafe by default. The XmlDocument object has an XmlResolver object within it that needs to be set to null in versions prior to 4.5.2. In versions 4.5.2 and up, this XmlResolver is set to null by default.
The following example shows how it is made safe:
 static void LoadXML()
 {
   string xxePayload = "<![[_content/dictionary#D|DOCTYPE]] doc [<![[_content/dictionary#E|ENTITY]] win [[_content/dictionary#S|SYSTEM]] 'file:///C:/Users/testdata2.txt'>]>"
                     + "<doc>&win;</doc>";
   string xml = "<?xml version='1.0' ?>" + xxePayload;

   [[_content/dictionary#X|XmlDocument]] xmlDoc = new XmlDocument();
   // Setting this to [[_content/dictionary#N|NULL]] disables DTDs - Its [[_content/dictionary#N|NOT]] null by default.
   xmlDoc.[[_content/dictionary#X|XmlResolver]] = null;
   xmlDoc.[[_content/dictionary#L|LoadXml]](xml);
   Console.[[_content/dictionary#W|WriteLine]](xmlDoc.[[_content/dictionary#I|InnerText]]);
   Console.[[_content/dictionary#R|ReadLine]]();
 }

For .NET Framework version ≥4.5.2, this is safe by default.
[[_content/dictionary#X|XmlDocument]] can become unsafe if you create your own nonnull [[_content/dictionary#X|XmlResolver]] with default or unsafe settings. If you need to enable [[_content/dictionary#D|DTD]] processing, instructions on how to do so safely are described in detail in the [[referenced [[_content/dictionary#M|MSDN]] article](https://msdn.microsoft.com/en-us/magazine/ee335713.aspx)](https://msdn.microsoft.com/en-us/magazine/ee335713.aspx).
#### [[_content/dictionary#X|XmlNodeReader]]¶
System.Xml.XmlNodeReader objects are safe by default and will ignore DTDs even when constructed with an unsafe parser or wrapped in another unsafe parser.
#### [[_content/dictionary#X|XmlReader]]¶
System.Xml.XmlReader objects are safe by default.
They are set by default to have their [[_content/dictionary#P|ProhibitDtd]] property set to false in .NET Framework versions 4.0 and earlier, or their [[_content/dictionary#D|DtdProcessing]] property set to Prohibit in .NET versions 4.0 and later.
Additionally, in .NET versions 4.5.2 and later, the [[_content/dictionary#X|XmlReaderSettings]] belonging to the XmlReader has its XmlResolver set to null by default, which provides an additional layer of safety.
Therefore, XmlReader objects will only become unsafe in version 4.5.2 and up if both the DtdProcessing property is set to Parse and the [[_content/dictionary#X|XmlReaderSetting]]'s XmlResolver is set to a nonnull XmlResolver with default or unsafe settings. If you need to enable DTD processing, instructions on how to do so safely are described in detail in the referenced MSDN article.
#### [[_content/dictionary#X|XmlTextReader]]¶
System.Xml.XmlTextReader is unsafe by default in .NET Framework versions prior to 4.5.2. Here is how to make it safe in various .NET versions:
##### Prior to .[[_content/dictionary#N|NET]] 4.0¶
In .NET Framework versions prior to 4.0, DTD parsing behavior for XmlReader objects like XmlTextReader are controlled by the Boolean ProhibitDtd property found in the System.Xml.XmlReaderSettings and System.Xml.XmlTextReader classes.
Set these values to true to disable inline DTDs completely.
XmlTextReader reader = new XmlTextReader(stream);
// [[_content/dictionary#N|NEEDED]] because the default is [[_content/dictionary#F|FALSE]]!!
reader.ProhibitDtd = true;  

##### .[[_content/dictionary#N|NET]] 4.0 - .NET 4.5.2¶
In .NET Framework version 4.0, [[_content/dictionary#D|DTD]] parsing behavior has been changed. The [[_content/dictionary#P|ProhibitDtd]] property has been deprecated in favor of the new [[_content/dictionary#D|DtdProcessing]] property.
However, they didn't change the default settings so [[_content/dictionary#X|XmlTextReader]] is still vulnerable to [[_content/dictionary#X|XXE]] by default.
Setting DtdProcessing to Prohibit causes the runtime to throw an exception if a <![[_content/dictionary#D|DOCTYPE]]> element is present in the [[_content/dictionary#X|XML]].
To set this value yourself, it looks like this:
XmlTextReader reader = new XmlTextReader(stream);
// [[_content/dictionary#N|NEEDED]] because the default is Parse!!
reader.DtdProcessing = DtdProcessing.Prohibit;  

Alternatively, you can set the [[_content/dictionary#D|DtdProcessing]] property to Ignore, which will not throw an exception on encountering a <![[_content/dictionary#D|DOCTYPE]]> element but will simply skip over it and not process it. Finally, you can set DtdProcessing to Parse if you do want to allow and process inline DTDs.
##### .[[_content/dictionary#N|NET]] 4.5.2 and later¶
In .NET Framework versions 4.5.2 and up, [[_content/dictionary#X|XmlTextReader]]'s internal [[_content/dictionary#X|XmlResolver]] is set to null by default, making the XmlTextReader ignore DTDs by default. The XmlTextReader can become unsafe if you create your own nonnull XmlResolver with default or unsafe settings.
#### XPathNavigator¶
System.Xml.[[_content/dictionary#X|XPath]].XPathNavigator is unsafe by default in .NET Framework versions prior to 4.5.2.
This is due to the fact that it implements IXPathNavigable objects like [[_content/dictionary#X|XmlDocument]], which are also unsafe by default in versions prior to 4.5.2.
You can make XPathNavigator safe by giving it a safe parser like [[_content/dictionary#X|XmlReader]] (which is safe by default) in the XPathDocument's constructor.
Here is an example:
XmlReader reader = XmlReader.Create("example.xml");
XPathDocument doc = new XPathDocument(reader);
XPathNavigator nav = doc.[[_content/dictionary#C|CreateNavigator]]();
string xml = nav.[[_content/dictionary#I|InnerXml]].[[_content/dictionary#T|ToString]]();

For .[[_content/dictionary#N|NET]] Framework version ≥4.5.2, XPathNavigator is safe by default.
#### [[_content/dictionary#X|XslCompiledTransform]]¶
System.Xml.Xsl.XslCompiledTransform (an [[_content/dictionary#X|XML]] transformer) is safe by default as long as the parser it's given is safe.
It is safe by default because the default parser of the Transform() methods is an [[_content/dictionary#X|XmlReader]], which is safe by default (per above).
[The source code for this method is here.](http://www.dotnetframework.org/default.aspx/4@0/4@0/DEVDIV_TFS/Dev10/Releases/RTMRel/ndp/fx/src/Xml/System/Xml/Xslt/XslCompiledTransform@cs/1305376/XslCompiledTransform@cs)
Some of the Transform() methods accept an XmlReader or IXPathNavigable (e.g., [[_content/dictionary#X|XmlDocument]]) as an input, and if you pass in an unsafe XML Parser then the Transform will also be unsafe.
### iOS¶
libxml2¶
iOS includes the C/C++ libxml2 library described above, so that guidance applies if you are using libxml2 directly.
However, the version of libxml2 provided up through iOS6 is prior to version 2.9 of libxml2 (which protects against [[_content/dictionary#X|XXE]] by default).
#### NSXMLDocument¶
iOS also provides an NSXMLDocument type, which is built on top of libxml2.
However, NSXMLDocument provides some additional protections against XXE that aren't available in libxml2 directly.
Per the 'NSXMLDocument External Entity Restriction [[_content/dictionary#A|API]]' section of this [page](https://developer.apple.com/library/archive/releasenotes/Foundation/[[_content/dictionary#R|RN]]-Foundation-iOS/Foundation_iOS5.html):

- iOS4 and earlier: All external entities are loaded by default.
- iOS5 and later: Only entities that don't require network access are loaded. (which is safer)

However, to completely disable [[_content/dictionary#X|XXE]] in an NSXMLDocument in any version of iOS you simply specify NSXMLNodeLoadExternalEntitiesNever when creating the NSXMLDocument.
### [[_content/dictionary#P|PHP]]¶
When using the default [[_content/dictionary#X|XML]] parser (based on libxml2), PHP 8.0 and newer [prevent XXE by default](https://www.php.net/manual/en/function.libxml-disable-entity-loader.php).
For PHP versions prior to 8.0, per [the PHP documentation](https://www.php.net/manual/en/function.libxml-set-external-entity-loader.php), the following should be set when using the default PHP XML parser in order to prevent XXE:
libxml_set_external_entity_loader(null);

A description of how to abuse this in [[_content/dictionary#P|PHP]] is presented in a good [[[_content/dictionary#S|SensePost]] article](https://www.sensepost.com/blog/2014/revisting-xxe-and-abusing-protocols/) describing a cool PHP based [[_content/dictionary#X|XXE]] vulnerability that was fixed in Facebook.
### Python¶
The Python 3 official documentation contains a section on [xml vulnerabilities](https://docs.python.org/3/library/xml.html#xml-vulnerabilities). As of the 1st January 2020 Python 2 is no longer supported, however the Python website still contains [some legacy documentation](https://docs.Python.org/2/library/xml.html#xml-vulnerabilities).
The table below shows you which various [[_content/dictionary#X|XML]] parsing modules in Python 3 are vulnerable to certain XXE attacks.

Attack Type
sax
etree
minidom
pulldom
xmlrpc

Billion Laughs
Vulnerable
Vulnerable
Vulnerable
Vulnerable
Vulnerable

Quadratic Blowup
Vulnerable
Vulnerable
Vulnerable
Vulnerable
Vulnerable

External Entity Expansion
Safe
Safe
Safe
Safe
Safe

[[_content/dictionary#D|DTD]] Retrieval
Safe
Safe
Safe
Safe
Safe

Decompression Bomb
Safe
Safe
Safe
Safe
Vulnerable

To protect your application from the applicable attacks, [two packages](https://docs.python.org/3/library/xml.html#the-defusedxml-and-defusedexpat-packages) exist to help you sanitize your input and protect your application against [[_content/dictionary#D|DDoS]] and remote attacks.
### Semgrep Rules¶
Semgrep is a command-line tool for offline static analysis. Use pre-built or custom rules to enforce code and security standards in your codebase.
Java¶
Below are the rules for different [[_content/dictionary#X|XML]] parsers in Java
##### Digester¶
Identifying [[_content/dictionary#X|XXE]] vulnerability in the org.apache.commons.digester3.Digester library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-Digester](https://semgrep.dev/s/salecharohit:xxe-Digester)
##### [[_content/dictionary#D|DocumentBuilderFactory]]¶
Identifying XXE vulnerability in the javax.xml.parsers.DocumentBuilderFactory library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-dbf](https://semgrep.dev/s/salecharohit:xxe-dbf)
SAXBuilder¶
Identifying XXE vulnerability in the org.jdom2.input.SAXBuilder library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-saxbuilder](https://semgrep.dev/s/salecharohit:xxe-saxbuilder)
##### SAXParserFactory¶
Identifying XXE vulnerability in the javax.xml.parsers.SAXParserFactory library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-SAXParserFactory](https://semgrep.dev/s/salecharohit:xxe-SAXParserFactory)
SAXReader¶
Identifying XXE vulnerability in the org.dom4j.io.SAXReader library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-SAXReader](https://semgrep.dev/s/salecharohit:xxe-SAXReader)
##### XMLInputFactory¶
Identifying XXE vulnerability in the javax.xml.stream.XMLInputFactory library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-XMLInputFactory](https://semgrep.dev/s/salecharohit:xxe-XMLInputFactory)
XMLReader¶
Identifying XXE vulnerability in the org.xml.sax.XMLReader library
Rule can be played here [https://semgrep.dev/s/salecharohit:xxe-XMLReader](https://semgrep.dev/s/salecharohit:xxe-XMLReader)
### References¶

[- [[_content/dictionary#X|XXE]] by [[_content/dictionary#I|InfoSecInstitute]]](https://resources.infosecinstitute.com/identify-mitigate-xxe-vulnerabilities/)
[- [[_content/dictionary#O|OWASP]] Top 10-2017 A4: [[_content/dictionary#X|XML]] External Entities (XXE)](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A4-XML_External_Entities_%28XXE%29)
Timothy Morgan's 2014 paper: "XML Schema, [[_content/dictionary#D|DTD]], and Entity Attacks"
[- [[_content/dictionary#F|FindSecBugs]] XXE Detection](https://find-sec-bugs.github.io/bugs.htm#XXE_SAXPARSER)
[- XXEbugFind Tool](https://github.com/ssexxe/XXEBugFind)
[- Testing for XML Injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/07-Testing_for_XML_Injection.html)