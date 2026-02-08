"""
Machine Learning - Mean, Median, Mode
=======================================
These are fundamental statistical measures used to understand data.

- Mean   : The average value (sum / count)
- Median : The middle value when data is sorted
- Mode   : The most frequently occurring value(s)

Understanding these helps in data preprocessing and feature analysis.
"""

import numpy as np
from scipy import stats

# ============================================================
# 1. Mean (Average)
# ============================================================
# The sum of all values divided by the number of values

speeds = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean_value = np.mean(speeds)
print(f"Data: {speeds}")
print(f"Mean (average): {mean_value:.2f}")
# Output: Mean (average): 89.77

# Manual calculation
manual_mean = sum(speeds) / len(speeds)
print(f"Manual mean:    {manual_mean:.2f}")


# ============================================================
# 2. Median (Middle Value)
# ============================================================
# The value in the middle after sorting
# If even count: average of the two middle values

print(f"\n{'='*50}")
print("MEDIAN")
print(f"{'='*50}")

# Odd number of elements
speeds_odd = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
median_odd = np.median(speeds_odd)
sorted_odd = sorted(speeds_odd)
print(f"Sorted (odd count):  {sorted_odd}")
print(f"Median: {median_odd}")
# Output: Median: 87.0 (the 7th value in sorted list)

# Even number of elements
speeds_even = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85]
median_even = np.median(speeds_even)
sorted_even = sorted(speeds_even)
print(f"\nSorted (even count): {sorted_even}")
print(f"Median: {median_even}")
# Output: Median: 87.5 (average of 87 and 88)


# ============================================================
# 3. Mode (Most Frequent Value)
# ============================================================
print(f"\n{'='*50}")
print("MODE")
print(f"{'='*50}")

speeds = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
mode_result = stats.mode(speeds, keepdims=True)
print(f"Data: {speeds}")
print(f"Mode: {mode_result.mode[0]}")
print(f"Count: {mode_result.count[0]}")
# Output: Mode: 86, Count: 3

# Mode with multiple modes
data_multi = [1, 2, 2, 3, 3, 4]
# Using collections.Counter for multiple modes
from collections import Counter

counter = Counter(data_multi)
max_count = max(counter.values())
modes = [k for k, v in counter.items() if v == max_count]
print(f"\nData: {data_multi}")
print(f"Modes (multimodal): {modes} (each appears {max_count} times)")
# Output: Modes: [2, 3] (each appears 2 times)


# ============================================================
# 4. Comparing Mean, Median, Mode on skewed data
# ============================================================
print(f"\n{'='*50}")
print("COMPARISON ON SKEWED DATA")
print(f"{'='*50}")

# Right-skewed data (most values are low, few are very high)
salaries = [30000, 32000, 35000, 36000, 37000, 40000, 42000, 45000, 150000, 500000]

mean_sal = np.mean(salaries)
median_sal = np.median(salaries)
mode_sal = stats.mode(salaries, keepdims=True)

print(f"Salaries: {salaries}")
print(f"Mean:   ${mean_sal:,.2f}")
print(f"Median: ${median_sal:,.2f}")
print(f"Mode:   ${mode_sal.mode[0]:,} (appears {mode_sal.count[0]} time(s))")
print("\nNote: The mean is pulled UP by the outliers (150k, 500k)")
print("The median is more representative of a 'typical' salary")


# ============================================================
# 5. Weighted Mean
# ============================================================
print(f"\n{'='*50}")
print("WEIGHTED MEAN")
print(f"{'='*50}")

# GPA calculation: grades weighted by credit hours
grades  = [4.0, 3.5, 3.0, 3.7, 2.8]   # grade points
credits = [3,   4,   3,   2,   4]       # credit hours (weights)

weighted_mean = np.average(grades, weights=credits)
simple_mean = np.mean(grades)

print(f"Grades:  {grades}")
print(f"Credits: {credits}")
print(f"Simple mean GPA:   {simple_mean:.2f}")
print(f"Weighted mean GPA: {weighted_mean:.2f}")


# ============================================================
# 6. Practical example: Analyzing a dataset
# ============================================================
print(f"\n{'='*50}")
print("PRACTICAL EXAMPLE - Student Test Scores")
print(f"{'='*50}")

np.random.seed(42)
scores = np.random.normal(loc=75, scale=10, size=50).astype(int)

print(f"Number of students: {len(scores)}")
print(f"Scores (first 10):  {list(scores[:10])}")
print(f"\nMean:   {np.mean(scores):.1f}")
print(f"Median: {np.median(scores):.1f}")

mode_scores = stats.mode(scores, keepdims=True)
print(f"Mode:   {mode_scores.mode[0]} (appears {mode_scores.count[0]} times)")
print(f"Min:    {np.min(scores)}")
print(f"Max:    {np.max(scores)}")

print("\n--- Mean, Median, Mode complete! ---")
