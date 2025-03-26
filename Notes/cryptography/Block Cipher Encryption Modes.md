## Explained in Simple Terms
- Block ciphers (like [[_content/dictionary#A|AES]]) work on fixed-size blocks of data (typically 128 bits or 16 bytes). But what if your message is longer or shorter than that exact size? That's where block cipher modes come in. They're like different recipes that tell you how to use a block cipher to encrypt data of any length. Each mode has different security properties and trade-offs. Some modes are like linking blocks together in a chain, others turn block ciphers into stream ciphers, and some provide built-in authentication to detect tampering. Choosing the right mode is crucial for security.

## Basic Concepts

### What is a Block Cipher?
- Encrypts fixed-size blocks of data (e.g., 128 bits for [[_content/dictionary#A|AES]])
- Same key used for each block
- Common block ciphers: [[_content/dictionary#A|AES]], [[_content/dictionary#D|DES]], [[_content/dictionary#3|3DES]], [[_content/dictionary#B|Blowfish]]

### Why Modes Matter
- Handle messages of arbitrary length
- Prevent patterns in plaintext from showing in ciphertext
- Provide different security properties (confidentiality, integrity)
- Offer different performance characteristics

### Common Challenges Addressed by Modes
- Padding requirements
- Initialization vector usage
- Parallelizability
- Error propagation
- Authentication

## Common Block Cipher Modes

### [[_content/dictionary#E|ECB]] (Electronic Codebook)

![[[_content/dictionary#E|ECB]] Mode](../images/block_cipher_ecb.md)

#### How it Works
- Each block is encrypted independently
- Same plaintext block always encrypts to same ciphertext block
- No initialization vector needed

#### Properties
- **Confidentiality**: Weak - patterns in plaintext are visible in ciphertext
- **Parallelizability**: Excellent - blocks can be encrypted/decrypted in parallel
- **Error propagation**: None - errors affect only the corresponding block
- **Padding**: Required for partial blocks
- **Simplicity**: Very simple implementation

#### Security Concerns
- Patterns in data remain visible in ciphertext (the "[[_content/dictionary#E|ECB]] penguin" problem)
- Susceptible to replay attacks (identical blocks can be substituted)
- Generally not recommended for secure applications

#### Use Cases
- Appropriate only for encrypting small amounts of random data (e.g., encryption keys)
- Never use for images, text, or structured data

### [[_content/dictionary#C|CBC]] (Cipher Block Chaining)

![[[_content/dictionary#C|CBC]] Mode](../images/block_cipher_cbc.md)

#### How it Works
- Each plaintext block is XORed with the previous ciphertext block before encryption
- First block uses an initialization vector ([[_content/dictionary#I|IV]])
- Encryption is sequential, decryption can be parallelized

#### Properties
- **Confidentiality**: Good - when used with random, unpredictable [[_content/dictionary#I|IV]]
- **Parallelizability**: Encryption is sequential, decryption can be parallel
- **Error propagation**: Error in one block affects that block and corresponding bit positions in the next block
- **Padding**: Required for partial blocks
- **[[_content/dictionary#I|IV]] requirement**: Random, unpredictable IV needed

#### Security Concerns
- Padding oracle attacks possible with improper implementations
- Predictable IVs lead to chosen-plaintext attacks
- No built-in authentication

#### Use Cases
- General-purpose encryption
- Was the standard mode for many years before [[_content/dictionary#G|GCM]]
- Used in many protocols and standards

### [[_content/dictionary#C|CTR]] (Counter)

![[[_content/dictionary#C|CTR]] Mode](../images/block_cipher_ctr.md)

#### How it Works
- Turns a block cipher into a stream cipher
- Encrypts a counter value and XORs the result with plaintext
- Counter typically consists of a nonce (number used once) plus a block counter

#### Properties
- **Confidentiality**: Good - when used with unique nonce for each message
- **Parallelizability**: Excellent - both encryption and decryption can be parallelized
- **Error propagation**: None - errors affect only the corresponding bit positions
- **Padding**: Not required - can encrypt any bit length
- **[[_content/dictionary#I|IV]] requirement**: Unique nonce needed for each message with same key

#### Security Concerns
- Catastrophic security failure if nonce is reused
- No built-in authentication
- Counter management must be careful to avoid repeats

#### Use Cases
- High-performance encryption scenarios
- When parallelization is important
- Streaming applications
- Basis for more complex modes like [[_content/dictionary#G|GCM]]

### [[_content/dictionary#O|OFB]] (Output Feedback)

![[[_content/dictionary#O|OFB]] Mode](../images/block_cipher_ofb.md)

#### How it Works
- Generates a keystream by repeatedly encrypting the [[_content/dictionary#I|IV]]
- Plaintext is XORed with keystream for encryption
- Functions like a synchronous stream cipher

#### Properties
- **Confidentiality**: Good - when used with random [[_content/dictionary#I|IV]]
- **Parallelizability**: Poor - sequential by nature
- **Error propagation**: None - bit errors only affect corresponding bit positions
- **Padding**: Not required - can encrypt any bit length
- **[[_content/dictionary#I|IV]] requirement**: Random IV needed

#### Security Concerns
- [[_content/dictionary#I|IV]] must never be reused with same key
- No built-in authentication
- Susceptible to bit-flipping attacks

#### Use Cases
- When bit-level encryption is needed
- Applications where error propagation is a concern
- Less commonly used today

### [[_content/dictionary#C|CFB]] (Cipher Feedback)

![[[_content/dictionary#C|CFB]] Mode](../images/block_cipher_cfb.md)

#### How it Works
- Previous ciphertext block is encrypted and XORed with plaintext
- Initial block uses an [[_content/dictionary#I|IV]]
- Functions like a self-synchronizing stream cipher

#### Properties
- **Confidentiality**: Good - when used with random [[_content/dictionary#I|IV]]
- **Parallelizability**: Encryption is sequential, decryption can be parallel
- **Error propagation**: Limited - errors affect the current block and several subsequent blocks
- **Padding**: Not required - can encrypt any bit length
- **[[_content/dictionary#I|IV]] requirement**: Random IV needed

#### Security Concerns
- [[_content/dictionary#I|IV]] must never be reused with same key
- No built-in authentication
- Susceptible to bit-flipping attacks

#### Use Cases
- Legacy systems
- When self-synchronization is desirable
- Less commonly used in new designs

### [[_content/dictionary#G|GCM]] (Galois/Counter Mode)

![[[_content/dictionary#G|GCM]] Mode](../images/block_cipher_gcm.md)

#### How it Works
- Combines [[_content/dictionary#C|CTR]] mode with Galois field multiplication for authentication
- Provides both encryption (confidentiality) and authentication (integrity)
- Uses a nonce ([[_content/dictionary#I|IV]]) and can include additional authenticated data ([[_content/dictionary#A|AAD]])

#### Properties
- **Confidentiality**: Excellent - when used with unique nonce
- **Authentication**: Provides built-in authentication
- **Parallelizability**: Excellent - highly parallelizable
- **Error propagation**: None for confidentiality, complete for authentication
- **Padding**: Not required
- **[[_content/dictionary#I|IV]] requirement**: Unique nonce for each encryption with same key

#### Security Concerns
- Catastrophic security failure if nonce is reused
- Authentication tag length affects security level
- Implementation complexity

#### Use Cases
- Modern standard for authenticated encryption
- [[_content/dictionary#T|TLS]] 1.2 and 1.3
- IPsec
- Recommended for most new applications requiring authenticated encryption

### [[_content/dictionary#C|CCM]] (Counter with [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]])

![[[_content/dictionary#C|CCM]] Mode](../images/block_cipher_ccm.md)

#### How it Works
- Combines [[_content/dictionary#C|CTR]] mode for encryption with [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]] for authentication
- Single key used for both operations
- Two passes over the data required

#### Properties
- **Confidentiality**: Good - when used with unique nonce
- **Authentication**: Provides built-in authentication
- **Parallelizability**: Limited - two-pass algorithm
- **Error propagation**: None for confidentiality, complete for authentication
- **Padding**: Not required
- **[[_content/dictionary#I|IV]] requirement**: Unique nonce for each encryption with same key

#### Security Concerns
- Nonce must never be reused
- Less efficient than [[_content/dictionary#G|GCM]] for large messages
- Two passes over the data required

#### Use Cases
- Wireless security ([[_content/dictionary#I|IEEE]] 802.11i/WPA2)
- Some IoT and constrained environments
- Where hardware support for [[_content/dictionary#G|GCM]] is not available

## Choosing the Right Mode

### Security Considerations
- **Confidentiality only**: [[_content/dictionary#C|CTR]] or [[_content/dictionary#C|CBC]] (but consider authenticated modes instead)
- **Confidentiality + Integrity**: [[_content/dictionary#G|GCM]], [[_content/dictionary#C|CCM]], or another authenticated mode
- **Avoiding padding complexities**: [[_content/dictionary#C|CTR]], [[_content/dictionary#G|GCM]] (no padding required)
- **Strong security guarantees**: Always prefer authenticated encryption ([[_content/dictionary#G|GCM]], [[_content/dictionary#C|CCM]])

### Performance Considerations
- **Parallelization**: [[_content/dictionary#C|CTR]] and [[_content/dictionary#G|GCM]] are highly parallelizable
- **Hardware acceleration**: [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] often has hardware support in modern CPUs
- **Memory constraints**: [[_content/dictionary#C|CBC]] uses less memory than [[_content/dictionary#G|GCM]]
- **Processing overhead**: [[_content/dictionary#G|GCM]] more complex than [[_content/dictionary#C|CTR]], but usually hardware-accelerated

### Implementation Factors
- **Existing systems**: May dictate mode choice for compatibility
- **Available libraries**: Quality implementations matter more than theoretical differences
- **Hardware support**: Use hardware-accelerated modes when available
- **Key management**: All modes require strong key management

## Common Vulnerabilities and Attacks

### Initialization Vector Misuse
- **Reused IVs/nonces**: Catastrophic for stream cipher modes ([[_content/dictionary#C|CTR]], [[_content/dictionary#G|GCM]])
- **Predictable IVs**: Enables chosen-plaintext attacks in [[_content/dictionary#C|CBC]] mode
- **Fixed IVs**: Reveals patterns and enables attacks

### Padding Oracle Attacks
- Affects modes requiring padding ([[_content/dictionary#C|CBC]], [[_content/dictionary#E|ECB]])
- Allows decryption of data without knowing the key
- Mitigated by authenticated encryption or proper error handling

### Bit Flipping Attacks
- Affects unauthenticated modes ([[_content/dictionary#E|ECB]], [[_content/dictionary#C|CBC]], [[_content/dictionary#C|CTR]], [[_content/dictionary#C|CFB]], [[_content/dictionary#O|OFB]])
- Attacker can modify ciphertext to make predictable changes to plaintext
- Prevented by authenticated encryption modes

### Length Extension Attacks
- Not directly related to block cipher modes, but relevant to authentication
- Some [[_content/dictionary#M|MAC]] constructions are vulnerable
- [[_content/dictionary#G|GCM]] and [[_content/dictionary#C|CCM]] are not vulnerable

## Best Practices

### Always Use Authenticated Encryption
- Prefer [[_content/dictionary#G|GCM]] or another authenticated encryption mode
- If using an unauthenticated mode, add a separate [[_content/dictionary#M|MAC]]/[[_content/dictionary#H|HMAC]]
- Verify the integrity tag before using decrypted data

### Proper [[_content/dictionary#I|IV]]/Nonce Management
- Generate cryptographically secure random IVs when required
- Never reuse nonces with the same key
- Use a secure random number generator

### Secure Implementation
- Use established libraries, don't implement modes yourself
- Follow recommended parameters (tag length, nonce size)
- Be aware of language/library-specific quirks

### Key Management
- Rotate keys regularly
- Different keys for different purposes
- Protect key material in storage and memory

## Code Examples

### [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]] Encryption (Python)
```python
from cryptography.hazmat.primitives.ciphers.aead import [[_content/dictionary#A|AESGCM]]
import os

def encrypt_aes_gcm(plaintext, associated_data=None):
    # Generate a random 12-byte nonce
    nonce = os.urandom(12)

    # Generate a random 256-bit key
    key = [[_content/dictionary#A|AESGCM]].generate_key(bit_length=256)
    aesgcm = AESGCM(key)

    # Encrypt and authenticate
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)

    return key, nonce, ciphertext

def decrypt_aes_gcm(key, nonce, ciphertext, associated_data=None):
    aesgcm = [[_content/dictionary#A|AESGCM]](key)

    # Decrypt and verify
    plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data)

    return plaintext
```

### [[_content/dictionary#A|AES]]-[[_content/dictionary#C|CBC]] Encryption (Python)
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_aes_cbc(plaintext):
    # Generate a random 16-byte [[_content/dictionary#I|IV]]
    iv = os.urandom(16)

    # Generate a random 256-bit key
    key = os.urandom(32)

    # Create an encryptor object
    cipher = Cipher(algorithms.[[_content/dictionary#A|AES]](key), modes.[[_content/dictionary#C|CBC]](iv))
    encryptor = cipher.encryptor()

    # Pad the plaintext to a multiple of the block size
    padder = padding.PKCS7(algorithms.[[_content/dictionary#A|AES]].block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return key, iv, ciphertext

def decrypt_aes_cbc(key, iv, ciphertext):
    # Create a decryptor object
    cipher = Cipher(algorithms.[[_content/dictionary#A|AES]](key), modes.[[_content/dictionary#C|CBC]](iv))
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.[[_content/dictionary#A|AES]].block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext
``` 

## Article links:
[[Block cipher mode of operation]]

