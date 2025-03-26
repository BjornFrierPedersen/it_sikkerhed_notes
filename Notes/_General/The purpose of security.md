## Formål: 
- Teknologi understøtter vores processer der gør at de personer der skal arbejde med det, kan opnå deres mål. Altså er vores udgangspunkt at hjælpe mennesker.

### Formel: Risk = Threat * Vulnerability (* Asset) (* Impact)
- Threat actor: The dude who wants to punch you in the face
- Threat: The punch being thrown
- Vulnerability: Your inability to defend against the punch
- Risk: The likelyhood of being punched in the face
- Acceptable risk: Your willingness to being punched in the face

### Handling risks:
- Acceptance: This risk is [[_content/dictionary#O|OK]]. We don't need to care about it.
- Mitigation: Firewall, anti-malware software, encryption, etc. Decrease and actually handle the risk.
- Transfer: Insurance, etc.
- Avoidance: This is to risky, we don't want to do it.

### The three pillars ([[_content/dictionary#C|CIA]] triad)
- Confidentiality: Prevent disclosure to unauthorized access to data
  - Identification (passboard)
  - Authentication (the boarding agent looks at my password)
    - Something you know (password)
    - Something you have (two-factor device)
    - Something you are (fingerprint) 
    - Some**where** you are
  - Authorization (The boarding agent looks up my name in the system)
  - Accountability (The boarding agent registers that I have boarded the plane)
- Integrity: Prevent unauthorized modification
- Availability: Ensure that the information is available. (failover, loadbalancer, etc.)

### Different Perspectives on CIA Priorities

The importance of each pillar in the CIA triad can vary significantly depending on the perspective of different stakeholders. What's most critical for one group may be less important for another, creating tension in security design.

#### Healthcare Information Systems Example

**For Patients (Customers):**
- **Priority: Confidentiality > Integrity > Availability**
- Patients primarily care about keeping their private medical information secret. They want to ensure their diagnoses, treatments, and personal health information remain confidential.
- While data integrity is important (correct diagnoses), and availability matters (access to medical records when needed), privacy concerns typically dominate.

**For Healthcare Providers (Employees):**
- **Priority: Integrity > Availability > Confidentiality**
- Medical professionals need accurate patient information to provide proper care, making integrity the top priority.
- They also need immediate access to medical records during emergencies, making availability critical.
- While they respect confidentiality, it may take third place compared to the immediate clinical needs.

**For Healthcare Organizations (Business):**
- **Priority: Compliance & All Three Balanced**
- Healthcare organizations must balance all three aspects while complying with regulations like HIPAA.
- They face legal and financial penalties for breaches in any of the three areas.
- Their security frameworks typically try to give equal weight to all three principles.

**For Society:**
- **Priority: Availability > Integrity > Confidentiality**
- From a public health perspective, having medical systems available during crises is paramount.
- The integrity of aggregate health data is crucial for research and policy-making.
- While individual confidentiality matters, societal needs during health emergencies may prioritize the other aspects.

This healthcare example demonstrates how the same system requires different security priorities depending on which stakeholder's perspective you consider. Similar variations in CIA priorities can be observed in financial systems, government services, educational institutions, and critical infrastructure.

#### Recommendations for Balancing CIA

When implementing security measures:
1. Consider all stakeholder perspectives
2. Conduct a thorough risk assessment
3. Recognize that CIA priorities may shift based on context and circumstances
4. Document and communicate the security trade-offs to stakeholders
5. Review and adjust security controls as needs and threats evolve

The security triad of Confidentiality, Integrity, and Availability provides a valuable framework for assessing security requirements, but its application must be tailored to the specific needs and priorities of different stakeholders and contexts.

[You can have security without privacy, but you cannot have privacy without security.](https://www.differencebetween.net/technology/internet/difference-between-security-and-privacy/#:~:text=While%20security%20and%20privacy%20are%20interdependent%2C%20security%20can,privacy%20but%20privacy%20cannot%20be%20achieved%20without%20security) 