# -------------------------------------------------
# File Name: 20_city_wise_count.py
# Author: Florentino Báez
# Date: 09_Pandas
# Description: Pandas exercise: 28 city wise count.
# -------------------------------------------------

"""Practice 28: City Wise Count."""
import pandas as pd

# Sample dataset: city and name of person
data = {
    "city": [
        "California",
        "Georgia",
        "Los Angeles",
        "California",
        "Georgia",
        "Los Angeles",
        "California",
        "California",
        "Los Angeles",
        "Los Angeles",
    ],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"],
}
df_practice_28 = pd.DataFrame(data)
result = df_practice_28.groupby("city", as_index=False).agg(
    **{"Number of people": ("name", "size")}
)
print(result)
