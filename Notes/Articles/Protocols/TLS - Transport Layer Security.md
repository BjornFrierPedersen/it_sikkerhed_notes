## Source: 
- https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:secure-internet-protocols/a/transport-layer-security-protocol-tls

## <span style="color:rgb(57, 224, 140);">Overview</span>
- [[_content/dictionary#T|TLS]] adds a layer of security on top of [[_content/dictionary#T|TCP]]/[[_content/dictionary#I|IP]] protocols.
- It uses both symmetric and public key encryption to securely send private data.
- [[_content/dictionary#T|TLS]] also provides authentication and message tampering detection.

## <span style="color:rgb(57, 224, 140);">Process of Secure Communication with TLS</span>
- [[_content/dictionary#T|TCP]] Handshake: Establishes a connection between client and server.
- [[_content/dictionary#T|TLS]] Initiation: Client requests a [[_content/dictionary#T|TLS]] connection and specifies encryption techniques.
- Server Confirmation: Server confirms the protocol and sends a digital certificate with its public key.
- Certificate Verification: Client verifies the server's certificate.
- Shared Key Generation: Client and server generate a shared key using public key encryption.
- Secure Data Transmission: Data is encrypted with the shared key and securely transmitted.

## <span style="color:rgb(57, 224, 140);">Applications</span>
- [[_content/dictionary#T|TLS]] is used for secure email, file uploads, and most notably, secure website browsing ([[_content/dictionary#H|HTTPS]]).

## <span style="color:rgb(57, 224, 140);">Security Benefits</span>
- Provides a secure layer on top of [[_content/dictionary#T|TCP]]/[[_content/dictionary#I|IP]].
- Ensures private data is protected during transmission.