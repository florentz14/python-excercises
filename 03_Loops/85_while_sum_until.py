"""
While loop: Sum numbers until -1.
Accumulates user input; stops when user enters -1.

# Author: Florentino Báez
"""

print("Example: Sum numbers (enter -1 to stop)")
print("-" * 40)

total = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num

print(f"Total sum: {total}")
