# -------------------------------------------------
# File Name: 04_slice.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Slice a Tuple.
#              Slicing extracts sub-tuples with the syntax
#              tuple[start:stop:step]. Omitting start defaults
#              to 0, omitting stop defaults to len(). A step
#              of -1 reverses the tuple.
# -------------------------------------------------

print("Example 4: Slice a tuple")
print("-" * 40)

letters = ("a", "b", "c", "d", "e", "f")
print("Original tuple:", letters)

print("First 3 elements:", letters[0:3])       # ('a', 'b', 'c')
print("Elements from index 2 to 4:", letters[2:5])  # ('c', 'd', 'e')
print("Every second element:", letters[::2])   # ('a', 'c', 'e') — step of 2
print("Reverse tuple:", letters[::-1])         # ('f', 'e', 'd', 'c', 'b', 'a')
