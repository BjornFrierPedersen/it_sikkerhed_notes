```mermaid
graph [[_content/dictionary#L|LR]]
    %% [[_content/dictionary#E|ECB]] Mode Diagram
    subgraph "Electronic Codebook (ECB) Mode"
        %% Plaintext blocks
        P1["Plaintext Block 1"]
        P2["Plaintext Block 2"]
        P3["Plaintext Block 3"]

        %% Encryption operations
        E1["Encryption"]
        E2["Encryption"]
        E3["Encryption"]

        %% Ciphertext blocks
        C1["Ciphertext Block 1"]
        C2["Ciphertext Block 2"]
        C3["Ciphertext Block 3"]

        %% Key
        K["Key"]

        %% Connections
        P1 --> E1
        P2 --> E2
        P3 --> E3

        K --> E1
        K --> E2
        K --> E3

        E1 --> C1
        E2 --> C2
        E3 --> C3
    end

    %% Styling nodes
    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d
    style P3 fill:#d9f7be,stroke:#389e0d

    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08
    style E3 fill:#f5d8a8,stroke:#d46b08

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96
    style C3 fill:#ffd6e7,stroke:#eb2f96

    style K fill:#ffd666,stroke:#fa8c16
```

## Electronic Codebook ([[_content/dictionary#E|ECB]]) Mode

In [[_content/dictionary#E|ECB]] mode, each plaintext block is independently encrypted using the same key. There is no chaining or dependency between blocks.

**Key properties:**
- The simplest block cipher mode
- Each block is encrypted independently
- Identical plaintext blocks will always produce identical ciphertext blocks
- No initialization vector is required
- Encryption and decryption can be parallelized

**Security considerations:**
- Not recommended for encrypting more than one block of data
- Patterns in the plaintext can be visible in the ciphertext (lacks diffusion)
- Vulnerable to replay attacks where individual blocks can be rearranged
- Generally considered insecure for most applications 