"""
Machine Learning - Standard Deviation
=======================================
Standard deviation measures how spread out the data is from the mean.

- Low standard deviation  -> data points are close to the mean
- High standard deviation -> data points are spread over a wide range

Formula: σ = sqrt( Σ(xi - μ)² / N )
Where:
  σ  = standard deviation
  xi = each data point
  μ  = mean of the data
  N  = number of data points

Related concept: Variance = σ² (standard deviation squared)
"""

import numpy as np

# ============================================================
# 1. Basic Standard Deviation
# ============================================================
speed = [86, 87, 88, 86, 87, 85, 86]

std_dev = np.std(speed)
print(f"Data: {speed}")
print(f"Standard Deviation: {std_dev:.4f}")
# Output: Standard Deviation: 0.9035 (low -> values are close together)

speed2 = [32, 111, 138, 28, 59, 77, 97]
std_dev2 = np.std(speed2)
print(f"\nData: {speed2}")
print(f"Standard Deviation: {std_dev2:.4f}")
# Output: Standard Deviation: 37.85 (high -> values are spread out)


# ============================================================
# 2. Variance (σ²)
# ============================================================
print(f"\n{'='*50}")
print("VARIANCE")
print(f"{'='*50}")

# Variance is the average of the squared differences from the mean
variance = np.var(speed)
variance2 = np.var(speed2)

print(f"Data 1: {speed}")
print(f"  Variance:  {variance:.4f}")
print(f"  Std Dev:   {std_dev:.4f}")
print(f"  √Variance: {np.sqrt(variance):.4f} (same as std dev)")

print(f"\nData 2: {speed2}")
print(f"  Variance:  {variance2:.4f}")
print(f"  Std Dev:   {std_dev2:.4f}")


# ============================================================
# 3. Step-by-step calculation
# ============================================================
print(f"\n{'='*50}")
print("STEP-BY-STEP CALCULATION")
print(f"{'='*50}")

data = [86, 87, 88, 86, 87, 85, 86]
mean = sum(data) / len(data)
print(f"Data: {data}")
print(f"Step 1 - Mean: {mean:.2f}")

# Step 2: Squared differences from mean
squared_diffs = [(x - mean) ** 2 for x in data]
print(f"Step 2 - Squared differences: {[f'{d:.2f}' for d in squared_diffs]}")

# Step 3: Variance (mean of squared differences)
variance_manual = sum(squared_diffs) / len(squared_diffs)
print(f"Step 3 - Variance: {variance_manual:.4f}")

# Step 4: Standard deviation (square root of variance)
std_manual = variance_manual ** 0.5
print(f"Step 4 - Std Dev:  {std_manual:.4f}")
print(f"NumPy result:      {np.std(data):.4f}")


# ============================================================
# 4. Population vs Sample Standard Deviation
# ============================================================
print(f"\n{'='*50}")
print("POPULATION vs SAMPLE STD DEV")
print(f"{'='*50}")

data = [4, 8, 6, 5, 3, 7, 9, 1]

# Population std dev: divide by N
pop_std = np.std(data)           # ddof=0 (default)

# Sample std dev: divide by N-1 (Bessel's correction)
sample_std = np.std(data, ddof=1)

print(f"Data: {data}")
print(f"Population std dev (÷N):   {pop_std:.4f}")
print(f"Sample std dev (÷N-1):     {sample_std:.4f}")
print("\nUse sample std dev when working with a SAMPLE of a larger population")
print("Use population std dev when you have ALL the data")


# ============================================================
# 5. The 68-95-99.7 Rule (Empirical Rule)
# ============================================================
print(f"\n{'='*50}")
print("THE 68-95-99.7 RULE (EMPIRICAL RULE)")
print(f"{'='*50}")

# For normally distributed data:
# ~68% of data falls within 1 std dev of the mean
# ~95% of data falls within 2 std devs of the mean
# ~99.7% of data falls within 3 std devs of the mean

np.random.seed(42)
normal_data = np.random.normal(loc=100, scale=15, size=10000)

mean_val = np.mean(normal_data)
std_val = np.std(normal_data)

within_1 = np.sum((normal_data >= mean_val - std_val) & 
                   (normal_data <= mean_val + std_val)) / len(normal_data)
within_2 = np.sum((normal_data >= mean_val - 2*std_val) & 
                   (normal_data <= mean_val + 2*std_val)) / len(normal_data)
within_3 = np.sum((normal_data >= mean_val - 3*std_val) & 
                   (normal_data <= mean_val + 3*std_val)) / len(normal_data)

print(f"Mean: {mean_val:.2f}, Std Dev: {std_val:.2f}")
print(f"Within 1σ: {within_1*100:.1f}% (expected ~68%)")
print(f"Within 2σ: {within_2*100:.1f}% (expected ~95%)")
print(f"Within 3σ: {within_3*100:.1f}% (expected ~99.7%)")


# ============================================================
# 6. Practical: Comparing consistency of two datasets
# ============================================================
print(f"\n{'='*50}")
print("PRACTICAL - Comparing Consistency")
print(f"{'='*50}")

# Two basketball players' scores per game
player_a = [22, 24, 20, 23, 21, 25, 22, 24, 23, 21]
player_b = [10, 35, 15, 30, 5, 40, 20, 28, 12, 35]

print(f"Player A scores: {player_a}")
print(f"  Mean: {np.mean(player_a):.1f}, Std Dev: {np.std(player_a):.2f}")

print(f"\nPlayer B scores: {player_b}")
print(f"  Mean: {np.mean(player_b):.1f}, Std Dev: {np.std(player_b):.2f}")

print("\nConclusion: Both have similar means, but Player A is MORE CONSISTENT")
print("(lower std dev), while Player B is MORE VARIABLE (higher std dev)")

print("\n--- Standard Deviation complete! ---")
