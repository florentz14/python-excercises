# Example 4: Add and remove elements
print("Example 4: Add and remove elements")
print("-" * 40)
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.add("date")
print("After add('date'):", fruits)
fruits.remove("banana")
print("After remove('banana'):", fruits)
fruits.discard("grape")  # No error if element doesn't exist
print("After discard('grape'):", fruits)
