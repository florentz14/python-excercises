"""
Machine Learning - Data Distribution
======================================
Data distribution describes how data values are spread across a range.
Understanding distributions helps choose the right ML algorithm
and preprocessing techniques.

Key concepts:
- Histogram: Visual representation of data distribution
- Uniform distribution: All values equally likely
- Normal distribution: Bell-shaped curve (covered in next file)
- Skewed distribution: Data concentrated on one side
- Big Data distributions: When datasets have thousands+ of values
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Creating a random data distribution
# ============================================================
# numpy.random.uniform: all values equally likely within a range

np.random.seed(42)
uniform_data = np.random.uniform(0.0, 5.0, 250)

print("Uniform Distribution (250 values between 0 and 5):")
print(f"  Min:    {np.min(uniform_data):.2f}")
print(f"  Max:    {np.max(uniform_data):.2f}")
print(f"  Mean:   {np.mean(uniform_data):.2f}")
print(f"  Std:    {np.std(uniform_data):.2f}")

# Visualize
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(uniform_data, bins=20, color="steelblue", edgecolor="black")
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")


# ============================================================
# 2. Normal (Gaussian) Distribution
# ============================================================
normal_data = np.random.normal(5.0, 1.0, 250)  # mean=5, std=1

print(f"\nNormal Distribution (mean=5, std=1, n=250):")
print(f"  Min:    {np.min(normal_data):.2f}")
print(f"  Max:    {np.max(normal_data):.2f}")
print(f"  Mean:   {np.mean(normal_data):.2f}")
print(f"  Std:    {np.std(normal_data):.2f}")

plt.subplot(1, 2, 2)
plt.hist(normal_data, bins=20, color="coral", edgecolor="black")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("21_Machine_Learning/dist_comparison.png", dpi=80, bbox_inches="tight")
plt.show()


# ============================================================
# 3. Big Data Distribution
# ============================================================
print(f"\n{'='*50}")
print("BIG DATA DISTRIBUTION")
print(f"{'='*50}")

# With larger datasets, patterns become clearer
big_data = np.random.normal(5.0, 1.0, 100000)

print(f"Big data (100,000 values):")
print(f"  Mean:   {np.mean(big_data):.4f} (closer to 5.0)")
print(f"  Std:    {np.std(big_data):.4f} (closer to 1.0)")

plt.figure(figsize=(8, 5))
plt.hist(big_data, bins=100, color="mediumseagreen", edgecolor="none", alpha=0.8)
plt.title("Normal Distribution - 100,000 Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axvline(np.mean(big_data), color="red", linestyle="--", label=f"Mean={np.mean(big_data):.2f}")
plt.legend()
plt.tight_layout()
plt.show()


# ============================================================
# 4. Skewed Distributions
# ============================================================
print(f"\n{'='*50}")
print("SKEWED DISTRIBUTIONS")
print(f"{'='*50}")

# Right-skewed (positive skew): tail extends to the right
right_skew = np.random.exponential(scale=2.0, size=5000)

# Left-skewed (negative skew): tail extends to the left
left_skew = -np.random.exponential(scale=2.0, size=5000) + 15

from scipy.stats import skew

print(f"Right-skewed data: skewness = {skew(right_skew):.2f}")
print(f"  (positive value = right skew, tail to the right)")
print(f"Left-skewed data:  skewness = {skew(left_skew):.2f}")
print(f"  (negative value = left skew, tail to the left)")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(right_skew, bins=50, color="salmon", edgecolor="none")
plt.title("Right-Skewed (Positive)")
plt.xlabel("Value")

plt.subplot(1, 2, 2)
plt.hist(left_skew, bins=50, color="mediumpurple", edgecolor="none")
plt.title("Left-Skewed (Negative)")
plt.xlabel("Value")

plt.tight_layout()
plt.show()


# ============================================================
# 5. Describing a distribution
# ============================================================
print(f"\n{'='*50}")
print("DESCRIBING A DISTRIBUTION")
print(f"{'='*50}")

from scipy.stats import describe, kurtosis

data = np.random.normal(100, 15, 1000)
desc = describe(data)

print(f"Sample size:  {desc.nobs}")
print(f"Min / Max:    {desc.minmax[0]:.2f} / {desc.minmax[1]:.2f}")
print(f"Mean:         {desc.mean:.2f}")
print(f"Variance:     {desc.variance:.2f}")
print(f"Skewness:     {desc.skewness:.4f}")
print(f"Kurtosis:     {desc.kurtosis:.4f}")
print("\nSkewness ≈ 0 and Kurtosis ≈ 0 => approximately normal distribution")

print("\n--- Data Distribution complete! ---")
