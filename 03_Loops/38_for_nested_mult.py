"""For loop: Nested loops multiplication grid.
Prints a 3x3 multiplication table.
"""
# Author: Florentino Báez


for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
