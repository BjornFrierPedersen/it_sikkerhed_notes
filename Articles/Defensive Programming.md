Overview
	1. Defensive programming aims to develop software that can handle unforeseen circumstances and potential security abnormalities.
	2. It is crucial for high availability, safety, and security.

Key Practices
	1. General Quality: Reducing software bugs and problems.
	2. Comprehensibility: Making source code readable and understandable.
	3. Predictable Behavior: Ensuring software behaves predictably despite unexpected inputs or user actions.

Secure Programming
	1. Subset of Defensive Programming: Focuses on computer security.
	2. Primary Objective: Avoiding bugs to reduce the attack surface.
	3. Example: Secure handling of input to prevent buffer overflow exploits.

Offensive Programming
	1. Category of Defensive Programming: Emphasizes handling only external errors.
	2. Trusting Internal Data: Internal data and software components are trusted.

Techniques
	1. Intelligent Source Code Reuse: Reusing tested and known-to-work code.
	2. Legacy Problems: Addressing issues with old designs and code.
	3. Canonicalization: Avoiding bugs due to non-canonical input.
	4. Low Tolerance Against Potential Bugs: Proactively protecting against known and unknown security exploits.

Three Rules of Data Security
	1. All data is important until proven otherwise.
	2. All data is tainted until proven otherwise.
	3. All code is insecure until proven otherwise.