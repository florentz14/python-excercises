# -------------------------------------------------
# File Name: 05_bitwise_operators.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Demonstrates bitwise operators (&, |, ^, ~, <<, >>) with binary
# -------------------------------------------------

a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(f"a = {a} (binary: {bin(a)}), b = {b} (binary: {bin(b)})")

# Bitwise AND
print(f"a & b: {a & b} (binary: {bin(a & b)})")

# Bitwise OR
print(f"a | b: {a | b} (binary: {bin(a | b)})")

# Bitwise XOR
print(f"a ^ b: {a ^ b} (binary: {bin(a ^ b)})")

# Bitwise NOT
print(f"~a: {~a} (binary: {bin(~a)})")

# Left shift
print(f"a << 1: {a << 1} (binary: {bin(a << 1)})")

# Right shift
print(f"a >> 1: {a >> 1} (binary: {bin(a >> 1)})")

# Another example
c = 12  # Binary: 1100
d = 6   # Binary: 0110
print(f"\nc = {c} (binary: {bin(c)}), d = {d} (binary: {bin(d)})")
print(f"c & d: {c & d} (binary: {bin(c & d)})")