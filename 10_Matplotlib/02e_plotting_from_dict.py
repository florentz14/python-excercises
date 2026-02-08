# -------------------------------------------------
# File Name: 02e_plotting_from_dict.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Plotting from a dictionary (data= parameter).
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Plotting from a dictionary
# =========================================================================

data = {"day": [1, 2, 3, 4, 5, 6, 7],
        "temperature": [72, 75, 71, 78, 82, 79, 85]}

plt.figure(figsize=(6, 4))
plt.plot("day", "temperature", data=data, marker="o", color="tomato")  # When data= is given, strings refer to dict keys
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (F)")
plt.grid(True, alpha=0.3)
plt.show()
