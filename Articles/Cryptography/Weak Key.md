Source: https://en.wikipedia.org/wiki/Weak_key

## Overview
- Weak keys are specific keys that cause a cipher to behave in undesirable ways.
- They represent a very small fraction of the overall keyspace, making them unlikely to cause security problems when generated randomly.

## Historical Origins
- Rotor-based cipher machines from 1925 onwards had implementation flaws leading to weak keys.
- The [[_content/dictionary#T|T52]] stream cipher machine had notable weak key problems detected by the British during [[_content/dictionary#W|WWII]].

## Weak Keys in DES
- [[_content/dictionary#D|DES]] (Data Encryption Standard) has specific weak and semi-weak keys.
- Weak keys produce identical subkeys, causing the encryption function to be self-inverting.
- Semi-weak keys produce two different subkeys, used eight times each in the algorithm.

## List of Algorithms with Weak Keys
- [[_content/dictionary#D|DES]], [[_content/dictionary#R|RC4]], [[_content/dictionary#I|IDEA]], [[_content/dictionary#B|Blowfish]], [[_content/dictionary#G|GMAC]], [[_content/dictionary#R|RSA]], and [[_content/dictionary#D|DSA]] are examples of algorithms with weak keys.
- Weak keys in these algorithms can lead to predictable relationships between plaintext and ciphertext or compromised security.

## No Weak Keys as a Design Goal
- The goal is to have a flat keyspace where all keys are equally strong.
- Countermeasures include checking generated keys against known weak keys or rejecting weak keys during key scheduling.