# -------------------------------------------------
# File Name: 59_for_pattern_inverted.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Inverted triangle pattern.
# -------------------------------------------------

print("Triángulo Invertido")
print("=" * 30)

size = 5

# Rows from size down to 1
for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
