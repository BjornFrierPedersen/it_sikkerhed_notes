# Social Engineering & Phishing Attacks

## Social Engineering

### What is Social Engineering?

Social engineering is a technique that uses psychological manipulation to deceive people into revealing sensitive information, performing actions, or transferring money. It is a type of attack that relies on human interaction and trust, rather than technical vulnerabilities.

Unlike technical attacks that exploit software or hardware vulnerabilities, social engineering exploits human psychology and behavior patterns. These attacks are particularly dangerous because they bypass technical security controls by targeting the human element.

### Types of Social Engineering

Social engineering attacks come in many forms, each with unique characteristics:

- **Piggybacking**: This attack occurs when an unauthorized person physically follows an authorized person into a restricted area, exploiting courtesy or politeness to gain access to secure locations.

- **Shoulder Surfing**: The attacker observes someone entering sensitive information such as [[_content/dictionary#P|PIN]] codes, passwords, or other credentials by looking over their shoulder or using visual recording devices.

- **Baiting**: Attackers leave malware-infected physical devices (like [[_content/dictionary#U|USB]] drives) in public places where potential victims might find and use them, or they create fake job offers or other enticing opportunities to collect personal information.

- **Dumpster Diving**: Searching through discarded materials (physical trash) to find sensitive information such as passwords written on notes, organizational charts, or other documents with valuable data.

- **Tailgating**: Similar to piggybacking, this involves following someone through a secure door or access point that would normally require authentication. It often involves some pretext or story to explain why the attacker doesn't have proper credentials.

## Phishing Attacks

### What is Phishing?

Phishing is a specific type of social engineering attack that uses fraudulent communications appearing to come from trustworthy sources. The goal is typically to steal sensitive data such as login credentials, credit card numbers, or to install malware on the victim's system.

The term "phishing" is a play on the word "fishing," as attackers are fishing for sensitive information by dangling a fake "lure" (the fraudulent message) hoping users will "bite" by providing the information or taking the requested action.

### Types of Phishing Attacks

Phishing has evolved into several specialized forms:

- **Email Phishing**: The most common form where attackers send emails impersonating legitimate organizations to trick recipients into revealing sensitive information. Organizations can test their security awareness using tools like [[[_content/dictionary#G|GoPhish]]](https://gophish.hack3r.party) to create simulated phishing campaigns.

- **Spear Phishing**: A more targeted form of phishing that uses personalized information about the victim to increase the likelihood of success. These attacks research specific individuals and customize communications to appear more legitimate.

- **Whaling**: A form of spear phishing that specifically targets high-level executives, C-suite members, or other high-value individuals within an organization. These attacks are typically highly sophisticated and well-researched.

- **Smishing**: Phishing conducted via [[_content/dictionary#S|SMS]] text messages rather than email. These messages often contain malicious links or request sensitive information.

- **Vishing**: Voice phishing conducted via telephone calls, where attackers impersonate legitimate entities like banks, government agencies, or technical support to extract sensitive information.

### Phishing Kits

A phishing kit is a collection of tools and resources used to launch a phishing attack. These kits typically include:

- Email templates designed to look like legitimate communications
- Landing pages that mimic legitimate websites
- Backend systems to collect and store stolen credentials
- Distribution systems to send out phishing messages

For security professionals, tools like [[[_content/dictionary#G|GoPhish]]](https://gophish.hack3r.party) can be used ethically to test an organization's resilience to phishing attacks by conducting simulated campaigns in a controlled environment.

## Prevention and Mitigation

### Social Engineering Defenses

1. **Security Awareness Training**: Regular training for all employees on recognizing and responding to social engineering attempts.

2. **Access Control Policies**: Strict physical and logical access controls with proper authentication procedures.

3. **Clean Desk Policy**: Ensuring sensitive information is not left visible on desks or screens.

4. **Data Classification**: Properly marking sensitive information so employees understand its importance.

### Phishing Defenses

1. **Email Filtering**: Implementing robust email security solutions to filter suspicious messages.

2. **Multi-factor Authentication ([[_content/dictionary#M|MFA]])**: Requiring additional verification beyond passwords.

3. **Security Awareness**: Training employees to recognize phishing attempts and providing clear reporting channels.

4. **Simulated Phishing Exercises**: Regular tests to evaluate employee awareness and response to phishing attempts.

5. **Browser Security**: Using browser extensions or security features that warn about suspicious websites.

## Real-World Impact

Social engineering and phishing attacks have been responsible for many high-profile breaches. Organizations should implement comprehensive security programs that address both technical controls and human factors to effectively combat these threats. 