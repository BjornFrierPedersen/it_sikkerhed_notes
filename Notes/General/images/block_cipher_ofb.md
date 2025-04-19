```mermaid
graph [[_content/dictionary#L|LR]]
    %% [[_content/dictionary#O|OFB]] Mode Diagram
    subgraph "Output Feedback (OFB) Mode"
        %% Input components
        [[_content/dictionary#I|IV]]["Initialization Vector (IV)"]
        K["Key"]

        %% Encryption operations
        E1["Encryption"]
        E2["Encryption"]
        E3["Encryption"]

        %% Keystream blocks
        KS1["Keystream 1"]
        KS2["Keystream 2"]
        KS3["Keystream 3"]

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

        %% Connections for keystream generation
        [[_content/dictionary#I|IV]] --> E1
        K --> E1
        K --> E2
        K --> E3

        E1 --> KS1
        KS1 --> E2
        E2 --> KS2
        KS2 --> E3
        E3 --> KS3

        %% Connections for encryption
        KS1 --> XOR1
        P1 --> XOR1
        XOR1 --> C1

        KS2 --> XOR2
        P2 --> XOR2
        XOR2 --> C2

        KS3 --> XOR3
        P3 --> XOR3
        XOR3 --> C3
    end

    %% Styling nodes
    style [[_content/dictionary#I|IV]] fill:#bae7ff,stroke:#1890ff
    style K fill:#ffd666,stroke:#fa8c16

    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08
    style E3 fill:#f5d8a8,stroke:#d46b08

    style KS1 fill:#91caff,stroke:#096dd9
    style KS2 fill:#91caff,stroke:#096dd9
    style KS3 fill:#91caff,stroke:#096dd9

    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d
    style P3 fill:#d9f7be,stroke:#389e0d

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96
    style C3 fill:#ffd6e7,stroke:#eb2f96
```

## Output Feedback ([[_content/dictionary#O|OFB]]) Mode

In [[_content/dictionary#O|OFB]] mode, an Initialization Vector ([[_content/dictionary#I|IV]]) is encrypted with the block cipher, and the output is both fed back for the next block's input and XORed with plaintext to create ciphertext. This generates a keystream that is independent of both the plaintext and ciphertext.

**Key properties:**
- Transforms a block cipher into a synchronous stream cipher
- The keystream is generated independently of the plaintext and ciphertext
- No padding is required (can encrypt data of any length)
- Both encryption and decryption use the same process ([[_content/dictionary#X|XOR]] with keystream)
- The entire keystream can be pre-computed given the key and [[_content/dictionary#I|IV]]

**Security considerations:**
- Requires a unique [[_content/dictionary#I|IV]] for each message encrypted with the same key
- [[_content/dictionary#I|IV]] should never be reused with the same key
- Bit flipping attacks are possible without authentication
- Errors in transmission only affect the corresponding bits in the decrypted plaintext (no error propagation)
- Should be used with an authentication mechanism (like [[_content/dictionary#H|HMAC]]) 