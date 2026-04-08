# -------------------------------------------------
# File Name: 51_convert_index_to_column.py
# Author: Florentino Báez
# Date: 12/03/2026
# Description: Converts the index of a DataFrame to a column.
# -------------------------------------------------

# Import pandas and numpy libraries
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).parent.parent / "data" / "exam_attempts.csv"
df = pd.read_csv(csv_path)

# Reset the index to convert it to a column
df = df.reset_index()
print("After converting index in a column:")
print(df)
