Source: https://en.wikipedia.org/wiki/Cryptographic_hash_function

## Properties
- Pre-image resistance: Difficult to find any message that matches a given hash value.
- Second pre-image resistance: Difficult to find a different input that matches the hash of a given input.
- Collision resistance: Difficult to find two different messages with the same hash value.

## Applications
- Message integrity: Verifying the integrity of messages and files.
- Digital signatures: Used in signature generation and verification.
- Password hashing: Securely storing passwords by hashing them.
- Proof-of-work: Used in systems like Bitcoin mining to deter service abuses.
- File identification: Identifying files in systems like Git and peer-to-peer networks.

## Hash Function Design
- Merkle–Damgård construction: A common method for building hash functions.
- Wide pipe vs. narrow pipe: Modern hash functions use wide-pipe constructions for better security.

## Cryptographic Hash Algorithms
- [[_content/dictionary#M|MD5]]: Produces a 128-bit digest, but is considered broken.
- [[_content/dictionary#S|SHA]]-1: Produces a 160-bit digest, but is also considered broken.
- [[_content/dictionary#S|SHA]]-2: Includes SHA-256 and SHA-512, widely used and secure.
- [[_content/dictionary#S|SHA]]-3: Released in 2015, based on the [[_content/dictionary#K|Keccak]] algorithm.
- [[_content/dictionary#B|BLAKE2]]: An improved version of [[_content/dictionary#B|BLAKE]], faster than [[_content/dictionary#S|SHA]]-3.

## Attacks on Cryptographic Hash Algorithms
- Length-extension attacks: Vulnerable hash functions include [[_content/dictionary#M|MD5]], [[_content/dictionary#S|SHA]]-1, and SHA-256.
- Attacks on hashed passwords: Brute-force attacks can be mitigated using key derivation functions like [[_content/dictionary#P|PBKDF2]], [[_content/dictionary#B|bcrypt]], and [[_content/dictionary#S|scrypt]].