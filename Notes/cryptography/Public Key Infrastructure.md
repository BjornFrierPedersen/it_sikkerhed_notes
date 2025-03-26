# Public Key Infrastructure ([[_content/dictionary#P|PKI]])

## Explained in Simple Terms
Public Key Infrastructure ([[_content/dictionary#P|PKI]]) is like a digital passport system that helps verify people's identities online. In the physical world, a government issues passports that confirm your identity. In the digital world, Certificate Authorities ([[_content/dictionary#C|CA]]s) issue digital certificates that confirm a website or person is who they claim to be. [[_content/dictionary#P|PKI]] solves the problem of knowing whether you're really communicating with your bank's website and not an impostor. It creates a chain of trust that helps secure the internet.

## How [[_content/dictionary#P|PKI]] Works

![[[_content/dictionary#P|PKI]] Certificate Authority Process](../images/pki_certificate_authority.md)

As shown in the image above:

### Left Side: Certificate Issuance
1. Alice generates a key pair (private and public keys)
2. The Certificate Authority ([[_content/dictionary#C|CA]]) verifies Alice's identity (e.g., using her passport or other identity documents)
3. The [[_content/dictionary#C|CA]] signs Alice's public key, creating a digital certificate
4. Alice can now share her certificate with Bob
5. Bob trusts the [[_content/dictionary#C|CA]], so he can trust that the public key really belongs to Alice

### Right Side: Certificate Usage
1. Alice signs data using her private key
2. She sends the signed data to Bob
3. Bob verifies the signature using Alice's public key from her certificate
4. Bob trusts the [[_content/dictionary#C|CA]]'s signature on Alice's certificate
5. This establishes a trusted communication channel between Alice and Bob

## Core Components of [[_content/dictionary#P|PKI]]

### Certificate Authority ([[_content/dictionary#C|CA]])
- Trusted third-party organization that issues digital certificates
- Verifies the identity of certificate applicants before issuance
- Signs certificates with its own private key
- Examples: [[_content/dictionary#D|DigiCert]], Comodo, Let's Encrypt, [[_content/dictionary#G|GlobalSign]]

### Digital Certificates
- Electronic documents that bind a public key to an entity (organization, individual, server)
- Contains: public key, identity information, expiration date, issuer information, digital signature of the [[_content/dictionary#C|CA]]
- Most commonly use the [[_content/dictionary#X|X.509]] standard format
- Types: Server certificates, client certificates, code signing certificates, email certificates

### Registration Authority ([[_content/dictionary#R|RA]])
- Optional component that handles the verification of certificate requests
- Performs identity verification on behalf of the [[_content/dictionary#C|CA]]
- Forwards approved requests to the [[_content/dictionary#C|CA]] for certificate issuance

### Certificate Repository
- Public database of issued certificates
- Allows users to retrieve certificates for verification
- Often implemented using [[_content/dictionary#L|LDAP]] directories

### Certificate Revocation List ([[_content/dictionary#C|CRL]])
- List of certificates that have been revoked before their expiration date
- Reasons for revocation: key compromise, [[_content/dictionary#C|CA]] compromise, change of affiliation, certificate replacement
- Published regularly by [[_content/dictionary#C|CA]]s

### Online Certificate Status Protocol ([[_content/dictionary#O|OCSP]])
- Real-time certificate validation protocol
- Alternative to [[_content/dictionary#C|CRL]]s that provides more timely revocation information
- Reduces latency in certificate validation

## Certificate Lifecycle

### 1. Certificate Request
- Applicant generates key pair
- Creates a Certificate Signing Request ([[_content/dictionary#C|CSR]])
- Includes public key and identity information
- Signed with the applicant's private key

### 2. Identity Verification
- [[_content/dictionary#C|CA]] or [[_content/dictionary#R|RA]] verifies the applicant's identity
- Methods vary based on certificate type:
  - Domain validation ([[_content/dictionary#D|DV]]): Prove control of domain
  - Organization validation ([[_content/dictionary#O|OV]]): Verify organization details
  - Extended validation ([[_content/dictionary#E|EV]]): Rigorous verification of legal identity

### 3. Certificate Issuance
- [[_content/dictionary#C|CA]] signs the public key and identity information
- Creates the certificate in [[_content/dictionary#X|X.509]] format
- Delivers to the applicant

### 4. Certificate Usage
- Installed on web servers, email clients, etc.
- Used for secure communications, digital signatures, etc.

### 5. Renewal or Revocation
- Certificates have a limited validity period
- Must be renewed before expiration
- Can be revoked if compromised

## Trust Models in [[_content/dictionary#P|PKI]]

### Hierarchical (Tree) Model
- Single root [[_content/dictionary#C|CA]] at the top
- Intermediate CAs below root
- End-entity certificates at the bottom
- Most common model on the internet

### Web of Trust
- Decentralized model without central authorities
- Users sign each other's certificates
- Used in [[_content/dictionary#P|PGP]]/[[_content/dictionary#G|GPG]] email encryption
- Trust based on network of trusted peers

### Mesh Model
- Multiple CAs cross-sign each other's certificates
- Creates redundancy and multiple trust paths
- Used in some enterprise environments

### Bridge [[_content/dictionary#C|CA]] Model
- Special [[_content/dictionary#C|CA]] connects multiple [[_content/dictionary#P|PKI]] domains
- Allows cross-domain certificate validation
- Used in government and multi-organization settings

## [[_content/dictionary#P|PKI]] Applications

### Secure Web Browsing ([[_content/dictionary#H|HTTPS]])
- [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] certificates secure website connections
- Browsers verify certificate authenticity
- Green padlock indicates valid certificate

### Secure Email
- [[_content/dictionary#S|S/[[_content/dictionary#M|MIME]]]] uses certificates for email signing and encryption
- Provides authentication and confidentiality

### Code Signing
- Software publishers sign code with certificates
- Operating systems verify signatures before execution

### Virtual Private Networks (VPNs)
- Certificate-based authentication for secure remote access
- Stronger than password-based authentication

### Document Signing
- Digital signatures for legal documents
- Non-repudiation for contracts and agreements

### Smart Cards and Authentication
- Certificates stored on physical devices
- Used for secure access to systems and facilities

## [[_content/dictionary#P|PKI]] Security Challenges

### Certificate Authority Compromises
- If a [[_content/dictionary#C|CA]] is compromised, all issued certificates become untrustworthy
- Major incidents: [[_content/dictionary#D|DigiNotar]] (2011), Comodo (2011)
- Requires rapid revocation and reissuance of certificates

### Revocation Challenges
- CRLs can become large and unwieldy
- [[_content/dictionary#O|OCSP]] adds latency and potential privacy concerns
- Some clients may not check revocation status

### Trust Store Management
- Browsers and operating systems maintain lists of trusted root CAs
- Improper management can lead to security vulnerabilities

### Implementation Flaws
- Certificate validation errors in software
- Missing hostname verification
- Improper certificate chain validation

## Best Practices for [[_content/dictionary#P|PKI]] Deployment

### Certificate Management
- Implement automated certificate lifecycle management
- Track certificate expiration dates
- Plan for timely renewals

### Private Key Protection
- Store private keys securely
- Consider hardware security modules (HSMs) for critical keys
- Implement strong access controls

### Validation Procedures
- Always verify the full certificate chain
- Check certificate revocation status
- Validate certificate attributes (domain name, expiration, usage)

### Certificate Policies
- Define clear policies for certificate issuance and use
- Document validation procedures
- Establish incident response procedures for key compromise

### Monitoring and Auditing
- Monitor for unauthorized certificate issuance
- Audit certificate usage
- Implement Certificate Transparency ([[_content/dictionary#C|CT]]) logging

## Future of [[_content/dictionary#P|PKI]]

### Post-Quantum Cryptography
- Preparing for quantum computing threats
- Developing quantum-resistant algorithms
- Transitioning existing [[_content/dictionary#P|PKI]] to new algorithms

### Blockchain-Based [[_content/dictionary#P|PKI]]
- Decentralized certificate management
- Transparent certificate issuance and revocation
- Eliminates single points of failure

### Automated Certificate Management
- Standards like [[_content/dictionary#A|ACME]] protocol (used by Let's Encrypt)
- Reduces human error in certificate deployment
- Enables short-lived certificates 