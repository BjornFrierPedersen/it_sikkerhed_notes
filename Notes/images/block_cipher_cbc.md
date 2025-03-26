[[[_content/dictionary#T|THIS]] [[_content/dictionary#I|IS]] [[_content/dictionary#A|AN]] [[_content/dictionary#I|IMAGE]]: Cipher Block Chaining ([[_content/dictionary#C|CBC]]) mode diagram showing how each plaintext block is XORed with the previous ciphertext block before encryption. The first block uses an Initialization Vector ([[_content/dictionary#I|IV]]). The diagram shows the sequential nature of encryption, with each block depending on the result of the previous block.] 

```mermaid
graph [[_content/dictionary#L|LR]]
    %% [[_content/dictionary#C|CBC]] Mode Diagram
    subgraph "CBC Mode Encryption"
        P1["Plaintext Block 1"] 
        P2["Plaintext Block 2"]
        P3["Plaintext Block 3"]

        [[_content/dictionary#I|IV]]["Initialization Vector (IV)"]

        E1["Encryption"]
        E2["Encryption"]
        E3["Encryption"]

        XOR1((⊕))
        XOR2((⊕))
        XOR3((⊕))

        C1["Ciphertext Block 1"]
        C2["Ciphertext Block 2"]
        C3["Ciphertext Block 3"]

        [[_content/dictionary#I|IV]] -->|"IV"| XOR1
        P1 --> XOR1
        XOR1 --> E1
        E1 --> C1

        C1 -->|"Previous Ciphertext"| XOR2
        P2 --> XOR2
        XOR2 --> E2
        E2 --> C2

        C2 -->|"Previous Ciphertext"| XOR3
        P3 --> XOR3
        XOR3 --> E3
        E3 --> C3
    end

    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d
    style P3 fill:#d9f7be,stroke:#389e0d

    style [[_content/dictionary#I|IV]] fill:#bae7ff,stroke:#1890ff

    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08
    style E3 fill:#f5d8a8,stroke:#d46b08

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96
    style C3 fill:#ffd6e7,stroke:#eb2f96
```

## Cipher Block Chaining ([[_content/dictionary#C|CBC]]) Mode

In [[_content/dictionary#C|CBC]] mode, each plaintext block is XORed with the previous ciphertext block before encryption. The first block uses an Initialization Vector ([[_content/dictionary#I|IV]]). This sequential nature of encryption means each block depends on the result of all previous blocks.

**Key properties:**
- The same plaintext blocks will encrypt to different ciphertext blocks
- Errors in one ciphertext block affect the decryption of that block and the next block
- Requires a random, unpredictable [[_content/dictionary#I|IV]] for security
- Encryption cannot be parallelized, but decryption can 