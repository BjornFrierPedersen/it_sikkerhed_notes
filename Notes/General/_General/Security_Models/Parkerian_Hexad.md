# Parkerian Hexad

## Overview

The Parkerian Hexad is an expanded information security model developed by Donn B. Parker that builds upon the traditional [[_content/dictionary#C|CIA]] Triad (Confidentiality, Integrity, Availability) by adding three additional attributes. This model provides a more comprehensive framework for evaluating and protecting information security.

## The Six Components

The Parkerian Hexad consists of the following six elements:

### 1. Confidentiality
Protection from unauthorized disclosure or access to information. This involves ensuring that only authorized individuals can view sensitive information and that data is not revealed to unauthorized parties.

Key aspects:
- Access controls and authorization mechanisms
- Encryption of data at rest and in transit
- Data classification
- Privacy protection

### 2. Integrity
Assurance that information remains accurate, complete, and unchanged by unauthorized modifications. This ensures that data can be trusted and has not been improperly altered.

Key aspects:
- Data validation
- Change management
- Checksums and hash functions
- Digital signatures

### 3. Availability
Ensuring that information and resources are accessible to authorized users when needed. This requires systems to be operational and usable, with minimal downtime or service interruptions.

Key aspects:
- Redundancy and fault tolerance
- Backup and recovery systems
- Disaster recovery planning
- Protection against denial-of-service attacks

### 4. Authenticity
Verification that information is genuine and from the claimed source. This ensures that users can trust the origin of data and communications.

Key aspects:
- Authentication mechanisms
- Digital certificates
- Non-repudiation
- Source verification

### 5. Possession (or Control)
Maintaining physical control over information assets and preventing unauthorized individuals from obtaining the data, regardless of whether they can read or understand it.

Key aspects:
- Physical security measures
- Asset management
- Media controls
- Chain of custody for information

### 6. Utility
Ensuring that information is in a format that allows authorized users to use it for its intended purpose. Data must not only be available and accurate but also usable.

Key aspects:
- Data format standardization
- Information architecture
- User experience design
- Compatibility and interoperability

## Comparison with the CIA Triad

While the CIA Triad has been the traditional foundation of information security, the Parkerian Hexad provides a more comprehensive approach:

| CIA Triad | Parkerian Hexad |
|-----------|-----------------|
| Confidentiality | Confidentiality |
| Integrity | Integrity |
| Availability | Availability |
| - | Authenticity |
| - | Possession/Control |
| - | Utility |

## Practical Applications

The Parkerian Hexad can be used in:

1. **Risk Assessment**: Evaluating threats and vulnerabilities across all six attributes provides a more thorough risk analysis.
2. **Security Architecture**: Designing systems with controls that address all six elements.
3. **Security Policies**: Developing comprehensive policies that cover all aspects of information security.
4. **Incident Response**: Classifying and responding to security incidents based on which attributes were compromised.
5. **Compliance**: Mapping regulatory requirements to specific attributes of the Hexad.

## Example Scenarios

### Scenario 1: Data Breach
A data breach might compromise:
- **Confidentiality**: Unauthorized access to sensitive data
- **Possession**: Loss of control over who has the data
- While potentially not affecting the other attributes

### Scenario 2: Data Corruption
Data corruption might compromise:
- **Integrity**: Data is altered from its original state
- **Utility**: Data may no longer be usable for its intended purpose
- While not necessarily affecting confidentiality or possession

### Scenario 3: Service Outage
A system outage might compromise:
- **Availability**: Users cannot access the system
- **Utility**: Even if data exists, it cannot be used
- While not affecting confidentiality, integrity, or authenticity

## Implementing the Parkerian Hexad

When implementing information security controls based on the Parkerian Hexad, organizations should:

1. Consider all six attributes in security planning and design
2. Map threats and vulnerabilities to specific attributes
3. Implement controls that address each attribute
4. Monitor and measure security effectiveness across all six elements
5. Maintain awareness that a comprehensive security approach requires attention to all attributes

## Conclusion

The Parkerian Hexad provides a more nuanced and complete view of information security than the traditional CIA Triad. By considering authenticity, possession, and utility alongside confidentiality, integrity, and availability, organizations can develop more robust security programs that address the full spectrum of information security requirements. 