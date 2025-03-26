Source: https://en.wikipedia.org/wiki/Secure_coding

	• Definition: 
		○ Secure coding is the practice of developing software to prevent security vulnerabilities caused by defects, bugs, and logic flaws.
	• Common Vulnerabilities:
		○ Buffer Overflow: Occurs when data exceeds a buffer’s capacity, potentially leading to security issues like stack smashing or program termination.
		○ Format-String Attack: Happens when user input is improperly formatted, leading to potential security bugs.
		○ Integer Overflow: Occurs when an arithmetic operation results in a value too large to be represented, causing potential bugs and exploits.
		○ Path Traversal: A vulnerability where untrusted paths allow unauthorized file access.
	• Prevention Techniques:
		○ Use functions like strncpy to prevent buffer overflows.
		○ Properly format inputs to avoid format-string attacks.
		○ Check for integer overflow by validating arithmetic operations.
		○ Validate and sanitize file paths to prevent path traversal attacks.
	• Importance: 
Secure coding helps reduce or eliminate vulnerabilities before software deployment, ensuring better protection against insider attacks and application security threats.