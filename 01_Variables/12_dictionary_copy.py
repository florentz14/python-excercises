# Example 11: Copy dictionary
print("Example 11: Copy dictionary")
print("-" * 40)
original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()
print("Original:", original)
print("Copy:", copy_dict)
copy_dict["a"] = 100
print("After modifying copy:")
print("Original:", original)
print("Copy:", copy_dict)
