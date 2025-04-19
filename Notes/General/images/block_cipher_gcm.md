```mermaid
graph [[_content/dictionary#T|TD]]
    %% [[_content/dictionary#G|GCM]] Mode Diagram
    subgraph "Galois/Counter Mode (GCM)"
        %% Input components
        [[_content/dictionary#I|IV]]["IV/Nonce"]
        K["Key"]
        P["Plaintext"]
        [[_content/dictionary#A|AAD]]["Additional Authenticated Data"]

        %% [[_content/dictionary#C|CTR]] Mode components (for confidentiality)
        subgraph "Counter Mode (Encryption)"
            CTR0["Counter 0"]
            CTR1["Counter 1"]
            CTR2["Counter 2"]

            E0["Encrypt"]
            E1["Encrypt"]
            E2["Encrypt"]

            Y0["Y0"]
            Y1["Y1"]
            Y2["Y2"]

            XOR1((⊕))
            XOR2((⊕))

            P1["Block 1"]
            P2["Block 2"]

            C1["Ciphertext Block 1"]
            C2["Ciphertext Block 2"]
        end

        %% [[_content/dictionary#G|GHASH]] components (for authentication)
        subgraph "GHASH (Authentication)"
            H["H = E(K, 0)"]

            MUL1[("⊗")]
            MUL2[("⊗")]
            MUL3[("⊗")]
            MUL4[("⊗")]

            XORA1((⊕))
            XORA2((⊕))
            XORA3((⊕))

            A["[[_content/dictionary#A|AAD]] blocks"]
            AAD_LEN["AAD Length"]
            C_LEN["Ciphertext Length"]

            AUTH_XOR((⊕))

            AUTH_TAG["Authentication Tag"]
        end

        %% Final outputs
        [[_content/dictionary#C|CTEXT]]["Ciphertext"]
        [[_content/dictionary#T|TAG]]["Authentication Tag"]

        %% Counter generation
        [[_content/dictionary#I|IV]] --> CTR0
        IV --> CTR1
        IV --> CTR2

        %% Encryption
        K --> E0
        K --> E1
        K --> E2
        K --> H

        CTR0 --> E0
        CTR1 --> E1
        CTR2 --> E2

        E0 --> Y0
        E1 --> Y1
        E2 --> Y2

        P --> P1
        P --> P2

        P1 --> XOR1
        Y1 --> XOR1
        XOR1 --> C1

        P2 --> XOR2
        Y2 --> XOR2
        XOR2 --> C2

        C1 --> [[_content/dictionary#C|CTEXT]]
        C2 --> CTEXT

        %% Authentication calculations
        [[_content/dictionary#A|AAD]] --> A
        A --> XORA1
        XORA1 --> MUL1
        H --> MUL1
        MUL1 --> XORA2

        C1 --> XORA2
        XORA2 --> MUL2
        H --> MUL2
        MUL2 --> XORA3

        C2 --> XORA3
        XORA3 --> MUL3
        H --> MUL3

        AAD_LEN --> AUTH_XOR
        C_LEN --> AUTH_XOR
        MUL3 --> AUTH_XOR
        AUTH_XOR --> MUL4
        H --> MUL4

        Y0 --> AUTH_TAG
        MUL4 --> AUTH_TAG
        AUTH_TAG --> [[_content/dictionary#T|TAG]]
    end

    %% Styling nodes
    style [[_content/dictionary#I|IV]] fill:#bae7ff,stroke:#1890ff
    style K fill:#ffd666,stroke:#fa8c16
    style P fill:#d9f7be,stroke:#389e0d
    style [[_content/dictionary#A|AAD]] fill:#d6e4ff,stroke:#1d39c4

    style CTR0 fill:#bae7ff,stroke:#1890ff
    style CTR1 fill:#bae7ff,stroke:#1890ff
    style CTR2 fill:#bae7ff,stroke:#1890ff

    style E0 fill:#f5d8a8,stroke:#d46b08
    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08

    style Y0 fill:#91caff,stroke:#096dd9
    style Y1 fill:#91caff,stroke:#096dd9
    style Y2 fill:#91caff,stroke:#096dd9

    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96

    style H fill:#ffd666,stroke:#fa8c16

    style AAD_LEN fill:#d6e4ff,stroke:#1d39c4
    style C_LEN fill:#ffd6e7,stroke:#eb2f96

    style A fill:#d6e4ff,stroke:#1d39c4

    style AUTH_TAG fill:#d3adf7,stroke:#722ed1
    style [[_content/dictionary#T|TAG]] fill:#d3adf7,stroke:#722ed1
    style [[_content/dictionary#C|CTEXT]] fill:#ffd6e7,stroke:#eb2f96
```

## Galois/Counter Mode ([[_content/dictionary#G|GCM]])

[[_content/dictionary#G|GCM]] combines Counter ([[_content/dictionary#C|CTR]]) mode for encryption with a Galois field multiplication-based authentication mechanism called [[_content/dictionary#G|GHASH]]. This provides both confidentiality and authentication in a single algorithm.

**Key components:**

1. **Counter Mode Encryption**:
   - Uses a counter value ([[_content/dictionary#I|IV]]/nonce + counter) that is encrypted and XORed with plaintext
   - Provides efficient, parallelizable encryption

2. **[[_content/dictionary#G|GHASH]] Authentication**:
   - Processes both the ciphertext and Additional Authenticated Data ([[_content/dictionary#A|AAD]])
   - Uses Galois field multiplication (⊗) to create an authentication tag
   - The tag authenticates both the encrypted data and any associated data that wasn't encrypted

**Key properties:**
- Provides both confidentiality and integrity/authentication
- Highly efficient and parallelizable in both hardware and software
- Can authenticate additional data that is not encrypted ([[_content/dictionary#A|AAD]])
- Requires a unique [[_content/dictionary#I|IV]] for each message encrypted with the same key
- Widely adopted in protocols like [[_content/dictionary#T|TLS]] 1.2+, [[_content/dictionary#I|IPsec]], and [[_content/dictionary#I|IEEE]] 802.1AE

**Security considerations:**
- Never reuse an [[_content/dictionary#I|IV]] with the same key (catastrophic security failure)
- Considered very secure when implemented correctly
- One of the most widely recommended authenticated encryption modes 