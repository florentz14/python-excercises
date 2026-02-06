# Example 9: Set difference (elements in first but not second)
print("Example 9: Set difference (elements in first but not second)")
print("-" * 40)
set_x = {1, 2, 3, 4, 5}
set_y = {4, 5, 6, 7}
print("Set X:", set_x)
print("Set Y:", set_y)
difference = set_x - set_y  # or set_x.difference(set_y)
print("Difference (set_x - set_y):", difference)
