# -------------------------------------------------
# File Name: 09_subset_superset.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Subset and Superset Comparison.
#              issubset() checks if all elements of one set
#              are contained in another. issuperset() is the
#              inverse. isdisjoint() checks for zero overlap.
# -------------------------------------------------

# Example 11: Set comparison (subset, superset)
print("Example 11: Set comparison")
print("-" * 40)

parent_set = {1, 2, 3, 4, 5}
child_set = {2, 4}

print("Parent set:", parent_set)
print("Child set:", child_set)

# issubset(): every element of child_set is in parent_set
print("Is child_set a subset of parent_set?", child_set.issubset(parent_set))   # True

# issuperset(): parent_set contains every element of child_set
print("Is parent_set a superset of child_set?", parent_set.issuperset(child_set))  # True

# isdisjoint(): True only if the sets share NO elements
print("Are they disjoint?", child_set.isdisjoint(parent_set))  # False (they share 2, 4)
