---
title: "Infrastructure as Code Security Cheat Sheet"
source: "[[_content/dictionary#O|OWASP]] Cheatsheet"
source_url: "https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html"
created: "1741872881.9112234"
tags: [owasp, cheatsheet, security]
---
# Infrastructure as Code Security

## Infrastructure as Code Security Cheatsheet[[[[[[[¶](#references)](#runtime)](#deploy)](#develop-and-distribute)](#security-best-practices)](#introduction)](#infrastructure-as-code-security-cheatsheet)
### Introduction¶
Infrastructure as code ([[_content/dictionary#I|IaC]]), also known as software-defined infrastructure, allows the configuration and deployment of infrastructure components faster with consistency by allowing them to be defined as a code and also enables repeatable deployments across environments.
#### Security best practices¶
Here are some of the security best practices for IaC that can be easily integrated into the Software Development Lifecycle:
#### Develop and Distribute¶

- IDE plugins - Leverage standard security plug-ins in the integrated development environment (IDE) which helps in the early detection of potential risks and drastically reduces the time to address any issues later in the development cycle. Plugins such as TFLint, Checkov, Docker Linter, docker-vulnerability-extension, Security Scan, Contrast Security, etc., help in the security assessment of the [[_content/dictionary#I|IaC]].
- Threat modelling - Build the threat modelling landscape earlier in the development cycle to ensure there is enough visibility of the high-risk, high-volume aspects of the code and flexibility to include security throughout to ensure the assets are safely managed.
Managing secrets -  Secrets are confidential data and information such as application tokens required for authentication, passwords, and [[_content/dictionary#S|SSH]] (Secure Shell) keys. The problem is not the secrets, but where you store them. If you are using a simple text file or SCMs like Git, then the secrets can be easily exposed. Open-source tools such as truffleHog, git-secrets, [[_content/dictionary#G|GitGuardian]] and similar can be utilized to detect such vulnerable management of secrets. See the [[Secrets_Management_Cheat_Sheet|Secrets Management Cheat Sheet]] for more information.
- Version control - Version control is the practice of tracking and managing changes to software code. Ensure all the changes to the [[_content/dictionary#I|IaC]] are tracked with the right set of information that helps in any revert operation. The important part is that you’re checking in those changes alongside the features they support and not separately. A feature’s infrastructure requirements should be a part of a feature’s branch or merge request. Git is generally used as the source code version control system.

- Principle of least privilege - define the access management policies based on the principle of least privilege with the following priority items:

- - Defining who is and is not authorized to create/update/run/delete the scripts and inventory.
- - Limiting the permissions of authorized [[_content/dictionary#I|IaC]] users to what is necessary to perform their tasks. The IaC scripts should ensure that the permissions granted to the various resources it creates are limited to what is required for them to perform their work.

- Static analysis - Analyzes code in isolation, identifying risks, misconfigurations, and compliance faults only relevant to the [[_content/dictionary#I|IaC]] itself. Tools such as kubescan, Snyk, Coverity etc, can be leveraged for static analysis of IaC.

- Open Source dependency check - Analyzes the open source dependencies such as [[_content/dictionary#O|OS]] packages, libraries, etc., to identify potential risks. Tools such as [[_content/dictionary#B|BlackDuck]], Snyk, [[_content/dictionary#W|WhiteSource]] Bolt for [[_content/dictionary#G|GitHub]], and similar can be leveraged for open source dependency analysis of [[_content/dictionary#I|IaC]].
- Container image scan - Image scanning refers to the process of analyzing the contents and the build process of a container image in order to detect security issues, vulnerabilities or potential risks. Open-source tools such as Dagda, Clair, Trivy, Anchore, etc., can be leveraged for container image analysis.
[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]] pipeline and Consolidated reporting - enabling the security checks to be made available in the [[_content/dictionary#C|[[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]]]] pipeline enables the analysis of each of the code changes, excludes the need for manual intervention, and enables maintaining the history of compliance. Along with consolidated reporting, these integrations enhance the speed of development of a secure IaC codebase. Open-source tools such as Jenkins, etc., can be leveraged to build the [[_content/dictionary#C|CI]]/[[_content/dictionary#C|CD]] pipelines, and [[_content/dictionary#D|DefectDojo]] and [[_content/dictionary#O|OWASP]] Glue can help in tying the checks together and visualizing the check results in a single dashboard.
- Artifact signing - Digital signing of artifacts at build time and validation of the signed data before use protects artifacts from tampering between build and runtime, thus ensuring the integrity and provenance of an artifact. Open-source tools such as [[_content/dictionary#T|TUF]] helps in the digital signing of artifacts.

#### Deploy¶

- Inventory management:
- - Commissioning - whenever a resource is deployed, ensure the resource is labeled, tracked and logged as part of the inventory management.
- - Decommissioning - whenever a resource deletion is initiated, ensure the underlying configurations are erased, data is securely deleted and the resource is completely removed from the runtime as well as from the inventory management.
- - Tagging - It is essential to tag cloud assets properly. During [[_content/dictionary#I|IaC]] operations, untagged assets are most likely to result in ghost resources that make it difficult to detect, visualize, and gain observability within the cloud environment and can affect the posture causing a drift. These ghost resources can add to billing costs, make maintenance difficult, and affect the reliability. The only solution to this is careful tagging and monitoring for untagged resources.

- Dynamic analysis - Dynamic analysis helps in evaluating any existing environments and services that it will interoperate with or run on. This helps in uncovering potential risks due to the interoperability. Open-source tools such as [[_content/dictionary#Z|ZAP]], Burp, [[_content/dictionary#G|GVM]], etc., can be leveraged for dynamic analysis.

#### Runtime¶

- Immutability of infrastructure - The idea behind immutable infrastructure is to build the infrastructure components to an exact set of specifications. No deviation, no changes. If a change to a specification is required, then a whole new set of infrastructure is provisioned based on the updated requirements, and the previous infrastructure is taken out of service as obsolete.
- Logging - Keeping a record is a critical aspect to keeping an eye on risks. You should enable logging - both security logs and audit logs - while provisioning infrastructure, as they help assess the security risks related to sensitive assets. They also assist in analyzing the root cause of incidents and in identifying potential threats. Open-source tools such as [[_content/dictionary#E|ELK]], etc., can be leveraged for log analysis.
- Monitoring - Continuous monitoring assists in looking out for any security and compliance violations, helps in identifying attacks and also provides alerts upon such incidents. Certain solutions also incorporate new technologies like [[_content/dictionary#A|AI]] to identify potential threats early. Open-source tools such as Prometheus, Grafana, etc., can be leveraged for monitoring of cloud infrastructure.
- Runtime threat detection: Implementing a runtime threat detection solution helps in recognizing unexpected application behavior and alerts on threats at runtime. Open-source tools such as Falco, etc., can be leveraged for runtime threat detection. Certain application such as Contrast (Contrast Community Edition) can also detect [[_content/dictionary#O|OWASP]] Top 10 attacks on the application during runtime and help block them in order to protect and secure the application.

### References¶

Securing Infrastructure as code: [https://www.opcito.com/blogs/securing-infrastructure-as-code](https://www.opcito.com/blogs/securing-infrastructure-as-code)
Infrastructure as code security: [https://dzone.com/articles/infrastructure-as-code-security](https://dzone.com/articles/infrastructure-as-code-security)
Shifting cloud security left with infrastructure as code: [https://securityboulevard.com/2020/04/shifting-cloud-security-left-with-infrastructure-as-code/](https://securityboulevard.com/2020/04/shifting-cloud-security-left-with-infrastructure-as-code/)