## Sources
- [MITRE ATT&CK Resources](https://attack.mitre.org/resources/)
- [LinkedIn Learning: Introduction to the MITRE ATT&CK Framework](https://www.linkedin.com/learning/introduction-to-the-mitre-att-ck-framework/course-introduction?u=57077785)

# ATT&CK Framework

ATT&CK is a knowledge base of adversarial techniques based on real-world observations. ATT&CK focuses on how adversaries interact with systems during an operation, reflecting the various phases of an adversary's attack lifecycle and the platforms they are known to target.

## Key Concepts

ATT&CK is a model that attempts to systematically categorize adversary behavior. The main components of the model are:

- **Tactics:** Represents "why" or the reason an adversary is performing an action.
- **Techniques:** Represents "how" adversaries achieve tactical goals by performing an action.
- **Sub-techniques:** A more specific or lower-level description of adversarial behavior.
- **Procedures:** Specific implementation or in-the-wild use the adversary uses for techniques or sub-techniques.

ATT&CK is organized in a series of technology domains, the ecosystem an adversary operates within. Currently, there are three technology domains:

- **Enterprise:** Representing traditional enterprise networks and cloud technologies.
- **Mobile:** For mobile communication devices.
- **ICS:** For industrial control systems.

Within each domain are platforms, which may be an operating system or application (e.g., Microsoft Windows). Techniques and sub-techniques can apply to multiple platforms.

For more information on the principles behind ATT&CK, its creation, and its ongoing maintenance, read the *ATT&CK Philosophy Paper*. For additional information focused on ATT&CK for ICS, including the unique elements and commonalities with ATT&CK, read the *ATT&CK for ICS*.

## Understanding ATT&CK

- The ATT&CK framework started as a mind map for hackers gathering different attacks and defenses for and against software applications. MITRE is an organization that started collecting these attacks in an effort to give developers and organizations tools to help protect against cybersecurity threats.

### ATT&CK Acronym

- **A**: Adversarial (*The hackers, attackers, or adversaries*)
- **T**: Tactics (*The tactics or rules of the hacker to attack*)
- **T**: Techniques (*The techniques and methods with which the attacker targets the vulnerable software*)
- **&**: And
- **CK**: Common Knowledge

## ATT&CK Pillars Overview

| Category   | Enterprise | Mobile | ICS |
|------------|------------|--------|-----|
| Tactics    | 14         | 14     | 12  |
| Techniques | 196        | 66     | 81  |

ATT&CK collects data from many different data sources around the world. It also collects data and notes from various groups around the world, such as hacker groups, cybersecurity groups, etc. Additionally, it keeps a collection of software sets which function as tools for cybersecurity professionals and hackers. Their website is kept updated as an open-source repository and contains a treasure trove of information. See more on the [[Notes/_Important Links]] page.

## The 14 Phases (Tactics) of ATT&CK

### 1. Reconnaissance (TA0043)
*Goal: Gathering information to plan future adversary operations.*

- Consists of techniques involving active and/or passive information gathering used to select targets and understand their environment.
- **Examples:** Scanning target networks for vulnerabilities (*e.g., IP filtering, vulnerability scans*), gathering victim identity information (*e.g., employee names, email addresses from social media or data breaches*), searching open sources (*e.g., WHOIS, search engines, technical databases*) for information about infrastructure, software, and configurations.
- The goal is to understand the target, their technology stack, potential weaknesses (*gaping holes*), and identify entry points.

### 2. Resource Development (TA0042)
*Goal: Establishing resources adversaries can use to support operations.*

- Consists of techniques for acquiring or creating resources needed for an attack.
- **Examples:** Setting up command and control (C2) infrastructure (*servers, domains*), acquiring compromised credentials (*e.g., purchasing from the dark web*), setting up bots for DDoS, developing or acquiring malware/exploits, compromising third-party websites to use as watering holes, establishing fake online personas or websites.
- Attackers try to *build, borrow, buy, lease, or compromise* resources for their campaign.

### 3. Initial Access (TA0001)
*Goal: Trying to get into your network.*

- A collection of techniques attackers use to gain an initial foothold within the target environment.
- **Examples:** Spear phishing campaigns (*malicious links or attachments*), exploitation of public-facing vulnerabilities (*e.g., web servers, attacking VPNs*), using valid but compromised accounts, drive-by compromise, exploiting trusted relationships.

### 4. Execution (TA0002)
*Goal: Trying to run malicious code.*

- Includes techniques used by attackers to execute their code on a local or remote system.
- **Examples:** Running malicious scripts via command-line interpreters (*e.g., PowerShell, Bash, Python*), executing payloads through cloud administration tools, exploiting software vulnerabilities for code execution, using native APIs, scheduling tasks to run malicious code.
- Scripts can be used to *deep dive* into the infrastructure, cause damage, or extract information.

### 5. Persistence (TA0003)
*Goal: Trying to maintain their foothold.*

- Tactics that allow attackers to maintain continuous access to a system, making their presence *impervious to reboots, password rotation, session termination*, etc.
- **Examples:** Creating new accounts (*local or domain*), manipulating existing accounts (*e.g., adding SSH keys, modifying permissions*), modifying boot processes or system services (*e.g., Windows Services, Linux systemd, LaunchDaemons*), scheduling tasks, installing browser extensions, creating registry run keys, planting rootkits or web shells.

### 6. Privilege Escalation (TA0004)
*Goal: Trying to gain higher-level permissions.*

- Techniques allowing an attacker to gain higher privileges (*e.g., administrator or root access*) than initially obtained.
- Often necessary to achieve the *higher end goal* like accessing sensitive data or moving laterally.
- **Examples:** Exploiting vulnerabilities in the OS or applications (*running exploit code*), utilizing misconfigured system settings, finding and using existing *privileged accounts (admin)*, bypassing User Account Control (UAC), abusing Sudo rights.

### 7. Defense Evasion (TA0005)
*Goal: Trying to avoid being detected.*

- A collection of techniques attackers use to avoid detection by security tools (like antivirus, EDR) and analysts.
- Enables attackers to *keep control of a system undetected for a longer period*, extending their potential gain.
- **Examples:** Obfuscating or encrypting malware/scripts, disabling security software or logging, clearing command history or event logs, using legitimate tools for malicious purposes (LOLBins/LOLBAS), modifying the registry, hiding files, processes or network connections, masquerading as legitimate processes, using rootkits.

### 8. Credential Access (TA0006)
*Goal: Trying to steal account names and passwords.*

- Techniques used by attackers to steal credentials like account names, passwords, tokens, hashes, or keys.
- **Examples:** Brute-forcing passwords (*password spraying, guessing*), keylogging, dumping credentials from memory (*e.g., LSASS*), network sniffing, phishing for credentials, stealing web browser cookies or stored passwords, exploiting Kerberos (*Kerberoasting, AS-REP Roasting*), reading unsecured credentials stored in files or registry, Man-in-the-Middle (MitM) attacks.

### 9. Discovery (TA0007)
*Goal: Trying to figure out your environment.*

- Techniques allowing attackers to explore the compromised network and systems to understand the environment, identify valuable assets (*"crown jewels"*), and plan their next steps.
- **Examples:** Discovering system information, network configuration, running processes, logged-in users, *privileged accounts*, network shares, connected devices, cloud services, domain trusts, software inventory, security software presence.

### 10. Lateral Movement (TA0008)
*Goal: Trying to move through your environment.*

- A collection of techniques allowing attackers to *move from one system to another* within the target network after gaining initial access.
- Often relies on stolen credentials and exploits remote services.
- **Examples:** Using remote desktop protocols (RDP), exploiting remote services (*SMB, WinRM, SSH, DCOM*), transferring malicious tools to other systems, using valid accounts (Pass the Hash, Pass the Ticket) to access other machines, exploiting trust relationships.

### 11. Collection (TA0009)
*Goal: Gathering data of interest to the adversary's goal.*

- Techniques used to *accrue data from the target system* and other network locations relevant to the attacker's objectives before exfiltration.
- **Examples:** Copying data from databases, capturing screenshots or keystrokes, collecting files from local systems or network shares, accessing email archives, scraping web portals, accessing cloud storage objects.

### 12. Command and Control (C2 / TA0011)
*Goal: Communicating with compromised systems to control them.*

- Techniques allowing attackers to *communicate with compromised systems* within the target network to issue commands and receive output.
- Often involves establishing covert channels back to attacker-controlled infrastructure.
- **Examples:** Using common protocols like HTTP/HTTPS, DNS, or ICMP for C2 traffic; utilizing legitimate web services (*e.g., social media, cloud storage, paste sites*) as C2 channels; employing encryption or obfuscation to hide C2 communications; using techniques like Domain Fronting or Dynamic DNS.

### 13. Exfiltration (TA0010)
*Goal: Trying to steal data.*

- Consists of techniques used by attackers to *steal collected data* by transferring it out of the target network to an external, attacker-controlled location.
- **Examples:** Transferring data over the C2 channel, uploading data to cloud storage or FTP servers, using alternative protocols (*e.g., DNS tunneling*), compressing and encrypting data before transfer, transferring data via physical media like USB drives.

### 14. Impact (TA0040)
*Goal: Trying to manipulate, interrupt, or destroy your systems and data.*

- A collection of techniques used by attackers to *disrupt business activities*, manipulate data integrity, destroy systems, or otherwise deny service/availability.
- **Examples:** Encrypting data for ransom (*ransomware*), wiping disks or firmware, corrupting data, shutting down or restarting systems, defacing websites, executing denial-of-service (DoS) attacks, resource hijacking (*cryptomining*), manipulating industrial control system processes. 
