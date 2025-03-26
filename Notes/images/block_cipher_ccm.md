```mermaid
graph [[_content/dictionary#T|TD]]
    %% [[_content/dictionary#C|CCM]] Mode Diagram

    subgraph "Counter with [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]] ([[_content/dictionary#C|CCM]]) Mode"
        %% Input components
        M["Message/Plaintext"]
        N["Nonce"]
        K["Key"]

        %% [[_content/dictionary#C|CTR]] Mode components (for confidentiality)
        subgraph "CTR Mode (Encryption)"
            CTR1["Counter 1"]
            CTR2["Counter 2"]
            CTR3["Counter n"]

            ECTRL1["Encrypt"]
            ECTRL2["Encrypt"]
            ECTRL3["Encrypt"]

            XOR1((⊕))
            XOR2((⊕))
            XOR3((⊕))

            P1["Block 1"]
            P2["Block 2"]
            P3["Block n"]

            C1["Ciphertext Block 1"]
            C2["Ciphertext Block 2"]
            C3["Ciphertext Block n"]
        end

        %% [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]] components (for authentication)
        subgraph "CBC-MAC (Authentication)"
            IV0["[[_content/dictionary#I|IV]] = 0"]

            B0["Formatted Header"]
            B1["Block 1"]
            B2["Block 2"]
            B3["Block n"]

            E0["Encrypt"]
            E1["Encrypt"]
            E2["Encrypt"]
            E3["Encrypt"]

            XORA1((⊕))
            XORA2((⊕))
            XORA3((⊕))

            T1["Intermediate"]
            T2["Intermediate"]
            T3["Intermediate"]

            T["[[_content/dictionary#M|MAC]] Tag"]
        end

        %% Final outputs
        [[_content/dictionary#C|CT]]["Encrypted Ciphertext"]
        [[_content/dictionary#A|AT]]["Authentication Tag"]

        %% Connections for [[_content/dictionary#C|CTR]] Mode
        K --> ECTRL1
        K --> ECTRL2
        K --> ECTRL3

        CTR1 --> ECTRL1
        CTR2 --> ECTRL2
        CTR3 --> ECTRL3

        ECTRL1 --> XOR1
        ECTRL2 --> XOR2
        ECTRL3 --> XOR3

        M --> P1
        M --> P2
        M --> P3

        P1 --> XOR1
        P2 --> XOR2
        P3 --> XOR3

        XOR1 --> C1
        XOR2 --> C2
        XOR3 --> C3

        C1 --> [[_content/dictionary#C|CT]]
        C2 --> CT
        C3 --> CT

        %% Connections for [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]]
        IV0 --> E0
        K --> E0
        K --> E1
        K --> E2
        K --> E3

        B0 --> E0
        E0 --> T1

        T1 --> XORA1
        B1 --> XORA1
        XORA1 --> E1
        E1 --> T2

        T2 --> XORA2
        B2 --> XORA2
        XORA2 --> E2
        E2 --> T3

        T3 --> XORA3
        B3 --> XORA3
        XORA3 --> E3
        E3 --> T

        T --> [[_content/dictionary#A|AT]]
    end

    %% Styling nodes
    style M fill:#d9f7be,stroke:#389e0d
    style N fill:#bae7ff,stroke:#1890ff
    style K fill:#ffd666,stroke:#fa8c16

    style CTR1 fill:#bae7ff,stroke:#1890ff
    style CTR2 fill:#bae7ff,stroke:#1890ff
    style CTR3 fill:#bae7ff,stroke:#1890ff

    style ECTRL1 fill:#f5d8a8,stroke:#d46b08
    style ECTRL2 fill:#f5d8a8,stroke:#d46b08
    style ECTRL3 fill:#f5d8a8,stroke:#d46b08

    style P1 fill:#d9f7be,stroke:#389e0d
    style P2 fill:#d9f7be,stroke:#389e0d
    style P3 fill:#d9f7be,stroke:#389e0d

    style C1 fill:#ffd6e7,stroke:#eb2f96
    style C2 fill:#ffd6e7,stroke:#eb2f96
    style C3 fill:#ffd6e7,stroke:#eb2f96

    style B0 fill:#d9f7be,stroke:#389e0d
    style B1 fill:#d9f7be,stroke:#389e0d
    style B2 fill:#d9f7be,stroke:#389e0d
    style B3 fill:#d9f7be,stroke:#389e0d

    style E0 fill:#f5d8a8,stroke:#d46b08
    style E1 fill:#f5d8a8,stroke:#d46b08
    style E2 fill:#f5d8a8,stroke:#d46b08
    style E3 fill:#f5d8a8,stroke:#d46b08

    style T1 fill:#d3adf7,stroke:#722ed1
    style T2 fill:#d3adf7,stroke:#722ed1
    style T3 fill:#d3adf7,stroke:#722ed1
    style T fill:#d3adf7,stroke:#722ed1

    style [[_content/dictionary#C|CT]] fill:#ffd6e7,stroke:#eb2f96
    style [[_content/dictionary#A|AT]] fill:#d3adf7,stroke:#722ed1
```

## Counter with [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]] ([[_content/dictionary#C|CCM]]) Mode

[[_content/dictionary#C|CCM]] mode combines two operations:

1. **Counter ([[_content/dictionary#C|CTR]]) Mode** - For confidentiality:
   - Uses a counter (nonce + counter value) that is encrypted and XORed with plaintext blocks
   - Provides encryption of the message

2. **[[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]]** - For authentication:
   - Processes blocks of the message in CBC mode to generate an authentication tag
   - Authenticates both the message and any associated data

The combination provides both confidentiality and integrity protection using a single key. [[_content/dictionary#C|CCM]] is widely used in protocols like [[_content/dictionary#I|IEEE]] 802.11i (WPA2), IPsec, and [[_content/dictionary#T|TLS]].

**Key properties:**
- Provides both confidentiality and authentication
- Uses only a single key for both operations
- Requires a unique nonce for each message encrypted with the same key
- Can authenticate additional data that is not encrypted 