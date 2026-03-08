# -------------------------------------------------
# File Name: 17_min_max_numbers.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Finds min and max with built-ins and manual loop.
# -------------------------------------------------

def find_min_max(numbers):
    """Find minimum and maximum in a list"""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


def find_min_max_manual(numbers):
    """Find min and max manually without built-in functions"""
    if not numbers:
        return None, None

    minimum = maximum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum


# Examples
print("Min/Max Calculations:")
print("=" * 20)

# Integer list
nums1 = [5, 2, 8, 1, 9, 3]
min_val, max_val = find_min_max(nums1)
print(f"List: {nums1}")
print(f"Min: {min_val}, Max: {max_val}")

# Float list
nums2 = [3.14, 2.71, 1.41, 1.73]
min_val2, max_val2 = find_min_max(nums2)
print(f"\nList: {nums2}")
print(f"Min: {min_val2}, Max: {max_val2}")

# Negative numbers
nums3 = [-5, -2, -8, -1]
min_val3, max_val3 = find_min_max(nums3)
print(f"\nList: {nums3}")
print(f"Min: {min_val3}, Max: {max_val3}")

# Mixed positive and negative
nums4 = [-3, 0, 7, -1, 4]
min_val4, max_val4 = find_min_max(nums4)
print(f"\nList: {nums4}")
print(f"Min: {min_val4}, Max: {max_val4}")

# Single element
nums5 = [42]
min_val5, max_val5 = find_min_max(nums5)
print(f"\nList: {nums5}")
print(f"Min: {min_val5}, Max: {max_val5}")

# Empty list
nums6 = []
min_val6, max_val6 = find_min_max(nums6)
print(f"\nList: {nums6}")
print(f"Min: {min_val6}, Max: {max_val6}")

# Manual calculation
print("\nManual calculation:")
nums = [4, 7, 2, 9, 1]
min_manual, max_manual = find_min_max_manual(nums)
print(f"List: {nums}")
print(f"Manual Min: {min_manual}, Max: {max_manual}")

# Using built-in functions directly
print(f"\nBuilt-in min: {min(nums)}")
print(f"Built-in max: {max(nums)}")

# Finding min/max with conditions
numbers = [10, 25, 30, 15, 40, 5]
even_nums = [x for x in numbers if x % 2 == 0]
odd_nums = [x for x in numbers if x % 2 != 0]

print(f"\nOriginal: {numbers}")
print(
    f"Even numbers: {even_nums}, Min: {min(even_nums)}, Max: {max(even_nums)}")
print(f"Odd numbers: {odd_nums}, Min: {min(odd_nums)}, Max: {max(odd_nums)}")

# String comparison (lexicographical)
words = ["apple", "banana", "cherry", "date"]
print(f"\nWords: {words}")
print(f"Min (alphabetical): {min(words)}")
print(f"Max (alphabetical): {max(words)}")
