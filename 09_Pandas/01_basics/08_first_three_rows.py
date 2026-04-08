# -------------------------------------------------
# File Name: 08_first_three_rows.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Select the first three rows of a DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

# print the DataFrame
print("First three rows of the data frame:")
print(df.head(3))
