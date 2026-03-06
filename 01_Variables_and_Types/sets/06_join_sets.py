# -------------------------------------------------
# File Name: 06_join_sets.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Join / Combine Sets.
#              Union (|), Intersection (&), Difference (-),
#              and Symmetric Difference (^). Each has both
#              an operator and a method form, plus in-place
#              update variants that modify the set directly.
# -------------------------------------------------

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "grape", "mango", "cherry"}

print("Set 1:", set1)
print("Set 2:", set2)

# =========================================================================
# UNION - All items from both sets (no duplicates)
# =========================================================================
# Operator: |    Method: .union()
union_op = set1 | set2
union_method = set1.union(set2)
print(f"\nUnion (|):      {union_op}")
print(f"Union (method): {union_method}")
# Output: {'apple', 'banana', 'cherry', 'grape', 'mango'}

# Union of multiple sets at once
set3 = {"kiwi", "pear"}
multi_union = set1 | set2 | set3
print(f"Multi union:    {multi_union}")

# =========================================================================
# INTERSECTION - Only items that exist in BOTH sets
# =========================================================================
# Operator: &    Method: .intersection()
inter_op = set1 & set2
inter_method = set1.intersection(set2)
print(f"\nIntersection (&):      {inter_op}")
print(f"Intersection (method): {inter_method}")
# Output: {'banana', 'cherry'}

# =========================================================================
# DIFFERENCE - Items in set1 but NOT in set2
# =========================================================================
# Operator: -    Method: .difference()
diff_op = set1 - set2
diff_method = set1.difference(set2)
print(f"\nDifference (set1-set2):       {diff_op}")     # {'apple'}

diff_reverse = set2 - set1
print(f"Difference (set2-set1):       {diff_reverse}")  # {'grape', 'mango'}

# =========================================================================
# SYMMETRIC DIFFERENCE - Items in either set, but NOT in both
# =========================================================================
# Operator: ^    Method: .symmetric_difference()
sym_op = set1 ^ set2
sym_method = set1.symmetric_difference(set2)
print(f"\nSymmetric diff (^):      {sym_op}")
print(f"Symmetric diff (method): {sym_method}")
# Output: {'apple', 'grape', 'mango'}

# =========================================================================
# IN-PLACE update methods (modify the set directly)
# =========================================================================
print("\n" + "=" * 50)
print("In-place update methods:")

# update() — union in-place (adds all items)
a = {1, 2, 3}
a.update({3, 4, 5})
print(f"\nupdate (union in-place): {a}")           # {1, 2, 3, 4, 5}

# intersection_update() — keeps only common items
b = {1, 2, 3, 4, 5}
b.intersection_update({2, 4, 6})
print(f"intersection_update:     {b}")              # {2, 4}

# difference_update() — removes items found in another set
c = {1, 2, 3, 4, 5}
c.difference_update({2, 4})
print(f"difference_update:       {c}")              # {1, 3, 5}

# symmetric_difference_update() — keeps only non-common items
d = {1, 2, 3}
d.symmetric_difference_update({2, 3, 4})
print(f"symmetric_diff_update:   {d}")              # {1, 4}

# =========================================================================
# Quick-reference summary table
# =========================================================================
print("\n" + "=" * 50)
print("| Operation            | Operator | Method                         |")
print("|----------------------|----------|--------------------------------|")
print("| Union                | a | b    | a.union(b)                     |")
print("| Intersection         | a & b    | a.intersection(b)              |")
print("| Difference           | a - b    | a.difference(b)                |")
print("| Symmetric Difference | a ^ b    | a.symmetric_difference(b)      |")
