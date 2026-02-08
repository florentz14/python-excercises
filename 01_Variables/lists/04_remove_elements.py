# Example 4: Remove elements from a list
print("Example 4: Remove elements from a list")
print("-" * 40)
animals = ["cat", "dog", "bird", "fish", "dog"]
print("Original list:", animals)
animals.remove("dog")  # Remove first occurrence
print("After remove 'dog':", animals)
removed_item = animals.pop()  # Remove and return last element
print("Popped item:", removed_item)
print("After pop:", animals)
