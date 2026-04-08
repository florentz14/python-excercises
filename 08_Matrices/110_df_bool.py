# -------------------------------------------------
# File Name: 110_df_bool.py
# Author: Florentino Báez
# Date: 08_Matrices
# Description: Pandas DataFrame from dict; boolean masks on columns (rows).
# See also: 78_bool_ix.py
# -------------------------------------------------

import pandas as pd

data = {
    "color": ["blue", "green", "yellow", "red", "white"],
    "object": ["ball", "pen", "pencil", "paper", "mug"],
    "price": [1.2, 1.0, 0.6, 0.9, 1.7],
}
data_colors = pd.DataFrame(data)
print("data_colors:\n", data_colors)
print("\nRows with price > 1:\n", data_colors[data_colors["price"] > 1])
