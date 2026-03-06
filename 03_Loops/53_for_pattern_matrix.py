"""For loop: Matrix of symbols.
Creates a 4x5 grid showing row/col coordinates.
"""
# Author: Florentino Báez


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
