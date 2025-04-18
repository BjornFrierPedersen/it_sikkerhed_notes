---
title: "Mobile Application Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Mobile_Application_Security_Cheat_Sheet.html"
created: "1741872882.0185266"
tags: [owasp, cheatsheet, security]
---
# Mobile Application Security

## Mobile Application Security Cheat Sheet[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[¶](#additional-security-considerations)](#widgetkit-security)](#deep-link-security)](#siri-permissions)](#shortcuts-permissions)](#ios-and-ipados)](#android)](#platform-specific-guidance)](#3-monitoring-and-analytics)](#2-updates)](#1-incident-response)](#post-deployment)](#3-usability-testing)](#2-automated-tests)](#1-penetration-testing)](#testing)](#application-integrity)](#3-update-libraries)](#2-code-reviews)](#1-static-analysis)](#code-quality)](#4-output-validation)](#3-input-validation)](#2-user-notifications)](#1-ui-data-masking)](#user-interface)](#3-certificate-pinning)](#2-use-secure-protocols)](#1-dont-trust-the-network)](#network-communication)](#5-personally-identifiable-information-pii)](#4-third-party-libraries)](#3-use-https)](#2-data-leakage)](#1-data-encryption)](#data-storage-privacy)](#7-sensitive-operations)](#6-token-storage)](#5-session-management)](#4-biometric-authentication)](#3-passwords-and-pin-policy)](#2-credential-handling)](#1-dont-trust-the-client)](#authentication-authorization)](#4-supply-chain)](#3-principle-of-least-privilege)](#2-secure-apis)](#1-secure-by-design)](#architecture-design)](#mobile-application-security-cheat-sheet)
Mobile application development presents certain security challenges that are
unique compared to web applications and other forms of software. This cheat
sheet provides guidance on security considerations for mobile app development.
It is not a comprehensive guide by any means, but rather a starting point for
developers to consider security in their mobile app development.
### Architecture & Design¶
#### 1. Secure by Design¶

- Opt for a secure design at the beginning of development, not as an
  afterthought.
- Keep in mind security principles like least privilege, defense in depth, and
  separation of concerns.
