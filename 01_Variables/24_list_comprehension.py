# Example 7: List comprehension
print("Example 7: List comprehension")
print("-" * 40)
numbers_list = [1, 2, 3, 4, 5]
print("Original numbers:", numbers_list)
squared = [x ** 2 for x in numbers_list]
print("Squared numbers:", squared)
even_numbers = [x for x in numbers_list if x % 2 == 0]
print("Even numbers:", even_numbers)
