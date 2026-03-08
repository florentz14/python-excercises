# -------------------------------------------------
# File Name: 89_while_nested.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Nested while loops pattern.
# -------------------------------------------------

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
