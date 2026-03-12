# -------------------------------------------------
# File Name: 111_pivot_vs_pivot_table.py
# Description: Pivot vs pivot_table
# -------------------------------------------------

import pandas as pd

df = pd.DataFrame({"date": ["2024-01", "2024-01", "2024-02"], "product": ["A", "B", "A"], "sales": [100, 150, 120]})
print("pivot_table (handles duplicates with aggfunc):")
print(df.pivot_table(index="date", columns="product", values="sales", aggfunc="sum"))
