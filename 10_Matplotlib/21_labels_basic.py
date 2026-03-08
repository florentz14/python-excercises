# -------------------------------------------------
# File Name: 21_labels_basic.py
# Author: Florentino Báez
# Date: 10_Matplotlib
# Description: Basic title, xlabel, ylabel.
# -------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 5, 4, 6, 8]

# =========================================================================
# Basic labels and title
# =========================================================================

plt.figure(figsize=(7, 5))  # Create a 7x5 inch figure for the basic labels demo
plt.plot(x, y, "b-o")

plt.title("Monthly Sales Report")     # Title
plt.xlabel("Month")                    # X-axis label
plt.ylabel("Sales (thousands)")        # Y-axis label

plt.show()
