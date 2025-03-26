# Digital Signatures

## Explained in Simple Terms
A digital signature is like a personal stamp that only you can create, but anyone can verify is yours. It's created using your private key (which only you have), and it can be verified using your public key (which anyone can access). Digital signatures ensure that a message truly came from you (authentication) and also prove that the message hasn't been altered (integrity). Unlike physical signatures, digital signatures are different for every document you sign, making them impossible to copy from one document to another.

## How Digital Signatures Work

![Message Signing Process](../images/digital_signatures.md)

As shown in the image above:

### Process of Signing:
1. The original message is processed through a hash function to create a fixed-size "message digest"
2. This digest is then signed (encrypted) using the sender's private key
3. The resulting signature is attached to the message

### Verification Process:
1. The receiver calculates the hash of the received message
2. The signature is verified (decrypted) using the sender's public key, yielding the original hash
3. If the calculated hash matches the decrypted hash, the signature is valid

## Key Properties of Digital Signatures

### 1. Authentication
- Verifies the identity of the signer
- Only the holder of the private key could have created the signature
- Recipient can be confident of who signed the message

### 2. Integrity
- Ensures the message hasn't been altered after signing
- Even a single bit change in the message will cause verification to fail
- Provides tamper detection

### 3. Non-repudiation
- Signer cannot later deny having signed the document
- Provides legal accountability
- Crucial for e-commerce, legal documents, and contracts

### 4. Uniqueness
- Each signature is unique to both the document and the signer
- Cannot be copied from one document to another
- Every document gets a different signature, even from the same signer

## Digital Signature Algorithms

### [[_content/dictionary#R|RSA]] Signatures
- Based on the [[_content/dictionary#R|RSA]] asymmetric encryption algorithm
- Most widely used signature algorithm
- Process: hash the message, encrypt the hash with signer's private key
- Security depends on difficulty of factoring large numbers
- Key sizes typically 2048 or 4096 bits

### [[_content/dictionary#D|DSA]] (Digital Signature Algorithm)
- Designed specifically for digital signatures
- Based on the discrete logarithm problem
- Standardized by [[_content/dictionary#N|NIST]] in [[_content/dictionary#F|FIPS]] 186
- Faster signature generation than [[_content/dictionary#R|RSA]], but slower verification
- Only used for signatures, not encryption

### [[_content/dictionary#E|ECDSA]] (Elliptic Curve Digital Signature Algorithm)
- Based on elliptic curve cryptography
- More efficient than [[_content/dictionary#R|RSA]] and [[_content/dictionary#D|DSA]]
- Requires smaller keys for equivalent security
- 256-bit [[_content/dictionary#E|ECDSA]] roughly equivalent to 3072-bit [[_content/dictionary#R|RSA]]
- Used in Bitcoin, Ethereum, and other cryptocurrencies

### EdDSA (Edwards-curve Digital Signature Algorithm)
- Modern signature algorithm (e.g., Ed25519)
- High security and performance
- Resistant to many side-channel attacks
- Used in modern secure systems, [[_content/dictionary#S|SSH]], [[_content/dictionary#T|TLS]], etc.

## Applications of Digital Signatures

### Document Signing
- [[_content/dictionary#P|PDF]] and other document formats
- Electronic contracts
- Government forms
- Legal agreements

### Code Signing
- Software publishers sign their code
- Operating systems can verify the authenticity of software
- Helps prevent malware distribution
- Example: Microsoft Authenticode, Apple Developer signing

### Email Signing
- [[_content/dictionary#S|S/[[_content/dictionary#M|MIME]]]] and [[_content/dictionary#P|PGP]] standards
- Verifies email origin and integrity
- Commonly used in business and government communications

### Certificate Signing
- Certificate Authorities sign [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] certificates
- Creates chain of trust for secure websites
- Fundamental to the security of the web

### Financial Transactions
- Cryptocurrencies use digital signatures to authorize transactions
- Banking systems use signatures for wire transfers
- Payment processing systems

## Digital Signature Standards and Frameworks

### [[_content/dictionary#X|X.509]]
- Standard format for public key certificates
- Defines how certificates are structured and validated
- Used in [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]] for [[_content/dictionary#H|HTTPS]]

### [[_content/dictionary#P|PKCS]] (Public Key Cryptography Standards)
- Set of standards for implementing public key cryptography
- [[_content/dictionary#P|PKCS]]#1 defines [[_content/dictionary#R|RSA]] cryptography standard
- [[_content/dictionary#P|PKCS]]#7 defines cryptographic message syntax for signatures

### [[_content/dictionary#X|XML]] Digital Signature
- Standard for [[_content/dictionary#X|XML]]-based signatures
- Used in [[_content/dictionary#S|SAML]], [[_content/dictionary#S|SOAP]], and other [[_content/dictionary#X|XML]]-based protocols
- Allows signing specific parts of [[_content/dictionary#X|XML]] documents

### [[_content/dictionary#J|JSON]] Web Signature ([[_content/dictionary#J|JWS]])
- Standard for signing [[_content/dictionary#J|JSON]] data
- Used in [[_content/dictionary#J|JSON]] Web Tokens ([[_content/dictionary#J|JWT]])
- Common in modern web APIs and authentication systems

## Security Considerations and Best Practices

### Hash Algorithm Selection
- Use strong, collision-resistant hash algorithms ([[_content/dictionary#S|SHA]]-256 or better)
- Avoid [[_content/dictionary#M|MD5]] and [[_content/dictionary#S|SHA]]-1 (both have known vulnerabilities)

### Key Management
- Protect private signing keys with strong security controls
- Consider hardware security modules (HSMs) for important keys
- Implement proper key rotation procedures

### Signature Validation
- Always validate the entire certificate chain
- Check certificate revocation status
- Verify time validity

### Implementation Vulnerabilities
- Beware of signature verification bypass attacks
- Validate all aspects of the signature process
- Use established cryptographic libraries—don't implement yourself

## Legal Status

Digital signatures have legal standing in many jurisdictions:

### [[_content/dictionary#E|eIDAS]] Regulation ([[_content/dictionary#E|EU]])
- Establishes framework for electronic identification and trust services
- Gives qualified electronic signatures the same legal effect as handwritten signatures

### [[_content/dictionary#E|ESIGN]] Act ([[_content/dictionary#U|US]])
- Gives electronic signatures the same legal weight as handwritten signatures
- Facilitates e-commerce and electronic contracts

### Similar laws exist in many countries
- Enables paperless legal processes
- Requirements vary by jurisdiction 

## Article links:
[[[[_content/dictionary#T|TCP]] - Transmission Control Protocol]]