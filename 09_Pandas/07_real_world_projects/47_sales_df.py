# -------------------------------------------------
# File Name: 93_sales_dataframe.py
# Author: Florentino Báez
# Date: Pandas
# Description: DataFrame Month, Sales, Expenses.
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [30500, 35600, 28300, 33900],
    "Expenses": [22000, 23400, 18100, 20700],
})

print("Exercise 4: Sales and Expenses DataFrame")
print("-" * 40)
print(df)
