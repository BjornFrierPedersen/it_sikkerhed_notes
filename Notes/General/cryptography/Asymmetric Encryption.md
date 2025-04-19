# Asymmetric Encryption

## Explained in Simple Terms
Asymmetric encryption (also called public-key cryptography) uses two different but mathematically linked keys: a public key that can be freely shared with anyone, and a private key that must be kept secret. It's like a special mailbox where anyone can drop a letter through the slot (encrypt with public key), but only the person with the unique key can open it and read the messages (decrypt with private key).

## How Asymmetric Encryption Works

![Message Encrypted with the Receiver's Public Key](../images/asymmetric_encryption.md)

As shown in the image above:
1. When Bob wants to send a secure message to Alice, he encrypts it using Alice's public key
2. Only Alice's private key can decrypt the message
3. Even though Bob used Alice's public key for encryption, he cannot decrypt the message himself
4. Alice has no guarantee about who sent the message without additional authentication

### Key Pairs
- Each user generates a mathematically linked pair of keys
- The private key must remain absolutely secret
- The public key can be freely distributed
- What is encrypted with the public key can only be decrypted with the corresponding private key

## Core Mathematical Principles

Asymmetric encryption relies on mathematical problems that are:
- Easy to compute in one direction
- Extremely difficult to reverse (computationally infeasible)

Common mathematical foundations include:

### Integer Factorization ([[_content/dictionary#R|RSA]])
- Based on the difficulty of factoring the product of two large prime numbers
- Given N = p × q (where p and q are very large primes), it's extremely difficult to find p and q

### Discrete Logarithm Problem (Diffie-Hellman, [[_content/dictionary#D|DSA]], [[_content/dictionary#E|ElGamal]])
- Based on the difficulty of finding the exponent when given the base and result in modular arithmetic
- Given g^x mod p = y, it's very difficult to find x

### Elliptic Curve Discrete Logarithm Problem ([[_content/dictionary#E|ECC]])
- Based on the properties of elliptic curves over finite fields
- More efficient than traditional asymmetric algorithms (smaller key sizes for equivalent security)

## Common Asymmetric Algorithms

### [[_content/dictionary#R|RSA]] (Rivest-Shamir-Adleman)
- The most widely used asymmetric algorithm
- Key sizes typically 2048 or 4096 bits
- Used for encryption and digital signatures
- Security relies on the difficulty of factoring large numbers
- **Applications**: Digital signatures, key exchange, secure communications

### ECC (Elliptic Curve Cryptography)
- Based on algebraic structures of elliptic curves
- Requires smaller keys than [[_content/dictionary#R|RSA]] for equivalent security
- 256-bit [[_content/dictionary#E|ECC]] roughly equivalent to 3072-bit [[_content/dictionary#R|RSA]]
- More efficient for mobile and resource-constrained devices
- **Applications**: [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]], Bitcoin and other cryptocurrencies

### Diffie-Hellman Key Exchange
- Not an encryption algorithm but a key exchange protocol
- Allows two parties to generate a shared secret over an insecure channel
- Forms the basis for many secure communications protocols
- **Applications**: [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]] handshakes, secure messaging apps
- If you have two parties, Alice and Bob, and they want to exchange a secret key, without Eve knowing the secret key they can do so using [[_content/dictionary#D|Diffie-Hellman]]. If we take colors as an example, Alice and Bob can agree to a public color, that everyone knows, say <span style="color: #FFFF00; background-color: #333333;">yellow</span>. Alice and Bob can then each pick a secret color, say Alice chooses <span style="color: #FF0000;">red</span> and Bob chooses <span style="color: #0000FF;">blue</span>. Alice and Bob can then each take the public color <span style="color: #FFFF00; background-color: #333333;">yellow</span> and mix it with their secret color to form a new color. Alice's new color is <span style="color: #FFFF00; background-color: #333333;">yellow</span> mixed with <span style="color: #FF0000;">red</span>, which is <span style="color: #FFA500;">orange</span>. Bob's new color is <span style="color: #FFFF00; background-color: #333333;">yellow</span> mixed with <span style="color: #0000FF;">blue</span>, which is <span style="color: #00FF00;">green</span>. Then they send the result of their mixture to each other, so Alice send the <span style="color: #FFA500;">orange</span> color to Bob and Bob sends the <span style="color: #00FF00;">green</span> color to Alice. Now Alice mixes her secret color with Bobs result, resulting in <span style="color: #FF0000;">red</span> mixed with <span style="color: #00FF00;">green</span>, which is <span style="color: #FFFF00; background-color: #333333;">yellow</span>. Bob does the same thing and mixes his secret color with Alices result, resulting in <span style="color: #0000FF;">blue</span> mixed with <span style="color: #FFA500;">orange</span>, which is also <span style="color: #FFFF00; background-color: #333333;">yellow</span>. Eve, who is listening in on the conversation, knows the public color <span style="color: #FFFF00; background-color: #333333;">yellow</span>, but does not know the secret colors of Alice and Bob, so she cannot determine the secret key. In practive this is done with modular arithmetics and very large numbers, but colors works fine as an example.

### [[_content/dictionary#E|ElGamal]]
- Based on the discrete logarithm problem
- Used for both encryption and digital signatures
- **Applications**: [[_content/dictionary#P|PGP]]/[[_content/dictionary#G|GPG]] email encryption, some government systems

## Advantages of Asymmetric Encryption

1. **Solves the Key Distribution Problem**
   - No need to securely share secret keys before communication
   - Public keys can be distributed openly

2. **Enables Secure Communication Between Strangers**
   - Parties can communicate securely without prior contact

3. **Supports Digital Signatures**
   - Provides authentication and non-repudiation
   - Sender can "sign" messages with their private key

4. **Scalability**
   - N users only need N key pairs, as opposed to N(N-1)/2 keys in symmetric encryption

## Limitations of Asymmetric Encryption

1. **Performance**
   - Much slower than symmetric encryption (100-1000x)
   - Computationally intensive, especially for large amounts of data

2. **Key Size**
   - Requires much longer keys than symmetric encryption for equivalent security
   - [[_content/dictionary#R|RSA]] typically uses 2048-4096 bit keys vs. 256 bits for symmetric algorithms

3. **Quantum Computing Vulnerability**
   - Most current algorithms (especially [[_content/dictionary#R|RSA]]) are vulnerable to quantum computing attacks
   - [[_content/dictionary#S|Shor's algorithm]] could potentially break RSA and [[_content/dictionary#E|ECC]]

## Hybrid Encryption Systems

In practice, asymmetric and symmetric encryption are usually combined:

1. **Key Encapsulation**
   - Generate a random symmetric key (session key)
   - Encrypt the data with the fast symmetric key
   - Encrypt only the symmetric key with asymmetric encryption
   - Send both the encrypted data and the encrypted symmetric key

2. **Benefits**
   - Speed of symmetric encryption for bulk data
   - Security of asymmetric encryption for key exchange
   - Used in [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]], secure messaging, and most modern cryptographic systems

## Real-World Applications

### Secure Communication
- [[_content/dictionary#H|HTTPS]] websites use asymmetric encryption during the [[_content/dictionary#T|TLS]] handshake
- Secure messaging apps use public key cryptography for end-to-end encryption

### Digital Signatures
- Software code signing
- Document authentication
- Email signatures ([[_content/dictionary#S|S/[[_content/dictionary#M|MIME]]]], [[_content/dictionary#P|PGP]])

### [[_content/dictionary#P|PKI]] and Certificate Authorities
- Basis for the trust system of the internet
- Verifies ownership of public keys
- Underpins secure web browsing

### Cryptocurrencies
- Bitcoin and other cryptocurrencies use public/private key pairs for wallet security
- Transactions are signed with private keys

## Best Practices

1. **Key Length Selection**
   - [[_content/dictionary#R|RSA]]: Minimum 2048 bits (3072+ bits for sensitive data)
   - [[_content/dictionary#E|ECC]]: Minimum 256 bits
   - Follow [[_content/dictionary#N|NIST]] or equivalent guidelines

2. **Private Key Protection**
   - Store private keys in secure, isolated environments
   - Consider hardware security modules (HSMs) for critical keys
   - Use strong access controls and encryption for private key storage

3. **Algorithm Selection**
   - Consider moving to elliptic curve algorithms for better performance
   - Be aware of post-quantum cryptography developments
   - Use established libraries and implementations

4. **Certificate Management**
   - Implement proper certificate validation
   - Check certificate revocation
   - Establish clear certificate lifecycle procedures 

   ## Article links:
   - [[Digital Signatures]]
   - [[Block Cipher Encryption Modes]]
   - [[[[_content/dictionary#T|TCP]] - Transmission Control Protocol]]
   - [[Cryptographic Hash Functions]]