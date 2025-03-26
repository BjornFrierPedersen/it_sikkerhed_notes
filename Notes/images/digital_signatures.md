```mermaid
graph [[_content/dictionary#T|TD]]
    %% Digital Signatures Diagram

    subgraph "Digital Signature Process"
        subgraph "Signing Process (Alice)"
            %% Inputs
            M1["Message"]
            APriv["Alice's Private Key"]

            %% Operations
            Hash1["Hash Function"]
            Sign["Sign"]

            %% Outputs
            H1["Message Hash"]
            Sig["Signature"]

            %% Connections
            M1 --> Hash1
            Hash1 --> H1
            H1 --> Sign
            APriv --> Sign
            Sign --> Sig
        end

        %% Transfer
        M2["Message"] 
        Transfer["⟹"]

        subgraph "Verification Process (Bob)"
            %% Inputs
            M3["Message"]
            [[_content/dictionary#R|ReceivedSig]]["Signature"]
            APub["Alice's Public Key"]

            %% Operations
            Hash2["Hash Function"]
            Verify["Verify"]
            Compare["Compare"]

            %% Outputs
            H2["Message Hash"]
            [[_content/dictionary#D|DecSig]]["Decrypted Signature"]
            Result["Verification Result"]

            %% Connections
            M3 --> Hash2
            Hash2 --> H2
            H2 --> Compare

            [[_content/dictionary#R|ReceivedSig]] --> Verify
            APub --> Verify
            Verify --> [[_content/dictionary#D|DecSig]]
            DecSig --> Compare
            Compare --> Result
        end

        %% Connect the subgraphs
        M1 --> M2
        Sig --> [[_content/dictionary#R|ReceivedSig]]
        M2 --> M3
    end

    %% Styling nodes
    style M1 fill:#d6e4ff,stroke:#1d39c4
    style M2 fill:#d6e4ff,stroke:#1d39c4
    style M3 fill:#d6e4ff,stroke:#1d39c4

    style APriv fill:#ffa39e,stroke:#cf1322
    style APub fill:#ffd666,stroke:#fa8c16

    style Hash1 fill:#f5d8a8,stroke:#d46b08
    style Hash2 fill:#f5d8a8,stroke:#d46b08

    style H1 fill:#d3adf7,stroke:#722ed1
    style H2 fill:#d3adf7,stroke:#722ed1

    style Sign fill:#f5d8a8,stroke:#d46b08
    style Verify fill:#f5d8a8,stroke:#d46b08

    style Sig fill:#ffd6e7,stroke:#eb2f96
    style [[_content/dictionary#R|ReceivedSig]] fill:#ffd6e7,stroke:#eb2f96
    style [[_content/dictionary#D|DecSig]] fill:#d3adf7,stroke:#722ed1

    style Compare fill:#91caff,stroke:#096dd9
    style Result fill:#b7eb8f,stroke:#52c41a
```

## Digital Signatures

Digital signatures provide authentication, non-repudiation, and integrity for digital messages or documents. They are the electronic equivalent of handwritten signatures but offer much stronger security guarantees.

### Signing Process (By Alice):
1. **Hashing**: The message is processed through a cryptographic hash function to produce a fixed-size hash value
2. **Signing**: The hash is encrypted using Alice's private key to create the signature
3. **Attachment**: The original message and the signature are sent together

### Verification Process (By Bob):
1. **Hashing**: Bob computes the hash of the received message using the same hash function
2. **Signature Verification**: Bob decrypts the signature using Alice's public key to recover the original hash
3. **Comparison**: Bob compares the computed hash with the hash recovered from the signature
4. **Result**: If they match, the signature is valid; the message hasn't been altered and came from Alice

### Key Properties:
- **Authentication**: Verifies the sender's identity
- **Non-repudiation**: Sender cannot deny having sent the message
- **Integrity**: Detects any changes to the message after signing
- **No confidentiality**: Does not encrypt the message content (can be combined with encryption if needed)

### Applications:
- Software distribution (code signing)
- Email security ([[_content/dictionary#S|S/[[_content/dictionary#M|MIME]]]], [[_content/dictionary#P|PGP]])
- Digital certificates
- Document signing
- Financial transactions 