---
title: "Deserialization Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html"
created: "1741872881.8246207"
tags: [owasp, cheatsheet, security]
---
# Deserialization

## Deserialization Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#references)](#detection-tools)](#mitigation-toolslibraries)](#only-deserialize-signed-data)](#using-alternative-data-formats)](#language-agnostic-methods-for-deserializing-safely)](#known-net-rce-gadgets)](#general-precautions)](#opaque-box-review_2)](#clear-box-review_3)](#net-csharp)](#other-deserialization-libraries-and-formats)](#harden-all-javaioobjectinputstream-usage-with-an-agent)](#harden-your-own-javaioobjectinputstream)](#prevent-deserialization-of-domain-objects)](#prevent-data-leakage-and-trusted-field-clobbering)](#opaque-box-review_1)](#clear-box-review_2)](#java)](#clear-box-review_1)](#opaque-box-review)](#python)](#clear-box-review)](#php)](#guidance-on-deserializing-objects-safely)](#what-is-deserialization)](#introduction)](#deserialization-cheat-sheet)
### Introduction¶
This article is focused on providing clear, actionable guidance for safely deserializing untrusted data in your applications.
### What is Deserialization¶
Serialization is the process of turning some object into a data format that can be restored later. People often serialize objects in order to save them for storage, or to send as part of communications.
Deserialization is the reverse of that process, taking data structured in some format, and rebuilding it into an object. Today, the most popular data format for serializing data is [[_content/dictionary#J|JSON]]. Before that, it was [[_content/dictionary#X|XML]].
However, many programming languages have native ways to serialize objects. These native formats usually offer more features than JSON or XML, including customization of the serialization process.
Unfortunately, the features of these native deserialization mechanisms can sometimes be repurposed for malicious effect when operating on untrusted data. Attacks against deserializers have been found to allow denial-of-service, access control, or remote code execution ([[_content/dictionary#R|RCE]]) attacks.
### Guidance on Deserializing Objects Safely¶
The following language-specific guidance attempts to enumerate safe methodologies for deserializing data that can't be trusted.
#### [[_content/dictionary#P|PHP]]¶
##### ##### ##### ##### Clear-box Review¶
Check the use of [unserialize()](https://www.php.net/manual/en/function.unserialize.php) function and review how the external parameters are accepted. Use a safe, standard data interchange format such as JSON (via json_decode() and json_encode()) if you need to pass serialized data to the user.
#### Python¶
##### ##### ##### Opaque-box Review¶
If the traffic data contains the symbol dot . at the end, it's very likely that the data was sent in serialization. It will be only true if the data is not being encoded using Base64 or Hexadecimal schemas. If the data is being encoded, then it's best to check if the serialization is likely happening or not by looking at the starting characters of the parameter value. For example if data is Base64 encoded, then it will most likely start with gASV.
Clear-box Review¶
The following [[_content/dictionary#A|API]] in Python will be vulnerable to serialization attack. Search code for the pattern below.

1. The uses of pickle/c_pickle/_pickle with load/loads:

import pickle
data = """ cos.system(S'dir')tR. """
pickle.loads(data)

1. Uses of PyYAML with load:

import yaml
document = "!!python/object/apply:os.system ['ipconfig']"
print(yaml.load(document))

1. Uses of jsonpickle with encode or store methods.

#### Java¶
The following techniques are all good for preventing attacks against deserialization against [[Java's Serializable format](https://docs.oracle.com/javase/7/docs/api/java/io/Serializable.html)](https://docs.oracle.com/javase/7/docs/api/java/io/Serializable.html).
Implementation advice:

In your code, override the [[_content/dictionary#O|ObjectInputStream]]#resolveClass() method to prevent arbitrary classes from being deserialized. This safe behavior can be wrapped in a library like [[[_content/dictionary#S|SerialKiller]]](https://github.com/ikkisoft/SerialKiller).
Use a safe replacement for the generic readObject() method as seen [here](https://github.com/wsargent/paranoid-java-serialization). Note that this addresses "[billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack)" type attacks by checking input length and number of objects deserialized.

Clear-box Review¶
Be aware of the following Java [[_content/dictionary#A|API]] uses for potential serialization vulnerability.
1. XMLdecoder with external user defined parameters
2. XStream with fromXML method (xstream version <= v1.4.6 is vulnerable to the serialization issue)
3. [[_content/dictionary#O|ObjectInputStream]] with readObject
4. Uses of readObject, readObjectNoData, readResolve or readExternal
5. ObjectInputStream.readUnshared
6. Serializable
Opaque-box Review¶
If the captured traffic data includes the following patterns, it may suggest that the data was sent in Java serialization streams:

- [[_content/dictionary#A|AC]] [[_content/dictionary#E|ED]] 00 05 in Hex
- rO0 in Base64
- Content-type header of an [[_content/dictionary#H|HTTP]] response set to application/x-java-serialized-object

##### Prevent Data Leakage and Trusted Field Clobbering¶
If there are data members of an object that should never be controlled by end users during deserialization or exposed to users during serialization, they should be declared as [the transient keyword](https://docs.oracle.com/javase/7/docs/platform/serialization/spec/serial-arch.html#7231) (section Protecting Sensitive Information).
For a class that defined as Serializable, the sensitive information variable should be declared as private transient.
For example, the class myAccount, the variables 'profit' and 'margin' were declared as transient to prevent them from being serialized.
public class myAccount implements Serializable
{
    private transient double profit; // declared transient

    private transient double margin; // declared transient
    ....

##### Prevent Deserialization of Domain Objects¶
Some of your application objects may be forced to implement Serializable due to their hierarchy. To guarantee that your application objects can't be deserialized, a readObject() method should be declared (with a final modifier) which always throws an exception:
private final void readObject([[_content/dictionary#O|ObjectInputStream]] in) throws java.io.IOException {
    throw new java.io.IOException("Cannot be deserialized");
}

##### Harden Your Own java.io.[[_content/dictionary#O|ObjectInputStream]]¶
The java.io.ObjectInputStream class is used to deserialize objects. It's possible to harden its behavior by subclassing it. This is the best solution if:

- you can change the code that does the deserialization;
- you know what classes you expect to deserialize.

The general idea is to override [[[_content/dictionary#O|ObjectInputStream]].html#resolveClass()](http://docs.oracle.com/javase/7/docs/api/java/io/ObjectInputStream.html#resolveClass(java.io.[[_content/dictionary#O|ObjectStreamClass]])) in order to restrict which classes are allowed to be deserialized.
Because this call happens before a readObject() is called, you can be sure that no deserialization activity will occur unless the type is one that you allow.
A simple example is shown here, where the [[_content/dictionary#L|LookAheadObjectInputStream]] class is guaranteed to not deserialize any other type besides the Bicycle class:
public class LookAheadObjectInputStream extends ObjectInputStream {

    public [[_content/dictionary#L|LookAheadObjectInputStream]]([[_content/dictionary#I|InputStream]] inputStream) throws IOException {
        super(inputStream);
    }

    /**
    * Only deserialize instances of our expected Bicycle class
    */
    @Override
    protected Class<?> resolveClass([[_content/dictionary#O|ObjectStreamClass]] desc) throws IOException, [[_content/dictionary#C|ClassNotFoundException]] {
        if (!desc.getName().equals(Bicycle.class.getName())) {
            throw new [[_content/dictionary#I|InvalidClassException]]("Unauthorized deserialization attempt", desc.getName());
        }
        return super.resolveClass(desc);
    }
}

More complete implementations of this approach have been proposed by various community members:

[[[_content/dictionary#N|NibbleSec]]](https://github.com/ikkisoft/[[_content/dictionary#S|SerialKiller]]) - a library that allows creating lists of classes that are allowed to be deserialized
[IBM](https://www.ibm.com/developerworks/library/se-lookahead/) - the seminal protection, written years before the most devastating exploitation scenarios were envisioned.
[- Apache Commons [[_content/dictionary#I|IO]] classes](https://commons.apache.org/proper/commons-io/javadocs/api-2.5/org/apache/commons/io/serialization/[[_content/dictionary#V|ValidatingObjectInputStream]].html)

##### Harden All java.io.[[_content/dictionary#O|ObjectInputStream]] Usage with an Agent¶
As mentioned above, the java.io.ObjectInputStream class is used to deserialize objects. It's possible to harden its behavior by subclassing it. However, if you don't own the code or can't wait for a patch, using an agent to weave in hardening to java.io.ObjectInputStream is the best solution.
Globally changing ObjectInputStream is only safe for block-listing known malicious types, because it's not possible to know for all applications what the expected classes to be deserialized are. Fortunately, there are very few classes needed in the denylist to be safe from all the known attack vectors, today.
It's inevitable that more "gadget" classes will be discovered that can be abused. However, there is an incredible amount of vulnerable software exposed today, in need of a fix. In some cases, "fixing" the vulnerability may involve re-architecting messaging systems and breaking backwards compatibility as developers move towards not accepting serialized objects.
To enable these agents, simply add a new [[_content/dictionary#J|JVM]] parameter:
-javaagent:name-of-agent.jar

Agents taking this approach have been released by various community members:

[- rO0 by Contrast Security](https://github.com/Contrast-Security-[[_content/dictionary#O|OSS]]/contrast-rO0)

A similar, but less scalable approach would be to manually patch and bootstrap your [[_content/dictionary#J|JVM]]'s [[_content/dictionary#O|ObjectInputStream]]. Guidance on this approach is available here.
##### Other Deserialization Libraries and Formats¶
While the advice above is focused on Java's Serializable format, there are a number of other libraries
that use other formats for deserialization. Many of these libraries may have similar security
issues if not configured correctly. This section lists some of these libraries and
recommended configuration options to avoid security issues when deserializing untrusted data:
Can be used safely with default configuration:
The following libraries can be used safely with default configuration:

[fastjson2](https://github.com/alibaba/fastjson2) ([[_content/dictionary#J|JSON]]) - can be used safely as long as
the [autotype](https://github.com/alibaba/fastjson2/wiki/fastjson2_autotype_cn) option is not turned on
[jackson-databind](https://github.com/FasterXML/jackson-databind) (JSON) - can be used safely as long
as polymorphism is not used ([see blog post](https://cowtowncoder.medium.com/on-jackson-cves-dont-panic-here-is-what-you-need-to-know-54cd0d6e8062))
[Kryo v5.0.0+](https://github.com/[[_content/dictionary#E|EsotericSoftware]]/kryo) (custom format) - can be used safely
as long as class registration is not turned off ([[[[[see [documentation](https://x-stream.github.io/security.html#explicit)](https://github.com/alibaba/fastjson/wiki/enable_autotype)](https://github.com/EsotericSoftware/kryo#optional-registration)](https://github.com/alibaba/fastjson/wiki/enable_autotype)](https://x-stream.github.io/security.html)](https://github.com/EsotericSoftware/kryo#optional-registration)
and [[this issue](https://github.com/EsotericSoftware/kryo/issues/929)](https://github.com/EsotericSoftware/kryo/issues/929))
[[[_content/dictionary#Y|YamlBeans]] v1.16+](https://github.com/EsotericSoftware/yamlbeans) ([[_content/dictionary#Y|YAML]]) - can be used safely
as long as the [[_content/dictionary#U|UnsafeYamlConfig]] class isn't used (see [this commit](https://github.com/EsotericSoftware/yamlbeans/commit/b1122588e7610ae4e0d516c50d08c94ee87946e6))
[[_content/dictionary#N|NOTE]]: because these versions are not available in Maven Central,
[a fork exists](https://github.com/Contrast-Security-[[_content/dictionary#O|OSS]]/yamlbeans) that can be used instead.

[XStream v1.4.17+](https://x-stream.github.io/) ([[_content/dictionary#J|JSON]] and [[_content/dictionary#X|XML]]) - can be used safely
as long as the allowlist and other security controls are not relaxed (see documentation)

Requires configuration before can be used safely:
The following libraries require configuration options to be set before they can be used safely:

[fastjson v1.2.68+](https://github.com/alibaba/fastjson) ([[_content/dictionary#J|JSON]]) - cannot be used safely unless
the [safemode](https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en) option is turned on, which disables
deserialization of any class (see documentation).
Previous versions are not safe.
[json-io](https://github.com/jdereg/json-io) (JSON) - cannot be used safely since the use of @type property in
JSON allows deserialization of any class. Can only be used safely in following situations:
In [non-typed mode](https://github.com/jdereg/json-io/blob/master/user-guide.md#non-typed-usage) using the [[_content/dictionary#J|JsonReader]].USE_MAPS setting which turns off generic object deserialization
[With a custom deserializer](https://github.com/jdereg/json-io/blob/master/user-guide.md#customization-technique-4-custom-serializer) controlling which classes get deserialized

[Kryo < v5.0.0](https://github.com/[[_content/dictionary#E|EsotericSoftware]]/kryo) (custom format) - cannot be used safely unless class registration is turned on,
which disables deserialization of any class (see documentation
and this issue)
[[_content/dictionary#N|NOTE]]: other wrappers exist around Kryo such as [Chill](https://github.com/twitter/chill), which may also have class registration
not required by default regardless of the underlying version of Kryo being used

[SnakeYAML](https://bitbucket.org/snakeyaml/snakeyaml/src) ([[_content/dictionary#Y|YAML]]) - cannot be used safely unless
the org.yaml.snakeyaml.constructor.[[_content/dictionary#S|SafeConstructor]] class is used, which disables
deserialization of any class ([see docs](https://bitbucket.org/snakeyaml/snakeyaml/wiki/[[_content/dictionary#C|CVE]]-2022-1471))

Cannot be used safely:
The following libraries are either no longer maintained or cannot be used safely with untrusted input:

[Castor](https://github.com/castor-data-binding/castor) ([[_content/dictionary#X|XML]]) - appears to be abandoned with no commits since 2016
[fastjson < v1.2.68](https://github.com/alibaba/fastjson) ([[_content/dictionary#J|JSON]]) - these versions allows deserialization of any class
(see documentation)
[XMLDecoder in the [[_content/dictionary#J|JDK]]](https://docs.oracle.com/javase/8/docs/api/java/beans/XMLDecoder.html) (XML) - "close to impossible to securely deserialize Java objects in this format from untrusted inputs"
("Red Hat Defensive Coding Guide", [end of section 2.6.5](https://redhat-crypto.gitlab.io/defensive-coding-guide/#sect-Defensive_Coding-Tasks-Serialization-XML))
[XStream < v1.4.17](https://x-stream.github.io/) (JSON and XML) - these versions allows deserialization of any class (see documentation)
[[[_content/dictionary#Y|YamlBeans]] < v1.16](https://github.com/[[_content/dictionary#E|EsotericSoftware]]/yamlbeans) ([[_content/dictionary#Y|YAML]]) - these versions allows deserialization of any class
(see [this document](https://github.com/Contrast-Security-[[_content/dictionary#O|OSS]]/yamlbeans/blob/main/[[_content/dictionary#S|SECURITY]].md))

#### .Net CSharp¶
Clear-box Review¶
Search the source code for the following terms:

1. [[_content/dictionary#T|TypeNameHandling]]
2. [[_content/dictionary#J|JavaScriptTypeResolver]]

Look for any serializers where the type is set by a user controlled variable.
Opaque-box Review¶
Search for the following base64 encoded content that starts with:
AAEAAAD/////

Search for content with the following text:

1. [[_content/dictionary#T|TypeObject]]
2. $type:

##### General Precautions¶
Microsoft has stated that the [[_content/dictionary#B|BinaryFormatter]] type is dangerous and cannot be secured. As such, it should not be used. Full details are in the [BinaryFormatter security guide](https://docs.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide).
Don't allow the datastream to define the type of object that the stream will be deserialized to. You can prevent this by for example using the [[_content/dictionary#D|DataContractSerializer]] or [[_content/dictionary#X|XmlSerializer]] if at all possible.
Where [[_content/dictionary#J|JSON]].Net is being used make sure the [[_content/dictionary#T|TypeNameHandling]] is only set to None.
TypeNameHandling = TypeNameHandling.None

If [[_content/dictionary#J|JavaScriptSerializer]] is to be used then do not use it with a [[_content/dictionary#J|JavaScriptTypeResolver]].
If you must deserialize data streams that define their own type, then restrict the types that are allowed to be deserialized. One should be aware that this is still risky as many native .Net types potentially dangerous in themselves. e.g.
System.[[_content/dictionary#I|IO]].[[_content/dictionary#F|FileInfo]]

[[_content/dictionary#F|FileInfo]] objects that reference files actually on the server can when deserialized, change the properties of those files e.g. to read-only, creating a potential denial of service attack.
Even if you have limited the types that can be deserialized remember that some types have properties that are risky. System.[[_content/dictionary#C|ComponentModel]].[[_content/dictionary#D|DataAnnotations]].[[_content/dictionary#V|ValidationException]], for example has a property Value of type Object. if this type is the type allowed for deserialization then an attacker can set the Value property to any object type they choose.
Attackers should be prevented from steering the type that will be instantiated. If this is possible then even [[_content/dictionary#D|DataContractSerializer]] or [[_content/dictionary#X|XmlSerializer]] can be subverted e.g.
// Action below is dangerous if the attacker can change the data in the database
var typename = [[_content/dictionary#G|GetTransactionTypeFromDatabase]]();

var serializer = new [[_content/dictionary#D|DataContractJsonSerializer]](Type.[[_content/dictionary#G|GetType]](typename));

var obj = serializer.[[_content/dictionary#R|ReadObject]](ms);

Execution can occur within certain .Net types during deserialization. Creating a control such as the one shown below is ineffective.
var suspectObject = myBinaryFormatter.Deserialize(untrustedData);

//Check below is too late! Execution may have already occurred.
if (suspectObject is [[_content/dictionary#S|SomeDangerousObjectType]])
{
    //generate warnings and dispose of suspectObject
}

For [[_content/dictionary#J|JSON]].Net it is possible to create a safer form of allow-list control using a custom [[_content/dictionary#S|SerializationBinder]].
Try to keep up-to-date on known .Net insecure deserialization gadgets and pay special attention where such types can be created by your deserialization processes. A deserializer can only instantiate types that it knows about.
Try to keep any code that might create potential gadgets separate from any code that has internet connectivity. As an example - System.Windows.Data.[[_content/dictionary#O|ObjectDataProvider]] used in [[_content/dictionary#W|WPF]] applications is a known gadget that allows arbitrary method invocation. It would be risky to have this a reference to this assembly in a [[_content/dictionary#R|REST]] service project that deserializes untrusted data.
##### Known .[[_content/dictionary#N|NET]] [[_content/dictionary#R|RCE]] Gadgets¶

- System.Configuration.Install.[[_content/dictionary#A|AssemblyInstaller]]
- System.Activities.Presentation.[[_content/dictionary#W|WorkflowDesigner]]
- System.Windows.[[_content/dictionary#R|ResourceDictionary]]
System.Windows.Data.[[_content/dictionary#O|ObjectDataProvider]]
- System.Windows.Forms.[[_content/dictionary#B|BindingSource]]
- Microsoft.Exchange.Management.[[_content/dictionary#S|SystemManager]].[[_content/dictionary#W|WinForms]].[[_content/dictionary#E|ExchangeSettingsProvider]]
- System.Data.[[_content/dictionary#D|DataViewManager]], System.Xml.[[_content/dictionary#X|XmlDocument]]/[[_content/dictionary#X|XmlDataDocument]]
- System.Management.Automation.PSObject

### Language-Agnostic Methods for Deserializing Safely¶
#### Using Alternative Data Formats¶
A great reduction of risk is achieved by avoiding native (de)serialization formats. By switching to a pure data format like [[_content/dictionary#J|JSON]] or [[_content/dictionary#X|XML]], you lessen the chance of custom deserialization logic being repurposed towards malicious ends.
Many applications rely on a [data-transfer object pattern](https://en.wikipedia.org/wiki/Data_transfer_object) that involves creating a separate domain of objects for the explicit purpose data transfer. Of course, it's still possible that the application will make security mistakes after a pure data object is parsed.
#### Only Deserialize Signed Data¶
If the application knows before deserialization which messages will need to be processed, they could sign them as part of the serialization process. The application could then to choose not to deserialize any message which didn't have an authenticated signature.
### Mitigation Tools/Libraries¶

[[[- - - Java secure deserialization library](https://github.com/ikkisoft/[[_content/dictionary#S|SerialKiller]])](https://github.com/ikkisoft/SerialKiller)](https://github.com/ikkisoft/SerialKiller)
[- [[_content/dictionary#S|SWAT]] - tool for creating allowlists](https://github.com/cschneider4711/SWAT)
[- [[_content/dictionary#N|NotSoSerial]]](https://github.com/kantega/notsoserial)

### Detection Tools¶

[[- - Java deserialization cheat sheet aimed at pen testers](https://github.com/[[_content/dictionary#G|GrrrDog]]/- Java-Deserialization-Cheat-Sheet)](https://github.com/GrrrDog/[Java-Deserialization-Cheat-Sheet](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet))
[[- - A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.](https://github.com/frohoff/ysoserial)](https://github.com/frohoff/ysoserial)
[[- - Java De-serialization toolkits](https://github.com/brianwrf/hackUtils)](https://github.com/brianwrf/hackUtils)
[[- - Java de-serialization tool](https://github.com/frohoff/ysoserial)](https://github.com/frohoff/ysoserial)
[- .Net payload generator](https://github.com/pwntester/ysoserial.net)
[[- - Burp Suite extension](https://github.com/federicodotta/Java-Deserialization-Scanner/releases)](https://github.com/federicodotta/Java-Deserialization-Scanner/releases)
Java secure deserialization library
[[- - Serianalyzer is a static bytecode analyzer for deserialization](https://github.com/mbechler/serianalyzer)](https://github.com/mbechler/serianalyzer)
[[- - Payload generator](https://github.com/mbechler/marshalsec)](https://github.com/mbechler/marshalsec)
[[- - Android Java Deserialization Vulnerability Tester](https://github.com/modzero/modjoda)](https://github.com/modzero/modjoda)
Burp Suite Extension
[[- - - - [[_content/dictionary#J|JavaSerialKiller]]](https://github.com/NetSPI/JavaSerialKiller)](https://github.com/NetSPI/JavaSerialKiller)
[[- - - - Java Deserialization Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner)](https://github.com/federicodotta/Java-Deserialization-Scanner)
[[- - - - Burp-ysoserial](https://github.com/summitt/burp-ysoserial)](https://github.com/summitt/burp-ysoserial)
[[- - - - [[_content/dictionary#S|SuperSerial]]](https://github.com/[[_content/dictionary#D|DirectDefense]]/SuperSerial)](https://github.com/DirectDefense/SuperSerial)
[[- - - - SuperSerial-Active](https://github.com/DirectDefense/SuperSerial-Active)](https://github.com/DirectDefense/SuperSerial-Active)

### References¶

Java-Deserialization-Cheat-Sheet
[- Deserialization of untrusted data](https://owasp.org/www-community/vulnerabilities/Deserialization_of_untrusted_data)
[- Java Deserialization Attacks - German [[_content/dictionary#O|OWASP]] Day 2016](../assets/Deserialization_Cheat_Sheet_GOD16Deserialization.pdf)
[- [[_content/dictionary#A|AppSecCali]] 2015 - Marshalling Pickles](http://www.slideshare.net/frohoff1/appseccali-2015-marshalling-pickles)
[- [[_content/dictionary#F|FoxGlove]] Security - Vulnerability Announcement](http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/#websphere)
Java deserialization cheat sheet aimed at pen testers
A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.
Java De-serialization toolkits
Java de-serialization tool
Burp Suite extension
Java secure deserialization library
Serianalyzer is a static bytecode analyzer for deserialization
Payload generator
Android Java Deserialization Vulnerability Tester
- - Burp Suite Extension
[[_content/dictionary#J|JavaSerialKiller]]
Java Deserialization Scanner
Burp-ysoserial
[[_content/dictionary#S|SuperSerial]]
SuperSerial-Active

.Net
[- - Alvaro Muñoz: .[[_content/dictionary#N|NET]] Serialization: Detecting and defending vulnerable endpoints](https://www.youtube.com/watch?v=qDoBlLwREYk)
[- - James Forshaw - Black Hat [[_content/dictionary#U|USA]] 2012 - Are You My Type? Breaking .net Sandboxes Through Serialization](https://www.youtube.com/watch?v=Xfbu-pQ1tIc)
[- - Jonathan Birch [[_content/dictionary#B|BlueHat]] v17 - Dangerous Contents - Securing .Net Deserialization](https://www.youtube.com/watch?v=oxlD8VWWHE8)
[- - Alvaro Muñoz & Oleksandr Mirosh - Friday the 13th: Attacking [[_content/dictionary#J|JSON]] - AppSecUSA 2017](https://www.youtube.com/watch?v=NqHsaVhlxAQ)

Python
[- - Exploiting Insecure Deserialization bugs found in the Wild (Python Pickles)](https://macrosec.tech/index.php/2021/06/29/exploiting-insecuredeserialization-bugs-found-in-the-wild-python-pickles.)