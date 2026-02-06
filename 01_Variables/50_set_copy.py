# Example 13: Copy a set
print("Example 13: Copy a set")
print("-" * 40)
original_set = {1, 2, 3}
copied_set = original_set.copy()
print("Original:", original_set)
print("Copied:", copied_set)
copied_set.add(4)
print("After adding 4 to copy:")
print("Original:", original_set)
print("Copied:", copied_set)
