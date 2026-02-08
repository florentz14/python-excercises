# -------------------------------------------------
# File Name: 07_frozenset.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Frozenset — Immutable Sets.
#              A frozenset cannot be modified after creation
#              (no add, remove, pop, etc.). Because it is
#              hashable, it can serve as a dict key or as
#              an element inside another set. Supports all
#              read-only set operations (|, &, -, ^, in).
# -------------------------------------------------

# =========================================================================
# Create a frozenset from different iterables
# =========================================================================

# From a list
fruits = frozenset(["apple", "banana", "cherry", "grape"])
print("Frozenset:", fruits)
print("Type:", type(fruits))

# From a set
numbers = frozenset({1, 2, 3, 4, 5})
print("\nFrom set:", numbers)

# From a string (each character becomes an element)
chars = frozenset("hello")
print("From string:", chars)
# Output: frozenset({'h', 'e', 'l', 'o'})

# Empty frozenset
empty = frozenset()
print("Empty:", empty)

# =========================================================================
# Frozenset is IMMUTABLE — mutating methods raise AttributeError
# =========================================================================

try:
    fruits.add("mango")
except AttributeError as e:
    print(f"\nadd() Error: {e}")

try:
    fruits.remove("apple")
except AttributeError as e:
    print(f"remove() Error: {e}")

# Unavailable methods: add, remove, discard, pop, clear, update

# =========================================================================
# Frozenset supports READ operations and set math
# =========================================================================

# Membership test (O(1) average)
print(f"\n'banana' in fruits: {'banana' in fruits}")  # True
print(f"Length: {len(fruits)}")

# Loop through a frozenset
print("\nLoop:")
for fruit in fruits:
    print(f"  {fruit}")

# Set operations return NEW frozensets
fs1 = frozenset({1, 2, 3, 4})
fs2 = frozenset({3, 4, 5, 6})

print(f"\nfs1: {fs1}")
print(f"fs2: {fs2}")
print(f"Union:                {fs1 | fs2}")      # All unique elements
print(f"Intersection:         {fs1 & fs2}")      # Common elements
print(f"Difference:           {fs1 - fs2}")      # In fs1, not in fs2
print(f"Symmetric difference: {fs1 ^ fs2}")      # In one but not both

# Methods also work
print(f"fs1.union(fs2):       {fs1.union(fs2)}")
print(f"fs1.issubset(fs2):    {fs1.issubset(fs2)}")

# =========================================================================
# Frozenset as a dictionary key (regular sets CANNOT be keys)
# =========================================================================

# This works because frozenset is hashable (immutable)
permissions = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "admin"}): "admin"
}

user_perms = frozenset({"read", "write"})
print(f"\nRole for {set(user_perms)}: {permissions[user_perms]}")
# Output: editor

# =========================================================================
# Frozenset as an element of another set
# =========================================================================

# Regular sets CANNOT be nested inside other sets (unhashable)
try:
    invalid = {{1, 2}, {3, 4}}
except TypeError as e:
    print(f"\nSet in set Error: {e}")

# But frozensets CAN (they are hashable)
valid = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}
print(f"Set of frozensets: {valid}")
# Note: duplicate frozenset({1,2}) is removed

# =========================================================================
# Convert between set and frozenset
# =========================================================================
regular = {10, 20, 30}
frozen = frozenset(regular)    # set -> frozenset (immutable copy)
back = set(frozen)             # frozenset -> set (mutable copy)

print(f"\nRegular set: {regular}")
print(f"Frozenset:   {frozen}")
print(f"Back to set: {back}")

# -------------------------------------------------
# Summary:
# - frozenset = immutable set (cannot add/remove)
# - Supports: in, len, |, &, -, ^, loop, min, max, sum
# - Does NOT support: add, remove, discard, pop, clear, update
# - Can be used as dict key or set element (hashable)
# -------------------------------------------------
