"""
While loop: Sum positive numbers until 0.
User enters numbers; sum only positives, stop on zero or negative.

# Author: Florentino Báez
"""

total = 0
print("Enter positive numbers (0 or negative to stop):")
while True:
    num = int(input("Number: "))
    if num <= 0:
        break
    total += num
print(f"Sum of positives: {total}")
