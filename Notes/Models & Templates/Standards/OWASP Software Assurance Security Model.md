# Software Assurance Maturity Model ([[_content/dictionary#S|SAMM]])

## [[_content/dictionary#T|TL]];[[_content/dictionary#D|DR]]

[[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] is a framework that helps organizations evaluate and improve their software security practices. It consists of 5 business functions (Governance, Design, Implementation, Verification, Operations), each containing 3 security practices, for a total of 15 practices. Each practice has 3 maturity levels with specific activities and objectives. SAMM is measurable, actionable, and adaptable to organizations of all sizes and types. The framework guides organizations to assess their current security posture, define improvement targets, and create a roadmap to reach those targets, all while balancing security with business needs.

## What is [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]]?

[[_content/dictionary#S|SAMM]] stands for Software Assurance Maturity Model.

The mission of [[_content/dictionary#S|SAMM]] is to provide an effective and measurable way for all types of organizations to analyze and improve their software security posture. It aims to raise awareness and educate organizations on how to design, develop, and deploy secure software through a self-assessment model. SAMM supports the complete software lifecycle and is technology and process agnostic. SAMM is built to be evolutive and risk-driven in nature, as there is no single recipe that works for all organizations.

### Key Characteristics

- **[[_content/dictionary#M|MEASURABLE]]**: Defined maturity levels across security practices
- **[[_content/dictionary#A|ACTIONABLE]]**: Clear pathways for improving maturity levels
- **[[_content/dictionary#V|VERSATILE]]**: Technology, process, and organization agnostic

The [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] community is powered by security knowledgeable volunteers from businesses and educational organizations. The global community works to create freely-available articles, methodologies, documentation, tools, and technologies.

## About [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]]

### The [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] Model

[[_content/dictionary#S|SAMM]] is a prescriptive model, an open framework which is simple to use, fully defined, and measurable. The solution details are easy enough to follow even for non-security personnel. It helps organizations:

- Analyze their current software security practices
- Build a security program in defined iterations
- Show progressive improvements in secure practices
- Define and measure security-related activities

[[_content/dictionary#S|SAMM]] was defined with flexibility in mind so that small, medium, and large organizations using any style of development can customize and adopt it. It provides a means of knowing where your organization is on its journey towards software assurance and understanding what is recommended to move to the next level of maturity.

[[_content/dictionary#S|SAMM]] does not insist that all organizations achieve the maximum maturity level in every category. Each organization can determine the target maturity level for each Security Practice that is the best fit and adapt the available templates for their specific needs.

### [[_content/dictionary#O|OWASP]] [[_content/dictionary#S|SAMM]] Structure

[[_content/dictionary#S|SAMM]] is based around 15 security practices grouped into 5 business functions. Every security practice contains a set of activities, structured into 3 maturity levels. The activities on a lower maturity level are typically easier to execute and require less formalization than the ones on a higher maturity level.

At the highest level, [[_content/dictionary#S|SAMM]] defines five business functions. Each business function is a category of activities that any organization involved with software development must fulfill to some degree.

Each business function has three security practices, areas of security-related activities that build assurance for the related business function.

Security practices have activities, grouped in logical flows and divided into two streams. Streams cover different aspects of a practice and have their own objectives, aligning and linking the activities in the practice over the different maturity levels.

For each security practice, [[_content/dictionary#S|SAMM]] defines three maturity levels. Each level has a successively more sophisticated objective with specific activities, and more strict success metrics.

The structure and setup of the [[_content/dictionary#S|SAMM]] model support:
- The assessment of the organization's current software security posture
- The definition of the organization's target
- The definition of an implementation roadmap to get there
- Prescriptive advice on how to implement particular activities

## [[_content/dictionary#S|SAMM]] Business Functions and Security Practices

### 1. Governance
Governance focuses on the processes and activities related to how an organization manages overall software development activities. More specifically, this includes concerns that impact cross-functional groups involved in development, as well as business processes established at the organization level.

#### Security Practices:
- **Strategy & Metrics**: This practice forms the basis of your secure software activities by building an overall plan.
- **Policy & Compliance**: This practice focuses on understanding and meeting external legal and regulatory requirements while driving internal security standards to ensure compliance in a way that's aligned with the business purpose of the organization.
- **Education & Guidance**: This practice focuses on increasing the knowledge in the organization regarding secure software.

##### Strategy & Metrics

**Practice Overview**

Software assurance entails many different activities and concerns. Without an overall plan, you might be spending a lot of effort to build in security, while in fact your efforts may be unaligned, disproportional or even counterproductive. The goal of the Strategy and Metrics ([[_content/dictionary#S|SM]]) practice is to build an efficient and effective plan for realizing your software security objectives within your organization.

A software security program, that selects and prioritizes activities of the rest of the model, serves as the foundation for your efforts. The practice works on building the plan, maintaining and disseminating it.

At the same time, you want to keep track of your security posture and program improvements. A metrics-driven approach is included to ensure an accurate view on your activities. To measure is to know.

**Streams Overview**

*Stream A - Create & Promote*
This stream is about creating and promoting an application security roadmap to set the objectives of the enterprise on this topic and increase alignment among stakeholders.

*Stream B - Measure & Improve*
This stream aims to drive the validity, relevance, and improvement of the application security roadmap through measurements of performance within the organization.

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Create & Promote:
- **Benefit**: Common understanding of your organization's security posture
- **Activity**: Understand, based on application risk exposure, what threats exist or may exist, as well as how tolerant executive leadership is of these risks. This understanding is a key component of determining software security assurance priorities. To ascertain these threats, interview business owners and stakeholders and document drivers specific to industries where the organization operates as well as drivers specific to the organization. Gathered information includes worst-case scenarios that could impact the organization, as well as opportunities where an optimized software development lifecycle and more secure applications could provide a market-differentiator or create additional opportunities.
- Gathered information provides a baseline for the organization to develop and promote its application security program. Items in the program are prioritized to address threats and opportunities most important to the organization. The baseline is split into several risk factors and drivers linked directly to the organization's priorities and used to help build a risk profile of each custom-developed application by documenting how they can impact the organization if they are compromised.
- The baseline and individual risk factors should be published and made available to application development teams to ensure a more transparent process of creating application risk profiles and incorporating the organization's priorities into the program. Additionally, these goals should provide a set of objectives which should be used to ensure all application security program enhancements provide direct support of the organization's current and future needs.
- **Quality Criteria**:
  - You capture the risk appetite of your organization's executive leadership
  - The organization's leadership vet and approve the set of risks
  - You identify the main business and technical threats to your assets and data
  - You document risks and store them in an accessible location

Stream B - Measure & Improve:
- **Benefit**: Basic insights into your [[_content/dictionary#A|AppSec]] program's effectiveness and efficiency
- **Activity**: Define and document metrics to evaluate the effectiveness and efficiency of the application security program. This way improvements are measurable and you can use them to secure future support and funding for the program.
- Considering the dynamic nature of most development environments, metrics should be comprised of measurements in the following categories:
  - 'Effort' metrics measure the effort spent on security. For example training hours, time spent performing code reviews, and number of applications scanned for vulnerabilities.
  - 'Result' metrics measure the results of security efforts. Examples include number of outstanding patches with security defects and number of security incidents involving application vulnerabilities.
  - 'Environment' metrics measure the environment where security efforts take place. Examples include number of applications or lines of code as a measure of difficulty or complexity.
- Each metric by itself is useful for a specific purpose, but a combination of two or three metrics together helps explain spikes in metrics trends. For example, a spike in a total number of vulnerabilities may be caused by the organization on-boarding several new applications that have not been previously exposed to the implemented application security mechanisms. Alternatively, an increase in the environment metrics without a corresponding increase in the effort or result could be an indicator of a mature and efficient security program.
- While identifying metrics, it's always recommended to stick to the metrics that meet several criteria:
  - Consistently Measured
  - Inexpensive to gather
  - Expressed as a cardinal number or a percentage
  - Expressed as a unit of measure
- Document metrics and include descriptions of best and most efficient methods for gathering data, as well as recommended methods for combining individual measures into meaningful metrics. For example, a number of applications and a total number of defects across all applications may not be useful by themselves but, when combined as a number of outstanding high-severity defects per application, they provide a more actionable metric.
- **Quality Criteria**:
  - You document each metric, including a description of the sources, measurement coverage, and guidance on how to use it to explain application security trends
  - Metrics include measures of efforts, results, and the environment measurement categories
  - Most of the metrics are frequently measured, easy or inexpensive to gather, and expressed as a cardinal number or a percentage
  - Application security and development teams publish metrics

*Maturity Level 2*

Stream A - Create & Promote:
- **Benefit**: Available and agreed upon roadmap of your [[_content/dictionary#A|AppSec]] program
- **Activity**: Based on the magnitude of assets, threats, and risk tolerance, develop a security strategic plan and budget to address business priorities around application security. The plan covers 1 to 3 years and includes milestones consistent with the organization's business drivers and risks. It provides tactical and strategic initiatives and follows a roadmap that makes its alignment with business priorities and needs visible.
- In the roadmap, you reach a balance between changes requiring financial expenditures, changes of processes and procedures, and changes impacting the organization's culture. This balance helps accomplish multiple milestones concurrently and without overloading or exhausting available resources or development teams. The milestones are frequent enough to help monitor program success and trigger timely roadmap adjustments.
- For the program to be successful, the application security team obtains buy-in from the organization's stakeholders and application development teams. A published plan is available to anyone who is required to support or participate in its implementation.
- **Quality Criteria**:
  - The plan reflects the organization's business priorities and risk appetite
  - The plan includes measurable milestones and a budget
  - The plan is consistent with the organization's business drivers and risks
  - The plan lays out a roadmap for strategic and tactical initiatives
  - You have buy-in from stakeholders, including development teams

Stream B - Measure & Improve:
- **Benefit**: Transparency on your [[_content/dictionary#A|AppSec]] program's performance
- **Activity**: Once the organization has defined its application security metrics, collect enough information to establish realistic goals. Test identified metrics to ensure you can gather data consistently and efficiently over a short period. After the initial testing period, the organization should have enough information to commit to goals and objectives expressed through Key Performance Indicators (KPIs).
- While several measurements are useful for monitoring the information security program and its effectiveness, KPIs are comprised of the most meaningful and effective metrics. Aim to remove volatility common in application development environments from KPIs to reduce chances of unfavorable numbers resulting from temporary or misleading individual measurements. Base KPIs on metrics considered valuable not only to Information Security professionals but also to individuals responsible for the overall success of the application, and organization's leadership. View KPIs as definitive indicators of the success of the whole program and consider them actionable.
- Fully document KPIs and distribute them to the teams contributing to the success of the program as well as organization's leadership. Ideally, include a brief explanation of the information sources for each [[_content/dictionary#K|KPI]] and the meaning if the numbers are high or low. Include short and long-term goals, and ranges for unacceptable measurements requiring immediate intervention. Share action plans with application security and application development teams to ensure full transparency in understanding of the organization's objectives and goals.
- **Quality Criteria**:
  - You defined KPIs after gathering enough information to establish realistic objectives
  - You developed KPIs with the buy-in from the leadership and teams responsible for application security
  - KPIs are available to the application teams and include acceptability thresholds and guidance in case teams need to take action
  - Success of the application security program is clearly visible based on defined KPIs

*Maturity Level 3*

Stream A - Create & Promote:
- **Benefit**: Continuous [[_content/dictionary#A|AppSec]] program alignment with the organization's business goals
- **Activity**: You review the application security plan periodically for ongoing applicability and support of the organization's evolving needs and future growth. To do this, you repeat the steps from the first two maturity levels of this Security Practice at least annually. The goal is for the plan to always support the current and future needs of the organization, which ensures the program is aligned with the business.
- In addition to reviewing the business drivers, the organization closely monitors the success of the implementation of each of the roadmap milestones. You evaluate the success of the milestones based on a wide range of criteria, including completeness and efficiency of the implementation, budget considerations, and any cultural impacts or changes resulting from the initiative. You review missed or unsatisfactory milestones and evaluate possible changes to the overall program.
- The organization develops dashboards and measurements for management and teams responsible for software development to monitor the implementation of the roadmap. These dashboards are detailed enough to identify individual projects and initiatives and provide a clear understanding of whether the program is successful and aligned with the organization's needs.
- **Quality Criteria**:
  - You review and update the plan in response to significant changes in the business environment, the organization, or its risk appetite
  - Plan update steps include reviewing the plan with all the stakeholders and updating the business drivers and strategies
  - You adjust the plan and roadmap based on lessons learned from completed roadmap activities
  - You publish progress information on roadmap activities, making sure they are available to all stakeholders

Stream B - Measure & Improve:
- **Benefit**: Continuous improvement of your program according to results
- **Activity**: Define guidelines for influencing the Application Security program based on the KPIs and other application security metrics. These guidelines combine the maturity of the application development process and procedures with different metrics to make the program more efficient. The following examples show a relationship between measurements and ways of evolving and improving application security:
  - Focus on maturity of the development lifecycle makes the relative cost per defect lower by applying security proactively.
  - Monitoring the balance between effort, result, and environment metrics improves the program's efficiency and justifies additional automation and other methods for improving the overall application security baselines.
  - Individual Security Practices could provide indicators of success or failure of individual application security initiatives.
  - Effort metrics helps ensure application security work is directed at the more relevant and important technologies and disciplines.
- When defining the overall metrics strategy, keep the end-goal in mind and define what decisions can be made as a result of changes in KPIs and metrics as soon as possible, to help guide development of metrics.
- **Quality Criteria**:
  - You review KPIs at least yearly for their efficiency and effectiveness
  - KPIs and application security metrics trigger most of the changes to the application security strategy

#### Policy & Compliance

**Practice Overview**

The Policy and Compliance ([[_content/dictionary#P|PC]]) practice focuses on understanding and meeting external legal and regulatory requirements while driving internal security standards to ensure compliance in a way that's aligned with the business purpose of the organization.

A driving theme for improvement within this practice is describing organization's standards and 3rd party obligations as application requirements, enabling efficient and automated audits that may be leveraged within the [[_content/dictionary#S|SDLC]] and continuously demonstrate that all expectations are met.

In a sophisticated form, provision of this practice entails an organization-wide understanding of both internal standards and external compliance drivers while also maintaining low-latency checkpoints with project teams to ensure no project is operating outside expectations without visibility.

**Streams Overview**

*Stream A - Policy & Standards*
This stream focuses on maintaining policies and standards and providing them to support integration into the [[_content/dictionary#S|SDLC]].

*Stream B - Compliance Management*
This stream focuses on identifying and providing compliance requirements to support integration into the [[_content/dictionary#S|SDLC]].

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Policy & Standards:
- **Benefit**: Clear expectation of minimum security level in the organization
- **Activity**: Develop a library of policies and standards to govern all aspects of software development in the organization. Policies and standards are based on existing industry standards and appropriate for the organization's industry. Due to the full range of technology-specific limitations and best practices, review proposed standards with the various product teams. With the overarching objective of increasing security of the applications and computing infrastructure, invite product teams to offer feedback on any aspects of the standards that would not be feasible or cost-effective to implement, as well as opportunities for standards to go further with little effort on the product teams.
- For policies, emphasize high-level definitions and aspects of application security that do not depend on specific technology or hosting environment. Focus on broader objectives of the organization to protect the integrity of its computing environment, safety and privacy of the data, and maturity of the software development life-cycles. For larger organizations, policies may qualify specific requirements based on data classification or application functionality, but should not be detailed enough to offer technology-specific guidance.
- For standards, incorporate requirements set forth by policies, and focus on technology-specific implementation guidance intended to capture and take advantage of the security features of different programming languages and frameworks. Standards require input from senior developers and architects considered experts in various technologies in use by the organization. Create them in a format that allows for periodic updates. Label or tag individual requirements with the policy or a 3rd party requirement, to make maintenance and audits easier and more efficient.
- **Quality Criteria**:
  - You have adapted existing standards appropriate for the organization's industry to account for domain-specific considerations
  - Your standards are aligned with your policies and incorporate technology-specific implementation guidance

Stream B - Compliance Management:
- **Benefit**: Security policies and standards aligned with external compliance drivers
- **Activity**: Create a comprehensive list of all compliance requirements, including any triggers that could help determine which applications are in scope. Compliance requirements may be considered in scope based on factors such as geographic location, types of data, or contractual obligations with clients or business partners. Review each identified compliance requirement with the appropriate experts and legal, to ensure the obligation is understood. Since many compliance obligations vary in applicability based on how the data is processed, stored, or transmitted across the computing environment, compliance drivers should always indicate opportunities for lowering the overall compliance burden by changing how the data is handled.
- Evaluate publishing a compliance matrix to help identify which factors could put an application in scope for a specific regulatory requirement. Have the matrix indicate which compliance requirements are applicable at the organization level and do not depend on individual applications. The matrix provides at least a basic understanding of useful compliance requirements to review obligations around different applications.
- Since many compliance standards are focused around security best-practices, many compliance requirements may already be a part of the Policy and Standards library published by the organization. Therefore, once you review compliance requirements, map them to any applicable existing policies and standards. Whenever there are discrepancies, update the policies and standards to include organization-wide compliance requirements. Then, begin creating compliance-specific standards only applicable to individual compliance requirements. The goal is to have a compliance matrix that indicates which policies and standards have more detailed information about compliance requirements, as well as ensure individual policies and standards reference applicable compliance requirements.
- **Quality Criteria**:
  - You have identified all sources of external compliance obligations
  - You have captured and reconciled compliance obligations from all sources

*Maturity Level 2*

Stream A - Policy & Standards:
- **Benefit**: Common understanding of how to reach compliance with security policies for product teams
- **Activity**: To assist with the ongoing implementation and verification of compliance with policies and standards, develop application security and appropriate test scripts related to each applicable requirement. Organize these documents into libraries and make them available to all application teams in formats most conducive for inclusion into each application. Clearly label the documents and link them to the policies and standards they represent, to assist with the ongoing updates and maintenance. Version policies and standards and include detailed change logs with each iterative update to make ongoing inclusion into different products' [[_content/dictionary#S|SDLC]] easier.
- Write application security requirements in a format consistent with the existing requirements management processes. You may need more than one version catering to different development methodologies or technologies. The goal is to make it easy for various product teams to incorporate policies and standards into their existing development life-cycles needing minimal interpretation of requirements.
- Test scripts help reinforce application security requirements through clear expectations of application functionality, and guide automated or manual testing efforts that may already be part of the development process. These efforts not only help each team establish the current state of compliance with existing policies and standards, but also ensure compliance as applications continue to change.
- **Quality Criteria**:
  - You create verification checklists and test scripts where applicable, aligned with the policy's requirements and the implementation guidance in the associated standards
  - You create versions adapted to each development methodology and technology the organization uses

Stream B - Compliance Management:
- **Benefit**: Common understanding how to reach compliance with external compliance drivers for product teams
- **Activity**: Develop a library of application requirements and test scripts to establish and verify regulatory compliance of applications. Some of these are tied to individual compliance requirements like [[_content/dictionary#P|PCI]] or [[_content/dictionary#G|GDPR]], while others are more general in nature and address global compliance requirements such as [[_content/dictionary#I|ISO]]. The library is available to all application development teams. It includes guidance for determining all applicable requirements including considerations for reducing the compliance burden and scope. Implement a process to periodically re-assess each application's compliance requirements. Re-assessment includes reviewing all application functionality and opportunities to reduce scope to lower the overall cost of compliance.
- Requirements include enough information for developers to understand functional and non-functional requirements of the different compliance obligations. They include references to policies and standards, and provide explicit references to regulations. If there are questions about the implementation of a particular requirement, the original text of the regulation can help interpret the intent more accurately. Each requirement includes a set of test scripts for verifying compliance. In addition to assisting [[_content/dictionary#Q|QA]] with compliance verification, these can help clarify compliance requirements for developers and make the compliance process transparent. Requirements have a format that allows importing them into individual requirements repositories. further clarify compliance requirements for developers and ensure the process of achieving compliance is fully transparent.
- **Quality Criteria**:
  - You map each external compliance obligation to a well-defined set of application requirements
  - You define verification procedures, including automated tests, to verify compliance with compliance-related requirements

*Maturity Level 3*

Stream A - Policy & Standards:
- **Benefit**: Understanding of your organization's compliance with policies and standards
- **Activity**: Develop a program to measure each application's compliance with existing policies and standards. Mandatory requirements should be motivated and reported consistently across all teams. Whenever possible, tie compliance status into automated testing and report with each version. Compliance reporting includes the version of policies and standards and appropriate code coverage factors.
- Encourage non-compliant teams to review available resources such as security requirements and test scripts, to ensure non-compliance is not a result of inadequate guidance. Forward issues resulting from insufficient guidance to the teams responsible for publishing application requirements and test scripts, to include them in the future releases. Escalate issues resulting from the inability to meet policies and standards to teams that handle application security risks.
- **Quality Criteria**:
  - You have procedures (automated, if possible) to regularly generate compliance reports
  - You deliver compliance reports to all relevant stakeholders
  - Stakeholders use the reported compliance status information to identify areas for improvement

Stream B - Compliance Management:
- **Benefit**: Understanding of your organization's compliance with external compliance drivers
- **Activity**: Develop a program for measuring and reporting on the status of compliance between different applications. Application requirements and test scripts help determine the status of compliance. Leverage testing automation to promptly detect compliance regressions in frequently updated applications and ensure compliance is maintained through the different application versions. Whenever fully automated testing is not possible, [[_content/dictionary#Q|QA]], Internal Audit, or Information Security teams assess compliance periodically through a combination of manual testing and interview.
- While full compliance is always the ultimate goal, include tracking remediation actions and periodic updates in the program. Review compliance remediation activities periodically to check teams are making appropriate progress, and that remediation strategies will be effective in achieving compliance. To further improve the process, develop a series of standard reports and compliance scorecards. These help individual teams understand the current state of compliance, and the organization manage assistance for remediating compliance gaps more effectively.
- Review compliance gaps requiring significant expenses or development with the subject-matter experts and compare them against the cost of reducing the application's functionality, minimizing scope or eliminating the compliance requirement. longterm compliance gaps require management approval and a formal compliance risk acceptance, so they receive appropriate attention and scrutiny from the organization's leadership.
- **Quality Criteria**:
  - You have established, well-defined compliance metrics
  - You measure and report on applications' compliance metrics regularly
  - Stakeholders use the reported compliance status information to identify compliance gaps and prioritize gap remediation efforts

#### Education & Guidance

**Practice Overview**

The Education and Guidance ([[_content/dictionary#E|EG]]) practice focuses on arming personnel involved in the software lifecycle with knowledge and resources to design, develop, and deploy secure software. With improved access to information, project teams can proactively identify and mitigate the specific security risks that apply to their organization.

One major theme for improvement across the Objectives is providing training for employees and increasing their security awareness, either through instructor-led sessions or computer-based modules. As an organization progresses, it builds a broad base of training starting with developers and moving to other roles, culminating with the addition of role-based training to ensure applicability and effectiveness.

In addition to training, this practice also requires the organization to make a significant investment in improving organizational culture to promote application security through collaboration between teams. Collaboration tools and increased transparency between technologies and tools support this approach to improve the security of the applications.

**Streams Overview**

*Stream A - Training & Awareness*
Training and awareness focuses on increasing the overall knowledge around software security among the different stakeholders within the organization.

*Stream B - Organization & Culture*
Organization and culture focuses on promoting the culture of application security within the organization as an important success factor of an [[_content/dictionary#S|SDLC]] project.

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Training & Awareness:
- **Benefit**: Basic security awareness for all relevant employees
- **Activity**: Conduct security awareness training for all roles currently involved in the management, development, testing, or auditing of the software. The goal is to increase the awareness of application security threats and risks, security best practices, and secure software design principles. Develop training internally or procure it externally. Ideally, deliver training in person so participants can have discussions as a team, but Computer-Based Training ([[_content/dictionary#C|CBT]]) is also an option.
- Course content should include a range of topics relevant to application security and privacy, while remaining accessible to a non-technical audience. Suitable concepts are secure design principles including Least Privilege, Defense-in-Depth, Fail Secure (Safe), Complete Mediation, Session Management, Open Design, and Psychological Acceptability. Additionally, the training should include references to any organization-wide standards, policies, and procedures defined to improve application security. The [[_content/dictionary#O|OWASP]] Top 10 vulnerabilities should be covered at a high level.
- Training is mandatory for all employees and contractors involved with software development and includes an auditable sign-off to demonstrate compliance. Consider incorporating innovative ways of delivery (such as gamification) to maximize its effectiveness and combat desensitization.
- **Quality Criteria**:
  - Training is repeatable, consistent, and available to anyone involved with software development lifecycle
  - Training includes the latest OWASP Top 10 if appropriate and includes concepts such as Least Privilege, Defense-in-Depth, Fail Secure (Safe), Complete Mediation, Session Management, Open Design, and Psychological Acceptability
  - Training requires a sign-off or an acknowledgement from attendees
  - You have updated the training in the last 12 months
  - Training is required during employees' onboarding process

Stream B - Organization & Culture:
- **Benefit**: Basic embedding of security in the development organization
- **Activity**: Implement a program where each software development team has a member considered a "Security Champion" who is the liaison between Information Security and developers. Depending on the size and structure of the team the "Security Champion" may be a software developer, tester, or a product manager. The "Security Champion" has a set number of hours per week for Information Security related activities. They participate in periodic briefings to increase awareness and expertise in different security disciplines. "Security Champions" have additional training to help develop these roles as Software Security subject-matter experts. You may need to customize the way you create and support "Security Champions" for cultural reasons.
- The goals of the position are to increase effectiveness and efficiency of application security and compliance and to strengthen the relationship between various teams and Information Security. To achieve these objectives, "Security Champions" assist with researching, verifying, and prioritizing security and compliance related software defects. They are involved in all Risk Assessments, Threat Assessments, and Architectural Reviews to help identify opportunities to remediate security defects by making the architecture of the application more resilient and reducing the attack threat surface.
- In addition to assisting Information Security, "Security Champions" provide periodic reviews of all security-related issues for the project team so everyone is aware of the problems and any current and future remediation efforts. These reviews are leveraged to help brainstorm solutions to more complex problems by engaging the entire development team.
- **Quality Criteria**:
  - Security Champions receive appropriate training
  - Application Security and Development teams receive periodic briefings from Security Champions on the overall status of security initiatives and fixes
  - The Security Champion reviews the results of external testing before adding to the application backlog

*Maturity Level 2*

Stream A - Training & Awareness:
- **Benefit**: Relevant employee roles trained according to their specific role
- **Activity**: Conduct instructor-led or [[_content/dictionary#C|CBT]] security training specific to the organization's roles and technologies, starting with the core development team. The organization customizes training for product managers, software developers, testers, and security auditors, based on each group's technical needs.
- Product managers train on topics related to [[_content/dictionary#S|SAMM]] business functions and security practices, with emphasis on security requirements, threat modeling, and defect tracking.
- Developers train on coding standards and best practices for the technologies they work with to ensure the training directly benefits application security. They have a solid technical understanding of the [[_content/dictionary#O|OWASP]] Top 10 vulnerabilities, or similar weaknesses relevant to the technologies and frameworks used (e.g. mobile), and the most common remediation strategies for each issue.
- Testers train on the different testing tools and best practices for technologies used in the organization, and in tools that identify security defects.
- Security auditors train on the software development lifecycle, application security mechanisms used in the organization, and the process for submitting security defects for remediation.
- Security Champions train on security topics from various phases of the [[_content/dictionary#S|SDLC]]. They receive the same training as developers and testers, but also understand threat modeling and secure design, as well as security tools and technologies that can be integrated into the build environment.
- Include all training content from the Maturity Level 1 activities of this stream and additional role-specific and technology-specific content. Eliminate unnecessary aspects of the training.
- Ideally, identify a subject-matter expert in each technology to assist with procuring or developing the training content and updating it regularly. The training consists of demonstrations of vulnerability exploitation using intentionally weakened applications, such as [[_content/dictionary#W|WebGoat]] or Juice Shop. Include results of the previous penetration as examples of vulnerabilities and implemented remediation strategies. Ask a penetration tester to assist with developing examples of vulnerability exploitation demonstrations.
- Training is mandatory for all employees and contractors involved with software development, and includes an auditable sign-off to demonstrate compliance. Whenever possible, training should also include a test to ensure understanding, not just compliance. Update and deliver training annually to include changes in the organization, technology, and trends. Poll training participants to evaluate the quality and relevance of the training. Gather suggestions of other information relevant to their work or environments.
- **Quality Criteria**:
  - Training includes all topics from maturity level 1, and adds more specific tools, techniques, and demonstrations
  - Training is mandatory for all employees and contractors
  - Training includes input from in-house SMEs and trainees
  - Training includes demonstrations of tools and techniques developed in-house
  - You use feedback to enhance and make future training more relevant

Stream B - Organization & Culture:
- **Benefit**: Specific security best practices tailored to the organization
- **Activity**: The organization implements a formal secure coding center of excellence, with architects and senior developers representing the different business units and technology stacks. The team has an official charter and defines standards and best practices to improve software development practices. The goal is to mitigate the way velocity of change in technology, programming languages, and development frameworks and libraries makes it difficult for Information Security professionals to be fully informed of all the technical nuances that impact security. Even developers often struggle keeping up with all the changes and new tools intended to make software development faster, better, and safer.
- This ensures all current programming efforts follow industry's best practices and organization's development and implementation standards include all critical configuration settings. It helps identify, train, and support "Product Champions", responsible for assisting different teams with implementing tools that automate, streamline, or improve various aspects of the [[_content/dictionary#S|SDLC]]. It identifies development teams with higher maturity levels within their SDLC and the practices and tools that enable these achievements, with the goal of replicating them to other teams.
- The group provides subject matter expertise, helping information security teams evaluate tools and solutions to improve application security, ensuring these tools are not only useful but also compatible with the way different teams develop applications. Teams looking to make significant architectural changes to their software consult with this group to avoid adversely impacting the [[_content/dictionary#S|SDLC]] lifecycle or established security controls.
- **Quality Criteria**:
  - The [[_content/dictionary#S|SSCE]] has a charter defining its role in the organization
  - Development teams review all significant architectural changes with the SSCE
  - The SSCE publishes SDLC standards and guidelines related to Application Security
  - Product Champions are responsible for promoting the use of specific security tools

*Maturity Level 3*

Stream A - Training & Awareness:
- **Benefit**: Adequate security knowledge of all employees ensured prior to working on critical tasks
- **Activity**: Implement a formal training program requiring anyone involved with the software development lifecycle to complete appropriate role and technology-specific training as part of the onboarding process. Based on the criticality of the application and user's role, consider restricting access until the onboarding training has been completed. While the organization may source some modules externally, the program is facilitated and managed in-house and includes content specific to the organization going beyond general security best practices. The program has a defined curriculum, checks participation, and tests understanding and competence. The training consists of a combination of industry best practices and organization's internal standards, including training on specific systems used by the organization.
- In addition to issues directly related to security, the organization includes other standards to the program, such as code complexity, code documentation, naming convention, and other process-related disciplines. This training minimizes issues resulting from employees following practices incorporated outside the organization and ensures continuity in the style and competency of the code.
- To facilitate progress monitoring and successful completion of each training module the organization has a learning management platform or another centralized portal with similar functionality. Employees can monitor their progress and have access to all training resources even after they complete initial training.
- Review issues resulting from employees not following established standards, policies, procedures, or security best practices at least annually to gauge the effectiveness of the training and ensure it covers all issues relevant to the organization. Update the training periodically and train employees on any changes and most prevalent security deficiencies.
- **Quality Criteria**:
  - A Learning Management System ([[_content/dictionary#L|LMS]]) is used to track trainings and certifications
  - Training is based on internal standards, policies, and procedures
  - You use certification programs or attendance records to determine access to development systems and resources

Stream B - Organization & Culture:
- **Benefit**: Collective development of security know-how among all product teams
- **Activity**: Security is the responsibility of all employees, not just the Information Security team. Deploy communication and knowledge sharing platforms to help developers build communities around different technologies, tools, and programming languages. In these communities employees share information, discuss challenges with other developers, and search the knowledge base for answers to previously discussed issues.
- Form communities around roles and responsibilities and enable developers and engineers from different teams and business units to communicate freely and benefit from each other's expertise. Encourage participation, set up a program to promote those who help the most people as thought leaders, and have management recognize them. In addition to improving application security, this platform may help identify future members of the Secure Software Center of Excellence, or 'Security Champions' based on their expertise and willingness to help others.
- The Secure Software Center of Excellence and Application Security teams review the information portal regularly for insights into the new and upcoming technologies, as well as opportunities to assist the development community with new initiatives, tools, programs, and training resources. Use the portal to disseminate information about new standards, tools, and resources to all developers for the continued improvement of [[_content/dictionary#S|SDLC]] maturity and application security.
- **Quality Criteria**:
  - The organization promotes use of a single portal across different teams and business units
  - The portal is used for timely information such as notification of security incidents, tool updates, architectural standard changes, and other related announcements
  - The portal is widely recognized by developers and architects as a centralized repository of the organization-specific application security information
  - All content is considered persistent and searchable
  - The portal provides access to application-specific security metrics

### 2. Design

Business Function Overview

Design concerns the processes and activities related to how an organization defines goals and creates software within development projects. In general, this will include requirements gathering, high-level architecture specification and detailed design.

#### Security Practices:
- **Threat Assessment**: Identification and understanding of project-level risks based on the functionality of the software being developed and characteristics of the runtime environment.
- **Security Requirements**: Specification of the expectations for security controls and security functionality in the software.
- **Security Architecture**: The design elements that describe how security controls are designed into the software.

##### Threat Assessment

**Practice Overview**

The Threat Assessment ([[_content/dictionary#T|TA]]) practice focuses on identifying and understanding of project-level risks based on the functionality of the software being developed and characteristics of the runtime environment. From details about threats and likely attacks against each project, the organization as a whole operates more effectively through better decisions about prioritization of initiatives for security. Additionally, decisions for risk acceptance are more informed, therefore better aligned to the business.

By starting with simple threat models and building application risk profiles, an organization improves over time. Ultimately, a sophisticated organization would maintain this information in a way that is tightly coupled to the compensating factors and pass-through risks from external entities. This provides greater breadth of understanding for potential downstream impacts from security issues while keeping a close watch on the organization's current performance against known threats.

**Streams Overview**

*Stream A - Application Risk Profile*
An application risk profile helps to identify which applications can pose a serious threat to the organization if they were attacked or breached.

*Stream B - Threat Modeling*
Threat modeling is intended to help software development teams understand what risks exist in what is being built, what could go wrong, and how we the risks can be mitigated or remediated.

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Application Risk Profile:
- **Benefit**: Ability to classify applications according to risk
- **Activity**: Use a simple method to evaluate the application risk per application, estimating the potential business impact that it poses for the organization in case of an attack. To achieve this, evaluate the impact of a breach in the confidentiality, integrity and availability of the data or service. Consider using a set of 5-10 questions to understand important application characteristics, such as whether the application processes financial data, whether it is internet facing, or whether privacy-related data is involved. The application risk profile tells you whether these factors are applicable and if they could significatly impact the organization.
- Next, use a scheme to classify applications according to this risk. A simple, qualitative scheme (e.g. high/medium/low) that translates these characteristics into a value is often effective. It is important to use these values to represent and compare the risk of different applications against each other. Mature highly risk-driven organizations might make use of more quantitative risk schemes. Don't invent a new risk scheme if your organization already has one that works well.
- **Quality Criteria**:
  - An agreed-upon risk classification exists
  - The application team understands the risk classification
  - The risk classification covers critical aspects of business risks the organization is facing
  - The organization has an inventory for the applications in scope

Stream B - Threat Modeling:
- **Benefit**: Identification of architectural design flaws in your applications
- **Activity**: Threat modeling is a structured activity for identifying, evaluating, and managing system threats, architectural design flaws, and recommended security mitigations. It is typically done as part of the design phase or as part of a security assessment.
- Threat modeling is a team exercise, including product owners, architects, security champions, and security testers. At this maturity level, expose teams and stakeholders to threat modeling to increase security awareness and to create a shared vision on the security of the system.
- At maturity level 1, you perform threat modeling ad-hoc for high-risk applications and use simple threat checklists, such as [[_content/dictionary#S|STRIDE]]. Avoid lengthy workshops and overly detailed lists of low-relevant threats. Perform threat modeling iteratively to align to more iterative development paradigms. If you add new functionality to an existing application, look only into the newly added functions instead of trying to cover the entire scope. A good starting point is the existing diagrams that you annotate during discussion workshops. Always make sure to persist the outcome of a threat modeling discussion for later use.
- Your most important tool to start threat modeling is a whiteboard, smartboard, or a piece of paper. Aim for security awareness, a simple process, and actionable outcomes that you agree upon with your team.
- **Quality Criteria**:
  - You perform threat modeling for high-risk applications
  - You use simple threat checklists, such as STRIDE
  - You persist the outcome of a threat model for later use

*Maturity Level 2*

Stream A - Application Risk Profile:
- **Benefit**: Solid understanding of the risk level of your application portfolio
- **Activity**: The goal of this activity is to thoroughly understand the risk level of all applications within the organization, to focus the effort of your software assurance activities where it really matters.
- From a risk evaluation perspective, the basic set of questions is not enough to thoroughly evaluate the risk of all applications. Create an extensive and standardized way to evaluate the risk of the application, among others via their impact on information security (confidentiality, integrity and availability of data). Next to security, you also want to evaluate the privacy risk of the application. Understand the data that the application processes and what potential privacy violations are relevant. Finally, study the impact that this application has on other applications within the organization (e.g., the application might be modifying data that was considered read-only in another context). Evaluate all applications within the organization, including all existing and legacy ones.
- Leverage business impact analysis to quantify and classify application risk. A simple qualitative scheme (such as high/medium/low) is not enough to effectively manage and compare applications on an enterprise-wide level. Based on this input, Security Officers leverage the classification to define the risk profile to build a centralized inventory of risk profiles and manage accountability. This inventory gives Product Owners, Managers, and other organizational stakeholders an aligned view of the risk level of an application in order to assign appropriate priority to security-related activities.
- **Quality Criteria**:
  - The application risk profile is in line with the organizational risk standard
  - The application risk profile covers impact to security and privacy
  - You validate the quality of the risk profile manually and/or automatically
  - The application risk profiles are stored in a central inventory

Stream B - Threat Modeling:
- **Benefit**: Clear expectations of the quality of threat modeling activities
- **Activity**: Use a standardized threat modeling methodology for your organization and align this on your application risk levels. Think about ways to support the scaling of threat modeling throughout the organization.
- Train your architects, security champions, and other stakeholders on how to do practical threat modeling. Threat modeling requires understanding, clear playbooks and templates, organization-specific examples, and experience, which is hard to automate.
- Your threat modeling methodology includes at least diagramming, threat identification, design flaw mitigations, and how to validate your threat model artifacts. Your threat model diagram allows a detailed understanding of the environment and the mechanics of the application. You discover threats to your application with checklists, such as [[_content/dictionary#S|STRIDE]] or more organization-specific threats. For identified design flaws (ranked according to risk for your organization), you add mitigating controls to support stakeholders in dealing with particular threats. Define what triggers updating a threat model, for example, a technology change or deployment of an application in a new environment.
- Feed the output of threat modeling to the defect management process for adequate follow-up. Capture the threat modeling artifacts with tools that are used by your application teams.
- **Quality Criteria**:
  - You train your architects, security champions, and other stakeholders on how to do practical threat modeling
  - Your threat modeling methodology includes at least diagramming, threat identification, design flaw mitigations, and how to validate your threat model artifacts
  - Changes in the application or business context trigger a review of the relevant threat models
  - You capture the threat modeling artifacts with tools that are used by your application teams

*Maturity Level 3*

Stream A - Application Risk Profile:
- **Benefit**: Timely update of the application classification in case of changes
- **Activity**: The application portfolio of an organization changes, as well as the conditions and constraints in which an application lives (e.g., driven by the company strategy). Periodically review the risk inventory to ensure correctness of the risk evaluations of the different applications.
- Have a periodic review at an enterprise-wide level. Also, as your enterprise matures in software assurance, stimulate teams to continuously question which changes in conditions might impact the risk profile. For instance, an internal application might become exposed to the internet by a business decision. This should trigger the teams to rerun the risk evaluation and update the application risk profile accordingly.
- In a mature implementation of this practice, train and continuously update teams on lessons learned and best practices from these risk evaluations. This leads to a better execution and a more accurate representation of the application risk profile.
- **Quality Criteria**:
  - The organizational risk standard considers historical feedback to improve the evaluation method
  - Significant changes in the application or business context trigger a review of the relevant risk profiles

Stream B - Threat Modeling:
- **Benefit**: Assurance of continuous improvement of threat modeling activities
- **Activity**: Threat modeling is integrated into your [[_content/dictionary#S|SDLC]] and has become part of the developer security culture. Reusable risk patterns, comprising of related threat libraries, design flaws, and security mitigations, are created and improved, based on the organization's threat models. You regularly (e.g., yearly) review the existing threat models to verify that no new threats are relevant for your applications.
- You optimize your threat modeling methodology. You capture lessons learned from threat models and use these to improve your threat modeling methodology. You review the threat categories relevant to your organization and update your methodology appropriately. From time to time, you evaluate the quality of your threat models independently.
- You automate parts of your threat modeling process with threat modeling tools. You integrate your threat modeling tools with other security tools, such as security verification tools and risk tracking tools. You consider "threat modeling as code" practices to integrate threat modeling artifacts with application code.
- **Quality Criteria**:
  - The threat model methodology considers historical feedback for improvement
  - You regularly (e.g., yearly) review the existing threat models to verify that no new threats are relevant for your applications
  - You automate parts of your threat modeling process with threat modeling tools

#### Security Requirements

**Practice Overview**

The Security Requirements ([[_content/dictionary#S|SR]]) practice focuses on security requirements that are important in the context of secure software. A first type deals with typical software-related requirements, to specify objectives and expectations to protect the service and data at the core of the application. A second type deals with requirements relative to supplier organizations that are part of the development context of the application, in particular for outsourced development. It is important to streamline the expectations in terms of secure development because outsourced development can have significant impact on the security of the application. The security of 3rd party (technical) libraries is part of the software supply chains stream (see Secure Build), and it is not included in this practice.

**Streams Overview**

*Stream A - Software Requirements*
Software requirements specify objectives and expectations to protect the service and data at the core of the application.

*Stream B - Supplier Security*
Supplier security deals with requirements that are relative to supplier organizations within the development context of the application, in particular for outsourced development.

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Software Requirements:
- **Benefit**: Understanding of key security requirements during development
- **Activity**: Perform a review of the functional requirements of the software project. Identify relevant security requirements (i.e. expectations) for this functionality by reasoning on the desired confidentiality, integrity or availability of the service or data offered by the software project. Requirements state the objective (e.g., "personal data for the registration process should be transferred and stored securely"), but not the actual measure to achieve the objective (e.g., "use TLSv1.2 for secure transfer").
- At the same time, review the functionality from an attacker perspective to understand how it could be misused. This way you can identify extra protective requirements for the software project at hand.
- Security objectives can relate to specific security functionality you need to add to the application (e.g., "Identify the user of the application at all times") or to the overall application quality and behavior (e.g., "Ensure personal data is properly protected in transit"), which does not necessarily lead to new functionality. Follow good practices for writing security requirements. Make them specific, measurable, actionable, relevant and time-bound ([[_content/dictionary#S|SMART]]). Beware of adding requirements too general-purpose to not relate to the application at hand (e.g., The application should protect against the [[_content/dictionary#O|OWASP]] Top 10). While they can be true, they don't add value to the discussion.
- **Quality Criteria**:
  - Teams derive security requirements from functional requirements and customer or organization concerns
  - Security requirements are specific, measurable, and reasonable
  - Security requirements are in line with the organizational baseline

Stream B - Supplier Security:
- **Benefit**: Transparency of security practices of your software suppliers
- **Activity**: The security competences and habits of the external suppliers involved in the development of your software can have a significant impact on the security posture of the final product. Consequently, it is important to know and evaluate your suppliers on this front.
- Carry out a vendor assessment to understand the strengths and weaknesses of your suppliers. Use a basic checklist or conduct interviews to review their typical practices and deliveries. This gives you an idea of how they organize themselves and elements to evaluate whether you need to take additional measures to mitigate potential risks. Ideally, speak to different roles in the organization, or even set up a small maturity evaluation to this end. Strong suppliers will run their own software assurance program and will be able to answer most of your questions. If suppliers have weak competences in software security, discuss with them how and to what extent they plan to work on this and evaluate whether this is enough for your organization. A software supplier might be working on a low-risk project, but this could change.
- It is important that your suppliers understand and align to the risk appetite and are able to meet your requirements in that area. Make what you expect from them explicit and discuss this clearly.
- **Quality Criteria**:
  - You consider including specific security requirements, activities, and processes when creating third-party agreements
  - A vendor questionnaire is available and used to assess the strengths and weaknesses of your suppliers

*Maturity Level 2*

Stream A - Software Requirements:
- **Benefit**: Alignment of security requirements with other types of requirements
- **Activity**: Security requirements can originate from other sources including policies and legislation, known problems within the application, and intelligence from metrics and feedback. At this level, a more systematic elicitation of security requirements must be achieved by analysing different sources of such requirements. Ensure that appropriate input is received from these sources to help the elicitation of requirements. For example, organize interviews or brainstorm sessions (e.g., in the case of policy and legislation), analyze historical logs or vulnerability systems.
- Use a structured notation of security requirements across applications and an appropriate formalism that integrates well with how you specify other (functional) requirements for the project. This could mean, for example, extending analysis documents, writing user stories, etc.
- When requirements are specified, it is important to ensure that these requirements are taken into account during product development. Set up a mechanism to stimulate or force project teams to meet these requirements in the product. For example, annotate requirements with priorities, or influence the handling of requirements to enforce sufficient security appetite, while balancing against other non-functional requirements.
- **Quality Criteria**:
  - Security requirements take into consideration domain specific knowledge when applying policies and guidance to product development
  - Domain experts are involved in the requirements definition process
  - You have an agreed upon structured notation for security requirements
  - Development teams have a security champion dedicated to reviewing security requirements and outcomes

Stream B - Supplier Security:
- **Benefit**: Clearly defined security responsibilities of your software suppliers
- **Activity**: Increase your confidence in the capability of your suppliers for software security. Discuss concrete responsibilities and expectations from your suppliers and your own organization and establish a contract with the supplier. The responsibilities can be specific quality requirements or particular tasks, and minimal service can be detailed in a Service Level Agreement ([[_content/dictionary#S|SLA]]). A quality requirement example is that they will deliver software that is protected against the [[_content/dictionary#O|OWASP]] Top 10, and in case issues are detected, these will be fixed. A task example is that they have to perform continuous static code analysis, or perform an independent penetration test before a major release. The agreement stipulates liabilities and caps in case an important issue arises.
- Once you have implemented this for a few suppliers, work towards a standard agreement for suppliers that forms the basis of your negotiations. You can deviate from this standard agreement on a case by case basis, but it will help you to ensure you do not overlook important topics.
- **Quality Criteria**:
  - You discuss security requirements with the vendor when creating vendor agreements
  - Vendor agreements provide specific guidance on security defect remediation within an agreed upon timeframe
  - The organization has a templated agreement of responsibilities and service levels for key vendor security processes
  - You measure key performance indicators

*Maturity Level 3*

Stream A - Software Requirements:
- **Benefit**: Efficient and effective handling of security requirements in your organization
- **Activity**: Setup a security requirements framework to help projects elicit an appropriate and complete requirements set for their project. This framework considers the different types of requirements and sources of requirements. It should be adapted to the organizational habits and culture, and provide effective methodology and guidance in the elicitation and formation of requirements.
- The framework helps project teams increase the efficiency and effectiveness of requirements engineering. It can provide a categorisation of common requirements and a number of reusable requirements. Do remember that, while thoughtless copying is ineffective, the fact of having potential relevant requirements to reason about is often productive.
- The framework also gives clear guidance on the quality of requirements and formalizes how to describe them. For user stories, for instance, concrete guidance can explain what to describe in the definition of done, definition of ready, story description, and acceptance criteria.
- **Quality Criteria**:
  - A security requirements framework is available for project teams
  - The framework is categorized by common requirements and standards-based requirements
  - The framework gives clear guidance on the quality of requirements and how to describe them
  - The framework is adaptable to specific business requirements

Stream B - Supplier Security:
- **Benefit**: Alignment of software development practices with suppliers to limit security risks
- **Activity**: The best way to minimize the risk of issues in software is to align maximally and integrate closely between the different parties. From a process perspective, this means using similar development paradigms and introducing regular milestones to ensure proper alignment and qualitative progress. From a tools perspective, this might mean using similar build, verification and deployment environments, and sharing other supporting tools (e.g. requirements, architecture tools, or code repositories).
- In case suppliers cannot meet the objectives that you have set, implement compensating controls so that, overall, you meet your objectives. Execute extra activities (e.g., threat modelling before starting the actual implementation cycle) or implement extra tooling (e.g., 3rd party library analysis at solution intake). The more suppliers deviate from your requirements, the more work will be required to compensate.
- **Quality Criteria**:
  - The vendor has a secure [[_content/dictionary#S|SDLC]] that includes secure build, secure deployment, defect management, and incident management that align with those used in your organization
  - You verify the solution meets quality and security objectives before every major release
  - When standard verification processes are not available, you use compensating controls such as software composition analysis and independent penetration testing

#### Security Architecture

**Practice Overview**

The Security Architecture ([[_content/dictionary#S|SA]]) practice focuses on the security linked to components and technology you deal with during the architectural design of your software. Secure Architecture Design looks at the selection and composition of components that form the foundation of your solution, focusing on its security properties. Technology Management looks at the security of supporting technologies used during development, deployment and operations, such as development stacks and tooling, deployment tooling, and operating systems and tooling.

**Streams Overview**

*Stream A - Architecture Design*
The design of a software architecture can significantly impact the security posture of a software and the use of good security practices will improve the overall design.

*Stream B - Technology Management*
Technologies and frameworks are the cornerstones of any software solution. The security properties of these must be looked into to ensure an appropriate security level and to anticipate any potential issues herein.

**Activities by Maturity Level**

*Maturity Level 1*

Stream A - Architecture Design:
- **Benefit**: Sets of security basic principles available to product teams
- **Activity**: During design, technical staff on the product team use a short checklist of security principles. Typically, security principles include defense in depth, securing the weakest link, use of secure defaults, simplicity in design of security functionality, secure failure, balance of security and usability, running with least privilege, avoidance of security by obscurity, etc.
- For perimeter interfaces, the team considers each principle in the context of the overall system and identifies features that can be added to bolster security at each such interface. Limit these such that they only take a small amount of extra effort beyond the normal implementation cost of functional requirements. Note anything larger, and schedule it for future releases.
- Train each product team with security awareness before this process, and incorporate more security-savvy staff to aid in making design decisions.
- **Quality Criteria**:
  - You have an agreed upon checklist of security principles
  - You store your checklist in an accessible location
  - Relevant stakeholders understand security principles

Stream B - Technology Management:
- **Benefit**: Understanding of the security implications of technology choices
- **Activity**: Elicit technologies, frameworks and integrations within the overall solution to identify risk. Create and maintain an inventory of the different technologies and frameworks used by your teams to develop and deploy their products. Document the responsible teams (or individuals), the different versions used, and other relevant metadata (support, end of life, etc.).
- Align on a standardized way to assess your technologies to cater for security. As technologies come in different forms, such as programming languages, frameworks, databases, or application servers, you might need more than one approach. For programming languages, frameworks, databases, or application servers, you typically want to understand in what way security features are supported. For instance, frameworks often include libraries to help protect against common attacks, and databases provide different options for authentication, authorization, and data encryption. Understanding which features and components are available to implement security requirements, and how they should be used, is a prerequisite to providing teams with the necessary input to properly address security concerns.
- From the assessments, you learn which features are provided by which components and in what way they should be used. If gaps are identified when mapping existing solutions against the organization's security requirements, they are documented and provided to all potential users of these components. Use the outcome to classify the different technologies and frameworks from a security perspective.
- **Quality Criteria**:
  - You document which security features are available in a technology
  - You understand the security model behind a specific technology and the different security features and components
  - You know to which policies and standards a technology maps
  - You provide support for proper use of security features

*Maturity Level 2*

Stream A - Architecture Design:
- **Benefit**: Common security solutions for product teams
- **Activity**: Establish common design patterns and reference architectures that satisfy your organization's security objectives. A pattern or reference architecture represents a reusable solution for mitigating against the organization's most important threats, thus reducing the overall risk and potentially avoiding known pitfalls and vulnerabilities in software designs.
- A reference architecture considers the different security features you expect to see in a solution (for example, how and when to authenticate and authorize users, what type of input sanitization and output encoding you expect and to which data). It describes which elements of the architecture are responsible for what type of security features, and how are they supposed to integrate with other elements.
- Reference architectures are generally implementation-independent, but they do make use of established security principles and practices which form the foundation of the document. In some cases, reference architectures get quite specific and describe exactly which components to use and how to use them.
- Along with a reference architecture, a list of approved and recommended frameworks and packages simplifies the implementation of specific functions. Indicate clearly which libraries and frameworks should be preferred. Define the acceptable deployment options and the security controls required for each.
- **Quality Criteria**:
  - You have customized and reusable solutions for the most important threats to your software
  - Your reference architectures describe security functionality that satisfies applicable security requirements
  - You reference architectures help prevent known vulnerabilities in software designs

Stream B - Technology Management:
- **Benefit**: Standardized technology stacks with security assurance
- **Activity**: In this phase, the organization is starting to standardize technologies and frameworks to be used throughout the different applications. They have defined a (small) number of technology stacks that is consistently used and generally well understood by the staff. The need for support for exotic technologies is limited. As a result, the teams can focus on ensuring proper security support for a reasonably small set of technology stacks.
- From a security perspective, you now define guidelines for particular choices such as (web) frameworks, components and libraries, deployment platform, etc. These guidelines specify the secure usage of the specific technology and define clear responsibilities and integration guidelines for the different components. For instance, if a server-side [[_content/dictionary#M|MVC]] web framework is chosen, the guidelines would elaborate the security responsibilities of the [[_content/dictionary#U|UI]] components (View), the wiring (Control) and the business logic components (Model) and how to leverage framework-specific security features such as automatic input sanitization or output encoding.
- For each of the different technologies that are considered for use within your organization, a lightweight technology risk assessment is performed. This risk assessment is then verified by the party responsible for the overall security strategy.
- The outcome of this phase is a set of technologies documented with necessary security aspects and recommended solutions for given technical problems (how to implement authentication, what crypto protocols to use, etc.)
- **Quality Criteria**:
  - You have defined a list of technologies that have been assessed for security
  - For each approved technology or framework, you document the main risks
  - You have a technology adoption process with a specific gate for the security review
  - You have defined guidelines for secure use of technologies

*Maturity Level 3*

Stream A - Architecture Design:
- **Benefit**: Security architecture assurance at each stage of development
- **Activity**: Reference architectures are utilized and continuously evaluated for adoption and appropriateness. Software architecture has several domains, including reference architectures, which identify patterns and essential components of related applications; application architectures, which define aspects unique to specific applications; and solution architectures, which are integrations between application stacks. Just as the organization maintains a culture of constant improvement, the reference architectures evolve as well.
- Require that a designated Security Architect reviews all software designs against reference security architectures. The review includes the appropriate implementation of the required security controls, the appropriate use of the selected tools and frameworks, and a final judgment of the adequacy and effectiveness of the security design. Document issues and resolve them prior to implementation. In parallel, also review the security of provisioning and operations components, such as infrastructure setup, system baselines, deployment pipeline, and security monitoring.
- Based on these reviews, common themes in design flaws in security architecture are identified and incorporated into threat modeling processes, reference architectures, and coding standards. Ensure architecture documentation includes an overview of high-risk components, providing a monitoring priority for operations.
- Continuously upgrade the effectiveness of the implemented controls through user feedback, penetration testing, and coordination across product teams. Teams collect performance metrics during design, implementation, and operations and share them across the organization. Verify control implementation for both effectiveness and efficiency. Inefficient controls can degrade the overall security of a product if they result in end users' implementing workarounds.
- **Quality Criteria**:
  - The Security Architect can veto architecture decisions without proper security controls
  - Architects analyze how well controls work in the architecture context and receive feedback from implementation and operations
  - Architects recommend improved implementations of mitigating controls
  - An efficient control catalog exists for the organization's most important technical threats

Stream B - Technology Management:
- **Benefit**: Long-term assurance of security across all technologies
- **Activity**: Impose the use of standard technologies on all software development. At this point, the organization limits further divergence and defines a clear set of technologies that can be properly secured.
- Create a technology lifecycle management plan for the organization, outlining the introduction of new technologies and the deprecation of old ones. Communicate this plan to all teams, to keep them informed about technologies in which they should or should not invest. To enforce the technology lifecycle management, some organizations limit or even forbid changes to applications using deprecated technologies, making it financially more sensible to update the technologies before implementing more business changes.
- Establish a centralized team to ensure proper security understanding and usage of technologies and frameworks. Technical specialists of this team guide and coach other development teams on using frameworks and tools, including security features, and lead by example via proof-of-concept or reference implementations. To ensure that development teams build and operate a secure solution, this team may provide a pre-configured and vetted set of security solutions that others can directly use in their respective applications. Develop detailed documents on specific security solutions, or provide ready-to-use implementations of them.
- To facilitate the introduction of new technologies, establish a vetting process, including a security analysis with proper documentation of the results. Security-critical features are assessed deeply, including a code review of any components implementing a significant security control or mitigation.
- **Quality Criteria**:
  - You enforce a limited number of approved technologies for use within your organization
  - You have a security knowledge base per technology used
  - You have reusable code snippets for security functionality in a repository

### 3. Implementation

#### Security Practices:
- **Secure Build**: Activities to ensure that the process of creating executable software minimizes vulnerabilities.
- **Secure Deployment**: Ensuring the confidentiality and integrity of the application code and configuration in the deployment environment.
- **Defect Management**: Activities to ensure that security defects in the software are tracked and remediated appropriately.

### 4. Verification

#### Security Practices:
- **Architecture Assessment**: Review of the high-level technical architecture for key security features and controls.
- **Requirements-driven Testing**: Testing the software to verify that it meets the security requirements.
- **Security Testing**: Testing the software to verify that the components function as expected and to identify potential vulnerabilities.

### 5. Operations

#### Security Practices:
- **Incident Management**: Activities to ensure that security events involving the software are handled appropriately.
- **Environment Management**: Activities to ensure that the production environment is configured with proper security controls.
- **Operational Management**: Activities to ensure that security is maintained in the software as it evolves.
