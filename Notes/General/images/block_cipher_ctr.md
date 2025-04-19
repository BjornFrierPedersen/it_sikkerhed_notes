```mermaid
graph [[_content/dictionary#L|LR]]
    %% [[_content/dictionary#C|CTR]] Mode Diagram
    subgraph "Counter (CTR) Mode"
        %% Input components
        N["Nonce"]
        K["Key"]

        %% Counter values
        CTR1["Counter 1"]
        CTR2["Counter 2"]
        CTR3["Counter 3"]

        %% Encryption operations
        E1["Encryption"]
        E2["Encryption"]
        E3["Encryption"]

        %% [[_content/dictionary#X|XOR]] operations
        XOR1((⊕))
        XOR2((⊕))
        XOR3((⊕))

        %% Plaintext blocks
        P1["Plaintext Block 1"]
        P2["Plaintext Block 2"]
        P3["Plaintext Block 3"]

        %% Ciphertext blocks
        C1["Ciphertext Block 1"]
        C2["Ciphertext Block 2"]
        C3["Ciphertext Block 3"]

        %% Connections for counter generation
        N --> CTR1
        N --> CTR2
        N --> CTR3

        %% Connections for encryption
        CTR1 --> E1
        CTR2 --> E2
        CTR3 --> E3

        K --> E1
        K --> E2
        K --> E3

        %% Connections for [[_content/dictionary#X|XOR]]
        E1 --> XOR1
        E2 --> XOR2
        E3 --> XOR3

        P1 --> XOR1
        P2 --> XOR2
        P3 --> XOR3

        %% Connections to ciphertext
        XOR1 --> C1
        XOR2 --> C2
        XOR3 --> C3
    end

    %% Styling nodes
    style N fill:#bae7ff,stroke:#1890ff
    style K fill:#ffd666,stroke:#fa8c16

    style CTR1 fill:#bae7ff,stroke:#1890ff
    style CTR2 fill:#bae7ff,stroke:#1890ff
    style CTR3 fill:#bae7ff,stroke:#1890ff

    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08
    style E3 fill:#f5d8a8,stroke:#d46b08

    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d
    style P3 fill:#d9f7be,stroke:#389e0d

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96
    style C3 fill:#ffd6e7,stroke:#eb2f96
```

## Counter ([[_content/dictionary#C|CTR]]) Mode

In [[_content/dictionary#C|CTR]] mode, a counter value (typically composed of a nonce plus an incrementing counter) is encrypted with the block cipher, and then the result is XORed with the plaintext to produce the ciphertext.

**Key properties:**
- Effectively turns a block cipher into a stream cipher
- No need for padding since it can encrypt any number of bits
- Both encryption and decryption can be performed in parallel
- The same algorithm is used for both encryption and decryption ([[_content/dictionary#X|XOR]] operation is symmetric)
- Random access to encrypted data (can decrypt any block independently)

**Security considerations:**
- Requires a unique counter for each block encrypted with the same key
- Counter values must never be reused with the same key
- No inherent authentication (often combined with a [[_content/dictionary#M|MAC]] for integrity/authentication)
- Generally considered secure when implemented correctly 