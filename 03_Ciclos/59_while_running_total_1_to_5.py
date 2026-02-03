# -------------------------------------------------
# File Name: 59_while_running_total_1_to_5.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Simple while-loop example — running total from 1 to 5.
# -------------------------------------------------

print("=" * 40)
print("While #3 – Running Total (1 to 5)")
print("=" * 40)

# Initialize total and counter
total = 0
i = 1

# Loop while i is less than or equal to 5
while i <= 5:
    # Add current i to the running total
    total += i
    # Print current counter and running total
    print("i:", i, "total:", total)
    # Increment the counter
    i += 1

print("=" * 40)
