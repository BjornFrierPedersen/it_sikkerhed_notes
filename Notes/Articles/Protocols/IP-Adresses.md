## <span style="color:rgb(57, 224, 140);">Source:</span> https://en.wikipedia.org/wiki/IP_address

## <span style="color:rgb(57, 224, 140);">Overview</span>
- [[_content/dictionary#I|IP]] (Internet Protocol) addresses are unique identifiers for devices connected to the Internet.
- They are essential for addressing and routing messages between devices.

## <span style="color:rgb(57, 224, 140);">IPv4 Addresses</span>
### Overview
- IPv4 is the first version of the Internet Protocol ([[_content/dictionary#I|IP]]) and a core protocol for internetworking.
- It was deployed for production on [[_content/dictionary#S|SATNET]] in 1982 and on the [[_content/dictionary#A|ARPANET]] in January 1983.
- Despite the introduction of IPv6, IPv4 is still widely used to route most Internet traffic.

### Addressing
- IPv4 uses a 32-bit address space, providing 4,294,967,296 unique addresses.
- Addresses are written in dot-decimal notation (e.g., 192.168.0.1).
- Special address blocks are reserved for private networks and multicast addresses.

### Special-Use Addresses
- Private Networks: Addresses reserved for local communications within private networks (e.g., 10.0.0.0/8).
- Link-Local Addresses: Used for communication between devices on the same local network segment (e.g., 169.254.0.0/16).
- Loopback Addresses: Used for testing and communication within the same device (e.g., 127.0.0.1).

### Address Space Exhaustion
- The rapid growth of Internet users and devices led to the depletion of available IPv4 addresses.
- IPv6 was introduced to address this issue, offering a vastly larger address space.
- Transition technologies are used to allow interoperability between IPv4 and IPv6.

### Packet Structure
- An IPv4 packet consists of a header and a data section.
- The header includes fields such as source and destination addresses, [[_content/dictionary#T|TTL]] (Time to Live), and protocol.

## <span style="color:rgb(57, 224, 140);">IPv6 Addresses</span>
### Overview
- IPv6 is the latest version of the Internet Protocol, designed to replace IPv4 due to address exhaustion.
- It uses 128-bit addresses, allowing for a vastly larger address space compared to IPv4's 32-bit addresses.

### Main Features
- Hierarchical Address Allocation: Facilitates route aggregation and limits the expansion of routing tables.
- Multicast Addressing: Expanded and simplified compared to IPv4.
- Stateless Address Autoconfiguration ([[_content/dictionary#S|SLAAC]]): Allows devices to configure themselves automatically.
- Simplified Packet Processing: IPv6 headers are simpler, reducing the processing load on routers.

### Addressing
- Unicast, Anycast, and Multicast: Three types of transmission supported.
- Link-Local Addresses: Automatically configured for local network communication.
- Global Addresses: Assigned by routers for global communication.

### Transition Mechanisms
- Dual-Stack Implementation: Supports both IPv4 and IPv6 simultaneously.
- Tunneling: Encapsulates IPv6 traffic within IPv4 networks to ensure compatibility.

### Security
- [[_content/dictionary#I|IPsec]]: Originally mandatory for IPv6, now recommended, providing secure communication.
- Shadow Networks: Potential security risks due to IPv6-enabled devices bypassing IPv4 security measures.

### Deployment
- Gradual Adoption: IPv6 is being deployed alongside IPv4, with mechanisms to ensure interoperability.
- Global Reach: IPv6 support exists in every country, with varying levels of deployment.

## <span style="color:rgb(57, 224, 140);">Dynamic and Static [[_content/dictionary#I|IP]] Addresses</span>
- Dynamic [[_content/dictionary#I|IP]] addresses change periodically and are assigned by ISPs.
- Static [[_content/dictionary#I|IP]] addresses remain constant and are often used by servers.

## <span style="color:rgb(57, 224, 140);">Finding Your [[_content/dictionary#I|IP]] Address</span>
- You can find your [[_content/dictionary#I|IP]] address by searching "IP address" on Google.
- Your [[_content/dictionary#I|IP]] address may change if you switch networks or reconnect to the Internet.
