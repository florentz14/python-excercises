"""
While loop: Nested while loops pattern.
Prints a right-aligned triangle of asterisks (1, 2, 3 stars).

# Author: Florentino Báez
"""

print("Example: Nested while loops pattern")
print("-" * 40)

outer = 1
while outer <= 3:
    inner = 1
    while inner <= outer:
        print("*", end="")
        inner += 1
    print()
    outer += 1
