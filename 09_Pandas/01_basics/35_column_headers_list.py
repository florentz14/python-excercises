# -------------------------------------------------
# File Name: 35_column_headers_list.py
# Author: Florentino Báez
# Date: 3/11/2026
# Description: Getting a list of column headers from a DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df_column_headers_list = pd.read_csv(csv_path)
df_column_headers_list.index = list("abcdefghij")

print(df_column_headers_list.columns.tolist())
# print the list of column headers
print(f"List of column headers: {df_column_headers_list.columns.tolist()}")