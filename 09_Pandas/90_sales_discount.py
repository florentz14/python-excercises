# -------------------------------------------------
# File Name: 90_sales_discount.py
# Author: Florentino Báez
# Date: Pandas
# Description: Sales by year with 10% discount.
# -------------------------------------------------

import pandas as pd

print("Exercise 1: Sales with 10% discount")
print("-" * 50)

start_year = int(input("Start year: "))
end_year = int(input("End year: "))

sales = {}
for year in range(start_year, end_year + 1):
    v = float(input(f"Sales {year}: "))
    sales[year] = v

s = pd.Series(sales)
s_discount = s * 0.9

print("\nOriginal series (indexed by year):")
print(s)
print("\nSeries with 10% discount:")
print(s_discount)
