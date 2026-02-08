"""
Machine Learning - Normal Data Distribution
=============================================
The Normal (Gaussian) distribution is the most important distribution in ML.
It forms a bell-shaped curve, symmetric around the mean.

Key properties:
- Mean, Median, and Mode are all at the center
- Symmetric around the mean
- Defined by two parameters: mean (μ) and standard deviation (σ)
- 68-95-99.7 rule applies

The formula (probability density function):
  f(x) = (1 / (σ√(2π))) * e^(-(x-μ)²/(2σ²))
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ============================================================
# 1. Generating Normal Distribution Data
# ============================================================
np.random.seed(42)

# Generate 1000 random values with mean=170, std=10
# (like human heights in cm)
heights = np.random.normal(170, 10, 1000)

print("Normal Distribution: Human Heights (cm)")
print(f"  Mean:   {np.mean(heights):.2f}")
print(f"  Median: {np.median(heights):.2f}")
print(f"  Std:    {np.std(heights):.2f}")
print(f"  Min:    {np.min(heights):.2f}")
print(f"  Max:    {np.max(heights):.2f}")


# ============================================================
# 2. Visualizing the Bell Curve
# ============================================================
plt.figure(figsize=(10, 5))

# Histogram of the data
plt.hist(heights, bins=50, density=True, alpha=0.6, color="steelblue",
         edgecolor="white", label="Data histogram")

# Overlay the theoretical PDF (bell curve)
x = np.linspace(130, 210, 200)
pdf = stats.norm.pdf(x, loc=170, scale=10)
plt.plot(x, pdf, "r-", linewidth=2, label="Normal PDF (μ=170, σ=10)")

plt.title("Normal Distribution - Human Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Probability Density")
plt.legend()
plt.tight_layout()
plt.show()


# ============================================================
# 3. The 68-95-99.7 Rule Visualized
# ============================================================
print(f"\n{'='*50}")
print("68-95-99.7 RULE")
print(f"{'='*50}")

mean, std = 170, 10

within_1 = np.sum((heights >= mean - std) & (heights <= mean + std))
within_2 = np.sum((heights >= mean - 2*std) & (heights <= mean + 2*std))
within_3 = np.sum((heights >= mean - 3*std) & (heights <= mean + 3*std))

print(f"Within 1σ ({mean-std}-{mean+std} cm): {within_1/len(heights)*100:.1f}% (expected ~68%)")
print(f"Within 2σ ({mean-2*std}-{mean+2*std} cm): {within_2/len(heights)*100:.1f}% (expected ~95%)")
print(f"Within 3σ ({mean-3*std}-{mean+3*std} cm): {within_3/len(heights)*100:.1f}% (expected ~99.7%)")

# Visualization with shaded regions
fig, ax = plt.subplots(figsize=(10, 5))
x = np.linspace(130, 210, 300)
y = stats.norm.pdf(x, mean, std)

ax.plot(x, y, "k-", linewidth=2)
ax.fill_between(x, y, where=(x >= mean - 3*std) & (x <= mean + 3*std),
                alpha=0.15, color="green", label="99.7% (3σ)")
ax.fill_between(x, y, where=(x >= mean - 2*std) & (x <= mean + 2*std),
                alpha=0.2, color="blue", label="95% (2σ)")
ax.fill_between(x, y, where=(x >= mean - std) & (x <= mean + std),
                alpha=0.3, color="red", label="68% (1σ)")

ax.set_title("68-95-99.7 Rule")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Probability Density")
ax.legend()
plt.tight_layout()
plt.show()


# ============================================================
# 4. Z-Score: How far is a value from the mean?
# ============================================================
print(f"\n{'='*50}")
print("Z-SCORE")
print(f"{'='*50}")

# Z = (X - μ) / σ
# A Z-score tells how many standard deviations a value is from the mean

test_heights = [150, 160, 170, 180, 190, 200]

print(f"Mean: {mean}, Std: {std}")
print(f"\n{'Height':>8s} | {'Z-score':>8s} | Interpretation")
print("-" * 50)
for h in test_heights:
    z = (h - mean) / std
    if abs(z) < 1:
        interp = "common"
    elif abs(z) < 2:
        interp = "uncommon"
    elif abs(z) < 3:
        interp = "rare"
    else:
        interp = "very rare (outlier)"
    print(f"{h:>8d} | {z:>8.2f} | {interp}")


# ============================================================
# 5. Testing for Normality
# ============================================================
print(f"\n{'='*50}")
print("TESTING FOR NORMALITY")
print(f"{'='*50}")

# Shapiro-Wilk test: tests if data is normally distributed
# H0: Data is normally distributed
# If p-value > 0.05, we FAIL to reject H0 (data is likely normal)

normal_sample = np.random.normal(0, 1, 500)
uniform_sample = np.random.uniform(0, 1, 500)

stat_n, p_n = stats.shapiro(normal_sample[:200])
stat_u, p_u = stats.shapiro(uniform_sample[:200])

print(f"Normal data  -> Shapiro p-value: {p_n:.4f} {'✓ Normal' if p_n > 0.05 else '✗ Not normal'}")
print(f"Uniform data -> Shapiro p-value: {p_u:.6f} {'✓ Normal' if p_u > 0.05 else '✗ Not normal'}")


# ============================================================
# 6. Comparing Normal Distributions
# ============================================================
print(f"\n{'='*50}")
print("COMPARING DISTRIBUTIONS")
print(f"{'='*50}")

plt.figure(figsize=(10, 5))

# Different means, same std
for mu in [160, 170, 180]:
    x = np.linspace(130, 220, 200)
    y = stats.norm.pdf(x, mu, 10)
    plt.plot(x, y, linewidth=2, label=f"μ={mu}, σ=10")

plt.title("Same Std Dev, Different Means")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()

# Same mean, different std
plt.figure(figsize=(10, 5))

for sigma in [5, 10, 20]:
    x = np.linspace(100, 240, 200)
    y = stats.norm.pdf(x, 170, sigma)
    plt.plot(x, y, linewidth=2, label=f"μ=170, σ={sigma}")

plt.title("Same Mean, Different Std Devs")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()

print("\n--- Normal Data Distribution complete! ---")
