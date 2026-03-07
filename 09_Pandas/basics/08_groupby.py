# ------------------------------------------------------------
# Basic case: Group and aggregate
# ------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "category": ["A", "A", "B", "B", "A"],
    "sales": [100, 150, 80, 120, 200],
    "units": [5, 6, 4, 5, 8],
})

# Mean per category
print("Mean sales per category:\n", df.groupby("category")["sales"].mean())

# Multiple aggregations
print("\nSum and mean per category:\n", df.groupby("category").agg({"sales": ["sum", "mean"], "units": "sum"}))

# agg with dict per column
print("\nSales=sum, Units=mean:\n", df.groupby("category").agg({"sales": "sum", "units": "mean"}))
