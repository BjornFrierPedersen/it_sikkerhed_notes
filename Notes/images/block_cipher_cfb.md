```mermaid
graph [[_content/dictionary#L|LR]]
    %% [[_content/dictionary#C|CFB]] Mode Diagram
    subgraph "Cipher Feedback (CFB) Mode"
        %% Input components
        [[_content/dictionary#I|IV]]["Initialization Vector (IV)"]
        K["Key"]

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

        %% Connections for encryption
        [[_content/dictionary#I|IV]] --> E1
        K --> E1
        K --> E2
        K --> E3

        %% First block
        E1 --> XOR1
        P1 --> XOR1
        XOR1 --> C1

        %% Second block
        C1 --> E2
        E2 --> XOR2
        P2 --> XOR2
        XOR2 --> C2

        %% Third block
        C2 --> E3
        E3 --> XOR3
        P3 --> XOR3
        XOR3 --> C3
    end

    %% Styling nodes
    style [[_content/dictionary#I|IV]] fill:#bae7ff,stroke:#1890ff
    style K fill:#ffd666,stroke:#fa8c16

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

## Cipher Feedback ([[_content/dictionary#C|CFB]]) Mode

In [[_content/dictionary#C|CFB]] mode, the previous ciphertext block is encrypted with the block cipher, and the result is XORed with the current plaintext block to produce the current ciphertext block. The first block uses an Initialization Vector ([[_content/dictionary#I|IV]]).

**Key properties:**
- Transforms a block cipher into a self-synchronizing stream cipher
- Each encryption operation depends on all previous ciphertext blocks
- Similar plaintext blocks will encrypt to different ciphertext blocks
- No padding is required (can encrypt data of any length)
- Encryption cannot be parallelized, but decryption can

**Security considerations:**
- Requires a random, unpredictable [[_content/dictionary#I|IV]] for security
- Errors in one ciphertext block affect decryption of that block and a few subsequent blocks (self-healing)
- Bit flipping attacks are possible without authentication
- Often used with an authentication mechanism (like [[_content/dictionary#H|HMAC]]) 