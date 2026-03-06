# -------------------------------------------------
# File Name: 05_slice.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Slice a List.
#              list[start:stop:step] extracts a sub-list.
#              Omit start for 0, omit stop for len().
#              Step of -1 reverses the list.
# -------------------------------------------------

print("Example 5: Slice a list")
print("-" * 40)

letters = ["a", "b", "c", "d", "e", "f"]
print("Original list:", letters)

print("First 3 elements:", letters[0:3])        # ['a', 'b', 'c']
print("Elements from index 2 to 4:", letters[2:5])  # ['c', 'd', 'e']
print("Every second element:", letters[::2])    # ['a', 'c', 'e']
print("Reverse list:", letters[::-1])           # ['f', 'e', 'd', 'c', 'b', 'a']