- Follow industry standards and best practices, such as:
- - National Institute of Standards and Technology ([[_content/dictionary#N|NIST]])
- - Internet Engineering Task Force ([[_content/dictionary#I|IETF]])

For more information, see the
[[Secure_Product_Design_Cheat_Sheet|Secure Product Design Cheat Sheet]].
#### 2. Secure APIs¶

- Ensure that your mobile app communicates securely with backend services.
- Use OAuth2, [[_content/dictionary#J|JWT]], or similar for secure authentication.
- Regularly update and rotate any used [[_content/dictionary#A|API]] keys or tokens.

#### 3. Principle of Least Privilege¶

- Request only the permissions your app needs.
- This applies not only to device permissions granted by the user, but also to
  permissions granted to the app by backend services.
- Avoid storing application files with overly permissive permissions.
- Secure by default: applications should have the most secure settings by default.

#### 4. Supply Chain¶
Developing with third-party libraries and components introduces the possibility
of security unknowns.

- Ensure app signing.
- Use only trusted and validated third-party libraries and components.
- Establish security controls for app updates, patches, and releases.
- Monitor and detect security incidents of used third-party products.

See the [[Vulnerable_Dependency_Management_Cheat_Sheet|Vulnerable Dependency Management Cheat Sheet]] for recommendations on managing third-party dependencies when vulnerabilities are discovered.
### Authentication & Authorization¶
Authentication is a complex topic and there are many pitfalls. Authentication
logic must be written and tested with extreme care. The tips here are only a
starting point and barely scratch the surface. For more information, see the
[[Authentication_Cheat_Sheet|Authentication Cheat Sheet]] and
[M1: Insecure Authentication/Authorization](https://owasp.org/www-project-mobile-top-10/2023-risks/m1-insecure-authentication-authorization.html)
from the [[_content/dictionary#O|OWASP]] Mobile Top 10.
#### 1. Don't Trust the Client¶

- Perform authentication/authorization server-side and only load data on
the device after successful authentication.
- If storing data locally, encrypt it using a key derived from the user’s
login credentials.
- Do not store user passwords on the device; use device-specific tokens
that can be revoked.
- Avoid using spoofable values like device identifiers for authentication.
- Assume all client-side controls can be bypassed and perform them
server-side as well.
- Include client side code to detect code/binary tampering.

#### 2. Credential Handling¶

- Do not hardcode credentials in the mobile app.
- Encrypt credentials in transmission.
- Do not store user credentials on the device. Consider using
secure, revocable access tokens.

#### 3. Passwords and [[_content/dictionary#P|PIN]] Policy¶

- Require password complexity.
- Do not allow short PINs such as 4 digits.
- Use platform specific secure storage mechanisms, such as
Keychain (iOS) or Keystore (Android).

#### 4. Biometric Authentication¶

- Use platform-supported methods for biometric authentication.
- Always provide a fallback, such as a [[_content/dictionary#P|PIN]].

#### 5. Session Management¶

- Sessions should timeout after inactivity.
- Offer a remote logout feature.
- Use randomly generated session tokens.
- Secure session data, both client and server side.

#### 6. Token Storage¶

- Store authentication tokens securely.
- Handle token expiration gracefully.

#### 7. Sensitive Operations¶

- Require users to re-authenticate for sensitive operations like changing
  passwords or updating payment information.
- Consider requiring re-authentication before displaying highly sensitive
  information as well.
- Require authorization checks on any backend functionality.

### Data Storage & Privacy¶
#### 1. Data Encryption¶

- Encrypt sensitive data both at rest and in transit.
- Store private data on the device's internal storage.
- Use platform APIs for encryption. Do not attempt to implement your own
  encryption algorithms.

#### 2. Data Leakage¶

- Beware of caching, logging, and background snapshots. Ensure that sensitive
  data is not leaked through these mechanisms.

See the [Logging Cheat Sheet](Logging_Cheat_Sheet.html#data-to-exclude) for
examples of data that should not be logged.
#### 3. Use [[_content/dictionary#H|HTTPS]]¶

- Always use [[_content/dictionary#H|HTTPS]] for network communications.

#### 4. Third-Party Libraries¶

- Ensure all third-party libraries are secure and up to date.

#### 5. Personally Identifiable Information ([[_content/dictionary#P|PII]])¶

- Minimise any [[_content/dictionary#P|PII]] to necessity.
- Attempt to replace [[_content/dictionary#P|PII]] with less critical information if possible.
- Reduce [[_content/dictionary#P|PII]], e.g. less frequent location updates.
- Implement automatic expiration and deletion of [[_content/dictionary#P|PII]] to minimize retention.
- Ask for user consent before collecting or using [[_content/dictionary#P|PII]].

### Network Communication¶
#### 1. Don't Trust the Network¶

- Assume that all network communication is insecure and can be intercepted.

#### 2. Use Secure Protocols¶

- Use [[_content/dictionary#H|HTTPS]] for all network communication.
- Do not override [[_content/dictionary#S|SSL]] certificate validation to allow self-signed or invalid
  certificates.
- Avoid mixed version [[_content/dictionary#S|SSL]] sessions.
- Encrypt data even if sent over [[_content/dictionary#S|SSL]], in case of future SSL vulnerabilities.
- Use strong, industry standard cipher suites, with appropriate key lengths.
- Use certificates signed by a trusted [[_content/dictionary#C|CA]] provider
- Avoid sending sensitive data via [[_content/dictionary#S|SMS]].

#### 3. Certificate Pinning¶

Consider certificate pinning. See the [[Pinning_Cheat_Sheet|Pinning Cheat Sheet]]
  for pros and cons of this approach.

### User Interface¶
#### 1. [[_content/dictionary#U|UI]] Data Masking¶

- Mask sensitive information on [[_content/dictionary#U|UI]] fields to prevent shoulder surfing.

#### 2. User Notifications¶

- Inform the user about security-related activities, such as logins from new
  devices.

#### 3. Input Validation¶

Validate and sanitize user input. See the
  [[Input_Validation_Cheat_Sheet|Input Validation Cheat Sheet]] for more
  information.

#### 4. Output Validation¶

- Validate and sanitize output to prevent injection and execution attacks.

### Code Quality¶
#### 1. Static Analysis¶

- Use static analysis tools to identify vulnerabilities.

#### 2. Code Reviews¶

- Make security a focal point during code reviews.

#### 3. Update Libraries¶

- Keep all your libraries up to date to patch known vulnerabilities.

### Application Integrity¶

- Disable debugging.
- Include code to validate integrity of application code.
- Obfuscate the app binary.

### Testing¶
#### 1. Penetration Testing¶

- Perform ethical hacking to identify vulnerabilities.
- Example tests:
- - Cryptographic vulnerability assessment.
- - Attempt to execute backend server functionality anonymously by removing any
  session tokens from [[_content/dictionary#P|POST]]/[[_content/dictionary#G|GET]] requests.

#### 2. Automated Tests¶

- Leverage automated tests to ensure that security features are working as
  expected and that access controls are enforced.

#### 3. Usability Testing¶

- Ensure that security features do not harm usability, which could cause users
  to bypass security features.

### Post-Deployment¶
#### 1. Incident Response¶

- Have a clear incident response plan in place.

#### 2. Updates¶

- Plan for regular updates and patches. In the case of mobile apps, this is
  especially important due to the delay between when a patch is released and
  when users actually receive the updated version due to app store review
  processes and the time it takes for users to update their apps.

- Use a mechanism to force users to update their app version when necessary.

#### 3. Monitoring and Analytics¶

- Use real-time monitoring to detect and respond to threats.

### Platform-Specific Guidance¶
#### Android¶

- Use Android’s [[_content/dictionary#P|ProGuard]] for code obfuscation.
Avoid storing sensitive data in [[_content/dictionary#S|SharedPreferences]]. See the
  [Android docs](https://developer.android.com/topic/security/data)
  on working with data securely for more details.
- Disable backup mode to prevent sensitive data being stored in backups.

#### iOS and iPadOS¶
##### Shortcuts Permissions¶

- iOS/iPadOS Shortcuts allow for automation of app functions, which may
enable sensitive actions even when the device is locked.

- There are several scenarios in which a user can execute a Shortcut
while the device is locked:

1. If a Shortcut is added as a widget to Today View, it can be accessed
and executed while the device is locked.
2. If a Shortcut is assigned to the Action Button (on iPhone 15 Pro and
iPhone 16 Pro models), it can be executed by pressing the Action Button
while the device is locked.
3. If a Shortcut is assigned to the Control Center (on iOS/iPadOS 18+),
it can be executed by pulling up the Control Center and pressing the
Shortcut button while the device is locked.
4. A Shortcut can be invoked via Siri while the device is locked.
5. If a Shortcut is added to the user's Home Screen (on iOS/iPadOS 18+),
it can be directly executed by tapping the Shortcut button on the user's
lock screen while the device is locked.
6. If a Shortcut is set to run at a specific interval or a specific time,
it can execute even if the device is locked.

- Sensitive app functionalities triggered via Shortcuts should always
require device unlock before execution.

- How: Store secure tokens in Keychain that the app validates before
executing sensitive shortcuts. Implement checks with
UIApplication.shared.isProtectedDataAvailable to restrict execution
of sensitive actions when the device is locked.

##### Siri Permissions¶

Siri can access app functionalities through voice or [Type to Siri](https://support.apple.com/guide/iphone/change-siri-accessibility-settings-iphaff1d606/ios.)
  commands, which is by default accessible even when the device is locked
  potentially enabling unauthorized actions.
How: Configure requiresUserAuthentication to true on intents that expose
sensitive information or functionality. Additionally, set
INIntent.userConfirmationRequired = true for operations requiring explicit
user confirmation. These settings ensure proper authentication
(e.g., Face ID or [[_content/dictionary#P|PIN]]) and explicit approval before Siri can
execute sensitive commands. (For more information, see Apple Developer's
[[[_content/dictionary#S|SiriKit]]](https://developer.apple.com/documentation/sirikit) documentation.)

##### Deep Link Security¶

- Deep links offer direct access to specific app screens, which could
potentially bypass authentication if not secured, allowing unauthorized
users access to secure sections of the app.
- An example of this on Microsoft Authenticator for iOS (which was
remediated in July 2024) allowed users to bypass App Lock by simply
navigating to msauth://microsoft.aad.brokerplugin/?, which would
open Authenticator and dismiss the Face ID/Touch ID/passcode prompt.
How: Implement authentication checks on any view controllers
or endpoints accessed via deep links. Configure and validate Universal
Links using apple-app-site-association files for secure deep linking.
Sanitize and validate all parameters received through deep links to
prevent injection attacks. Ensure unauthorized users are redirected
to the login screen, preventing direct access to sensitive parts of
the app without proper authentication. (See Apple Developer's
[Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)
documentation for more information.)

##### [[_content/dictionary#W|WidgetKit]] Security¶

- Widgets on the lock screen may display sensitive data, potentially
exposing it without the device being unlocked.
How: For iOS/iPadOS versions 17 and higher, use [[_content/dictionary#W|WidgetInfo]].isLocked
to detect lock screen state. For earlier iOS versions, implement custom
logic based on available widget states since widgetFamily alone doesn't
directly provide lock screen information. Apply conditional logic to mask
or restrict sensitive widget content when appropriate security conditions
aren't met. (See Apple's [[[_content/dictionary#W|WidgetKit]] security](https://support.apple.com/guide/security/widgetkit-security-secbb0a1f9b4/web)
for more information.)

##### Additional Security Considerations¶

- Configure appropriate background refresh policies to prevent sensitive data
updates while the device is locked.
- Implement proper privacy-related configurations in Info.plist for
features requiring user permissions.
- Use App Groups with appropriate security configurations when sharing data
between app and widgets.
- Use [[_content/dictionary#A|ATS]] (App Transport Security) to enforce strong security policies for
network communication.
- Do not store sensitive data in plist files.

For further reading, visit the
[[[_content/dictionary#O|OWASP]] Mobile Top 10 Project](https://owasp.org/www-project-mobile-top-10/).
For a more detailed framework for mobile security, see the
[OWASP Mobile Application Security Project](https://mas.owasp.org/).