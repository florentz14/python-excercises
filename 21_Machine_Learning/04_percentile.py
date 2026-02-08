"""
Machine Learning - Percentile
===============================
A percentile indicates the value below which a given percentage of data falls.

- The 75th percentile means 75% of the data is below that value
- Percentiles help understand the distribution and ranking of data
- Quartiles are specific percentiles:
  - Q1 = 25th percentile
  - Q2 = 50th percentile (median)
  - Q3 = 75th percentile
- IQR (Interquartile Range) = Q3 - Q1
"""

import numpy as np

# ============================================================
# 1. Basic Percentile
# ============================================================
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6,
        25, 36, 27, 61, 31]

# What percentage of people are younger than 43?
percentile_75 = np.percentile(ages, 75)
print(f"Ages: {sorted(ages)}")
print(f"75th percentile: {percentile_75}")
# Output: 75th percentile: 43.0
# This means 75% of the people are 43 years old or younger


# ============================================================
# 2. Common Percentiles
# ============================================================
print(f"\n{'='*50}")
print("COMMON PERCENTILES")
print(f"{'='*50}")

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

for p in [10, 25, 50, 75, 90]:
    value = np.percentile(data, p)
    print(f"  {p:3d}th percentile: {value:.1f}")

print(f"\n  Min (0th):   {np.percentile(data, 0):.1f}")
print(f"  Max (100th): {np.percentile(data, 100):.1f}")


# ============================================================
# 3. Quartiles and IQR
# ============================================================
print(f"\n{'='*50}")
print("QUARTILES AND IQR")
print(f"{'='*50}")

scores = [55, 60, 62, 65, 67, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95, 100]

q1 = np.percentile(scores, 25)
q2 = np.percentile(scores, 50)  # Median
q3 = np.percentile(scores, 75)
iqr = q3 - q1

print(f"Scores: {scores}")
print(f"Q1 (25th percentile): {q1:.1f}")
print(f"Q2 (50th percentile): {q2:.1f} (median)")
print(f"Q3 (75th percentile): {q3:.1f}")
print(f"IQR (Q3 - Q1):        {iqr:.1f}")


# ============================================================
# 4. Detecting Outliers with IQR
# ============================================================
print(f"\n{'='*50}")
print("OUTLIER DETECTION WITH IQR")
print(f"{'='*50}")

data = [12, 15, 14, 10, 16, 13, 15, 14, 11, 100, 12, 15, 14, 200]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Outlier boundaries (1.5 * IQR rule)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in data if x < lower_bound or x > upper_bound]
clean_data = [x for x in data if lower_bound <= x <= upper_bound]

print(f"Data: {data}")
print(f"Q1: {q1:.1f}, Q3: {q3:.1f}, IQR: {iqr:.1f}")
print(f"Lower bound: {lower_bound:.1f}")
print(f"Upper bound: {upper_bound:.1f}")
print(f"Outliers:    {outliers}")
print(f"Clean data:  {clean_data}")


# ============================================================
# 5. Multiple percentiles at once
# ============================================================
print(f"\n{'='*50}")
print("MULTIPLE PERCENTILES AT ONCE")
print(f"{'='*50}")

np.random.seed(42)
exam_scores = np.random.normal(loc=72, scale=12, size=100).astype(int)

percentiles = np.percentile(exam_scores, [10, 25, 50, 75, 90])

print(f"Exam scores ({len(exam_scores)} students)")
print(f"  Min:  {np.min(exam_scores)}")
print(f"  10th: {percentiles[0]:.0f}  (bottom 10% scored below this)")
print(f"  25th: {percentiles[1]:.0f}  (Q1)")
print(f"  50th: {percentiles[2]:.0f}  (Median)")
print(f"  75th: {percentiles[3]:.0f}  (Q3)")
print(f"  90th: {percentiles[4]:.0f}  (top 10% scored above this)")
print(f"  Max:  {np.max(exam_scores)}")


# ============================================================
# 6. Percentile Rank: What percentile is a specific value?
# ============================================================
print(f"\n{'='*50}")
print("PERCENTILE RANK")
print(f"{'='*50}")

from scipy import stats

scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
my_score = 80

rank = stats.percentileofscore(scores, my_score)
print(f"Scores: {scores}")
print(f"Your score: {my_score}")
print(f"Percentile rank: {rank:.1f}%")
print(f"You scored higher than {rank:.0f}% of students")

print("\n--- Percentile complete! ---")
