# Symmetric Encryption

## Explained in Simple Terms
Symmetric encryption is like having a single key that both locks and unlocks a box. The same key is used by both the sender to encrypt (lock) a message and by the receiver to decrypt (unlock) it. It's fast and efficient, but has one big challenge: you need to securely share that key with others before you can exchange secret messages with them.

## Key Concepts

### How Symmetric Encryption Works
1. A single secret key is used for both encryption and decryption
2. The key must be shared securely between all parties that need to encrypt/decrypt the data
3. The encryption algorithm scrambles the data in a way that can only be unscrambled with the key
4. Symmetric algorithms are relatively fast and efficient for large amounts of data

## Common Symmetric Key Algorithms

### [[_content/dictionary#A|AES]] (Advanced Encryption Standard)
- Current standard for symmetric encryption
- Key sizes: 128, 192, or 256 bits
- Block size: 128 bits
- Replaced [[_content/dictionary#D|DES]] as the federal standard in 2001
- Highly secure when implemented correctly
- Used in: Wi-Fi security, file encryption, [[_content/dictionary#H|HTTPS]], and more

### [[_content/dictionary#D|DES]] (Data Encryption Standard)
- Older algorithm developed in the 1970s
- Key size: 56 bits (too small by modern standards)
- Block size: 64 bits
- **Security status**: Considered broken and insecure
- **Legacy usage**: Some legacy systems still use Triple [[_content/dictionary#D|DES]] ([[_content/dictionary#3|3DES]])

### [[_content/dictionary#3|3DES]] (Triple [[_content/dictionary#D|DES]])
- Enhancement of [[_content/dictionary#D|DES]] that applies the algorithm three times
- Effective key length: 112 bits
- Slower than modern alternatives
- **Security status**: Being phased out
- **Legacy usage**: Banking systems and payment processing

### [[_content/dictionary#C|ChaCha20]]
- Stream cipher (encrypts data bit-by-bit, not in blocks)
- Key size: 256 bits
- Fast, especially in software implementations
- Popular alternative to [[_content/dictionary#A|AES]] in some applications
- Used in: [[_content/dictionary#T|TLS]] connections, secure messaging

### [[_content/dictionary#B|Blowfish]] and Twofish
- [[_content/dictionary#B|Blowfish]]: Block cipher with variable key length (32-448 bits)
- Twofish: [[_content/dictionary#A|AES]] finalist with key sizes up to 256 bits
- Both designed by Bruce Schneier
- Used in: Password management tools, file encryption

## Block Cipher Encryption Modes

Block ciphers like [[_content/dictionary#A|AES]] encrypt fixed-size blocks of data (typically 128 or 64 bits). To encrypt larger amounts of data, different modes of operation are used:

### [[_content/dictionary#E|ECB]] (Electronic Codebook)
- Simplest mode: each block is encrypted independently
- **Security issue**: Patterns in the plaintext can show in the ciphertext
- **Usage**: Generally not recommended for secure applications
- **Visual example**: The famous "[[_content/dictionary#E|ECB]] penguin" demonstrates the pattern problem

### [[_content/dictionary#C|CBC]] (Cipher Block Chaining)
- Each block is XORed with the previous ciphertext block before encryption
- Requires an Initialization Vector ([[_content/dictionary#I|IV]]) for the first block
- Each encrypted block depends on all previous blocks
- **Security level**: Good when properly implemented with random IVs
- **Usage**: Was the standard mode for many years

### [[_content/dictionary#C|CTR]] (Counter)
- Turns a block cipher into a stream cipher
- Encrypts a counter value and XORs the result with the plaintext
- Allows parallel encryption/decryption
- **Security level**: Secure when used properly (never reuse counter+key)
- **Usage**: Modern applications, good for performance

### [[_content/dictionary#G|GCM]] (Galois/Counter Mode)
- Combines [[_content/dictionary#C|CTR]] mode with authentication
- Provides both encryption and integrity verification
- **Security level**: Very good when properly implemented
- **Usage**: Modern standard for authenticated encryption ([[_content/dictionary#H|HTTPS]], VPNs)
- **Special property**: Authenticated encryption with associated data ([[_content/dictionary#A|AEAD]])

## Initialization Vectors (IVs)

### What is an [[_content/dictionary#I|IV]]?
- A random or unique value used to ensure the same plaintext encrypts to different ciphertexts
- Typically the size of one block (e.g., 128 bits for [[_content/dictionary#A|AES]])
- Not a secret (usually sent alongside the ciphertext)

### Why IVs Matter
- Prevents patterns in the plaintext from being visible in the ciphertext
- Ensures the same message encrypted twice produces different outputs
- Critical for security in many modes ([[_content/dictionary#C|CBC]], [[_content/dictionary#C|CTR]], [[_content/dictionary#G|GCM]])

### [[_content/dictionary#I|IV]] Requirements by Mode
- **[[_content/dictionary#C|CBC]] mode**: [[_content/dictionary#I|IV]] must be unpredictable (ideally random)
- **[[_content/dictionary#C|CTR]] mode**: [[_content/dictionary#I|IV]] (nonce + counter) must never be reused with the same key
- **[[_content/dictionary#G|GCM]] mode**: [[_content/dictionary#I|IV]] should never be reused with the same key

### [[_content/dictionary#I|IV]] Security Issues
- Reusing an [[_content/dictionary#I|IV]] with the same key can lead to catastrophic security failures
- Predictable IVs in [[_content/dictionary#C|CBC]] mode can enable chosen-plaintext attacks
- [[_content/dictionary#I|IV]] misuse is a common cause of cryptographic vulnerabilities

## Advantages of Symmetric Encryption

1. **Speed**: Much faster than asymmetric encryption
2. **Efficiency**: Requires less computational resources
3. **Strong security**: With proper key length and implementation
4. **Suitable for large data**: Efficient for encrypting large files or streams

## Limitations of Symmetric Encryption

1. **Key distribution problem**: How to securely share the key?
2. **Key management complexity**: Increases with number of users
3. **No built-in authentication**: Basic encryption doesn't verify who sent the message
4. **Scalability issues**: Requires n(n-1)/2 keys for n users to communicate securely

## Common Applications

- **File encryption**: Protecting stored data
- **Database encryption**: Securing sensitive database fields
- **Communication security**: Often used for the bulk data encryption in [[_content/dictionary#T|TLS]]/[[_content/dictionary#S|SSL]]
- **Disk encryption**: [[_content/dictionary#B|BitLocker]], [[_content/dictionary#F|FileVault]], [[_content/dictionary#L|LUKS]]
- **VPNs**: Encrypting network traffic

## Best Practices

1. Use established algorithms ([[_content/dictionary#A|AES]]-256, [[_content/dictionary#C|ChaCha20]])
2. Use appropriate modes ([[_content/dictionary#G|GCM]], [[_content/dictionary#C|CTR]]) with proper [[_content/dictionary#I|IV]] handling
3. Use cryptographic libraries—don't implement algorithms yourself
4. Rotate encryption keys periodically
5. Protect keys in secure storage
6. Combine with proper authentication
7. Consider authenticated encryption modes (GCM) 