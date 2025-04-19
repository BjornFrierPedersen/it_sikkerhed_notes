## Source: 
- https://en.wikipedia.org/wiki/Transmission_Control_Protocol
- https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/transmission-control-protocol--tcp

## <span style="color:rgb(57, 224, 140);">Definition</span>
- Digital signatures are cryptographic schemes used to verify the authenticity of digital messages or documents.
- They provide confidence that a message came from a known sender and has not been altered.

## <span style="color:rgb(57, 224, 140);">History</span>
- First described by Whitfield Diffie and Martin Hellman in 1976.
- [[_content/dictionary#R|RSA]] algorithm, invented by Rivest, Shamir, and Adleman, was one of the earliest implementations.

## <span style="color:rgb(57, 224, 140);">Method</span>
- Involves three algorithms: key generation, signing, and verification.
- Uses asymmetric cryptography, where a private key signs the message and a public key verifies it.

## <span style="color:rgb(57, 224, 140);">Applications</span>
- Commonly used in software distribution, financial transactions, and contract management.
- Ensures the integrity and authenticity of electronic documents.

## <span style="color:rgb(57, 224, 140);">Security Properties</span>
- Authentication: Confirms the identity of the sender.
- Non-repudiation: Prevents the sender from denying the authenticity of their signature.
- Integrity: Ensures the message has not been altered.

## <span style="color:rgb(57, 224, 140);">Additional Security Precautions</span>
- Smart Cards: Store private keys securely and require a [[_content/dictionary#P|PIN]] for activation.
- [[_content/dictionary#W|WYSIWYS]] (What You See Is What You Sign): Ensures the signed content is exactly what the signer intended.

## <span style="color:rgb(57, 224, 140);">Legal and Practical Use</span>
- Digital signatures have legal significance in many countries.
- They are equivalent to handwritten signatures but are more secure and harder to forge.

![[[_content/dictionary#T|TCP]] Diagram](tcp_diagram.png)

## Connection termination
The connection termination phase uses a four-way handshake, with each side of the connection terminating independently. When an endpoint wishes to stop its half of the connection, it transmits a [[_content/dictionary#F|FIN]] packet, which the other end acknowledges with an [[_content/dictionary#A|ACK]]. Therefore, a typical tear-down requires a pair of FIN and ACK segments from each [[_content/dictionary#T|TCP]] endpoint. After the side that sent the first FIN has responded with the final ACK, it waits for a timeout before finally closing the connection, during which time the local port is unavailable for new connections; this state lets the TCP client resend the final acknowledgment to the server in case the ACK is lost in transit. The time duration is implementation-dependent, but some common values are 30 seconds, 1 minute, and 2 minutes. After the timeout, the client enters the [[_content/dictionary#C|CLOSED]] state and the local port becomes available for new connections.
![TCP Diagram](tcp_initiator_receiver.png)

## Packet Content
When sending packets using [[_content/dictionary#T|TCP/[[_content/dictionary#I|IP]]]], the data portion of each IP packet is formatted as a [[_content/dictionary#T|TCP]] segment. Each [[_content/dictionary#T|TCP]] segment contains a header and data. The [[_content/dictionary#T|TCP]] header contains many more fields than the [[_content/dictionary#U|UDP]] header and can range in size from **20** to **60** bytes, depending on the size of the options field. The [[_content/dictionary#T|TCP]] header shares some fields with the [[_content/dictionary#U|UDP]] header: source port number, destination port number, and checksum. To remember how those are used, review the UDP article.
![TCP Diagram](tcp_packet_content.png)
