# -------------------------------------------------
# File Name: 09e_bars_grouped.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Grouped Bar Chart — comparing three
#              products across quarters.
# -------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

labels = ["Q1", "Q2", "Q3", "Q4"]
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 25, 28, 30]

x_pos = np.arange(len(labels))  # Numeric positions [0, 1, 2, 3] used to offset grouped bars
width = 0.25  # Each bar group gets 0.25 width so three groups fit side by side

plt.figure(figsize=(8, 5))
# Offset to the left by 'width' for the first product group
plt.bar(x_pos - width, product_a, width, label="Product A", color="#FF6B6B")
plt.bar(x_pos, product_b, width, label="Product B", color="#4ECDC4")
plt.bar(x_pos + width, product_c, width, label="Product C", color="#45B7D1")

plt.xticks(x_pos, labels)
plt.title("Quarterly Sales by Product")
plt.xlabel("Quarter")
plt.ylabel("Sales (thousands)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()
