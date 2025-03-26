## Source: 
- https://www.khanacademy.org/computing/ap-computer-science-principles/the-internet/x2d2f703b37b450a3:web-protocols/a/domain-name-system-dns-protocol
- https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:web-protocols/a/the-world-wide-web
- https://developer.mozilla.org/en-[[_content/dictionary#U|US]]/docs/Web/[[_content/dictionary#H|HTTP]]/Guides/Overview

## <span style="color:rgb(57, 224, 140);">The World Wide Web</span>
### Powered by protocols
- A web browser loads a webpage using various protocols:
- It uses the Domain Name System ([[_content/dictionary#D|DNS]]) protocol to convert a domain name into an [[_content/dictionary#I|IP]] address.
- It uses the [[_content/dictionary#H|HyperText]] Transfer Protocol ([[_content/dictionary#H|HTTP]]) to request the webpage contents from that [[_content/dictionary#I|IP]] address.
- It may also use the Transport Layer Security ([[_content/dictionary#T|TLS]]) protocol to serve the website over a secure, encrypted connection.
- The web browser uses these protocols on top of the Internet protocols, so every [[_content/dictionary#H|HTTP]] request also uses [[_content/dictionary#T|TCP]] and [[_content/dictionary#I|IP]].
- The Web is just one of the applications built on top of the Internet protocols, but it is by far the most popular.

## <span style="color:rgb(57, 224, 140);">[[_content/dictionary#D|DNS]] - Domain Name System</span>
### Overview
- [[_content/dictionary#D|DNS]] translates human-friendly domain names (like www.wikipedia.org) into [[_content/dictionary#I|IP]] addresses (like 74.125.20.113).
- It simplifies navigation on the Internet by allowing users to use memorable domain names instead of numeric [[_content/dictionary#I|IP]] addresses.

### Anatomy of a Domain Name
- A domain name consists of three parts: third-level domain, second-level domain, and top-level domain ([[_content/dictionary#T|TLD]]).
- Example: In "www.wikipedia.org", "www" is the third-level domain, "wikipedia" is the second-level domain, and "org" is the [[_content/dictionary#T|TLD]].

### [[_content/dictionary#D|DNS]] Lookup Process
- Local Cache: Checks if the domain name is stored locally.
- [[_content/dictionary#I|ISP]] Cache: Queries the Internet Service Provider's cache.
- Name Servers: Involves root name servers, [[_content/dictionary#T|TLD]] name servers, and host name servers to find the [[_content/dictionary#I|IP]] address.

### Efficiency and Redundancy
- [[_content/dictionary#D|DNS]] uses caching and a hierarchical structure to efficiently resolve domain names.
- The system has scaled well since 1985, handling the growth of the Internet through redundancy and caching.

### [[_content/dictionary#D|DNS]] Record Types
- A records: Maps a domain name to an [[_content/dictionary#I|IP]] address.
- [[_content/dictionary#M|MX]] records: Specifies the mail server for a domain.

## <span style="color:rgb(57, 224, 140);">[[_content/dictionary#H|HTTP]] - [[_content/dictionary#H|HyperText]] Transfer Protocol</span>
### Overview
- [[_content/dictionary#H|HTTP]] is a protocol for fetching resources such as [[_content/dictionary#H|HTML]] documents.
- It is the foundation of any data exchange on the Web and is a client-server protocol.

### Components of [[_content/dictionary#H|HTTP]]-based Systems
- Client (User-Agent): Typically a web browser that initiates requests.
- Server: Responds to requests, serving documents or resources.
- Proxies: Intermediate entities that can cache, filter, or load balance requests.

### Basic Aspects of [[_content/dictionary#H|HTTP]]
- Human-Readable: [[_content/dictionary#H|HTTP]] messages are designed to be readable by humans.
- Extensible: [[_content/dictionary#H|HTTP]] headers allow for easy extension and experimentation.
- Stateless: Each request is independent, but sessions can be managed using cookies.

### [[_content/dictionary#H|HTTP]] Flow
- Open a [[_content/dictionary#T|TCP]] Connection: Establish a connection to send requests and receive responses.
- Send an [[_content/dictionary#H|HTTP]] Message: Includes methods like [[_content/dictionary#G|GET]] or [[_content/dictionary#P|POST]].
- Read the Response: Server sends back a response with status codes and content.
- Close or Reuse the Connection: Depending on the need for further requests.

### APIs Based on [[_content/dictionary#H|HTTP]]
- Fetch [[_content/dictionary#A|API]]: Used to make [[_content/dictionary#H|HTTP]] requests from [[_content/dictionary#J|JavaScript]].
- Server-Sent Events: Allows servers to send events to clients using [[_content/dictionary#H|HTTP]].

### History
- Developed by Tim Berners-Lee at [[_content/dictionary#C|CERN]] in 1989.
- The first version, [[_content/dictionary#H|HTTP]]/0.9, was introduced in 1991.
- [[_content/dictionary#H|HTTP]]/1.0 was finalized in 1996, followed by HTTP/1.1 in 1997.
- [[_content/dictionary#H|HTTP]]/2 was published in 2015, and HTTP/3 in 2022.

### Technical Overview
- [[_content/dictionary#H|HTTP]] functions as a request-response protocol in the client-server model.
- It uses methods like [[_content/dictionary#G|GET]], [[_content/dictionary#P|POST]], [[_content/dictionary#P|PUT]], [[_content/dictionary#D|DELETE]], etc., to perform actions on resources.
- [[_content/dictionary#H|HTTP]]/1.1 introduced persistent connections and pipelining.
- [[_content/dictionary#H|HTTP]]/2 and HTTP/3 improve performance with features like multiplexing and using [[_content/dictionary#Q|QUIC]] over [[_content/dictionary#U|UDP]].

### Security
- [[_content/dictionary#H|HTTPS]] is the secure version of [[_content/dictionary#H|HTTP]], using [[_content/dictionary#T|TLS]] for encryption.
- Other methods for establishing encrypted connections include Secure Hypertext Transfer Protocol and using the [[_content/dictionary#H|HTTP]]/1.1 Upgrade header.

### Similar Protocols
- [[_content/dictionary#S|SPDY]]: An alternative to [[_content/dictionary#H|HTTP]] developed by Google, which influenced HTTP/2.
- Gopher: A content delivery protocol displaced by [[_content/dictionary#H|HTTP]] in the early 1990s.
