# -------------------------------------------------
# File Name: 01_complex.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Create complex numbers (1+2j), real/imaginary parts,
# -------------------------------------------------

# Import the cmath module for complex number operations
import cmath

# Examples of different numeric types in Python
x = 1+2j   # complex: real=1, imaginary=2
print(x)

# Display the real and imaginary parts of the complex number
print("Real part:", x.real)
print("Imaginary part:", x.imag)

# Perform and display various arithmetic operations
print("Addition:", x + (2 + 3j))
print("Subtraction:", x - (1 + 1j))
print("Multiplication:", x * (0 + 2j))
print("Division:", x / (1 + 0j))
print("Conjugate:", x.conjugate())
print("Magnitude:", abs(x))
print("Phase (angle):", cmath.phase(x))
