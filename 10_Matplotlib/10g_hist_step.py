# -------------------------------------------------
# File Name: 10g_hist_step.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Step Histogram — outline and filled
#              step histogram styles.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Fix seed so the random data is the same every time
np.random.seed(42)
# Normal distribution: mean=170 cm, std=10 cm, 250 samples
data = np.random.normal(loc=170, scale=10, size=250)

plt.figure(figsize=(7, 5))
# "step" draws only the outline without filling the bars
plt.hist(data, bins=20, histtype="step", color="darkblue", linewidth=2)
# "stepfilled" draws filled area under the step outline
plt.hist(data, bins=20, histtype="stepfilled", color="skyblue", alpha=0.3)
plt.title("Step Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

print("\n--- Histogram Summary ---")
print("plt.hist(data, bins=N)           -> Basic histogram")
print("density=True                     -> Normalize (area=1)")
print("cumulative=True                  -> Cumulative histogram")
print("orientation='horizontal'         -> Horizontal bars")
print("histtype='step'                  -> Unfilled outline")
print("alpha=0.5                        -> Transparency for overlapping")
