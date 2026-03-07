# Sum Numbers in Python

def sum_numbers(numbers):
    """Calculate sum of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total


def sum_recursive(numbers):
    """Calculate sum using recursion"""
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


# Examples
print("Sum Calculations:")
print("=" * 15)

# Integer list
nums1 = [1, 2, 3, 4, 5]
sum1 = sum_numbers(nums1)
print(f"Sum of {nums1}: {sum1}")

# Using built-in sum
print(f"Built-in sum: {sum(nums1)}")

# Float list
nums2 = [1.5, 2.5, 3.5]
sum2 = sum_numbers(nums2)
print(f"\nSum of {nums2}: {sum2}")

# Negative numbers
nums3 = [-1, -2, -3, 4, 5]
sum3 = sum_numbers(nums3)
print(f"\nSum of {nums3}: {sum3}")

# Empty list
nums4 = []
sum4 = sum_numbers(nums4)
print(f"\nSum of empty list: {sum4}")

# Single element
nums5 = [42]
sum5 = sum_numbers(nums5)
print(f"\nSum of {nums5}: {sum5}")

# Large numbers
nums6 = [1000000, 2000000, 3000000]
sum6 = sum_numbers(nums6)
print(f"\nSum of {nums6}: {sum6}")

# Recursive sum
print("\nRecursive sum:")
nums7 = [1, 2, 3, 4]
recursive_sum = sum_recursive(nums7)
print(f"Recursive sum of {nums7}: {recursive_sum}")

# Sum with range
print("\nSum with range:")
n = 10
range_sum = sum(range(1, n+1))  # Sum from 1 to 10
print(f"Sum from 1 to {n}: {range_sum}")
print(f"Formula verification: n*(n+1)/2 = {n*(n+1)//2}")

# Sum of even numbers
even_sum = sum(x for x in range(1, 11) if x % 2 == 0)
print(f"\nSum of even numbers 1-10: {even_sum}")

# Sum of squares
squares_sum = sum(x**2 for x in range(1, 6))
print(f"Sum of squares 1-5: {squares_sum}")

# Conditional sum
numbers = [10, 15, 20, 25, 30]
greater_than_20 = sum(x for x in numbers if x > 20)
print(f"\nNumbers: {numbers}")
print(f"Sum of numbers > 20: {greater_than_20}")

# Running sum
print("\nRunning sum:")
nums = [1, 3, 5, 7, 9]
running_total = 0
for num in nums:
    running_total += num
    print(f"After adding {num}: {running_total}")
