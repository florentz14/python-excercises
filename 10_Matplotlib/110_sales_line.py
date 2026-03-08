# -------------------------------------------------
# File Name: 110_sales_line.py
# Author: Florentino Báez
# Date: Matplotlib
# Description: Line chart of sales evolution by year (user input).
# -------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

print("Exercise 1: Sales evolution line chart")
print("-" * 50)

start_year = int(input("Start year: "))
end_year = int(input("End year: "))

sales = {}
for year in range(start_year, end_year + 1):
    v = float(input(f"Sales {year}: "))
    sales[year] = v

s = pd.Series(sales)
plt.figure(figsize=(8, 5))
plt.plot(s.index, s.values, marker="o", linewidth=2, markersize=8)
plt.title("Sales Evolution", fontsize=14, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
