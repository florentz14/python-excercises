# -------------------------------------------------
# File Name: 36_remove_duplicates.py
# Purpose: Convert list to set for uniqueness
# Description: Use set() to remove duplicates from a list.
#              Note: order is not preserved (sets are unordered).
# -------------------------------------------------

print("Remove Duplicates Using Sets")
print("-" * 40)

# List with duplicates
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

print("Original list:", numbers)
unique_numbers = list(set(numbers))
print("Unique (order not preserved):", unique_numbers)
print()

print("Original words:", words)
unique_words = list(set(words))
print("Unique words:", unique_words)
print()

# Preserving order: use dict.fromkeys() or manual loop
def unique_preserve_order(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

ordered_unique = unique_preserve_order(numbers)
print("Unique with order preserved:", ordered_unique)
