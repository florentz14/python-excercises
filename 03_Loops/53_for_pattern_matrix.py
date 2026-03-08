# -------------------------------------------------
# File Name: 53_for_pattern_matrix.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Matrix of symbols.
# -------------------------------------------------

print("Matriz Rectangular de Símbolos")
print("=" * 30)

rows = 4
cols = 5

# Outer loop: each row
for i in range(rows):
    # Inner loop: each column
    for j in range(cols):
        print(f"[{i},{j}]", end=" ")
    print()
