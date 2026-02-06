# Example 10: Set symmetric difference (elements in either but not both)
print("Example 10: Set symmetric difference (elements in either but not both)")
print("-" * 40)
set_m = {1, 2, 3, 4}
set_n = {3, 4, 5, 6}
print("Set M:", set_m)
print("Set N:", set_n)
sym_diff = set_m ^ set_n  # or set_m.symmetric_difference(set_n)
print("Symmetric Difference (set_m ^ set_n):", sym_diff)
