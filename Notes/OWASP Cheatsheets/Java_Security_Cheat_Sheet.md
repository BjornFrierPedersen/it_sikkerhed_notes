---
title: "Java Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Java_Security_Cheat_Sheet.html"
created: "1741872881.9458601"
tags: [owasp, cheatsheet, security]
---
# Java Security

## Java Security Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#asymmetric-example-using-built-in-jcajce-classes)](#asymmetric-example-using-google-tink)](#encryption-for-transmission)](#symmetric-example-using-built-in-jcajce-classes)](#symmetric-example-using-google-tink)](#encryption-for-storage)](#general-cryptography-guidance)](#cryptography)](#references_6)](#example-using-logback)](#example-using-log4j-core-2)](#how-to-prevent_6)](#symptom_6)](#log-injection)](#references_5)](#example-mongodb)](#how-to-prevent_5)](#symptom_5)](#nosql)](#ldap)](#references_4)](#example_4)](#how-to-prevent_4)](#symptom_4)](#htmljavascriptcss)](#references_3)](#example_3)](#how-to-prevent_3)](#symptom_3)](#xml-xpath-injection)](#references_2)](#example_2)](#how-to-prevent_2)](#symptom_2)](#operating-system)](#references_1)](#example_1)](#how-to-prevent_1)](#symptom_1)](#jpa)](#references)](#example)](#how-to-prevent)](#symptom)](#sql)](#specific-injection-types)](#general-advice-to-prevent-injection)](#what-is-injection)](#injection-prevention-in-java)](#java-security-cheat-sheet)
### [Injection](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection) Prevention in Java¶
This section aims to provide tips to handle Injection in Java application code.
Sample code used in tips is located [here](https://github.com/righettod/injection-cheat-sheets).
#### What is Injection¶
Injection in [[_content/dictionary#O|OWASP]] Top 10 is defined as following:
Consider anyone who can send untrusted data to the system, including external users, internal users, and administrators.
#### General advice to prevent Injection¶
The following point can be applied, in a general way, to prevent Injection issue:

1. Apply Input Validation (using allowlist approach) combined with Output Sanitizing+Escaping on user input/output.
2. If you need to interact with system, try to use [[_content/dictionary#A|API]] features provided by your technology stack (Java / .Net / [[_content/dictionary#P|PHP]]...) instead of building command.

Additional advice is provided on this [[LDAP_Injection_Prevention_Cheat_Sheet|[cheatsheet]]](Input_Validation_Cheat_Sheet.html).
### Specific Injection types¶
Examples in this section will be provided in Java technology (see Maven project associated) but advice is applicable to others technologies like .Net / [[_content/dictionary#P|PHP]] / Ruby / Python...
#### [[_content/dictionary#S|SQL]]¶
##### ##### ##### ##### ##### ##### ##### Symptom¶
Injection of this type occur when the application uses untrusted user input to build an SQL query using a String and execute it.
##### ##### ##### ##### ##### ##### ##### How to prevent¶
Use Query Parameterization in order to prevent injection.
##### ##### ##### ##### ##### Example¶
/*No [[_content/dictionary#D|DB]] framework used here in order to show the real use of
  Prepared Statement from Java [[_content/dictionary#A|API]]*/
/*Open connection with H2 database and use it*/
Class.forName("org.h2.Driver");
String jdbcUrl = "jdbc:h2:file:" + new File(".").getAbsolutePath() + "/target/db";
try (Connection con = [[_content/dictionary#D|DriverManager]].getConnection(jdbcUrl)) {

    /* Sample A: Select data using Prepared Statement*/
    String query = "select * from color where friendly_name = ?";
    List<String> colors = new [[_content/dictionary#A|ArrayList]]<>();
    try ([[_content/dictionary#P|PreparedStatement]] pStatement = con.prepareStatement(query)) {
        pStatement.setString(1, "yellow");
        try ([[_content/dictionary#R|ResultSet]] rSet = pStatement.executeQuery()) {
            while (rSet.next()) {
                colors.add(rSet.getString(1));
            }
        }
    }

    /* Sample B: Insert data using Prepared Statement*/
    query = "insert into color(friendly_name, red, green, blue) values(?, ?, ?, ?)";
    int insertedRecordCount;
    try ([[_content/dictionary#P|PreparedStatement]] pStatement = con.prepareStatement(query)) {
        pStatement.setString(1, "orange");
        pStatement.setInt(2, 239);
        pStatement.setInt(3, 125);
        pStatement.setInt(4, 11);
        insertedRecordCount = pStatement.executeUpdate();
    }

   /* Sample C: Update data using Prepared Statement*/
    query = "update color set blue = ? where friendly_name = ?";
    int updatedRecordCount;
    try ([[_content/dictionary#P|PreparedStatement]] pStatement = con.prepareStatement(query)) {
        pStatement.setInt(1, 10);
        pStatement.setString(2, "orange");
        updatedRecordCount = pStatement.executeUpdate();
    }

   /* Sample D: Delete data using Prepared Statement*/
    query = "delete from color where friendly_name = ?";
    int deletedRecordCount;
    try ([[_content/dictionary#P|PreparedStatement]] pStatement = con.prepareStatement(query)) {
        pStatement.setString(1, "orange");
        deletedRecordCount = pStatement.executeUpdate();
    }

}

##### ##### ##### ##### ##### ##### ##### References¶

[[SQL_Injection_Prevention_Cheat_Sheet|- [[_content/dictionary#S|SQL]] Injection Prevention Cheat Sheet]]

#### [[_content/dictionary#J|JPA]]¶
Symptom¶
Injection of this type occur when the application uses untrusted user input to build a JPA query using a String and execute it. It's quite similar to [[_content/dictionary#S|SQL]] injection but here the altered language is not SQL but JPA [[_content/dictionary#Q|QL]].
How to prevent¶
Use Java Persistence Query Language Query Parameterization in order to prevent injection.
Example¶
[[_content/dictionary#E|EntityManager]] entityManager = null;
try {
    /* Get a ref on EntityManager to access [[_content/dictionary#D|DB]] */
    entityManager = Persistence.createEntityManagerFactory("testJPA").createEntityManager();

    /* Define parameterized query prototype using named parameter to enhance readability */
    String queryPrototype = "select c from Color c where c.friendlyName = :colorName";

    /* Create the query, set the named parameter and execute the query */
    Query queryObject = entityManager.createQuery(queryPrototype);
    Color c = (Color) queryObject.setParameter("colorName", "yellow").getSingleResult();

} finally {
    if (entityManager != null && entityManager.isOpen()) {
        entityManager.close();
    }
}

References¶

[- SQLi and [[_content/dictionary#J|JPA]]](https://software-security.sans.org/developer-how-to/fix-sql-injection-in-java-persistence-api-jpa)

#### Operating System¶
Symptom¶
Injection of this type occur when the application uses untrusted user input to build an Operating System command using a String and execute it.
How to prevent¶
Use technology stack API in order to prevent injection.
Example¶
/* The context taken is, for example, to perform a [[_content/dictionary#P|PING]] against a computer.
* The prevention is to use the feature provided by the Java [[_content/dictionary#A|API]] instead of building
* a system command as String and execute it */
[[_content/dictionary#I|InetAddress]] host = InetAddress.getByName("localhost");
var reachable = host.isReachable(5000);

References¶

[- Command Injection](https://owasp.org/www-community/attacks/Command_Injection)

#### [[_content/dictionary#X|XML]]: [[_content/dictionary#X|XPath]] Injection¶
Symptom¶
Injection of this type occur when the application uses untrusted user input to build a XPath query using a String and execute it.
How to prevent¶
Use XPath Variable Resolver in order to prevent injection.
Example¶
Variable Resolver implementation.
/**
 * Resolver in order to define parameter for [[_content/dictionary#X|XPATH]] expression.
 *
 */
public class [[_content/dictionary#S|SimpleVariableResolver]] implements XPathVariableResolver {

    private final Map<QName, Object> vars = new [[_content/dictionary#H|HashMap]]<QName, Object>();

    /**
     * External methods to add parameter
     *
     * @param name Parameter name
     * @param value Parameter value
     */
    public void addVariable(QName name, Object value) {
        vars.put(name, value);
    }

    /**
     * {@inheritDoc}
     *
     * @see javax.xml.xpath.XPathVariableResolver#resolveVariable(javax.xml.namespace.QName)
     */
    public Object resolveVariable(QName variableName) {
        return vars.get(variableName);
    }
}

Code using it to perform [[_content/dictionary#X|XPath]] query.
/*Create a [[_content/dictionary#X|XML]] document builder factory*/
[[_content/dictionary#D|DocumentBuilderFactory]] dbf = DocumentBuilderFactory.newInstance();

/*Disable External Entity resolution for different cases*/
//Do not performed here in order to focus on variable resolver code
//but do it for production code !

/*Load [[_content/dictionary#X|XML]] file*/
[[_content/dictionary#D|DocumentBuilder]] builder = dbf.newDocumentBuilder();
Document doc = builder.parse(new File("src/test/resources/SampleXPath.xml"));

/* Create and configure parameter resolver */
String bid = "bk102";
[[_content/dictionary#S|SimpleVariableResolver]] variableResolver = new SimpleVariableResolver();
variableResolver.addVariable(new QName("bookId"), bid);

/*Create and configure [[_content/dictionary#X|XPATH]] expression*/
[[_content/dictionary#X|XPath]] xpath = XPathFactory.newInstance().newXPath();
xpath.setXPathVariableResolver(variableResolver);
XPathExpression xPathExpression = xpath.compile("//book[@id=$bookId]");

/* Apply expression on [[_content/dictionary#X|XML]] document */
Object nodes = xPathExpression.evaluate(doc, XPathConstants.[[_content/dictionary#N|NODESET]]);
[[_content/dictionary#N|NodeList]] nodesList = (NodeList) nodes;
Element book = (Element)nodesList.item(0);
var containsRalls = book.getTextContent().contains("Ralls, Kim");

References¶

[- [[_content/dictionary#X|XPATH]] Injection](https://owasp.org/www-community/attacks/XPATH_Injection)

#### [[_content/dictionary#H|HTML]]/[[_content/dictionary#J|JavaScript]]/[[_content/dictionary#C|CSS]]¶
Symptom¶
Injection of this type occur when the application uses untrusted user input to build an [[_content/dictionary#H|HTTP]] response and sent it to browser.
How to prevent¶
Either apply strict input validation (allowlist approach) or use output sanitizing+escaping if input validation is not possible (combine both every time is possible).
Example¶
/*
[[_content/dictionary#I|INPUT]] [[_content/dictionary#W|WAY]]: Receive data from user
Here it's recommended to use strict input validation using allowlist approach.
In fact, you ensure that only allowed characters are part of the input received.
*/

String userInput = "You user login is owasp-user01";

/* First we check that the value contains only expected character*/
if (!Pattern.matches("[a-zA-Z0-9\\s\\-]{1,50}", userInput))
{
    return false;
}

/* If the first check pass then ensure that potential dangerous character
that we have allowed for business requirement are not used in a dangerous way.
For example here we have allowed the character '-', and, this can
be used in [[_content/dictionary#S|SQL]] injection so, we
ensure that this character is not used is a continuous form.
Use the [[_content/dictionary#A|API]] [[_content/dictionary#C|COMMONS]] [[_content/dictionary#L|LANG]] v3 to help in String analysis...
*/
If (0 != [[_content/dictionary#S|StringUtils]].countMatches(userInput.replace(" ", ""), "--"))
{
    return false;
}

/*
[[_content/dictionary#O|OUTPUT]] [[_content/dictionary#W|WAY]]: Send data to user
Here we escape + sanitize any data sent to user
Use the [- [[_content/dictionary#O|OWASP]] Java [[_content/dictionary#H|HTML]] Sanitizer](https://github.com/owasp/java-html-sanitizer) [[_content/dictionary#A|API]] to handle sanitizing
Use the [- OWASP Java Encoder](https://github.com/owasp/owasp-java-encoder) API to handle HTML tag encoding (escaping)
*/

String outputToUser = "You <p>user login</p> is <strong>owasp-user01</strong>";
outputToUser += "<script>alert(22);</script><img src='#' onload='javascript:alert(23);'>";

/* Create a sanitizing policy that only allow tag '<p>' and '<strong>'*/
[[_content/dictionary#P|PolicyFactory]] policy = new [[_content/dictionary#H|HtmlPolicyBuilder]]().allowElements("p", "strong").toFactory();

/* Sanitize the output that will be sent to user*/
String safeOutput = policy.sanitize(outputToUser);

/* Encode [[_content/dictionary#H|HTML]] Tag*/
safeOutput = Encode.forHtml(safeOutput);
String finalSafeOutputExpected = "You <p>user login</p> is <strong>owasp-user01</strong>";
if (!finalSafeOutputExpected.equals(safeOutput))
{
    return false;
}

References¶

[- [[_content/dictionary#X|XSS]]](https://owasp.org/www-community/attacks/xss/)
[[_content/dictionary#O|OWASP]] Java [[_content/dictionary#H|HTML]] Sanitizer
OWASP Java Encoder
[- Java [[_content/dictionary#R|RegEx]]](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)

#### [[_content/dictionary#L|LDAP]]¶
A dedicated cheatsheet has been created.
#### [[_content/dictionary#N|NoSQL]]¶
Symptom¶
Injection of this type occur when the application uses untrusted user input to build a NoSQL [[_content/dictionary#A|API]] call expression.
How to prevent¶
As there many NoSQL database system and each one use an API for call, it's important to ensure that user input received and used to build the API call expression does not contain any character that have a special meaning in the target API syntax. This in order to avoid that it will be used to escape the initial call expression in order to create another one based on crafted user input. It's also important to not use string concatenation to build API call expression but use the API to create the expression.
##### Example - MongoDB¶
 /* Here use MongoDB as target NoSQL [[_content/dictionary#D|DB]] */
String userInput = "Brooklyn";

/* First ensure that the input do no contains any special characters
for the current [[_content/dictionary#N|NoSQL]] [[_content/dictionary#D|DB]] call [[_content/dictionary#A|API]],
here they are: ' " \ ; { } $
*/
//Avoid regexp this time in order to made validation code
//more easy to read and understand...
[[_content/dictionary#A|ArrayList]] < String > specialCharsList = new ArrayList < String > () {
    {
        add("'");
        add("\"");
        add("\\");
        add(";");
        add("{");
        add("}");
        add("$");
    }
};

for (String specChar: specialCharsList) {
    if (userInput.contains(specChar)) {
        return false;
    }
}

//Add also a check on input max size
if (!userInput.length() <= 50)
{
    return false;
}

/* Then perform query on database using [[_content/dictionary#A|API]] to build expression */
//Connect to the local MongoDB instance
try([[_content/dictionary#M|MongoClient]] mongoClient = new MongoClient()){
    [[_content/dictionary#M|MongoDatabase]] db = mongoClient.getDatabase("test");
    //Use API query builder to create call expression
    //Create expression
    Bson expression = eq("borough", userInput);
    //Perform call
    [[_content/dictionary#F|FindIterable]]<org.bson.Document> restaurants = db.getCollection("restaurants").find(expression);
    //Verify result consistency
    restaurants.forEach(new Block<org.bson.Document>() {
        @Override
        public void apply(final org.bson.Document doc) {
            String restBorough = (String)doc.get("borough");
            if (!"Brooklyn".equals(restBorough))
            {
                return false;
            }
        }
    });
}

References¶

[- Testing for [[_content/dictionary#N|NoSQL]] injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection.html)
[- [[_content/dictionary#S|SQL]] and NoSQL Injection](https://ckarande.gitbooks.io/owasp-nodegoat-tutorial/content/tutorial/a1_-_sql_and_nosql_injection.html)
[- No SQL, No Injection?](https://arxiv.org/ftp/arxiv/papers/1506/1506.04082.pdf)

#### [[Log Injection](https://owasp.org/www-community/attacks/Log_Injection)](https://owasp.org/www-community/attacks/Log_Injection)¶
Symptom¶
Log Injection occurs when an application includes untrusted data in an application log message (e.g., an attacker can cause an additional log entry that looks like it came from a completely different user, if they can inject [[_content/dictionary#C|CRLF]] characters in the untrusted data). More information about this attack is available on the [[_content/dictionary#O|OWASP]] Log Injection page.
How to prevent¶
To prevent an attacker from writing malicious content into the application log, apply defenses such as:

Use structured log formats, such as [[_content/dictionary#J|JSON]], instead of unstructured text formats.
  Unstructured formats are susceptible to Carriage Return ([[_content/dictionary#C|CR]]) and Line Feed ([[_content/dictionary#L|LF]]) injection (see [[[_content/dictionary#C|CWE]]-93](https://cwe.mitre.org/data/definitions/93.html)).
- Limit the size of the user input value used to create the log message.
Make sure [[Cross_Site_Scripting_Prevention_Cheat_Sheet|all [[_content/dictionary#X|XSS]] defenses]] are applied when viewing log files in a web browser.

##### Example using Log4j Core 2¶
The recommended logging policy for a production environment is sending logs to a network socket using the structured
[[[_content/dictionary#J|JSON]] Template Layout](https://logging.apache.org/log4j/2.x/manual/json-template-layout.html)
introduced in
[Log4j 2.14.0](https://logging.apache.org/log4j/2.x/release-notes.html#release-notes-2-14-0)
and limit the size of strings to 500 bytes using the
[maxStringLength configuration attribute](https://logging.apache.org/log4j/2.x/manual/json-template-layout.html#plugin-attr-maxStringLength):
<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8"?>
<Configuration xmlns="https://logging.apache.org/xml/ns"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:schemaLocation="
                   https://logging.apache.org/xml/ns
                   https://logging.apache.org/xml/ns/log4j-config-2.xsd">
  <Appenders>
    <Socket name="[[_content/dictionary#S|SOCKET]]"
            host="localhost"
            port="12345">
      <!-- Limit the size of any string field in the produced JSON document to 500 bytes -->
      <[[_content/dictionary#J|JsonTemplateLayout]] maxStringLength="500"
                          nullEventDelimiterEnabled="true"/>
    </Socket>
  </Appenders>
  <Loggers>
    <Root level="[[_content/dictionary#D|DEBUG]]">
      <[[_content/dictionary#A|AppenderRef]] ref="SOCKET"/>
    </Root>
  </Loggers>
</Configuration>

See
[Integration with service-oriented architectures](https://logging.apache.org/log4j/2.x/soa.html)
on
[Log4j website](https://logging.apache.org/log4j/2.x/index.html)
for more tips.
Usage of the logger at code level:
import org.apache.logging.log4j.[[_content/dictionary#L|LogManager]];
import org.apache.logging.log4j.Logger;
...
// Most common way to declare a logger
private static final [[_content/dictionary#L|LOGGER]] = LogManager.getLogger();
// [[_content/dictionary#G|GOOD]]!
//
// Use parameterized logging to add user data to a message
// The pattern should be a compile-time constant
logger.warn("Login failed for user {}.", username);
// [[_content/dictionary#B|BAD]]!
//
// Don't mix string concatenation and parameters
// If `username` contains `{}`, the exception will leak into the message
logger.warn("Failure for user " + username + " and role {}.", role, ex);
...

See
[Log4j [[_content/dictionary#A|API]] Best Practices](https://logging.apache.org/log4j/2.x/manual/api.html#best-practice)
for more information.
##### Example using Logback¶
The recommended logging policy for a production environment is using the structured
[[[_content/dictionary#J|JsonEncoder]]](https://logback.qos.ch/manual/encoders.html#JsonEncoder)
introduced in
[Logback 1.3.8](https://logback.qos.ch/news.html#1.3.8).
In the example below, Logback is configured to roll on 10 log files of 5 MiB each:
<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8" ?>
<![[_content/dictionary#D|DOCTYPE]] configuration>
<configuration>
  <import class="ch.qos.logback.classic.encoder.JsonEncoder"/>
  <import class="ch.qos.logback.core.rolling.[[_content/dictionary#F|FixedWindowRollingPolicy]]"/>
  <import class="ch.qos.logback.core.rolling.[[_content/dictionary#R|RollingFileAppender]]"/>
  <import class="ch.qos.logback.core.rolling.[[_content/dictionary#S|SizeBasedTriggeringPolicy]]"/>

  <appender name="[[_content/dictionary#R|RollingFile]]" class="[[_content/dictionary#R|RollingFileAppender]]">
    <file>app.log</file>
    <rollingPolicy class="[[_content/dictionary#F|FixedWindowRollingPolicy]]">
      <fileNamePattern>app-%i.log</fileNamePattern>
      <minIndex>1</minIndex>
      <maxIndex>10</maxIndex>
    </rollingPolicy>
    <triggeringPolicy class="[[_content/dictionary#S|SizeBasedTriggeringPolicy]]">
      <maxFileSize>5MB</maxFileSize>
    </triggeringPolicy>
    <encoder class="[[_content/dictionary#J|JsonEncoder]]"/>
  </appender>

  <root level="[[_content/dictionary#D|DEBUG]]">
    <appender-ref ref="[[_content/dictionary#S|SOCKET]]"/>
  </root>
</configuration>

Usage of the logger at code level:
import org.slf4j.Logger;
import org.slf4j.[[_content/dictionary#L|LoggerFactory]];
...
// Most common way to declare a logger
Logger logger = LoggerFactory.getLogger([[_content/dictionary#M|MyClass]].class);
// [[_content/dictionary#G|GOOD]]!
//
// Use parameterized logging to add user data to a message
// The pattern should be a compile-time constant
logger.warn("Login failed for user {}.", username);
// [[_content/dictionary#B|BAD]]!
//
// Don't mix string concatenation and parameters
// If `username` contains `{}`, the exception will leak into the message
logger.warn("Failure for user " + username + " and role {}.", role, ex);
...

References¶

[- Log4j Core Configuration File](https://logging.apache.org/log4j/2.x/manual/configuration.html)
[- Log4j [[_content/dictionary#J|JSON]] Template Layout](https://logging.apache.org/log4j/2.x/manual/json-template-layout.html)
[- Log4j Appenders](https://logging.apache.org/log4j/2.x/manual/appenders.html)
[- Logback Configuration File](https://logback.qos.ch/manual/configuration.html)
[- Logback [[_content/dictionary#J|JsonEncoder]]](https://logback.qos.ch/manual/encoders.html#JsonEncoder)
[- Logback Appenders](https://logback.qos.ch/manual/appenders.html)

### Cryptography¶
#### General cryptography guidance¶

- Never, ever write your own cryptographic functions.
Wherever possible, try and avoid writing any cryptographic code at all. Instead try and either use pre-existing secret management solutions or the secret management solution provided by your cloud provider. For more information, see the [[Secrets_Management_Cheat_Sheet|[[_content/dictionary#O|OWASP]] Secrets Management Cheat Sheet]].
- If you cannot use a pre-existing secret management solution, try and use a trusted and well known implementation library rather than using the libraries built into [[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] as it is far too easy to make cryptographic errors with them.
- Make sure your application or protocol can easily support a future change of cryptographic algorithms.
- Use your package manager wherever possible to keep all of your packages up to date. Watch the updates on your development setup, and plan updates to your applications accordingly.
- We will show examples below based on Google Tink, which is a library created by cryptography experts for using cryptography safely (in the sense of minimizing common mistakes made when using standard cryptography libraries).

#### Encryption for storage¶
Follow the algorithm guidance in the [[[[_content/dictionary#O|OWASP]] Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#algorithms)](Cryptographic_Storage_Cheat_Sheet.html#algorithms).
##### Symmetric example using Google Tink¶
Google Tink has documentation on performing common tasks.
For example, this page (from Google's website) shows [how to perform simple symmetric encryption](https://developers.google.com/tink/encrypt-data).
The following code snippet shows an encapsulated use of this functionality:

Click here to view the "Tink symmetric encryption" code snippet.
import static java.nio.charset.[[_content/dictionary#S|StandardCharsets]].UTF_8;

import com.google.crypto.tink.Aead;
import com.google.crypto.tink.[[_content/dictionary#I|InsecureSecretKeyAccess]];
import com.google.crypto.tink.[[_content/dictionary#K|KeysetHandle]];
import com.google.crypto.tink.[[_content/dictionary#T|TinkJsonProtoKeysetFormat]];
import com.google.crypto.tink.aead.[[_content/dictionary#A|AeadConfig]];
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Base64;

// [[_content/dictionary#A|AesGcmSimpleTest]]
public class App {

    // Based on example from:
    // https://github.com/tink-crypto/tink-java/tree/main/examples/aead

    public static void main(String[] args) throws Exception {

        // Key securely generated using:
        // tinkey create-keyset --key-template AES128_GCM --out-format [[_content/dictionary#J|JSON]] --out aead_test_keyset.json

        // Register all [[_content/dictionary#A|AEAD]] key types with the Tink runtime.
        [[_content/dictionary#A|AeadConfig]].register();

        // Read the keyset into a [[_content/dictionary#K|KeysetHandle]].
        KeysetHandle handle =
        [[_content/dictionary#T|TinkJsonProtoKeysetFormat]].parseKeyset(
            new String(Files.readAllBytes( Paths.get("/home/fredbloggs/aead_test_keyset.json")), UTF_8), [[_content/dictionary#I|InsecureSecretKeyAccess]].get());

        String message = "This message to be encrypted";
        System.out.println(message);

        // Add some relevant context about the encrypted data that should be verified
        // on decryption
        String metadata = "Sender: fredbloggs@example.com";

        // Encrypt the message
        byte[] cipherText = [[_content/dictionary#A|AesGcmSimple]].encrypt(message, metadata, handle);
        System.out.println(Base64.getEncoder().encodeToString(cipherText));

        // Decrypt the message
        String message2 = [[_content/dictionary#A|AesGcmSimple]].decrypt(cipherText, metadata, handle);
        System.out.println(message2);
    }
}

class [[_content/dictionary#A|AesGcmSimple]] {

    public static byte[] encrypt(String plaintext, String metadata, [[_content/dictionary#K|KeysetHandle]] handle) throws Exception {
        // Get the primitive.
        Aead aead = handle.getPrimitive(Aead.class);
        return aead.encrypt(plaintext.getBytes(UTF_8), metadata.getBytes(UTF_8));
    }

    public static String decrypt(byte[] ciphertext, String metadata, [[_content/dictionary#K|KeysetHandle]] handle) throws Exception {
        // Get the primitive.
        Aead aead = handle.getPrimitive(Aead.class);
        return new String(aead.decrypt(ciphertext, metadata.getBytes(UTF_8)),UTF_8);
    }

}

##### Symmetric example using built-in [[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] classes¶
If you absolutely cannot use a separate library, it is still possible to use the built [[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] classes but it is strongly recommended to have a cryptography expert review the full design and code, as even the most trivial error can severely weaken your encryption.
The following code snippet shows an example of using [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] to perform encryption/decryption of data.
A few constraints/pitfalls with this code:

- - It does not take into account key rotation or management which is a whole topic in itself.
It is important to use a different nonce for every encryption operation, especially if the same key is used. For more information, see [this answer on Cryptography Stack Exchange](https://crypto.stackexchange.com/a/66500).
- The key will need to be stored securely.

Click here to view the "[[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] symmetric encryption" code snippet.
import java.nio.charset.[[_content/dictionary#S|StandardCharsets]];
import java.security.[[_content/dictionary#S|SecureRandom]];
import javax.crypto.spec.*;
import javax.crypto.*;
import java.util.Base64;

// [[_content/dictionary#A|AesGcmSimpleTest]]
class Main {

    public static void main(String[] args) throws Exception {
        // Key of 32 bytes / 256 bits for [[_content/dictionary#A|AES]]
        [[_content/dictionary#K|KeyGenerator]] keyGen = KeyGenerator.getInstance([[_content/dictionary#A|AesGcmSimple]].[[_content/dictionary#A|ALGORITHM]]);
        keyGen.init(AesGcmSimple.KEY_SIZE, new [[_content/dictionary#S|SecureRandom]]());
        [[_content/dictionary#S|SecretKey]] secretKey = keyGen.generateKey();

        // Nonce of 12 bytes / 96 bits and this size should always be used.
        // It is critical for [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] that a unique nonce is used for every cryptographic operation.
        byte[] nonce = new byte[[[_content/dictionary#A|AesGcmSimple]].IV_LENGTH];
        [[_content/dictionary#S|SecureRandom]] random = new SecureRandom();
        random.nextBytes(nonce);

        var message = "This message to be encrypted";
        System.out.println(message);

        // Encrypt the message
        byte[] cipherText = [[_content/dictionary#A|AesGcmSimple]].encrypt(message, nonce, secretKey);
        System.out.println(Base64.getEncoder().encodeToString(cipherText));

        // Decrypt the message
        var message2 = [[_content/dictionary#A|AesGcmSimple]].decrypt(cipherText, nonce, secretKey);
        System.out.println(message2);
    }
}

class [[_content/dictionary#A|AesGcmSimple]] {

    public static final String [[_content/dictionary#A|ALGORITHM]] = "[[_content/dictionary#A|AES]]";
    public static final String CIPHER_ALGORITHM = "AES/[[_content/dictionary#G|GCM]]/[[_content/dictionary#N|NoPadding]]";
    public static final int KEY_SIZE = 256;
    public static final int TAG_LENGTH = 128;
    public static final int IV_LENGTH = 12;

    public static byte[] encrypt(String plaintext, byte[] nonce, [[_content/dictionary#S|SecretKey]] secretKey) throws Exception {
        return cryptoOperation(plaintext.getBytes([[_content/dictionary#S|StandardCharsets]].UTF_8), nonce, secretKey, Cipher.ENCRYPT_MODE);
    }

    public static String decrypt(byte[] ciphertext, byte[] nonce, [[_content/dictionary#S|SecretKey]] secretKey) throws Exception {
        return new String(cryptoOperation(ciphertext, nonce, secretKey, Cipher.DECRYPT_MODE), [[_content/dictionary#S|StandardCharsets]].UTF_8);
    }

    private static byte[] cryptoOperation(byte[] text, byte[] nonce, [[_content/dictionary#S|SecretKey]] secretKey, int mode) throws Exception {
        Cipher cipher = Cipher.getInstance(CIPHER_ALGORITHM);
        GCMParameterSpec gcmParameterSpec = new GCMParameterSpec(TAG_LENGTH, nonce);
        cipher.init(mode, secretKey, gcmParameterSpec);
        return cipher.doFinal(text);
    }

}

#### Encryption for transmission¶
Again, follow the algorithm guidance in the [[_content/dictionary#O|OWASP]] Cryptographic Storage Cheat Sheet.
##### Asymmetric example using Google Tink¶
Google Tink has documentation on performing common tasks.
For example, this page (from Google's website) shows [how to perform a hybrid encryption process](https://developers.google.com/tink/exchange-data) where two parties want to share data based on their asymmetric key pair.
The following code snippet shows how this functionality can be used to share secrets between Alice and Bob:

Click here to view the "Tink hybrid encryption" code snippet.
import static java.nio.charset.[[_content/dictionary#S|StandardCharsets]].UTF_8;

import com.google.crypto.tink.[[_content/dictionary#H|HybridDecrypt]];
import com.google.crypto.tink.[[_content/dictionary#H|HybridEncrypt]];
import com.google.crypto.tink.[[_content/dictionary#I|InsecureSecretKeyAccess]];
import com.google.crypto.tink.[[_content/dictionary#K|KeysetHandle]];
import com.google.crypto.tink.[[_content/dictionary#T|TinkJsonProtoKeysetFormat]];
import com.google.crypto.tink.hybrid.[[_content/dictionary#H|HybridConfig]];
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Base64;

// [[_content/dictionary#H|HybridReplaceTest]]
class App {
    public static void main(String[] args) throws Exception {
        /*

        Generated public/private keypairs for Bob and Alice using the
        following tinkey commands:

        ./tinkey create-keyset \
        --key-template DHKEM_X25519_HKDF_SHA256_HKDF_SHA256_AES_256_GCM \
        --out-format [[_content/dictionary#J|JSON]] --out alice_private_keyset.json

        ./tinkey create-keyset \
        --key-template DHKEM_X25519_HKDF_SHA256_HKDF_SHA256_AES_256_GCM \
        --out-format [[_content/dictionary#J|JSON]] --out bob_private_keyset.json

        ./tinkey create-public-keyset --in alice_private_keyset.json \
        --in-format [[_content/dictionary#J|JSON]] --out-format JSON --out alice_public_keyset.json

        ./tinkey create-public-keyset --in bob_private_keyset.json \
        --in-format [[_content/dictionary#J|JSON]] --out-format JSON --out bob_public_keyset.json
        */

        [[_content/dictionary#H|HybridConfig]].register();

        // Generate [[_content/dictionary#E|ECC]] key pair for Alice
        var alice = new [[_content/dictionary#H|HybridSimple]](
                getKeysetHandle("/home/alicesmith/private_keyset.json"),
                getKeysetHandle("/home/alicesmith/public_keyset.json")

        );

        [[_content/dictionary#K|KeysetHandle]] alicePublicKey = alice.getPublicKey();

        // Generate [[_content/dictionary#E|ECC]] key pair for Bob
        var bob = new [[_content/dictionary#H|HybridSimple]](
                getKeysetHandle("/home/bobjones/private_keyset.json"),
                getKeysetHandle("/home/bobjones/public_keyset.json")

        );

        [[_content/dictionary#K|KeysetHandle]] bobPublicKey = bob.getPublicKey();

        // This keypair generation should be reperformed every so often in order to
        // obtain a new shared secret to avoid a long lived shared secret.

        // Alice encrypts a message to send to Bob
        String plaintext = "Hello, Bob!";

        // Add some relevant context about the encrypted data that should be verified
        // on decryption
        String metadata = "Sender: alicesmith@example.com";

        System.out.println("Secret being sent from Alice to Bob: " + plaintext);
        var cipherText = alice.encrypt(bobPublicKey, plaintext, metadata);
        System.out.println("Ciphertext being sent from Alice to Bob: " + Base64.getEncoder().encodeToString(cipherText));

        // Bob decrypts the message
        var decrypted = bob.decrypt(cipherText, metadata);
        System.out.println("Secret received by Bob from Alice: " + decrypted);
        System.out.println();

        // Bob encrypts a message to send to Alice
        String plaintext2 = "Hello, Alice!";

        // Add some relevant context about the encrypted data that should be verified
        // on decryption
        String metadata2 = "Sender: bobjones@example.com";

        System.out.println("Secret being sent from Bob to Alice: " + plaintext2);
        var cipherText2 = bob.encrypt(alicePublicKey, plaintext2, metadata2);
        System.out.println("Ciphertext being sent from Bob to Alice: " + Base64.getEncoder().encodeToString(cipherText2));

        // Bob decrypts the message
        var decrypted2 = alice.decrypt(cipherText2, metadata2);
        System.out.println("Secret received by Alice from Bob: " + decrypted2);
    }

    private static [[_content/dictionary#K|KeysetHandle]] getKeysetHandle(String filename) throws Exception
    {
        return [[_content/dictionary#T|TinkJsonProtoKeysetFormat]].parseKeyset(
                new String(Files.readAllBytes( Paths.get(filename)), UTF_8), [[_content/dictionary#I|InsecureSecretKeyAccess]].get());
    }
}
class [[_content/dictionary#H|HybridSimple]] {

    private [[_content/dictionary#K|KeysetHandle]] privateKey;
    private KeysetHandle publicKey;

    public [[_content/dictionary#H|HybridSimple]]([[_content/dictionary#K|KeysetHandle]] privateKeyIn, KeysetHandle publicKeyIn) throws Exception {
        privateKey = privateKeyIn;
        publicKey = publicKeyIn;
    }

    public [[_content/dictionary#K|KeysetHandle]] getPublicKey() {
        return publicKey;
    }

    public byte[] encrypt([[_content/dictionary#K|KeysetHandle]] partnerPublicKey, String message, String metadata) throws Exception {

        [[_content/dictionary#H|HybridEncrypt]] encryptor = partnerPublicKey.getPrimitive(HybridEncrypt.class);

        // return the encrypted value
        return encryptor.encrypt(message.getBytes(UTF_8), metadata.getBytes(UTF_8));
    }
    public String decrypt(byte[] ciphertext, String metadata) throws Exception {

        [[_content/dictionary#H|HybridDecrypt]] decryptor = privateKey.getPrimitive(HybridDecrypt.class);

        // return the encrypted value
        return new String(decryptor.decrypt(ciphertext, metadata.getBytes(UTF_8)),UTF_8);
    }

}

##### Asymmetric example using built-in [[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] classes¶
If you absolutely cannot use a separate library, it is still possible to use the built [[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] classes but it is strongly recommended to have a cryptography expert review the full design and code, as even the most trivial error can severely weaken your encryption.
The following code snippet shows an example of using Elliptic Curve/Diffie Helman ([[_content/dictionary#E|ECDH]]) together with [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] to perform encryption/decryption of data between two different sides without the need the transfer the symmetric key between the two sides. Instead, the sides exchange public keys and can then use ECDH to generate a shared secret which can be used for the symmetric encryption.
Note that this code sample relies on the [[_content/dictionary#A|AesGcmSimple]] class from the [previous section](#symmetric-example-using-built-in-jcajce-classes).
A few constraints/pitfalls with this code:

It does not take into account key rotation or management which is a whole topic in itself.
- The code deliberately enforces a new nonce for every encryption operation but this must be managed as a separate data item alongside the ciphertext.
- The private keys will need to be stored securely.
- The code does not consider the validation of public keys before use.
- Overall, there is no verification of authenticity between the two sides.

Click here to view the "[[_content/dictionary#J|JCA]]/[[_content/dictionary#J|JCE]] hybrid encryption" code snippet.
import java.nio.charset.[[_content/dictionary#S|StandardCharsets]];
import java.security.[[_content/dictionary#S|SecureRandom]];
import javax.crypto.spec.*;
import javax.crypto.*;
import java.util.*;
import java.security.*;
import java.security.spec.*;
import java.util.Arrays;

// ECDHSimpleTest
class Main {
    public static void main(String[] args) throws Exception {

        // Generate [[_content/dictionary#E|ECC]] key pair for Alice
        var alice = new ECDHSimple();
        Key alicePublicKey = alice.getPublicKey();

        // Generate [[_content/dictionary#E|ECC]] key pair for Bob
        var bob = new ECDHSimple();
        Key bobPublicKey = bob.getPublicKey();

        // This keypair generation should be reperformed every so often in order to
        // obtain a new shared secret to avoid a long lived shared secret.

        // Alice encrypts a message to send to Bob
        String plaintext = "Hello"; //, Bob!";
        System.out.println("Secret being sent from Alice to Bob: " + plaintext);

        var retPair = alice.encrypt(bobPublicKey, plaintext);
        var nonce = retPair.getKey();
        var cipherText = retPair.getValue();

        System.out.println("Both cipherText and nonce being sent from Alice to Bob: " + Base64.getEncoder().encodeToString(cipherText) + " " + Base64.getEncoder().encodeToString(nonce));

        // Bob decrypts the message
        var decrypted = bob.decrypt(alicePublicKey, cipherText, nonce);
        System.out.println("Secret received by Bob from Alice: " + decrypted);
        System.out.println();

        // Bob encrypts a message to send to Alice
        String plaintext2 = "Hello"; //, Alice!";
        System.out.println("Secret being sent from Bob to Alice: " + plaintext2);

        var retPair2 = bob.encrypt(alicePublicKey, plaintext2);
        var nonce2 = retPair2.getKey();
        var cipherText2 = retPair2.getValue();
        System.out.println("Both cipherText2 and nonce2 being sent from Bob to Alice: " + Base64.getEncoder().encodeToString(cipherText2) + " " + Base64.getEncoder().encodeToString(nonce2));

        // Bob decrypts the message
        var decrypted2 = alice.decrypt(bobPublicKey, cipherText2, nonce2);
        System.out.println("Secret received by Alice from Bob: " + decrypted2);
    }
}
class ECDHSimple {
    private [[_content/dictionary#K|KeyPair]] keyPair;

    public class [[_content/dictionary#A|AesKeyNonce]] {
        public [[_content/dictionary#S|SecretKey]] Key;
        public byte[] Nonce;
    }

    public ECDHSimple() throws Exception {
        [[_content/dictionary#K|KeyPairGenerator]] keyPairGenerator = KeyPairGenerator.getInstance("[[_content/dictionary#E|EC]]");
        ECGenParameterSpec ecSpec = new ECGenParameterSpec("secp256r1"); // Using secp256r1 curve
        keyPairGenerator.initialize(ecSpec);
        keyPair = keyPairGenerator.generateKeyPair();
    }

    public Key getPublicKey() {
        return keyPair.getPublic();
    }

    public [[_content/dictionary#A|AbstractMap]].[[_content/dictionary#S|SimpleEntry]]<byte[], byte[]> encrypt(Key partnerPublicKey, String message) throws Exception {

        // Generate the [[_content/dictionary#A|AES]] Key and Nonce
        [[_content/dictionary#A|AesKeyNonce]] aesParams = generateAESParams(partnerPublicKey);

        // return the encrypted value
        return new [[_content/dictionary#A|AbstractMap]].[[_content/dictionary#S|SimpleEntry]]<>(
            aesParams.Nonce,
            [[_content/dictionary#A|AesGcmSimple]].encrypt(message, aesParams.Nonce, aesParams.Key)
            );
    }
    public String decrypt(Key partnerPublicKey, byte[] ciphertext, byte[] nonce) throws Exception {

        // Generate the [[_content/dictionary#A|AES]] Key and Nonce
        [[_content/dictionary#A|AesKeyNonce]] aesParams = generateAESParams(partnerPublicKey, nonce);

        // return the decrypted value
        return [[_content/dictionary#A|AesGcmSimple]].decrypt(ciphertext, aesParams.Nonce, aesParams.Key);
    }

    private [[_content/dictionary#A|AesKeyNonce]] generateAESParams(Key partnerPublicKey, byte[] nonce) throws Exception {

        // Derive the secret based on this side's private key and the other side's public key
        [[_content/dictionary#K|KeyAgreement]] keyAgreement = KeyAgreement.getInstance("[[_content/dictionary#E|ECDH]]");
        keyAgreement.init(keyPair.getPrivate());
        keyAgreement.doPhase(partnerPublicKey, true);
        byte[] secret = keyAgreement.generateSecret();

        [[_content/dictionary#A|AesKeyNonce]] aesKeyNonce = new AesKeyNonce();

        // Copy first 32 bytes as the key
        byte[] key = Arrays.copyOfRange(secret, 0, ([[_content/dictionary#A|AesGcmSimple]].KEY_SIZE / 8));
        aesKeyNonce.Key = new [[_content/dictionary#S|SecretKeySpec]](key, 0, key.length, "[[_content/dictionary#A|AES]]");

        // Passed in nonce will be used.
        aesKeyNonce.Nonce = nonce;
        return aesKeyNonce;

    }

    private [[_content/dictionary#A|AesKeyNonce]] generateAESParams(Key partnerPublicKey) throws Exception {

        // Nonce of 12 bytes / 96 bits and this size should always be used.
        // It is critical for [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] that a unique nonce is used for every cryptographic operation.
        // Therefore this is not generated from the shared secret
        byte[] nonce = new byte[[[_content/dictionary#A|AesGcmSimple]].IV_LENGTH];
        [[_content/dictionary#S|SecureRandom]] random = new SecureRandom();
        random.nextBytes(nonce);
        return generateAESParams(partnerPublicKey, nonce);

    }
}