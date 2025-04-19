---
title: "DotNet Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html"
created: "1741872881.8582923"
tags: [owasp, cheatsheet, security]
---
# [[_content/dictionary#D|DotNet]] Security

## [[_content/dictionary#D|DotNet]] Security Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#wcf-guidance)](#windows-forms-guidance)](#xaml-guidance)](#forms-authentication)](#http-validation-and-encoding)](#asp-net-web-forms-guidance)](#data-access)](#configuration-and-deployment)](#guidance-for-specific-topics)](#sample-project)](#other-advice)](#a102013-unvalidated-redirects-and-forwards)](#a082017-insecure-deserialization)](#a072017-cross-site-scripting-xss)](#a042017-xml-external-entities-xxe)](#owasp-2013-2017)](#a10-server-side-request-forgery-ssrf)](#monitoring)](#logging)](#a09-security-logging-and-monitoring-failures)](#a08-software-and-data-integrity-failures)](#a07-identification-and-authentication-failures)](#a06-vulnerable-and-outdated-components)](#using-net-core-or-net-framework-with-ajax)](#using-net-core-20-or-later)](#using-net-framework)](#cross-site-request-forgery)](#debug-and-stack-trace)](#a05-security-misconfiguration)](#a04-insecure-design)](#ldap-injection)](#os-injection)](#sql-injection)](#a03-injection)](#encryption-for-transmission)](#encryption-for-storage)](#encryption)](#passwords)](#hashing)](#general-cryptography-guidance)](#a02-cryptographic-failures)](#insecure-direct-object-references)](#missing-function-level-access-control)](#weak-account-management)](#a01-broken-access-control)](#net-general-guidance)](#security-announcements)](#updating-the-framework)](#the-net-framework)](#introduction)](#dotnet-security-cheat-sheet)
### Introduction¶
This page intends to provide quick basic [.NET](https://docs.microsoft.com/en-us/aspnet/web-api/overview/security/preventing-cross-site-request-forgery-csrf-attacks) security tips for developers.
#### The .[[_content/dictionary#N|NET]] Framework¶
The .NET Framework is Microsoft's principal platform for enterprise development. It is the supporting [[_content/dictionary#A|API]] for [[_content/dictionary#A|ASP]].NET, Windows Desktop applications, Windows Communication Foundation services, [[_content/dictionary#S|SharePoint]], Visual Studio Tools for Office and other technologies.
The .NET Framework constitutes a collection of APIs that facilitate the usage of an advanced type system, managing data, graphics, networking, file operations, and more - essentially covering the vast majority of requirements for developing enterprise applications within the Microsoft ecosystem. It is a nearly ubiquitous library that is strongly named and versioned at the assembly level.
#### Updating the Framework¶
The .NET Framework is kept up-to-date by Microsoft with the [Windows Update](http://windowsupdate.microsoft.com/) service. Developers do not normally need to run separate updates to the Framework. Windows Update can be accessed at Windows Update or from the Windows Update program on a Windows computer.
Individual frameworks can be kept up to date using [[[[_content/dictionary#N|NuGet]]](https://docs.microsoft.com/en-us/nuget/)](https://docs.microsoft.com/en-us/nuget/). As Visual Studio prompts for updates, build it into your lifecycle.
Remember that third-party libraries have to be updated separately and not all of them use NuGet. [[_content/dictionary#E|ELMAH]] for instance, requires a separate update effort.
#### Security Announcements¶
Receive security notifications by selecting the "Watch" button at the following repositories:

[[.[[_content/dictionary#N|NET]] Core](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-7.0#aspnet-core-antiforgery-configuration) Security Announcements](https://github.com/dotnet/announcements/issues?q=is%3Aopen+is%3Aissue+label%3ASecurity)
[[[_content/dictionary#A|ASP]].NET Core & [Entity Framework](https://docs.microsoft.com/en-us/ef/) Core Security Announcements](https://github.com/aspnet/Announcements/issues?q=is%3Aopen+is%3Aissue+label%3ASecurity)

### .[[_content/dictionary#N|NET]] General Guidance¶
This section contains general guidance for .NET applications.
This applies to all .NET applications, including [[_content/dictionary#A|ASP]].NET, [[_content/dictionary#W|WPF]], [[_content/dictionary#W|WinForms]], and others.
The [[_content/dictionary#O|OWASP]] Top 10 lists the most prevalent and dangerous threats to web security in the world today and is reviewed every few years
and updated with the latest threat data. This section of the cheat sheet is based on this list.
Your approach to securing your web application should be to start at the top threat A1 below and work down;
this will ensure that any time spent on security will be spent most effectively and
cover the top threats first and lesser threats afterwards. After covering the Top 10 it is generally advisable
to assess for other threats or get a professionally completed Penetration Test.
#### A01 Broken Access Control¶
##### Weak Account management¶
Ensure cookies are sent with the [[[_content/dictionary#H|HttpOnly]]](https://docs.microsoft.com/en-us/dotnet/api/system.web.configuration.httpcookiessection.httponlycookies) flag set to prevent client side scripts from accessing the cookie:
[[_content/dictionary#C|CookieHttpOnly]] = true,

Reduce the time period a session can be stolen in by reducing session timeout and removing sliding expiration:
[[_content/dictionary#E|ExpireTimeSpan]] = [[_content/dictionary#T|TimeSpan]].[[_content/dictionary#F|FromMinutes]](60),
[[_content/dictionary#S|SlidingExpiration]] = false

See [[[[[[here](https://support.microsoft.com/en-us/help/954002/how-to-add-a-custom-http-response-header-to-a-web-site-that-is-hosted)](https://github.com/johnstaveley/[[_content/dictionary#S|SecurityEssentials]]/blob/master/SecurityEssentials/Core/[[_content/dictionary#H|HttpHeaders]].cs)](https://github.com/microsoft/code-with-engineering-playbook/blob/main/docs/observability/[[_content/dictionary#R|README]].md)](https://docs.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger)](https://docs.microsoft.com/en-us/aspnet/web-api/overview/security/preventing-cross-site-request-forgery-csrf-attacks#anti-csrf-and-ajax)](https://github.com/johnstaveley/SecurityEssentials/blob/master/SecurityEssentials/App_Start/Startup.Auth.cs) for an example of a full startup code snippet.
Ensure cookies are sent over [[[_content/dictionary#H|HTTPS]]](http://support.microsoft.com/kb/324069) in production. This should be enforced in the config transforms:
<httpCookies [requireSSL](https://docs.microsoft.com/en-us/dotnet/api/system.web.configuration.httpcookiessection.requiressl)="true" />
<authentication>
    <forms requireSSL="true" />
</authentication>

Protect [[_content/dictionary#L|LogOn]], Registration and password reset methods against brute force attacks by throttling requests (see code below). Consider also using [[_content/dictionary#R|ReCaptcha]].
[[[_content/dictionary#H|HttpPost]]]
[[[_content/dictionary#A|AllowAnonymous]]]
[[[_content/dictionary#V|ValidateAntiForgeryToken]]]
[AllowXRequestsEveryXSecondsAttribute(Name = "LogOn",
Message = "You have performed this action more than {x} times in the last {n} seconds.",
Requests = 3, Seconds = 60)]
public async Task<[[_content/dictionary#A|ActionResult]]> LogOn([[_content/dictionary#L|LogOnViewModel]] model, string returnUrl)

[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Roll your own authentication or session management. Use the one provided by .[[_content/dictionary#N|NET]].
DO NOT: Tell someone if the account exists on [[_content/dictionary#L|LogOn]], Registration or Password reset. Say something like 'Either the username or password was incorrect', or 'If this account exists then a reset token will be sent to the registered email address'. This protects against account enumeration.
The feedback to the user should be identical whether or not the account exists, both in terms of content and behavior. E.g., if the response takes 50% longer when the account is real then membership information can be guessed and tested.
##### Missing function-level access control¶
DO: Authorize users on all externally facing endpoints. The .NET framework has many ways to authorize a user, use them at method level:
[Authorize(Roles = "Admin")]
[[[_content/dictionary#H|HttpGet]]]
public [[_content/dictionary#A|ActionResult]] Index(int page = 1)

or better yet, at controller level:
[Authorize]
public class UserController

You can also check roles in code using identity features in .net: System.Web.Security.Roles.[[_content/dictionary#I|IsUserInRole]](userName, roleName)
You can find more information in the [[Authorization_Cheat_Sheet|Authorization Cheat Sheet]] and
[[Authorization_Testing_Automation_Cheat_Sheet|Authorization Testing Automation Cheat Sheet]].
##### Insecure Direct object references¶
When you have a resource (object) which can be accessed by a reference (in the sample below this is the id), you need to ensure that the user is intended to have access to that resource.
// Insecure
public [[_content/dictionary#A|ActionResult]] Edit(int id)
{
  var user = _context.Users.[[_content/dictionary#F|FirstOrDefault]](e => e.Id == id);
  return View("Details", new [[_content/dictionary#U|UserViewModel]](user);
}

// Secure
public [[_content/dictionary#A|ActionResult]] Edit(int id)
{
  var user = _context.Users.[[_content/dictionary#F|FirstOrDefault]](e => e.Id == id);
  // Establish user has right to edit the details
  if (user.Id != _userIdentity.[[_content/dictionary#G|GetUserId]]())
  {
        [[_content/dictionary#H|HandleErrorInfo]] error = new HandleErrorInfo(
            new Exception("[[_content/dictionary#I|INFO]]: You do not have permission to edit these details"));
        return View("Error", error);
  }
  return View("Edit", new [[_content/dictionary#U|UserViewModel]](user);
}

More information can be found in the [[Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet|Insecure Direct Object Reference Prevention Cheat Sheet]].
#### A02 Cryptographic Failures¶
##### General cryptography guidance¶

- Never, ever write your own cryptographic functions.
Wherever possible, try and avoid writing any cryptographic code at all. Instead try and either use pre-existing secrets management solutions or the secret management solution provided by your cloud provider. For more information, see the [[Secrets_Management_Cheat_Sheet|[[_content/dictionary#O|OWASP]] Secrets Management Cheat Sheet]].
- If you cannot use a pre-existing secrets management solution, try and use a trusted and well known implementation library rather than using the libraries built into .[[_content/dictionary#N|NET]] as it is far too easy to make cryptographic errors with them.
- Make sure your application or protocol can easily support a future change of cryptographic algorithms.

##### Hashing¶
[[_content/dictionary#D|DO]]: Use a strong hashing algorithm.

In .[[_content/dictionary#N|NET]] (both Framework and Core), the strongest hashing algorithm for general hashing requirements is
  [System.Security.Cryptography.SHA512](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha512).
In .NET Framework 4.6 and earlier, the strongest algorithm for password hashing is [[_content/dictionary#P|PBKDF2]], implemented as
  [System.Security.Cryptography.Rfc2898DeriveBytes](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.rfc2898derivebytes).
In .NET Framework 4.6.1 and later and .NET Core, the strongest algorithm for password hashing is PBKDF2, implemented as
  [Microsoft.[[_content/dictionary#A|AspNetCore]].Cryptography.[[_content/dictionary#K|KeyDerivation]].Pbkdf2](https://docs.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/password-hashing)
  which has several significant advantages over Rfc2898DeriveBytes.
- When using a hashing function to hash non-unique inputs such as passwords, use a salt value added to the original value before hashing.
Refer to the [[Password_Storage_Cheat_Sheet|[Password Storage Cheat Sheet]]](Password_Storage_Cheat_Sheet.html) for more information.

##### Passwords¶
[[_content/dictionary#D|DO]]: Enforce passwords with a minimum complexity that will survive a dictionary attack; i.e. longer passwords that use the full character set (numbers, symbols and letters) to increase entropy.
##### Encryption¶
DO: Use a strong encryption algorithm such as [[_content/dictionary#A|AES]]-512 where personally identifiable data needs to be restored to it's original format.
DO: Protect encryption keys more than any other asset. Find more information about storing encryption keys at rest in the
  [Key Management Cheat Sheet](Key_Management_Cheat_Sheet.html#storage).
DO: Use [[_content/dictionary#T|TLS]] 1.2+ for your entire site. Get a free certificate [[[_content/dictionary#L|LetsEncrypt]].org](https://letsencrypt.org/) and automate renewals.
DO [[_content/dictionary#N|NOT]]: [Allow [[_content/dictionary#S|SSL]], this is now obsolete](https://github.com/ssllabs/research/wiki/SSL-and-TLS-Deployment-Best-Practices).
DO: Have a strong TLS policy (see [SSL Best Practices](https://www.ssllabs.com/projects/best-practices/index.html)), use TLS 1.2+ wherever possible. Then check the configuration using [SSL Test](https://www.ssllabs.com/ssltest/) or [TestSSL](https://testssl.sh/).
More information on Transport Layer Protection can be found in the
[[Transport_Layer_Security_Cheat_Sheet|Transport Layer Security Cheat Sheet]].
DO: Ensure headers are not disclosing information about your application. See [[[_content/dictionary#H|HttpHeaders]].cs](https://github.com/johnstaveley/[[_content/dictionary#S|SecurityEssentials]]/blob/master/SecurityEssentials/Core/HttpHeaders.cs), [Dionach [[_content/dictionary#S|StripHeaders]]](https://github.com/Dionach/StripHeaders/), disable via web.config or [Startup.cs](https://medium.com/bugbountywriteup/security-headers-1c770105940b).
e.g Web.config
<system.web>
    <httpRuntime enableVersionHeader="false"/>
</system.web>
<system.webServer>
    <security>
        <requestFiltering removeServerHeader="true" />
    </security>
    <httpProtocol>
        <customHeaders>
            <add name="X-Content-Type-Options" value="nosniff" />
            <add name="X-Frame-Options" value="[[_content/dictionary#D|DENY]]" />
            <add name="X-Permitted-Cross-Domain-Policies" value="master-only"/>
            <add name="X-[[_content/dictionary#X|XSS]]-Protection" value="0"/>
            <remove name="X-Powered-By"/>
        </customHeaders>
    </httpProtocol>
</system.webServer>

e.g Startup.cs
app.[[_content/dictionary#U|UseHsts]](hsts => hsts.[[_content/dictionary#M|MaxAge]](365).[[_content/dictionary#I|IncludeSubdomains]]());
app.UseXContentTypeOptions();
app.[[_content/dictionary#U|UseReferrerPolicy]](opts => opts.[[_content/dictionary#N|NoReferrer]]());
app.UseXXssProtection(options => options.[[_content/dictionary#F|FilterDisabled]]());
app.[[_content/dictionary#U|UseXfo]](options => options.Deny());

app.[[_content/dictionary#U|UseCsp]](opts => opts
 .[[_content/dictionary#B|BlockAllMixedContent]]()
 .[[_content/dictionary#S|StyleSources]](s => s.Self())
 .StyleSources(s => s.[[_content/dictionary#U|UnsafeInline]]())
 .[[_content/dictionary#F|FontSources]](s => s.Self())
 .[[_content/dictionary#F|FormActions]](s => s.Self())
 .[[_content/dictionary#F|FrameAncestors]](s => s.Self())
 .[[_content/dictionary#I|ImageSources]](s => s.Self())
 .[[_content/dictionary#S|ScriptSources]](s => s.Self())
 );

More information about headers can be found at the [[[_content/dictionary#O|OWASP]] Secure Headers Project](https://owasp.org/www-project-secure-headers/).
##### Encryption for storage¶

Use the [Windows Data Protection [[_content/dictionary#A|API]] ([[_content/dictionary#D|DPAPI]])](https://docs.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection) for secure local storage of sensitive data.
Where DPAPI cannot be used, follow the algorithm guidance in the [[[[_content/dictionary#O|OWASP]] Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#algorithms)](Cryptographic_Storage_Cheat_Sheet.html#algorithms).

The following code snippet shows an example of using [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] to perform encryption/decryption of data. It is strongly recommended to have a cryptography expert review your final design and code, as even the most trivial error can severely weaken your encryption.
The code is based on example from here: [https://www.scottbrady91.com/c-sharp/aes-gcm-dotnet](https://www.scottbrady91.com/c-sharp/aes-gcm-dotnet)
A few constraints/pitfalls with this code:

- - It does not take into account key rotation or management which is a whole topic in itself.
- It is important to use a different nonce for every encryption operation, even if the same key is used.
- The key will need to be stored securely.

Click here to view the "[[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] symmetric encryption" code snippet.
// Code based on example from here:
// https://www.scottbrady91.com/c-sharp/aes-gcm-dotnet

public class [[_content/dictionary#A|AesGcmSimpleTest]]
{
    public static void Main()
    {

        // Key of 32 bytes / 256 bits for [[_content/dictionary#A|AES]]
        var key = new byte[32];
        [[_content/dictionary#R|RandomNumberGenerator]].Fill(key);

        // [[_content/dictionary#M|MaxSize]] = 12 bytes / 96 bits and this size should always be used.
        var nonce = new byte[[[_content/dictionary#A|AesGcm]].[[_content/dictionary#N|NonceByteSizes]].MaxSize];
        [[_content/dictionary#R|RandomNumberGenerator]].Fill(nonce);

        // Tag for authenticated encryption
        var tag = new byte[[[_content/dictionary#A|AesGcm]].[[_content/dictionary#T|TagByteSizes]].[[_content/dictionary#M|MaxSize]]];

        var message = "This message to be encrypted";
        Console.[[_content/dictionary#W|WriteLine]](message);

        // Encrypt the message
        var cipherText = [[_content/dictionary#A|AesGcmSimple]].Encrypt(message, nonce, out tag, key);
        Console.[[_content/dictionary#W|WriteLine]](Convert.ToBase64String(cipherText));

        // Decrypt the message
        var message2 = [[_content/dictionary#A|AesGcmSimple]].Decrypt(cipherText, nonce, tag, key);
        Console.[[_content/dictionary#W|WriteLine]](message2);

    }
}

public static class [[_content/dictionary#A|AesGcmSimple]]
{

    public static byte[] Encrypt(string plaintext, byte[] nonce, out byte[] tag, byte[] key)
    {
        using(var aes = new [[_content/dictionary#A|AesGcm]](key))
        {
            // Tag for authenticated encryption
            tag = new byte[AesGcm.[[_content/dictionary#T|TagByteSizes]].[[_content/dictionary#M|MaxSize]]];

            // Create a byte array from the message to encrypt
            var plaintextBytes = Encoding.UTF8.[[_content/dictionary#G|GetBytes]](plaintext);

            // Ciphertext will be same length in bytes as plaintext
            var ciphertext = new byte[plaintextBytes.Length];

            // perform the actual encryption
            aes.Encrypt(nonce, plaintextBytes, ciphertext, tag);
            return ciphertext;
        }
    }

    public static string Decrypt(byte[] ciphertext, byte[] nonce, byte[] tag, byte[] key)
    {
        using(var aes = new [[_content/dictionary#A|AesGcm]](key))
        {
            // Plaintext will be same length in bytes as Ciphertext
            var plaintextBytes = new byte[ciphertext.Length];

            // perform the actual decryption
            aes.Decrypt(nonce, ciphertext, tag, plaintextBytes);

            return Encoding.UTF8.[[_content/dictionary#G|GetString]](plaintextBytes);
        }
    }
}

##### Encryption for transmission¶

- Again, follow the algorithm guidance in the [[_content/dictionary#O|OWASP]] Cryptographic Storage Cheat Sheet.

The following code snippet shows an example of using Eliptic Curve/Diffie Helman ([[_content/dictionary#E|ECDH]]) together with [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] to perform encryption/decryption of data between two different sides without the need the transfer the symmetric key between the two sides. Instead, the sides exchange public keys and can then use ECDH to generate a shared secret which can be used for the symmetric encryption.
Again, it is strongly recommended to have a cryptography expert review your final design and code, as even the most trivial error can severely weaken your encryption.
Note that this code sample relies on the [[_content/dictionary#A|AesGcmSimple]] class from the [previous section](#encryption-for-storage).
A few constraints/pitfalls with this code:

It does not take into account key rotation or management which is a whole topic in itself.
- The code deliberately enforces a new nonce for every encryption operation but this must be managed as a separate data item alongside the ciphertext.
- The private keys will need to be stored securely.
- The code does not consider the validation of public keys before use.
- Overall, there is no verification of authenticity between the two sides.

Click here to view the "[[_content/dictionary#E|ECDH]] asymmetric encryption" code snippet.
public class ECDHSimpleTest
{
    public static void Main()
    {
        // Generate [[_content/dictionary#E|ECC]] key pair for Alice
        var alice = new ECDHSimple();
        byte[] alicePublicKey = alice.[[_content/dictionary#P|PublicKey]];

        // Generate [[_content/dictionary#E|ECC]] key pair for Bob
        var bob = new ECDHSimple();
        byte[] bobPublicKey = bob.[[_content/dictionary#P|PublicKey]];

        string plaintext = "Hello, Bob! How are you?";
        Console.[[_content/dictionary#W|WriteLine]]("Secret being sent from Alice to Bob: " + plaintext);

        // Note that a new nonce is generated with every encryption operation in line with
        // in line with the [[_content/dictionary#A|AES]] [[_content/dictionary#G|GCM]] security
        byte[] tag;
        byte[] nonce;
        var cipherText = alice.Encrypt(bobPublicKey, plaintext, out nonce, out tag);
        Console.[[_content/dictionary#W|WriteLine]]("Ciphertext, nonce, and tag being sent from Alice to Bob: " + Convert.ToBase64String(cipherText) + " " + Convert.ToBase64String(nonce) + " " + Convert.ToBase64String(tag));

        var decrypted = bob.Decrypt(alicePublicKey, cipherText, nonce, tag);
        Console.[[_content/dictionary#W|WriteLine]]("Secret received by Bob from Alice: " + decrypted);

        Console.[[_content/dictionary#W|WriteLine]]();

        string plaintext2 = "Hello, Alice! I'm good, how are you?";
        Console.[[_content/dictionary#W|WriteLine]]("Secret being sent from Bob to Alice: " + plaintext2);

        byte[] tag2;
        byte[] nonce2;
        var cipherText2 = bob.Encrypt(alicePublicKey, plaintext2, out nonce2, out tag2);
        Console.[[_content/dictionary#W|WriteLine]]("Ciphertext, nonce, and tag being sent from Bob to Alice: " + Convert.ToBase64String(cipherText2) + " " + Convert.ToBase64String(nonce2) + " " + Convert.ToBase64String(tag2));

        var decrypted2 = alice.Decrypt(bobPublicKey, cipherText2, nonce2, tag2);
        Console.[[_content/dictionary#W|WriteLine]]("Secret received by Alice from Bob: " + decrypted2);
    }
}

public class ECDHSimple
{

    private ECDiffieHellmanCng ecdh = new ECDiffieHellmanCng();

    public byte[] [[_content/dictionary#P|PublicKey]]
    {
        get
        {
            return ecdh.PublicKey.[[_content/dictionary#T|ToByteArray]]();
        }
    }

    public byte[] Encrypt(byte[] partnerPublicKey, string message, out byte[] nonce, out byte[] tag)
    {
        // Generate the [[_content/dictionary#A|AES]] Key and Nonce
        var aesKey = GenerateAESKey(partnerPublicKey);

        // Tag for authenticated encryption
        tag = new byte[[[_content/dictionary#A|AesGcm]].[[_content/dictionary#T|TagByteSizes]].[[_content/dictionary#M|MaxSize]]];

        // [[_content/dictionary#M|MaxSize]] = 12 bytes / 96 bits and this size should always be used.
        // A new nonce is generated with every encryption operation in line with
        // the [[_content/dictionary#A|AES]] [[_content/dictionary#G|GCM]] security model
        nonce = new byte[[[_content/dictionary#A|AesGcm]].[[_content/dictionary#N|NonceByteSizes]].MaxSize];
        [[_content/dictionary#R|RandomNumberGenerator]].Fill(nonce);

        // return the encrypted value
        return [[_content/dictionary#A|AesGcmSimple]].Encrypt(message, nonce, out tag, aesKey);
    }

    public string Decrypt(byte[] partnerPublicKey, byte[] ciphertext, byte[] nonce, byte[] tag)
    {
        // Generate the [[_content/dictionary#A|AES]] Key and Nonce
        var aesKey = GenerateAESKey(partnerPublicKey);

        // return the decrypted value
        return [[_content/dictionary#A|AesGcmSimple]].Decrypt(ciphertext, nonce, tag, aesKey);
    }

    private byte[] GenerateAESKey(byte[] partnerPublicKey)
    {
        // Derive the secret based on this side's private key and the other side's public key
        byte[] secret = ecdh.[[_content/dictionary#D|DeriveKeyMaterial]]([[_content/dictionary#C|CngKey]].Import(partnerPublicKey, [[_content/dictionary#C|CngKeyBlobFormat]].[[_content/dictionary#E|EccPublicBlob]]));

        byte[] aesKey = new byte[32]; // 256-bit [[_content/dictionary#A|AES]] key
        Array.Copy(secret, 0, aesKey, 0, 32); // Copy first 32 bytes as the key

        return aesKey;
    }
}

#### A03 Injection¶
##### [[_content/dictionary#S|SQL]] Injection¶
[[_content/dictionary#D|DO]]: Using an object relational mapper ([[_content/dictionary#O|ORM]]) or stored procedures is the most effective way of countering the SQL Injection vulnerability.
DO: Use parameterized queries where a direct SQL query must be used. More Information can be found in the
[[Query_Parameterization_Cheat_Sheet|Query Parameterization Cheat Sheet]].
E.g., using Entity Framework:
var sql = @"Update [User] [[_content/dictionary#S|SET]] [[_content/dictionary#F|FirstName]] = @FirstName [[_content/dictionary#W|WHERE]] Id = @Id";
context.Database.Execute[[[_content/dictionary#S|SqlCommand]]](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlcommand)(
    sql,
    new [[_content/dictionary#S|SqlParameter]]("@FirstName", firstname),
    new SqlParameter("@Id", id));

[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Concatenate strings anywhere in your code and execute them against your database (Known as dynamic [[_content/dictionary#S|SQL]]).
Note: You can still accidentally do this with ORMs or Stored procedures so check everywhere. For example:
string sql = "[[_content/dictionary#S|SELECT]] * [[_content/dictionary#F|FROM]] Users [[_content/dictionary#W|WHERE]] [[_content/dictionary#U|UserName]]='" + txtUser.Text + "' [[_content/dictionary#A|AND]] Password='"
                + txtPassword.Text + "'";
context.Database.[[_content/dictionary#E|ExecuteSqlCommand]](sql); // SQL Injection vulnerability!

[[_content/dictionary#D|DO]]: Practice Least Privilege - connect to the database using an account with a minimum set of permissions required
to do its job, not the database administrator account.
##### [[_content/dictionary#O|OS]] Injection¶
General guidance about OS Injection can be found in the [[OS_Command_Injection_Defense_Cheat_Sheet|OS Command Injection Defense Cheat Sheet]].
DO: Use [System.Diagnostics.Process.Start](https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.process.start?view=netframework-4.7.2) to call underlying OS functions.
e.g
var process = new System.Diagnostics.Process();
var startInfo = new System.Diagnostics.[[_content/dictionary#P|ProcessStartInfo]]();
startInfo.[[_content/dictionary#F|FileName]] = "validatedCommand";
startInfo.Arguments = "validatedArg1 validatedArg2 validatedArg3";
process.[[_content/dictionary#S|StartInfo]] = startInfo;
process.Start();

[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Assume that this mechanism will protect against malicious input designed to break out of one argument and then tamper with another argument to the process. This will still be possible.
DO: Use allowlist validation on all user supplied input wherever possible. Input validation prevents improperly formed data from entering an information system. For more information please see the [[Input_Validation_Cheat_Sheet|Input Validation Cheat Sheet]].
e.g Validating user input using [IPAddress.[[[_content/dictionary#T|TryParse]]](https://docs.microsoft.com/en-us/dotnet/api/system.int32.tryparse#System_Int32_TryParse_System_String_System_Int32__) Method](https://docs.microsoft.com/en-us/dotnet/api/system.net.ipaddress.tryparse?view=netframework-4.8)
//User input
string ipAddress = "127.0.0.1";

//check to make sure an ip address was provided
if (!string.[[_content/dictionary#I|IsNullOrEmpty]](ipAddress))
{
 // Create an instance of IPAddress for the specified address string (in
 // dotted-quad, or colon-hexadecimal notation).
 if (IPAddress.[[_content/dictionary#T|TryParse]](ipAddress, out var address))
 {
  // Display the address in standard notation.
  return address.[[_content/dictionary#T|ToString]]();
 }
 else
 {
  //ipAddress is not of type IPAddress
  ...
 }
    ...
}

[[_content/dictionary#D|DO]]: Try to only accept characters which are simple alphanumeric.
DO [[_content/dictionary#N|NOT]]: Assume you can sanitize special characters without actually removing them. Various combinations of \, ' and @ may have an unexpected impact on sanitization attempts.
DO NOT: Rely on methods without a security guarantee.
e.g. .[[_content/dictionary#N|NET]] Core 2.2 and greater and .NET 5 and greater support [[[_content/dictionary#P|ProcessStartInfo]].[[_content/dictionary#A|ArgumentList]]](https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.argumentlist) which performs some character escaping but the object includes [a disclaimer that it is not safe with untrusted input](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.argumentlist#remarks).
DO: Look at alternatives to passing raw untrusted arguments via command-line parameters such as encoding using Base64 (which would safely encode any special characters as well) and then decode the parameters in the receiving application.
##### [[_content/dictionary#L|LDAP]] injection¶
Almost any characters can be used in Distinguished Names. However, some must be escaped with the backslash \ escape character.
A table showing which characters that should be escaped for Active Directory can be found at the in the
[[LDAP_Injection_Prevention_Cheat_Sheet|[LDAP Injection Prevention Cheat Sheet]]](LDAP_Injection_Prevention_Cheat_Sheet.html).
Note: The space character must be escaped only if it is the leading or trailing character in a component name, such as a Common Name.
Embedded spaces should not be escaped.
More information can be found in the LDAP Injection Prevention Cheat Sheet.
#### A04 Insecure Design¶
Insecure design refers to security failures in the design of the application or system. This is different than the other items
in the [[_content/dictionary#O|OWASP]] Top 10 list which refer to implementation failures. The topic of secure design is therefore not related to a specific
technology or language and is therefore out of scope for this cheat sheet. See the [[Secure_Product_Design_Cheat_Sheet|Secure Product Design Cheat Sheet]] for more information.
#### A05 Security Misconfiguration¶
##### Debug and Stack Trace¶
Ensure debug and trace are off in production. This can be enforced using web.config transforms:
<compilation xdt:Transform="[[_content/dictionary#R|RemoveAttributes]](debug)" />
<trace enabled="false" xdt:Transform="Replace"/>

[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Use default passwords
DO: Redirect a request made over [[_content/dictionary#H|HTTP]] to [[_content/dictionary#H|HTTPS]]:
E.g, Global.asax.cs:
protected void Application_BeginRequest()
{
    #if ![[_content/dictionary#D|DEBUG]]
    // [[_content/dictionary#S|SECURE]]: Ensure any request is returned over [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] in production
    if (!Request.[[_content/dictionary#I|IsLocal]] && !Context.Request.[[_content/dictionary#I|IsSecureConnection]]) {
        var redirect = Context.Request.Url.[[_content/dictionary#T|ToString]]()
                        .[[_content/dictionary#T|ToLower]]([[_content/dictionary#C|CultureInfo]].[[_content/dictionary#C|CurrentCulture]])
                        .Replace("http:", "https:");
        Response.Redirect(redirect);
    }
    #endif
}

E.g., Startup.cs in Configure():
  app.[[_content/dictionary#U|UseHttpsRedirection]]();

##### Cross-site request forgery¶
[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Send sensitive data without validating Anti-Forgery-Tokens (.NET / .NET Core).
DO: Send the anti-forgery token with every [[_content/dictionary#P|POST]]/[[_content/dictionary#P|PUT]] request:
###### Using .[[_content/dictionary#N|NET]] Framework¶
using (Html.[[_content/dictionary#B|BeginForm]]("[[_content/dictionary#L|LogOff]]", "Account", [[_content/dictionary#F|FormMethod]].Post, new { id = "logoutForm",
                        @class = "pull-right" }))
{
    @Html.[[_content/dictionary#A|AntiForgeryToken]]()
    <ul class="nav nav-pills">
        <li role="presentation">
        Logged on as @User.Identity.Name
        </li>
        <li role="presentation">
        <a href="javascript:document.getElementById('logoutForm').submit()">Log off</a>
        </li>
    </ul>
}

Then validate it at the method or preferably the controller level:
[[[_content/dictionary#H|HttpPost]]]
[[[_content/dictionary#V|ValidateAntiForgeryToken]]]
public [[_content/dictionary#A|ActionResult]] [[_content/dictionary#L|LogOff]]()

Make sure the tokens are removed completely for invalidation on logout.
/// <summary>
/// [[_content/dictionary#S|SECURE]]: Remove any remaining cookies including Anti-[[_content/dictionary#C|CSRF]] cookie
/// </summary>
public void [[_content/dictionary#R|RemoveAntiForgeryCookie]](Controller controller)
{
    string[] allCookies = controller.Request.Cookies.[[_content/dictionary#A|AllKeys]];
    foreach (string cookie in allCookies)
    {
        if (controller.Response.Cookies[cookie] != null &&
            cookie == "__RequestVerificationToken")
        {
            controller.Response.Cookies[cookie].Expires = [[_content/dictionary#D|DateTime]].Now.[[_content/dictionary#A|AddDays]](-1);
        }
    }
}

###### Using .[[_content/dictionary#N|NET]] Core 2.0 or later¶
Starting with .NET Core 2.0 it is possible to [automatically generate and verify the antiforgery token](https://docs.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-7.0#aspnet-core-antiforgery-configuration).
If you are using [tag-helpers](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/intro), which is the default for most web project templates, then all forms will automatically send the anti-forgery token. You can check if tag-helpers are enabled by checking if your main _ViewImports.cshtml file contains:
@addTagHelper *, Microsoft.[[_content/dictionary#A|AspNetCore]].Mvc.[[_content/dictionary#T|TagHelpers]]

IHtmlHelper.[[_content/dictionary#B|BeginForm]] also sends anti-forgery-tokens automatically.
If you are not using tag-helpers or IHtmlHelper.BeginForm, you must use the requisite helper on forms as seen here:
<form action="[[_content/dictionary#R|RelevantAction]]" >
@Html.[[_content/dictionary#A|AntiForgeryToken]]()
</form>

To automatically validate all requests other than [[_content/dictionary#G|GET]], [[_content/dictionary#H|HEAD]], [[_content/dictionary#O|OPTIONS]] and [[_content/dictionary#T|TRACE]] you need to add a global action filter with the [Auto[[[_content/dictionary#V|ValidateAntiforgeryToken]]](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.validateantiforgerytokenattribute?view=aspnetcore-7.0)](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.autovalidateantiforgerytokenattribute?view=aspnetcore-7.0) attribute inside your Startup.cs as mentioned in the following [article](https://andrewlock.net/automatically-validating-anti-forgery-tokens-in-asp-net-core-with-the-autovalidateantiforgerytokenattribute/):
services.[[_content/dictionary#A|AddMvc]](options =>
{
    options.Filters.Add(new [[[_content/dictionary#A|AutoValidateAntiforgeryToken]]](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.autovalidateantiforgerytokenattribute?view=aspnetcore-7.0)Attribute());
});

If you need to disable the attribute validation for a specific method on a controller you can add the [[[_content/dictionary#I|IgnoreAntiforgeryToken]]](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.ignoreantiforgerytokenattribute?view=aspnetcore-7.0) attribute to the controller method (for [[_content/dictionary#M|MVC]] controllers) or parent class (for Razor pages):
[IgnoreAntiforgeryToken]
[[[_content/dictionary#H|HttpDelete]]]
public IActionResult Delete()

[[[_content/dictionary#I|IgnoreAntiforgeryToken]]]
public class [[_content/dictionary#U|UnsafeModel]] : [[_content/dictionary#P|PageModel]]

If you need to also validate the token on [[_content/dictionary#G|GET]], [[_content/dictionary#H|HEAD]], [[_content/dictionary#O|OPTIONS]] and [[_content/dictionary#T|TRACE]] requests you can add the [[_content/dictionary#V|ValidateAntiforgeryToken]] attribute to the controller method (for [[_content/dictionary#M|MVC]] controllers) or parent class (for Razor pages):
[[[_content/dictionary#H|HttpGet]]]
[ValidateAntiforgeryToken]
public IActionResult [[_content/dictionary#D|DoSomethingDangerous]]()

[[[_content/dictionary#H|HttpGet]]]
[[[_content/dictionary#V|ValidateAntiforgeryToken]]]
public class [[_content/dictionary#S|SafeModel]] : [[_content/dictionary#P|PageModel]]

In case you can't use a global action filter, add the [[_content/dictionary#A|AutoValidateAntiforgeryToken]] attribute to your controller classes or razor page models:
[AutoValidateAntiforgeryToken]
public class UserController

[[[_content/dictionary#A|AutoValidateAntiforgeryToken]]]
public class [[_content/dictionary#S|SafeModel]] : [[_content/dictionary#P|PageModel]]

###### Using .Net Core or .[[_content/dictionary#N|NET]] Framework with [[_content/dictionary#A|AJAX]]¶
You will need to attach the anti-forgery token to AJAX requests.
If you are using jQuery in an [[_content/dictionary#A|ASP]].NET Core [[_content/dictionary#M|MVC]] view this can be achieved using this snippet:
@inject  Microsoft.[[_content/dictionary#A|AspNetCore]].Antiforgery.IAntiforgery antiforgeryProvider
$.ajax(
{
    type: "[[_content/dictionary#P|POST]]",
    url: '@Url.Action("Action", "Controller")',
    contentType: "application/x-www-form-urlencoded; charset=utf-8",
    data: {
        id: id,
        '__RequestVerificationToken': '@antiforgeryProvider.[[_content/dictionary#G|GetAndStoreTokens]](this.Context).[[_content/dictionary#R|RequestToken]]'
    }
})

If you are using the .[[_content/dictionary#N|NET]] Framework, you can find some code snippets here.
More information can be found in the [[Cross-Site_Request_Forgery_Prevention_Cheat_Sheet|Cross-Site Request Forgery Prevention Cheat Sheet]].
#### A06 Vulnerable and Outdated Components¶
[[_content/dictionary#D|DO]]: Keep the .NET framework updated with the latest patches
DO: Keep your [[_content/dictionary#N|NuGet]] packages up to date
DO: Run the [[[_content/dictionary#O|OWASP]] Dependency Checker](Vulnerable_Dependency_Management_Cheat_Sheet.html#tools) against your application as part of your build process and act on any high or critical level vulnerabilities.
DO: Include [[_content/dictionary#S|SCA]] (software composition analysis) tools in your [[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]] pipeline to ensure that any new vulnerabilities
in your dependencies are detected and acted upon.
#### A07 Identification and Authentication Failures¶
DO: Use [[[_content/dictionary#A|ASP]].NET Core Identity](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-2.2&).
ASP.NET Core Identity framework is well configured by default, where it uses secure password hashes and an individual salt. Identity uses the [[_content/dictionary#P|PBKDF2]] hashing function for passwords, and generates a random salt per user.
DO: Set secure password policy
e.g ASP.NET Core Identity
//Startup.cs
services.Configure<[[_content/dictionary#I|IdentityOptions]]>(options =>
{
 // Password settings
 options.Password.[[_content/dictionary#R|RequireDigit]] = true;
 options.Password.[[_content/dictionary#R|RequiredLength]] = 8;
 options.Password.[[_content/dictionary#R|RequireNonAlphanumeric]] = true;
 options.Password.[[_content/dictionary#R|RequireUppercase]] = true;
 options.Password.[[_content/dictionary#R|RequireLowercase]] = true;
 options.Password.[[_content/dictionary#R|RequiredUniqueChars]] = 6;

 options.Lockout.[[_content/dictionary#D|DefaultLockoutTimeSpan]] = [[_content/dictionary#T|TimeSpan]].[[_content/dictionary#F|FromMinutes]](30);
 options.Lockout.[[_content/dictionary#M|MaxFailedAccessAttempts]] = 3;

 options.[[_content/dictionary#S|SignIn]].[[_content/dictionary#R|RequireConfirmedEmail]] = true;

 options.User.[[_content/dictionary#R|RequireUniqueEmail]] = true;
});

[[_content/dictionary#D|DO]]: Set a cookie policy
e.g
//Startup.cs
services.[[_content/dictionary#C|ConfigureApplicationCookie]](options =>
{
 options.Cookie.[[_content/dictionary#H|HttpOnly]] = true;
 options.Cookie.Expiration = [[_content/dictionary#T|TimeSpan]].[[_content/dictionary#F|FromHours]](1)
 options.[[_content/dictionary#S|SlidingExpiration]] = true;
});

#### A08 Software and Data Integrity Failures¶
[[_content/dictionary#D|DO]]: Digitally sign assemblies and executable files
DO: Use Nuget package signing
DO: Review code and configuration changes to avoid malicious code
or dependencies being introduced
DO [[_content/dictionary#N|NOT]]: Send unsigned or unencrypted serialized objects over the network
DO: Perform integrity checks or validate digital signatures on serialized
objects received from the network
DO NOT: Use the [[_content/dictionary#B|BinaryFormatter]] type which is dangerous and [not recommended](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide) for data processing.
.[[_content/dictionary#N|NET]] offers several in-box serializers that can handle untrusted data safely:

- [[_content/dictionary#X|XmlSerializer]] and [[_content/dictionary#D|DataContractSerializer]] to serialize object graphs into and from [[_content/dictionary#X|XML]]. Do not confuse DataContractSerializer with [[_content/dictionary#N|NetDataContractSerializer]].
- [[_content/dictionary#B|BinaryReader]] and [[_content/dictionary#B|BinaryWriter]] for [[_content/dictionary#X|XML]] and [[_content/dictionary#J|JSON]].
- The System.Text.Json APIs to serialize object graphs into [[_content/dictionary#J|JSON]].

#### A09 Security Logging and Monitoring Failures¶
[[_content/dictionary#D|DO]]: Ensure all login, access control, and server-side input validation failures are logged with sufficient user context to identify suspicious or malicious accounts.
DO: Establish effective monitoring and alerting so suspicious activities are detected and responded to in a timely fashion.
DO [[_content/dictionary#N|NOT]]: Log generic error messages such as: csharp Log.Error("Error was thrown");. Instead, log the stack trace, error message and user ID who caused the error.
DO NOT: Log sensitive data such as user's passwords.
##### Logging¶
What logs to collect and more information about logging can be found in the [[Logging_Cheat_Sheet|Logging Cheat Sheet]].
.[[_content/dictionary#N|NET]] Core comes with a [[_content/dictionary#L|LoggerFactory]], which is in Microsoft.Extensions.Logging. More information about ILogger can be found here.
Here's how to log all errors from the Startup.cs, so that anytime an error is thrown it will be logged:
public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
    if (env.[[_content/dictionary#I|IsDevelopment]]())
    {
        _isDevelopment = true;
        app.[[_content/dictionary#U|UseDeveloperExceptionPage]]();
    }

    //Log all errors in the application
    app.[[_content/dictionary#U|UseExceptionHandler]](errorApp =>
    {
        errorApp.Run(async context =>
        {
            var errorFeature = context.Features.Get<IExceptionHandlerFeature>();
            var exception = errorFeature.Error;

            Log.Error(String.Format("Stacktrace of error: {0}",exception.[[_content/dictionary#S|StackTrace]].[[_content/dictionary#T|ToString]]()));
        });
    });

    app.[[_content/dictionary#U|UseAuthentication]]();
    app.[[_content/dictionary#U|UseMvc]]();
 }
}

E.g. injecting into the class constructor, which makes writing unit test simpler. This is recommended if instances of the class will be created using dependency injection (e.g. [[_content/dictionary#M|MVC]] controllers). The below example shows logging of all unsuccessful login attempts.
public class [[_content/dictionary#A|AccountsController]] : Controller
{
        private ILogger _Logger;

        public [[_content/dictionary#A|AccountsController]](ILogger logger)
        {
            _Logger = logger;
        }

        [[[_content/dictionary#H|HttpPost]]]
        [[[_content/dictionary#A|AllowAnonymous]]]
        [[[_content/dictionary#V|ValidateAntiForgeryToken]]]
        public async Task<IActionResult> Login([[_content/dictionary#L|LoginViewModel]] model)
        {
            if ([[_content/dictionary#M|ModelState]].[[_content/dictionary#I|IsValid]])
            {
                var result = await _signInManager.[[_content/dictionary#P|PasswordSignInAsync]](model.Email, model.Password, model.[[_content/dictionary#R|RememberMe]], lockoutOnFailure: false);
                if (result.Succeeded)
                {
                    //Log all successful log in attempts
                    Log.Information(String.Format("User: {0}, Successfully Logged in", model.Email));
                    //Code for successful login
                    //...
                }
                else
                {
                    //Log all incorrect log in attempts
                    Log.Information(String.Format("User: {0}, Incorrect Password", model.Email));
                }
             }
            ...
        }

##### Monitoring¶
Monitoring allow us to validate the performance and health of a running system through key performance indicators.
In .[[_content/dictionary#N|NET]] a great option to add monitoring capabilities is [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/asp-net-core).
More information about Logging and Monitoring can be found here.
#### A10 Server-Side Request Forgery ([[_content/dictionary#S|SSRF]])¶
[[_content/dictionary#D|DO]]: Validate and sanitize all user input before using it to make a request
DO: Use an allowlist of allowed protocols and domains
DO: Use IPAddress.[[_content/dictionary#T|TryParse]]() and Uri.[[_content/dictionary#C|CheckHostName]]() to ensure that [[_content/dictionary#I|IP]] addresses and domain names are valid
DO [[_content/dictionary#N|NOT]]: Follow [[_content/dictionary#H|HTTP]] redirects
DO NOT: Forward raw HTTP responses to the user
For more information please see the [[Server_Side_Request_Forgery_Prevention_Cheat_Sheet|Server-Side Request Forgery Prevention Cheat Sheet]].
#### [[_content/dictionary#O|OWASP]] 2013 & 2017¶
Below are vulnerabilities that were included in the 2013 or 2017 OWASP Top 10 list
that were not included in the 2021 list. These vulnerabilities are still relevant
but were not included in the 2021 list because they have become less prevalent.
##### A04:2017 [[_content/dictionary#X|XML]] External Entities ([[_content/dictionary#X|XXE]])¶
XXE attacks occur when an XML parse does not properly process user input that contains external entity declarations in the doctype of an XML payload.
[This article](https://docs.microsoft.com/en-us/dotnet/standard/data/xml/xml-processing-options) discusses the most common XML Processing Options for .NET.
Please refer to the [XXE cheat sheet](XML_External_Entity_Prevention_Cheat_Sheet.html#net) for more detailed information on preventing XXE and other XML Denial of Service attacks.
##### A07:2017 Cross-Site Scripting ([[_content/dictionary#X|XSS]])¶
DO NOT: Trust any data the user sends you. Prefer allowlists (always safe) over denylists.
You get encoding of all [[_content/dictionary#H|HTML]] content with MVC3. To properly encode all content whether HTML,
[[_content/dictionary#J|JavaScript]], [[_content/dictionary#C|CSS]], [[_content/dictionary#L|LDAP]], etc., use the Microsoft AntiXSS library:
Install-Package AntiXSS
Then set in config:
<system.web>
<httpRuntime targetFramework="4.5"
enableVersionHeader="false"
encoderType="Microsoft.Security.Application.[[[_content/dictionary#A|AntiXssEncoder]]](https://docs.microsoft.com/en-us/dotnet/api/system.web.security.antixss.antixssencoder?view=netframework-4.7.2), [[_content/dictionary#A|AntiXssLibrary]]"
maxRequestLength="4096" />

[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Use the [AllowHTML] attribute or helper class @Html.Raw unless you are absolutely
sure that the content you are writing to the browser is safe and has been escaped properly.
DO: Enable a [Content Security Policy](Content_Security_Policy_Cheat_Sheet.html#context). This will prevent your pages from accessing assets they should not be able to access (e.g. malicious scripts):
<system.webServer>
    <httpProtocol>
        <customHeaders>
            <add name="Content-Security-Policy"
                value="default-src 'none'; style-src 'self'; img-src 'self';
                font-src 'self'; script-src 'self'" />

More information can be found in the [[Cross_Site_Scripting_Prevention_Cheat_Sheet|Cross Site Scripting Prevention Cheat Sheet]].
##### A08:2017 Insecure Deserialization¶
[[_content/dictionary#D|DO]] [[_content/dictionary#N|NOT]]: Accept Serialized Objects from Untrusted Sources
DO: Validate User Input
Malicious users are able to use objects like cookies to insert malicious information to change user roles. In some cases, hackers are able to elevate their privileges to administrator rights by using a pre-existing or cached password hash from a previous session.
DO: Prevent Deserialization of Domain Objects
DO: Run the Deserialization Code with Limited Access Permissions
If a deserialized hostile object tries to initiate a system process or access a resource within the server or the host's [[_content/dictionary#O|OS]], it will be denied access and a permission flag will be raised so that a system administrator is made aware of any anomalous activity on the server.
More information about Insecure Deserialization can be found in the [Deserialization Cheat Sheet](Deserialization_Cheat_Sheet.html#net-csharp).
##### A10:2013 Unvalidated redirects and forwards¶
A protection against this was introduced in [[_content/dictionary#M|MVC]] 3 template. Here is the code:
public async Task<[[_content/dictionary#A|ActionResult]]> [[_content/dictionary#L|LogOn]]([[_content/dictionary#L|LogOnViewModel]] model, string returnUrl)
{
    if ([[_content/dictionary#M|ModelState]].[[_content/dictionary#I|IsValid]])
    {
        var logonResult = await _userManager.[[_content/dictionary#T|TryLogOnAsync]](model.[[_content/dictionary#U|UserName]], model.Password);
        if (logonResult.Success)
        {
            await _userManager.[[_content/dictionary#L|LogOnAsync]](logonResult.UserName, model.[[_content/dictionary#R|RememberMe]]);  
            return [[_content/dictionary#R|RedirectToLocal]](returnUrl);
...

private [[_content/dictionary#A|ActionResult]] [[_content/dictionary#R|RedirectToLocal]](string returnUrl)
{
    if (Url.[[_content/dictionary#I|IsLocalUrl]](returnUrl))
    {
        return Redirect(returnUrl);
    }
    else
    {
        return [[_content/dictionary#R|RedirectToAction]]("Landing", "Account");
    }
}

#### Other advice¶

Protect against Clickjacking and Man-in-the-Middle attack from capturing an initial Non-[[_content/dictionary#T|TLS]] request: Set the X-Frame-Options and Strict-Transport-Security ([[[_content/dictionary#H|HSTS]]](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Strict-Transport-Security)) headers. Full details here
Protect against a man-in-the-middle attack for a user who has never been to your site before. Register for [HSTS preload](https://hstspreload.org/)
- Maintain security testing and analysis on Web [[_content/dictionary#A|API]] services. They are hidden inside [[_content/dictionary#M|MVC]] sites, and are public parts of a site that
will be found by an attacker. All of the MVC guidance and much of the [[_content/dictionary#W|WCF]] guidance applies to Web API as well.
Also see the [[Unvalidated_Redirects_and_Forwards_Cheat_Sheet|Unvalidated Redirects and Forwards Cheat Sheet]].

##### Sample project¶
For more information on all of the above and code samples incorporated into a sample MVC5 application with an enhanced security baseline
go to [Security Essentials Baseline project](http://github.com/johnstaveley/[[_content/dictionary#S|SecurityEssentials]]/).
### Guidance for specific topics¶
This section contains guidance for specific topics in .[[_content/dictionary#N|NET]].
#### Configuration and Deployment¶

Lock down config files.
- - Remove all aspects of configuration that are not in use.
Encrypt sensitive parts of the web.config using aspnet_regiis -pe ([command line help](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-2.0/k6h9cz8h(v=vs.80))).

- For [[_content/dictionary#C|ClickOnce]] applications, the .[[_content/dictionary#N|NET]] Framework should be upgraded to use the latest version to ensure support of [[_content/dictionary#T|TLS]] 1.2 or later.

#### Data Access¶

Use [Parameterized [[_content/dictionary#S|SQL]]](https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlcommand.prepare?view=netframework-4.7.2) commands for all data access, without exception.
Do not use [[_content/dictionary#S|SqlCommand]] with a string parameter made up of a [concatenated SQL String](https://docs.microsoft.com/en-gb/visualstudio/code-quality/ca2100-review-sql-queries-for-security-vulnerabilities?view=vs-2017).
List allowable values coming from the user. Use enums, [[_content/dictionary#T|TryParse]] or lookup values to assure that the data coming from the user is as expected.
Enums are still vulnerable to unexpected values because .[[_content/dictionary#N|NET]] only validates a successful cast to the underlying data type, integer by default. [Enum.[[_content/dictionary#I|IsDefined]]](https://docs.microsoft.com/en-us/dotnet/api/system.enum.isdefined) can validate whether the input value is valid within the list of defined constants.

- Apply the principle of least privilege when setting up the Database User in your database of choice. The database user should only be able to access items that make sense for the use case.
Use of Entity Framework is a very effective [[SQL_Injection_Prevention_Cheat_Sheet|[[_content/dictionary#S|SQL]] injection]] prevention mechanism. Remember that building your own ad hoc queries in Entity Framework is just as susceptible to SQLi as a plain SQL query.
When using SQL Server, prefer [integrated authentication](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/using-integrated-authentication?view=sql-server-ver16) over [SQL authentication](https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode?view=sql-server-ver16#connecting-through-sql-server-authentication).
Use [Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine) where possible for sensitive data (SQL Server 2016+ and Azure SQL)

### [[_content/dictionary#A|ASP]] [[_content/dictionary#N|NET]] Web Forms Guidance¶
ASP.NET Web Forms is the original browser-based application development [[_content/dictionary#A|API]] for the .NET Framework, and is still the most common enterprise platform for web application development.

- Always use [[_content/dictionary#H|HTTPS]].
- Enable requireSSL on cookies and form elements and [[_content/dictionary#H|HttpOnly]] on cookies in the web.config.
Implement [customErrors](https://docs.microsoft.com/en-us/dotnet/api/system.web.configuration.customerror).
Make sure [tracing](http://www.iis.net/configreference/system.webserver/tracing) is turned off.
While [[_content/dictionary#V|ViewState]] isn't always appropriate for web development, using it can provide [[_content/dictionary#C|CSRF]] mitigation. To make the ViewState protect against CSRF attacks you need to set the [[[_content/dictionary#V|ViewStateUserKey]]](https://docs.microsoft.com/en-us/dotnet/api/system.web.ui.page.viewstateuserkey):

protected override [[_content/dictionary#O|OnInit]]([[_content/dictionary#E|EventArgs]] e) {
    base.OnInit(e);
    [[_content/dictionary#V|ViewStateUserKey]] = Session.SessionID;
}

If you don't use Viewstate, then look to the default main page of the ASP.NET Web Forms default template for a manual anti-CSRF token using a double-submit cookie.
private const string AntiXsrfTokenKey = "__AntiXsrfToken";
private const string AntiXsrfUserNameKey = "__AntiXsrfUserName";
private string _antiXsrfTokenValue;
protected void Page_Init(object sender, EventArgs e)
{
    // The code below helps to protect against XSRF attacks
    var requestCookie = Request.Cookies[AntiXsrfTokenKey];
    Guid requestCookieGuidValue;
    if (requestCookie != null && Guid.TryParse(requestCookie.Value, out requestCookieGuidValue))
    {
       // Use the Anti-XSRF token from the cookie
       _antiXsrfTokenValue = requestCookie.Value;
       Page.ViewStateUserKey = _antiXsrfTokenValue;
    }
    else
    {
       // Generate a new Anti-XSRF token and save to the cookie
       _antiXsrfTokenValue = Guid.NewGuid().ToString("N");
       Page.ViewStateUserKey = _antiXsrfTokenValue;
       var responseCookie = new HttpCookie(AntiXsrfTokenKey)
       {
          HttpOnly = true,
          Value = _antiXsrfTokenValue
       };
       if (FormsAuthentication.RequireSSL && Request.IsSecureConnection)
       {
          responseCookie.Secure = true;
       }
       Response.Cookies.Set(responseCookie);
    }
    Page.PreLoad += master_Page_PreLoad;
}
protected void master_Page_PreLoad(object sender, EventArgs e)
{
    if (!IsPostBack)
    {
       // Set Anti-XSRF token
       ViewState[AntiXsrfTokenKey] = Page.ViewStateUserKey;
       ViewState[AntiXsrfUserNameKey] = Context.User.Identity.Name ?? String.Empty;
    }
    else
    {
       // Validate the Anti-XSRF token
       if ((string)ViewState[AntiXsrfTokenKey] != _antiXsrfTokenValue ||
          (string)ViewState[AntiXsrfUserNameKey] != (Context.User.Identity.Name ?? String.Empty))
       {
          throw new InvalidOperationException("Validation of Anti-XSRF token failed.");
       }
    }
}

- Consider [[_content/dictionary#H|HSTS]] in [[_content/dictionary#I|IIS]]. See here for the procedure.
- This is a recommended web.config setup that handles [[_content/dictionary#H|HSTS]] among other things.

<?xml version="1.0" encoding="[[_content/dictionary#U|UTF]]-8"?>
 <configuration>
   <system.web>
     <httpRuntime enableVersionHeader="false"/>
   </system.web>
   <system.webServer>
     <security>
       <requestFiltering removeServerHeader="true" />
     </security>
     <staticContent>
       <clientCache cacheControlCustom="public"
            cacheControlMode="[[_content/dictionary#U|UseMaxAge]]"
            cacheControlMaxAge="1.00:00:00"
            setEtag="true" />
     </staticContent>
     <httpProtocol>
       <customHeaders>
         <add name="Content-Security-Policy"
            value="default-src 'none'; style-src 'self'; img-src 'self'; font-src 'self'" />
         <add name="X-Content-Type-Options" value="[[_content/dictionary#N|NOSNIFF]]" />
         <add name="X-Frame-Options" value="[[_content/dictionary#D|DENY]]" />
         <add name="X-Permitted-Cross-Domain-Policies" value="master-only"/>
         <add name="X-[[_content/dictionary#X|XSS]]-Protection" value="0"/>
         <remove name="X-Powered-By"/>
       </customHeaders>
     </httpProtocol>
     <rewrite>
       <rules>
         <rule name="Redirect to https">
           <match url="(.*)"/>
           <conditions>
             <add input="{[[_content/dictionary#H|HTTPS]]}" pattern="Off"/>
             <add input="{REQUEST_METHOD}" pattern="^get$|^head$" />
           </conditions>
           <action type="Redirect" url="https://{HTTP_HOST}/{R:1}" redirectType="Permanent"/>
         </rule>
       </rules>
       <outboundRules>
         <rule name="Add [[_content/dictionary#H|HSTS]] Header" enabled="true">
           <match serverVariable="RESPONSE_Strict_Transport_Security" pattern=".*" />
           <conditions>
             <add input="{HTTPS}" pattern="on" ignoreCase="true" />
           </conditions>
           <action type="Rewrite" value="max-age=15768000" />
         </rule>
       </outboundRules>
     </rewrite>
   </system.webServer>
 </configuration>

- Remove the version header by adding the following line in Machine.config file:

<httpRuntime enableVersionHeader="false" />

- Also remove the Server header using the [[_content/dictionary#H|HttpContext]] Class in your code.

[[_content/dictionary#H|HttpContext]].Current.Response.Headers.Remove("Server");

#### [[_content/dictionary#H|HTTP]] validation and encoding¶

Do not disable [validateRequest](http://www.asp.net/whitepapers/request-validation) in the web.config or the page setup. This value enables limited XSS protection in [[_content/dictionary#A|ASP]].NET and should be left intact as it provides partial prevention of Cross Site Scripting. Complete request validation is recommended in addition to the built-in protections.
- The 4.5 version of the .[[_content/dictionary#N|NET]] Frameworks includes the [[_content/dictionary#A|AntiXssEncoder]] library, which has a comprehensive input encoding library for the prevention of [[_content/dictionary#X|XSS]]. Use it.
- List allowable values anytime user input is accepted.
Validate the format of URIs using [Uri.[[_content/dictionary#I|IsWellFormedUriString]]](https://docs.microsoft.com/en-us/dotnet/api/system.uri.iswellformeduristring).

#### Forms authentication¶

Use cookies for persistence when possible. Cookieless auth will default to [[[_content/dictionary#U|UseDeviceProfile]]](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpcookiemode?view=netframework-4.7.2).
- Don't trust the [[_content/dictionary#U|URI]] of the request for persistence of the session or authorization. It can be easily faked.
Reduce the Forms Authentication timeout from the default of 20 minutes to the shortest period appropriate for your application. If [[[slidingExpiration](https://docs.microsoft.com/en-us/dotnet/api/system.web.security.formsauthentication.slidingexpiration?view=netframework-4.7.2)](https://docs.microsoft.com/en-us/dotnet/api/system.web.security.formsauthentication.slidingexpiration?view=netframework-4.7.2)](https://docs.microsoft.com/en-us/dotnet/api/system.web.security.formsauthentication.slidingexpiration?view=netframework-4.7.2) is used this timeout resets after each request, so active users won't be affected.
- If [[_content/dictionary#H|HTTPS]] is not used, slidingExpiration should be disabled. Consider disabling slidingExpiration even with HTTPS.
- Always implement proper access controls.
- - Compare user provided username with User.Identity.Name.
- - Check roles against User.Identity.[[_content/dictionary#I|IsInRole]].

Use the [[[_content/dictionary#A|ASP]].[[_content/dictionary#N|NET]] Membership provider and role provider](https://docs.microsoft.com/en-us/dotnet/framework/wcf/samples/membership-and-role-provider), but review the password storage. The default storage hashes the password with a single iteration of [[_content/dictionary#S|SHA]]-1 which is rather weak. The ASP.NET MVC4 template uses [ASP.NET Identity](http://www.asp.net/identity/overview/getting-started/introduction-to-aspnet-identity) instead of ASP.NET Membership, and ASP.NET Identity uses [[_content/dictionary#P|PBKDF2]] by default which is better. Review the [[_content/dictionary#O|OWASP]] Password Storage Cheat Sheet for more information.
- Explicitly authorize resource requests.
- Leverage role based authorization using User.Identity.[[_content/dictionary#I|IsInRole]].

### [[_content/dictionary#X|XAML]] Guidance¶

- Work within the constraints of Internet Zone security for your application.
- - Use [[_content/dictionary#C|ClickOnce]] deployment. For enhanced permissions, use permission elevation at runtime or trusted application deployment at install time.

### Windows Forms Guidance¶

- Use partial trust when possible. Partially trusted Windows applications reduce the attack surface of an application. Manage a list of what permissions your app must use, and what it may use, and then make the request for those permissions declaratively at runtime.
Use [[_content/dictionary#C|ClickOnce]] deployment. For enhanced permissions, use permission elevation at runtime or trusted application deployment at install time.

### [[_content/dictionary#W|WCF]] Guidance¶

- Keep in mind that the only safe way to pass a request in RESTful services is via [[_content/dictionary#H|HTTP]] [[_content/dictionary#P|POST]], with [[_content/dictionary#T|TLS]] enabled.
Using HTTP [[_content/dictionary#G|GET]] necessitates putting the data in the [[_content/dictionary#U|URL]] (e.g. the query string) which is visible to the user and will
be logged and stored in their browser history.
Avoid [[[_content/dictionary#B|BasicHttpBinding]]](https://docs.microsoft.com/en-us/dotnet/api/system.servicemodel.basichttpbinding?view=netframework-4.7.2). It has no default security configuration. Use [WSHttpBinding](https://docs.microsoft.com/en-us/dotnet/api/system.servicemodel.wshttpbinding?view=netframework-4.7.2) instead.
Use at least two security modes for your binding. Message security includes security provisions in the headers. Transport security means use of [[_content/dictionary#S|SSL]]. [[[_content/dictionary#T|TransportWithMessageCredential]]](https://docs.microsoft.com/en-us/dotnet/framework/wcf/samples/ws-transport-with-message-credential) combines the two.
Test your [[_content/dictionary#W|WCF]] implementation with a fuzzer like [[[_content/dictionary#Z|ZAP]]](https://www.zaproxy.org/).