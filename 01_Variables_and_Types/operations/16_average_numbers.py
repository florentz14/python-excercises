# -------------------------------------------------
# File Name: 16_average_numbers.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Average and weighted average of lists of numbers.
# -------------------------------------------------

import statistics


def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_weighted_average(values, weights):
    """Calculate weighted average"""
    if len(values) != len(weights):
        return "Error: Values and weights must have same length"
    if sum(weights) == 0:
        return "Error: Sum of weights cannot be zero"
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)


# Examples with lists
print("Average Calculations:")
print("=" * 25)

# Simple average
nums1 = [1, 2, 3, 4, 5]
avg1 = calculate_average(nums1)
print(f"Average of {nums1}: {avg1}")

nums2 = [10, 20, 30, 40, 50]
avg2 = calculate_average(nums2)
print(f"Average of {nums2}: {avg2}")

# Empty list
empty = []
avg_empty = calculate_average(empty)
print(f"Average of empty list: {avg_empty}")

# Single number
single = [42]
avg_single = calculate_average(single)
print(f"Average of {single}: {avg_single}")

# Float numbers
floats = [1.5, 2.5, 3.5, 4.5]
avg_floats = calculate_average(floats)
print(f"Average of {floats}: {avg_floats}")

# Weighted average
print("\nWeighted Average:")
grades = [90, 85, 95]
weights = [0.3, 0.3, 0.4]  # 30%, 30%, 40%
weighted_avg = calculate_weighted_average(grades, weights)
print(f"Grades: {grades}")
print(f"Weights: {weights}")
print(f"Weighted average: {weighted_avg}")

# Manual calculation for verification
print("\nManual verification:")
total = sum(nums1)
count = len(nums1)
manual_avg = total / count
print(f"Sum: {total}, Count: {count}, Average: {manual_avg}")

# Using statistics module
print(f"\nUsing statistics.mean(): {statistics.mean(nums1)}")
print(f"Using statistics.mean() for floats: {statistics.mean(floats)}")

# Average of even numbers
even_nums = [x for x in range(1, 11) if x % 2 == 0]
print(f"\nEven numbers from 1-10: {even_nums}")
print(f"Average: {calculate_average(even_nums)}")

# Average temperature
temperatures = [20.5, 22.1, 19.8, 21.3, 23.0]
print(f"\nTemperatures: {temperatures}")
print(f"Average temperature: {calculate_average(temperatures):.2f}°C")
