"""For loop: range() examples.
Demonstrates range() with start, stop, and step parameters.
"""
# Author: Florentino Báez


# Range 4 to 7 (8 is excluded)
for v in range(4, 8):
    print(v)

print("---")

# Range 2 to 6
for o in range(2, 7):
    print(o)

print("---")

# Range 1 to 5
for i in range(1, 6):
    print(i)

print("---")

# Range 0 to 10, step 2 (even numbers)
for i in range(0, 11, 2):
    print(i)

print("---")

# Range 1 to 9, step 2 (odd numbers)
for i in range(1, 10, 2):
    print(i)

print("---")

# Range 5 to 0, step -1 (countdown)
for i in range(5, 0, -1):
    print(i)
