# [[_content/dictionary#S|STRIDE]] Threat Modeling Framework

[[_content/dictionary#S|STRIDE]] is a threat modeling framework developed by Microsoft that categorizes security threats into six distinct categories. This diagram illustrates the relationship between the STRIDE categories and the security properties they violate.

```mermaid
classDiagram
    class [[_content/dictionary#S|STRIDE]] {
        A threat modeling framework
        Systematically identifies security threats
        Developed by Microsoft
    }

    class Spoofing {
        Example: Stealing authentication tokens
        Mitigation: Multi-factor authentication
    }

    class Tampering {
        Example: Modifying data in transit or storage
        Mitigation: Digital signatures, input validation
    }

    class Repudiation {
        Example: Manipulating logs to hide actions
        Mitigation: Secure logging and auditing
    }

    class Information_Disclosure {
        Example: Data leakage from database
        Mitigation: Encryption, access controls
    }

    class Denial_of_Service {
        Example: Overwhelming system with requests
        Mitigation: Rate limiting, load balancing
    }

    class Elevation_of_Privilege {
        Example: Modifying tokens to gain admin rights
        Mitigation: Principle of least privilege
    }

    class Authenticity {
        Users are who they claim to be
    }

    class Integrity {
        Data is complete and accurate
        No unauthorized modifications
    }

    class Non_repudiability {
        Actions cannot be denied
        All activities can be traced
    }

    class Confidentiality {
        Data is only accessible to authorized users
        Protected from unauthorized disclosure
    }

    class Availability {
        Systems are operational when needed
        Resources accessible when required
    }

    class Authorization {
        Users can only access what they're permitted to
        Proper access control enforcement
    }

    [[_content/dictionary#S|STRIDE]] --> Spoofing
    STRIDE --> Tampering
    STRIDE --> Repudiation
    STRIDE --> Information_Disclosure
    STRIDE --> Denial_of_Service
    STRIDE --> Elevation_of_Privilege

    Spoofing --> Authenticity : violates
    Tampering --> Integrity : violates
    Repudiation --> Non_repudiability : violates
    Information_Disclosure --> Confidentiality : violates
    Denial_of_Service --> Availability : violates
    Elevation_of_Privilege --> Authorization : violates
```

## [[_content/dictionary#S|STRIDE]] Categories Explained

| Category | Violates | Description | Example | Mitigation |
|----------|----------|-------------|---------|------------|
| **S**poofing | Authenticity | Illegally accessing and using another user's authentication information | Stealing authentication tokens to impersonate a user | Multi-factor authentication, strong credential management |
| **T**ampering | Integrity | Malicious modification of data in transit, storage, or memory | Modifying database records or intercepting and changing network traffic | Digital signatures, input validation, checksums |
| **R**epudiation | Non-repudiability | Ability to deny performing an action without others being able to prove otherwise | Manipulating logs to hide malicious actions | Secure logging and auditing, digital signatures, timestamps |
| **I**nformation Disclosure | Confidentiality | Exposing information to unauthorized individuals | Data leakage from databases or improper error messages | Encryption, proper access controls, data minimization |
| **D**enial of Service | Availability | Attacks that deny service to valid users | Overwhelming a system with requests to make it unavailable | Rate limiting, resource quotas, load balancing |
| **E**levation of Privilege | Authorization | Gaining access intended for higher-privileged users | Modifying a JWT token to obtain admin rights | Principle of least privilege, proper access control checks |

## Implementation in Threat Modeling Process

When conducting threat modeling with [[_content/dictionary#S|STRIDE]]:

1. Create a data flow diagram ([[_content/dictionary#D|DFD]]) of your system
2. Identify trust boundaries where data crosses security domains
3. For each element in the DFD, systematically consider each [[_content/dictionary#S|STRIDE]] category
4. Document and prioritize threats based on risk assessment
5. Develop mitigations for each identified threat
6. Validate that mitigations effectively address the threats 