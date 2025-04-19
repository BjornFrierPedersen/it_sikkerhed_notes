```mermaid
graph [[_content/dictionary#T|TD]]
    %% Asymmetric Encryption Diagram
    subgraph "Asymmetric Encryption Flow"
        %% Participants
        Bob["Bob (Sender)"]
        Alice["Alice (Recipient)"]

        %% Keys
        APubKey["Alice's Public Key"]
        APrivKey["Alice's Private Key"]

        %% Message components
        M["Original Message"]
        C["Ciphertext"]
        D["Decrypted Message"]

        %% Operations
        Encrypt["Encryption"]
        Decrypt["Decryption"]

        %% Connections for sending
        Bob --> M
        M --> Encrypt
        APubKey --> Encrypt
        Encrypt --> C
        C --> Alice

        %% Connections for receiving
        Alice --> APrivKey
        APrivKey --> Decrypt
        C --> Decrypt
        Decrypt --> D
    end

    %% Styling nodes
    style Bob fill:#d9f7be,stroke:#389e0d
    style Alice fill:#d9f7be,stroke:#389e0d

    style APubKey fill:#ffd666,stroke:#fa8c16
    style APrivKey fill:#ffa39e,stroke:#cf1322

    style M fill:#d6e4ff,stroke:#1d39c4
    style C fill:#ffd6e7,stroke:#eb2f96
    style D fill:#d6e4ff,stroke:#1d39c4

    style Encrypt fill:#f5d8a8,stroke:#d46b08
    style Decrypt fill:#f5d8a8,stroke:#d46b08
```

## Asymmetric Encryption

Asymmetric encryption (also called public-key cryptography) uses a pair of mathematically related keys:

1. **Public Key**: Shared freely with anyone
2. **Private Key**: Kept secret by the owner

### Process:
- Anyone can encrypt a message using the recipient's public key
- Only the recipient with the matching private key can decrypt the message

### Key Properties:
- **One-way function**: Data encrypted with the public key can only be decrypted with the private key
- **No shared secret**: Sender and receiver don't need to exchange a secret key
- **Key distribution**: Solves the key distribution problem of symmetric encryption
- **Computationally intensive**: Much slower than symmetric encryption

### Security Considerations:
- The recipient has no cryptographic assurance of who sent the message
- Often used together with digital signatures for authentication
- Commonly used to exchange symmetric keys rather than for bulk data encryption
- The security relies on mathematical problems that are computationally difficult to solve (e.g., factoring large primes) 