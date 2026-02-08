# ---------------------------------------------------------------------------
# Sets - 04: Remove Set Items
# ---------------------------------------------------------------------------
# Description: Remove items from a set using remove(), discard(), pop(),
#              clear(), or del. Each method behaves differently.
# ---------------------------------------------------------------------------

fruits = {"apple", "banana", "cherry", "pineapple", "grape", "mango", "kiwi"}
print("Original:", fruits)

# =========================================================================
# remove() - Removes the specified item. Raises KeyError if not found.
# =========================================================================

fruits.remove("banana")
print("\nAfter remove('banana'):", fruits)

# Error if item doesn't exist
try:
    fruits.remove("pear")
except KeyError as e:
    print(f"remove('pear') Error: {e}")

# =========================================================================
# discard() - Removes the specified item. NO error if not found.
# =========================================================================

fruits.discard("cherry")
print("\nAfter discard('cherry'):", fruits)

# No error if item doesn't exist
fruits.discard("pear")  # Does nothing, no error
print("After discard('pear'): no error, set unchanged")

# =========================================================================
# pop() - Removes and returns a RANDOM item. Raises KeyError if empty.
# =========================================================================

popped = fruits.pop()
print(f"\nPopped item: '{popped}'")
print("After pop():", fruits)
# Note: Since sets are unordered, you don't know which item gets removed

# =========================================================================
# clear() - Removes ALL items (set becomes empty, variable still exists)
# =========================================================================

temp_set = {"a", "b", "c"}
print(f"\nBefore clear: {temp_set}")
temp_set.clear()
print(f"After clear: {temp_set}")
# Output: set()

# =========================================================================
# del - Deletes the set variable entirely
# =========================================================================

temp_set2 = {1, 2, 3}
del temp_set2

try:
    print(temp_set2)
except NameError as e:
    print(f"\nAfter del: {e}")
# Output: name 'temp_set2' is not defined

# =========================================================================
# Comparison summary
# =========================================================================
print("\n" + "=" * 50)
print("Method Comparison:")
print("=" * 50)
print("remove(x)  -> Removes x, KeyError if not found")
print("discard(x) -> Removes x, NO error if not found")
print("pop()      -> Removes random item, returns it")
print("clear()    -> Empties the set (variable remains)")
print("del set    -> Deletes the variable entirely")

# =========================================================================
# Practical: safe removal pattern
# =========================================================================
colors = {"red", "blue", "green", "yellow"}

# Safe pattern 1: check before remove
to_remove = "purple"
if to_remove in colors:
    colors.remove(to_remove)
else:
    print(f"\n'{to_remove}' not in set, skipping")

# Safe pattern 2: just use discard (simpler)
colors.discard("purple")  # Always safe

# Remove multiple items
items_to_remove = {"red", "blue", "orange"}
colors -= items_to_remove  # Set difference assignment
print(f"After removing multiple: {colors}")
# Output: {'green', 'yellow'}
