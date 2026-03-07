# -------------------------------------------------
# File Name: 31_modify_sets.py
# Purpose: Summary of set modification methods
# Description: add(), remove(), discard(), pop(), clear() with examples.
# -------------------------------------------------

print("Set Modification Methods")
print("-" * 40)

# add(element): add a single element
s = {1, 2, 3}
print("Original:", s)
s.add(4)
print("After add(4):", s)
s.add(2)  # duplicate, no change
print("After add(2) (duplicate):", s)
print()

# remove(element): remove element, raises KeyError if not found
s = {1, 2, 3}
s.remove(2)
print("After remove(2):", s)
# s.remove(99)  # KeyError if uncommented
print()

# discard(element): remove element, no error if not found
s = {1, 2, 3}
s.discard(2)
print("After discard(2):", s)
s.discard(99)  # no error
print("After discard(99) (not in set):", s)
print()

# pop(): remove and return arbitrary element, KeyError if empty
s = {10, 20, 30}
popped = s.pop()
print("Popped:", popped, "| Remaining:", s)
print()

# clear(): remove all elements
s = {1, 2, 3}
s.clear()
print("After clear():", s, "| len =", len(s))
