**Source:** https://security.stackexchange.com/questions/41702/how-do-poor-quality-initialization-vectors-affect-the-security-of-cbc-mode

**Question:** 
How do poor-quality initialization vectors affect the security of [[_content/dictionary#C|CBC]] mode?
From what I have read (looking specifically at [[_content/dictionary#A|AES]] in Cipher Block Chaining mode), initialization vectors should be non-repeating, or better, under some circumstances at least, totally unpredictable. If we consider the following sequence of "weakening" [[_content/dictionary#I|IV]]s:

Cryptographically sound random number

Any old "random number"

A non-repeating, monotonically increasing, non-continuous counter (such as a high-resolution clock)

A 1-by-1 counter, large enough not to repeat in, say 10 times the expected usefulness of the protected data.

A constant [[_content/dictionary#I|IV]]

An all-zeros [[_content/dictionary#I|IV]]

Now, as we weaken the [[_content/dictionary#I|IV]], what attacks become possible, and at what stage in the weakening? I am particularly interested in storing data "at rest", and for the moment, without authentication.

**Answer:** 
There are two distinct "dangers" with [[_content/dictionary#C|CBC]]. Remember that [[_content/dictionary#C|CBC]] works the following way: to encrypt a block, first [[_content/dictionary#X|XOR]] it with the previous encrypted block. The [[_content/dictionary#I|IV]] is just the "previous encrypted block" for the very first block to encrypt. The idea is that a block cipher is a deterministic permutation: with the same key and the same input block, you get the same output. The XOR with the previous encrypted block is meant as a "randomization". So the dangers are:

Block collisions.
Chosen-plaintext attacks.
Block collisions are when, through bad luck or lack of randomness, the [[_content/dictionary#X|XOR]] of a block with the previous block leads to a value which was already obtained beforehand.

For instance, if you use a fixed [[_content/dictionary#I|IV]] (all-zero or not, it does not matter), then two messages which begin with the same sequence of bytes will yield two encrypted streams which also begin with the same sequence of bytes. This allows outsiders ("attackers") to see that the two files were identical up to some point, which can be pinpointed with block granularity. This is considered a bad thing; encryption is supposed to prevent such kinds of leaks.

If using a counter as [[_content/dictionary#I|IV]], you may still have such collisions, because counters have structure, and "normal" data also has structure. As an extreme case, suppose that the encrypted message also begins with a counter (e.g. it is part of a protocol in which messages have a header which begins with a sequence number): the counter-for-[[_content/dictionary#I|IV]] and that counter may cancel each other with the [[_content/dictionary#X|XOR]], leading you back to the fixed-[[_content/dictionary#I|IV]] situation. This is bad. We really prefer it when encryption systems provide confidentiality without requiring some complex requirements on the plaintext format. A high-res clock as "counter" could also incur the same issue.

Chosen-plaintext attacks are when the attacker can choose part of the data that is to be encrypted. With [[_content/dictionary#C|CBC]], if the attacker can predict the [[_content/dictionary#I|IV]], then he can adjust his plaintext data to match it.

This is the basis of the [[_content/dictionary#B|BEAST]] attack. In the [[_content/dictionary#B|BEAST]] attack, the attacker tries to "see through" [[_content/dictionary#S|SSL]]. In [[_content/dictionary#S|SSL]] 3.0 and [[_content/dictionary#T|TLS]] 1.0, each record is encrypted with [[_content/dictionary#C|CBC]], and the [[_content/dictionary#I|IV]] for each record is the last encrypted block of the previous record: an attacker observing the wire and in position to input some data in the stream can push just enough bytes to trigger emission of a record, observe it, and thus deduce the [[_content/dictionary#I|IV]] which will be used for the next record, whose contents will begin by the next byte the attacker will push.

Of all the [[_content/dictionary#I|IV]] generation methods you show, only the first one ([[_content/dictionary#I|IV]] generated with a cryptographically strong [[_content/dictionary#P|PRNG]]) will protect you against chosen-plaintext attacks. This is what was added to [[_content/dictionary#T|TLS]] 1.1.

On a specific situation like your credit cards in a database, some of the possible attacks may or may not apply. However, don't try to "cut corners" too much. If you put user data in the database, then chosen-plaintext attacks may apply: an attacker who can look at your database (e.g. with some [[_content/dictionary#S|SQL]] injection technique) may also act as a "basic user" to feed you with phony credit card numbers, just to see what shows up in the database.

In particular, in that scenario, if you use deterministic encryption (and that's exactly what you get with a fixed [[_content/dictionary#I|IV]], be it all-zeros or not), then the attacker can simply brute-force credit card numbers: a number is 16 digits, but one of them is a checksum, and the first four or six digits are from the bank, and the remaining one are not necessarily "random", so such kinds of attacks can be effective.

Bottom-line is that if you use [[_content/dictionary#C|CBC]], then you must use [[_content/dictionary#C|CBC]] properly, i.e. with a strongly random [[_content/dictionary#I|IV]]. If you prefer a monotonic counter (or clock), then don't use [[_content/dictionary#C|CBC]]; instead, use a mode which is known to be perfectly happy with a monotonic counter, e.g. [[_content/dictionary#G|GCM]]. It is already hard enough to achieve security when cryptographic algorithms are used by the book, so any "creativity" here is to be shunned.

And, of course, contents which has been encrypted with a given key is no more secret than the key itself. When an attacker has read access to your database, he might have read access to more than the database -- in particular, to the encryption key itself. It depends on where you store the key, and also on the extent of the attacker's access ([[_content/dictionary#S|SQL]] injection, stolen backup tape, front-end system complete hijack,...).

**Explained in simple terms**

Imagine encryption as putting your data in a lockbox. [[_content/dictionary#C|CBC]] mode is a specific way to lock that box, and the Initialization Vector ([[_content/dictionary#I|IV]]) is like a special key component that changes how the lock works.

Here's what happens with different types of [[_content/dictionary#I|IV]]s:

- **Strong Random [[_content/dictionary#I|IV]] (Best)**: Using a completely random component each time you lock the box. Nobody can predict the pattern, so it's very secure.

- **Weak Random or Predictable [[_content/dictionary#I|IV]]**: Like using a component that follows a pattern. If someone figures out the pattern, they can start guessing what's in your lockbox.

- **Counter as [[_content/dictionary#I|IV]]**: Using numbers in sequence (1, 2, 3...). This can be problematic if your data also contains sequences that might cancel each other out.

- **Fixed [[_content/dictionary#I|IV]] (Worst)**: Using the exact same component every time. This allows attackers to see patterns in your encrypted data. If two documents start the same way, their encrypted versions will also start the same way.

The biggest risks with poor [[_content/dictionary#I|IV]]s are:

1. **Pattern Detection**: Attackers can see when encrypted items are identical or similar, leaking information.

2. **Predictable Encryption**: If attackers can predict your [[_content/dictionary#I|IV]], they can manipulate what goes into the encryption process to reveal secrets.

For maximum security, always use a cryptographically strong random [[_content/dictionary#I|IV]] or switch to a different encryption mode (like [[_content/dictionary#G|GCM]]) if you need to use a predictable counter.