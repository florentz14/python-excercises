# -------------------------------------------------
# File Name: 40_sampling_bias.py
# Description: Shows how biased sampling distorts estimates compared with simple random sampling.
# -------------------------------------------------

import numpy as np

# Population (truth)
np.random.seed(42)
population = np.concatenate([
    np.random.normal(50, 10, 800),   # majority
    np.random.normal(90, 5, 200),    # minority, different mean
])

# Biased sample: oversampling the "easier to reach" group (high values)
# e.g. voluntary response, convenience sampling
biased_sample = np.random.choice(population[population > 70], 100)

# Unbiased: simple random sample
unbiased_sample = np.random.choice(population, 100, replace=False)

print("=== SAMPLING BIAS ===")
print("Population mean:", np.mean(population))
print()
print("Biased sample (e.g. voluntary, convenience):")
print("  mean:", np.mean(biased_sample))
print("  overestimates if high values easier to reach")
print()
print("Unbiased (simple random):")
print("  mean:", np.mean(unbiased_sample))
print()
print("Common biases: selection, non-response, survivorship.")
