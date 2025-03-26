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

[You can have security without privacy, but you cannot have privacy without security.](https://www.differencebetween.net/technology/internet/difference-between-security-and-privacy/#:~:text=While%20security%20and%20privacy%20are%20interdependent%2C%20security%20can,privacy%20but%20privacy%20cannot%20be%20achieved%20without%20security) 