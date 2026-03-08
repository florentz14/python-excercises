# -------------------------------------------------
# File Name: 38_stratified_sampling.py
# Description: Builds a proportional stratified sample by combining samples from each stratum.
# -------------------------------------------------

import numpy as np

np.random.seed(42)
# Strata: age groups with different sizes
stratum_a = np.random.normal(50, 10, 100)   # young
stratum_b = np.random.normal(70, 12, 200)   # middle
stratum_c = np.random.normal(80, 15, 150)   # elderly

# Proportional stratified sample (e.g. 10% from each)
n_a = int(0.1 * 100)
n_b = int(0.1 * 200)
n_c = int(0.1 * 150)
sample_a = np.random.choice(stratum_a, n_a, replace=False)
sample_b = np.random.choice(stratum_b, n_b, replace=False)
sample_c = np.random.choice(stratum_c, n_c, replace=False)

stratified_sample = np.concatenate([sample_a, sample_b, sample_c])
print("=== STRATIFIED SAMPLING ===")
print(f"Strata sizes: 100, 200, 150 (total 450)")
print(f"Sample from each: {n_a}, {n_b}, {n_c} (proportional)")
print(f"Combined sample mean: {np.mean(stratified_sample):.2f}")
