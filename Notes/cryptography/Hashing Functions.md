# Hashing Functions

## Explained in Simple Terms
A hash function is like a digital fingerprinting machine—it takes input of any size (a file, a message, or any data) and produces a fixed-size "fingerprint" (hash) that uniquely represents the original data. If even one tiny bit of the original data changes, the fingerprint changes completely. You can't reverse the process to get the original data from the fingerprint, and it's extremely unlikely that two different inputs will produce the same fingerprint.

## Key Characteristics

### 1. One-Way Function
- It's computationally infeasible to reverse the process and find the original input from the hash value
- This property is known as "pre-image resistance"
- Example: If H(x) = y, it should be extremely difficult to find x given only y

### 2. Deterministic
- The same input will always produce the exact same output hash
- This consistency is essential for verification purposes

### 3. Avalanche Effect
- A small change in the input (even a single bit) should result in a drastically different hash value
- This ensures the hash value doesn't reveal patterns from the original data

### 4. Fixed Output Size
- Regardless of input size (1 byte or 1 terabyte), the output hash has a fixed length
- Common lengths: [[_content/dictionary#M|MD5]] (128 bits), [[_content/dictionary#S|SHA]]-1 (160 bits), [[_content/dictionary#S|SHA]]-256 (256 bits)

### 5. Collision Resistance
- It should be computationally infeasible to find two different inputs that produce the same hash output
- This property is critical for security applications
- As computing power increases, older hash functions may lose this property

## Common Hash Functions

### [[_content/dictionary#M|MD5]] (Message Digest Algorithm 5)
- Produces 128-bit hash values
- **Security status**: Considered cryptographically broken and unsuitable for security applications
- **Usage**: Sometimes still used for non-security purposes like checksums

### [[_content/dictionary#S|SHA]]-1 (Secure Hash Algorithm 1)
- Produces 160-bit hash values
- **Security status**: Considered vulnerable to collision attacks
- **Usage**: Being phased out of security applications

### SHA-2 Family
- Includes [[_content/dictionary#S|SHA]]-224, [[_content/dictionary#S|SHA]]-256, [[_content/dictionary#S|SHA]]-384, [[_content/dictionary#S|SHA]]-512
- **Security status**: Currently considered secure
- **Usage**: Widely used in security applications, digital signatures, [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]]

### SHA-3 Family
- The newest member of the Secure Hash Algorithm family
- Uses a different internal structure (sponge construction) than [[_content/dictionary#S|SHA]]-2
- **Security status**: Currently considered very secure
- **Usage**: Gaining adoption in cryptographic applications

### [[_content/dictionary#B|BLAKE2]], [[_content/dictionary#B|BLAKE3]]
- Modern, high-performance hash functions
- **Security status**: Currently considered secure
- **Usage**: Applications requiring high-speed hashing

## Applications of Hash Functions

### 1. Password Storage
- Systems store hash values of passwords rather than actual passwords
- When a user tries to log in, the entered password is hashed and compared to the stored hash
- Even if the database is compromised, attackers don't get actual passwords

### 2. Data Integrity Checks
- File downloads include hash values to verify the file wasn't corrupted or tampered with
- Software distributors publish hash values so users can verify downloaded packages

### 3. Digital Signatures
- The data being signed is first hashed, then the hash is encrypted with the private key
- Makes signing large documents efficient

### 4. Proof-of-Work Systems
- Cryptocurrency mining often involves finding inputs that produce hash values with specific patterns
- The difficulty of finding such inputs regulates the rate of mining

### 5. Hash Tables
- Data structures that use hash functions to map data to storage locations
- Enables efficient data retrieval

## Security Considerations

### Salt and Pepper
- **Salt**: A random value added to the input before hashing, unique for each input
- **Pepper**: A secret value added to all inputs before hashing
- Both defend against rainbow table attacks and make brute force attacks more difficult

### Slow Hashing / Key Stretching
- Functions like [[_content/dictionary#P|PBKDF2]], [[_content/dictionary#B|bcrypt]], and [[_content/dictionary#A|Argon2]] deliberately slow down the hashing process
- Makes brute-force attacks more time-consuming
- Essential for password hashing

### Common Attacks
- **Collision attacks**: Finding two different inputs with the same hash output
- **Preimage attacks**: Attempting to find an input that hashes to a specific output
- **Rainbow table attacks**: Using precomputed tables of hash values to crack passwords

## Visual Representation
```mermaid
graph [[_content/dictionary#T|TD]]
    A[Input Data] --> B[Hash Function]
    B --> C[Fixed-Size Hash Value]
    D[Different Input] --> B
    B --> E[Completely Different Hash Value]
    F[Input + Small Change] --> B
    B --> G[Completely Different Hash Value]
    style C fill:#afa
    style E fill:#faa
    style G fill:#ffa
```

## Hash Function Comparison Table

| Hash Function | Output Size | Speed | Security Status | Best Use Cases |
|---------------|-------------|-------|----------------|----------------|
| [[_content/dictionary#M|MD5]]           | 128 bits    | Very Fast | Broken | Non-security checksums |
| [[_content/dictionary#S|SHA]]-1         | 160 bits    | Fast | Vulnerable | Legacy systems only |
| SHA-256       | 256 bits    | Moderate | Secure | General cryptographic use |
| SHA-3         | Variable    | Moderate | Very Secure | High-security applications |
| [[_content/dictionary#B|BLAKE2]]        | Variable    | Very Fast | Secure | Performance-critical applications |
| [[_content/dictionary#B|bcrypt]]        | 184 bits    | Deliberately slow | Secure | Password storage |
| [[_content/dictionary#A|Argon2]]        | Variable    | Deliberately slow | Very Secure | Password storage, modern applications |

## Code Example: [[_content/dictionary#S|SHA]]-256 Hash
```python
import hashlib

def calculate_sha256(data):
    """Calculate the [[_content/dictionary#S|SHA]]-256 hash of the input data."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

# Example usage
message = "Hello, World!"
hash_value = calculate_sha256(message)
print(f"Message: {message}")
print(f"[[_content/dictionary#S|SHA]]-256 Hash: {hash_value}")
``` 

Article links:
[[Cryptographic Hash Functions]]