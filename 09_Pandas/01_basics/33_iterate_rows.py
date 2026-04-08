# -------------------------------------------------
# File Name: 33_iterate_rows.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Iterating over the rows of a DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_iterate_rows = pd.read_csv(csv_path)[["name", "score"]].head(3)

# iterate over the rows of the DataFrame
for _, row in df_iterate_rows.iterrows():
    # print the name and score of the row
    print(f"Name: {row['name']}, Score: {row['score']}")
