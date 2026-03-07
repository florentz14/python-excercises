# -------------------------------------------------
# File Name: 09f_bars_stacked.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Stacked bar chart.
# -------------------------------------------------

import matplotlib.pyplot as plt

# =========================================================================
# Stacked bar chart
# =========================================================================

labels = ["Q1", "Q2", "Q3", "Q4"]
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 25, 28, 30]

plt.figure(figsize=(7, 5))
plt.bar(labels, product_a, label="Product A", color="#FF6B6B")
plt.bar(labels, product_b, bottom=product_a, label="Product B", color="#4ECDC4")  # bottom= stacks this bar on top of product_a
plt.bar(labels, product_c,
        bottom=[a + b for a, b in zip(product_a, product_b)],  # Stack C on top of A+B by calculating cumulative heights
        label="Product C", color="#45B7D1")

plt.title("Stacked Bar Chart")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.legend()
plt.show()
