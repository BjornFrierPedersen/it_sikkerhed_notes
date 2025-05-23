---
title: "Pinning Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html"
created: "1741872882.077294"
tags: [owasp, cheatsheet, security]
---
# Pinning

## Pinning Cheat Sheet[[[[[[[[[[[[[[[[[[[[¶](#references)](#electron)](#openssl)](#net)](#ios)](#android)](#examples-of-pinning)](#hash)](#public-key)](#certificate)](#what-should-be-pinned)](#how-do-you-pin)](#when-to-apply-exceptions)](#when-do-you-not-pin)](#when-do-you-perform-pinning)](#when-to-add-a-pin)](#what-is-pinning)](#whats-the-problem)](#introduction)](#pinning-cheat-sheet)
### Introduction¶
The Pinning Cheat Sheet is a technical guide to implementing certificate and public key pinning as discussed by Jeffrey Walton at the Virginia chapter's presentation [Securing Wireless Channels in the Mobile Space](https://wiki.owasp.org/images/8/8f/Securing-Wireless-Channels-in-the-Mobile-Space.ppt). This guide is focused on providing clear, simple, actionable guidance for securing the channel in a hostile environment where actors could be malicious and the conference of trust a liability.
### What's the problem¶
Users, developers, and applications expect security on their communication channels, but some channels may not meet this expectation. Channels built using well known protocols like [[_content/dictionary#S|SSL]], and [[_content/dictionary#T|TLS]] can be vulnerable to Man-in-the-Middle ([[_content/dictionary#M|MITM]]) attacks if certificate-based trusts are misused. Malicious attacks come in two forms:

1. An attacker is able to acquire a rogue digital certificate from a trusted certificate authority ([[_content/dictionary#C|CA]]) in the name of the victim site;
2. The attacker is able to inject a dangerous CA into the client’s trust store.

In the case of the latter issue, an attacker with the access to update a trust store will have the access to change the workings of the mobile application, potentially defeating pinning.
As [[Certificate and Public Key Pinning](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning) makes clear, this problem is very small due to years of security advancements by the certificate authority and browser communities.
### What Is Pinning¶
Pinning is the process of associating a host with their expected X509 certificate or public key. Once a certificate or public key is known or seen for a host, the certificate or public key is associated or 'pinned' to the host. If more than one certificate or public key is acceptable, then the program holds a pinset (taken from [Jon Larimer and Kenny Root Google I/O talk](https://www.youtube.com/watch?v=RPJENzweI-A)). In this case, the advertised credential must match one of the elements in the pinset.
#### When to Add a Pin¶
A host or service's certificate or public key can be added to an application at development time, it can be added upon first encountering the certificate or public key (an approach commonly known as “Trust On First Use”, or [[_content/dictionary#T|TOFU]]), or it can be added and updated in real time via an unpinned channel. The former - adding at development time - is preferred since preloading the certificate or public key out-of-band usually means the attacker cannot taint the pin.
Keep in mind that this "when" is about at what point in time you pin. The first question should be, “Should I Pin?”. The answer to this is probably never.
#### When Do You Perform Pinning¶
There is almost no situation where you should consider pinning. The risk of outages almost always outweighs any security risks given advances in security. If you consider pinning, you should read Certificate and Public Key Pinning and fully understand the threat model.
#### When Do You Not Pin?¶

- If you don’t control the client and server side of the connection, don’t pin.
- If you can’t update the pinset securely, don’t pin.
- If updating the pinset is disruptive, such as requiring application redeployment, probably don’t pin. (A possible exception is when you control the redeployment of the application, such as in forced updates within the confines of a corporation.)
- If the certificate key pair cannot be predicted in advance before it is put into service, don’t pin.
- If it is not a native mobile application, do not pin.

#### When to Apply Exceptions¶
If you are working for an organization which practices "egress filtering" as part of a Data Loss Prevention ([[_content/dictionary#D|DLP]]) strategy, you will likely encounter Interception Proxies. We like to refer to these things as "good" bad actors (as opposed to "bad" bad actors) since both break end-to-end security and we can't tell them apart. In this case, do not offer to allow-list the interception proxy since it defeats your security goals. Add the interception proxy's public key to your pinset after being instructed to do so by the folks in Risk Acceptance.
#### How Do You Pin¶
The idea is to reuse the existing protocols and infrastructure, but use them in a hardened manner. For reuse, a program would keep doing the things it used to do when establishing a secure connection.
To harden the channel, the program would take advantage of the [[_content/dictionary#O|OnConnect]] callback offered by a library, framework or platform. In the callback, the program would verify the remote host's identity by validating its certificate or public key. See [some examples](#examples-of-pinning) below.
#### What Should Be Pinned¶
In order to decide what should be pinned you can follow the following steps.

1. Decide if you want to pin the root [[_content/dictionary#C|CA]], intermediate CA or leaf certificate:

- Pinning the root [[_content/dictionary#C|CA]] is generally not recommended since it highly increases the risk because it implies also trusting all its intermediate CAs.
- Pinning a specific issuing or intermediate [[_content/dictionary#C|CA]] reduces the risk but the application will be also trusting any other certificates issued by that CA or sub-CAs, not only the ones meant for your application.
- Pinning a leaf certificate is recommended but must include backup (e.g. intermediate [[_content/dictionary#C|CA]] or a pinset containing alternates). This provides 100% certainty that the app exclusively trusts the remote hosts it was designed to connect to while adding resiliency for failover or certificate rotation.

For example, the application pins the remote endpoint leaf certificate but includes a backup pin for the intermediate [[_content/dictionary#C|CA]]. This increases the risk by trusting more certificate authorities but decreases the chances of bricking your app. If there's any issue with the leaf certificate, the app can always fall back to the intermediate CA until you release an app update.

1. Choose if you want to pin the whole certificate or just its public key.

2. If you chose the public key, you have two additional choices:

- Pin the subjectPublicKeyInfo.
- Pin one of the concrete types such as RSAPublicKey or DSAPublicKey.

The three choices are explained below in more detail. You are encouraged to pin the subjectPublicKeyInfo because it has the public parameters (such as {e,n} for an [[_content/dictionary#R|RSA]] public key) and contextual information such as an algorithm and [[_content/dictionary#O|OID]]. The context will help you keep your bearings at times, and the figure to the right shows the additional information available.
##### Certificate¶
The certificate is easiest to pin. You can fetch the certificate out of band for the website, have the [[_content/dictionary#I|IT]] folks email your company certificate to you, use openssl s_client to retrieve the certificate, etc. At runtime, you can retrieve the website or server's certificate in a callback. Within the callback, you compare the retrieved certificate with the certificate embedded within the program. If the comparison fails, then fail the method or function, log it on the client-side and alert the end user. If your threat model warrants pinning, understand that users will click past any warnings, so do not give the user an option to proceed and bypass the pin.
Benefits:

- It might be easier to implement than the other methods, especially in languages such as Cocoa/[[_content/dictionary#C|CocoaTouch]] and OpenSSL.

Downsides:

- If the site rotates its certificate on a regular basis, then your application would need to be updated regularly. If you do not control when this certificate is put into service, then pinning will lead to an outage.

##### Public Key¶
Public key pinning is more flexible but a little trickier due to the extra steps necessary to extract the public key from a certificate. As with a certificate, the program checks the extracted public key with its embedded copy of the public key. Given that most certificates today are only good for 90 days, using public key pinning can also make the timeline for updating pinsets longer, as you can pin a key where the certificate has not even been issued yet.
Benefits:

- It allows access to public key parameters (such as {e,n} for an [[_content/dictionary#R|RSA]] public key) and contextual information such as an algorithm and [[_content/dictionary#O|OID]].
- It's more flexible than certificate pinning. The pin can be calculated long before the certificate is issued and if policy allows, the certificate can be renewed with the same key to avoid breaking pinning. The latter is a bad key management practice and should only be used in an emergency.

Downsides:

- It can be harder to work with keys (versus certificates) since you must extract the key from the certificate. Extraction is a minor inconvenience in Java and .Net, but it's uncomfortable in the iOS Cocoa/[[_content/dictionary#C|CocoaTouch]] framework and OpenSSL.
- Some service providers generate new keys upon renewal making pre-caching impossible.

##### Hash¶
While the three choices above used [[_content/dictionary#D|DER]] encoding, it's also acceptable to use a hash of the information. In fact, the original sample programs were written using digested certificates and public keys. The samples were changed to allow a programmer to inspect the objects with tools like dumpasn1 and other [[_content/dictionary#A|ASN]].1 decoders.
Benefits:

- It's convenient to use. A digested certificate fingerprint is often available as a native [[_content/dictionary#A|API]] for many libraries.
- The hash is small and a fixed length.

Downsides:

- No access to public key parameters nor contextual information such as an algorithm and [[_content/dictionary#O|OID]] which might be needed in certain use cases.
- If the site rotates its certificate on a regular basis, then your application would need to be updated regularly. If you do not control when this certificate is put into service, then pinning would lead to an outage.

### Examples of Pinning¶
This section discusses certificate and public key pinning in Android Java, iOS, .Net, and OpenSSL. Code has been omitted for brevity, but the key points for the platform are highlighted.
#### Android¶
Since Android N, the preferred way for implementing pinning is by leveraging Android's [Network Security Configuration](https://developer.android.com/training/articles/security-config.html) feature, which lets apps customize their network security settings in a safe, declarative configuration file without modifying app code.
To enable pinning, [the <pin-set> configuration setting](https://developer.android.com/training/articles/security-config.html#[[_content/dictionary#C|CertificatePinning]]) can be used.
Alternatively you can use methods such as the pinning from OkHTTP in order to set specific pins programmatically, as explained in the [[[_content/dictionary#O|OWASP]] [Mobile Security Testing Guide](https://github.com/OWASP/owasp-mstg) ([[_content/dictionary#M|MSTG]])](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#network-libraries-and-webviews) and [the OKHttp documentation](https://square.github.io/okhttp/3.x/okhttp/okhttp3/[[_content/dictionary#C|CertificatePinner]].html).
The Android documentation provides an example of how [[_content/dictionary#S|SSL]] validation can be customized within the app's code (in order to implement pinning) in the [Unknown [[_content/dictionary#C|CA]] implementation document](https://developer.android.com/training/articles/security-ssl.html#[[_content/dictionary#U|UnknownCa]]). However, implementing pinning validation from scratch should be avoided, as implementation mistakes are extremely likely and usually lead to severe vulnerabilities.
Lastly, if you want to validate whether the pinning is successful, please follow instructions from the [[introduction into testing network communication](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md#testing-network-communication)](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md#testing-network-communication) and the [Android specific network testing](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md) chapters of the - OWASP Mobile Security Testing Guide (MSTG).
#### iOS¶
Apple suggests pinning a CA public key by specifying it in Info.plist file under [App Transport Security Settings](https://developer.apple.com/documentation/security/preventing_insecure_network_connections). More details in the article ["Identity Pinning: How to configure server certificates for your app"](https://developer.apple.com/news/?id=g9ejcf8y).
[[[_content/dictionary#T|TrustKit]]](https://github.com/datatheorem/TrustKit), an open-source SSL pinning library for iOS and macOS is available. It provides an easy-to-use [[_content/dictionary#A|API]] for implementing pinning, and has been deployed in many apps.
Otherwise, more details regarding how SSL validation can be customized on iOS (in order to implement pinning) are available in the [[[_content/dictionary#H|HTTPS]] Server Trust Evaluation](https://developer.apple.com/library/content/technotes/tn2232/_index.html) technical note. However, implementing pinning validation from scratch should be avoided, as implementation mistakes are extremely likely and usually lead to severe vulnerabilities.
Lastly, if you want to validate whether the pinning is successful, please follow instructions from the introduction into testing network communication and the [iOS specific network testing](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md) chapters of the OWASP Mobile Security Testing Guide (MSTG).
#### .Net¶
.Net pinning can be achieved by using [[[_content/dictionary#S|ServicePointManager]]](https://docs.microsoft.com/en-us/dotnet/api/system.net.servicepointmanager?view=netframework-4.7.2). An example can be found at the [OWASP MSTG](https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#xamarin-applications).
Download the [.Net sample program](../assets/Pinning_Cheat_Sheet_Certificate_DotNetSample.zip).
#### OpenSSL¶
Pinning can occur at one of two places with OpenSSL. First is the user supplied verify_callback. Second is after the connection is established via SSL_get_peer_certificate. Either method will allow you to access the peer's certificate.
Though OpenSSL performs the X509 checks, you must fail the connection and tear down the socket on error. By design, a server that does not supply a certificate will result in X509_V_OK with a [[_content/dictionary#N|NULL]] certificate. To check the result of the customary verification:

1. You must call SSL_get_verify_result and verify the return code is X509_V_OK;
2. You must call SSL_get_peer_certificate and verify the certificate is non-[[_content/dictionary#N|NULL]].

Download: [OpenSSL sample program](../assets/Pinning_Cheat_Sheet_Certificate_OpenSSLSample.zip).
#### [Electron](https://electronjs.org)¶
[electron-ssl-pinning](https://github.com/dialogs/electron-ssl-pinning), an open-source [[_content/dictionary#S|SSL]] pinning library for Electron based applications. It provides an easy-to-use [[_content/dictionary#A|API]] for implementing pinning and also provides a tool for fetching configuration based on needed hosts.
Otherwise, you can validate certificates by yourself using [ses.setCertificateVerifyProc(proc)](https://electronjs.org/docs/api/session#sessetcertificateverifyprocproc).
### References¶

[[_content/dictionary#O|OWASP]] [Injection Theory](https://owasp.org/www-community/Injection_Theory)
OWASP [Data Validation](https://wiki.owasp.org/index.php/Data_Validation)
OWASP [[Transport_Layer_Security_Cheat_Sheet|Transport Layer Security Cheat Sheet]]
OWASP Mobile Security Testing Guide
[[_content/dictionary#I|IETF]] [[[_content/dictionary#R|RFC]] 1421 ([[_content/dictionary#P|PEM]] Encoding)](http://www.ietf.org/rfc/rfc1421.txt)
IETF [RFC 4648 (Base16, Base32, and Base64 Encodings)](http://www.ietf.org/rfc/rfc4648.txt)
IETF [RFC 5280 (Internet [[_content/dictionary#X|X.509]], [[_content/dictionary#P|PKIX]])](http://www.ietf.org/rfc/rfc5280.txt)
IETF [RFC 3279 ([[_content/dictionary#P|PKI]], X509 Algorithms and [[_content/dictionary#C|CRL]] Profiles)](http://www.ietf.org/rfc/rfc3279.txt)
IETF [RFC 4055 (PKI, X509 Additional Algorithms and CRL Profiles)](http://www.ietf.org/rfc/rfc4055.txt)
IETF [RFC 2246 ([[_content/dictionary#T|TLS]] 1.0)](http://www.ietf.org/rfc/rfc2246.txt)
IETF [RFC 4346 (TLS 1.1)](http://www.ietf.org/rfc/rfc4346.txt)
IETF [RFC 5246 (TLS 1.2)](http://www.ietf.org/rfc/rfc5246.txt)
IETF [[[_content/dictionary#P|PKCS]] #1: [[_content/dictionary#R|RSA]] Cryptography Specifications Version 2.2](https://tools.ietf.org/html/rfc8017)