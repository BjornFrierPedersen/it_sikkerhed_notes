# Random Numbers in Cryptography

## Explained in Simple Terms
Random numbers in cryptography are like the unpredictable dice rolls that make a game fair. If someone could predict the dice, they could cheat. Similarly, cryptographic systems need truly unpredictable random numbers to generate keys, initialization vectors, and other critical values. If an attacker can predict these "random" values, they can break the encryption. The challenge is that computers are designed to be predictable and deterministic, so generating true randomness is surprisingly difficult and requires special techniques.

## Types of Random Number Generators

### 1. True Random Number Generators (TRNGs)
- Also called Hardware Random Number Generators
- Generate randomness from physical processes
- Examples: radioactive decay, atmospheric noise, thermal noise, quantum effects
- Characteristics:
  - Non-deterministic (unpredictable)
  - Slower generation rate
  - Not reproducible
  - Truly random output

### 2. Pseudo-Random Number Generators (PRNGs)
- Algorithm-based generators that produce sequences that appear random
- Start with a seed value and apply mathematical transformations
- Examples: Linear Congruential Generators, Mersenne Twister
- Characteristics:
  - Deterministic (will produce the same sequence given the same seed)
  - Fast generation
  - Reproducible if seed is known
  - Only appears random

### 3. Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs)
- Specialized PRNGs designed specifically for cryptographic use
- Designed to resist prediction even if parts of their state become known
- Examples: [[_content/dictionary#H|HMAC]]-[[_content/dictionary#D|DRBG]], [[_content/dictionary#C|CTR]]-DRBG, Fortuna
- Characteristics:
  - Deterministic but cryptographically unpredictable
  - Pass statistical randomness tests
  - Cannot be practically distinguished from true randomness
  - Resistant to various cryptographic attacks

## Sources of Randomness

### Hardware-Based Sources
- **Intel [[_content/dictionary#R|RDRAND]]/[[_content/dictionary#R|RDSEED]]**: [[_content/dictionary#C|CPU]] instructions for hardware-based random number generation
- **Dedicated hardware random number generators**: Special devices that measure physical phenomena
- **Quantum random number generators**: Based on inherently random quantum processes
- **Electronic noise**: Thermal noise in resistors or semiconductor components

### [[_content/dictionary#O|OS]]-Based Collection
- **Linux /dev/random and /dev/urandom**: Kernel entropy pools collecting environmental noise
- **Windows [[_content/dictionary#C|CryptGenRandom]]**: Microsoft's cryptographic random number generator
- **macOS/iOS [[_content/dictionary#S|SecRandomCopyBytes]]**: Apple's secure random number generation [[_content/dictionary#A|API]]

### Environmental Sources
- **User input timing**: Keystroke timing, mouse movements
- **Network traffic patterns**: Timing and content variations
- **System performance metrics**: Disk access times, interrupt timings
- **Sensor data**: Microphone noise, camera sensor noise, accelerometer data

## Entropy in Random Number Generation

### What is Entropy?
- Measure of unpredictability or randomness
- Typically measured in bits
- Higher entropy means more unpredictability
- Critical concept for seed generation in CSPRNGs

### Entropy Collection
- Process of gathering unpredictable data from various sources
- Mixed into an "entropy pool" maintained by the system
- Used to seed and periodically reseed PRNGs

### Entropy Depletion
- When a system uses randomness faster than it can gather new entropy
- Can lead to reduced security in cryptographic operations
- Especially problematic in embedded systems, virtualized environments, and during system startup

## Attacks on Random Number Generators

### Seed Prediction
- Attacking a [[_content/dictionary#P|PRNG]] by attempting to determine or influence its seed
- If the seed is compromised, all subsequent "random" output is predictable

### State Compromise Extension Attacks
- Even after a [[_content/dictionary#P|PRNG]] is compromised, it should eventually recover security if it gets new entropy
- Some poorly designed PRNGs never recover security after compromise

### Side-Channel Attacks
- Exploiting physical information leakage (timing, power consumption, etc.) to infer [[_content/dictionary#R|RNG]] state
- Can potentially extract information about random numbers being generated

### Implementation Flaws
- Improper seeding (e.g., using time() as the only seed)
- Failure to initialize [[_content/dictionary#R|RNG]] state properly
- Using non-cryptographic PRNGs for security purposes

## Notable [[_content/dictionary#R|RNG]] Failures

### Debian OpenSSL Vulnerability (2008)
- A code change reduced entropy in the OpenSSL random number generator
- Limited the possible keys to just 32,768 values
- Affected [[_content/dictionary#S|SSL]]/[[_content/dictionary#T|TLS]] keys, [[_content/dictionary#S|SSH]] keys, and other cryptographic material

### Dual [[_content/dictionary#E|EC]] [[_content/dictionary#D|DRBG]] Backdoor
- A [[_content/dictionary#N|NIST]]-standardized [[_content/dictionary#P|PRNG]] suspected to contain a backdoor
- Allowed those who knew a secret value to predict the output
- Allegedly promoted by the [[_content/dictionary#N|NSA]]

### [[_content/dictionary#P|PlayStation]] 3 [[_content/dictionary#E|ECDSA]] Implementation
- Sony used the same random number for every signature
- Allowed complete recovery of the private key
- Led to the compromise of the [[_content/dictionary#P|PlayStation]] 3's security system

### Android Bitcoin Wallet Vulnerability (2013)
- Java [[_content/dictionary#S|SecureRandom]] implementation in Android had flaws
- Generated repeated values in some cases
- Led to theft of bitcoins from affected wallets

## Testing Random Number Quality

### Statistical Tests
- **[[_content/dictionary#N|NIST]] Statistical Test Suite**: Comprehensive set of tests for randomness
- **Diehard Tests**: Battery of statistical tests for random number generators
- **TestU01**: C library implementing multiple [[_content/dictionary#R|RNG]] tests

### Visual Analysis
- Plotting generated values can reveal patterns not apparent in statistical tests
- 2D and 3D visualizations can help identify structure in supposedly random data

## Best Practices for Cryptographic Randomness

### Use Established CSPRNGs
- Rely on well-vetted, widely reviewed implementations
- Examples: 
  - OpenSSL's RAND_bytes()
  - [[_content/dictionary#N|NIST]]-approved [[_content/dictionary#D|DRBG]] implementations
  - /dev/urandom on Linux (for most applications)
  - [[_content/dictionary#C|CryptGenRandom]]() on Windows

### Proper Seeding
- Ensure CSPRNGs are seeded with sufficient entropy
- Gather entropy from multiple sources when possible
- Be especially careful during system startup when entropy may be limited

### Regular Reseeding
- Periodically introduce fresh entropy into long-running PRNGs
- Helps protect against state compromise

### Secure Implementation
- Protect [[_content/dictionary#R|RNG]] state in memory
- Clear sensitive values after use
- Avoid exposing internal state or seeds

### Testing and Validation
- Verify [[_content/dictionary#R|RNG]] output passes statistical tests
- Monitor for implementation or hardware issues
- Consider formal verification for critical implementations

## Random Numbers in Different Cryptographic Contexts

### Key Generation
- Requires highest quality randomness
- Directly impacts system security
- Use hardware RNGs or well-seeded CSPRNGs

### Nonces and Initialization Vectors
- Must be unpredictable in many protocols
- Never reuse across different encryptions with the same key
- May need to be random or merely unique depending on the algorithm

### Salts for Password Hashing
- Need to be unique but not necessarily unpredictable
- Should be stored alongside the hash
- Prevent precomputation attacks like rainbow tables

### Challenge-Response Protocols
- Require unpredictable random values
- Prevent replay attacks and ensure freshness 