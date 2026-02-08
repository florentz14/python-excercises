# ---------------------------------------------------------------------------
# Sets - 07: Frozenset
# ---------------------------------------------------------------------------
# Description: A frozenset is an IMMUTABLE version of a set. Once created,
#              you cannot add, remove, or change its elements. Because it
#              is immutable, a frozenset can be used as a dictionary key
#              or as an element of another set.
# Syntax:      my_frozenset = frozenset(iterable)
# ---------------------------------------------------------------------------

# =========================================================================
# Create a frozenset
# =========================================================================

# From a list
fruits = frozenset(["apple", "banana", "cherry", "grape"])
print("Frozenset:", fruits)
print("Type:", type(fruits))
# Output: frozenset({'apple', 'banana', 'cherry', 'grape'})

# From a set
numbers = frozenset({1, 2, 3, 4, 5})
print("\nFrom set:", numbers)

# From a string
chars = frozenset("hello")
print("From string:", chars)
# Output: frozenset({'h', 'e', 'l', 'o'})

# Empty frozenset
empty = frozenset()
print("Empty:", empty)

# =========================================================================
# Frozenset is IMMUTABLE - cannot add or remove
# =========================================================================

try:
    fruits.add("mango")
except AttributeError as e:
    print(f"\nadd() Error: {e}")

try:
    fruits.remove("apple")
except AttributeError as e:
    print(f"remove() Error: {e}")

# No: add, remove, discard, pop, clear, update
# These methods do NOT exist on frozenset

# =========================================================================
# Frozenset supports READ operations and set math
# =========================================================================

# Membership test
print(f"\n'banana' in fruits: {'banana' in fruits}")  # True
print(f"Length: {len(fruits)}")

# Loop through a frozenset
print("\nLoop:")
for fruit in fruits:
    print(f"  {fruit}")

# Set operations (return new frozensets)
fs1 = frozenset({1, 2, 3, 4})
fs2 = frozenset({3, 4, 5, 6})

print(f"\nfs1: {fs1}")
print(f"fs2: {fs2}")
print(f"Union:                {fs1 | fs2}")
print(f"Intersection:         {fs1 & fs2}")
print(f"Difference:           {fs1 - fs2}")
print(f"Symmetric difference: {fs1 ^ fs2}")

# Methods also work
print(f"fs1.union(fs2):       {fs1.union(fs2)}")
print(f"fs1.issubset(fs2):    {fs1.issubset(fs2)}")

# =========================================================================
# Frozenset as a dictionary key (sets CANNOT be keys)
# =========================================================================

# This works because frozenset is hashable (immutable)
permissions = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "admin"}): "admin"
}

user_perms = frozenset({"read", "write"})
print(f"\nRole for {set(user_perms)}: {permissions[user_perms]}")
# Output: Role for {'read', 'write'}: editor

# =========================================================================
# Frozenset as an element of another set
# =========================================================================

# Regular sets CANNOT be inside other sets
try:
    invalid = {{1, 2}, {3, 4}}  # Error!
except TypeError as e:
    print(f"\nSet in set Error: {e}")

# But frozensets CAN
valid = {frozenset({1, 2}), frozenset({3, 4}), frozenset({1, 2})}
print(f"Set of frozensets: {valid}")
# Note: duplicate frozenset({1,2}) is removed

# =========================================================================
# Convert between set and frozenset
# =========================================================================
regular = {10, 20, 30}
frozen = frozenset(regular)    # set -> frozenset
back = set(frozen)             # frozenset -> set

print(f"\nRegular set: {regular}")
print(f"Frozenset:   {frozen}")
print(f"Back to set: {back}")

# ---------------------------------------------------------------------------
# Summary:
# - frozenset = immutable set
# - Supports: in, len, |, &, -, ^, loop, min, max, sum
# - Does NOT support: add, remove, discard, pop, clear, update
# - Can be used as dict key or set element (hashable)
# ---------------------------------------------------------------------------
