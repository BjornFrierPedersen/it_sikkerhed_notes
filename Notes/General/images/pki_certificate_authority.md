```mermaid
graph [[_content/dictionary#T|TD]]
    %% [[_content/dictionary#P|PKI]] Certificate Authority Diagram

    subgraph "Certificate Creation & Distribution"
        %% Alice's keys
        APriv["Alice's Private Key"]
        APub["Alice's Public Key"]
        Alice["Alice"]

        %% [[_content/dictionary#C|CA]] components
        CA["Certificate Authority"]
        CAPriv["CA's Private Key"]
        Verify["Identity Verification"]
        Sign["Sign"]

        %% Certificate
        Cert["Alice's Certificate"]

        %% Bob
        Bob["Bob"]

        %% Connections for certificate creation
        Alice -- "generates" --> APriv
        Alice -- "generates" --> APub
        APub --> [[_content/dictionary#C|CA]]
        Alice -- "provides identity proof" --> CA
        CA -- "verifies identity" --> Verify
        Verify --> Sign
        APub --> Sign
        CAPriv --> Sign
        Sign --> Cert

        %% Certificate distribution
        Cert --> Bob
    end

    subgraph "Certificate Usage"
        %% Message components
        M1["Message"]
        SignedM["Signed Message"]

        %% Bob's verification
        [[_content/dictionary#B|BobRecv]]["Bob"]
        CATrust["Trust in [[_content/dictionary#C|CA]]"]
        [[_content/dictionary#C|CertVerify]]["Certificate Verification"]
        [[_content/dictionary#S|SigVerify]]["Signature Verification"]

        %% Results
        [[_content/dictionary#T|TrustAlice]]["Trust Alice's Public Key"]
        Result["Verification Result"]

        %% Connections for certificate usage
        Alice -- "creates" --> M1
        APriv -- "signs" --> M1
        M1 --> SignedM
        SignedM --> [[_content/dictionary#B|BobRecv]]

        [[_content/dictionary#B|BobRecv]] -- "has" --> Cert
        BobRecv -- "has" --> CATrust
        CATrust --> [[_content/dictionary#C|CertVerify]]
        Cert --> CertVerify
        CertVerify --> [[_content/dictionary#T|TrustAlice]]

        SignedM --> [[_content/dictionary#S|SigVerify]]
        [[_content/dictionary#T|TrustAlice]] --> SigVerify
        SigVerify --> Result
    end

    %% Styling nodes
    style Alice fill:#d9f7be,stroke:#389e0d
    style Bob fill:#d9f7be,stroke:#389e0d
    style [[_content/dictionary#B|BobRecv]] fill:#d9f7be,stroke:#389e0d

    style APriv fill:#ffa39e,stroke:#cf1322
    style APub fill:#ffd666,stroke:#fa8c16
    style CAPriv fill:#ffa39e,stroke:#cf1322

    style [[_content/dictionary#C|CA]] fill:#91caff,stroke:#096dd9
    style Verify fill:#f5d8a8,stroke:#d46b08
    style Sign fill:#f5d8a8,stroke:#d46b08

    style Cert fill:#d3adf7,stroke:#722ed1

    style M1 fill:#d6e4ff,stroke:#1d39c4
    style SignedM fill:#ffd6e7,stroke:#eb2f96

    style CATrust fill:#b7eb8f,stroke:#52c41a
    style [[_content/dictionary#C|CertVerify]] fill:#f5d8a8,stroke:#d46b08
    style [[_content/dictionary#S|SigVerify]] fill:#f5d8a8,stroke:#d46b08

    style [[_content/dictionary#T|TrustAlice]] fill:#b7eb8f,stroke:#52c41a
    style Result fill:#b7eb8f,stroke:#52c41a
```

## Public Key Infrastructure ([[_content/dictionary#P|PKI]]) and Certificate Authorities

Public Key Infrastructure ([[_content/dictionary#P|PKI]]) provides a framework for managing digital certificates and public-key encryption. Certificate Authorities (CAs) are trusted entities that validate the identity of certificate holders and issue digital certificates.

### Certificate Creation & Distribution:
1. **Key Generation**: Alice generates her public and private key pair
2. **Identity Verification**: A Certificate Authority verifies Alice's identity through various methods
3. **Certificate Creation**: The [[_content/dictionary#C|CA]] signs Alice's public key with its private key, creating a digital certificate
4. **Certificate Distribution**: Alice can share her certificate with anyone who needs to verify her identity

### Certificate Usage:
1. **Signing**: Alice creates data and signs it with her private key
2. **Sharing**: Alice shares the signed data with Bob
3. **Trust Establishment**: Bob trusts the [[_content/dictionary#C|CA]] that signed Alice's certificate
4. **Certificate Verification**: Bob verifies the CA's signature on Alice's certificate
5. **Message Verification**: Bob uses Alice's public key from the certificate to verify the signature on the data

### Key Components:
- **Certificate Authority ([[_content/dictionary#C|CA]])**: Trusted third party that issues and verifies digital certificates
- **Digital Certificate**: Contains a public key and identity information, signed by a [[_content/dictionary#C|CA]]
- **Certificate Revocation List ([[_content/dictionary#C|CRL]])**: List of certificates that are no longer valid
- **Registration Authority ([[_content/dictionary#R|RA]])**: Handles the verification of user identities for the [[_content/dictionary#C|CA]]
- **Trust Store**: Collection of trusted [[_content/dictionary#C|CA]] certificates

### Applications:
- **Secure Web Browsing ([[_content/dictionary#H|HTTPS]])**: [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] certificates verify website identities
- **Secure Email**: [[_content/dictionary#S|S/[[_content/dictionary#M|MIME]]]] certificates for email signing and encryption
- **Code Signing**: Certificates that verify the authenticity of software
- **[[_content/dictionary#V|VPN]] Authentication**: Certificates used to authenticate VPN connections
- **Document Signing**: Certificates that validate the signer's identity 