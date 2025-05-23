---
title: "Forgot Password Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html"
created: "1741872881.882292"
tags: [owasp, cheatsheet, security]
---
# Forgot Password

## Forgot Password Cheat Sheet[[[[[[[[[[[[¶](#account-lockout)](#security-questions)](#offline-methods)](#pins)](#url-tokens)](#general-security-practices)](#methods)](#user-resets-password)](#forgot-password-request)](#forgot-password-service)](#introduction)](#forgot-password-cheat-sheet)
### Introduction¶
In order to implement a proper user management system, systems integrate a Forgot Password service that allows the user to request a password reset.
Even though this functionality looks straightforward and easy to implement, it is a common source of vulnerabilities, such as the renowned [user enumeration attack](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account.html).
The following short guidelines can be used as a quick reference to protect the forgot password service:

- - Return a consistent message for both existent and non-existent accounts.
- Ensure that the time taken for the user response message is uniform.
- Use a side-channel to communicate the method to reset their password.
Use [[[[_content/dictionary#U|URL]] tokens](#url-tokens)](#url-tokens) for the simplest and fastest implementation.
- Ensure that generated tokens or codes are:
- - Randomly generated using a cryptographically safe algorithm.
- - Sufficiently long to protect against brute-force attacks.
- - Stored securely.
- - Single use and expire after an appropriate period.

- Do not make a change to the account until a valid token is presented, such as locking out the account

This cheat sheet is focused on resetting users passwords. For guidance on resetting multifactor authentication ([[_content/dictionary#M|MFA]]), see the relevant section in the [[Authentication_Cheat_Sheet|Multifactor [Authentication Cheat Sheet]]](Multifactor_Authentication_Cheat_Sheet.html#resetting-mfa).
### Forgot Password Service¶
The password reset process can be broken into two main steps, detailed in the following sections.
#### Forgot Password Request¶
When a user uses the forgot password service and inputs their username or email, the below should be followed to implement a secure process:

Return a consistent message for both existent and non-existent accounts.
- Ensure that responses return in a consistent amount of time to prevent an attacker enumerating which accounts exist. This could be achieved by using asynchronous calls or by making sure that the same logic is followed, instead of using a quick exit method.
- Implement protections against excessive automated submissions such as rate-limiting on a per-account basis, requiring a [[_content/dictionary#C|CAPTCHA]], or other controls. Otherwise an attacker could make thousands of password reset requests per hour for a given account, flooding the user's intake system (e.g., email inbox or [[_content/dictionary#S|SMS]]) with useless requests.
Employ normal security measures, such as [[SQL_Injection_Prevention_Cheat_Sheet|[[_content/dictionary#S|SQL]] Injection Prevention methods]] and [[Input_Validation_Cheat_Sheet|Input Validation]].

#### User Resets Password¶
Once the user has proved their identity by providing the token (sent via an email) or code (sent via [[_content/dictionary#S|SMS]] or other mechanisms), they should reset their password to a new secure one. In order to secure this step, the measures that should be taken are:

- The user should confirm the password they set by writing it twice.
- Ensure that a secure password policy is in place, and is consistent with the rest of the application.
Update and store the password following [[Password_Storage_Cheat_Sheet|secure practices]].
- Send the user an email informing them that their password has been reset (do not send the password in the email!).
- Once they have set their new password, the user should then login through the usual mechanism. Don't automatically log the user in, as this introduces additional complexity to the authentication and session handling code, and increases the likelihood of introducing vulnerabilities.
- Ask the user if they want to invalidate all of their existing sessions, or invalidate the sessions automatically.

### Methods¶
In order to allow a user to request a password reset, you will need to have some way to identify the user, or a means to reach out to them through a side-channel.
This can be done through any of the following methods:

- [[_content/dictionary#U|URL]] tokens.
[[- PINs](#pins)](#pins)
[- Offline methods](#offline-methods)
[Security questions](#security-questions).

These methods can be used together to provide a greater degree of assurance that the user is who they claim to be. No matter what, you must ensure that a user always has a way to recover their account, even if that involves contacting the support team and proving their identity to staff.
#### General Security Practices¶
It is essential to employ good security practices for the reset identifiers (tokens, codes, PINs, etc.). Some points don't apply to the [offline methods](#offline-methods), such as the lifetime restriction. All tokens and codes should be:

Generated [cryptographically secure random number generator](Cryptographic_Storage_Cheat_Sheet.html#secure-random-number-generation).
It is also possible to use [[_content/dictionary#J|JSON]] Web Tokens (JWTs) in place of random tokens, although this can introduce additional vulnerability, such as those discussed in the [[JSON_Web_Token_for_Java_Cheat_Sheet|JSON Web Token Cheat Sheet]].

- Long enough to protect against brute-force attacks.
- Linked to an individual user in the database.
- Invalidated after they have been used.
Stored in a secure manner, as discussed in the [[Password_Storage_Cheat_Sheet|Password Storage Cheat Sheet]].

#### [[_content/dictionary#U|URL]] Tokens¶
URL tokens are passed in the query string of the URL, and are typically sent to the user via email. The basic overview of the process is as follows:

1. Generate a token to the user and attach it in the [[_content/dictionary#U|URL]] query string.
Send this token to the user via email.
   - Don't rely on the [Host](https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Headers/Host) header while creating the reset URLs to avoid [Host Header Injection](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection) attacks. The URL should be either be hard-coded, or should be validated against a list of trusted domains.
   - Ensure that the URL is using [[_content/dictionary#H|HTTPS]].
The user receives the email, and browses to the URL with the attached token.
   - Ensure that the reset password page adds the [Referrer Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) tag with the noreferrer value in order to avoid [referrer leakage](https://portswigger.net/kb/issues/00500400_cross-domain-referer-leakage).
   - Implement appropriate protection to prevent users from brute-forcing tokens in the URL, such as rate limiting.
If required, perform any additional validation steps such as requiring the user to answer [security questions](#security-questions).
5. 5. Let the user create a new password and confirm it. Ensure that the same password policy used elsewhere in the application is applied.

Note: [[_content/dictionary#U|URL]] tokens can follow on the same behavior of the PINs by creating a restricted session from the token. Decision should be made based on the needs and the expertise of the developer.
#### PINs¶
PINs are numbers (between 6 and 12 digits) that are sent to the user through a side-channel such as [[_content/dictionary#S|SMS]].

1. Generate a [[_content/dictionary#P|PIN]].
2. Send it to the user via [[_content/dictionary#S|SMS]] or another mechanism.
   - Breaking the PIN up with spaces makes it easier for the user to read and enter.
3. The user then enters the PIN along with their username on the password reset page.
4. Create a limited session from that PIN that only permits the user to reset their password.
Let the user create a new password and confirm it. Ensure that the same password policy used elsewhere in the application is applied.

#### Offline Methods¶
Offline methods differ from other methods by allowing the user to reset their password without requesting a special identifier (such as a token or [[_content/dictionary#P|PIN]]) from the backend. However, authentication still needs to be conducted by the backend to ensure that the request is legitimate. Offline methods provide a certain identifier either on registration, or when the user wishes to configure it.
These identifiers should be stored offline and in a secure fashion (e.g. password managers), and the backend should properly follow the [general security practices](#general-security-practices). Some implementations are built on [hardware [[_content/dictionary#O|OTP]] tokens](Multifactor_Authentication_Cheat_Sheet.html#hardware-otp-tokens), [certificates](Multifactor_Authentication_Cheat_Sheet.html#certificates), or any other implementation that could be used inside of an enterprise. These are out of scope for this cheat sheet.
If account has [[_content/dictionary#M|MFA]] enabled, and you are looking for MFA recovery, different methods can be found in the corresponding [Multifactor Authentication cheat sheet](Multifactor_Authentication_Cheat_Sheet.html#resetting-mfa).
#### Security Questions¶
Security questions should not be used as the sole mechanism for resetting passwords due to their answers frequently being easily guessable or obtainable by attackers. However, they can provide an additional layer of security when combined with the other methods discussed in this cheat sheet. If they are used, then ensure that secure questions are chosen as discussed in the [[Choosing_and_Using_Security_Questions_Cheat_Sheet|Security Questions cheat sheet]].
### Account Lockout¶
Accounts should not be locked out in response to a forgotten password attack, as this can be used to deny access to users with known usernames. For more details on account lockouts, see the Authentication Cheat Sheet.