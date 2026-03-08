# -------------------------------------------------
# File Name: 51_for_pattern_triangle.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Triangle number pattern.
# -------------------------------------------------

print("Patrón Triangular de Números")
print("=" * 30)

# Outer loop: row count (1 to 5)
for i in range(1, 6):
    # Inner loop: print numbers 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
