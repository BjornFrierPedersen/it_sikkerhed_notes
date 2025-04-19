# A04:2021 - Insecure Design

## Description
Insecure Design is a new category for 2021 that focuses on risks related to design and architectural flaws. Unlike implementation flaws which can be fixed by perfect coding, an insecure design cannot be fixed by perfect implementation because the necessary security controls were never planned for in the first place. 

This category emphasizes the importance of secure design patterns, threat modeling, and reference architectures, highlighting the need to "shift left" and incorporate security considerations earlier in the [[_content/dictionary#S|SDLC]].

## Common Vulnerabilities
1. Missing or ineffective control design
2. Lack of business risk profiling
3. Failure to determine the protection needs of the application
4. Failure to model threats and identify attack vectors
5. Insufficient security requirements
6. Insecure authentication mechanisms
7. Business logic flaws that can be exploited
8. Inadequate access control design
9. Assuming security can be added later in development

## Prevention
1. Establish and use a secure development lifecycle with security professionals
2. Use secure design patterns, components, and reference architectures
3. Conduct threat modeling for critical authentication, access control, business logic, and key flows
4. Integrate security language and controls into user stories
5. Write unit and integration tests to validate critical security controls
6. Segment application layers and network boundaries based on exposure and protection needs
7. Limit resource consumption by user or service
8. Develop security requirements based on threat modeling and business needs

## Impact
The impact of insecure design can be severe, as it often leads to systemic problems that affect multiple parts of an application. Business impacts can include complete system compromise, data theft, regulatory violations, and reputational damage. 