# Digital Signatures

## Source: https://en.wikipedia.org/wiki/Digital_signature

## Overview
[[_content/dictionary#D|Digital signatures]] are cryptographic schemes used to verify the authenticity of digital messages or documents.
They provide confidence that a message came from a known sender and has not been altered.

## Key Components
- Key Generation: Involves creating a private key and a corresponding public key.
- Signing: Uses the private key to generate a signature for a message.
- Verification: Uses the public key to verify the authenticity of the signature.

## Applications
Commonly used in software distribution, financial transactions, and contract management.
[[_content/dictionary#D|Digital signatures]] ensure the integrity and authenticity of electronic documents.

## Security Properties
- Authentication: Confirms the identity of the sender.
- Non-repudiation: Prevents the sender from denying the authenticity of their signature.
- Integrity: Ensures the message has not been altered.

## Challenges and Precautions
- Replay Attacks: Valid signed messages can be maliciously reused.
- Smart Cards: Used to store private keys securely and require a [[_content/dictionary#P|PIN]] for activation.
- [[_content/dictionary#W|WYSIWYS]] (What You See Is What You Sign): Ensures the signed content is exactly what the signer intended.

## Legal and Practical Use
- [[_content/dictionary#D|Digital signatures]] have legal significance in many countries.
- They are equivalent to handwritten signatures but are more secure and harder to forge.