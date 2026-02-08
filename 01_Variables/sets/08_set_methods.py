# ---------------------------------------------------------------------------
# Sets - 08: Set Methods (Complete Reference)
# ---------------------------------------------------------------------------
# Description: Comprehensive reference of ALL set methods in Python.
#              Demonstrates each method with practical examples.
# ---------------------------------------------------------------------------

# =========================================================================
# ADDING ELEMENTS
# =========================================================================
print("=" * 50)
print("ADDING ELEMENTS")
print("=" * 50)

s = {"apple", "banana"}

# add(elem) - Add a single element
s.add("cherry")
print(f"add('cherry'):          {s}")

# update(iterable) - Add multiple elements from iterable
s.update(["grape", "mango"])
print(f"update(['grape','mango']): {s}")

# =========================================================================
# REMOVING ELEMENTS
# =========================================================================
print(f"\n{'='*50}")
print("REMOVING ELEMENTS")
print("=" * 50)

s = {"apple", "banana", "cherry", "grape", "mango"}

# remove(elem) - Remove element; raises KeyError if not found
s.remove("banana")
print(f"remove('banana'):  {s}")

# discard(elem) - Remove element; NO error if not found
s.discard("pear")  # No error
print(f"discard('pear'):   {s} (no error)")

# pop() - Remove and return an arbitrary element
popped = s.pop()
print(f"pop() returned:    '{popped}', set: {s}")

# clear() - Remove all elements
temp = {"a", "b", "c"}
temp.clear()
print(f"clear():           {temp}")

# =========================================================================
# SET OPERATIONS
# =========================================================================
print(f"\n{'='*50}")
print("SET OPERATIONS")
print("=" * 50)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}")
print(f"b = {b}")

# union(*others) - Return all unique elements
print(f"\na.union(b):                    {a.union(b)}")

# intersection(*others) - Return common elements
print(f"a.intersection(b):             {a.intersection(b)}")

# difference(*others) - Return elements in a but not in b
print(f"a.difference(b):               {a.difference(b)}")

# symmetric_difference(other) - Return elements in either but not both
print(f"a.symmetric_difference(b):     {a.symmetric_difference(b)}")

# =========================================================================
# IN-PLACE SET OPERATIONS
# =========================================================================
print(f"\n{'='*50}")
print("IN-PLACE OPERATIONS (modify the set)")
print("=" * 50)

# update(*others) - Add all elements (union in-place)
x = {1, 2}
x.update({2, 3})
print(f"update (|=):                   {x}")     # {1, 2, 3}

# intersection_update(*others) - Keep only common
x = {1, 2, 3, 4}
x.intersection_update({2, 4, 6})
print(f"intersection_update (&=):      {x}")     # {2, 4}

# difference_update(*others) - Remove items found in other
x = {1, 2, 3, 4, 5}
x.difference_update({2, 4})
print(f"difference_update (-=):        {x}")     # {1, 3, 5}

# symmetric_difference_update(other) - Keep only non-common
x = {1, 2, 3}
x.symmetric_difference_update({2, 3, 4})
print(f"symmetric_difference_update:   {x}")     # {1, 4}

# =========================================================================
# COMPARISON METHODS
# =========================================================================
print(f"\n{'='*50}")
print("COMPARISON METHODS")
print("=" * 50)

c = {1, 2}
d = {1, 2, 3, 4}

# issubset(other) - Is c a subset of d?
print(f"c = {c}, d = {d}")
print(f"c.issubset(d):     {c.issubset(d)}")       # True
print(f"c <= d:            {c <= d}")               # True

# issuperset(other) - Is d a superset of c?
print(f"d.issuperset(c):   {d.issuperset(c)}")     # True
print(f"d >= c:            {d >= c}")               # True

# isdisjoint(other) - No common elements?
e = {5, 6, 7}
print(f"\ne = {e}")
print(f"c.isdisjoint(e):   {c.isdisjoint(e)}")     # True
print(f"c.isdisjoint(d):   {c.isdisjoint(d)}")     # False

# =========================================================================
# COPY
# =========================================================================
print(f"\n{'='*50}")
print("COPY")
print("=" * 50)

original = {1, 2, 3}
copy_set = original.copy()
copy_set.add(4)
print(f"Original: {original}")  # {1, 2, 3} (unchanged)
print(f"Copy:     {copy_set}")   # {1, 2, 3, 4}

# =========================================================================
# COMPLETE METHOD REFERENCE TABLE
# =========================================================================
print(f"\n{'='*50}")
print("ALL SET METHODS")
print("=" * 50)
print("""
| Method                        | Description                          |
|-------------------------------|--------------------------------------|
| add(elem)                     | Add element                          |
| update(*iterables)            | Add elements from iterables          |
| remove(elem)                  | Remove element (KeyError if missing) |
| discard(elem)                 | Remove element (no error if missing) |
| pop()                         | Remove and return arbitrary element  |
| clear()                       | Remove all elements                  |
| copy()                        | Return shallow copy                  |
| union(*others)                | Return set with all elements         |
| intersection(*others)         | Return set with common elements      |
| difference(*others)           | Return set with unique elements      |
| symmetric_difference(other)   | Return set with non-common elements  |
| update(*others)               | Union in-place                       |
| intersection_update(*others)  | Intersection in-place                |
| difference_update(*others)    | Difference in-place                  |
| symmetric_difference_update() | Symmetric difference in-place        |
| issubset(other)               | Test if subset                       |
| issuperset(other)             | Test if superset                     |
| isdisjoint(other)             | Test if no common elements           |
""")
