# [[_content/dictionary#S|SSL]] and [[_content/dictionary#T|TLS]]

## Explained in Simple Terms
[[_content/dictionary#S|SSL]] (Secure Sockets Layer) and its successor [[_content/dictionary#T|TLS]] (Transport Layer Security) are protocols that provide secure communication over the internet. They're like an armored mail truck for your data — they ensure that when you send information online, it's encrypted so no one can read it except the intended recipient, verified so you know you're communicating with the right website, and protected from tampering so no one can alter the contents during transit. When you see "https://" or a padlock icon in your browser, that means [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] is protecting your connection.

## Evolution of [[_content/dictionary#S|SSL]] and [[_content/dictionary#T|TLS]]

### SSL 2.0 (1995)
- First publicly released version of [[_content/dictionary#S|SSL]]
- Developed by Netscape
- **Status**: Deprecated in 2011 ([[_content/dictionary#R|RFC]] 6176)
- **Security**: Fundamentally insecure, multiple vulnerabilities

### SSL 3.0 (1996)
- Significant redesign of [[_content/dictionary#S|SSL]] 2.0
- Still developed by Netscape
- **Status**: Deprecated in 2015 ([[_content/dictionary#R|RFC]] 7568)
- **Security**: Vulnerable to [[_content/dictionary#P|POODLE]] attack

### TLS 1.0 (1999)
- First version of [[_content/dictionary#T|TLS]], based on [[_content/dictionary#S|SSL]] 3.0
- Defined in [[_content/dictionary#R|RFC]] 2246
- **Status**: Deprecated in 2020
- **Security**: Vulnerable to [[_content/dictionary#B|BEAST]], [[_content/dictionary#C|CRIME]] attacks

### [[_content/dictionary#T|TLS]] 1.1 (2006)
- Added protection against cipher block chaining attacks
- Defined in [[_content/dictionary#R|RFC]] 4346
- **Status**: Deprecated in 2020
- **Security**: Lacks support for modern cryptographic algorithms

### [[_content/dictionary#T|TLS]] 1.2 (2008)
- Major upgrade allowing more secure hash functions
- Defined in [[_content/dictionary#R|RFC]] 5246
- **Status**: Currently widely deployed
- **Security**: Strong when properly configured

### [[_content/dictionary#T|TLS]] 1.3 (2018)
- Significant redesign with improved security and performance
- Defined in [[_content/dictionary#R|RFC]] 8446
- **Status**: Modern standard, increasing adoption
- **Security**: Removed all legacy insecure algorithms

## How [[_content/dictionary#T|TLS]] Works

### TLS Handshake Process
1. **Client Hello**: Client sends supported [[_content/dictionary#T|TLS]] versions, cipher suites, and a random value
2. **Server Hello**: Server chooses [[_content/dictionary#T|TLS]] version and cipher suite, sends its certificate and a random value
3. **Certificate Validation**: Client verifies the server's certificate against trusted [[_content/dictionary#C|CA]]s
4. **Key Exchange**: Client and server establish a shared secret using asymmetric cryptography
5. **Session Key Generation**: Both parties derive symmetric session keys from the shared secret
6. **Finished Messages**: Both sides confirm the handshake completed successfully

### Key [[_content/dictionary#T|TLS]] Components

#### Cipher Suites
- Combinations of algorithms for key exchange, authentication, encryption, and message integrity
- Example: `TLS_AES_256_GCM_SHA384` ([[_content/dictionary#T|TLS]] 1.3 suite using [[_content/dictionary#A|AES]]-256 in [[_content/dictionary#G|GCM]] mode with [[_content/dictionary#S|SHA]]-384)
- Older [[_content/dictionary#T|TLS]] versions used more complex naming: `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

#### Digital Certificates
- [[_content/dictionary#X|X.509]] certificates containing:
  - Server's public key
  - Server identity (domain name)
  - Issuing Certificate Authority information
  - Validity period
  - Digital signature from the issuing [[_content/dictionary#C|CA]]

#### Session Keys
- Symmetric encryption keys used for bulk data encryption
- Generated uniquely for each connection
- Discarded after the session ends (forward secrecy in modern implementations)

## [[_content/dictionary#T|TLS]] Security Features

### Confidentiality
- Encryption of all data transmitted between client and server
- Modern ciphers: [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]], [[_content/dictionary#C|ChaCha20]]-[[_content/dictionary#P|Poly1305]]
- Perfect Forward Secrecy in [[_content/dictionary#T|TLS]] 1.2 (with proper configurations) and [[_content/dictionary#T|TLS]] 1.3

### Integrity
- Message Authentication Codes (MACs) detect any tampering with transmitted data
- Modern algorithms: [[_content/dictionary#H|HMAC]]-SHA256, HMAC-SHA384, [[_content/dictionary#P|Poly1305]]

### Authentication
- Server authentication using [[_content/dictionary#X|X.509]] certificates
- Optional client authentication (mutual [[_content/dictionary#T|TLS]])
- Certificate chain validation through trusted Certificate Authorities

### Replay Protection
- Sequence numbers prevent replay attacks
- Each record contains a unique sequence number
- Prevents attackers from capturing and retransmitting previous messages

## Common [[_content/dictionary#T|TLS]] Vulnerabilities and Attacks

### Protocol-Level Vulnerabilities

#### [[_content/dictionary#B|BEAST]] (Browser Exploit Against [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]])
- Affects: [[_content/dictionary#T|TLS]] 1.0 and below
- Type: Chosen plaintext attack against [[_content/dictionary#C|CBC]] mode ciphers
- Mitigation: Upgrade to [[_content/dictionary#T|TLS]] 1.1+, or use mitigations like 1/n-1 record splitting

#### [[_content/dictionary#P|POODLE]] (Padding Oracle On Downgraded Legacy Encryption)
- Affects: [[_content/dictionary#S|SSL]] 3.0
- Type: Padding oracle attack
- Mitigation: Disable [[_content/dictionary#S|SSL]] 3.0 completely

#### [[_content/dictionary#F|FREAK]] (Factoring Attack on [[_content/dictionary#R|RSA]] Export Keys)
- Affects: Implementations supporting export-grade cryptography
- Type: Downgrade attack forcing weak [[_content/dictionary#R|RSA]] export keys
- Mitigation: Disable support for export cipher suites

#### [[_content/dictionary#H|Heartbleed]]
- Affects: OpenSSL 1.0.1 through 1.0.1f
- Type: Implementation bug allowing memory leakage
- Impact: Could expose private keys, session keys, and sensitive data
- Mitigation: Update OpenSSL

#### [[_content/dictionary#L|Logjam]]
- Affects: Systems using Diffie-Hellman key exchange with weak parameters
- Type: Downgrade attack forcing weak [[_content/dictionary#D|DH]] parameters
- Mitigation: Use sufficiently large [[_content/dictionary#D|DH]] parameters or Elliptic Curve DH

### Implementation Vulnerabilities

#### Certificate Validation Errors
- Failure to properly validate certificate chains
- Incorrect hostname verification
- Accepting self-signed certificates

#### Insecure Cipher Suite Selection
- Supporting deprecated or weak cipher suites
- Incorrect priorities allowing downgrade attacks

#### Renegotiation Issues
- Vulnerabilities in the [[_content/dictionary#T|TLS]] renegotiation process
- Can lead to man-in-the-middle attacks in some implementations

## Best Practices for [[_content/dictionary#T|TLS]] Implementation

### Protocol Version
- Use [[_content/dictionary#T|TLS]] 1.2 or TLS 1.3
- Disable [[_content/dictionary#S|SSL]] 2.0, SSL 3.0, [[_content/dictionary#T|TLS]] 1.0, and TLS 1.1

### Cipher Suite Selection
- Prioritize [[_content/dictionary#A|AEAD]] ciphers ([[_content/dictionary#G|GCM]], [[_content/dictionary#C|ChaCha20]]-[[_content/dictionary#P|Poly1305]])
- Prefer Elliptic Curve Diffie-Hellman ([[_content/dictionary#E|ECDHE]]) key exchange
- Disable weak algorithms ([[_content/dictionary#R|RC4]], [[_content/dictionary#D|DES]], [[_content/dictionary#3|3DES]], [[_content/dictionary#M|MD5]])
- Recommended modern cipher suites:
  - [[_content/dictionary#T|TLS]] 1.3: `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`
  - TLS 1.2: `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

### Certificate Management
- Use certificates from reputable Certificate Authorities
- Properly validate the entire certificate chain
- Implement [[_content/dictionary#O|OCSP]] stapling for revocation checking
- Use appropriate key sizes ([[_content/dictionary#R|RSA]]: 2048+ bits, [[_content/dictionary#E|ECC]]: 256+ bits)

### Extended Validation
- Enable Certificate Transparency ([[_content/dictionary#C|CT]]) logging
- Implement [[_content/dictionary#H|HTTP]] Strict Transport Security ([[_content/dictionary#H|HSTS]])
- Consider Certificate Authority Authorization ([[_content/dictionary#C|CAA]]) [[_content/dictionary#D|DNS]] records

### Proper Implementation
- Use established [[_content/dictionary#T|TLS]] libraries (OpenSSL, GnuTLS, SChannel)
- Keep libraries updated with security patches
- Follow language-specific best practices for [[_content/dictionary#T|TLS]] implementation

## [[_content/dictionary#T|TLS]] Performance Optimization

### Session Resumption
- Reduces handshake overhead for returning clients
- Methods: Session IDs, Session Tickets (stateless)
- Security considerations: rotation of encryption keys for session tickets

### [[_content/dictionary#T|TLS]] False Start
- Begin sending application data before handshake fully completes
- Reduces latency for new connections
- Only works with forward-secure cipher suites

### [[_content/dictionary#T|TLS]] 1.3 Improvements
- 1-[[_content/dictionary#R|RTT]] handshakes (reduced from 2-RTT in [[_content/dictionary#T|TLS]] 1.2)
- 0-[[_content/dictionary#R|RTT]] resumption (optional, with security tradeoffs)
- Simplified cipher suite negotiation

### Connection Pooling
- Reuse existing [[_content/dictionary#T|TLS]] connections for multiple requests
- Eliminates handshake overhead for subsequent requests
- Important for high-traffic applications

## [[_content/dictionary#T|TLS]] Testing and Verification

### Online Testing Tools
- [[[_content/dictionary#S|SSL]] Labs Server Test](https://www.ssllabs.com/ssltest/)
- [[[_content/dictionary#S|SSL]] Labs Client Test](https://www.ssllabs.com/ssltest/viewMyClient.html)
- [Hardenize](https://www.hardenize.com/)

### Command Line Tools
- OpenSSL command line tools
- testssl.sh for comprehensive scanning
- nmap with ssl-enum-ciphers script

### Monitoring
- Regular scanning of [[_content/dictionary#T|TLS]] configurations
- Certificate expiration monitoring
- Vulnerability scanning

## Future of [[_content/dictionary#T|TLS]]

### [[_content/dictionary#T|TLS]] 1.3 Adoption
- Increased deployment across the internet
- Improved security by removing legacy algorithms
- Better performance with reduced handshake latency

### Post-Quantum [[_content/dictionary#T|TLS]]
- Research into quantum-resistant algorithms for [[_content/dictionary#T|TLS]]
- Potential future [[_content/dictionary#T|TLS]] versions with post-quantum security
- Hybrid approaches during transition period

### Encrypted [[_content/dictionary#S|SNI]] (Server Name Indication)
- Protecting the hostname during [[_content/dictionary#T|TLS]] handshakes
- Improving privacy by concealing which specific site is being visited
- Implementation via [[_content/dictionary#T|TLS]] extensions

### [[_content/dictionary#T|TLS]] Inspection Challenges
- Balancing security monitoring with encryption
- Enterprise challenges with decryption and re-encryption
- Privacy and security implications of [[_content/dictionary#T|TLS]] interception 