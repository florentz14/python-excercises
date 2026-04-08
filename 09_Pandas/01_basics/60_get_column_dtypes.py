# -------------------------------------------------
# File Name: 60_get_column_dtypes.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Gets the data types of the columns in a DataFrame.
# -------------------------------------------------

# import libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)
df.index = list("abcdefghij")

# print the data types of the columns
print("Data types of the columns of the said DataFrame:")
print(df.dtypes)
