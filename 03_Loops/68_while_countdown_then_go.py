# -------------------------------------------------
# File Name: 58_while_countdown_then_go.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Simple while-loop example — countdown from 5 then print "Go!".
# -------------------------------------------------

print("=" * 40)
print("While #2 – Countdown then Go")
print("=" * 40)

# Start value
n = 5

# Loop while n is greater than 0
while n > 0:
    # Print the current countdown number
    print(n)
    # Decrement by 1 each iteration
    n -= 1

# After the loop ends, print the final message
print("Go!")
print("=" * 40)
