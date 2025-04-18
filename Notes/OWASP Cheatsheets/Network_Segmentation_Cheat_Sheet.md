---
title: "Network Segmentation Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Network_Segmentation_Cheat_Sheet.html"
created: "1741872882.0311482"
tags: [owasp, cheatsheet, security]
---
# Network Segmentation

## Network segmentation Cheat Sheet[[[[[[[[[[[[[[[[[¶](#useful-[link](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet)s)](#permissions-for-monitoring-systems)](#secure-logging)](#permissions-for-cicd)](#examples-of-individual-policy-provisions)](#network-security-policy)](#many-applications-on-the-same-network)](#interservice-interaction)](#example-of-three-layer-network-architecture)](#backend)](#middleware)](#frontend)](#three-layer-network-architecture)](#schematic-symbols)](#content)](#introduction)](#network-segmentation-cheat-sheet)
### Introduction¶
Network segmentation is the core of multi-layer defense in depth for modern services. Segmentation slow down an attacker if he cannot implement attacks such as:

[[_content/dictionary#S|SQL]]-injections, see [SQL Injection Prevention Cheat Sheet](https://github.com/[[_content/dictionary#O|OWASP]]/[[_content/dictionary#C|CheatSheetSeries]]/blob/master/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md);
- compromise of workstations of employees with elevated privileges;
- compromise of another server in the perimeter of the organization;
- compromise of the target service through the compromise of the [[_content/dictionary#L|LDAP]] directory, [[_content/dictionary#D|DNS]] server, and other corporate services and sites published on the Internet.

The main goal of this cheat sheet is to show the basics of network segmentation to effectively counter attacks by building a secure and maximally isolated service network architecture.
Segmentation will avoid the following situations:

- executing arbitrary commands on a public web server (NginX, Apache, Internet Information Service) prevents an attacker from gaining direct access to the database;
- having unauthorized access to the database server, an attacker cannot access CnC on the Internet.

### Content¶

- Schematic symbols;
- Three-layer network architecture;
- Interservice interaction;
- Network security policy;
- Useful links.

### Schematic symbols¶
Elements used in network diagrams:

Crossing the border of the rectangle means crossing the firewall:

In the image above, traffic passes through two firewalls with the names FW1 and FW2

In the image above, traffic passes through one firewall, behind which there are two VLANs
Further, the schemes do not contain firewall icons so as not to overload the schemes
### Three-layer network architecture¶
By default, developed information systems should consist of at least three components (security zones):

[[[_content/dictionary#F|FRONTEND]]](https://github.com/[[_content/dictionary#O|OWASP]]/[[_content/dictionary#C|CheatSheetSeries]]/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#FRONTEND);
[[[_content/dictionary#M|MIDDLEWARE]]](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#MIDDLEWARE);
[[[_content/dictionary#B|BACKEND]]](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Network_Segmentation_Cheat_Sheet.md#BACKEND).

#### [[_content/dictionary#F|FRONTEND]]¶
FRONTEND - A frontend is a set of segments with the following network elements:

- balancer;
- application layer firewall;
- web server;
- web cache.

#### [[_content/dictionary#M|MIDDLEWARE]]¶
MIDDLEWARE - a set of segments to accommodate the following network elements:

- web applications that implement the logic of the information system (processing requests from clients, other services of the company and external services; execution of requests);
- authorization services;
- analytics services;
- message queues;
- stream processing platform.

#### [[_content/dictionary#B|BACKEND]]¶
BACKEND - a set of network segments to accommodate the following network elements:

- [[_content/dictionary#S|SQL]] database;
- [[_content/dictionary#L|LDAP]] directory (Domain controller);
- storage of cryptographic keys;
- file server.

#### Example of Three-layer network architecture¶

The following example shows an organization's local network. The organization is called "Сontoso".
The edge firewall contains 2 VLANs of [[_content/dictionary#F|FRONTEND]] security zone:

- [[_content/dictionary#D|DMZ]] Inbound - a segment for hosting services and applications accessible from the Internet, they must be protected by [[_content/dictionary#W|WAF]];
- [[_content/dictionary#D|DMZ]] Outgoing - a segment for hosting services that are inaccessible from the Internet, but have access to external networks (the firewall does not contain any rules for allowing traffic from external networks).

The internal firewall contains 4 VLANs:

- [[_content/dictionary#M|MIDDLEWARE]] security zone contains only one [[_content/dictionary#V|VLAN]] with name [[_content/dictionary#A|APPLICATIONS]] - a segment designed to host information system applications that interact with each other (interservice communication) and interact with other services;
- [[_content/dictionary#B|BACKEND]] security zone contains:
- - [[_content/dictionary#D|DATABASES]] - a segment designed to delimit various databases of an automated system;
- - [[_content/dictionary#A|AD]] [[_content/dictionary#S|SERVICES]] - segment designed to host various Active Directory services, in the example only one server with a domain controller Contoso.com is shown;
- - [[_content/dictionary#L|LOGS]] - segment, designed to host servers with logs, servers centrally store application logs of an automated system.

### Interservice interaction¶
Usually some information systems of the company interact with each other. It is important to define a firewall policy for such interactions.
The base allowed interactions are indicated by the green arrows in the image below:

The image above also shows the allowed access from the [[_content/dictionary#F|FRONTEND]] and [[_content/dictionary#M|MIDDLEWARE]] segments to external networks (the Internet, for example).
From this image follows:

1. Access between [[_content/dictionary#F|FRONTEND]] and [[_content/dictionary#M|MIDDLEWARE]] segments of different information systems is prohibited;
2. Access from the MIDDLEWARE segment to the [[_content/dictionary#B|BACKEND]] segment of another service is prohibited (access to a foreign database bypassing the application server is prohibited).

Forbidden accesses are indicated by red arrows in the image below:

#### Many applications on the same network¶
If you prefer to have fewer networks in your organization and host more applications on each network, it is acceptable to host the load balancer on those networks. This balancer will balance traffic to applications on the network.
In this case, it will be necessary to open one port to such a network, and balancing will be performed, for example, based on the [[_content/dictionary#H|HTTP]] request parameters.
An example of such segmentation:

As you can see, there is only one incoming access to each network, access is opened up to the balancer in the network. However, in this case, segmentation no longer works, access control between applications from different network segments is performed at the 7th level of the [[_content/dictionary#O|OSI]] model using a balancer.
### Network security policy¶
The organization must define a "paper" policy that describes firewall rules and basic allowed network access.
This policy is at least useful:

- network administrators;
- security representatives;
- [[_content/dictionary#I|IT]] auditors;
- architects of information systems and software;
- developers;
- [[_content/dictionary#I|IT]] administrators.

It is convenient when the policy is described by similar images. The information is presented as concisely and simply as possible.
#### Examples of individual policy provisions¶
Examples in the network policy will help colleagues quickly understand what access is potentially allowed and can be requested.
##### Permissions for [[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]¶
The network security policy may define, for example, the basic permissions allowed for the software development system. Let's look at an example of what such a policy might look like:

##### Secure logging¶
It is important that in the event of a compromise of any information system, its logs are not subsequently modified by an attacker. To do this, you can do the following: copy the logs to a separate server, for example, using the syslog protocol, which does not allow an attacker to modify the logs, syslog only allows you to add new events to the logs.
The network security policy for this activity looks like this:

In this example, we are also talking about application logs that may contain security events, as well as potentially important events that may indicate an attack.
##### Permissions for monitoring systems¶
Suppose a company uses Zabbix as an [[_content/dictionary#I|IT]] monitoring system. In this case, the policy might look like this:

### Useful links¶

Full network segmentation cheat sheet by [sergiomarotco](https://github.com/sergiomarotco): link.