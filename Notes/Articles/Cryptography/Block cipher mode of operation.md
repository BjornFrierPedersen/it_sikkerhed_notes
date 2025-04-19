Source: https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

## Overview
- Block cipher modes of operation are algorithms that use a block cipher to provide information security such as confidentiality or authenticity.
- A block cipher by itself is suitable for the secure cryptographic transformation of one fixed-length group of bits called a block.

## Initialization Vector ([[_content/dictionary#I|IV]])
- IV is a unique binary sequence used for each encryption operation to ensure distinct ciphertexts.
- It must be non-repeating and, for some modes, random.

## Padding
- Some modes require padding of the final data fragment to a full block if it is smaller than the current block size.
- Modes like [[_content/dictionary#C|CFB]], [[_content/dictionary#O|OFB]], and [[_content/dictionary#C|CTR]] do not require padding.

## Common Modes
- [[_content/dictionary#E|ECB]] (Electronic Codebook): Encrypts each block separately; not recommended due to lack of diffusion.
- [[_content/dictionary#C|CBC]] (Cipher Block Chaining): Each block of plaintext is XORed with the previous ciphertext block before encryption.
- [[_content/dictionary#C|CFB]] (Cipher Feedback): Turns a block cipher into a self-synchronizing stream cipher.
- [[_content/dictionary#O|OFB]] (Output Feedback): Makes a block cipher into a synchronous stream cipher.
- [[_content/dictionary#C|CTR]] (Counter): Turns a block cipher into a stream cipher using a counter.

## Authenticated Encryption Modes
- [[_content/dictionary#G|GCM]] (Galois/Counter Mode): Combines counter mode encryption with Galois mode authentication.
- [[_content/dictionary#C|CCM]] (Counter with [[_content/dictionary#C|CBC]]-[[_content/dictionary#M|MAC]]): Provides both authentication and confidentiality.
- [[_content/dictionary#S|SIV]] (Synthetic Initialization Vector): Nonce-misuse resistant mode.
- [[_content/dictionary#A|AES]]-[[_content/dictionary#G|GCM]]-[[_content/dictionary#S|SIV]]: Provides similar performance to GCM with misuse resistance.

## Error Propagation
- Describes how decryption behaves during bit errors, affecting different decrypted bits.

## Other Modes
- Disk encryption: Uses special purpose modes like [[_content/dictionary#L|LRW]], [[_content/dictionary#X|XEX]], and [[_content/dictionary#X|XTS]] for narrow-block encryption and [[_content/dictionary#C|CMC]], [[_content/dictionary#E|EME]] for wide-block encryption.