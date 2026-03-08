# -------------------------------------------------
# File Name: 29_rotate_list.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Rotates lists left or right by n positions.
# -------------------------------------------------

def rotate_left(lst, n):
    """Rotate list left by n positions."""
    return lst[n:] + lst[:n]

def rotate_right(lst, n):
    """Rotate list right by n positions."""
    return lst[-n:] + lst[:-n]

original = [1, 2, 3, 4, 5]
print("Original:", original)
print("Rotate left by 2:", rotate_left(original, 2))
print("Rotate right by 2:", rotate_right(original, 2))

# Using collections.deque
from collections import deque
dq = deque(original)
dq.rotate(-2)  # Negative for left
print("Rotate left with deque:", list(dq))