Quantum Encryption of Images using Bitwise XOR and QRNG

Article:
http://muonray.blogspot.com/2022/02/quantum-encryption-of-images-in-python.html

Overview

This repository demonstrates image encryption using the bitwise XOR operation combined with either:

A pseudo-random key stream

A Quantum Random Number Generator (QRNG)

Anti-correlated entangled photon image data

The approach extends classical data encryption to image pixel matrices, treating each pixel value as binary data.

Core Encryption Principle

The encryption mechanism is based on the properties of the XOR operation:

If:

xor(a, b) = c

Then:

xor(c, b) = a
xor(c, a) = b

Where:

a = original image

b = encryption key

c = encrypted image (ciphertext)

Encryption
c = xor(a, b)
Decryption
a = xor(c, b)

Because XOR is symmetric and reversible, the same operation is used for both encryption and decryption.

Key Generation Methods

This project supports two QRNG-based key generation approaches:

1. Quantum Random Seed

Quantum randomness is used as a seed for generating a secure random key stream.

2. Quantum Superposition Sampling

Randomness is derived from superposition states (e.g., H and V polarization modes), producing inherently unpredictable key material.

Entangled Image Key Sharing

The system can also use correlated photon images captured from an entangled photon source:

Alice receives one half of the correlated image

Bob receives the anti-correlated half

These images serve as a shared secret key

The quantum key is transmitted through a secure quantum channel, while the encrypted classical image is transmitted separately.

This creates a form of quantum-assisted symmetric encryption.

Two-Way Secure Communication

The communication channel is bidirectional:

Alice encrypts → Bob decrypts

Bob encrypts → Alice decrypts

Both parties share correlated quantum-derived key material.

Security Considerations

When implemented correctly:

XOR encryption with a truly random, single-use key (one-time pad) is theoretically unbreakable.

Security depends entirely on:

Key randomness

Key secrecy

Key non-reuse

If the key is reused or predictable, the system becomes vulnerable.

Extensibility

While XOR encryption can be embedded inside more complex cryptographic overlays, this implementation focuses on:

Conceptual clarity

Computational efficiency

Demonstrating quantum-assisted key generation

Important Note

This repository demonstrates concepts in quantum-assisted encryption and QRNG integration.
It is intended for educational and experimental purposes.

For production security systems, formal cryptographic standards and peer-reviewed implementations should be used.